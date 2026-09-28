# Bias review

Run after verification passes, before writing the report. This step exists because verification (`verification-subagent.md`) checks whether themes are *accurate to the cited evidence* — it can't catch whether the evidence itself was selected or worded in a way that's misleading even when every individual check passes. Bias review is the layer that asks "accurate to what, exactly, and is that a fair picture?"

Write findings to `bias-review.md` — even "checked, found nothing" per item, so a reader can see the check happened rather than was skipped.

## 1. Leading questions

List every excerpt with `leading_question_flag: true` that ended up cited in a theme's `Support:` or `Counter-evidence:` line. For each:
- Would removing it drop the theme's participant count below the threshold in `theme-building.md`? If yes, the theme's existence depends on a leading-question answer — say so explicitly in the report rather than presenting the theme as if it were unconditionally supported.
- If the theme survives without it, no change needed, but the report should still note the leading-question answer wasn't load-bearing.

## 2. Dominant voices

For each theme, check whether one participant supplies a disproportionate share of the theme's excerpts relative to their share of all on-topic/adjacent excerpts in the whole study. The participant-count rule already prevents one voice from *creating* a theme alone, but it doesn't prevent one voice from *shaping the wording* of a theme that's otherwise legitimately multi-participant — e.g., a theme technically at "most (6 of 8)" whose description is really just one person's framing repeated back. Reword toward the pattern as a whole if you find this.

## 3. Vivid one-off quotes

Check whether the theme's headline wording was pulled from the most memorable or dramatic quote available, rather than the most representative one. A vivid quote is fine to *include* — it can be the best illustration — but the theme's core claim shouldn't be shaped by how quotable one participant happened to be. If the vivid quote is an outlier in tone or intensity relative to the theme's other supporting excerpts, say that in the theme's write-up rather than letting the quote imply the whole group felt that strongly.

## 4. Confirmation of the brief's hypotheses

List the brief's hypotheses. Check the theme set against them:
- Does every hypothesis get confirmed, with no theme contradicting or complicating any of them, and no theme outside what the brief expected? That pattern is itself worth flagging — real qualitative data is rarely this tidy, and a perfect match is more often a sign that tagging leaned toward the expected answer than that the hypotheses were exactly right.
- If you flag this, go back and specifically re-check the `adjacent` and `off_topic` excerpts (excluded from theme-building, but not deleted) for anything that complicates the tidy story — a disconfirming signal that got waved off as "not quite on-topic" during tagging is the most likely place it would hide.

Note anything from this review that changes a theme's evidence-strength label, wording, or whether it should be reported as a theme at all — carry that change into `report.md` (`report-template.md`), don't just leave it in `bias-review.md`.
