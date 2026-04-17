# Competitor Website Monitor (Uplizd) - Real-time market intelligence and change tracking

## Summary
The Competitor Website Monitor is an automated Uplizd AI workflow designed to track, analyze, and report on changes across competitor digital properties. By leveraging the Browserless integration, this solution provides RevOps and marketing teams with a single source of truth for pricing shifts, feature updates, and messaging pivots, ensuring your organization maintains a competitive edge through proactive data monitoring.

---

## Demo
![Competitor Website Monitor dashboard showing real-time change detection alerts and pricing comparison tables](../image.png)
**Alt text (SEO-ready):** Competitor Website Monitor dashboard showing real-time change detection alerts and pricing comparison tables for Uplizd AI workflow and Browserless integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/66631893-90d0-5943-a07e-d33814d8e73b)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** competitive analysis, web scraping, browserless, market monitoring, pricing intelligence, data sync, ai workflow, composio
- This solution bridges the gap between raw web data and actionable business insights by automating the monitoring of competitor digital assets.

---

## Who is this for?
This workflow is built for teams that need to stay ahead of market shifts without manual daily site checks.

- **Product Manager**
    - Identifies new feature releases and UI changes to inform product roadmap adjustments.
- **Marketing Strategist**
    - Monitors competitor messaging and landing page copy to refine brand positioning.
- **Pricing Analyst**
    - Tracks pricing page fluctuations to ensure your product remains competitively positioned.
- **Sales Operations Lead**
    - Generates real-time alerts on competitor activity to arm sales teams with battlecards.

---

## Features
- **Automated Change Detection**
    - Uses Browserless to crawl target URLs at scheduled intervals and identify DOM-level changes.
- **Intelligent Summarization**
    - Employs LLMs to distill complex website updates into concise, actionable executive summaries.
- **Multi-Platform Integration**
    - Seamlessly pushes findings into your CRM or Slack via the Composio Toolset for immediate team notification.
- **Historical Trend Analysis**
    - Maintains a log of detected changes, allowing for long-term monitoring of competitor strategy evolution.
- **Customizable Alerting**
    - Configures specific triggers for high-priority changes, such as pricing drops or new product launches.

---

## Use Cases
**Pricing Strategy Monitoring**
- Automatically alert the finance team when a competitor updates their pricing tier structure.
- Compare historical pricing data to detect seasonal discounting patterns.

**Product Launch Tracking**
- Detect the appearance of new "New" or "Beta" badges on competitor feature pages.
- Capture and archive screenshots of new landing page layouts for design benchmarking.

**Messaging & Positioning Analysis**
- Monitor changes in value propositions and taglines across competitor homepages.
- Identify shifts in target audience language to optimize your own lead generation copy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Browserless and relevant CRM/Notification accounts via the Composio dashboard.
3. Configure the target competitor URLs in the input node.
4. Ensure nodes are correctly linked from the trigger to the final notification output.

### 2) Setup the Nodes
- **Chat Input**: Defines the target competitor URLs and frequency of monitoring.
- **Agent**: Analyzes the scraped HTML content to extract meaningful business changes.
- **Composio Toolset**: Executes the web scraping tasks and pushes updates to your preferred destination.
- **Chat Output**: Delivers the final summary report to your team's communication channel.

### 3) Run the Flow
Use the Playground to test your monitor with these prompts:
- `Check https://competitor-a.com/pricing for any changes since yesterday and summarize them.`
- `Monitor https://competitor-b.com/features and alert me if any new product modules are added.`
- `Compare the current homepage messaging of https://competitor-c.com against our saved baseline.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your competitive intelligence.
- Instruct the agent to focus on specific elements like pricing tables or feature lists.
- Use a "diff" comparison instruction to ignore minor CSS changes and focus on content.
- Set the tone to "Executive Summary" for concise, high-impact reporting.

### 2) Composio Toolset Node
- Provide your Browserless API key to enable high-fidelity web scraping.
- Define the connection scope to include read-only access to target domains.

### 3) Tool Availability
- **Browserless**: For rendering and extracting content from dynamic websites.
- **Slack/Email API**: For delivering real-time alerts to stakeholders.
- **CRM Connector**: For logging competitor activity directly into your account records.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automate the gathering of company-level insights and firmographic data.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive research assistant for qualifying and mapping target accounts.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Track competitor video content performance and audience engagement metrics.
