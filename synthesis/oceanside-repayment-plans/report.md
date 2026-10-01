# Repayment Plan Comparison Tool — Research Findings

> **Note on the data:** Oceanside Loan Servicing, the comparison tool described, and all nine participants (P1–P9) are synthetic — built as demo data to test a qualitative-research-synthesis process, not findings from a real study on a real product. The methodology, evidence grading, and analysis below were produced exactly as they would be for real research, but nothing in this report should be read as describing an actual company, tool, or person.

## Background and hypotheses

Oceanside Loan Servicing has seen a rise in support tickets from borrowers calling in after using the online repayment plan comparison tool, asking questions the tool is supposed to answer. Going in, it wasn't clear whether this reflects a usability problem with the tool itself, a trust problem with the numbers it shows, or borrowers seeking reassurance regardless of how clear the tool is. This study tested three hypotheses, moderated sessions combining a think-aloud comparison task with follow-up questions about trust and decision-making. They're referenced by label throughout this report:

- **H1:** Borrowers scan for the monthly payment amount first and pay little attention to total interest paid over the life of the loan.
- **H2:** The comparison table's density (many plans, many columns) causes borrowers to disengage before reaching the plan that best fits their situation.
- **H3:** Borrowers distrust the numbers shown because the tool doesn't explain how they're calculated, not because the numbers themselves are wrong.

## The decision this informs

Whether to build a guided plan recommender or invest in improving the existing comparison table — and if the latter, whether the fix is simplification (H2), surfacing total interest more prominently (H1), or explanatory content about the numbers (H3). This also bears on the background question above: whether rising support-ticket volume reflects a usability problem with the tool, a trust problem with the numbers, or borrowers seeking reassurance regardless of clarity.

## Methodology and assumptions

Nine moderated sessions (P1–P9), each combining a think-aloud comparison task with follow-up interview questions. Every finding below is graded by evidence strength and cites the specific excerpts behind it (full excerpt-level data in `excerpts.jsonl`, theme construction in `themes.md`). A few judgment calls underlie the analysis and are flagged explicitly, by label, at the point they matter — they're collected here so a reader can weigh them upfront rather than discover them buried in a finding:

- **Assumption:** where an observer's note records cursor position or dwell time (no eye-tracking was used), it's treated as a proxy for visual attention, not a direct record of it. Flagged again at Finding 1, where it does real work.
- **Assumption:** live, present-tense narration during the task ("I look at X because...") is treated as observed behavior; conditional framing ("I'd look at X...") is treated as a stated intent, even when said while the participant is looking at the live page. This is a consistently-applied rule, not a fact the data forces, and it's a meaningful part of why one participant (P7) reads as a less reliable behavioral source throughout (see Finding 5 and "What this data cannot tell us").
- **Assumption:** the moderator's observer notes and transcript are taken as accurate, complete records of each session. A few sessions have noted gaps (an interruption, unlogged note-taking) — see "What this data cannot tell us."
- **Convention, not a finding:** the threshold for calling something a "theme" (at least 2 participants, scaled up for larger samples) and the words used for participant counts ("most," "some," "a couple") follow a fixed scale documented in `references/theme-building.md`. A different scale would relabel some findings without changing the underlying counts or quotes.
- **Assumption:** this sample of 9 is not a statistically representative sample of Oceanside's full borrower base. Findings describe what this sample showed, not confirmed prevalence across all borrowers — see "What this data cannot tell us."

## Executive summary

