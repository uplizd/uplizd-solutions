# Multi-Touch Attribution Optimizer (Uplizd) - Decode marketing funnels to optimize cross-channel spend

## Summary
The Multi-Touch Attribution Optimizer is an intelligent Uplizd workflow designed to ingest complex marketing data from Google BigQuery, analyze customer journey touchpoints, and provide actionable insights for budget allocation. By automating the synthesis of multi-source attribution models, this solution enables marketing teams to move beyond last-click bias, ensuring a single source of truth for campaign performance and maximizing pipeline velocity.

---

## Demo
![Multi-touch attribution dashboard showing channel performance and conversion paths](image.png)
**Alt text (SEO-ready):** Multi-touch attribution dashboard showing channel performance, conversion paths, and Uplizd AI workflow for marketing data analysis in Google BigQuery.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4193f98c-0b8a-52f6-a604-981b0874c9fd)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** google bigquery, attribution, marketing analytics, roi optimization, data pipeline, composio, ai workflow, growth marketing.
This solution bridges the gap between raw BigQuery marketing logs and strategic decision-making by automating the attribution modeling process.

---

## Who is this for?
This solution is designed for data-driven marketing teams looking to eliminate guesswork from their budget allocation.

*   **Marketing Operations Manager**
    *   Automates the reconciliation of multi-channel spend data to ensure accurate ROI reporting.
*   **Performance Marketer**
    *   Identifies high-performing touchpoints in the customer journey to optimize ad spend in real-time.
*   **Data Analyst**
    *   Reduces manual query time by using AI to interpret complex SQL outputs from BigQuery.
*   **Growth Lead**
    *   Provides a clear view of which channels drive long-term customer acquisition versus short-term clicks.

---

## Features
- **BigQuery Integration**
    Seamlessly queries raw interaction logs and conversion events stored in Google BigQuery via the Composio Toolset.
- **Multi-Touch Modeling**
    Applies sophisticated attribution logic (linear, time-decay, or position-based) to weigh touchpoints across the funnel.
- **Automated Insight Generation**
    Translates complex attribution data into plain-language summaries and actionable recommendations for channel optimization.
- **Real-Time Pipeline Velocity**
    Monitors how specific marketing channels impact the speed at which leads move through the sales pipeline.
- **Cross-Channel Normalization**
    Standardizes data formats from disparate ad platforms to ensure apples-to-apples comparisons of marketing performance.

---

## Use Cases
**Budget Allocation Optimization**
*   Reallocate spend from underperforming channels to those with the highest multi-touch conversion impact.
*   Identify "hidden" top-of-funnel channels that contribute significantly to final conversions.

**Customer Journey Analysis**
*   Map the sequence of interactions that lead to high-value enterprise deals.
*   Analyze the drop-off points between initial ad click and final conversion to improve landing page relevance.

**Marketing ROI Reporting**
*   Generate automated weekly reports that highlight the true contribution of each channel to total revenue.
*   Validate marketing campaign effectiveness by correlating spend spikes with conversion volume in BigQuery.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Google BigQuery account within the Composio Toolset node.
3. Configure the Chat Input to accept your specific date range or campaign parameters.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input:** Receives the user's query regarding specific marketing campaigns or timeframes.
*   **Agent:** Processes the request and determines which BigQuery tables to query for attribution data.
*   **Composio Toolset:** Executes secure SQL queries against your BigQuery environment to fetch interaction data.
*   **Chat Output:** Delivers a summarized report of attribution insights and budget recommendations.

### 3) Run the Flow
Use the Playground to test your attribution analysis:
*   `Analyze the last 30 days of campaign performance and identify the top 3 touchpoints for conversions.`
*   `Compare the ROI of LinkedIn ads versus Google Search based on the multi-touch attribution model.`
*   `Which marketing channels are most effective at driving users from the awareness stage to the demo request stage?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a marketing data scientist capable of interpreting SQL results.
*   Prioritize data accuracy and clear, concise reporting.
*   Use the provided attribution logic to weigh touchpoints correctly.
*   Always cite the data source (BigQuery table) when presenting findings.

### 2) Composio Toolset Node
*   **API Key:** Ensure your Google Cloud Service Account key is configured in the Composio dashboard.
*   **Connection Scope:** Grant `bigquery.jobs.create` and `bigquery.tables.getData` permissions to the agent.

### 3) Tool Availability
*   **BigQuery Query Executor:** For running SQL scripts to extract marketing interaction logs.
*   **Data Formatter:** For normalizing currency and date formats across different ad platforms.
*   **Insight Summarizer:** For converting raw JSON/CSV data into human-readable strategic summaries.

---

## Related Solutions
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automates the aggregation of account-level data for comprehensive reporting.
*   [AB Test Performance Analyzer](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) — Evaluates the success of website experiments to inform conversion optimization.
*   [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Analyzes video engagement data to refine content distribution strategies.
