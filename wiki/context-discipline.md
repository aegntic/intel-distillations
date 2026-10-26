# Context Discipline

Managing context state beats prompting skill: clearing sessions, handing off state, scheduling around cache windows, and distilling raw sources into wikis. Deduplicates the Nate Herk four-upgrade material that appears in both source-herk.md and the 26-video brief (v09/v12/v24). Related: [sub-agents-and-parallelism](sub-agents-and-parallelism.md), [definition-of-done](definition-of-done.md), [hermes-ecosystem-intel](hermes-ecosystem-intel.md).

## Synthesis

The operators winning on cost are not prompting better; they are managing context state [source-26-brief Theme 2]. The foundational measurement: one maker measured 96% of spend as re-sending conversation history. The fix costs nothing: /clear between jobs resets the base to zero [v09 1:30, 3:02, 3:49]. Prefer /clear over /compact, and check /context to see what is eating tokens before optimizing anything [iTY8Q449YNQ 16:46, 17:04].

Context rot is real and early: all 18 models Herk references degrade as conversation grows, well before the window fills. His heuristic: start a new session past ~250k of a 1M window [iTY8Q449YNQ 16:46, 17:04]. Hermes shows the same discipline in UI terms: a 0-100 context bar, fresh sessions for big jobs because the harness "trims old context to make room," and pointing the agent back at its own memory files on complex jobs to prevent drift [VdG2o91D_2k 27:30, 28:15].

The session handoff skill makes /clear lossless: before clearing, write a structured handoff (where it started, locked decisions, what shipped, key files, running state, verification status, deferred questions, "pick up here"), then /clear and paste it back. Clean window, zero lost state, and portable across tools [iTY8Q449YNQ 18:22, 20:24].

Cache economics compound the discipline: cron tasks should run at 45-minute-plus intervals because cache misses reprice the whole context at 10x [v09 13:42, 17:06]. This is the direct cost basis for scheduling nightly distillation jobs rather than continuous chatter.

The distillation loop is the highest-leverage instance: compress raw transcripts and notes into a compact wiki and query the wiki, never the raw pile [v14 15:19]. Measured effect: token usage on queries dropped 95% [unverified] [v24 131:19]. This wiki is that tactic applied to itself.

## Key claims

- 96% of spend measured as conversation-history rereads; /clear resets the base to zero [v09 1:30, 3:49].
- /clear over /compact; /context to audit token consumption [iTY8Q449YNQ 17:04].
- New session past ~250k of a 1M window; all tested models degrade before the window fills [iTY8Q449YNQ 16:46].
- Session handoff structure: origin, locked decisions, shipped, key files, running state, verification status, open questions, resume pointer [iTY8Q449YNQ 20:24].
- Cache misses reprice the full context at 10x; schedule cron at 45min+ intervals [v09 13:42, 17:06].
- Wiki distillation dropped query token usage 95% [unverified] [v24 131:19].
- Hermes UI exposes a 0-100 context bar and trims old context on big jobs [VdG2o91D_2k 27:30].
- "Over 200,000 stars on GitHub" for Hermes [unverified, star count is marketing framing] [VdG2o91D_2k 3:02].

## Contradictions

- Micro-optimizing every token (v09) versus running 2.5-hour daily multi-agent content engines on the same subscriptions (v23, v24). Both are real strategies optimizing different constraints: unit cost versus throughput [source-26-brief Theme 2].
- Cheap-stack ideology (Hermes on a 20/month subscription, v04) versus the same operators paying 300/month for a vendor bot just to benchmark it [v04 0:00; source-26-brief, cross-theme].

## Apply to aegntic

- Adopt the structured handoff as the standard between-session artifact for every forge run; make it portable (pasteable into any CLI, not just resumable).
- Schedule all cron jobs at 45-minute-plus spacing; audit current jobs for cache-hostile cadence.
- Treat ~250k of a 1M window as the concrete danger-zone number in AGENTS.md Layer-3 context budgeting.
- Keep this wiki as the only query surface over the harvest corpus; raw condensed files are for provenance checks, never for browsing.

## 2026-10-23 update (bank ingest)

New cost mechanics beyond cache spacing. A Jev-style classifier gated 4,451 routings for 18 cents [unverified], sending ~40% of traffic to a cheap model [f28 12:34]; scheduled routines were capped $10 to $4/week by re-prompting for waste [f28 18:10]; self-pings keep cache warm (~$437/month estimated [unverified]) [f28 29:14]. Memory direction: plain-text maps and card-catalog memory.md beat vector RAG, even at Anthropic scale [f28 24:44][f35 6:08].

## 2026-10-27 update (bank ingest)

The corpus adds a human-side law to token-side discipline: cognitive bandwidth does not parallelize, and parallel agent sessions are what force the switching [f02 1:42]. The named failure mode is guilt while waiting, which opens extra sessions and compounds the problem [f02 3:05]. The operating fix is batch check-ins, about once a day per stream, with recovered attention reinvested into harness autonomy [f02 13:10, 9:20]. Cole Medin predicts near-instant responses will collapse working style into one primary orchestrating session [f02 14:05]. His /goal verdict: a goal statement alone cannot encode how you personally babysit and validate work, so validation lives in the harness [f02 10:52].