- **H2 (table density causes disengagement) is not supported.** At most 2 of 9 participants said anything resembling a density complaint, and the clearer one was about a *past*, different session, not today's table. *(Moderate — see Finding 3.)*
- **H1 is half right.** Monthly payment is usually scanned first (7 of 9, **Strong**), but "little attention to total interest" does not hold — nearly all participants (8 of 9, **Strong**) substantively engage with total cost or payoff date at some point.
- **H3 mostly holds:** borrowers want the assumptions behind "projected" figures disclosed, not just labeled (6 of 9, **Strong**) — but one participant's distrust is rooted in a past, unrelated servicing betrayal that no amount of in-tool explanation would resolve.
- **Two concrete, high-confidence usability bugs were found:** the payoff-date column header looks sortable but does nothing (2 of 9, directly observed, **Thin** by count but high-confidence by evidence quality), and the income estimator's below-the-fold placement causes several borrowers to miss it or briefly mistake its default figure for their own (5 of 9, **Moderate**).
- **A guided recommender draws real, specific skepticism rooted in perceived conflict of interest** (4 of 9, **Moderate**) — and even the participants open to one attach a transparency condition, which is itself the actionable signal for that half of the decision.
- **Self-report of any kind — ease, stated intent, recalled scanning order — cannot be taken at face value in this data:** for close to half the sample, some form of it was directly contradicted by the same participant's observed behavior or later statement (4 of 9, **Moderate**). Two of those four are ease/satisfaction claims specifically; the other two are a contradicted stated intent and a contradicted claim about scanning order — related but distinct say/do gaps, bundled here (see Finding 5).

## Findings

Each finding below carries its `Support:` / `Counter-evidence:` line unchanged from `themes.md`, so the underlying data is exactly what was tagged and theme-built, not re-described here.

### Finding 1 — Monthly payment is usually the first thing scanned in the comparison table
**Evidence strength: Strong.** 77.8% of participants, includes directly observed behavior, no leading-question dependency.

Support: most (7 of 9) — [T1-L53, T3-L102, T4-L48, T5-L90, T6-L142, T8-L60, T9-L118]
Counter-evidence: no clean counter-evidence observed — see caveats below

> “The monthly payment column, first. I'm just looking down it.” (T1-L53)
> “The monthly. Then how long. Then total, if I'm feeling brave.” (T6-L142)

