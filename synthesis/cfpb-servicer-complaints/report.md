# CFPB Student Loan Servicer Complaints — Qualitative Synthesis (Feb–Jul 2026 sample)

> **Note on the data:** unlike the Oceanside repayment-plan-comparison study in this same project (which is synthetic, built for the research-synthesis skill demo), **this is real public data**: real CFPB complaints, naming real servicing companies (MOHELA, Nelnet, Maximus Federal Services, EdFinancial, Navient, and others) and real borrowers. Quotes below are borrowers' own words, with personally identifying details already redacted by CFPB (shown as `XXXX`). This report characterizes patterns in a sample of complaint narratives — it is not a finding about any named company's overall conduct or performance, and should not be read or circulated as one; see "What this data cannot tell us" before drawing conclusions about any specific company.

## What this report answers (no single business decision — see below)

This is an **independent, exploratory analysis** with no stakeholder-provided brief and no business decision it is accountable to (`brief.md`) — unlike the Oceanside study, nobody asked "should we ship X." It answers three self-authored research questions:

- **RQ1** — What does the full population of 1,948 complaints look like by company, sub-issue, and timeliness? → Answered quantitatively in the published dashboard (`synthesis/cfpb-servicer-complaints/dashboard.html`), not repeated here.
- **RQ2** — Within each CFPB sub-issue label, what are borrowers actually describing — does the label correspond to a narrow or a wide range of complaints? → Answered in Findings 3–9 below.
- **RQ3** — Is there a relationship between complaint content and outcome (timely vs. untimely response)? → Answered in Finding 10.

Findings 1–2 are cross-cutting (span all 99 sampled narratives); Findings 3–9 are scoped to one CFPB sub-issue category each (RQ2); Finding 10 is a structural, sample-level cross-tab (RQ3).

## Methodology and assumptions, stated explicitly

- **Assumption:** findings below describe the **stratified sample of 99** narratives (`sample-manifest.md`), not the full population of 1,948. The sample deliberately over-represents small categories (e.g. Co-signer: 8 of 13 total, 61.5%) relative to large ones (e.g. Received bad information: 18 of 760, 2.4%) so every category gets real qualitative representation. **Raw counts and percentages below are sample-internal and must never be read as population-level proportions.**
- **Assumption:** excerpts were drawn from the first one-to-two sentences of each narrative, not the full text, as a practical sampling-within-sampling choice. This is flagged explicitly where it limits a finding (see the Co-signer section).
- **Convention:** "N" varies by finding — 99 for cross-cutting findings, the stratum's own sample size for within-stratum findings (stated on each finding). Thresholds and wording bands are recomputed per N per `theme-building.md`.
- **Structural evidence ceiling:** every excerpt in this dataset is `self_reported_past_behavior` or `stated_attitude` (0 of 128 are `observed_behavior`) — these are unprompted written complaints with no moderator or observed session. **No finding in this report can be labeled "Strong"** under this skill's evidence-strength rubric, regardless of how many narratives support it; this is a property of what a CFPB complaint narrative is, not a tagging shortfall. Every finding below is Moderate or Thin.
- **Selection-bias caveat (load-bearing, not a footnote):** this is a database of people who chose to escalate to a federal regulator. It cannot contain interactions that were resolved to the customer's satisfaction without ever reaching CFPB. Findings describe what complaints are about, not how often these servicers fail borrowers in general.

## Executive summary

- Across the full sample, a substantial minority of complaints — **some (29 of 99), Moderate** — center specifically on getting no substantive response at all, despite repeated effort, rather than disagreeing with an answer they did receive. (Finding 1)
- A distinct but smaller, sub-threshold pattern — **16 of 99, not a theme** — describes the servicer's own prior statement, written confirmation, or system record being directly contradicted by its later action or a different representative. (Finding 2)
- CFPB's sub-issue labels vary widely in how well they predict content: "Trouble with how payments are being handled" is the **narrowest, most label-accurate** category in this sample (**most, 13 of 18, Moderate**), while "Don't agree with the fees charged" turns out to be mostly about interest/capitalization rather than discrete fees (**about half, 7 of 13, Moderate, numerically fragile**), and "Received bad information about your loan" is the **widest-ranging** label, with no majority sub-pattern. (Findings 3–9)
- Timeliness of response tracks **both** company and complaint content in this sample, and the two are correlated: one company (MOHELA) accounts for most of the sample's untimely responses, but even restricted to MOHELA alone, timeliness still varies sharply by what the complaint is about. (Finding 10 — structural/quantitative, sample-level only)

