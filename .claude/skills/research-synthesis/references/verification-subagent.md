# Verification subagent

After themes are built, spawn a fresh-context subagent (via the Agent tool) to check the themes before you show them to anyone. Give it **only** `themes.md` and `excerpts.jsonl` — not the research brief, not this conversation, not the source transcripts.

**Why fresh context and only those two files:** the agent that wrote the themes has a motivated reason to believe its own claims — it selected the quotes, so it's primed to see them as supportive. A subagent that never saw the brief has no hypothesis to confirm and no memory of "why" a theme was written a certain way; it can only check what's in front of it. Withholding the brief specifically prevents it from grading themes against "does this sound like a plausible finding" instead of "does the cited evidence actually say this."

## Exact brief to give the subagent

Use substantially this prompt when spawning it:

> You are verifying a qualitative research synthesis. You have not seen the research brief, the source transcripts, or any prior conversation about this project — verify strictly from the two files attached: `themes.md` and `excerpts.jsonl`. Do not trust the theme author's framing; re-derive everything from the data.
>
> For every theme in `themes.md`, check:
> 1. **Quote fidelity** — does every quoted string attributed to an excerpt ID appear verbatim (exact substring, whitespace differences aside) in that ID's `text` field in `excerpts.jsonl`?
> 2. **Quote relevance** — does the quote actually support the specific claim the theme is making, or is it merely on-topic/related without backing the stated claim?
> 3. **Participant count** — recompute the number of distinct `participant_id` values behind the theme's cited `Support:` excerpt IDs, and confirm it matches the stated count and word (e.g. "most (6 of 8)").
> 4. **Behavioral language check** — if the theme uses language like "users do X" / "participants X," confirm at least one cited excerpt has `evidence_type: observed_behavior`. If all cited excerpts are `stated_attitude` or `hypothetical_intent`, this is a failure — the claim is overstated for its evidence.
>
> Report one PASS or FAIL per check per theme, with specifics (which ID, what's wrong). Do not soften a finding to be diplomatic — a failed check is a failed check, state it plainly.

## What to do with the findings

Every FAIL must be resolved before moving to bias review — either fix the theme (correct the count, swap in a real supporting quote, reword the claim to match the evidence it actually has) or, if you disagree with a finding, write down why in `verification-findings.md` rather than silently overriding it. A finding that's dismissed without a written reason is indistinguishable, on the next read-through, from a finding nobody looked at.

Write the final resolved list — original finding, what you changed (or why you didn't) — to `verification-findings.md`. This file is part of the deliverable, not scratch work: it's the audit trail that lets the researcher (or anyone reviewing the synthesis later) see that verification happened and what it caught.
