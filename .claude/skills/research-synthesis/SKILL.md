---
name: research-synthesis
description: Synthesizes qualitative UX research data (interview transcripts, open-ended survey/diary responses) into an evidence-graded findings report, under a human researcher's direction. Trigger when asked to analyze, code, tag, theme, or synthesize qualitative research against a research brief, or to check/verify an existing qualitative synthesis for hallucinated quotes or unsupported claims. Never invents quotes or participant counts, stops at two mandatory human checkpoints, runs a fresh-context verification subagent, and runs a bias review before any report is called final.
---

# Research Synthesis

Synthesizes qualitative data (transcripts, open-ended responses) against a research brief, staying traceable to source and honest about evidence strength. You are assisting a human researcher, not replacing their judgment — the checkpoints below are mandatory stops, not formalities.

## Standing rules (apply throughout, every step)
- Every claim cites excerpt IDs. Never write a quote, count, or "users do X" claim you can't point to an ID for.
- Never invent a quote or tidy up its wording. If you aren't sure of the exact wording, don't quote it — paraphrase and say so.
- If evidence for something is thin, write "thin." Don't round up to sound more confident than the data supports.
- A theme's participant count is never "2+ people." It scales with sample size and is always written as `word (n of N)` — see `references/theme-building.md`. Count *distinct participants*, not excerpts — one talkative participant with ten quotes is still n=1.

## Workflow

1. **Intake.** Read the brief (questions, hypotheses, the decision it informs) and restate the decision in one line so you stay calibrated on what matters. Run `scripts/split_excerpts.py` over the source folder — it deterministically line/row-numbers every source file and writes a manifest, so excerpt IDs stay stable and later verifiable. Then use your own judgment to draw excerpt boundaries (a excerpt is one complete thought/turn/answer, not a fixed number of lines) and assign IDs per `references/id-schemes.md`. Write every excerpt — on-topic, adjacent, and off-topic alike — to `excerpts.jsonl`; nothing gets discarded at this stage.

2. **Tag.** Tag every excerpt's evidence type and relevance, and flag leading-question-adjacent excerpts, per `references/evidence-tagging.md`.
   **CHECKPOINT — stop and wait.** Show the tag distribution (counts by evidence type × relevance) and 10 sample excerpts spanning different tags. Do not start step 3 until the researcher approves or corrects the tagging.

3. **Build themes.** Using only on-topic and adjacent excerpts, build themes per `references/theme-building.md`: each theme lists its supporting excerpt IDs, a participant count in `word (n of N)` form, and counter-evidence (even a single dissenter, named explicitly). Patterns that don't clear the theme threshold are kept visible as individual/isolated observations, not silently dropped. Write to `themes.md` using the structured `Support:` / `Counter-evidence:` line format the reference file specifies — the verification and eval scripts parse it.

4. **Verify.** Spawn a subagent per `references/verification-subagent.md`, giving it only `themes.md` and `excerpts.jsonl` — no brief, no prior conversation. It has no reason to defend your work and no context to be talked out of a finding. Fix or explicitly downgrade every finding it returns before moving on; write the resolved findings to `verification-findings.md`.

5. **Bias review.** Work through `references/bias-review.md` (leading questions, dominant voices, vivid one-off quotes, confirmation of the brief's hypotheses). Note anything that changes a theme's wording, strength label, or existence in `bias-review.md`.

6. **Report.** Write `report.md` per `references/report-template.md`: findings labeled by evidence strength, an explicit "what this data cannot tell us" section, and implications tied directly to the decision named in the brief — not generic recommendations.
   Run `python scripts/verify_quotes.py --report report.md --excerpts excerpts.jsonl --sources <source-dir>`. It must report zero mismatches before you show the draft; fix any failure and rerun.
   **CHECKPOINT — stop and wait.** Show the draft report and the verification script's output together. Do not say the synthesis is finished until the researcher approves.

## Outputs
Keep everything for one run together, e.g. `synthesis/<study-name>/`: `excerpts.jsonl`, `themes.md`, `verification-findings.md`, `bias-review.md`, `report.md`.

## Scripts
- `scripts/split_excerpts.py --input-dir <sources> --output-dir <numbered-dir>` — deterministic line/row numbering + manifest (step 1). Never hand-number sources yourself; the script's numbering is what later verification trusts.
- `scripts/verify_quotes.py --report report.md --excerpts excerpts.jsonl --sources <sources-dir>` — deterministic, no LLM judgment: re-opens the actual source files and checks every quoted string is a verbatim substring at the cited location, and that every participant count is arithmetically correct. Gate step 6 on this passing.
- `scripts/eval_tags.py --excerpts excerpts.jsonl --themes themes.md --answer-key <path>/planted-flaws.json` — scores your tagging/theming against a hand-authored answer key of deliberately planted flaws, and prints what was caught vs. missed. No answer key ships with this skill; schema is in `references/eval-schema.md` — build your own demo set to use it.

## Reference files
- `references/id-schemes.md` — excerpt ID formats by source type
- `references/evidence-tagging.md` — evidence-type and relevance taxonomy, leading-question flag
- `references/theme-building.md` — participant-count threshold and the qual-quant wording lexicon
- `references/verification-subagent.md` — exact subagent brief and checks
- `references/bias-review.md` — bias checklist
- `references/report-template.md` — report structure and evidence-strength rubric
- `references/eval-schema.md` — `planted-flaws.json` schema for `eval_tags.py`
