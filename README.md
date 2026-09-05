# intel-distillations

Agent-economy advice lives in hour-long YouTube videos. The useful parts are
numbers, tactics, and contradictions, and they arrive buried in talk. This
repo is the talk distilled out: 33 videos (a 26-video session totaling
9,112,381 source views and 20.1 hours of watch time, plus two deep dives)
compressed into timestamped source docs, then merged into a query-first wiki
with one file per concept, not per source. You query the wiki; the raw files
stay for provenance.

Companion data to [cognitive-os](https://github.com/aegntic/cognitive-os).

## What the output looks like

Real excerpts, unedited. First, a per-video source doc (every claim carries a
timestamp; creator-stated marketing numbers get tagged):

    Quoting agents outsell chatbots. A VIN-decoding tire-and-brake quoter
    sold for 10-20K up front plus 1-2K/month, because it kills a 30-minute
    manual pricing chore every call (v07 31:25).
    ... a before/after photo mockup of the prospect's own parking lot pulled
    a 3% reply rate and 150K+ of quotes in two weeks [unverified] (v13 3:25).

Second, the wiki those docs merge into. Query recipes from `wiki/INDEX.md`:

    "Token spend is insane"        -> context-discipline.md
                                      (check the 96%-rereads claim, v09 3:02)
    "What do I charge?"            -> agent-business-models.md
                                      (anchors at 10-25k setup + 1-2k/month)
    "What do I do RIGHT NOW?"      -> HOT.md, always

`wiki/HOT.md` holds the current state, the top 5 ranked actions, what changed
since the last distillation, and open questions the corpus has not answered.

## Usage

One line, no install (it is a data repo, not a tool):

    git clone https://github.com/aegntic/intel-distillations && less intel-distillations/wiki/HOT.md

## Method

Sources are harvested with
[tab-harvest](https://github.com/aegntic/tab-harvest) (CDP tab extraction,
full transcripts), then distilled under a fixed contract: concepts with
timestamps, concrete numbers, verbatim quotes, honest [unverified] tags on
content-marketing claims. No invented metrics.

The loop: harvest (tab-harvest pulls transcripts) -> distill (source docs
with timestamps, numbers, [unverified] tags) -> wiki update (merge into
topic files, deduplicate, note contradictions) -> HOT.md refresh (re-rank
the top 5, record what changed). Raw files stay for provenance; the wiki is
the only query surface.

## Contents

- `wiki/` - the query-first knowledge base: 10 topic files, INDEX, HOT.
- `harvest-2026-09-01/` - 26-video YouTube session (9.1M combined source
  views, 20.1h watch time). `distilled-index.md` mirrors the interactive
  brief in cognitive-os `00_Showcase/agent-brief/`; `condensed/` holds the
  per-video analyses (numbers, tools, strided transcript samples).
- `deep-dives/` - single-topic distillations:
  - `six-video-hermes-agents-niches.md` - Hermes Agent business playbooks,
    the Runable "agents that finish" thesis, 61 faceless niches ranked
    against agent tooling + a 120-domain portfolio.
  - `nate-herk-claude-code-money.md` - the four-upgrade Claude Code
    operating method (roast council, verification loop, context discipline,
    sub-agents + goal gate).
- `creator-roster/` - outreach-ready creator contacts (public handles only)
  with alignment evidence, tiered by Hermes/aegntic coverage.

## Provenance

Every file carries source URLs and timestamps back to the original videos.
Claims flagged [unverified] were not independently checked and usually
smell like marketing.

## Limits

- This is a snapshot, not a feed. Everything was distilled 2026-09-01/02;
  it rots until the loop runs again. Refresh cadence is manual.
- All revenue and performance numbers are creator-stated. None were
  audited. That is what the [unverified] tag means; trust directions, not
  digits.
- Small, biased corpus: 33 videos plus roster research, English-language,
  YouTube-only, weighted toward people who make money talking about making
  money.
- The distillation is opinionated. Contradictions between sources are
  recorded, not adjudicated.
- No tooling ships here. The harvesting tool is
  [tab-harvest](https://github.com/aegntic/tab-harvest); this repo is the
  output of running it, not the thing you run.
- The creator roster is outreach planning material built from public
  information. No private contact data.

## License

MIT. See [LICENSE](LICENSE).