---

## Findings

### Finding 1 — Many complaints center on getting no substantive response at all, despite repeated effort (Moderate)

This is distinct from disagreeing with an outcome: these narratives describe a direct question or request met with no real answer — form letters, "it's being looked into," generic scripts, or literally no reply, often after many attempts over weeks or months.

Support: some (29 of 99) — [C3-L1, C7-L1, C17-L1, C18-L1, C21-L1b, C23-L1, C25-L1, C29-L1, C31-L1, C36-L1, C41-L1, C50-L1, C54-L1, C56-L1, C58-L1, C59-L1b, C62-L1, C65-L1, C68-L1, C70-L1, C71-L1, C72-L1, C75-L1, C77-L1, C86-L1, C87-L1, C89-L1, C91-L1, C92-L1]
Counter-evidence: a couple (2 of 99) — [C52-L1, C34-L1a]

> “To date, MOHELA has issued only form acknowledgment letters and has not provided any substantive response, qualifying payment count, or IDR Adjustment determination.” (C3-L1)
> “Despite these repeated attempts, I have not received any meaningful response or follow-up from MOHELA.” (C18-L1)
> “I've asked several times for them to fix the problem or to send me paper so I can try to apply through paperwork and yet I've got no help from them at all nothing in the mail and no call back nothing just dead air” (C65-L1)
> “I have emailed, chatted, called multiple times since then and documented every interaction to no avail.” (C87-L1)
> “On at least XXXX occasions XX/XX/XXXX, XX/XX/XXXX, XX/XX/XXXX, XX/XX/XXXX, XX/XX/XXXX, and XX/XX/year> logging in to view these messages produced only a generic placeholder with no substantive content.” (C91-L1)

Counter-evidence: in a couple of narratives, the servicer gave a specific, substantive reason — the complaint there is that the reason is wrong, not that nothing was said: “Their entire stated reason: "Lack of information that the school used misleading or deceptive practices." This directly contradicts a formal federal agency determination.” (C52-L1)

**Evidence-strength basis:** clears the 20-of-99 threshold comfortably (29, "some"); entirely `self_reported_past_behavior`/`stated_attitude` (no `observed_behavior` possible in this data — structural ceiling applies); no leading-question dependency (none exist in this dataset); counter-evidence weighed and does not undercut the pattern. Capped at Moderate solely by the structural ceiling.

### Finding 2 — Isolated pattern, not a theme: servicer told or showed the borrower one thing, then contradicted it (16 of 99)

A distinct, more specific pattern from Finding 1: not "no answer," but a written confirmation, verbal assurance, or the servicer's own system record later contradicted by the servicer's own subsequent action, statement, or document.

**This does not clear the 20-of-99 theme threshold** (16 of 99 = 16.2%, below the 20 required) and is reported as an isolated pattern, with the raw fraction rather than a qual-quant word, per `theme-building.md`.

16 of 99 — [C6-L9, C17-L1, C21-L1b, C27-L1a, C32-L1, C45-L1, C46-L1, C49-L1, C55-L1, C59-L1, C60-L1, C69-L1, C80-L1b, C84-L1b, C86-L1, C97-L1b]

> “Despite this, Nelnet later accrued more than {$10000.00} in interest during this same period, without notice, while continuing to keep my loans in forbearance.” (C6-L9) — after being told in writing the loans would sit at 0% interest.
> “However, despite this approval, my account now reflects presumed standard repayment amount of approximately {$5000.00} per month, which is more than my monthly net pay salary.” (C80-L1b) — after the servicer approved $440/month in writing.
> “On XX/XX/year>, I called back XXXX spoke with a representative who contrarily claimed there were " no notes '' on my account regarding the forbearance terms, XXXX that I had been considered past due since XXXX.” (C84-L1b) — directly contradicting what a different representative told the same borrower on a prior call.

