# Bank schema — how this knowledge bank adds to itself

The bank is the ongoing layer of intel-distillations. `wiki/` stays the
concept layer (one file per concept). The bank adds time: an append-only
ledger of what was ingested, dated synthesis drafts, and a money-move log
where every suggestion carries sources, a falsifier, and a status.

House rules (inherited from the wiki): no em-dashes; creator/vendor-stated
numbers keep their [unverified] tag; every claim cites its source; no
invented market sizes, ever.

## 1. Layout

    bank.py                  CLI: ingest | verify | stats
    bank/ledger.jsonl        append-only ingest log (one JSON object per line)
    bank/harvests/<date>.md  per-harvest synthesis draft (see section 3)
    bank/moves/immediate.md  ranked now-moves (regenerated on refresh)
    bank/moves/strategic.md  bigger-picture theses, each with a falsifier
    bank/moves/move-log.jsonl every move ever made, with status lifecycle
    wiki/                    concept layer (existing, unchanged role)
    wiki/HOT.md              current state + top actions (regenerated on refresh)

## 2. Citations

Each harvest draft defines its own citation namespace in a mapping table:

    | f00 | 00-cheating-gold-digger.md |

Claims then cite as [f00 3:25] (or [f07 1:31:22] for long videos). The
`fNN` must exist in that file's table and the timestamp must exist in the
mapped file's text — `bank.py verify` checks both mechanically. A citation
that fails verification is treated as fabricated and removed.

## 3. Ingest contract (run after every tab harvest)

1. `python3 bank.py ingest <harvest-dir>` — appends to the ledger, stubs the draft.
2. Write the synthesis draft `bank/harvests/<date>.md`: citation map, stats,
   new signals, per-concept update blocks (`### update: <concept-name>`),
   contradictions vs existing wiki, candidate moves (JSON), open questions.
3. Apply accepted update blocks to `wiki/*.md` files (append with date header).
4. Refresh `bank/moves/*` and append new rows to `move-log.jsonl`.
5. Update `wiki/HOT.md`: current state, top 5 actions, what changed, open questions.
6. `python3 bank.py verify` — must PASS before commit.
7. Commit as `bank: ingest <date> — N sources, M moves` and push.

## 4. Move rules

- Every move carries: mechanism (why money results), sources (bank citations),
  falsifier (what would disprove it), effort, first_step.
- Status lifecycle: `proposed` -> `acted` | `dead` | `superseded`. Log the
  transition date in the row. No move is ever silently deleted.
- Immediate = days, executable this week with assets we already have.
  Strategic = quarters; needs a falsifier and a review date.
- Vendor/creator revenue claims may motivate a move but never appear as our
  own expected numbers. Expected outcomes are written as hypotheses with a
  test, not projections.

## 5. Who runs this

Any agent in the fleet that completes a tab harvest runs the ingest contract
(see the tab-harvest skill, fleet notes). The github-d profile carries a
weekly sweep cron that ingests un-ingested `~/harvests/*` dirs and reports
one line. Humans redirect; the bank accumulates.
