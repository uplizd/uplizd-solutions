# Deal Pipeline Manager (Uplizd) - Automate deal progression and sales pipeline velocity

## Summary
The Deal Pipeline Manager is an intelligent Uplizd workflow designed to streamline sales operations by automating deal status updates, tracking progression, and identifying stalled opportunities. By integrating directly with your CRM, this solution ensures a single source of truth for your sales pipeline, reducing manual data entry for account executives and providing real-time visibility into revenue health for sales leadership.

---

## Demo
![Deal Pipeline Manager workflow showing CRM integration and automated status updates](image.png)
**Alt text (SEO-ready):** Deal Pipeline Manager Uplizd workflow showing CRM integration, automated sales pipeline status updates, and opportunity tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0b7bdce2-561f-5bff-8c70-562b1b0ed531)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, nocrm, sales pipeline, pipeline velocity, salesops, deal management, composio, ai workflow.
This solution optimizes the sales lifecycle by bridging the gap between active deal management and CRM data hygiene.

---

## Who is this for?
This solution is built for revenue-focused teams looking to eliminate manual pipeline maintenance and accelerate closing cycles.

* **Sales Operations Manager**
    * Automates the enforcement of pipeline stages and data entry standards across the team.
* **Account Executive**
    * Reduces time spent on administrative CRM updates, allowing more focus on high-value prospect interactions.
* **Sales Director**
    * Gains accurate, real-time insights into deal health and potential bottlenecks in the revenue funnel.
* **Revenue Operations (RevOps) Lead**
    * Ensures consistent data integrity across the sales stack for better forecasting and reporting.

---

## Features
- **Automated Stage Progression**
    Automatically advances deal stages based on trigger events or milestone completion within the CRM.
- **Stalled Deal Alerts**
    Proactively identifies opportunities that have remained stagnant in a specific stage beyond the defined threshold.
- **CRM Data Synchronization**
    Uses the Composio Toolset to ensure real-time bidirectional data flow between the agent and your CRM platform.
- **Actionable Follow-up Triggers**
    Generates automated reminders or tasks for sales reps when a deal requires immediate attention or a follow-up action.
- **Pipeline Health Analytics**
    Provides summarized insights into the overall health of the pipeline, highlighting at-risk deals and high-probability wins.

---

## Use Cases
**Pipeline Velocity Optimization**
* Automatically updating deal stages when a contract is sent or a meeting is logged.
* Flagging deals that have exceeded the average sales cycle duration for their current stage.

**Sales Team Productivity**
* Syncing meeting notes from the agent directly into the relevant CRM opportunity fields.
* Creating follow-up tasks in the CRM automatically after a discovery call is processed by the agent.

**Revenue Forecasting Accuracy**
* Cleaning up stale or "zombie" opportunities that have not seen activity in over 60 days.
* Standardizing deal probability percentages based on the current stage and recent engagement metrics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deal Pipeline Manager template from the solution library.
3. Connect your CRM credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives natural language queries or trigger signals regarding deal status.
* **Agent**: Processes CRM data and determines the necessary pipeline action.
* **Composio Toolset**: Executes read/write operations within the CRM (e.g., updating stages, creating tasks).
* **Chat Output**: Returns a confirmation summary or a list of identified stalled deals to the user.

### 3) Run the Flow
Use the Playground to test the agent's ability to manage your pipeline:
* `List all deals that have been in the 'Negotiation' stage for more than 14 days.`
* `Update the status of deal ID 5501 to 'Closed Won' and log a success note.`
* `Identify any high-value opportunities that lack a scheduled follow-up meeting.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized SalesOps assistant.
* Use a model with high reasoning capabilities to interpret complex CRM data.
* Instruction: "You are a Sales Pipeline Manager. Always verify the current CRM stage before suggesting an update."
* Instruction: "If a deal is stalled, provide the specific reason based on the last activity date."

### 2) Composio Toolset Node
* Requires a valid API key for your specific CRM (e.g., Salesforce, HubSpot, or NoCRM.io).
* Ensure the connection scope includes `read` and `write` permissions for Opportunities and Tasks.

### 3) Tool Availability
* **CRM Search/Query**: Fetching deal details and history.
* **CRM Update**: Modifying stage, probability, and close date fields.
* **Task Management**: Creating follow-up reminders for sales team members.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates deep-dive research on prospects before sales outreach.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Focuses on identifying and scoring new sales opportunities.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensures multi-platform data consistency and conflict resolution.
