# Evidence tagging

Every excerpt gets exactly one evidence-type tag, exactly one relevance tag, and an optional leading-question flag. Store all three as fields on the excerpt in `excerpts.jsonl` — tags travel with the excerpt for the life of the synthesis, they aren't a one-time note.

## Evidence type (pick the one that best describes what kind of claim the excerpt actually is)

| Tag | Definition | Example |
|---|---|---|
| `observed_behavior` | The participant did something you (or the moderator) directly watched or logged during the session — a task attempt, a click, a moment of hesitation narrated live. | "Okay, I'm clicking on... hm, this button isn't doing anything." |
| `self_reported_past_behavior` | The participant describes something they actually did, outside this session. Weaker than observed: subject to memory error and social desirability. | "Last time I applied for a loan, I gave up after the third form." |
| `stated_attitude` | An opinion, feeling, or preference — not a report of an action. | "I hate forms that make me re-enter information." |
| `hypothetical_intent` | A prediction about future or hypothetical behavior. The weakest tag for predicting what users will actually do. | "I'd probably just call the bank instead." |

**Why this matters downstream:** a claim phrased as "users do X" may only be backed by `observed_behavior`. If the only support for a behavioral claim is `hypothetical_intent` or `stated_attitude`, the claim must be reworded ("users say they would X," not "users do X") — this is one of the checks the verification subagent runs (`verification-subagent.md`), so getting the tag right here saves a round-trip.

## Relevance (pick one)

| Tag | Definition |
|---|---|
| `on_topic` | Directly addresses a question or hypothesis in the brief. |
| `adjacent` | Related to the topic area but doesn't answer a brief question directly — may surface an unplanned insight, but isn't automatically strong evidence for the exact question asked. |
| `off_topic` | Unrelated to the research, including venting about the product/situation itself that isn't about the research questions (e.g., frustration about the loan being denied, not about the application experience being tested). |

Only `on_topic` and `adjacent` excerpts feed theme-building. `off_topic` excerpts stay in `excerpts.jsonl` for audit and are never cited in the report as if they were on-topic — but they are never deleted either, so a researcher can always check what got excluded and why.

## Leading-question flag

Set `leading_question_flag: true` when the excerpt is a direct answer to a preceding moderator/interviewer question that supplies the expected answer or an evaluative frame — e.g. "Did that feel frustrating?", "So you'd want it to be faster, right?". Record the exact preceding question in a `preceding_question` field.

This flag doesn't exclude the excerpt automatically — a leading question doesn't always produce an unreliable answer, and excluding by default would let the moderator's phrasing quietly shrink the sample. Instead, the flag travels with the excerpt as data: bias review (`bias-review.md`) must address every flagged excerpt that ended up cited in a theme, and if the report cites one, the report must say the answer followed a leading question so the reader can weigh it themselves.

**Why flag rather than judge here:** tagging happens per-excerpt, before themes exist — you can't yet know whether a flagged excerpt will end up load-bearing for a theme's participant count. Deferring the judgment call to bias review (step 5), once themes exist, means the call is made with full context instead of guessed at in isolation.
