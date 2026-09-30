# Bias review — Oceanside Repayment Plan Comparison Study

Run after verification (see `verification-findings.md`), before writing the report. Working through the four checks in `references/bias-review.md`.

## 1. Leading questions

Of the 14 excerpts flagged `leading_question_flag: true` during tagging, four ended up cited in a theme's Support or Counter-evidence bracket. Checked each:

- **Theme 3 (H2, density) — T5-L84.** Already the theme's central subject, not a hidden dependency: the theme is explicitly *about* this being a leading-induced response, and Support would drop from "a couple (2 of 9)" to "one (1 of 9)" without it. No further action — this is as transparent as it can be.
- **Theme 4 (abandonment) — T2-L36.** The preceding question ("Was that because the tool was hard to use?") supplied a specific premise, but P2's answer *rejects* it ("No, cause of the numbers") and substitutes his own reason. A participant contradicting the leading frame is more credible, not less — this doesn't weaken the theme. No change needed.
- **Theme 5 (stated-vs-observed contradiction) — T3-L96 and T9-L58, both.** This is the one worth flagging clearly: two of this theme's four supporting instances (P3 and P9) are self-reports of "ease" that were themselves elicited by leading questions ("You found that pretty easily then, yeah?" / "So the table's easy to use then?"). Removing both would drop Support from "some (4 of 9)" to "a couple (2 of 9)" (P4 and P7 only). The leading-question dependency doesn't invalidate the theme — if anything it strengthens the underlying point (leading questions produce especially unreliable self-reports, and both participants undercut their own leading-prompted answer in the same breath) — but half the theme's support carries this dependency, which belongs in the report's evidence-strength grading, not just this file. **Carry into step 6:** grade this theme Moderate, not Strong, and say why in the finding itself.
- **Theme 8 (H3, want assumptions disclosed) — T5-L158, cited as Counter-evidence.** The preceding leading question ("Does that bother you?") invited a "yes"; P5 said "Not really." A resistant answer to a leading counter-question is, if anything, more credible counter-evidence, not less. No change needed.

The other ten leading-flagged excerpts (T1-L107, T2-L68a, T2-L88a, T2-L102, T2-L128, T3-L126, T3-L176, T5-L106, T6-L70) never entered a theme's bracket list — most were explicitly excluded during theme-building (e.g. T2-L68a, excluded by name from the monthly-first theme) or simply weren't selected as representative. No action needed on these.

## 2. Dominant voices

Checked raw excerpt share per participant across all on-topic/adjacent excerpts (not just what's quoted in themes.md):

| Participant | On/adjacent excerpts | Share |
|---|---|---|
| P3 | 49 | 16.5% |
| P5 | 39 | 13.1% |
| P1 | 33 | 11.1% |
| P4 | 32 | 10.8% |
| P7 | 32 | 10.8% |
| P6 | 31 | 10.4% |
| P2 | 29 | 9.8% |
| P8 | 28 | 9.4% |
| P9 | 24 | 8.1% |

**P3 has the highest raw excerpt share, not P4** — this is a function of her transcript's structure (many short back-and-forth exchanges with the moderator, a product of her low-confidence, deferential style generating more turns, not more *content*). Checked whether she disproportionately shapes any single theme's wording: she's cited in seven themes, but always as one of several representative quotes alongside other participants' — no theme's framing rests mainly on her phrasing specifically.

**P4's dominance concern is different in kind, already handled structurally, not a new finding here:** he restates one position (hide/reorder the monthly payment) roughly a dozen times within his own transcript. This is repetition of a single claim, not raw chattiness — the participant-count rule (count distinct `participant_id`, never excerpt count) already prevents this from inflating any theme's support, and it's called out explicitly in Individual Observations. Nothing further to do here beyond confirming the rule held (it did — P4 is never counted more than once in any Support/Counter-evidence bracket).

## 3. Vivid one-off quotes

Checked which representative quotes are notably more vivid/dramatic than the rest of their theme's support, since a memorable image can make a thin finding feel more established than it is:

- **P9's "Which chair you want on the Titanic" (T9-L26, abandonment theme).** This is the one to flag most: it's the most quotable line in the whole dataset, sitting inside a theme that is "some (4 of 9)," entirely self-reported, and — per the finding above — has at least one member (P6) whose fit is genuinely partial. A report drafted around this line risks implying the abandonment pattern is more dramatic or more universal than four self-reported, differently-motivated accounts support. **Carry into step 6:** if this quote is used in the report, pair it explicitly with the fraction and the note that reasons varied across participants — don't let it stand alone as the theme's voice.
- **P4's "it hypnotizes" (T4-L56) and P2's "a guess wearing a tie" (T2-L84b).** Both vivid, but sit inside themes with broad support (nearly all, 8/9; most, 6/9) — low risk of the color overstating the breadth, since the breadth is already there independent of the quote.
- **P8's "menu where the prices change" (T8-L44).** Already handled correctly in the current draft: explicitly kept out of both Support and Counter-evidence for the H2 theme and discussed as a mixed, uncounted case rather than let the vivid image imply either a density complaint or a clean "fine" rating.

## 4. Confirmation of the brief's hypotheses

The brief's three hypotheses, checked against the actual theme set:

- **H1** (monthly scanned first, little attention to total) — **partially confirmed, partially complicated.** Monthly-first scanning holds for most (7/9). "Little attention to total" does not hold — nearly all (8/9) substantively engage with total or payoff date.
- **H2** (table density causes disengagement) — **not supported.** At most 2 of 9 said anything resembling a density complaint, and real abandonment (4/9) is attributed to other causes by most of those who report it.
- **H3** (distrust is about missing explanation, not wrong numbers) — **mostly confirmed (6/9), with an explicit complication** for one participant whose distrust is rooted in a past, unrelated betrayal (undisclosed interest capitalization by a previous servicer) rather than this tool's explanatory content.

This is not a case of the data cleanly confirming everything the brief expected — two of three hypotheses are substantially complicated or disconfirmed, and the one that mostly holds (H3) is explicitly qualified. Per the checklist, a too-clean confirmation is the trigger for re-checking adjacent/off-topic excerpts for suppressed disconfirming signal; that trigger isn't met here, so no additional re-scan was required — but a quick pass through the off-topic excerpts (mostly venting about loan terms and interest rates, P2 and P9) turned up nothing that reads as an on-topic finding misfiled as venting.

## Summary of changes carried forward to the report (step 6)

1. Theme 5 (stated-vs-observed contradiction): grade Moderate, not Strong — half its support is self-report elicited by a leading question, even though the participants' own words undercut the leading premise.
2. If quoting P9's "Titanic" line in the report, keep it paired with the fraction and the note that the four abandonment accounts had different stated causes — don't let it imply a bigger or more uniform pattern than it is.
3. No theme's existence, count, or word-band changes as a result of this review — the four leading-question dependencies found were either already the theme's explicit subject, resisted by the participant, or don't change which side of the threshold the theme falls on.