This overlaps partially with Finding 1 (e.g. C17, C21, C59, C86 appear in both) — a single narrative can describe both "I got no real answer" and, separately, "what I was told turned out to be false." Kept as two distinct claims because they describe different failure modes.

---

### RQ2 — Within-stratum findings: does the CFPB sub-issue label match a narrow or wide range of complaints?

Each finding below uses the stratum's own N (its sampled count, per `sample-manifest.md`) and its own threshold. **These fractions describe only the sampled narratives within that stratum and must not be read as population proportions** (the sample over-represents small categories by design).

### Finding 3 — "Don't agree with the fees charged" is mostly an interest/capitalization dispute, not a dispute over discrete fee line-items (Moderate, numerically fragile)

N = 13, threshold = 3.

Support: about half (7 of 13) — [C1-L1, C4-L1, C6-L9, C19-L1b, C21-L1, C47-L1, C83-L1b]
Counter-evidence: about half (6 of 13) — [C29-L1, C38-L1, C54-L1, C57-L1, C33-L1, C73-L1]

> “I was enrolled in the SAVE plan and now being pushed to another plan. However, the correct payment terms and monthly payment fees can not be determined. Thus making it impossible for me to change plans. Interest has been accruing since XX/XX/year> and there is no avenue for me to continue payment.” (C1-L1)
> “Of the {$23000.00} paid over 23 years, only {$8900.00} ( 37.9 % ) went toward principal reduction. The remaining {$14000.00} ( 62.1 % ) was consumed by interest.” (C19-L1b)

**Fragility caveat (from bias review):** support (7) and counter-evidence (6) are separated by exactly one narrative — a different reasonable coder could plausibly classify 1–2 cases differently and flip which side is larger. The underlying observation (interest/capitalization language dominates over discrete-fee language) is still well-supported by the 7 clear cases, but this should not be read with the same confidence as Findings 4 or 6.

### Finding 4 — "Trouble with how payments are being handled" is the narrowest, most label-accurate category in this sample (Moderate)

N = 18, threshold = 4.

Support: most (13 of 18) — [C2-L3, C11-L1, C14-L1, C15-L1, C24-L1b, C28-L1, C39-L1, C41-L1, C55-L1, C61-L1b, C80-L1b, C82-L1, C88-L1]
Counter-evidence: a few (5 of 18) — [C34-L1b, C65-L1, C69-L1, C72-L1, C86-L1]

> “MOHELAs billing platform has generated a monthly payment amount of {$650.00}, based on a raw percentage of my discretionary income. This is a severe calculation error and a direct violation of federal student loan regulations.” (C82-L1)
> “This is the second month in a row that MOHELA keeps canceling my autopayment the day it's scheduled to be removed.” (C88-L1)

Unlike "fees," this category name reliably predicts content: payments recorded, applied, or billed differently than the borrower was told to expect.

### Finding 5 — "Problem with customer service" complaints are, in this sample, mostly the same non-responsiveness pattern as Finding 1 (Moderate)

N = 18, threshold = 4.

Support: more than half (10 of 18) — [C3-L1, C7-L1, C17-L1, C31-L1, C58-L1, C62-L1, C77-L1, C87-L1, C91-L1, C92-L1]
Counter-evidence: some (8 of 18) — [C10-L1, C12-L1, C40-L1, C43-L1, C66-L1, C81-L1, C85-L1, C53-L1]

> “In total, I have now sent nine ( 9 ) certified letters, and MOHELA has not provided a substantive written response to these letters.” (C62-L1)
> “I was then placed on hold for over XXXX hours without ever speaking to anyone. I eventually had to hang up after XXXX hours and XXXX minutes without resolution.” (C92-L1)

### Finding 6 — "Received bad information about your loan" is the widest-ranging label in this sample, with a sub-pattern of directly contradicted information covering only a third (Thin on the sub-pattern; the overall breadth claim is Moderate)

N = 18, threshold = 4.

Support: some (6 of 18) — [C32-L1, C49-L1, C52-L1, C59-L1, C84-L1b, C97-L1b]
Counter-evidence: most of the stratum (12 of 18) does not share this specific sub-pattern — [C5-L3, C9-L1, C25-L1, C30-L1, C67-L1, C76-L1, C78-L1, C79-L1, C89-L1, C95-L1, C96-L1, C71-L1]

