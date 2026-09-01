# Hermes Ecosystem Intel

What the corpus establishes about Hermes Agent itself: features as demoed, cost positioning, and the second-brain pattern. Merges the three Hermes-centric harvest videos with the Nick Puru feature walkthrough (deduplicated). Related: [context-discipline](context-discipline.md), [sub-agents-and-parallelism](sub-agents-and-parallelism.md), [agent-business-models](agent-business-models.md).

## Synthesis

Harness choice beats model choice on cost and completion. In head-to-head use, a 300/month vendor bot subscription lost to Hermes as the better harness, while Hermes ran on a 20/month ChatGPT subscription [v04 9:40, 10:27]. Composio's harness benchmarks (highest completion rate, cheapest cost per task, fastest runtime versus Claude Code) [unverified] argue for treating the harness as the primary stack decision [v14 2:56, 3:15, 3:50]. The tension is vendor convenience versus open harness economics; the operator paying 300/month still concludes Hermes wins [v04].

The Puru walkthrough is the fullest feature catalog in the corpus [VdG2o91D_2k]: one-click desktop installer for Mac/Windows/Linux handling environment, browser tools, and command wiring, positioned as the key adoption unlock (no terminal needed) [3:23-4:07]. Provider selection via OpenAI OAuth (ChatGPT 5.6 chosen because subscription beats API pricing), Anthropic, or OpenRouter [4:07, 4:29]. Telegram bot connect via BotFather with replies echoing in the desktop session log [4:48-6:53]. MCP servers added in natural language with HTTP transport and tool discovery [7:55]; Zapier MCP as universal adapter to ~9,000 SaaS apps through one connection [7:13, 8:35].

Memory intake as an interview: "ask me questions until you have all of this... keep asking until it's actually accurate, not just generic," covering core offer, ICP, pricing, tone, onboarding, tools, and boundaries [10:53, 11:56-13:02]. Jobs convert to named skills at the moment of success ("save everything you just did as a reusable skill called proposal writer") [15:49]. Parallel background jobs with completion pings [20:26-21:24], natural-language cron ("every morning at 7:00, brief me, send it to my Telegram") with no settings screens [22:06, 23:10], sub-agents visible in the UI [23:53], and permission prompts with always-allow [15:03].

Ops requirements: hosted uptime matters, "if your laptop is asleep, so is your agent"; run on a Mac mini, old desktop, or a VPS (Hetzner, Hostinger) [VdG2o91D_2k 28:37]. Training is the product: install takes 10 minutes, training decides success; framed as hiring a new employee who is useless on day one because they do not know your business [VdG2o91D_2k 1:23, 2:05, 29:18]. The three-move pattern repeated across sales, ops, admin, content: train it on a piece of the business, save it as a skill, put it on a schedule [VdG2o91D_2k 24:56].

The second-brain video lands the architecture argument: persistent memory is the differentiator versus ChatGPT, every conversation compounds, and killing a project stops the agent raising it [v14; l0Vqm0ZIySc 23:28]. Sellers describe Hermes as the execution layer, never the idea generator [GkHwnQdoDpM 0:32].

## Key claims

- Hermes on a 20/month subscription beat a 300/month vendor bot in head-to-head use [v04 10:27].
- Composio harness benchmarks: highest completion rate, cheapest cost per task, fastest runtime vs Claude Code [unverified] [v14 3:15].
- Zapier MCP reaches ~9,000 applications via one connection [VdG2o91D_2k 7:13].
- Proposal generation ~3 minutes with permission prompts; 10-lead research job with Gmail drafts in ~10 minutes [VdG2o91D_2k 14:46, 18:10].
- Hermes "over 200,000 stars on GitHub" [unverified, marketing framing; transcript renders Nous Research as "News Research"] [VdG2o91D_2k 3:02].
- Demo invoice anchor: Acme Dental, $2,500 monthly retainer rendered as a Google Doc [VdG2o91D_2k 25:38].
- Wiki distillation (the second-brain pattern) dropped query token usage 95% [unverified] [v24 131:19].
- Agent self-reported its model and flagged a missing macOS launch service for restart survival [VdG2o91D_2k 6:09].

## Contradictions

- "No coding required" title versus a demo whose entire value is configuration-as-programming (memory design, MCP wiring, cron authoring); Sharbel concedes clients will not configure Hermes properly on their own, which is the studio's service wedge [source-six-deep, contradictions].
- Vendor-stack convenience (300/month, v04) versus open-harness economics (20/month plus VPS); the same video pays for both and sides with Hermes [v04 0:00, 10:27].

## Apply to aegntic

- Copy the memory-intake interview as a productized onboarding artifact: the agent interrogates the client (offer, ICP, pricing, tone, boundaries) until accurate, then writes the memory file.
- Ship everything on an always-on box (Hetzner/Hostinger VPS or Mac mini) the day a cron job matters; sleeping laptop equals sleeping agent.
- Use the three-move pattern as the studio's standard delivery: train, save as skill, schedule.
- Steal the self-configuration transparency: agents should self-report model, wiring gaps, and restart-survival status on request.
