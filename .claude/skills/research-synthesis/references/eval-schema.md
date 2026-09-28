# `planted-flaws.json` schema

This skill ships no demo data. To use `scripts/eval_tags.py` — to self-check the skill's tagging and theme-building against known-correct answers, e.g. before relying on it for real studies, or as a regression test after editing the skill — build a small synthetic transcript set with deliberately planted flaws, and an answer key in this shape describing where they are:

```json
{
  "leading_question_excerpts": [
    "T3-L42"
  ],
  "off_topic_excerpts": [
    "T1-L10"
  ],
  "hypothetical_mislabeled_as_behavior": [
    "T2-L88"
  ],
  "single_participant_pseudo_themes": [
    {
      "claimed_theme": "users abandon the form after the third field",
      "excerpt_ids": ["T4-L12", "T4-L30", "T4-L55"]
    }
  ]
}
```

## What each key represents, and what "caught" means

| Key | What it plants | What "caught" means in `excerpts.jsonl` / `themes.md` |
|---|---|---|
| `leading_question_excerpts` | An excerpt written as the answer to a moderator question that supplies the expected answer. | The excerpt's `leading_question_flag` is `true`. |
| `off_topic_excerpts` | An excerpt that's venting or unrelated to the brief, easy to mistake for on-topic. | The excerpt's `relevance` is `off_topic`. |
| `hypothetical_mislabeled_as_behavior` | An excerpt phrased as future/hypothetical intent ("I'd probably just call the bank"), written to tempt a careless tagger into `observed_behavior`. | The excerpt's `evidence_type` is `hypothetical_intent` (not `observed_behavior`). |
| `single_participant_pseudo_themes` | Several excerpts from **one** participant, worded differently enough to look like a multi-person pattern if excerpt count were mistaken for participant count. | `themes.md` contains **no** theme whose `Support:` ID set is (a superset of) this list while claiming a participant count greater than 1 — i.e. the skill correctly refused to call it a theme. |

Each planted excerpt should live in a real synthetic source file under whatever `--input-dir` you point `split_excerpts.py` at, so the full pipeline (split → tag → theme) runs against it end to end — the eval script checks the skill's actual output files, not the answer key in isolation.

## Running the eval

```
python scripts/eval_tags.py --excerpts excerpts.jsonl --themes themes.md --answer-key /demo-data/answer-key/planted-flaws.json
```

Prints, per category: how many planted flaws were caught vs. missed, with IDs, plus (for the flag/tag categories) any excerpts the skill flagged that aren't in the answer key at all — worth a look, since that's either a second real flaw the demo data happened to contain, or a false positive in the tagging. Exits non-zero if anything was missed, so it can gate a "did I break this skill" check after edits.