> “On XX/XX/XXXX, MOHELA denied my SCRA request, stating that I have " no association '' with the loan. This directly contradicts their own records identifying me as the student tied to the obligation.” (C32-L1)

This label is the widest-ranging of the seven: 18 sampled narratives touch at least ten distinguishable underlying problems (wrong account status, denied relief contradicting a federal determination, conflicting balances, blame-shifting between servicer and Department of Education, undisclosed consolidation effects, post-discharge billing, uncorrected credit reporting, and more), with no single sub-pattern covering a majority. The 6-of-18 contradiction slice is this report's thinnest finding — just above its threshold of 4, lowest support percentage (33.3%) of the within-stratum themes — and should be read as a real but modest sub-pattern, not as characterizing this category overall.

### Finding 7 — "Keep getting calls about your loan" narrowly means unwanted call/contact volume, in this sample (Moderate)

N = 8, threshold = 2.

Support: more than half (5 of 8) — [C8-L1, C16-L1, C26-L1, C74-L1, C98-L1]
Counter-evidence: some (3 of 8) — [C42-L1, C60-L1, C90-L1]

> “Within three days they have called me 8 times from ( XXXX ) XXXX.” (C16-L1)
> “In the letter they were asked to cease and desist contacting me. They've continued to call, leave voice mails and email me on a frequent basis.” (C26-L1)

### Finding 8 — "Need information about your loan balance or loan terms" mostly means borrowers could not get an authoritative status or figure (Moderate)

N = 16, threshold = 4.

Support: more than half (9 of 16) — [C18-L1, C22-L1, C23-L1, C36-L1, C50-L1, C56-L1, C68-L1, C70-L1, C75-L1]
Counter-evidence: some (7 of 16) — [C13-L1, C35-L1, C37-L1, C51-L1a, C64-L1, C93-L1, C44-L1]

> “Aidvantage has told me several wildly different amounts I will owe, from $ XXXX to $ XXXX. They can not tell me what numbers they are using to calculate these figures.” (C50-L1)
> “I later received written confirmation that my request is in process under case number XXXX, but was also told there is no status mechanism available and that neither the Federal Student Aid contact center nor my servicer can provide a status update.” (C36-L1)

This label functions less like "I want to look up a number" and more like a specific instance of Finding 1 — 8 of its 9 supporting IDs also appear in that theme's support list.

### Finding 9 — Not themed: "Co-signer" category content could not be reliably characterized from the excerpted text (methodology limitation, not a finding)

N = 8. Only 3 of the 8 sampled narratives in this stratum (C20, C27, C99) reference a co-signer relationship in the excerpted text itself. The other 5 (C45, C46, C48, C63, C94) were coded from only the first one-to-two sentences of each narrative; the co-signer-specific detail may appear later in the full text, outside what was excerpted. This is reported as a **limitation of excerpt coverage**, not a conclusion that this label is scattered or incoherent — a fuller read of those five narratives would be needed before drawing any conclusion about this category's content range.

---

### RQ3 — Finding 10: Timeliness tracks both company and complaint content, and the two are correlated (Structural/quantitative, sample-level only — not the Strong/Moderate/Thin rubric)

This finding is derived from exact categorical metadata on the 99 sampled narratives (`sample-manifest.md`), cross-tabulated, not from counting qualitative patterns — the evidence-strength rubric above doesn't directly apply, but the same sample-level-only caveat does: **this describes the stratified sample, not the full population of 1,948** (see the dashboard for population-level timeliness by sub-issue, which is directionally consistent with what follows).

In the 99-narrative sample: MOHELA accounts for 46 of 99 narratives, and 32 of those 46 (70%) received an untimely response, versus 3 of 53 (6%) for every other company combined. That alone could make this purely a company-level story. It isn't purely that: **restricted to MOHELA narratives only**, timeliness still varies sharply by sub-issue —

