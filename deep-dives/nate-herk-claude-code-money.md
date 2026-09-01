# Distilled: 'I asked Claude Code to make me as much money as possible'

- source: https://www.youtube.com/watch?v=iTY8Q449YNQ
- channel: Nate Herk | 28:12 | 201,261 views | uploaded 2026-06-25 | transcript: auto-captions via yt-dlp
- one-line: four 'upgrades' that turn Claude Code from a yes-man into a business partner: adversarial review, self-verification, context discipline, parallel sub-agents + external goal loop.

## Concepts worth keeping

1. **Sycophancy is the default failure mode** [0:00, 1:53] - models are tuned to make you *feel* productive, not to make you money. The ELEPHANT study: models fail to push back on framing ~88% of the time (humans ~60%); MIT/Penn State: personalization + memory make it *worse* over a long conversation.
2. **Roast pattern (adversarial council)** [2:50] - before approving any plan, spin up personas that attack it: contrarian (fatal flaws), expansionist (biggest upside), first-principles thinker, deep researcher (pulls real market data + competitor pricing), buyer (role-plays the customer, says if they'd pay), judge (verdict: green light / reshape / kill + cheapest 48-hour test).
3. **Verification loop (factory-test metaphor)** [8:00, 10:57] - 'finished' and 'working' are different things; NYU study: ~40% of ~1,600 Copilot-generated programs had security vulnerabilities. Fix: never trust the first render - verify with real browser automation (Playwright screenshots at both viewports), iterate until a definition-of-done, then STRESS TEST: submit forms in multiple passes with malformed emails, weird whitespace, dropdown permutations; count pass/reject and surface non-blocking notes (e.g. no duplicate-email guard, lenient validation).
4. **Context rot** [16:46, 17:04] - all 18 tested models degrade as conversation length grows, well before the window fills; his heuristic: new session past ~250k of a 1M window; /context to see what's eating tokens; /clear over /compact.
5. **Session handoff skill** [18:22, 20:24] - before clearing: write a structured handoff (where it started, locked decisions, what shipped, key files, running state, verification status, deferred/open questions, 'pick up here'), then /clear and paste it back - clean window, zero lost state; portable across tools (he pastes into Codex too).
6. **Sub-agents beat single-threading** [21:23] - Anthropic's own test: lead agent coordinating parallel sub-agents beat a single agent by >90% on their internal eval. Each sub-agent gets its own clean context (also solves context rot). Fire one per independent deliverable.
7. **/goal pattern: separate worker and judge** [22:19] - set an objective finish line + a SECOND model/evaluator that checks every turn whether done==true; the worker never grades its own homework. Define done objectively (all 6 files exist and are non-empty, >=6 competitors, 25 drafts...). 6 deliverables via 6 parallel sub-agents finished in ~8 minutes.

## Actionable for our stack (aegntic / Hermes / the forge)

1. **We already run the roast pattern** - council + war-council skills (5-adviser MC, Zapier personas). Gap vs his version: no 'buyer' persona and no forced 'cheapest 48-hour test' output. Cheap upgrade to council-of-skills when the forge PR lands.
2. **Verification loop = our 'Finishing the job' doctrine, productized.** His Playwright screenshot-every-section + form stress-test is exactly our webapp-testing/browser harness. Actionable: bake a 'definition of done' field into card contracts so sub-agents self-verify before reporting.
3. **Session handoff exists in Hermes** (handoff skill) - his twist worth stealing: make the handoff PORTABLE (paste into any CLI, not just resume).
4. **Context discipline**: his 250k-of-1M heuristic is a concrete number for the AGENTS.md Layer-3 danger-zone math.
5. **The /goal evaluator split is the forge's loop in miniature** - qc.py + verification gates ARE the second model. The 'objective done condition' checklist style (file counts, competitor counts) is exactly how forge cards should define acceptance.
6. **Funnel**: free Skool community -> paid plus community; 400k members claim. Not ours, but the packaging of 'skills as lead magnet' validates the forge's distribution angle.

## Verbatim quotes that matter

> "By default, Claude is tuned to make you feel productive. It is not tuned to make you money." [0:57]
> "Something being finished and something actually working are not the same thing at all." [8:00]
> "Claude doesn't get to declare itself done. A different model has to look at it... and actually grade it." [22:38]

## Gaps / skepticism

- '3x more money in 30 days' is an unverified marketing claim; the 4 upgrades have real studies behind them but the headline number is content-marketing.
- The demo landing page is admittedly 'AI generic' - verification catches function, not taste. (Our design-contract approach covers that gap.)
- Studies cited loosely (ELEPHANT, NYU Copilot 40%, Anthropic 90%) - directions plausible, exact figures not checked here.