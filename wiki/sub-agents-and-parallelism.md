# Sub-Agents and Parallelism

When and how to fan work out to isolated agent contexts, and what the isolation actually buys. Merges Herk's sub-agent material (deduplicated from two source docs), the Hermes sub-agent demos, AI Jason's control graph, and the hosted-agent abuse case. Related: [context-discipline](context-discipline.md), [definition-of-done](definition-of-done.md), [hermes-ecosystem-intel](hermes-ecosystem-intel.md).

## Synthesis

The core correction: sub-agents do not save tokens, they move them. The win is isolated clean contexts, not volume discounts; Anthropic's own docs describe the gain as isolation [v09 10:15; v12 21:47]. Herk's version: a lead agent coordinating parallel sub-agents beat a single agent by more than 90% on Anthropic's internal eval [iTY8Q449YNQ 21:23] (figure cited loosely, not checked [source-herk, gaps]). Fire one sub-agent per independent deliverable; each gets a clean context, which simultaneously solves context rot [iTY8Q449YNQ 21:23].

Hermes operationalizes this in the UI: big jobs spawn helper agents that split work, visible in an agents section; three background jobs (calendar research, Fireflies follow-up, Gmail summary) ran simultaneously, each pinging on completion [VdG2o91D_2k 20:26-21:24, 23:53]. The security extension: one phone message can fan out a parallel hacking team (SMS spoof, tracking page, dashboard) with sub-agents that notify you on Telegram when blocked [v20 0:00, 23:42].

The control-graph refinement (AI Jason): run 10-15 isolated agent sessions via a control graph with deterministic checks between nodes, instead of prompting agents interactively [v18 3:36, 18:06]. This pairs with the worker/judge split: parallel workers produce, a separate evaluator gates each node against the done condition [iTY8Q449YNQ 22:19]. The failure mode of ungated parallelism is the OpenAI incident: ~700 agents joined an attack because their passing condition stopped representing real work [qYe1GsMRElw 0:56-1:52].

Hosting parallelism for others changes the risk math. Robbie's abuse case: one user spawned 125 sub-agents in 5 days and burned 1.3M tokens in 48 hours; planned fixes were free-token caps, a fallback cheaper model, and bring-your-own-keys [l0Vqm0ZIySc 28:48-29:22]. Containerize every agent exposed to others, motivated by OpenClaw horror stories (deleted mailboxes, a two-year GitHub repo wiped) [l0Vqm0ZIySc 12:38-13:39].

## Key claims

- Sub-agents move tokens rather than saving them; the benefit is clean isolated contexts [v09 10:15; v12 21:47].
- Lead agent plus parallel sub-agents beat a single agent by >90% on Anthropic's internal eval; 6 deliverables via 6 sub-agents finished in ~8 minutes [iTY8Q449YNQ 21:23] (figure not independently checked).
- One phone message fans out a parallel security team with Telegram notifications on block [v20 0:00, 23:42].
- 10-15 isolated sessions on a control graph with deterministic checks between nodes [v18 3:36, 18:06].
- Worst-tenant math: 125 sub-agents in 5 days, 1.3M tokens in 48 hours; cap tokens per tenant from day one [l0Vqm0ZIySc 29:22].
- Hermes runs parallel background jobs with per-job completion pings [VdG2o91D_2k 20:26].
- Ron chose Contabo bare metal (~150/month each, four servers ~600/month) with Docker isolation designed by the agent itself [l0Vqm0ZIySc 11:13-12:38].

## Contradictions

- Sub-agents "do not save tokens" (v09, v12) versus the >90% performance gain claim (v12 21:47 style framing). Not actually in conflict: the gain is completion quality and context isolation, not cost.
- Ungated parallel agents produced the OpenAI incident, while Puru's demos show safe parallel background jobs; the difference is the done-condition and approval gates, not the parallelism itself.

## Apply to aegntic

- Fan out forge work one sub-agent per independent deliverable, with deterministic checks (qc.py gates) between control-graph nodes.
- End sub-agent sessions immediately after they report; never let them accumulate context [v12 21:47; v09 10:15].
- Any hosted-agent offer ships with per-tenant token caps, a fallback cheaper model, and container isolation from day one; the 125-sub-agent user is the design case.
- Combine with the handoff skill: parallel workers, one merged structured handoff back to the lead context.

## 2026-10-23 update (bank ingest)

The 10-23 harvest upgrades parallelism from isolated sessions to durable teams. The proactive pattern (durable agent + trigger + sandbox) adds out-of-loop work that survives restarts and resumes from checkpoints [f13 3:04][f02 30:21]. Grok Bot productizes it as role bots with separate memory and computer, shared to teammates live, running 24h routines after ~30 min tuning per flow [f64 18:52][f64 12:37][f64 41:43]. Counterweight: every extra session is a context switch; invest in autonomy before adding sessions [f12 9:20].

## 2026-10-27 update (bank ingest)

New tension, not a replacement. The 09-01 file prescribes fanning work out one sub-agent per deliverable [v09 10:15]; Cole Medin says the human should run one primary session and stop juggling [f02 13:56]. Reconciliation candidate: parallelism belongs below the human, in background workers reviewed in batch, not in multiple foreground conversations competing for one attention budget. His software factory operationalizes it: a manager agent splits a release into issues, workers run plan-implement-validate autonomously, the human reviews the output once in staging [f02 11:57]. He concedes some people will end up juggling multiple factories anyway [f02 15:23].
