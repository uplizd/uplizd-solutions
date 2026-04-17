# Sales Performance Analyzer (Uplizd) - Real-time CRM pipeline insights and revenue growth recommendations

## Summary
The Sales Performance Analyzer is an intelligent Uplizd workflow designed to transform raw CRM data into actionable revenue insights. By leveraging the Composio Toolset to interface with your CRM, the agent identifies stalled opportunities, tracks quota attainment, and provides prescriptive coaching for sales teams. This solution serves as a single source of truth for RevOps and sales managers, significantly increasing pipeline velocity and improving forecast accuracy.

---

## Demo
![Sales Performance Analyzer dashboard showing CRM pipeline health and revenue forecasting metrics](image.png)
**Alt text (SEO-ready):** Sales Performance Analyzer Uplizd workflow dashboard for CRM pipeline health, revenue forecasting, and sales team performance tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d6a552d0-63a3-5fba-8937-799594797443)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, salesforce, hubspot, pipeline, revenue intelligence, sales operations, composio, ai workflow

This solution bridges the gap between raw CRM data and strategic decision-making by automating performance analysis and opportunity health monitoring.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their sales cycle and improve data-driven decision-making.

* **Sales Managers**
    * Gain immediate visibility into team performance and identify coaching opportunities for underperforming deals.
* **Revenue Operations (RevOps)**
    * Automate the generation of pipeline health reports to ensure data hygiene and accurate forecasting.
* **Account Executives**
    * Receive proactive alerts on stalled opportunities and suggested next steps to move deals forward.
* **Sales Directors**
    * Monitor real-time quota attainment and high-level trends to adjust regional or product-specific strategies.

---

## Features
- **Automated Pipeline Auditing**
  Continuously scans CRM objects to flag deals that have remained in a stage beyond the defined velocity threshold.
- **Intelligent Opportunity Scoring**
  Analyzes historical win/loss patterns to assign health scores to active opportunities, highlighting those at risk.
- **CRM-Integrated Tooling**
  Uses the Composio Toolset to securely read and update records across platforms like Salesforce and HubSpot in real-time.
- **Prescriptive Coaching Insights**
  Generates natural language summaries for managers, suggesting specific actions to unblock stalled or complex deals.
- **Customizable Performance Metrics**
  Allows users to define unique KPIs and thresholds that align with specific organizational sales methodologies.

---

## Use Cases
**Pipeline Health Monitoring**
* Identifying "zombie" deals that have not had activity in over 30 days.
* Flagging opportunities where the close date has passed without a stage update.

**Revenue Forecasting**
* Aggregating weighted pipeline values to provide a more accurate monthly revenue forecast.
* Detecting discrepancies between expected close dates and current deal progress.

**Sales Coaching & Enablement**
* Providing weekly summaries of top-performing sales reps and their winning behaviors.
* Alerting managers to large-value deals that require executive intervention or additional resources.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Sales Performance Analyzer template from the marketplace.
3. Connect your preferred CRM (e.g., Salesforce, HubSpot) via the Composio integration settings.
4. Ensure nodes are correctly mapped from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Accepts natural language queries about sales performance or specific deal status.
* **Agent:** Processes the request, interprets CRM data, and formulates strategic recommendations.
* **Composio Toolset:** Executes read/write operations to fetch deal records and update opportunity fields.
* **Chat Output:** Delivers the final analysis and actionable insights back to the user.

### 3) Run the Flow
Use the Playground to test your analysis:
* `Analyze the health of all opportunities in the 'Negotiation' stage for the current quarter.`
* `Which deals have been stalled for more than 21 days and need immediate attention?`
* `Provide a summary of team performance against quota for the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a senior Sales Operations analyst.
* Focus on identifying bottlenecks and revenue risks.
* Maintain a professional, data-driven, and proactive tone.
* Prioritize actionable recommendations over raw data dumps.

### 2) Composio Toolset Node
Requires a valid API key for your CRM platform. Ensure the scope includes read/write access to `Opportunities`, `Accounts`, and `Contacts` to enable full analysis and update capabilities.

### 3) Tool Availability
* **CRM Search:** Find specific accounts or deal IDs.
* **Record Retrieval:** Fetch detailed fields for opportunity analysis.
* **Update/Edit:** Modify deal stages or add notes based on agent recommendations.
* **Reporting:** Aggregate data across multiple records for trend analysis.

---

## Related Solutions
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and automate follow-up tasks.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new sales opportunities.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across multiple CRM platforms.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate CRM records.
