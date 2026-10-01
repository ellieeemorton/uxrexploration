# Themes — CFPB Servicer Complaint Narratives

Built from the 128 on-topic/adjacent excerpts tagged across the 99 sampled narratives (`excerpts.jsonl`), per `references/theme-building.md`. All evidence here is `self_reported_past_behavior` or `stated_attitude` — these are unprompted written complaints with no moderator, so `observed_behavior` is structurally impossible in this dataset. See the structural note at the end of this file before reading evidence-strength labels in `report.md`.

Two kinds of pattern are reported below:
- **Cross-cutting themes/patterns** — N = 99 (every sampled narrative produced at least one on-topic/adjacent excerpt), threshold = max(2, ceil(0.20 × 99)) = **20**.
- **Within-stratum themes** — scoped to one CFPB sub-issue category, N = that stratum's sample size (per `sample-manifest.md`), threshold recomputed per stratum. These answer RQ2 (does the category label correspond to a narrow or wide range of complaints) and are explicitly **sample-level, not population-level** — see `brief.md`'s scope note on the stratified sample.

---

## Cross-cutting (N = 99)

### Theme: Many complaints center on getting no substantive response at all, despite repeated effort

This is distinct from disagreeing with an outcome — these narratives describe asking a direct question or making a direct request and receiving no real answer: form letters, "it's being looked into," generic scripts, or literally no reply, often after many attempts over weeks or months.

Support: some (29 of 99) — [C3-L1, C7-L1, C17-L1, C18-L1, C21-L1b, C23-L1, C25-L1, C29-L1, C31-L1, C36-L1, C41-L1, C50-L1, C54-L1, C56-L1, C58-L1, C59-L1b, C62-L1, C65-L1, C68-L1, C70-L1, C71-L1, C72-L1, C75-L1, C77-L1, C86-L1, C87-L1, C89-L1, C91-L1, C92-L1]
Counter-evidence: a couple (2 of 99) — [C52-L1, C34-L1a]

> “To date, MOHELA has issued only form acknowledgment letters and has not provided any substantive response, qualifying payment count, or IDR Adjustment determination.” (C3-L1)
> “Despite these repeated attempts, I have not received any meaningful response or follow-up from MOHELA.” (C18-L1)
> “I've asked several times for them to fix the problem or to send me paper so I can try to apply through paperwork and yet I've got no help from them at all nothing in the mail and no call back nothing just dead air” (C65-L1)
> “I have emailed, chatted, called multiple times since then and documented every interaction to no avail.” (C87-L1)
> “On at least XXXX occasions XX/XX/XXXX, XX/XX/XXXX, XX/XX/XXXX, XX/XX/XXXX, XX/XX/XXXX, and XX/XX/year> logging in to view these messages produced only a generic placeholder with no substantive content.” (C91-L1)

Counter-evidence detail: in a couple of narratives, the servicer did give a specific, substantive reason — the complaint is that the reason is wrong or indefensible, not that nothing was said. "Their entire stated reason: \"Lack of information that the school used misleading or deceptive practices.\" This directly contradicts a formal federal agency determination." (C52-L1) The representative in C34 likewise gave the borrower a direct instruction ("DO NOT WORRY... call again in a year") rather than no answer — the borrower's complaint is that the advice was bad, not that none was given.

