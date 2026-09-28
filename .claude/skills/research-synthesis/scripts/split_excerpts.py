#!/usr/bin/env python3
"""Deterministically number source files so excerpt IDs are stable and verifiable.

This script does NOT decide excerpt boundaries -- that's a judgment call the
skill's workflow makes (an excerpt is "one complete thought," not a fixed
number of lines). What it does is remove every chance of the ID scheme itself
being ambiguous or hand-typed inconsistently:

  - assigns T1, T2, ... to transcript-like files in stable (sorted) order
  - writes a line-numbered rendering of each transcript, so citing "L42"
    always means the same physical line in the original file
  - for tabular (CSV) sources, enumerates every non-empty open-ended cell as
    a candidate excerpt with its R{row}-Q{question} id already computed,
    since a spreadsheet row IS the natural excerpt unit (no further
    judgment needed there)

Output layout under --output-dir:
  manifest.json         -- list of {source_id, filename, type, ...}
  T1.numbered.txt, ...  -- one per transcript file, each line prefixed "L{n}: "
  rows.json             -- one entry per non-empty cell, for all CSV sources combined

See references/id-schemes.md for the ID formats and the reasoning behind them.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

TRANSCRIPT_EXTS = {".txt", ".md", ".vtt", ".srt", ".log"}
TABULAR_EXTS = {".csv", ".tsv"}
IDENTIFIER_COLUMN_NAMES = {"id", "respondent", "respondent_id", "participant", "participant_id"}


def slugify(text: str, maxlen: int = 24) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip()).strip("-")
    return slug[:maxlen] if slug else "col"


def process_transcripts(files, output_dir: Path):
    manifest_entries = []
    for i, path in enumerate(sorted(files, key=lambda p: p.name), start=1):
        source_id = f"T{i}"
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        numbered_path = output_dir / f"{source_id}.numbered.txt"
        with numbered_path.open("w", encoding="utf-8") as out:
            for line_no, line in enumerate(lines, start=1):
                out.write(f"L{line_no}: {line}\n")
        manifest_entries.append({
            "source_id": source_id,
            "filename": path.name,
            "type": "transcript",
            "line_count": len(lines),
        })
        print(f"  {source_id} <- {path.name} ({len(lines)} lines) -> {numbered_path.name}")
    return manifest_entries


def process_tabular(files, output_dir: Path):
    manifest_entries = []
    all_rows = []
    for path in sorted(files, key=lambda p: p.name):
        delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
        with path.open(newline="", encoding="utf-8", errors="replace") as f:
            reader = csv.reader(f, delimiter=delimiter)
            rows = list(reader)
        if not rows:
            continue
        header = rows[0]
        columns = []
        for col in header:
            if col.strip().lower() in IDENTIFIER_COLUMN_NAMES:
                columns.append(None)  # metadata column, not a question
            else:
                columns.append(f"Q-{slugify(col)}")
        manifest_entries.append({
            "source_id": "R",
            "filename": path.name,
            "type": "tabular",
            "columns": [c for c in columns if c],
            "row_count": len(rows) - 1,
        })
        for row_idx, row in enumerate(rows[1:], start=2):  # row 1 is header
            participant_id = f"R{row_idx}"
            for col_idx, cell in enumerate(row):
                if col_idx >= len(columns) or columns[col_idx] is None:
                    continue
                text = cell.strip()
                if not text:
                    continue
                excerpt_id = f"{participant_id}-{columns[col_idx]}"
                all_rows.append({
                    "id": excerpt_id,
                    "participant_id": participant_id,
                    "source_file": path.name,
                    "row": row_idx,
                    "column_index": col_idx,
                    "column_header": header[col_idx],
                    "text": text,
                })
        print(f"  R <- {path.name} ({len(rows) - 1} respondent rows, {len(all_rows)} non-empty answers so far)")
    if all_rows:
        rows_path = output_dir / "rows.json"
        rows_path.write_text(json.dumps(all_rows, indent=2), encoding="utf-8")
        print(f"  wrote {rows_path.name} ({len(all_rows)} candidate excerpts)")
    return manifest_entries


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    if not args.input_dir.is_dir():
        print(f"error: --input-dir {args.input_dir} is not a directory", file=sys.stderr)
        return 1
    args.output_dir.mkdir(parents=True, exist_ok=True)

    files = [p for p in args.input_dir.iterdir() if p.is_file()]
    transcript_files = [p for p in files if p.suffix.lower() in TRANSCRIPT_EXTS]
    tabular_files = [p for p in files if p.suffix.lower() in TABULAR_EXTS]
    unhandled = [p for p in files if p not in transcript_files and p not in tabular_files]

    manifest = []
    if transcript_files:
        print(f"Transcripts ({len(transcript_files)}):")
        manifest += process_transcripts(transcript_files, args.output_dir)
    if tabular_files:
        print(f"Tabular sources ({len(tabular_files)}):")
        manifest += process_tabular(tabular_files, args.output_dir)

    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nWrote {manifest_path}")

    if unhandled:
        print(
            f"\nSkipped {len(unhandled)} file(s) with unsupported extensions "
            f"(.xlsx isn't supported natively -- export to .csv first): "
            + ", ".join(p.name for p in unhandled),
            file=sys.stderr,
        )
    if not manifest:
        print("warning: no source files were processed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
