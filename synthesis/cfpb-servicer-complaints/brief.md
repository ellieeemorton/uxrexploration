# Research Brief: CFPB Student Loan Servicing Complaints (Feb–Jul 2026)

## Note on this brief
Unlike the Oceanside study, no stakeholder-provided research brief exists for this dataset — the request was "break down categories of complaints and analyze the open-ended responses." This brief was drafted to give the qualitative coding pass a consistent frame of reference, per the research-synthesis skill's requirement that tagging be calibrated against stated questions rather than done ad hoc. Treat the research questions below as a reasonable, self-authored scope for an exploratory analysis, not a business decision this report is accountable to.

## Data
1,948 real CFPB consumer complaints: Product = "Student loan", Issue = "Dealing with your lender or servicer", with a non-empty narrative, received 2026-02-01 through 2026-07-28. 54 distinct companies (not Oceanside — these are real servicers: MOHELA, Nelnet, Maximus Federal Services, EdFinancial, Navient, and others). Source: `demo-data/cfpb-sample/feb-jul-2026/` (`labels.csv` + `narratives/`), derived from the raw CFPB complaint export by `demo-data/cfpb-scripts/`.

## Research questions
1. What does the categorical data show about the shape of these complaints — which companies, sub-issues, and outcomes (timely response, resolution type) dominate, and how does volume trend over the six-month window?
2. Within each sub-issue category, what are borrowers actually describing in their own words? Do the categories (e.g., "Trouble with how payments are being handled," "Received bad information about your loan") correspond to a narrow or a wide range of underlying complaints?
3. Is there a relationship between complaint content and outcome — e.g., do complaints that got an "Untimely response" describe a different kind of problem than ones closed with an explanation?

## Scope and limits set upfront
- This is an **independent analysis**, not cross-referenced against the Oceanside repayment-plan-comparison study. Oceanside is fictional and does not appear in this real dataset; any apparent similarity in themes is not evidence about Oceanside specifically.
- The quantitative breakdown (company, sub-issue, outcome, state, time trend) covers the full population of 1,948 complaints.
- The qualitative coding of open-ended narratives covers a **stratified random sample**, not the full population — see `sample-manifest.md` for the sampling method, stratum sizes, and random seed. Findings from the sample describe patterns within the sample; they are not a census of all 1,948 narratives, though the stratification is designed to give every sub-issue category real qualitative representation rather than letting the two largest categories dominate.
