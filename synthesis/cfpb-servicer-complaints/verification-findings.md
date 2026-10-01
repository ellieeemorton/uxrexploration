# Verification Findings — CFPB Servicer Complaint Themes

A fresh-context subagent (given only `themes.md` and `excerpts.jsonl`, per `references/verification-subagent.md` — no brief, no prior conversation) reviewed every theme and pattern for quote fidelity, quote relevance, participant-count arithmetic, and behavioral-language overreach. Deterministic `verify_quotes.py` was also run before and after resolving the subagent's findings.

## Result summary

- **Quote fidelity: 0 failures.** Every quoted string in `themes.md`, across all themes and patterns, is an exact verbatim substring of its cited excerpt's `text` field. No fabricated or altered quotes found anywhere.
- **Participant-count arithmetic (as cited): 0 failures.** Every `Support:`/`Counter-evidence:` line's stated count and word matched the distinct-participant count of its cited IDs, before and after the fixes below.
- **Behavioral-language overreach: 0 failures.** All themes consistently use "describe"/"report"/"stated" framing rather than asserting observed behavior, correctly respecting the structural evidence ceiling (0 of 128 excerpts are `observed_behavior`).
- **Quote relevance: 3 failures, 1 weak-fit flag.** All four resolved below.

## Findings and resolutions

### 1. "Fees charged" theme — C73-L1 miscited as support
**Finding:** C73-L1 ("I had completed 88 of 120 qualifying IDR payments... The 22-month administrative forbearance period has not been credited toward my qualifying payment count") is a PSLF/IDR payment-count-crediting dispute, not a fees-or-interest dispute. It does not support the claim that this is "mostly an interest/capitalization dispute."
**Resolution:** Moved C73 from Support to the "genuine mix, no shared sub-theme" counter-evidence group. Support recomputed from 8 of 13 ("more than half") to **7 of 13 ("about half")**; counter-evidence from 5 of 13 to **6 of 13 ("about half")**. Theme wording softened accordingly ("barely over 'about half' rather than 'more than half'").

### 2. "Problem with customer service" theme — C53-L1 miscited as support
**Finding:** C53-L1 ("they stated that because the loans were already discharged... they would not review the misconduct claim or provide any refund") shows the servicer giving a specific, substantive stated reason for refusal — the subagent correctly noted this is the exact pattern the cross-cutting non-responsiveness theme's own counter-evidence section, and this stratum's own C40, treat as *disputing an answer received*, not *receiving no answer*. Citing it as support was internally inconsistent with how the author treated the identical pattern elsewhere in the same file.
**Resolution:** Moved C53 from Support to Counter-evidence. Support recomputed from 11 of 18 to **10 of 18** (word unchanged: "more than half," 55.6%); counter-evidence from 7 of 18 to **8 of 18** ("some").

### 3. "Received bad information" contradiction theme — C71-L1 miscited as support
**Finding:** C71-L1 ("MOHELA has informed me that it does not determine discharge amounts... neither MOHELA nor the Department of Education has provided a clear explanation") is buck-passing/non-response, not a case where specific information was later directly contradicted. The subagent noted it is already correctly cited elsewhere, as support for the cross-cutting non-responsiveness theme — it simply doesn't also belong in this stratum's narrower contradiction sub-theme.
**Resolution:** Moved C71 out of this theme's Support list into the stratum's "doesn't share this sub-pattern" group. Support recomputed from 7 of 18 to **6 of 18** ("some"); the "doesn't share the pattern" count from 11 of 18 to **12 of 18** ("most").

### 4. "Need information about balance/terms" theme — C44-L1 weak fit (flagged, not a hard fail)
**Finding:** The subagent flagged C44-L1 ("told I would have an offer within 45 days. This has not happened") as a soft/borderline fit — closer to a missed-promise/non-response complaint than to "could not get an authoritative balance or figure," though not clearly wrong given the category's breadth.
**Resolution:** On review, agreed this is a judgment call worth tightening rather than leaving ambiguous — removed C44 from Support and placed it in Counter-evidence, consistent with the stricter reading. Support recomputed from 10 of 16 to **9 of 16** ("more than half," 56.25%); counter-evidence from 6 of 16 to **7 of 16** ("some"). The downstream cross-reference claim ("8 of its 10 supporting IDs also appear in the non-responsiveness theme") was updated to "8 of its 9."

## What was checked and found correct (no change)

- **Cross-cutting non-responsiveness theme (29 of 99)** — all 5 inline quotes and both counter-evidence citations verified exact and relevant; participant count confirmed.
- **Isolated pattern, contradicted information (16 of 99)** — all quotes verified exact; count and below-threshold classification confirmed correct.
- **"Trouble with how payments are being handled" theme (13 of 18)** — all 13 support IDs and 5 counter-evidence IDs verified relevant; no changes.
- **"Keep getting calls" theme (5 of 8)** — all IDs verified relevant; no changes.
- **"Co-signer" not-themed section** — the claim that only C20/C27/C99 reference a co-signer relationship in their excerpted text was verified accurate; correctly reported as an excerpt-coverage limitation rather than a false content-incoherence finding.
- **Structural evidence ceiling section** — 128-excerpt total, 0 `observed_behavior` count, and all seven within-stratum N's summing to 99 were independently recomputed and confirmed correct.

After these four fixes, `verify_quotes.py` was re-run and reports 19 quoted citations and 13 Support/Counter-evidence lines, zero mismatches.
