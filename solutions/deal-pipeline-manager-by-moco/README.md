# Deal Pipeline Manager (Uplizd) - Automated sales pipeline velocity and deal stage synchronization

## Summary
The Deal Pipeline Manager is an intelligent Uplizd workflow designed to automate sales pipeline updates, track deal stage transitions, and provide real-time notifications for stalled opportunities. By leveraging the Composio Toolset, this solution ensures that your CRM remains the single source of truth, reducing manual data entry for sales teams and increasing pipeline velocity through automated hygiene and proactive status management.

---

## Demo
![Deal Pipeline Manager workflow dashboard showing automated stage transition triggers and CRM integration nodes](image.png)
**Alt text (SEO-ready):** Deal Pipeline Manager Uplizd workflow screenshot showing automated CRM sales pipeline synchronization, stage updates, and real-time deal tracking integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c96c1e40-9f42-5ba0-9cd8-a74731382bbb)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, pipeline, sales, data sync, automation, salesops, opportunity management, composio
- This solution streamlines RevOps by synchronizing deal movements across platforms to ensure accurate forecasting and reporting.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual CRM updates and improve data accuracy.

- **Sales Operations Manager**
    - Ensures pipeline data integrity and reduces manual administrative overhead for the entire sales organization.
- **Account Executive**
    - Focuses on closing deals rather than updating CRM fields, with automated triggers keeping deal stages current.
- **Sales Director**
    - Gains real-time visibility into pipeline health and stalled opportunities to better forecast quarterly revenue.
- **Revenue Operations (RevOps) Lead**
    - Standardizes the lead-to-close workflow by enforcing consistent stage progression and data hygiene across the CRM.

---

## Features
- **Automated Stage Sync**
    - Automatically updates deal stages based on predefined triggers or communication milestones within the CRM.
- **Stalled Deal Alerts**
    - Proactively identifies opportunities that have remained in a single stage beyond the defined threshold, notifying the assigned owner.
- **Composio-Powered CRM Integration**
    - Utilizes the Composio Toolset to securely connect with leading CRM platforms for real-time read/write operations.
- **Pipeline Hygiene Monitoring**
    - Cleans up orphaned or misclassified deals to ensure reporting metrics remain accurate and actionable.
- **Custom Notification Logic**
    - Triggers alerts via email or Slack when high-value deals move to critical stages or require immediate attention.

---

## Use Cases
**Pipeline Velocity Optimization**
- Automatically advance deals to the "Negotiation" stage once a contract document is uploaded to the CRM.
- Flag deals that have not had a touchpoint in over 14 days to prevent pipeline decay.

**Sales Data Integrity**
- Standardize deal naming conventions and field formatting across global sales territories.
- Map custom CRM fields to ensure consistent data flow between marketing and sales modules.

**Opportunity Management**
- Notify the sales team when a high-value opportunity is marked as "Closed-Lost" to trigger a win-back campaign.
- Automatically assign follow-up tasks to BDRs when a lead moves from "Discovery" to "Qualified."

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the **Deal Pipeline Manager**.
2. Click "Import" to load the workflow template into your workspace.
3. Connect your CRM credentials via the Composio integration settings.
4. Ensure nodes are correctly mapped and all API connections are authorized before activating the flow.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or system-generated events for deal updates.
- **Agent**: Processes the logic to determine the correct CRM stage based on the input data.
- **Composio Toolset**: Executes the API calls to update the CRM records securely.
- **Chat Output**: Confirms the successful update or logs errors for the user.

### 3) Run the Flow
Use the Playground to test your pipeline logic:
- `Update deal ID 12345 to 'Negotiation' stage and notify the owner.`
- `List all stalled deals in the 'Discovery' stage that haven't been updated in 10 days.`
- `Check for missing mandatory fields in all open opportunities for the current quarter.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for CRM interactions, interpreting natural language requests into structured API calls.
- Use a model capable of high-precision instruction following (e.g., GPT-4o or Claude 3.5 Sonnet).
- Maintain a system prompt that emphasizes CRM field mapping accuracy.
- Ensure the agent is instructed to prioritize data validation before executing write operations.

### 2) Composio Toolset Node
- Provide your CRM API key within the Composio dashboard.
- Set the connection scope to include read/write access for "Deals," "Opportunities," and "Tasks."

### 3) Tool Availability
- **CRM Search/Query**: Locate specific deal IDs and associated metadata.
- **Record Update**: Modify stage, close date, and custom field values.
- **Notification Dispatch**: Send alerts to Slack or Email channels upon status changes.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects and accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep multi-platform CRM data synchronized in real-time.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score high-potential sales opportunities.
