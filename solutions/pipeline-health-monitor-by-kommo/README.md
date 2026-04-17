# Pipeline Health Monitor (Uplizd) - Real-time sales pipeline optimization and deal velocity tracking

## Summary
The Pipeline Health Monitor by Kommo is an intelligent automation workflow designed to track deal progression, identify stalled opportunities, and trigger corrective actions. By leveraging the Composio Toolset to interface with your CRM, this solution provides a single source of truth for sales operations, ensuring pipeline hygiene and accelerating deal velocity through automated status updates and proactive team alerts.

---

## Demo
![Pipeline Health Monitor dashboard showing real-time deal status, stalled opportunity alerts, and automated CRM update triggers](image.png)
**Alt text (SEO-ready):** Pipeline Health Monitor dashboard showing real-time deal status, stalled opportunity alerts, and automated CRM update triggers via Uplizd and Kommo.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6e93932f-4c7d-524e-ac9b-b41747f1db6a)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** `kommo`, `crm`, `pipeline`, `sales operations`, `deal velocity`, `automation`, `composio`, `ai workflow`
- This solution bridges the gap between raw CRM data and actionable sales intelligence to maintain a healthy, high-velocity pipeline.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual CRM maintenance and improve conversion rates.

- **Sales Managers**
    - Gain visibility into stalled deals and team performance bottlenecks to coach effectively.
- **RevOps Specialists**
    - Automate data hygiene and pipeline reporting to ensure CRM accuracy without manual entry.
- **Account Executives**
    - Receive proactive notifications on at-risk opportunities to prioritize high-impact outreach.
- **Sales Development Reps**
    - Focus on qualified leads by automating the movement of deals through defined pipeline stages.

---

## Features
- **Real-time Pipeline Auditing**
    - Automatically scan CRM deal stages to identify opportunities that have exceeded expected cycle times.
- **Automated Status Updates**
    - Trigger CRM field updates based on AI-driven analysis of recent communication and activity logs.
- **Proactive Stalled Deal Alerts**
    - Notify team members via integrated channels when a deal requires immediate attention to prevent churn.
- **Composio-Powered CRM Integration**
    - Seamlessly execute read/write operations across Kommo and other CRM platforms using secure toolset connectors.
- **Customizable Health Scoring**
    - Define and apply specific logic to score deal health based on engagement frequency and stage progression.

---

## Use Cases
**Pipeline Hygiene Management**
- Automatically flag deals that have remained in the "Negotiation" stage for more than 14 days.
- Update "Last Contacted" fields based on recent email or chat interactions synced via the agent.

**Deal Velocity Acceleration**
- Trigger an automated follow-up task for the assigned owner when a deal moves to a "Closed-Lost" risk category.
- Identify and highlight "Hot" opportunities that show high engagement signals but lack recent activity logs.

**Sales Operations Reporting**
- Generate weekly summaries of pipeline health metrics to identify common drop-off points in the sales funnel.
- Sync deal status changes across multiple platforms to ensure consistent reporting for cross-functional teams.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Pipeline Health Monitor template from the solution gallery.
3. Connect your Kommo account and any secondary CRM tools via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled cron-job signals to initiate the audit.
- **Agent**: Analyzes CRM data against defined health criteria to determine necessary actions.
- **Composio Toolset**: Executes API calls to fetch deal data and perform updates in Kommo.
- **Chat Output**: Delivers status reports and alerts to the designated sales dashboard or communication channel.

### 3) Run the Flow
Use the Playground to test the agent's ability to interpret your pipeline data:
- `Scan the pipeline for all deals in 'Negotiation' that haven't been updated in 7 days.`
- `Update the status of stalled deals in the 'Prospecting' stage to 'At Risk'.`
- `Summarize the current health of the Q4 sales pipeline and highlight top 3 priorities.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a sales operations analyst.
- Use a model with strong reasoning capabilities to interpret CRM field data.
- **Recommended instruction pattern:**
    - "You are a sales pipeline expert; analyze the provided CRM data for inactivity."
    - "Prioritize deals based on deal value and time spent in the current stage."
    - "Only perform updates when specific threshold criteria are met."

### 2) Composio Toolset Node
- Authenticate the node using your Kommo API key.
- Set the connection scope to allow read/write access to `deals`, `contacts`, and `tasks`.

### 3) Tool Availability
- `kommo_get_deals`: Retrieve current pipeline records.
- `kommo_update_deal`: Modify deal stages or custom fields.
- `kommo_list_tasks`: Check for existing follow-ups to avoid duplicate alerts.
- `crm_search_contacts`: Cross-reference deal owners with contact information.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and follow-ups for improved sales efficiency.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new opportunities to maximize growth.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean up CRM data decay and maintain high-quality records.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across multiple CRM platforms for a unified view.
