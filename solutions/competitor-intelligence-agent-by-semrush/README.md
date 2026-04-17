# Competitor Intelligence Agent (Uplizd) - Automated competitive analysis and SEO monitoring

## Summary
The Competitor Intelligence Agent by Semrush is an automated workflow designed to streamline competitive research, SEO tracking, and PPC campaign monitoring. By leveraging the Composio Toolset to interface with Semrush data, this agent enables marketing teams and SEO specialists to maintain a single source of truth for market positioning, identify competitor content gaps, and accelerate pipeline velocity through data-driven insights.

---

## Demo
![Competitor Intelligence Agent dashboard showing automated Semrush data retrieval and SEO keyword analysis](image.png)
**Alt text (SEO-ready):** Competitor Intelligence Agent dashboard showing automated Semrush data retrieval, SEO keyword analysis, and competitive landscape monitoring on the Uplizd platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/957ae84b-73fd-55e7-8149-da2e0a01c31c)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** semrush, seo, ppc, competitive intelligence, market research, data integration, composio, ai workflow
- This solution bridges the gap between raw competitive data and actionable marketing strategy by automating the retrieval and synthesis of market intelligence.

---

## Who is this for?
This solution is designed for marketing and growth professionals who need to stay ahead of market shifts without manual data collection.

- **SEO Specialist**
    - Automatically identifies keyword gaps and tracks competitor ranking fluctuations in real-time.
- **PPC Manager**
    - Monitors competitor ad spend and creative strategy to optimize bidding and campaign performance.
- **Marketing Strategist**
    - Aggregates market intelligence to inform quarterly planning and product positioning.
- **Growth Lead**
    - Quickly benchmarks brand performance against industry leaders to identify new expansion opportunities.

---

## Features
- **Automated Competitor Tracking**
    - Seamlessly pulls real-time data from Semrush to monitor competitor domains and keyword performance.
- **Keyword Gap Analysis**
    - Identifies high-value keywords that competitors rank for but your brand is currently missing.
- **PPC Intelligence**
    - Extracts competitor ad copy and landing page strategies to refine your own paid search initiatives.
- **Unified Data Synthesis**
    - Uses the Composio Toolset to process complex API responses into concise, human-readable executive summaries.
- **Dynamic Alerting**
    - Triggers notifications based on significant shifts in competitor SEO rankings or new ad campaign launches.

---

## Use Cases
**Market Positioning**
- Analyze competitor backlink profiles to discover new outreach opportunities.
- Compare domain authority metrics to benchmark your site against top industry players.

**SEO Strategy**
- Monitor daily ranking changes for core business keywords across target regions.
- Audit competitor content clusters to plan your next high-authority blog series.

**Paid Search Optimization**
- Track competitor ad spend trends to adjust budget allocation during peak seasons.
- Identify underperforming ad keywords in your own campaigns by comparing them against competitor success metrics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd template library and select the Competitor Intelligence Agent.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your Semrush account within the Composio connection settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your specific query regarding a competitor domain or keyword set.
- **Agent**: Processes instructions to fetch, filter, and analyze competitive data.
- **Composio Toolset**: Executes secure API calls to Semrush to retrieve live market data.
- **Chat Output**: Delivers a structured report or actionable insight directly to your dashboard.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze the top 5 organic competitors for domain: example.com and list their primary keyword gaps.`
- `What are the current PPC ad strategies being used by my top competitor for the keyword 'CRM software'?`
- `Generate a summary of the latest ranking fluctuations for our core keywords compared to our main competitor.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized marketing analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are an expert SEO analyst. Use the provided tools to fetch data, then synthesize it into a clear, actionable report."
- Instruction: "Always cite the specific metrics (e.g., search volume, CPC, ranking position) retrieved from the toolset."

### 2) Composio Toolset Node
- Requires a valid Semrush API key configured within your Composio account.
- Scope should include read access to domain analytics, keyword research, and advertising research endpoints.

### 3) Tool Availability
- `semrush_domain_overview`: Retrieves high-level traffic and keyword data for a domain.
- `semrush_keyword_gap`: Identifies keywords where competitors rank but the target domain does not.
- `semrush_ad_research`: Fetches active ad copy and historical PPC performance data.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Track company-level engagement and lead signals.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) - Analyze video content performance and audience demographics.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automate deep-dive research on target accounts and prospects.