The participant most vocally opposed to this pattern (see Individual Observations, P4) is nonetheless *counted in this finding's support*: his own cursor was observed resting on the monthly column for ~10 seconds before moving to total (T4-L48), in tension with his self-report that he always looks at date and total first, monthly last (T4-L60). **Assumption:** the session used no eye-tracking, so cursor position is a proxy for visual attention, not a direct record of it — a cursor can rest somewhere without the eyes being there, or vice versa. It's the most defensible proxy available in this data (an observer's contemporaneous note, not a recollection), and it's one of five directly-observed-behavior excerpts behind this finding, not the only one — but it is an inference, and is presented as one. P2's only relevant statement came immediately after a leading question and is excluded entirely, usable neither as support nor counter. P9's overall first look, before he ever reaches the table, is his account balance on the dashboard (T9-L114) — within the table itself, payment is still first.

### Finding 2 — Despite scanning monthly first, nearly all borrowers substantively engage with total cost and/or payoff date at some point
**Evidence strength: Strong.** 88.9% of participants, includes directly observed behavior, no counter-evidence.

Support: nearly all (8 of 9) — [T1-L57, T2-L64a, T3-L180, T4-L56, T5-L94, T6-L98, T8-L60, T9-L48, T9-L66b]
Counter-evidence: no counter-evidence observed; P7's account is entirely hypothetical (T7-L78) and unverified — excluded from both support and counter

> “I look at the total paid, because the lower payment is obviously going to cost more in the long run.” (T1-L57)
> “Standard says twenty-one. I owe nineteen. So it's two thousand in interest. And the income one says twenty-six. Five thousand more.” (T4-L56)
> “All of them have me paying way more than I borrowed. Lowest total's, let me look, forty-one. On twenty-one!” (T9-L66b)

**This directly complicates H1.** Engagement quality varies a lot in depth — P4 does detailed interest-cost arithmetic unprompted; P3's engagement is thin (“Um. A little. I saw there was dates.”, T3-L180) and she never spontaneously calculates a cost difference. But eight of nine participants demonstrably look past the monthly figure, most without being asked to. H1 is better read as "monthly is scanned first" than "total is ignored."

### Finding 3 (testing H2) — Table density gets almost no unprompted "overwhelming" reaction to today's table
**Evidence strength: Moderate.** The disconfirming side covers 77.8% of participants but rests entirely on stated attitude and self-report, no directly observed behavior — capped at Moderate by the evidence-strength rubric regardless of breadth.

Support: a couple (2 of 9) — [T5-L84, T6-L40a] — this is support for H2's proposed mechanism specifically (density itself causing disengagement)
Counter-evidence: most (7 of 9) — [T1-L111a, T2-L54, T3-L92, T4-L74, T6-L128b, T7-L52, T9-L54]

> “Yeah, kind of. I mean, yeah. There's a lot of columns.” (T5-L84) — following the leading question, "Wasn't that table confusing?"
> “Too many numbers.” (T6-L40a) — unprompted, but describing a *past* comparison attempt, not today's live table
> “Not really. I mean, the table's pretty clear. Four plans is a manageable number. If it was like ten I'd be lost.” (T1-L111a)
> “The payoff date. Cause that's what makes me mad. No, sorry, it's not the table. It's the situation. The table's fine. It says what it says.” (T9-L54)

Only two participants said anything resembling a density/overwhelm complaint. One (P5) was elicited by a leading question and explicitly walked back by the end of the same session (“I don't think so. The table's fine. I was just saying it was busy. It's not bad.”). The other (P6) was about a *different, past* comparison attempt — when he actually works through today's table, his only complaint is that the plan labels assume knowledge he doesn't have, not that there's too much on the page. **H2's specific mechanism — today's density causing today's disengagement — has no clean support in this data.**

### Finding 4 — Past abandonment of a plan comparison is reported by four participants, mostly for reasons other than density
**Evidence strength: Moderate.** 44.4% of participants; entirely self-reported (retrospective claims can't be directly observed, which structurally caps this at Moderate, not a flaw in how it was gathered).

Support: some (4 of 9) — [T2-L32, T2-L36, T5-L20, T5-L28, T6-L36, T6-L40a, T6-L40b, T9-L26]
Counter-evidence: no counter-evidence observed (self-reported history — there's no "didn't abandon" case to weigh against it)

> “No, cause of the numbers. You look at it and it's like oh you can pay less a month and only pay another twenty grand. Terrific.” (T2-L36)
> “I got overwhelmed I think. It was right after I started my job and there were forms and a new apartment lease and, yeah. I figured I'd come back. I didn't.” (T5-L28)
> “Once, a few years back. I was looking for anything. And I got to the end and thought this is just rearranging the same bad deal. Which chair you want on the Titanic.” (T9-L26)

Four participants describe quitting a past comparison before finishing, for different reasons: P2, the tradeoffs themselves; P5, overwhelm compounded by an unrelated stressful week (new job, new apartment); P9, a fatalistic conclusion that every option is equally bad. **P6 is a genuine partial exception:** he says "too many numbers" before mentioning a work interruption — that's hard to cleanly separate from a density complaint, even though it's about a past, possibly different version of the tool. Three of four attributions don't mention density at all; the fourth partially does.

### Finding 5 — Self-reports — of ease, of intent, of scanning order — are repeatedly contradicted by observed behavior
**Evidence strength: Moderate.** 44.4% of participants; half of this finding's support is a self-report elicited by a leading question (see `bias-review.md`), even though the participants' own words undercut the leading premise. **Note on scope (added on self-audit, see reply):** only P3 and P9 make actual ease/satisfaction claims that get contradicted; P4 and P7 are a different kind of say/do gap (stated scanning order and stated intent, not an ease rating). All four are real, verified contradictions, bundled here because they make one point — self-report of any kind is unreliable in this data — but this could reasonably be split into two "a couple (2 of 9)" findings instead. Left merged pending the researcher's preference.

Support: some (4 of 9) — [T3-L96, T4-L48, T7-L62, T7-L64, T9-L58]
Counter-evidence: no counter-evidence observed

> “Yeah, pretty easy. I guess.” (T3-L96) — said after 25 seconds of silent scrolling back and forth, then followed minutes later by a failed sort-header click and a validation error that she also downplayed: “It was fine. It just didn't like the comma.”
> “Yeah. Easy enough. I didn't really use it.” (T9-L58)

P3 shows the ease-claim pattern most extensively (see Individual Observations); P9 volunteers his own contradiction in the same breath. P4's stated *scanning order* contradicts his own cursor (Finding 1) — a claim about behavior, not satisfaction. P7 repeatedly states a firm *intent* (“I'd definitely use that, cause income-linked depends on what you make.”, T7-L62) that his own subsequent behavior doesn't follow — he never clicks the estimator field (T7-L64). **No kind of self-report can be taken at face value in this data** — for close to half the sample, some form of it (a satisfaction rating, a stated intent, a recollection of scanning order) was directly contradicted by what the same participant did or said minutes apart. This bears directly on the brief's background question: a support call framed as "the tool confused me" and a session where the same borrower rates the tool "easy" while visibly struggling with it are not necessarily in tension.

### Finding 6 — The payoff-date column header looks sortable but does nothing when clicked
**Evidence strength: Thin by count (barely clears the theme threshold), but directly observed and independently reproduced — treat as higher-confidence than the raw count suggests.**

Support: a couple (2 of 9) — [T3-L104, T3-L106, T4-L76]
Counter-evidence: no counter-evidence observed (no one else tested it)

> “clicks Payoff date header x2, nothing” (T3-L104), followed by “Oh it doesn't do anything.” (T3-L106)
> “Clicks Payoff date header. Nothing. Clicks again. Says "I assumed it would sort."” (T4-L76)

Only two participants tried this interaction — a thin count on its face — but both did so unprompted, expecting the same reasonable behavior, with no leading question involved, and both got the same (non-)result. This is a concrete, fixable interface bug, not a matter of interpretation.

### Finding 7 — The income estimator sits below the table and is easy to miss; several borrowers wouldn't use it unprompted, or briefly mistook its default number for their own
**Evidence strength: Moderate.** 55.6% of participants, mixed observed and self-reported evidence.

Support: more than half (5 of 9) — [T1-L103, T2-L106, T2-L118, T4-L128a, T5-L130, T5-L136, T6-L90]
Counter-evidence: a couple (2 of 9) — [T3-L118, T8-L90]

> “The income estimate thing. I mean, once I found it, it was fine, it worked. But it was below the table, and I almost didn't scroll down. If I hadn't been curious about where the number came from, I'd have just taken the first numbers as mine.” (T1-L103)
> “I didn't know what to expect, I never touch that. I never knew it was there, honestly. It's way down.” (T2-L118)
> “I don't know, it didn't say example. To me it looked like mine. Somebody could make a real bad call off that.” (T6-L94)

Two related patterns are bundled here: not using the estimator without being prompted, whether or not it was ever noticed (P2, P5), and discovering it late enough to have briefly taken the default income-linked figure at face value (P1, P4 near-miss; P2, P6 actually did so). P3 and P8 found and used it without difficulty; P9's non-use is a deliberate choice ("I know my income. I don't need a box.") rather than a discoverability failure.

### Finding 8 (testing H3) — Borrowers want the assumptions behind "projected" figures disclosed, not just labeled
**Evidence strength: Strong.** 66.7% of participants, includes directly observed behavior, no unresolved leading-question dependency, counter-evidence weighed.

Support: most (6 of 9) — [T1-L77, T2-L84b, T4-L70, T6-L82, T7-L86, T9-L74]
Counter-evidence: a couple (2 of 9) — [T3-L116, T5-L158]

> “And, hm, this little "i" thing, projected, projected on what. I'm self-employed, one year I make ninety, next year fifty-five, so when it says hundred forty for the Income one I'm like, based on WHAT. It doesn't say what income it's using. Last year? Average? And if they redo it every year then the total at the bottom is, it's made up. It's a guess wearing a tie. If it just said "this assumes you make X" I'd know how far to trust it. Right now, I don't.” (T2-L84b)
> “This. Income-Linked. A hundred ninety something. Almost half. But I don't see what it's based on. I'd want to know that.” (T6-L82)
> Counter: “It was fine. It says it includes interest.” (T3-L116); “Not really. Everything says that.” (T5-L158, said in direct response to a leading "Does that bother you?")

**Important complication for H3:** one supporting participant's distrust of "projected" (T9-L74) predates this tool and is rooted in a past experience of undisclosed interest capitalization by a *previous* servicer — no in-tool explanation would necessarily resolve it, because the injury is that a number changed on him before without warning, not that today's tooltip is unclear. H3 holds cleanly for most of this finding's support but not for that participant specifically.

### Finding 9 — Borrowers want the interest rate itself shown directly on the comparison page
**Evidence strength: Thin.** 22.2% of participants, right at the theme threshold — specific and directly actionable, but the smallest count in this report.

Support: a couple (2 of 9) — [T6-L134, T6-L138, T9-L78, T9-L84]
Counter-evidence: no counter-evidence observed

> “I wanted to see what the interest rate was. I think it's somewhere. I went to that documents thing first thinking it'd be there, then I just went to the plans.” (T6-L134), and afterward: “Yeah that was me looking for the rate. Didn't find it.” (T6-L138)
> “If they told me the rate. On this page. Next to the plans. It's not even on here. I'm looking. No, not here. It's the main thing! Why isn't it here.” (T9-L78)

One participant explicitly notes it wouldn't change his decision, "just feel honest" (T9-L84) — a transparency want, not a decision-changing one.

### Finding 10 — Trust in the table often rests on verifying one familiar number and extending that confidence to the rest
**Evidence strength: Moderate.** 33.3% of participants; entirely self-report/stated attitude, no directly observed behavior.

Support: some (3 of 9) — [T3-L220, T4-L96, T4-L100, T6-L102]
Counter-evidence: one (1 of 9) — [T1-L65]

> “I think so. They matched my standard one. So the others are probably right too.” (T3-L220)
> “The Standard within a couple dollars. Which is how I know to trust the rest. Though, the rest I can't check, so, you see the problem.” (T4-L100)
> Counter: “Mostly? I mean, for my current plan, yes, because I know roughly what I pay. For the income one I'm not sure how they're guessing my income.” (T1-L65) — this participant explicitly does *not* extend trust to a plan he hasn't personally verified

### Finding 11 — A guided plan recommender draws real skepticism specifically rooted in perceived conflict of interest
**Evidence strength: Moderate.** 44.4% of participants; entirely stated attitude, and reception is genuinely mixed (see counter-evidence).

Support: some (4 of 9) — [T1-L119, T2-L144, T6-L158a, T9-L134]
Counter-evidence: some (4 of 9) — [T3-L224, T5-L192, T7-L144, T8-L142]

> “A little. Not a lot. They're a servicer, they get paid either way. But I don't love the idea that a recommended plan would be, like, the one that keeps me paying longest.” (T1-L119)
> “Recommend what. They're all bad. You'd be recommending which bad one. If it said "refinance somewhere else" I'd use that. But they don't wanna lose the loan.” (T9-L134)
> Counter: “Yeah I'd love that. I'd definitely use it. A lot of people would. I'd want it to explain why though. I wouldn't trust a black box. I'd cross-check against the table.” (T7-L144)

Reception is genuinely mixed, not uniformly negative — but every positive response carries a transparency or relevance condition attached, which is itself the useful signal: any recommender needs to show its work and its scope, or it inherits the same distrust as an unexplained number.

### Finding 12 — Several borrowers explicitly separate the comparison tool from the loan terms as the real source of frustration
**Evidence strength: Moderate by count (33.3%), but each instance is spontaneous and specific rather than inferred, and it answers the brief's background question directly.**

Support: some (3 of 9) — [T2-L140b, T4-L26, T9-L54]
Counter-evidence: no counter-evidence observed

> “And look, I'm not gonna sit here and say the page is bad. The page is okay. It's a table. It's the loan that's bad. If you can pass that up the chain.” (T2-L140b)
> “The payoff date. Cause that's what makes me mad. No, sorry, it's not the table. It's the situation. The table's fine. It says what it says.” (T9-L54)

A third participant's variant targets the framing rather than the loan itself: “And I'll add, because people never say this, that the loan itself was fine. The rate was fine. It's that the whole structure trains you to ask the wrong question from the first letter they send.” (T4-L26)

## Individual and isolated observations (below theme threshold — not counted as findings, but not dropped)

- **P8 (n=1):** Needs a qualifying-payment-count / public-service-loan-forgiveness status tracker the tool doesn't provide anywhere: “the number you should really be watching is the qualifying payment count, and the tool never, it doesn't show you how many of those you've” (T8-L24). For her, total cost is structurally irrelevant: “"Includes projected interest." Fine. But total isn't what I care about. If I'm on the forgiveness track I don't pay it all so the column could say a million and it wouldn't tell me anything.” (T8-L72). She never noticed the existing "Forgiveness Programs" nav item. **This need falls outside all three hypotheses.**
- **P9 (n=1, a related but distinct shape):** Frames the income estimator, and by extension any recommender, as built for “people who have a choice. I don't have a choice. Lot of people don't.” (T9-L136) — a financial-constraint version of the same underlying gap (the tool assumes a decision-making latitude that doesn't apply to everyone).
- **P5 (n=1):** Trusts numbers by default authority — “It's their own tool so it should be right. I'd assume they did it properly.” (T5-L150) — a distinct mechanism from Finding 10's "verify one, extend to rest."
- **P7 (n=1, methodological caution):** Self-identified as an atypical, expert evaluator (“I'd probably judge this page harder than most people,” T7-L34) whose stated intentions repeatedly didn't match his session behavior (Finding 5). His individual claims should be weighted lightly as representative-user evidence, though his design critique may still be useful as expert-review-style input.
- **P4 (n=1, volume caution):** The single most vocal participant on hiding/reordering the monthly payment, with roughly a dozen restatements of the same position. Every one of those restatements is still one participant — he is never counted more than once in any finding above, regardless of how many times he said it. That caution is about *counting* him, not about *dismissing* his content: his core argument — that leading with the monthly figure anchors the comparison the way behavioral economics predicts — is a named, recognized effect, not just a personal opinion, and he taught it professionally. Treat him the same way as P7 below: one data point toward what borrowers actually do, but a critique worth taking seriously as expert-style input on its own terms.

## What this data cannot tell us

- **Prevalence.** Nine participants, not randomly sampled from Oceanside's borrower base. A finding at "3 of 9" or "4 of 9" tells us the pattern exists and roughly how common it was in this sample — it does not tell us what share of all Oceanside borrowers would show it. In particular, we don't know how common P8's public-service-forgiveness situation or P9's "no real choice" financial constraint are across the actual customer base; both are single-participant findings here but could be a meaningful segment or a rare edge case in the full population.
- **Whether the friction found here actually drives the support-ticket increase.** This study did not have access to the actual content of the support tickets that motivated it. Findings 6, 7, and 9 (broken sort header, hidden/misread estimator default, missing interest rate) are plausible contributors — each is a concrete point of confusion or unmet information need — but this report cannot confirm they're the specific cause of the ticket volume, only that they exist and are real.
- **What happened during past abandonment.** Finding 4 is built entirely from retrospective self-report; no one's screen was observed during an actual past abandonment. We know participants say they quit and why they believe they quit, not what they were doing at the time.
- **The reliability of P7's specific behavioral claims.** His stated intentions diverged from his observed behavior repeatedly enough (Finding 5, Individual Observations) that his individual data points about what he would do should be treated with more caution than the rest of the sample.
- **Session completeness.** A few sessions have real gaps: an interruption cut off what the observer flagged as a potentially important statement from P8 about resetting a payment count (T8-L24 is truncated mid-sentence in the source transcript); P4's session had unlogged note-taking gaps; the moderator in P2's session was working from an outdated mockup and momentarily lost track of the plan list. Checked specifically: P2's own naming confusion ("Who names these") happens *before* and independently of the moderator's separate mockup mix-up, so that particular finding isn't downstream of moderator error — but the general point stands that a few individual data points in this dataset are less complete or more session-noisy than others, and that's worth keeping in mind when weighing any single quote heavily.
- **Assumption (restated from Methodology): where the line between "observed" and "self-reported" was drawn for concurrent think-aloud.** Several participants narrated their actions in real time while performing them (e.g. "I look at the total paid, because..."). This report tags that kind of live, declarative narration as `observed_behavior`, and tags conditional framing ("I'd look at...", "what I'd do is...") as `hypothetical_intent` even when the person saying it is looking at the live page at that moment. That's a reasonable, consistently-applied rule, but it's a judgment call, not a fact the data forces — it's a meaningful part of why P7 in particular reads as an unreliable behavioral source throughout this report (his habitual conditional phrasing), and a different rule could classify some borderline excerpts differently.
- **What the verification subagent did and didn't check.** The fresh-context subagent (`verification-findings.md`) confirmed that `themes.md` accurately represents `excerpts.jsonl` — quotes are verbatim, participant counts are arithmetically correct, claims match their cited evidence type. It did not re-derive evidence-type or relevance tags from the raw transcripts itself; it trusted those tags as given. So a debatable original tagging judgment (like the think-aloud line-drawing above) would pass that check even if a different analyst would have tagged it differently. Verification here means internal consistency, not an independent second opinion on every tagging call.
- **The CFPB complaint sample.** A separate, larger dataset of real CFPB student-loan-servicing complaints (`demo-data/cfpb-sample/`) was gathered alongside this study's transcripts but has not been analyzed in this report. It could offer complementary, higher-N context on some of these same questions and is a natural next step, not a source this report already draws on. The off-topic venting excluded from this analysis (mostly P2 and P9, about loan terms and interest rates) is thematically close to that complaint data and may be worth a joint look later rather than treating it as pure noise.

## Implications for the decision

- **Do not lead with density-driven simplification (H2).** The data doesn't support the premise. Removing columns or plans on the theory that there's "too much" on the page addresses a problem this sample mostly didn't report having with today's table.
- **Don't assume total interest needs to be surfaced more prominently to earn attention (H1).** Most participants already look at it or the payoff date without being asked. The monthly-first scan order is real, but it's an entry point, not a blind spot — most who scan monthly first go on to look further.
- **Prioritize disclosure of assumptions behind "projected" figures, and disclosure of the default income-linked number specifically (H3, Findings 7 and 8).** Multiple participants independently proposed the same fix in similar words: state plainly, near the number, what income (or other assumption) it's based on, and label a default/example figure as an example prominently rather than relying on a tooltip that requires a hover to discover. This is the most convergent, most directly actionable finding in the dataset.
- **Fix the two concrete interface bugs regardless of the larger strategic decision (Findings 6 and 9):** the payoff-date header should either sort or not look clickable, and the interest rate should be visible on the comparison page even though it can't be changed there.
- **What the data shows on the recommender decision, versus what we recommend from it — kept separate on purpose.** The data itself is close to evenly split: 4 of 9 skeptical of a recommender specifically over conflict of interest, 4 of 9 conditionally receptive (Finding 11). What is consistent across *both* groups is the condition attached — show your work, don't hide the table, let me verify — so a recommender built without that transparency risks the same distrust the current tool's unlabeled default number already generates. That much is a direct reading of the data. Whether to build the recommender at all, versus investing the same effort in the table fixes above, is a cost and risk tradeoff this qualitative sample cannot settle by itself — nine interviews can tell you what borrowers would need from either option, not which one is the better investment. Our view, as a recommendation and not a finding: the table fixes (assumption disclosure, the two interface bugs) are cheaper, already validated here, and lower-risk to ship first; a recommender is a larger bet that only pays off if it's built transparent from day one. That's our judgment for you to weigh, not something the interviews decided on their own.
- **The support-ticket background question has a mixed answer, not a single-cause one.** Finding 12 shows several borrowers spontaneously separate "the tool is fine" from "the loan is the problem" — some support calls are plausibly reassurance-seeking or loan-frustration calls a clearer tool won't resolve. But Finding 5 shows self-reported "ease" can't be trusted at face value, and Findings 6, 7, 9, and 8 identify specific, real gaps in the tool's current information. Both things are true in this data: some of the ticket volume is likely tool-fixable, some of it likely isn't, and the fixes above address the fixable part.
- **Flag P8's and P9's individual findings for follow-up, not for design action from this study alone.** A qualifying-payment-count tracker for PSLF-track borrowers and a "no real choice" framing for constrained borrowers are each real, specific, and outside every hypothesis this study tested — but each rests on one participant. Before designing for either, it's worth finding out how large these segments actually are in Oceanside's portfolio.
