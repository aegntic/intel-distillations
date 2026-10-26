# HOT

The hot cache: what is true right now, the 5 highest-leverage cheapest actions, and what moved since the last distillation. Query this file first; it is regenerated on every wiki refresh. Entry point: [INDEX](INDEX.md).

## Current state (2026-10-27)

The corpus is now an ongoing bank: 33 videos from the 2026-09-01 wiki plus 21 videos and 14 documents from the 2026-10-23 ingest plus 10 sources from the 2026-10-27 ingest, all citation-verified mechanically (142 timestamped citations checked against source text by `bank.py verify`). Three new concept clusters landed: [proactive-and-durable-agents](proactive-and-durable-agents.md) (durable agent plus trigger inside a sandbox [f13 3:04]), [agent-security-baseline](agent-security-baseline.md) (AI phishing at expert efficacy for ~4 cents/email; voice-print authentication defeated; prompt limits are not guardrails [f15 10:22, 3:24; f12 3:14]), and [focus-and-attention-economics](focus-and-attention-economics.md) (cognitive bandwidth does not parallelize; batch check-ins over session juggling [f02 1:42, 13:10]). Pricing anchors widened: a KB-agent offer at 20-40k against the replaced employee's salary [unverified] [f24 15:26] and a flat 1,000/month done-for-you model at ~30 clients [unverified] [f17 0:00]. The session-topology contradiction (fan-out vs one primary session) has a candidate reconciliation, one human session with background workers reviewed in batch, and it is untested. The money theses live in [bank/moves](../bank/moves/immediate.md): 12 moves proposed, each with mechanism, sources, falsifier, and status.

## Top 5 actionable items, ranked by leverage x cheapness

1. **Run the next forge release through the software-factory loop with fan-out evals.** Grill intent, split issues, plan-implement-validate autonomously, one batch review in staging [f02 11:57, 10:24]; one brief fanned across three models, cherry-picked [f64 15:34]. The harness becomes the client demo. Log ids mv-007, mv-006.
2. **Adopt batch check-ins and backfill three playbook repos.** One daily review slot per agent stream, no mid-day peeking for a week [f02 13:10]; SOP-to-skills, monitoring, and distillation become forkable repos with evals [f05 3:08, 42:45]. Log ids mv-010, mv-009.
3. **Deposit-test the KB-agent offer beside SOP-to-skills.** Flagship stays (10-25k plus 1-2k/month [GkHwnQdoDpM 35:43]); add the KB-agent one-pager plus a 15-minute mock-data demo and book 5 calls from the existing network. The 20-40k anchor is [unverified]; deposits decide [f24 15:26]. Log id mv-004.
4. **Run the classifier-gating A/B on one cron loop.** Jev-style routing with a 2-week cost comparison before any rollout [f28 12:34]. Log id mv-002.
5. **Security posture after the 2026-10-27 review: already adequate for the video pipeline.** The harvest loop is public-data-in/markdown-out with no PII by rule; the box runs no PHP and no web servers, so mv-001 closed not-applicable per its own falsifier; spend rails (mv-008) wait for the first spend-holding agent. Remaining hygiene: confirm distiller subagents hold no push rights and the verify gate stays blocking on the sweep's auto-commit [mv-003, re-scoped].

**Carried from 09-02, still open:** council-of-skills personas [iTY8Q449YNQ 2:50], the three-creator wave [source-roster], and the one-documentary-domain proof [NAB9PyN2-3E 57:21]. Nothing has acted on them yet; they stay queued, not deleted.

## What changed since last distillation (2026-09-02 bank refresh)

- The wiki became an ongoing bank: append-only ledger, dated synthesis drafts under `bank/harvests/`, and a move log with falsifiers and status lifecycle. Contract: `bank/SCHEMA.md`. The 2026-10-23 ingest brought 109 verified citations across 35 files; the 2026-10-27 ingest brought 33 across 10.
- Three new concept files: [proactive-and-durable-agents](proactive-and-durable-agents.md), [agent-security-baseline](agent-security-baseline.md), [focus-and-attention-economics](focus-and-attention-economics.md). Fourteen concept files gained dated update blocks from the two new harvests.
- Eight contradictions recorded, both sides cited, including parallelism vs the focus tax [v12 21:47 vs f12 9:20], a 10x pricing-anchor spread [GkHwnQdoDpM 35:43 vs f24 15:26 vs f17 1:02], and harness build-vs-buy [v04 10:27 vs f17 12:26]. Two older positions revised: avatar-safety now reads "the slop category" [f06 56:04], and 80%-autonomy claims are scoped as task-type-dependent [f13 0:45 vs f02 5:21].
- New this cycle and verified nowhere: classifier gating at 18 cents per 4,451 routings [f28 12:34], $437/month cache-warming estimate [f28 29:14], $570K ARR [f17 0:00], the 20-40k KB anchor [f24 15:26]. All [unverified] until our own measurements or deposits exist.

## Open questions

- Does classifier gating survive our workloads once misroute rework is counted [f28 12:34]? Needs the 2-week A/B [mv-002].
- Is the KB-agent 20-40k anchor reachable for our buyer pool, or does the SOP wedge at 10-25k convert better? Deposit tests decide [mv-004].
- Does near-instant model response actually collapse multi-session juggling into one primary session [f02 14:05], or do four-screen factory multi-tables win [f06 1:18:08]? Task-type split is the working hypothesis.
- Is Meta's MCI pause permanent or a cooling-off period [f08 8:40]? What is the real false-block rate of hard card caps on our own fleet [f02 3:47]?
- Carried unresolved from 09-02: does the AI-transparency label cost nothing [gXaF4t4B4ss 16:30]; are Herk's study figures accurate as stated [source-herk]; which tier-2 creator converts first; does the 120-domain grid hold ranking discipline [v21 4:44 vs 11:26]; can a verification-gated pipeline clear sleep-niche RPM of $30-40 [unverified] [NAB9PyN2-3E 1:12:48]?
