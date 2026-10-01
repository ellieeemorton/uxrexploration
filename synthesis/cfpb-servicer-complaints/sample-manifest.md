# Sample Manifest — CFPB Complaint Narrative Sample

## Sampling method

Stratified random sample, stratified by **Sub-issue** (7 categories), drawn with a fixed random seed for reproducibility (`random.Random(20260930)`, Python stdlib `random.sample`, one draw per stratum, no replacement). The script is reproducible: given the same `labels.csv`, it produces the same 99 complaint IDs every time.

**Why stratify by Sub-issue, not simple random sampling:** a simple random sample proportional to the population would have given the two largest categories (*Received bad information*, *Trouble with how payments are being handled* — together 70% of all complaints) the overwhelming majority of the sample, leaving the smallest categories (*Co-signer*, population 13; *Keep getting calls*, population 36) with only 0-2 narratives each — not enough to say anything about what those categories actually contain. Stratifying guarantees every sub-issue gets real qualitative representation.

**Allocation rule:** per stratum, `target = max(8, min(18, round(population * 0.10)))`, capped at the stratum's actual population. This gives small categories a floor (8) so they are not reduced to 1-2 narratives, caps large categories at 18 so they do not dominate reading time disproportionately to the benefit of more examples, and otherwise scales with roughly 10% of the category.

| Sub-issue | Population | Sampled | % of category |
|---|---|---|---|
| Received bad information about your loan | 760 | 18 | 2.4% |
| Trouble with how payments are being handled | 606 | 18 | 3.0% |
| Problem with customer service | 245 | 18 | 7.3% |
| Need information about your loan balance or loan terms | 161 | 16 | 9.9% |
| Don't agree with the fees charged | 127 | 13 | 10.2% |
| Keep getting calls about your loan | 36 | 8 | 22.2% |
| Co-signer | 13 | 8 | 61.5% |
| **Total** | **1,948** | **99** | **5.1%** |

**What this sample can and cannot support:** within each stratum, the sampled narratives are a genuine random draw, so patterns found within a stratum are reasonably attributable to that stratum (modulo ordinary sampling variation at these small n). The sample is **not** proportionally representative of the overall population — small strata are deliberately over-sampled relative to their true share — so raw counts across strata in the qualitative findings should never be read as population-level proportions. The quantitative dashboard (published Artifact) uses the full population of 1,948 for all proportions; only the qualitative coding below uses this sample.

Scripts and inputs: sample drawn by an ad hoc script from `labels.csv`; narrative files copied into `sampled-narratives/`; line-numbered and ID-assigned by `scripts/split_excerpts.py --prefix C` into `numbered/` (see `numbered/manifest.json` for the `C{n}` → original-filename mapping).

## Full sample (C1–C99)