**Important caveat (selection bias, not a finding about the servicers' typical behavior):** this is a database of people who chose to escalate a complaint to a federal regulator. By construction, it cannot contain the (unknown, possibly large) set of interactions that were resolved to the customer's satisfaction without ever reaching CFPB. "Some (29 of 99) complaint narratives center on non-responsiveness" describes what people who already decided to complain are complaining about — it is not an estimate of how often this servicer population fails to respond, which would require a denominator this data doesn't have. See "What this data cannot tell us" in `report.md`.

---

### Isolated pattern (below the 20-of-99 theme threshold): told one thing, shown or told another

A distinct, more specific pattern from the one above: not "no answer," but a written confirmation, a verbal assurance, or the servicer's own system record was later contradicted by the servicer's own subsequent action, statement, or document.

This clears "at least 2 distinct participants" but **does not clear 20% of N=99** (16 of 99 = 16.2%, below the 20 required) — per `theme-building.md` this is reported as an isolated pattern, not promoted to a theme, and is written with the raw fraction rather than a qual-quant word.

16 of 99 — [C6-L9, C17-L1, C21-L1b, C27-L1a, C32-L1, C45-L1, C46-L1, C49-L1, C55-L1, C59-L1, C60-L1, C69-L1, C80-L1b, C84-L1b, C86-L1, C97-L1b]

> “Despite this, Nelnet later accrued more than {$10000.00} in interest during this same period, without notice, while continuing to keep my loans in forbearance.” (C6-L9) — after being told in writing the loans would sit at 0% interest.
> “However, despite this approval, my account now reflects presumed standard repayment amount of approximately {$5000.00} per month, which is more than my monthly net pay salary.” (C80-L1b) — after the servicer approved $440/month in writing.
> “On XX/XX/year>, I called back XXXX spoke with a representative who contrarily claimed there were " no notes '' on my account regarding the forbearance terms, XXXX that I had been considered past due since XXXX.” (C84-L1b) — directly contradicting what a different representative told the same borrower on the prior call.

This pattern overlaps partially with the non-responsiveness theme above (e.g. C17, C21, C59, C86 appear in both lists) — a single narrative can describe both "I got no real answer" and, separately, "what I was told turned out to be false." They are kept as two distinct claims because they describe different servicer failure modes and neither entails the other.

---

## Within-stratum themes (RQ2: does the sub-issue label match a narrow or wide range of complaints?)

Each stratum below uses its own N (the stratum's sampled count, per `sample-manifest.md`) and its own threshold = max(2, ceil(0.20×N)). **These fractions describe only the sampled narratives within that stratum — they are not population proportions** (the sample is stratified, not proportional; see `brief.md`).

### Theme: "Don't agree with the fees charged" is, in this sample, mostly an interest/capitalization dispute — not a dispute over discrete fee line-items

N = 13, threshold = max(2, ceil(2.6)) = 3.

Support: more than half (8 of 13) — [C1-L1, C4-L1, C6-L9, C19-L1b, C21-L1, C47-L1, C73-L1, C83-L1b]
Counter-evidence: some (5 of 13) — [C29-L1, C38-L1, C54-L1, C57-L1, C33-L1]

> “I was enrolled in the SAVE plan and now being pushed to another plan. However, the correct payment terms and monthly payment fees can not be determined. Thus making it impossible for me to change plans. Interest has been accruing since XX/XX/year> and there is no avenue for me to continue payment.” (C1-L1)
> “Of the {$23000.00} paid over 23 years, only {$8900.00} ( 37.9 % ) went toward principal reduction. The remaining {$14000.00} ( 62.1 % ) was consumed by interest.” (C19-L1b)

Counter-evidence detail: the remaining 5 of 13 are a genuine mix with no shared sub-theme of their own — a wrong portal balance with no ledger (C29), an undisclosed variable interest rate at signing (C38, arguably interest-adjacent but about disclosure, not accrual), a years-long forgiveness-paperwork wait that isn't about fees at all (C54), a billing dispute after a medical withdrawal (C57), and one `adjacent`-tagged narrative about a different, unrelated grievance (C33). The CFPB's "fees charged" label, at least here, functions more as "something costs more than the borrower expected," with interest capitalization as the dominant specific mechanism.

### Theme: "Trouble with how payments are being handled" narrowly and consistently means payments recorded, applied, or billed differently than the borrower was told to expect

N = 18, threshold = max(2, ceil(3.6)) = 4.

Support: most (13 of 18) — [C2-L3, C11-L1, C14-L1, C15-L1, C24-L1b, C28-L1, C39-L1, C41-L1, C55-L1, C61-L1b, C80-L1b, C82-L1, C88-L1]
Counter-evidence: a few (5 of 18) — [C34-L1b, C65-L1, C69-L1, C72-L1, C86-L1]

> “MOHELAs billing platform has generated a monthly payment amount of {$650.00}, based on a raw percentage of my discretionary income. This is a severe calculation error and a direct violation of federal student loan regulations.” (C82-L1)
> “This is the second month in a row that MOHELA keeps canceling my autopayment the day it's scheduled to be removed.” (C88-L1)

Counter-evidence detail: the remaining 5 of 18 are present but don't carry the "mis-recorded/mis-applied payment" signature as their primary content — they're about unresolved process/communication problems that happen to be filed under this label (an un-followed-through escalation promise, a stalled application, a non-responsive service request). This is the **narrowest** of the seven labels in this sample — unlike "fees," the category name is a good predictor of content.

### Theme: "Problem with customer service" complaints are, in this sample, mostly about the same non-responsiveness pattern found cross-sample

N = 18, threshold = max(2, ceil(3.6)) = 4.

Support: more than half (11 of 18) — [C3-L1, C7-L1, C17-L1, C31-L1, C53-L1, C58-L1, C62-L1, C77-L1, C87-L1, C91-L1, C92-L1]
Counter-evidence: some (7 of 18) — [C10-L1, C12-L1, C40-L1, C43-L1, C66-L1, C81-L1, C85-L1]

> “In total, I have now sent nine ( 9 ) certified letters, and MOHELA has not provided a substantive written response to these letters.” (C62-L1)
> “I was then placed on hold for over XXXX hours without ever speaking to anyone. I eventually had to hang up after XXXX hours and XXXX minutes without resolution.” (C92-L1)

This stratum is the clearest internal confirmation of the cross-cutting non-responsiveness theme: most of what gets filed as a "customer service" problem specifically is the servicer failing to substantively engage, not rudeness or a single bad interaction.

### Theme: "Received bad information about your loan" is broad in surface detail; roughly a third involve information that was later directly contradicted, and the remaining majority share no single pattern

N = 18, threshold = max(2, ceil(3.6)) = 4. The 7-of-18 contradiction slice clears this stratum's threshold (4) and so is reported as a proper theme — but note it still describes well under half the stratum: the remaining 11 of 18 narratives range across credit-report errors, incomplete refunds, undisclosed consolidation consequences, and billing after a legal discharge, each represented by only 1-2 narratives apiece with no shared sub-pattern among them.

Support: some (7 of 18) — [C32-L1, C49-L1, C52-L1, C59-L1, C71-L1, C84-L1b, C97-L1b]
Counter-evidence: most of the stratum (11 of 18) does not share this specific sub-pattern — [C5-L3, C9-L1, C25-L1, C30-L1, C67-L1, C76-L1, C78-L1, C79-L1, C89-L1, C95-L1, C96-L1]

> “On XX/XX/XXXX, MOHELA denied my SCRA request, stating that I have " no association '' with the loan. This directly contradicts their own records identifying me as the student tied to the obligation.” (C32-L1)

This label is the **widest-ranging** of the seven in this sample: 18 sampled narratives touch at least ten distinguishable underlying problems (wrong account status, denied relief contradicting a federal determination, conflicting balances, blame-shifting between servicer and Department of Education, undisclosed consolidation effects, post-discharge billing, uncorrected credit reporting, and more), with no single sub-pattern covering a majority.

### Theme: "Keep getting calls about your loan" narrowly means unwanted call/contact volume, in this sample

N = 8, threshold = max(2, ceil(1.6)) = 2.

Support: more than half (5 of 8) — [C8-L1, C16-L1, C26-L1, C74-L1, C98-L1]
Counter-evidence: some (3 of 8) — [C42-L1, C60-L1, C90-L1]

> “Within three days they have called me 8 times from ( XXXX ) XXXX.” (C16-L1)
> “In the letter they were asked to cease and desist contacting me. They've continued to call, leave voice mails and email me on a frequent basis.” (C26-L1)

Counter-evidence detail: 3 of 8 are filed under this label but center on something else — a billing dispute over a loan allegedly never disbursed (C42), a forbearance-confirmation contradiction where calls are incidental (C60), and fraud/identity-theft-driven credit damage (C90).

### Theme: "Need information about your loan balance or loan terms" mostly means borrowers could not get an authoritative status or figure, not that information was simply unavailable to look up

N = 16, threshold = max(2, ceil(3.2)) = 4.

Support: more than half (10 of 16) — [C18-L1, C22-L1, C23-L1, C36-L1, C44-L1, C50-L1, C56-L1, C68-L1, C70-L1, C75-L1]
Counter-evidence: some (6 of 16) — [C13-L1, C35-L1, C37-L1, C51-L1a, C64-L1, C93-L1]

> “Aidvantage has told me several wildly different amounts I will owe, from $ XXXX to $ XXXX. They can not tell me what numbers they are using to calculate these figures.” (C50-L1)
> “I later received written confirmation that my request is in process under case number XXXX, but was also told there is no status mechanism available and that neither the Federal Student Aid contact center nor my servicer can provide a status update.” (C36-L1)

This label functions less like "I want to look up a number" and more like a specific instance of the cross-cutting non-responsiveness theme (8 of its 10 supporting IDs also appear in that theme's support list).

### Not themed — methodology caveat: "Co-signer" (N = 8)

Only 3 of the 8 sampled narratives in this stratum (C20, C27, C99) reference a co-signer relationship in the excerpted text itself. The other 5 (C45, C46, C48, C63, C94) were coded from only the first one-to-two sentences of each narrative (per this skill's excerpting approach), and the co-signer-specific detail may appear later in the full narrative text, outside what was excerpted. Rather than report "this label is scattered/incoherent" as a finding, this is flagged as a **limitation of excerpt coverage, not a conclusion about the label** — a fuller read of the five under-excerpted narratives would be needed before drawing any conclusion about this stratum's content range. No theme or isolated pattern is claimed here.

---

## Structural evidence ceiling (applies to every theme and pattern above)

This dataset is unprompted written complaints with no moderator and no observation of actual behavior — every excerpt is `self_reported_past_behavior` or `stated_attitude` (128 of 128; 0 `observed_behavior`). Per `report-template.md`'s evidence-strength rubric, "Strong" requires `observed_behavior` to be present. **No finding in this file can ever be graded Strong, regardless of how many narratives support it** — this is a property of what a CFPB complaint narrative is, not a tagging shortfall. Every finding in `report.md` derived from this file is capped at Moderate or Thin.
