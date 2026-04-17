# Competitor Price Monitor (Uplizd) - Automated market intelligence and dynamic pricing alerts

## Summary
The Competitor Price Monitor is an intelligent Uplizd workflow that automates the tracking of competitor product pricing across the web. By leveraging the Composio Toolset to interface with web scraping engines, this solution provides real-time market visibility, enabling businesses to adjust their own pricing strategies, maintain competitive advantage, and react instantly to market fluctuations without manual data entry.

---

## Demo
![Competitor Price Monitor workflow dashboard showing automated scraping nodes and price alert triggers](image.png)
**Alt text (SEO-ready):** Competitor Price Monitor Uplizd workflow, automated web scraping for price tracking, real-time market intelligence, and dynamic pricing alerts using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/033458dc-003a-5949-9531-faf862f499f1)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** web scraping, competitor analysis, pricing strategy, market intelligence, automation, data sync, composio, ai workflow
- This solution bridges the gap between raw web data and actionable pricing strategy, ensuring your team is always informed of market changes.

---

## Who is this for?
This solution is designed for teams that need to maintain a pulse on the market and react to competitor movements with precision.

- **Pricing Manager**
    - Automates daily price audits to ensure margins remain protected against competitor undercutting.
- **E-commerce Operations Lead**
    - Monitors catalog-wide price shifts to trigger dynamic updates in the storefront.
- **Market Analyst**
    - Aggregates historical pricing trends to identify competitor promotional cycles and seasonal patterns.
- **Growth Strategist**
    - Receives instant alerts when key competitors change pricing, allowing for rapid tactical responses.

---

## Features
- **Automated Web Scraping**
    - Utilizes the Composio Toolset to extract real-time pricing data from target competitor URLs.
- **Dynamic Alerting**
    - Configurable triggers that notify stakeholders via Slack or email when price thresholds are breached.
- **Historical Data Logging**
    - Maintains a structured record of price changes to assist in long-term market trend analysis.
- **Multi-Platform Support**
    - Capable of monitoring diverse e-commerce platforms and custom web storefronts simultaneously.
- **Intelligent Data Normalization**
    - Cleans and formats scraped data into a consistent schema for easy integration with internal CRM or ERP systems.

---

## Use Cases
**Competitive Benchmarking**
- Track price parity across top 5 competitors for flagship product lines.
- Generate weekly reports comparing your average price point against the market median.

**Dynamic Pricing Response**
- Automatically flag products that have fallen out of the desired price range compared to competitors.
- Trigger internal approval workflows when a competitor drops prices below a specific margin threshold.

**Promotional Intelligence**
- Detect the start of competitor sales events by identifying sudden, temporary price drops.
- Monitor the duration of competitor discounts to optimize your own promotional timing.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your preferred web scraping tool via the Composio Toolset.
3. Define the target competitor URLs and the specific CSS selectors for pricing elements.
4. Ensure nodes are correctly mapped from **Chat Input** to **Agent**, **Composio Toolset**, and **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the list of competitor URLs and target products to monitor.
- **Agent**: Analyzes the scraped data, compares it against current internal pricing, and identifies anomalies.
- **Composio Toolset**: Executes the web scraping tasks and retrieves live data from the target sites.
- **Chat Output**: Delivers a summary report or alert notification to the user.

### 3) Run the Flow
Use the Playground to test your monitor:
- `Check the current price of the iPhone 15 on the competitor site and compare it to our current listing.`
- `Monitor all URLs in the 'Electronics' category and alert me if any price drops below $500.`
- `Generate a summary report of all competitor price changes detected over the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the analytical engine to interpret scraped data and identify pricing trends.
- **Recommended instruction pattern:**
    - "You are a market analyst assistant. Extract the price value from the provided HTML/text data."
    - "Compare the extracted price against the provided internal baseline price."
    - "If the difference exceeds 5%, flag it as a critical alert; otherwise, log it as a standard update."

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and authorized for web scraping tools.
- **Connection Scope**: Grant the toolset permission to access the specific domains you intend to monitor.

### 3) Tool Availability
- **Web Scraper**: For fetching live page content.
- **Data Parser**: For extracting specific price strings from complex HTML.
- **Notification Service**: For sending alerts to your team communication channels.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with external intelligence.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into competitor accounts.
- [Ad Trend Tracking Agent](../ad-trend-tracking-agent-by-adyntel/README.md) - Monitor competitor advertising and market positioning trends.
