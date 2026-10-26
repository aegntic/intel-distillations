# Validation Tactics

How the corpus actually validates: paid deposits, scraped demand signals, public budgeted experiments, and adversarial red-teaming before building. Related: [agent-business-models](agent-business-models.md), [definition-of-done](definition-of-done.md), [sub-agents-and-parallelism](sub-agents-and-parallelism.md).

## Synthesis

Nobody in this corpus validates with waitlists. The strongest sequence is Robbie's: give the agent a 100 dollar budget and a 90-day deadline, fail at the planned business (Fiverr gigs, new account, no reviews, no distribution [l0Vqm0ZIySc 7:20]), then let the agent scrape ~200 "I want a Ron" comments from the viral TikTok (via Apify) and propose hosting other people's agents [l0Vqm0ZIySc 10:20-11:13]. Validation was a 10 dollar deposit via Stan that filtered tire-kickers: 617 pre-orders (~$6,170) before anything was built, and 270 of 617 converted to the community, a ~44% close rate [l0Vqm0ZIySc 14:08, 18:36]. Monetization: $29/month founding rate; day 13 at $8,374 MRR (~$100k annualized), self-reported [unverified], against ~$2,500/month COGS (four Contabo servers ~600 plus ~2,000 inference) [l0Vqm0ZIySc 17:35, 19:11, 28:18-28:48].

The distribution insight underneath: "200 targeted views are better than 2 million untargeted views"; follower count no longer matters on TikTok, interest media replaced social media [l0Vqm0ZIySc 27:20, 27:50]. Koerner's summary: "Step one, do cool things. Step two, post about it... post your crap" [l0Vqm0ZIySc 26:20].

Pre-build red-teaming (Herk's roast pattern, deduplicated from two source docs): before approving any plan, spin up adversarial personas: contrarian (fatal flaws), expansionist (biggest upside), first-principles thinker, deep researcher (market data plus competitor pricing), buyer (role-plays the customer, says whether they would pay), judge (green light / reshape / kill plus the cheapest 48-hour test) [iTY8Q449YNQ 2:50]. The council-red-team entry in the steal list: spin up adversarial personas to kill weak ideas before building [v12 3:07].

Offer-level validation: run the four-leg filter (buyer, pain, flowing budget, articulable agent advantage) and kill deals that fail any leg [GkHwnQdoDpM 1:03]. Niche-level validation: packaging experiments beat niche tests, "post 15 videos and every single video should have a little bit of something different" to find the winning packaging fast [NAB9PyN2-3E 41:16]. Trading discipline generalizes: 99% of backtests fall apart, so journal and forward-test for 3 months before trusting any automated system [v17 10:36, 19:50].

## Key claims

- 617 pre-orders x $10 deposit (~$6,170) before build; 270 converted at ~44% [l0Vqm0ZIySc 13:39, 18:36].
- $8,374 MRR at day 13 (~$100k annualized) [unverified, self-reported]; ~$2,500/month COGS [l0Vqm0ZIySc 19:11, 28:18].
- Abuse-case sizing discovered post-launch: 125 sub-agents in 5 days, 1.3M tokens in 48 hours from one user [l0Vqm0ZIySc 29:22].
- Roast council personas: contrarian, expansionist, first-principles, deep researcher, buyer, judge with cheapest-48-hour-test output [iTY8Q449YNQ 2:50].
- Trigger-based cold email: one line referencing a real trigger event, no pitch, 3% reply rate on mockup outreach [v16 5:39; v13 1:13].
- Forward-test rule: expect backtests to lie; 3 months of journaling before trusting automation [v17 10:36, 19:50].
- A 22-hour Grok trading bot on 10K produced 6 trades, 3 wins, 3 losses, +11.60 total; the honest gap between champion discretionary skill and autonomous bots [v17 17:04].

## Contradictions

- The plan lost, the pivot won: the Fiverr plan produced nothing while the scraped-comment pivot built the business; validation attaches to demand signals, not to your plan [l0Vqm0ZIySc 7:20 vs 11:13].
- "3x more money in 30 days" headline on the Herk video is unverified marketing; the four upgrades behind it cite real studies loosely [source-herk, gaps].
- 200 targeted views beat 2M untargeted, yet the same ecosystem chases volume plays (hundreds of ad variants [v01 7:38]; 1,000 microsites [v21]); intent and volume strategies serve different business shapes [source-26-brief, cross-theme].

## Apply to aegntic

- Charge a small deposit at every validation step for studio offerings; free signups are not signal.
- Scrape our own comment sections and community threads for demand before building any new forge feature; the highest-signal market research in the corpus was Apify over "I want one" comments.
- Upgrade council-of-skills with Herk's missing personas: a buyer role-play and a forced "cheapest 48-hour test" output.
- Run one public, budgeted, deadline-bound agent experiment and post every day of it; the documentation asset outlives the experiment.

## 2026-10-23 update (bank ingest)

Intake discipline upgrades. Score information hype/fact/signal before acting: a fact you cannot act on is not signal [f13 5:19]. Adopt Galloway's falsifiable-test habit for macro claims: state what would disprove the thesis (sustained 20% unemployment) before believing either the boom or the doom case [f42 10:08]. Launch-pattern proof: First Index started from one Friday tweet, price and delivery channel stated, no site, DM to start [f17 1:02]. Corroborate self-reported revenue ($570K ARR) before this bank ever cites it [f17 0:00].

## 2026-10-27 update (bank ingest)

The rough first version is a validation tactic, not just a build tactic: build the ugly working artifact to extract requirements a stakeholder could not articulate, then let them react to it [f03 7:42, 8:24]. It pairs with a scope control: with identical tools, one person starts 15 projects in a month and quits each when work gets awkward, the other stays on one customer problem; sustained focus is underweighted in AI conversations [f03 11:44, 9:39]. Anti-goal for the council checklist: AI can make distraction look productive, many prototypes and three plans by 5pm, none far enough to matter [f03 12:31].
