#!/usr/bin/env python3
"""Score the skill's tagging/theming against a hand-authored answer key of planted flaws.

This is a regression test for the skill itself, not part of a normal run:
build a small synthetic source set with known flaws planted in it (see
references/eval-schema.md for the planted-flaws.json schema and what each
category means), run the skill's normal workflow over it to produce
excerpts.jsonl and themes.md, then run this script to see what the tagging
caught and what it missed.

Exits 0 if every planted flaw was caught, 1 otherwise.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SUPPORT_RE = re.compile(
    r'Support:\s*[^(]*\((\d+)\s+of\s+(\d+)\)\s*[—\-]+\s*\[([^\]]*)\]',
    re.IGNORECASE,
)


def load_excerpts(path: Path):
    excerpts = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                record = json.loads(line)
                excerpts[record["id"]] = record
    return excerpts


def load_theme_supports(path: Path):
    """Returns a list of (stated_n, id_set) for every Support: line in themes.md."""
    text = path.read_text(encoding="utf-8")
    supports = []
    for match in SUPPORT_RE.finditer(text):
        stated_n = int(match.group(1))
        ids = frozenset(i.strip() for i in match.group(3).split(",") if i.strip())
        supports.append((stated_n, ids))
    return supports


def score_flag(excerpts, planted_ids, field, expected_value, all_ids_with_value=None):
    caught, missed = [], []
    for excerpt_id in planted_ids:
        record = excerpts.get(excerpt_id)
        if record is None:
            missed.append((excerpt_id, "excerpt id not found in excerpts.jsonl"))
        elif record.get(field) == expected_value:
            caught.append(excerpt_id)
        else:
            missed.append((excerpt_id, f'{field}={record.get(field)!r}, expected {expected_value!r}'))

    false_positives = []
    if all_ids_with_value is not None:
        planted_set = set(planted_ids)
        false_positives = sorted(all_ids_with_value - planted_set)

    return caught, missed, false_positives


def score_pseudo_themes(excerpts, theme_supports, pseudo_themes):
    caught, missed = [], []
    for entry in pseudo_themes:
        claimed = entry["claimed_theme"]
        pseudo_ids = frozenset(entry["excerpt_ids"])
        true_participants = {excerpts[i]["participant_id"] for i in pseudo_ids if i in excerpts}

        accepted_as_theme = False
        for stated_n, theme_ids in theme_supports:
            if pseudo_ids <= theme_ids and stated_n > 1:
                accepted_as_theme = True
                break

        if accepted_as_theme:
            missed.append(f'"{claimed}" was accepted as a theme with n>1, '
                           f'but its excerpts resolve to {len(true_participants)} participant(s): {sorted(true_participants)}')
        else:
            caught.append(claimed)
    return caught, missed


def print_section(title, caught, missed, false_positives=None):
    print(f"\n== {title} ==")
    print(f"caught: {len(caught)}  missed: {len(missed)}"
          + (f"  false positives: {len(false_positives)}" if false_positives else ""))
    for item in missed:
        if isinstance(item, tuple):
            print(f"  MISSED  {item[0]}: {item[1]}")
        else:
            print(f"  MISSED  {item}")
    if false_positives:
        for fp in false_positives:
            print(f"  FALSE POSITIVE  {fp}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--excerpts", required=True, type=Path)
    parser.add_argument("--themes", required=True, type=Path)
    parser.add_argument("--answer-key", required=True, type=Path)
    args = parser.parse_args()

    if not args.answer_key.exists():
        print(
            f"error: answer key not found at {args.answer_key}.\n"
            f"This skill ships no demo data -- build your own synthetic set and answer key "
            f"per references/eval-schema.md before running this script.",
            file=sys.stderr,
        )
        return 2

    excerpts = load_excerpts(args.excerpts)
    theme_supports = load_theme_supports(args.themes)
    answer_key = json.loads(args.answer_key.read_text(encoding="utf-8"))

    total_missed = 0

    leading_ids = set(answer_key.get("leading_question_excerpts", []))
    all_flagged_leading = {i for i, r in excerpts.items() if r.get("leading_question_flag") is True}
    caught, missed, fps = score_flag(excerpts, leading_ids, "leading_question_flag", True, all_flagged_leading)
    print_section("Leading questions", caught, missed, fps)
    total_missed += len(missed)

    off_topic_ids = set(answer_key.get("off_topic_excerpts", []))
    all_off_topic = {i for i, r in excerpts.items() if r.get("relevance") == "off_topic"}
    caught, missed, fps = score_flag(excerpts, off_topic_ids, "relevance", "off_topic", all_off_topic)
    print_section("Off-topic excerpts", caught, missed, fps)
    total_missed += len(missed)

    hypo_ids = set(answer_key.get("hypothetical_mislabeled_as_behavior", []))
    caught, missed, _ = score_flag(excerpts, hypo_ids, "evidence_type", "hypothetical_intent")
    print_section("Hypothetical/intent mislabeled as behavior", caught, missed)
    total_missed += len(missed)

    pseudo_themes = answer_key.get("single_participant_pseudo_themes", [])
    caught, missed = score_pseudo_themes(excerpts, theme_supports, pseudo_themes)
    print_section("Single-participant pseudo-themes correctly rejected", caught, missed)
    total_missed += len(missed)

    print(f"\n{'PASS' if total_missed == 0 else 'FAIL'}: {total_missed} planted flaw(s) missed overall.")
    return 0 if total_missed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
