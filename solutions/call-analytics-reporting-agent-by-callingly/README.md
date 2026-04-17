# Call Analytics Reporting Agent (Uplizd) - Automate call performance insights and reporting

## Summary
The Call Analytics Reporting Agent by Callingly leverages Uplizd AI workflows to transform raw telephony data into actionable business intelligence. By automating the extraction, synthesis, and reporting of call metrics, this solution provides RevOps and support teams with a single source of truth, significantly reducing manual data entry and increasing pipeline velocity through real-time performance visibility.

---

## Demo
![Call Analytics Reporting Agent dashboard showing automated call performance metrics and trend analysis](../image.png)

**Alt text (SEO-ready):** Call Analytics Reporting Agent dashboard showing automated call performance metrics, trend analysis, Uplizd AI workflow, and Callingly data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9b2cc03d-1b5e-5353-815d-eb7aa6689158)

---

## Category
**Primary category:** Sales automation

**Secondary tags:** `callingly`, `analytics`, `reporting`, `salesops`, `data sync`, `ai workflow`, `composio`, `business intelligence`

This solution bridges the gap between raw telephony logs and executive reporting, ensuring data hygiene and actionable insights for sales and support operations.

---

## Who is this for?
This solution is designed for teams that need to turn high-volume call data into structured performance reports without manual intervention.

* **Sales Operations Manager**
    * Automates the aggregation of call volume and conversion metrics across the team.
* **Customer Success Lead**
    * Identifies recurring support themes and sentiment trends from recorded calls.
* **Revenue Analyst**
    * Maintains data integrity by syncing call outcomes directly into CRM reporting dashboards.
* **Business Development Representative**
    * Gains visibility into personal call performance and improvement areas through automated summaries.

---

## Features
- **Automated Data Extraction**
  Seamlessly pulls call logs and metadata from Callingly using the Composio Toolset.
- **Sentiment & Keyword Analysis**
  Uses AI to categorize call outcomes and extract key topics discussed during customer interactions.
- **Customizable Reporting Templates**
  Generates structured summaries formatted for Slack, email, or direct CRM entry.
- **Real-Time Performance Sync**
  Ensures that call metrics are updated in your data warehouse or CRM immediately after a call ends.
- **Anomaly Detection**
  Flags unusual call patterns or missed follow-up opportunities to maintain pipeline health.

---

## Use Cases
**Performance Monitoring**
* Aggregating weekly call volume and talk-time metrics for team leaderboards.
* Identifying top-performing call scripts based on conversion rates and sentiment scores.

**Operational Efficiency**
* Automatically logging call summaries into Salesforce or HubSpot to eliminate manual entry.
* Triggering follow-up tasks in project management tools when specific keywords are detected in calls.

**Quality Assurance**
* Flagging calls with negative sentiment for manager review and coaching.
* Generating monthly compliance reports based on call recording metadata.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the workflow.
3. Authenticate your Callingly and CRM accounts via the Composio connection prompt.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger signal or manual request for a call report.
* **Agent**: Processes raw call data, performs sentiment analysis, and drafts the report.
* **Composio Toolset**: Executes secure API calls to retrieve telephony logs and update CRM records.
* **Chat Output**: Delivers the final, formatted performance report to your preferred channel.

### 3) Run the Flow
Use the Uplizd Playground to test your agent with these prompts:
* `Generate a summary report of all calls made by the sales team yesterday.`
* `Identify the top 3 recurring customer pain points from last week's support calls.`
* `Sync the latest call outcomes to my CRM and notify me of any missed follow-ups.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a data analyst and reporting assistant.
* **Instruction Pattern:**
    * "You are an expert call analytics assistant; analyze call logs for sentiment, key topics, and conversion indicators."
    * "Always format output as a structured report with clear headings and actionable bullet points."
    * "Prioritize data accuracy by cross-referencing call metadata with CRM opportunity fields."

### 2) Composio Toolset Node
* **API Key:** Provide your unique Composio API key in the node settings.
* **Connection Scope:** Ensure the Callingly integration has read-access to call logs and write-access to your target CRM.

### 3) Tool Availability
* **Callingly API:** For fetching call transcripts, duration, and participant data.
* **CRM Connector (Salesforce/HubSpot):** For updating lead/opportunity records with call summaries.
* **Notification Tools (Slack/Email):** For delivering automated reports to stakeholders.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automate account intelligence gathering and reporting.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Multi-platform CRM data synchronization and conflict resolution.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and track stalled deals.
