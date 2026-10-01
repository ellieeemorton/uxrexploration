# Excerpt ID schemes

Every excerpt gets a stable ID that traces back to an exact, re-checkable location in a source file. The format depends on source type because "a line" and "a cell" are different units of traceability — forcing both into one scheme would make one of them fake precision.

## Transcripts (interview/session recordings transcribed to text)

`T{n}-L{line}`

- `n` — the transcript's position in the sorted file list, assigned once by `scripts/split_excerpts.py` and recorded in `manifest.json`. Don't reassign or renumber by hand; the manifest is the source of truth for which file `T3` is.
- `line` — the 1-indexed line number, in the *original* source file, where the excerpt begins. `split_excerpts.py` numbers every line so this is unambiguous even if your excerpt spans several lines.

One transcript file = one participant. If a session has two speakers (moderator + participant), the participant is still the unit of `T{n}` — only cite excerpts that are the participant speaking, not the moderator's question (the moderator's question is recorded separately as `preceding_question` when it's a leading-question flag, see `evidence-tagging.md`).

**Why line-anchored, not turn-anchored:** transcript formatting varies too much (timestamps, speaker labels, paragraph vs. turn-per-line) to number "turns" deterministically across every format a researcher might hand in. A line number is unambiguous and always re-checkable by a script with zero parsing of transcript structure.

### One-file-per-unit sources that aren't interview transcripts

The same `{prefix}{n}-L{line}` scheme applies to any source where one file is one unit of analysis and the unit's own internal line breaks are meaningful — not just moderated interviews. A folder of open-ended complaint narratives, one `.txt` file per complaint, works identically: `split_excerpts.py --prefix C` (instead of the default `T`) numbers them `C1, C2, ...` so a reader can tell at a glance, across two different studies' files, that `C14-L3` is a complaint narrative and `T4-L12` is an interview transcript — useful once more than one study's `excerpts.jsonl` might be open at the same time, even though IDs only need to be unique *within* one study's own file. Pick a prefix that names the source type (`C` for complaint, `R` is already taken by the tabular scheme below) and record it in that study's own notes.

## Tabular open-ended responses (CSV export of a survey, diary study, etc.)

`R{row}-Q{question}`

- `row` — the literal spreadsheet row number, including the header row as row 1 (so the first respondent's data is row 2, matching what you'd see if you opened the file in a spreadsheet app).
- `question` — a short slug of the column header (the question text), e.g. `Q3` or `Q-frequency` — whichever `split_excerpts.py`'s manifest recorded for that column.

Each row is one respondent — `R{row}` is also that respondent's participant ID (e.g., the excerpt `R12-Q3` belongs to participant `R12`).

When citing a tabular excerpt anywhere a human will read it (report, checkpoint summary), also give the literal cell address (e.g., "row 12, column C") so the researcher can jump straight to it in their spreadsheet tool without re-deriving row/column from the slug.

**Why row-anchored instead of reusing the transcript line scheme:** a CSV row *is* the natural unit of "one respondent's answer to one question" — there's no meaningful sub-row line number, and forcing one would imply a precision the data doesn't have. If you have multiple tabular files in one study, disambiguate manually (e.g., `R12-Q3-diary2`) rather than overloading the scheme further; this is rare enough not to warrant a fourth ID format.

## Non-negotiable: participant_id is a separate field

Store `participant_id` (`T3`, `R12`, …) as its own field in `excerpts.jsonl`, distinct from the excerpt ID. Theme participant counts (`theme-building.md`) are computed by counting **distinct `participant_id` values**, never by counting excerpt IDs — a participant with ten quotes in a theme is still one participant.
