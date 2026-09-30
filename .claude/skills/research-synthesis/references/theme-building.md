# Building themes

Themes are built only from `on_topic` and `adjacent` excerpts (`evidence-tagging.md`). Every theme must state, in a structured line the scripts can parse, its participant support and its counter-evidence. Free-form prose around that line is fine and expected — the structured line is what makes the claim checkable by a script instead of by re-reading.

## The rule this whole file exists to enforce

**A theme's participant count is the number of distinct `participant_id` values behind its supporting excerpt IDs — never the number of excerpt IDs.** One participant who says the same thing five different ways across a transcript is n=1. This is the direct fix for "one participant's volume creates a theme": volume (excerpt count) simply isn't the number being measured.

## Minimum bar to be called a theme

A pattern qualifies as a **theme** only if both hold:
- at least 2 distinct participants, **and**
- at least 20% of the total participant pool that produced on-topic/adjacent excerpts for this question (`N`)

As a formula: `threshold = max(2, ceil(0.20 × N))`.

Patterns that don't clear this bar are still written up — just not as themes. Report them separately:
- **Individual observation** — exactly 1 participant, however many excerpts.
- **Isolated pattern** — 2+ participants, but below 20% of N (only possible once N is large enough that 20% > 2, e.g. N=15+).

Nothing observed gets silently dropped for being small; it's labeled honestly instead of inflated.

**Why 20%, and why the max(2, …) floor:** at small sample sizes typical of qualitative studies (N=5–10), 20% rounds up to 2 anyway, so the floor and the percentage agree — you're never asking for more than "it wasn't just one person." At larger N (a big diary study, N=40), 20% raises the bar to 8 people, which is the right direction: with more data points on the table, a handful of matching quotes is more likely to be coincidence, and a theme claim should need more than a constant headcount to earn "most" or "many" language. A single fixed number (e.g., "always 3+") would either be too strict for a study of 5 or too loose for a study of 40; a fixed floor alone (2+) is exactly the volume-inflation failure mode this process is meant to prevent.

## Qual-quant wording lexicon

Use these words — and only these words — when describing how many participants support a theme or a piece of counter-evidence, and always pair the word with the exact fraction. The word alone is never sufficient; band edges are inherently fuzzy, and "most (6 of 8)" lets the reader judge the number for themselves instead of trusting your adjective.

| n as % of N | Word |
|---|---|
| 100% | all |
| ≥ 85% and < 100% | nearly all |
| ≥ 65% and < 85% | most |
| ≥ 55% and < 65% | more than half |
| ≥ 45% and < 55% | about half |
| ≥ 25% and < 45% | some / a few |
| exactly 2 participants, < 25% of N | a couple |
| 1 participant | one *(not a theme — individual observation)* |

This generalizes a fixed-N convention (e.g., "n=6 of 8 → most") to any sample size by working in percentages instead of raw counts, so the same words mean the same thing whether N is 5 or 50.

## Counter-evidence is mandatory, never glossed

Every theme states its counter-evidence explicitly, even if it's a single participant — "one participant (1 of 8) pushed back: [T7-L14]" is a complete and correct counter-evidence line. Never write "some participants disagreed" without naming exactly who and citing the ID; vague counter-evidence is functionally the same as omitting it.

If a theme genuinely has zero counter-evidence, say so explicitly ("no counter-evidence observed") rather than leaving the line out — an absent line reads as "not checked," not as "checked and found none."

## Required structured format in `themes.md`

Each theme is a heading followed by a `Support:` line and a `Counter-evidence:` line in exactly this shape (the verification subagent, `verify_quotes.py`, and `eval_tags.py` all parse these lines):

```
## Theme: <short theme name>

<one or two sentences describing the pattern>

Support: most (6 of 8) — [T1-L12, T2-L40, T3-L8, T4-L21, T5-L5, T6-L33]
Counter-evidence: one (1 of 8) — [T7-L14]

> “representative verbatim quote” (T1-L12)
> “another representative verbatim quote” (T4-L21)
```

- The bracketed ID list after `Support:` / `Counter-evidence:` must contain every excerpt ID being counted — this is what lets a script recompute the distinct-participant count and check it against the stated word/fraction. Every ID mentioned in prose as supporting or countering a theme belongs in that list too — a script can't see an ID you only wrote in a sentence.
- Quotes are written as `“exact text” (ID)` with **curly** outer quotes — this exact citation format is required in `report.md` too (see `report-template.md`) because `verify_quotes.py` parses it with a fixed pattern, and source text often contains its own straight-quoted dialogue or tooltip text that a straight-quote delimiter would collide with. Never trim a quote with an ellipsis — quote the exact full substring or don't quote it.
