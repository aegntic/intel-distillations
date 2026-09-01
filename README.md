# intel-distillations

Curated intelligence distillations produced by the aegntic studio pipeline:
video harvests, creator rosters, and agent-market analyses. Companion data
to [cognitive-os](https://github.com/aegntic/cognitive-os).

## Method

Sources are harvested with
[tab-harvest](https://github.com/aegntic/tab-harvest) (CDP tab extraction,
full transcripts), then distilled under a fixed contract: concepts with
timestamps, concrete numbers, verbatim quotes, honest [unverified] tags on
content-marketing claims. No invented metrics.

## The wiki (query-first)

`wiki/` is the knowledge base distilled from everything below it: one file
per CONCEPT, not per source. Query the wiki, never the raw pile. Start at
`wiki/HOT.md` (current state + top 5 actions, refreshed every distillation)
or `wiki/INDEX.md` (one line per topic + query recipes).

The loop: harvest (tab-harvest pulls transcripts) -> distill (source docs
with timestamps, numbers, [unverified] tags) -> wiki update (merge into
topic files, deduplicate, note contradictions) -> HOT.md refresh (re-rank
the top 5, record what changed). Raw files stay for provenance; the wiki is
the only query surface.

## Contents

- `wiki/` - the query-first knowledge base: 10 topic files, INDEX, HOT.
- `harvest-2026-09-01/` - 26-video YouTube session (9.1M combined views,
  20.1h watch time). `distilled-index.md` mirrors the interactive brief in
  cognitive-os `00_Showcase/agent-brief/`; `condensed/` holds the per-video
  analyses (numbers, tools, strided transcript samples).
- `deep-dives/` - single-topic distillations:
  - `six-video-hermes-agents-niches.md` - Hermes Agent business playbooks,
    the Runable "agents that finish" thesis, 61 faceless niches ranked
    against agent tooling + a 120-domain portfolio.
  - `nate-herk-claude-code-money.md` - the four-upgrade Claude Code
    operating method (roast council, verification loop, context discipline,
    sub-agents + goal gate).
- `creator-roster/` - outreach-ready creator contacts with alignment
  evidence, tiered by Hermes/aegntic coverage.

## Provenance

Every file carries source URLs and timestamps back to the original videos.
Claims flagged [unverified] were not independently checked and usually
smell like marketing.

License: MIT
