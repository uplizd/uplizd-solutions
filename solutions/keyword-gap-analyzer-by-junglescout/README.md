# Keyword Gap Analyzer (Uplizd) - Identify and capture untapped search opportunities

## Summary
The Keyword Gap Analyzer is an automated Uplizd workflow designed to bridge the gap between your content strategy and competitor performance. By leveraging the JungleScout integration, this agent identifies high-value keywords that your competitors rank for but you do not, allowing marketing teams to optimize their SEO pipeline, improve search visibility, and capture missed organic traffic with precision.

---

## Demo
![Keyword Gap Analyzer dashboard showing competitor keyword comparison and opportunity scoring](image.png)
**Alt text (SEO-ready):** Keyword Gap Analyzer dashboard showing competitor keyword comparison, search volume analysis, and SEO opportunity scoring within the Uplizd workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/24954d7b-5ee1-59d2-a255-a4db7f7eda30)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** seo, keyword research, content strategy, competitor analysis, junglescout, organic growth, search intent, ai workflow
- This solution empowers marketing teams to automate competitive intelligence gathering and turn search data into actionable content plans.

---

## Who is this for?
This workflow is built for growth-focused teams looking to scale their organic presence through data-driven insights.

- **SEO Specialist**
    - Automates the discovery of high-intent keywords to prioritize content production.
- **Content Strategist**
    - Identifies content gaps in the competitive landscape to build topical authority.
- **Digital Marketing Manager**
    - Monitors competitor search performance to adjust bidding and organic strategies in real-time.
- **Growth Marketer**
    - Uncovers low-hanging fruit opportunities to maximize ROI on organic search efforts.

---

## Features
- **Competitor Keyword Discovery**
    - Automatically pulls keyword data from JungleScout to identify terms where competitors hold top rankings.
- **Search Intent Analysis**
    - Uses the Agent node to categorize missing keywords by user intent, ensuring content aligns with buyer needs.
- **Automated Opportunity Scoring**
    - Ranks identified gaps based on search volume and difficulty, helping you prioritize high-impact content.
- **Seamless Integration**
    - Connects directly with the Composio Toolset to fetch real-time market data without manual exports.
- **Actionable Content Briefs**
    - Generates structured summaries for identified gaps, ready for hand-off to your writing team.

---

## Use Cases
**Competitor Benchmarking**
- Compare your domain's keyword footprint against top-tier competitors to identify visibility blind spots.
- Track shifts in competitor keyword rankings to proactively defend your search positions.

**Content Strategy Optimization**
- Generate a prioritized list of blog topics based on high-volume keywords you are currently missing.
- Refresh underperforming landing pages by incorporating missing semantic keywords identified by the agent.

**Market Intelligence**
- Identify emerging search trends in your niche before they become saturated by competitors.
- Analyze the keyword overlap between your brand and new market entrants to maintain a competitive edge.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your JungleScout API credentials within the Composio Toolset node.
3. Configure your target competitor domains in the Agent instructions.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target competitor domain and your own domain for comparison.
- **Agent**: Processes the data to identify gaps and assign priority scores.
- **Composio Toolset**: Executes queries against the JungleScout API to fetch keyword performance metrics.
- **Chat Output**: Delivers a formatted report of high-value keyword opportunities.

### 3) Run the Flow
Use the Playground to test your analysis:
- `Analyze the keyword gap between mydomain.com and competitor.com for the electronics category.`
- `Find 10 high-volume keywords that my competitor ranks for but I do not.`
- `Generate a content brief for the top 5 missing keywords identified in the last scan.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an SEO strategist, synthesizing raw data into actionable insights.
- Focus on high-volume, low-difficulty keywords first.
- Maintain a professional, data-driven tone in all generated content briefs.
- Ensure all suggestions include a brief rationale based on search intent.

### 2) Composio Toolset Node
- Requires a valid JungleScout API key with read access to keyword and competitor analytics.
- Ensure the connection scope includes `keyword_research` and `competitor_analysis` permissions.

### 3) Tool Availability
- `get_competitor_keywords`: Fetches ranking data for specified domains.
- `get_keyword_metrics`: Retrieves search volume and difficulty scores for target terms.
- `analyze_gap_overlap`: Compares two keyword sets to isolate unique opportunities.

---

## Related Solutions
- [../you-tube-competitor-intelligence-agent-by-youtube/README.md](../you-tube-competitor-intelligence-agent-by-youtube/README.md) - Track competitor video performance and audience engagement.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Monitor website visitor intent and account-level intelligence.
- [../ab-test-performance-analyzer-by-microsoft-clarity/README.md](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) - Analyze A/B test results to optimize landing page conversions.
