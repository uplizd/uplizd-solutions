# Deal Pipeline Manager (Uplizd) - Automate deal progression and pipeline health

## Summary
The Deal Pipeline Manager is an intelligent Uplizd workflow designed to streamline sales operations by automating deal stage transitions, monitoring pipeline velocity, and flagging stalled opportunities. By integrating directly with your CRM, this solution ensures data hygiene and provides real-time visibility into sales health, allowing teams to focus on high-impact closing activities rather than manual administrative updates.

---

## Demo
![Deal Pipeline Manager workflow showing CRM integration and automated stage progression](image.png)
**Alt text (SEO-ready):** Deal Pipeline Manager workflow in Uplizd, showing automated CRM integration, pipeline velocity tracking, and sales opportunity management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/99915945-d8c1-5321-bafb-4b61341db264)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, pipeline, sales operations, data hygiene, opportunity management, composio, ai workflow, revenue operations
This solution bridges the gap between raw CRM data and actionable sales insights, ensuring your pipeline remains accurate and optimized for growth.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual CRM data entry and improve forecast accuracy.

* **Sales Operations Manager**
    * Automates complex pipeline reporting and ensures data consistency across global sales territories.
* **Account Executive**
    * Reduces administrative overhead by automatically updating deal stages based on meeting outcomes and email signals.
* **Sales Director**
    * Gains immediate visibility into stalled deals and pipeline health metrics to make data-driven coaching decisions.
* **Revenue Operations Analyst**
    * Maintains high-quality CRM data hygiene by enforcing standardized stage progression and documentation requirements.

---

## Features
- **Automated Stage Progression**
    Trigger deal updates automatically based on specific milestones or client interactions captured in your CRM.
- **Stalled Deal Alerts**
    Proactively identify opportunities that have remained stagnant in a specific stage beyond the defined threshold.
- **CRM Data Synchronization**
    Leverage the Composio Toolset to maintain real-time bidirectional sync between your communication channels and CRM records.
- **Pipeline Velocity Tracking**
    Calculate the time spent in each stage to identify bottlenecks and optimize the overall sales cycle duration.
- **Actionable Insight Generation**
    Provide AI-driven summaries of deal health, highlighting potential risks and recommended next steps for the sales team.

---

## Use Cases
**Pipeline Health Monitoring**
* Automatically flag deals that have not had activity for more than 14 days.
* Generate weekly reports on the conversion rates between key pipeline stages.

**Sales Process Enforcement**
* Ensure all required fields are populated before a deal can be moved to the "Negotiation" stage.
* Trigger follow-up tasks for account owners when a deal is marked as "Closed-Lost" to gather feedback.

**Automated Administrative Cleanup**
* Sync meeting notes from calendar events directly to the corresponding CRM opportunity record.
* Standardize naming conventions for new deals created through inbound lead channels.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deal Pipeline Manager template using the provided solution URL.
3. Connect your CRM account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives manual triggers or automated webhooks from your CRM.
* **Agent**: Processes deal data, evaluates stage criteria, and formulates update actions.
* **Composio Toolset**: Executes precise API calls to update CRM records, fetch deal history, and log activities.
* **Chat Output**: Returns a confirmation summary of the actions taken or alerts the user to required manual interventions.

### 3) Run the Flow
Use the Playground to test your pipeline logic with these prompts:
* `Check for any stalled deals in the 'Proposal' stage and summarize their status.`
* `Update the deal for 'Acme Corp' to 'Closed-Won' and log the final contract value.`
* `Identify all opportunities that have been inactive for over 20 days and create a follow-up task.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your virtual sales operations assistant, interpreting CRM data and executing logic.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Set system instructions to prioritize data accuracy and CRM field mapping.
* Configure the agent to output structured JSON for reliable tool execution.

### 2) Composio Toolset Node
* Provide your CRM API key within the Composio connection settings.
* Ensure the connection scope includes read/write permissions for Deals, Contacts, and Activities.

### 3) Tool Availability
* **CRM Read/Write**: Fetch and update deal stages, owners, and custom fields.
* **Calendar Integration**: Sync meeting timestamps to validate deal activity.
* **Notification Service**: Send alerts to Slack or Email when a deal is flagged as stalled.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts to improve lead qualification.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new sales opportunities based on real-time lead signals.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain consistent data across multiple platforms with automated conflict resolution.
