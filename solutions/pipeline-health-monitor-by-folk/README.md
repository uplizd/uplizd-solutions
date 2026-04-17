# Pipeline Health Monitor (Uplizd) - Real-time sales pipeline visibility and risk management

## Summary
The Pipeline Health Monitor by Uplizd provides automated oversight of your sales funnel by integrating directly with Folk CRM. By continuously analyzing deal stages, velocity, and stagnation, this AI workflow ensures sales teams maintain high-quality pipelines, reduce deal leakage, and accelerate revenue conversion through proactive health alerts.

---

## Demo
![Pipeline Health Monitor dashboard showing real-time deal stage tracking and risk alerts in Folk CRM](image.png)
**Alt text (SEO-ready):** Pipeline Health Monitor dashboard showing real-time deal stage tracking and risk alerts in Folk CRM, powered by Uplizd AI workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1f1bb426-fdf3-53df-8cea-4561dcce98eb)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** folk, crm, pipeline, sales operations, revenue intelligence, data hygiene, composio, ai workflow
- This solution optimizes your sales operations by transforming raw CRM data into actionable pipeline intelligence.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate blind spots in their sales process.

- **Sales Managers**
    - Gain immediate visibility into stalled deals and team performance bottlenecks.
- **RevOps Specialists**
    - Standardize pipeline hygiene and ensure data consistency across the sales cycle.
- **Account Executives**
    - Receive automated nudges on high-priority opportunities that require immediate attention.
- **Sales Enablement Leads**
    - Identify coaching opportunities based on real-time deal progression metrics.

---

## Features
- **Automated Stagnation Alerts**
    - Detects deals that have remained in the same stage beyond the defined threshold, triggering proactive follow-up notifications.
- **Folk CRM Integration**
    - Leverages the Composio Toolset to read and update deal statuses directly within your Folk CRM environment.
- **Pipeline Velocity Tracking**
    - Analyzes the time spent in each stage to provide insights into your average sales cycle duration.
- **Risk Scoring Engine**
    - Evaluates deal health based on activity recency and stage progression to prioritize high-value targets.
- **Actionable Insights Delivery**
    - Synthesizes complex CRM data into clear, natural language summaries for daily team briefings.

---

## Use Cases
**Proactive Deal Management**
- Automatically flag deals that have not been updated in the last 14 days.
- Notify the assigned owner when a high-value opportunity moves to a "Closed Lost" stage without a clear reason.

**Pipeline Hygiene Maintenance**
- Identify and clean up duplicate or stale deal records to ensure accurate forecasting.
- Ensure all active opportunities have a scheduled next-step activity logged in the CRM.

**Performance Optimization**
- Aggregate weekly stage-transition data to identify which pipeline stages cause the most friction.
- Generate summary reports for leadership highlighting the total value of "at-risk" deals.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Connect your Folk CRM account via the Composio integration settings.
3. Configure your notification preferences (e.g., Slack or Email) for pipeline alerts.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual query to analyze current pipeline status.
- **Agent**: Processes CRM data to identify health risks and summarize pipeline metrics.
- **Composio Toolset**: Executes API calls to fetch and update deal records in Folk CRM.
- **Chat Output**: Delivers the final health report or alert to the designated stakeholder.

### 3) Run the Flow
Use the Playground to test your pipeline monitoring:
- `Analyze the pipeline health for all deals in the 'Negotiation' stage.`
- `List all high-value deals that haven't been updated in the last 10 days.`
- `Summarize the current pipeline velocity for the enterprise sales team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your dedicated sales analyst.
- Use a model with strong reasoning capabilities for data interpretation.
- Instruct the agent to prioritize high-value deals in its reporting.
- Maintain a professional, objective tone for all generated alerts.

### 2) Composio Toolset Node
- Provide your Folk CRM API key to enable secure read/write access.
- Set the connection scope to allow the agent to fetch deal properties and update stage fields.

### 3) Tool Availability
- `folk_get_deals`: Retrieves current pipeline data for analysis.
- `folk_update_deal`: Updates deal status or adds internal notes based on agent findings.
- `folk_list_contacts`: Cross-references deal owners with contact information for alert routing.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects to improve deal qualification.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages to ensure consistent pipeline progression.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms to maintain a single source of truth.
