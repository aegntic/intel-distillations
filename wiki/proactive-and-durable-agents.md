# Proactive and Durable Agents

The 10-23 cluster's core thesis: a proactive agent is a durable agent plus a trigger inside a sandbox; it works, then waits [f13 3:04]. This file holds the persistence, trigger, and maturity-ladder material that upgrades parallelism from isolated sessions to durable teams. Related: [sub-agents-and-parallelism](sub-agents-and-parallelism.md), [definition-of-done](definition-of-done.md), [context-discipline](context-discipline.md).

## Synthesis

Durable agents persist state through failures and clients, resume from checkpoints, share one application-state object, and treat deploys as non-replayable gated tasks [f02 30:21][f02 4:43]. They survive process kill and machine restart; tool sets flip live mid-session (read-only states swap without a rebuild) [f02 18:29][f02 22:08]. Pi Durable adds the durable/proactive layer Hermes lacks publicly: shared device state, resumable tasks, live tool swaps; still experimental pre-V1, and even its promoter withholds production use until V1 [f02 25:32].

Triggers are the cheap half. Jev, a JSON-programmed classifier, gates triggers and dangerous bash at near-zero cost; a bash-guard blocks rm -rf until a live toggle allows it [f02 21:19][f02 4:53][f53 14:31]. Grok Bot ships the same pattern as shareable role bots: one bot per job with its own memory, computer, and context, owner-managed skills pushed live to teammates, running 24h routines (metrics bot drops the bottom 3 stickers, designer bot drafts replacements, deploy bot ships) after ~30 minutes of human tuning per flow [f64 18:52][f64 12:37][f64 41:43].

The maturity metric is moving work from human-in-loop to near-loop to out-of-loop [f13 3:04][f02 3:08][f13 0:36]. The KPI: "how many agents are doing useful work for you right now"; move work from in-loop to out-of-loop [f02 34:10].

## Key claims

- Proactive = durable agent + trigger + sandbox; proactive agents "work for you, then wait" [f13 3:04][f02 3:08].
- Durable agents survive process kill and machine restart from checkpoints [f02 30:21].
- Deploys are non-replayable one-shot tasks behind an approval gate ("human near the loop") [f02 4:43][f02 10:44].
- A classifier bash-guard blocks rm -rf until a live toggle allows it [f02 21:19].
- Jev gates triggers and dangerous bash at near-zero cost [f02 4:53][f53 14:31].
- The 24h Grok Bot PMF loop needed ~30 minutes of human tuning per bot flow first [f64 41:43].
- Pi Durable is experimental; no production use until V1, per its own promoter [f02 25:32].

## Contradictions

- Autonomy magnitude: the wiki holds the human is the finish line with approval gates on anything client-facing; this corpus claims agents can do 80%+ of current work autonomously [f13 0:45] and demos 24h unprompted loops [f64 39:12]. Direction agrees, magnitude contested.
- Pi Durable is pitched as fleet infrastructure while its own promoter withholds production use until stable V1 [f02 25:32].

## Apply to aegntic

- Stand up the signal-curator demo on the always-on box: cron sweep, dedupe, Jev-style rank, 7 cards per tick [f13 16:53][f13 14:42].
- Wrap the nightly digest cron's classification behind a Jev-style JSON classifier and log both costs before fleet-wide rollout [f28 12:34].
- Track the KPI weekly: count agents doing useful work out-of-loop, not sessions open [f02 34:10].