| Sub-issue (MOHELA only) | Timely | Total | Rate |
|---|---|---|---|
| Co-signer | 2 | 2 | 100% |
| Keep getting calls about your loan | 2 | 2 | 100% |
| Received bad information about your loan | 6 | 10 | 60% |
| Problem with customer service | 2 | 6 | 33% |
| Need information about your loan balance or loan terms | 1 | 8 | 12% |
| Trouble with how payments are being handled | 1 | 14 | 7% |
| Don't agree with the fees charged | 0 | 4 | 0% |

Several of the qualitative findings above offer a plausible (not proven) interpretive lens on why: the slow categories (payments-handling, fees/interest, balance/terms) are exactly the ones this report found dominated by multi-step, individualized review — IDR/forgiveness payment-count audits, interest-capitalization disputes, cross-agency (servicer + Department of Education) determinations (Findings 3, 4, 8) — while the fast categories (co-signer release, stop-the-calls) are closer to single-step, proceduralized requests. This is a reasonable interpretation grounded in the qualitative content, not a demonstrated causal mechanism; the cell sizes above are small (as low as n=2), and non-MOHELA companies' near-uniform timeliness across categories (nearly all "Yes," based on far smaller per-company volumes in this sample) could equally reflect that smaller servicers in this sample simply have less complaint volume to triage, not a different process.

---

## Individual and isolated observations

- **Finding 2** (above) is the main cross-cutting isolated pattern (16 of 99, below the 20-of-99 theme threshold).
- Several narratives describe distinct, serious-sounding situations represented by only 1 participant each and not claimed as any theme: alleged forged loan-application signatures (C48), fraudulent credit lines opened in a servicer's name (C81), a scam-like collections call for an account that does not exist (C98), and a refund check that expired with no disclosed deadline (C43). Each is a single observation, not a pattern — flagged here so they aren't silently lost, not inflated into findings.

## What this data cannot tell us

- **How often these servicers fail to respond, in general.** This is a complaints database — a sample selected specifically for dissatisfaction. It cannot estimate the rate of unresolved issues among all interactions, only describe what complaints that do reach CFPB are about. Finding 1's "some (29 of 99)" is not "29% of all interactions with these servicers go unanswered."
- **Whether non-MOHELA servicers are actually faster, or just have less complaint volume.** The sample's non-MOHELA timeliness rate (94%) comes from far fewer total complaints per company than MOHELA's single large volume; small-number effects are plausible and this report cannot rule them out with this sample size.
- **Anything about the fictional Oceanside study.** Per the brief, this is an independent analysis; any apparent similarity in theme language (e.g., both studies surfacing a "contradiction between stated information and actual behavior/outcome" pattern) is not evidence that Oceanside's hypothetical borrowers would behave like real CFPB complainants, or vice versa.
- **The full content of the 5 under-excerpted Co-signer narratives** (Finding 9) — only their first one-to-two sentences were coded.
- **Causal explanation for Finding 10's company/content pattern.** The interpretive note offered is grounded in this report's qualitative findings but is not a demonstrated mechanism; cell sizes are small.
- **Anything about the ~95% of the population not in the qualitative sample.** The stratified sample guarantees every category real representation but is not a census; a pattern absent from the sample could still exist at scale, and a pattern present in the sample is not guaranteed to hold at the same rate across the full 1,948.

## Implications

- **Finding 1 + Finding 5 + Finding 8** (non-responsiveness, cutting across "customer service" and "balance/terms" complaints alike) suggest that if anyone is prioritizing what to fix first in a real servicer's complaint-handling process, "does every direct request get a substantive, specific answer" is a higher-yield question than "is the customer service department polite" — the pattern is about absence of a real answer, not tone.
- **Finding 10** suggests that if accountability for timeliness is being assigned, attributing it to one company's overall performance (MOHELA) without controlling for complaint-content mix risks over- or under-crediting that company — the same company looks very different (100% timely) on proceduralized requests than on multi-step case reviews (7% timely). Any comparison across servicers should control for the sub-issue mix each one actually receives.
- **Finding 3's fragility and Finding 9's coverage gap** are a process note for this skill, not a finding about servicers: a 50/50-ish split theme and an under-excerpted category are both signs that excerpting only the first 1-2 sentences per narrative is a real limitation for a sample this size — a follow-up pass reading full narratives for these two categories specifically would be worth the time before treating Findings 3 or 9 as settled.
