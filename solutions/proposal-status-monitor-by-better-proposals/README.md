# Proposal Status Monitor (Uplizd) - Automated tracking and follow-up for Better Proposals

## Summary
The Proposal Status Monitor is an intelligent Uplizd AI workflow that tracks the engagement status of your Better Proposals documents in real-time. By automating the monitoring of client interactions, this solution ensures your sales team never misses a follow-up window, maintaining high pipeline velocity and improving deal conversion rates through timely, data-driven communication.

---

## Demo
![Proposal Status Monitor dashboard showing real-time document engagement tracking and automated follow-up triggers](image.png)
**Alt text (SEO-ready):** Proposal Status Monitor dashboard showing real-time document engagement tracking, automated follow-up triggers, Uplizd AI workflow, and Better Proposals integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8d243157-095a-5f5b-b6c7-236e4dfc1b7b)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, better proposals, sales, pipeline, follow-up, document tracking, ai workflow, composio
- This solution bridges the gap between document engagement and sales outreach, ensuring your team acts on client interest the moment it happens.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual administrative overhead and accelerate the closing process.

- **Account Executives**
    - Receive instant notifications when a prospect opens or signs a proposal to time their outreach perfectly.
- **Sales Managers**
    - Gain visibility into stalled proposals and team follow-up performance across the entire sales department.
- **Revenue Operations (RevOps)**
    - Standardize the follow-up cadence across the organization to ensure consistent brand communication.
- **Customer Success Managers**
    - Monitor document engagement to identify potential friction points during the contract renewal or expansion phase.

---

## Features
- **Real-time Engagement Tracking**
    - Automatically syncs document status updates from Better Proposals to trigger immediate workflow actions.
- **Intelligent Follow-up Triggers**
    - Uses AI to determine the optimal time to send a follow-up email based on prospect activity levels.
- **Composio-Powered CRM Sync**
    - Seamlessly updates your CRM records with the latest proposal status, ensuring a single source of truth.
- **Automated Alerting System**
    - Sends proactive notifications to Slack or email when a high-value proposal is viewed or signed.
- **Customizable Outreach Templates**
    - Dynamically generates personalized follow-up messages based on the specific document and prospect context.

---

## Use Cases
**Pipeline Acceleration**
- Automatically trigger a follow-up task in your CRM when a proposal remains in 'Sent' status for more than 48 hours.
- Notify the assigned account owner the moment a client opens a proposal for the third time to capitalize on high intent.

**Data Hygiene & Reporting**
- Sync document status changes back to your CRM to keep deal stages accurate without manual data entry.
- Generate weekly reports on proposal conversion rates to identify which document templates perform best.

**Client Relationship Management**
- Send a personalized "Thank You" note automatically once a proposal is digitally signed by the client.
- Identify stalled deals by monitoring long periods of inactivity on sent documents and flagging them for manager review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and click "Import Flow."
3. Connect your Better Proposals and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped and all required API credentials are authenticated in the settings panel.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request to check proposal statuses.
- **Agent**: Analyzes the document engagement data and determines the necessary follow-up action.
- **Composio Toolset**: Executes actions within Better Proposals and your CRM (e.g., updating deal stages or sending emails).
- **Chat Output**: Confirms the action taken and provides a summary of the updated proposal status.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check the status of all proposals sent in the last 3 days and list those that haven't been opened.`
- `If a proposal is marked as 'Signed', update the CRM deal stage to 'Closed Won' and notify the sales team.`
- `Draft a follow-up email for the proposal sent to [Client Name] that has been viewed but not signed.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for interpreting document signals and drafting communications.
- **Instruction Pattern:**
    - "Monitor Better Proposals for status changes and map them to CRM deal stages."
    - "Draft professional, context-aware follow-up emails based on the prospect's interaction history."
    - "Prioritize actions based on deal value and the recency of client engagement."

### 2) Composio Toolset Node
- **API Key:** Provide your unique Composio API key to enable secure integration with your tools.
- **Connection Scope:** Ensure the connection has read/write access to your Better Proposals account and your primary CRM (e.g., Salesforce or HubSpot).

### 3) Tool Availability
- **Better Proposals API**: For fetching document status, view counts, and signature timestamps.
- **CRM Connector**: For updating deal records, creating tasks, and logging communication history.
- **Notification Service**: For sending Slack or email alerts to the sales team.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and optimize your sales pipeline stages and follow-up cadences.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent data across multiple platforms with automated conflict resolution.
- [Account Research Agent](../account-research-agent/README.md) - Gather deep intelligence on prospects to personalize your sales outreach.
