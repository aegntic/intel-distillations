# Agent Security Baseline

Agent adoption widened the attack surface, and the 10-23 corpus supplies both sides: what the attacks now cost, and the platform-level baseline that survives a prompt-injected agent. The baseline law: prompt-level limits are not guardrails; enforce at the platform and the payment instrument. Related: [sub-agents-and-parallelism](sub-agents-and-parallelism.md), [definition-of-done](definition-of-done.md), [agent-business-models](agent-business-models.md).

## Synthesis

The attack side is commodity-priced: AI-written spear-phishing matches human experts at ~4 cents/email (54% click both human and AI lures); cloned voices defeat voice-print authentication ("fully defeated" per Altman); ClickFix command-paste lures were the top initial access in Microsoft-expert-flagged attacks (47%); OpenAI's position is that prompt injection into browsers and summarizers may never be fully solved [f15 10:22][f15 3:24][f15 16:54][f15 14:18]. AI-assisted discovery cuts both ways: OpenAI and Google models found the PHP2Shell flaw class, the official PHP advisory and coordinated disclosure landed 2026-10-21, and Dutch government sites went offline as a precaution [f00 16:48].

The defensive baseline is enforced at the platform, not in the prompt: scoped expiring keys, .env only, read-only DB users, and local MCP proxies over legacy full-access keys [f24 12:24][f35 9:10][f35 7:51]. Spending gets locked at the payment instrument: an API-issued virtual card with a $50 weekly limit, merchant lock (software only), country lock, expiry, and transaction webhooks; a $60 attempt declines by card rules, not by instruction [f12 3:14].

## Key claims

- AI spear-phishing at expert efficacy for ~4 cents/email; 54% click both lure types [f15 10:22].
- Cloned voices have "fully defeated" voice-print authentication [f15 3:24].
- ClickFix was top initial access (47%) in Microsoft-expert-flagged attacks [f15 14:18].
- Prompt injection may never be fully solved, per OpenAI [f15 16:54].
- AI found the PHP2Shell flaw class; defenders patched on a 2-day-old advisory [f00 16:48].
- Baseline: scoped expiring keys, .env only, read-only DB users, local MCP proxies [f24 12:24][f35 9:10][f35 7:51].
- Card-level spend locks decline overages by card rules, not instruction [f12 3:14].

## Apply to aegntic

- List every credential an agent can touch; replace with read-only DB users, scoped expiring keys, or a local MCP proxy [f35 7:51][f35 9:10].
- Inventory PHP and legacy surfaces; apply the php.net 2026-10-21 advisory and Cloudflare WAF guidance [f00 16:48].
- Issue one capped virtual card per deployed agent and wire the charge webhook [f12 3:14].
