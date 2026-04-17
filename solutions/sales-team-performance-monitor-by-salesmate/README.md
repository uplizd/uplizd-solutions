# Sales Team Performance Monitor (Uplizd) - Optimize Salesmate CRM productivity and pipeline velocity

## Summary
The Sales Team Performance Monitor is an automated Uplizd workflow that bridges the gap between raw Salesmate CRM data and actionable performance insights. By leveraging AI-driven analysis, this solution enables sales leaders to track individual rep activity, identify stalled opportunities, and maintain high pipeline hygiene, ultimately accelerating revenue cycles and improving team accountability.

---

## Demo
![Sales Team Performance Monitor dashboard showing rep activity metrics and pipeline health status](image.png)
**Alt text (SEO-ready):** Sales Team Performance Monitor dashboard showing Uplizd workflow metrics, Salesmate CRM integration, and sales pipeline health analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6b4334e6-56cb-58b3-b3ed-cf36ce0f98ed)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** salesmate, crm, sales performance, pipeline management, revenue operations, ai workflow, data analytics, composio  
This solution streamlines RevOps by transforming Salesmate CRM data into real-time performance intelligence for sales teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual reporting and gain immediate visibility into sales performance.

- **Sales Managers**
    - Gain real-time visibility into rep activity levels and identify coaching opportunities before deals stall.
- **Revenue Operations (RevOps)**
    - Automate the aggregation of CRM data to ensure a single source of truth across the sales organization.
- **Account Executives**
    - Receive automated summaries of daily performance metrics to stay aligned with individual quota targets.
- **Sales Directors**
    - Monitor high-level pipeline velocity and forecast accuracy through AI-generated performance reports.

---

## Features
- **Automated Salesmate Sync**
    - Seamlessly pulls real-time activity data from Salesmate CRM using the Composio Toolset to ensure up-to-date reporting.
- **Performance Trend Analysis**
    - Utilizes advanced LLM reasoning to detect patterns in rep behavior and identify deviations from successful sales cadences.
- **Pipeline Health Scoring**
    - Automatically flags opportunities that have remained stagnant, providing actionable insights to keep the pipeline moving.
- **Customizable Reporting**
    - Generates tailored summaries of key performance indicators (KPIs) directly within the chat interface for quick review.
- **Actionable Coaching Insights**
    - Provides specific, data-backed recommendations for sales leaders to improve team efficiency and close rates.

---

## Use Cases
**Pipeline Velocity Optimization**
- Identify deals that have exceeded average stage duration and require immediate attention.
- Analyze conversion rates between pipeline stages to pinpoint bottlenecks in the sales process.

**Individual Rep Performance Tracking**
- Aggregate daily call, email, and meeting volumes to compare rep activity against team benchmarks.
- Generate weekly performance snapshots that highlight top-performing activities and areas for improvement.

**Data-Driven Sales Coaching**
- Extract insights from CRM records to prepare for 1:1 coaching sessions with specific performance data.
- Monitor adherence to sales playbooks by tracking the usage of specific deal stages and activity types.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Sales Team Performance Monitor template from the solution library.
3. Connect your Salesmate CRM account via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language queries regarding sales metrics.
- **Agent**: Processes CRM data using pre-defined instructions to analyze performance.
- **Composio Toolset**: Executes precise API calls to fetch and filter Salesmate CRM records.
- **Chat Output**: Delivers the final performance report or insight directly to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Analyze the performance of the sales team over the last 7 days.`
- `Which deals have been stuck in the 'Negotiation' stage for more than 14 days?`
- `Generate a summary of total calls and emails logged by each sales rep this month.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized Sales Operations Analyst.
- Use a high-reasoning model (e.g., GPT-4o) for accurate data interpretation.
- Instruction: "Act as a Sales Operations Analyst. Query Salesmate CRM to retrieve activity metrics and summarize them for management."
- Ensure the agent is instructed to prioritize identifying stalled deals and high-activity reps.

### 2) Composio Toolset Node
- Provide your Salesmate API key within the Composio configuration.
- Set the connection scope to allow read-only access to Deals, Contacts, and Activity logs.

### 3) Tool Availability
- `salesmate_get_deals`: Fetch opportunity status and stage history.
- `salesmate_list_activities`: Retrieve call, email, and meeting logs.
- `salesmate_get_users`: Identify specific sales reps for performance breakdown.

---

## Related Solutions
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manage and strengthen complex B2B client relationships.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Oversee pipeline stages and accelerate deal progression.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather and report on account-level engagement data.
