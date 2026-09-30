#!/usr/bin/env python3
"""Deterministically check a synthesis document against its sources. No LLM judgment.

This is the mechanical half of verification (the semantic half -- does the
quote actually support the claim -- is the fresh-context subagent's job, see
references/verification-subagent.md). This script only checks things that
have a single correct answer:

  1. Every `“quoted string” (ID)` in the document is a real excerpt ID, and
     the quoted text is a verbatim (whitespace-normalized) substring of that
     excerpt's recorded text in excerpts.jsonl. The outer delimiter is the
     curly quote pair “...” (U+201C/U+201D), not straight quotes --
     source text often contains its own straight-quoted dialogue or tooltip
     text (e.g. Says "I assumed it would sort."), and a straight-quote
     delimiter would terminate at the first embedded quote instead of the
     real end.
  2. That excerpt's recorded text is itself actually found in the original
     source file at/near the line or row it claims -- this catches drift
     introduced while building excerpts.jsonl, not just drift introduced
     while writing the document.
  3. Every `Support: <word> (n of N) -- [ID, ID, ...]` (and `Counter-evidence:`)
     line's stated participant count matches the number of *distinct*
     participant_id values behind the listed excerpt IDs.

Expected excerpts.jsonl record shape (one JSON object per line):
  {
    "id": "T3-L42", "participant_id": "T3", "source_file": "T3.txt",
    "line": 42, "row": null, "text": "...",
    "evidence_type": "...", "relevance": "...",
    "leading_question_flag": false, "preceding_question": null
  }

Exits 0 if everything checks out, 1 if anything failed.
"""
import argparse
import json
import re
import sys
from pathlib import Path

QUOTE_RE = re.compile(r'“([^”]+)”\s*\(([A-Za-z0-9_.\-]+)\)')
SUPPORT_RE = re.compile(
    r'(Support|Counter-evidence):\s*([^(]*)\((\d+)\s+of\s+(\d+)\)\s*[—\-]+\s*\[([^\]]*)\]',
    re.IGNORECASE,
)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_excerpts(path: Path):
    excerpts = {}
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"error: {path}:{line_no}: invalid JSON ({e})", file=sys.stderr)
                sys.exit(2)
            excerpts[record["id"]] = record
    return excerpts


def check_quotes(doc_text: str, excerpts: dict, sources_dir: Path):
    failures = []
    checked = 0
    for match in QUOTE_RE.finditer(doc_text):
        quote, excerpt_id = match.group(1), match.group(2)
        checked += 1
        record = excerpts.get(excerpt_id)
        if record is None:
            failures.append(f'unknown excerpt id "{excerpt_id}" cited for quote: "{quote}"')
            continue

        if normalize(quote) not in normalize(record.get("text", "")):
            failures.append(
                f'{excerpt_id}: quoted text does not match excerpts.jsonl.\n'
                f'    quoted in doc: "{quote}"\n'
                f'    excerpts.jsonl text: "{record.get("text", "")}"'
            )
            continue

        source_ok, reason = verify_against_source(record, sources_dir)
        if not source_ok:
            failures.append(f"{excerpt_id}: {reason}")
    return checked, failures


def verify_against_source(record: dict, sources_dir: Path):
    source_file = record.get("source_file")
    if not source_file:
        return False, "excerpts.jsonl record has no source_file field"
    source_path = sources_dir / source_file
    if not source_path.exists():
        return False, f"source file {source_file} not found under {sources_dir}"

    text = normalize(record.get("text", ""))
    if record.get("row") is not None:
        # Tabular: exact cell match expected.
        import csv
        delimiter = "\t" if source_path.suffix.lower() == ".tsv" else ","
        with source_path.open(newline="", encoding="utf-8", errors="replace") as f:
            rows = list(csv.reader(f, delimiter=delimiter))
        row_idx = record["row"] - 1  # rows are 1-indexed including header
        col_idx = record.get("column_index")
        if row_idx >= len(rows) or col_idx is None or col_idx >= len(rows[row_idx]):
            return False, f"row {record['row']} / column {col_idx} out of range in {source_file}"
        cell = normalize(rows[row_idx][col_idx])
        if text not in cell and cell not in text:
            return False, f"excerpt text not found at row {record['row']} of {source_file}"
        return True, ""
    else:
        # Transcript: substring search in a window starting at the claimed line.
        lines = source_path.read_text(encoding="utf-8", errors="replace").splitlines()
        line_no = record.get("line")
        if line_no is None or line_no < 1 or line_no > len(lines):
            return False, f"line {line_no} out of range in {source_file}"
        window = normalize(" ".join(lines[line_no - 1: line_no + 9]))  # excerpt may span lines
        if text not in window:
            return False, f"excerpt text not found near line {line_no} of {source_file}"
        return True, ""


def check_support_lines(doc_text: str, excerpts: dict):
    failures = []
    checked = 0
    for match in SUPPORT_RE.finditer(doc_text):
        label, _word, n_str, _big_n, id_list = match.groups()
        checked += 1
        ids = [i.strip() for i in id_list.split(",") if i.strip()]
        stated_n = int(n_str)
        participants = set()
        missing = []
        for excerpt_id in ids:
            record = excerpts.get(excerpt_id)
            if record is None:
                missing.append(excerpt_id)
                continue
            participants.add(record.get("participant_id"))
        if missing:
            failures.append(f'{label}: unknown excerpt id(s) {missing}')
            continue
        if len(participants) != stated_n:
            failures.append(
                f'{label} line claims n={stated_n} but the {len(ids)} cited excerpt IDs '
                f'resolve to {len(participants)} distinct participants: {sorted(participants)}'
            )
    return checked, failures


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", required=True, type=Path, help="report.md or themes.md to check")
    parser.add_argument("--excerpts", required=True, type=Path, help="excerpts.jsonl")
    parser.add_argument("--sources", required=True, type=Path, help="original source directory")
    args = parser.parse_args()

    excerpts = load_excerpts(args.excerpts)
    doc_text = args.report.read_text(encoding="utf-8")

    quotes_checked, quote_failures = check_quotes(doc_text, excerpts, args.sources)
    support_checked, support_failures = check_support_lines(doc_text, excerpts)

    print(f"Checked {quotes_checked} quoted citation(s), {support_checked} Support/Counter-evidence line(s).")

    all_failures = quote_failures + support_failures
    if not all_failures:
        print("OK: no mismatches found.")
        return 0

    print(f"\n{len(all_failures)} FAILURE(S):\n")
    for i, failure in enumerate(all_failures, start=1):
        print(f"{i}. {failure}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
