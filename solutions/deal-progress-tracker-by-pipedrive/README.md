# Deal Progress Tracker (Uplizd) - Automate sales pipeline health and follow-up workflows

## Summary
The Deal Progress Tracker is an intelligent Uplizd AI workflow designed to monitor sales pipeline velocity and automate critical follow-up actions within Pipedrive. By integrating real-time CRM data with autonomous agent logic, this solution ensures that no opportunity stalls, providing sales teams with a single source of truth for deal health, improved pipeline hygiene, and accelerated conversion rates.

---

## Demo
![Deal Progress Tracker workflow dashboard showing automated Pipedrive deal status updates and follow-up notifications](image.png)

**Alt text (SEO-ready):** Uplizd Deal Progress Tracker workflow for Pipedrive, automating sales pipeline management, deal health monitoring, and CRM data synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b42130a1-4f9b-5975-bb80-cb51f415debb)

---

## Category
*   **Primary category:** Sales automation
*   **Secondary tags:** `pipedrive`, `crm`, `sales pipeline`, `deal management`, `automation`, `composio`, `ai workflow`, `revenue operations`

This solution bridges the gap between static CRM data and proactive sales management by automating the tracking and progression of deal stages.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual CRM updates and improve deal visibility.

*   **Sales Managers**
    *   Gain real-time visibility into stalled deals and team performance metrics.
*   **Account Executives**
    *   Automate routine follow-up tasks to focus on high-value closing activities.
*   **Revenue Operations (RevOps)**
    *   Maintain pipeline hygiene through automated data validation and stage tracking.
*   **Sales Development Reps (SDRs)**
    *   Receive instant notifications when deal status changes require immediate outreach.

---

## Features
- **Automated Deal Monitoring**
  Continuously scan Pipedrive for updates, ensuring deal stages and custom fields remain current without manual intervention.
- **Intelligent Follow-up Triggers**
  Automatically initiate outreach or internal alerts when a deal remains in a specific stage beyond the defined threshold.
- **Composio-Powered CRM Integration**
  Leverage the Composio Toolset to execute complex read/write operations directly within Pipedrive via secure API connections.
- **Pipeline Health Analytics**
  Identify bottlenecks in the sales funnel by analyzing time-in-stage metrics and flagging inactive opportunities.
- **Unified Workflow Orchestration**
  Seamlessly connect Chat Input and Output nodes to provide human-in-the-loop oversight for automated CRM actions.

---

## Use Cases
**Pipeline Velocity Optimization**
*   Automatically flag deals that have exceeded the average sales cycle duration for their current stage.
*   Trigger a "stalled deal" alert to the assigned owner when no activity is logged for over 7 days.

**Automated Sales Administration**
*   Update deal probability scores based on recent interactions captured in Pipedrive.
*   Sync meeting outcomes from calendar events directly into the corresponding deal notes.

**Proactive Opportunity Management**
*   Send personalized follow-up reminders to prospects when a deal moves to the "Negotiation" stage.
*   Notify management when high-value deals are marked as "Lost" to facilitate immediate post-mortem analysis.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deal Progress Tracker template file.
3. Connect your Pipedrive account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual query regarding deal status.
*   **Agent**: Processes CRM data and determines the necessary follow-up action based on defined business logic.
*   **Composio Toolset**: Executes Pipedrive API calls to fetch deal details or update stage information.
*   **Chat Output**: Delivers a summary of the action taken or a status report to the user.

### 3) Run the Flow
Use the Playground to test your pipeline logic with the following prompts:
*   `"Check for any deals in the 'Negotiation' stage that haven't been updated in 5 days."`
*   `"Summarize the pipeline health for the current quarter and identify top 3 stalled deals."`
*   `"Update the status of deal ID 12345 to 'Closed Won' and trigger the follow-up email sequence."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting CRM data and deciding on the appropriate sales action.
*   Maintain a professional, action-oriented tone.
*   Prioritize data accuracy when parsing Pipedrive fields.
*   Focus on identifying actionable insights rather than raw data dumps.

### 2) Composio Toolset Node
Requires a valid Pipedrive API key configured within the Composio platform. Ensure the connection scope includes read/write access to `deals`, `persons`, and `activities`.

### 3) Tool Availability
*   `pipedrive_get_deal`: Retrieve specific deal metadata.
*   `pipedrive_update_deal`: Modify deal stages or custom fields.
*   `pipedrive_list_activities`: Audit recent interactions for deal health checks.
*   `pipedrive_search_deals`: Locate deals based on owner or status filters.

---

## Related Solutions
*   [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manage complex B2B account hierarchies and stakeholder mapping.
*   [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new sales opportunities based on lead signals.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize multi-platform CRM data with conflict resolution.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate data cleanup and formatting for improved CRM integrity.
