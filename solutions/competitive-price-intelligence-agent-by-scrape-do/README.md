# Competitive Price Intelligence Agent (Uplizd) - Automated real-time competitor pricing monitoring

## Summary
The Competitive Price Intelligence Agent is an automated workflow designed to track, analyze, and report on competitor pricing strategies in real-time. By leveraging the Scrape.do integration via the Composio Toolset, this solution empowers businesses to maintain market competitiveness, adjust their own pricing dynamically, and receive instant alerts on market shifts, serving as a single source of truth for pricing intelligence.

---

## Demo
![Competitive Price Intelligence Agent dashboard showing real-time competitor price tracking and automated alerts](../image.png)
**Alt text (SEO-ready):** Competitive Price Intelligence Agent dashboard showing real-time competitor price tracking, market data analysis, and automated alerts using Uplizd and Scrape.do.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0f0bed46-e419-5637-be26-5d2fe1e3149e)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** competitive intelligence, pricing strategy, web scraping, market analysis, data sync, composio, ai workflow, revenue operations
- This solution bridges the gap between raw web-scraped market data and actionable revenue intelligence for modern sales and operations teams.

---

## Who is this for?
This workflow is designed for professionals who need to maintain a pulse on market dynamics without manual data collection.

- **Pricing Analyst**
    - Automates the collection of competitor price points to inform dynamic pricing models.
- **E-commerce Manager**
    - Monitors catalog parity and identifies opportunities to undercut or match competitor promotions.
- **Sales Operations Lead**
    - Provides the sales team with real-time competitive intelligence to handle price-based objections.
- **Market Researcher**
    - Aggregates large-scale pricing trends to generate weekly market health reports.

---

## Features
- **Automated Web Scraping**
    - Utilizes Scrape.do to extract pricing data from competitor websites at scheduled intervals.
- **Real-time Price Alerts**
    - Triggers instant notifications when a competitor changes their pricing on key products.
- **Data Normalization**
    - Cleans and structures unstructured web data into a standardized format for easy analysis.
- **Competitive Benchmarking**
    - Automatically compares scraped data against internal product pricing to highlight discrepancies.
- **Seamless CRM Integration**
    - Pushes intelligence directly into your CRM to keep the sales team informed of market shifts.

---

## Use Cases
**Market Positioning**
- Track competitor discount cycles to time your own promotional campaigns effectively.
- Identify pricing gaps in the market to position new product launches for maximum impact.

**Operational Efficiency**
- Eliminate manual spreadsheet updates by automating the daily collection of competitor price lists.
- Reduce time-to-insight by having the AI summarize daily price changes into a concise executive brief.

**Sales Enablement**
- Equip account executives with real-time battle cards containing current competitor pricing.
- Proactively address price-based churn by identifying when a competitor drops their price below your threshold.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Competitive Price Intelligence template from the library.
3. Authenticate your Scrape.do account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target URLs and product identifiers for monitoring.
*   **Agent**: Analyzes the scraped data against your internal pricing rules.
*   **Composio Toolset**: Executes the Scrape.do calls to fetch live market data.
*   **Chat Output**: Delivers the summarized pricing report or alert to your preferred channel.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Check the current price of our flagship product on the competitor's website at [URL] and alert me if it is lower than $99.`
- `Scrape the latest pricing for all items in our category from [Competitor Site] and generate a summary report.`
- `Monitor [URL] for any price changes today and update the pricing intelligence log.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting raw scraped data and making decisions based on your business logic.
- Set the system prompt to prioritize accuracy and data extraction.
- Define specific thresholds for "price drop" or "price hike" alerts.
- Configure the agent to output data in a structured JSON format for downstream processing.

### 2) Composio Toolset Node
- Provide your Scrape.do API key to enable web data extraction.
- Ensure the connection scope allows for read-only access to target competitor domains.

### 3) Tool Availability
- **Scrape.do API**: For high-concurrency, reliable web scraping.
- **Data Parser**: For converting HTML/JSON responses into actionable insights.
- **Notification Service**: For sending alerts to Slack, Email, or CRM.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with external signals.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep dive into account-specific market positioning.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Monitor competitor video content and market presence.
