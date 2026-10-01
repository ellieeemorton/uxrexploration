# Bias Review — CFPB Servicer Complaint Themes

Run after verification (`verification-findings.md`) and before writing `report.md`, per `references/bias-review.md`.

## 1. Leading questions

**Checked, found nothing — structurally guaranteed, not just checked this run.** All 128 excerpts have `leading_question_flag: false`. This data type has no moderator (unprompted written complaints), so a leading-question dependency is not possible here, unlike the Oceanside interview study. No theme's existence depends on a leading question.

## 2. Dominant voices

**Checked, found nothing requiring a change.** Every `Support:`/`Counter-evidence:` list in `themes.md` was built by deliberately citing at most one excerpt ID per distinct participant (even where a participant had 2-3 tagged excerpts, e.g. C27, C55, C84, C97) — so no single participant's excerpt count inflates a theme's apparent weight within its own support list. Checked every list in the file for an accidental duplicate `participant_id`: none found.

Separately checked whether one participant's *specific wording* dominates a theme's description rather than just its count: the non-responsiveness theme (29 of 99) draws its five illustrative quotes from five different participants (C3, C18, C65, C87, C91) using varied phrasing ("form acknowledgment letters," "no meaningful response," "dead air," "to no avail," "generic placeholder") — no single participant's framing was repeated back as if representative of the group.

## 3. Vivid one-off quotes

**Checked, one soft note, no change made.** C65's "dead air" and C92's multi-hour hold time are the most quotable lines used as illustrations in the non-responsiveness theme — both are somewhat more vivid than the plainer, more administrative language most of the other 27 supporting excerpts use (e.g. C3's "has not provided any substantive response," C31's "did not receive a response to these inquiries"). Neither is an outlier in *content* (both describe exactly the pattern the theme claims — no response despite effort), only mildly more colorful in *phrasing*. No participant's unusually dramatic language (e.g. C34's "I AM FURIOUS," not quoted in any theme) was used to anchor a theme's headline claim. No change needed.

## 4. Confirmation of hypotheses / research questions

This is an exploratory, self-authored brief with no stakeholder hypotheses to confirm (`brief.md` states this explicitly) — so the usual risk ("every hypothesis confirmed, nothing complicates them") doesn't directly apply. The closer analogue here is whether the findings came out suspiciously tidy relative to the three self-authored research questions, which would itself suggest motivated tagging:

- **RQ2 (does the sub-issue label match a narrow or wide range of complaints?)** — the findings are **not** uniformly one answer: "Trouble with how payments are being handled" and "Keep getting calls" came out narrow and well-matched to their labels; "Don't agree with the fees charged" and "Received bad information about your loan" came out loose umbrella categories whose dominant content differs from (or is much broader than) what the label implies. A tidy, motivated analysis would have been more likely to find all seven categories equally coherent (or equally incoherent) rather than a genuine split.
- **RQ3 (does content relate to outcome)** — the finding is deliberately not a clean story: timeliness tracks company (MOHELA) more strongly than content category in aggregate, but content category still predicts timeliness *within* MOHELA specifically (see `report.md`). This is a more complicated, caveated answer than "yes, content predicts outcome" — which is itself a mild signal against cherry-picking a tidy result.

**Adjacent/off-topic excerpts re-checked for waved-off disconfirming signal:** only one excerpt in the whole dataset is tagged `adjacent` (C32... correction, **C33-L1**: "my prior physician was doing an evaluation... confirmed with me that [program] scammed me with my education") and zero are `off_topic`. C33 was not silently dropped — it's explicitly listed in the "fees charged" stratum's counter-evidence/genuine-mix group in `themes.md`. No disconfirming signal was found hiding in excluded excerpts, because there were essentially none excluded to check.

## Fragility note carried into the report

Two within-stratum themes are numerically fragile and should be flagged as such in `report.md`, not presented with the same confidence as the more robust ones:
- **"Fees charged" theme** — support (7 of 13) and counter-evidence (6 of 13) are separated by exactly one narrative. A different reasonable coder re-reading the same 13 narratives could plausibly classify 1-2 of them differently and flip which side is larger. The underlying observation (fee complaints are dominated by interest/capitalization language, not discrete fee line-items) is still well-supported by the 7 clear cases, but the "about half" framing (rather than "most") already reflects this fragility — the report should not round this up further.
- **"Received bad information" contradiction theme** — at 6 of 18 (just above this stratum's threshold of 4), this is the thinnest theme in the file. It should be labeled accordingly in the evidence-strength grading, not presented as being on equal footing with the 10-13-of-18/99 themes.

No theme's *existence* (whether it clears its threshold at all) changed as a result of this review — only wording/confidence framing, which is reflected above and will carry into `report.md`.
