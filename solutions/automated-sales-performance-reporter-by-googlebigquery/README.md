# Automated Sales Performance Reporter (Uplizd) - Transform raw sales data into executive-ready insights

## Summary
The Automated Sales Performance Reporter (Uplizd) streamlines the conversion of complex, fragmented sales data into actionable executive summaries. By leveraging the Composio Toolset to query Google BigQuery, this workflow eliminates manual reporting overhead, ensuring stakeholders receive real-time, accurate performance metrics to drive data-informed decision-making and pipeline velocity.

---

## Demo
![Automated Sales Performance Reporter workflow showing BigQuery data extraction and AI-driven report generation](image.png)
**Alt text (SEO-ready):** Automated Sales Performance Reporter (Uplizd) workflow showing Google BigQuery data extraction, AI-driven sales insights, and automated reporting for RevOps teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ee9df56c-db42-51cf-892f-a92ebc4c69f6)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** google bigquery, sales analytics, revops, data reporting, pipeline, ai workflow, composio, business intelligence.
This solution bridges the gap between raw cloud data warehouses and executive-level reporting through intelligent automation.

---

## Who is this for?
This solution is designed for data-driven teams looking to automate their reporting cadence and improve insight accuracy.

* **Sales Operations Manager**
    * Reduces time spent manually querying BigQuery for weekly performance reviews.
* **Revenue Operations (RevOps) Lead**
    * Ensures a single source of truth for pipeline metrics across the entire organization.
* **Sales Director**
    * Receives automated, high-level summaries of team performance without needing technical SQL access.
* **Data Analyst**
    * Offloads routine report generation to an AI agent, allowing focus on complex data modeling.

---

## Features
- **Automated BigQuery Integration**
  Seamlessly connects to Google BigQuery via the Composio Toolset to fetch real-time sales performance data.
- **AI-Driven Insight Synthesis**
  Translates raw SQL query results into natural language summaries, highlighting key trends and anomalies.
- **Customizable Reporting Cadence**
  Configurable trigger points allow for daily, weekly, or ad-hoc report generation based on specific business needs.
- **Executive-Ready Formatting**
  Structures output into professional, easy-to-read formats suitable for leadership briefings and stakeholder emails.
- **Pipeline Anomaly Detection**
  Identifies significant shifts in sales velocity or conversion rates, alerting management to potential risks or opportunities.

---

## Use Cases
**Weekly Performance Reviews**
* Generating summary reports of closed-won deals versus targets for the previous week.
* Highlighting top-performing sales regions based on BigQuery historical data.

**Pipeline Health Monitoring**
* Detecting stalled opportunities by analyzing stage-duration metrics in the CRM data warehouse.
* Flagging significant drops in lead conversion rates for immediate management review.

**Executive Briefings**
* Creating concise, high-level dashboards for quarterly business reviews (QBRs).
* Automating the delivery of key performance indicators (KPIs) directly to leadership communication channels.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in your dashboard.
2. Select your workspace and import the flow template.
3. Authenticate your Google BigQuery credentials within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the user's request for specific sales reports or time-period metrics.
* **Agent:** Processes the request, formulates the necessary SQL queries, and interprets the returned data.
* **Composio Toolset:** Executes secure queries against Google BigQuery to retrieve the requested sales data.
* **Chat Output:** Delivers the finalized, human-readable performance report to the user.

### 3) Run the Flow
Use the Playground to test the reporter with these prompts:
* `Generate a summary of total sales performance for the North American region over the last 30 days.`
* `Identify the top 5 sales opportunities that have stalled in the negotiation stage this week.`
* `Create a weekly performance report comparing current pipeline volume against quarterly targets.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data translator and analytical engine.
* Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Ensure the system prompt emphasizes data accuracy and professional tone.
* Instruct the agent to provide context for any anomalies found in the data.

### 2) Composio Toolset Node
* Provide your Google Cloud Project ID and service account credentials.
* Set the connection scope to read-only access for the relevant BigQuery datasets to maintain security.

### 3) Tool Availability
* `bigquery_query`: Executes SQL statements to fetch sales data.
* `bigquery_list_tables`: Helps the agent discover relevant schema information.
* `bigquery_get_table_metadata`: Provides context on column names and data types for accurate querying.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automates the gathering of account-level insights and firmographic data.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages sales stages, follow-ups, and identifies stalled deals.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes data across multiple platforms to ensure consistency.
