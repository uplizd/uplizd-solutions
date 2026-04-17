# Pipeline Health Monitor (Uplizd) - Automated deal velocity and stalled opportunity tracking

## Summary
The Pipeline Health Monitor is an intelligent Uplizd AI workflow designed to maintain sales velocity by proactively identifying stalled deals and automating follow-up task creation. By integrating directly with your CRM, this solution ensures that no opportunity slips through the cracks, providing RevOps teams and Sales Managers with a single source of truth for pipeline hygiene and actionable insights into deal progression.

---

## Demo
![Pipeline Health Monitor dashboard showing stalled deal alerts and automated task creation workflows](image.png)
**Alt text (SEO-ready):** Uplizd Pipeline Health Monitor dashboard displaying automated CRM deal tracking, stalled opportunity alerts, and sales workflow integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2ZmZiI+PHBhdGggZD0iTTEyIDJMMiAxMnYxMGgyMFYxMkwxMiAyeiIvPjwvc3ZnPg==)](https://uplizd.ai/solutions/675d05f2-ada1-5192-a92a-dce627b176ed)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, pipeline, sales operations, data hygiene, deal tracking, ai workflow, composio, revenue operations

This solution optimizes sales performance by automating the monitoring of deal stages and ensuring timely follow-up actions across your CRM ecosystem.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual pipeline auditing and improve conversion rates.

*   **Sales Managers**
    *   Gain real-time visibility into stalled opportunities and team performance bottlenecks.
*   **RevOps Specialists**
    *   Maintain high data hygiene standards by automating the identification of inactive records.
*   **Account Executives**
    *   Receive automated reminders to re-engage prospects before deals go cold.
*   **Sales Development Representatives (SDRs)**
    *   Prioritize daily outreach based on AI-driven signals for high-intent or at-risk deals.

---

## Features
- **Automated Stalled Deal Detection**
  Real-time monitoring of opportunity stages to flag deals that have exceeded defined inactivity thresholds.
- **Intelligent Task Generation**
  Automatically creates follow-up tasks in your CRM when a deal requires immediate attention or manual intervention.
- **CRM Integration Layer**
  Leverages the Composio Toolset to securely read and write data across major CRM platforms like Salesforce and HubSpot.
- **Customizable Threshold Logic**
  Define specific time windows and stage criteria to tailor the "health" definition to your unique sales cycle.
- **Actionable Insight Reporting**
  Delivers concise summaries of pipeline health directly to your preferred communication channels via the Chat Output node.

---

## Use Cases
**Pipeline Hygiene**
*   Automatically flag opportunities that have not been updated in over 30 days.
*   Identify deals stuck in "Negotiation" stages that lack a scheduled follow-up meeting.

**Sales Velocity Optimization**
*   Trigger instant notifications to AEs when a high-value deal moves to a "Closed Lost" risk category.
*   Automate the creation of "Check-in" tasks for leads that have gone silent for more than two weeks.

**Cross-Platform Synchronization**
*   Sync stalled deal alerts from your CRM to Slack or Microsoft Teams for immediate team visibility.
*   Update custom CRM fields based on AI-calculated risk scores to improve reporting accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Pipeline Health Monitor template from the solution library.
3. Connect your CRM credentials via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or scheduled interval signal to initiate the audit.
*   **Agent**: Analyzes CRM data against your defined health rules and determines if action is required.
*   **Composio Toolset**: Executes read/write operations to fetch deal status and create follow-up tasks.
*   **Chat Output**: Delivers the final report or confirmation of actions taken to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Check the pipeline for all opportunities in 'Negotiation' that haven't been updated in 14 days.`
* `Identify stalled deals over $50k and create a follow-up task for the assigned owner.`
* `Generate a summary report of all at-risk opportunities and post it to the sales channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your pipeline data.
*   **Role:** Sales Operations Analyst.
*   **Instruction Pattern:**
    *   Analyze deal timestamps and stage history against the provided threshold parameters.
    *   Prioritize actions based on deal value and the duration of inactivity.
    *   Maintain a neutral, professional tone when reporting findings to the sales team.

### 2) Composio Toolset Node
Requires a valid API key and authorized connection to your CRM (e.g., Salesforce, HubSpot). Ensure the scope includes read access to 'Opportunities' and write access to 'Tasks' or 'Activities'.

### 3) Tool Availability
*   **CRM Data Retrieval:** Fetching deal stages, last modified dates, and owner information.
*   **Task Management:** Creating, updating, and assigning follow-up tasks within the CRM.
*   **Notification Dispatch:** Sending alerts to external messaging platforms for real-time visibility.

---

## Related Solutions
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and follow-up sequences.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new sales opportunities.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean up and maintain CRM data integrity.