| source_id | complaint_id | company | sub_issue | timely_response | company_response |
|---|---|---|---|---|---|
| C1 | 19218391 | Nelnet, Inc. | Don't agree with the fees charged | Yes | Closed with explanation |
| C2 | 19242951 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C3 | 19263590 | MOHELA | Problem with customer service | No | Closed with explanation |
| C4 | 19362555 | Nelnet, Inc. | Don't agree with the fees charged | Yes | Closed with explanation |
| C5 | 19387321 | EdFinancial Services | Received bad information about your loan | Yes | Closed with explanation |
| C6 | 19388851 | Nelnet, Inc. | Don't agree with the fees charged | Yes | Closed with explanation |
| C7 | 19514910 | Nelnet, Inc. | Problem with customer service | Yes | Closed with explanation |
| C8 | 19566709 | SLM CORPORATION | Keep getting calls about your loan | Yes | Closed with non-monetary relief |
| C9 | 19620450 | Navient Solutions, LLC. | Received bad information about your loan | Yes | Closed with explanation |
| C10 | 19684118 | Servicer under contract with Federal Student Aid | Problem with customer service | No | Untimely response |
| C11 | 19691529 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C12 | 19762099 | Navient Solutions, LLC. | Problem with customer service | Yes | Closed with explanation |
| C13 | 19877026 | Nelnet, Inc. | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C14 | 19879407 | Central Research Inc | Trouble with how payments are being handled | Yes | Closed with explanation |
| C15 | 20139764 | Nelnet, Inc. | Trouble with how payments are being handled | Yes | Closed with explanation |
| C16 | 20170419 | SLM CORPORATION | Keep getting calls about your loan | Yes | Closed with non-monetary relief |
| C17 | 20186517 | MOHELA | Problem with customer service | No | Closed with explanation |
| C18 | 20200692 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C19 | 20200848 | IOWA STUDENT LOAN LIQUIDITY CORPORATION | Don't agree with the fees charged | Yes | Closed with explanation |
| C20 | 20490848 | MOHELA | Co-signer | Yes | Closed with explanation |
| C21 | 20569483 | MOHELA | Don't agree with the fees charged | No | Untimely response |
| C22 | 20618216 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C23 | 20689301 | Maximus Federal Services, Inc. | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C24 | 20761108 | MOHELA | Trouble with how payments are being handled | Yes | Closed with explanation |
| C25 | 20796722 | Nelnet, Inc. | Received bad information about your loan | Yes | Closed with explanation |
| C26 | 20818792 | MOHELA | Keep getting calls about your loan | Yes | Closed with explanation |
| C27 | 20891857 | MOHELA | Co-signer | Yes | Closed with explanation |
| C28 | 20997960 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C29 | 21014518 | SLM CORPORATION | Don't agree with the fees charged | Yes | Closed with explanation |
| C30 | 21039607 | MOHELA | Received bad information about your loan | No | Untimely response |
| C31 | 21137741 | Maximus Federal Services, Inc. | Problem with customer service | Yes | Closed with explanation |
| C32 | 21165456 | MOHELA | Received bad information about your loan | Yes | Closed with explanation |
| C33 | 21174122 | Central Research Inc | Don't agree with the fees charged | Yes | Closed with explanation |
| C34 | 21175815 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C35 | 21192282 | Georgia Student Finance Authority | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C36 | 21245214 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C37 | 21383731 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C38 | 21417379 | SLM CORPORATION | Don't agree with the fees charged | Yes | Closed with explanation |
| C39 | 21423969 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C40 | 21489481 | American Student Assistance | Problem with customer service | Yes | Closed with explanation |
| C41 | 21508023 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C42 | 21570319 | Maximus Federal Services, Inc. | Keep getting calls about your loan | Yes | Closed with explanation |
| C43 | 21629587 | Nelnet, Inc. | Problem with customer service | Yes | Closed with explanation |
| C44 | 21650312 | Servicer under contract with Federal Student Aid | Need information about your loan balance or loan terms | No | Untimely response |
| C45 | 21669203 | SOFI TECHNOLOGIES, INC. | Co-signer | Yes | Closed with explanation |
| C46 | 21669348 | College Ave Student Loan Servicing, LLC | Co-signer | Yes | Closed with explanation |
| C47 | 21701776 | MOHELA | Don't agree with the fees charged | No | Closed with explanation |
| C48 | 21707062 | Central Research Inc | Co-signer | Yes | Closed with explanation |
| C49 | 21729515 | MOHELA | Received bad information about your loan | No | Untimely response |
| C50 | 21738688 | Maximus Federal Services, Inc. | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C51 | 21838590 | Nelnet, Inc. | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C52 | 21839595 | SLM CORPORATION | Received bad information about your loan | Yes | Closed with explanation |
| C53 | 21870375 | Navient Solutions, LLC. | Problem with customer service | Yes | Closed with explanation |
| C54 | 21878664 | MOHELA | Don't agree with the fees charged | No | Untimely response |
| C55 | 21891210 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C56 | 21990137 | Maximus Federal Services, Inc. | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C57 | 22084643 | EdFinancial Services | Don't agree with the fees charged | Yes | Closed with explanation |
| C58 | 22150254 | Central Research Inc | Problem with customer service | Yes | Closed with explanation |
| C59 | 22222914 | MOHELA | Received bad information about your loan | Yes | Closed with explanation |
| C60 | 22294111 | Nelnet, Inc. | Keep getting calls about your loan | Yes | Closed with explanation |
| C61 | 22323913 | Central Research Inc | Trouble with how payments are being handled | Yes | Closed with explanation |
| C62 | 22341738 | MOHELA | Problem with customer service | Yes | Closed with explanation |
| C63 | 22355136 | Nelnet, Inc. | Co-signer | Yes | Closed with explanation |
| C64 | 22435951 | Servicer under contract with Federal Student Aid | Need information about your loan balance or loan terms | No | Untimely response |
| C65 | 22537801 | Maximus Federal Services, Inc. | Trouble with how payments are being handled | Yes | Closed with explanation |
| C66 | 22551301 | EdFinancial Services | Problem with customer service | Yes | Closed with explanation |
| C67 | 22553718 | Maximus Federal Services, Inc. | Received bad information about your loan | Yes | Closed with explanation |
| C68 | 22683213 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C69 | 22710332 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C70 | 22846670 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C71 | 23058760 | MOHELA | Received bad information about your loan | Yes | Closed with explanation |
| C72 | 23143344 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C73 | 23272733 | MOHELA | Don't agree with the fees charged | No | Untimely response |
| C74 | 23296311 | MOHELA | Keep getting calls about your loan | Yes | Closed with explanation |
| C75 | 23311497 | MOHELA | Need information about your loan balance or loan terms | No | Untimely response |
| C76 | 23456709 | MOHELA | Received bad information about your loan | Yes | Closed with explanation |
| C77 | 23477473 | Nelnet, Inc. | Problem with customer service | Yes | Closed with explanation |
| C78 | 23542344 | MOHELA | Received bad information about your loan | Yes | Closed with explanation |
| C79 | 23566647 | EdFinancial Services | Received bad information about your loan | Yes | Closed with explanation |
| C80 | 23666174 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C81 | 23692925 | MOHELA | Problem with customer service | No | Untimely response |
| C82 | 23693642 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C83 | 23751534 | SLM CORPORATION | Don't agree with the fees charged | Yes | Closed with explanation |
| C84 | 23772849 | MOHELA | Received bad information about your loan | No | Untimely response |
| C85 | 23795762 | EdFinancial Services | Problem with customer service | Yes | Closed with explanation |
| C86 | 23798703 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C87 | 23800259 | Maximus Federal Services, Inc. | Problem with customer service | Yes | Closed with explanation |
| C88 | 23873423 | MOHELA | Trouble with how payments are being handled | No | Untimely response |
| C89 | 23963809 | MOHELA | Received bad information about your loan | Yes | Closed with explanation |
| C90 | 23967979 | Nelnet, Inc. | Keep getting calls about your loan | Yes | Closed with explanation |
| C91 | 23969903 | MOHELA | Problem with customer service | No | Untimely response |
| C92 | 23989850 | MOHELA | Problem with customer service | Yes | Closed with explanation |
| C93 | 23997587 | MOHELA | Need information about your loan balance or loan terms | Yes | Closed with explanation |
| C94 | 24001127 | SOFI TECHNOLOGIES, INC. | Co-signer | Yes | Closed with explanation |
| C95 | 24026585 | Nelnet, Inc. | Received bad information about your loan | Yes | Closed with explanation |
| C96 | 24129004 | EdFinancial Services | Received bad information about your loan | Yes | Closed with explanation |
| C97 | 24184370 | MOHELA | Received bad information about your loan | No | Untimely response |
| C98 | 24207749 | Nelnet, Inc. | Keep getting calls about your loan | Yes | Closed with explanation |
| C99 | 24242700 | SLM CORPORATION | Co-signer | Yes | Closed with explanation |

