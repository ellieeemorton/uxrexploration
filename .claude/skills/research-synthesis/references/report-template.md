# Report structure

`report.md` is the only artifact most stakeholders will read — it has to carry the evidence discipline of the earlier steps without requiring the reader to go dig through `excerpts.jsonl` themselves. Structure:

1. **The decision this informs** — one line, quoting or closely paraphrasing the brief. Everything below should be answerable back to this line; if a finding doesn't connect to it, it probably belongs in "what this data cannot tell us," not in implications.
2. **Executive summary** — 3–5 bullets, each tagged with its evidence-strength label (below). This is the only section some readers will get to; it must not imply more certainty than the findings section does.
3. **Findings** — one subsection per theme (structured format below).
4. **Individual and isolated observations** — patterns that didn't clear the theme threshold (`theme-building.md`), kept visible and explicitly labeled as not a theme, not silently omitted.
5. **What this data cannot tell us** — explicit, not a throwaway line. Cover: evidence-type gaps (e.g., "no observed behavior was collected for the onboarding flow, only self-report"), sample limits on generalizability, anything a stakeholder might expect this study to cover that it doesn't (ruled off-topic, or never asked), and anything a leading question makes unreliable enough to caveat.
6. **Implications** — each one explicitly references which finding(s) it follows from and ties back to the decision in section 1. Not generic UX recommendations — if an implication would be the same regardless of what this data showed, it doesn't belong here.

## Evidence-strength rubric

Label every theme in the findings section with exactly one of these. Do not round up.

| Label | Criteria |
|---|---|
| **Strong** | ≥ 65% of N (i.e. "most" or higher on the lexicon), includes at least one `observed_behavior` excerpt among its support, no unresolved leading-question dependency (bias review), and any counter-evidence has been weighed and doesn't undercut the pattern. |
| **Moderate** | Clears the theme threshold, but is missing at least one of Strong's conditions — e.g. support is entirely `stated_attitude`/`self_reported_past_behavior` with no observed behavior, or falls in the 25–64% bands, or has counter-evidence worth real caveat. |
| **Thin** | Barely clears the theme threshold (just above `max(2, 20% of N)`), relies mainly on `hypothetical_intent` language, or depends on a leading-question-flagged excerpt for a meaningful share of its support. State this plainly in the finding itself — "this theme is thin: N=3 of 15, entirely stated intent, no observed behavior" — not just in a label. |

## Required citation format (parsed by `scripts/verify_quotes.py`)

Every verbatim quote in the report, in every section, is written with **curly quotes** as the outer delimiter:

```
“exact quote text” (ID)
```

— exactly matching how quotes are cited in `themes.md` (`theme-building.md`). Use curly quotes (“ ”), not straight ones, even though it looks like a typographic nicety: source text routinely contains its own straight-quoted dialogue or tooltip text (a moderator note reading `Says "I assumed it would sort."`, a tooltip reading `"Includes projected interest"`), and a straight-quote delimiter would terminate at that first embedded quote instead of the citation's real end — `verify_quotes.py` would silently fail to check the rest, or match the wrong span. Never truncate a quote with an ellipsis to fit it in a sentence — the substring has to be exact, so quote the full span or don't quote it at all. Do not paraphrase and then add an ID as if it were a citation of a verbatim quote; if you're paraphrasing, don't put it in quotation marks.

Every stated participant count is written as:

```
Support: most (6 of 8) — [T1-L12, T2-L40, T3-L8, T4-L21, T5-L5, T6-L33]
```

on its own line, exactly as in `themes.md` — carry the same `Support:` / `Counter-evidence:` lines from `themes.md` into the corresponding finding in `report.md` rather than re-describing the count in prose. This is what lets the verification script re-check the report itself, not just the intermediate `themes.md`, catching any drift introduced while writing up the findings.

## Before showing the draft

Run:

```
python scripts/verify_quotes.py --report report.md --excerpts excerpts.jsonl --sources <sources-dir>
```

It must exit clean. Any mismatch it reports is a bug in the report (a misquote, a wrong ID, a miscounted `Support:` line) — fix it and rerun before the checkpoint, don't present a draft you know fails this check.
