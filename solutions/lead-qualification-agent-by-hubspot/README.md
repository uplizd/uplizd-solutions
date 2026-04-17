# Lead Qualification Agent (Uplizd) - Automate lead scoring and routing for HubSpot CRM

## Summary
The Lead Qualification Agent is an intelligent Uplizd workflow designed to streamline your sales pipeline by automatically evaluating incoming leads against your ideal customer profile. By leveraging the Composio Toolset to interface directly with HubSpot, this agent scores leads in real-time, updates CRM fields, and routes high-intent prospects to the appropriate sales representatives, ensuring your team focuses their energy on the most promising opportunities.

---

## Demo
![Lead Qualification Agent workflow diagram showing HubSpot integration and automated scoring logic](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow diagram for HubSpot CRM, showing automated lead scoring, data synchronization, and sales routing using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=appveyor)](https://uplizd.ai/solutions/bbff928c-8554-5d69-9546-71cd1ae56671)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** hubspot, lead scoring, crm, sales pipeline, lead routing, data hygiene, composio, ai workflow
- This solution bridges the gap between raw lead intake and actionable sales intelligence, turning manual data entry into a high-velocity automated pipeline.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to eliminate manual lead triage and improve response times.

- **Sales Development Representative (SDR)**
    - Receives only pre-qualified, high-intent leads to maximize daily outreach efficiency.
- **Revenue Operations Manager**
    - Standardizes lead scoring criteria across the organization to ensure consistent data hygiene.
- **Sales Manager**
    - Gains visibility into pipeline velocity by automating the assignment of leads to the right account owners.
- **Marketing Operations Specialist**
    - Ensures that marketing-qualified leads (MQLs) are seamlessly transitioned to sales without manual intervention.

---

## Features
- **Automated Lead Scoring**
    - Evaluates incoming lead data against custom business rules to assign a priority score instantly.
- **HubSpot CRM Integration**
    - Uses the Composio Toolset to read lead properties and write qualification statuses back to HubSpot in real-time.
- **Intelligent Routing Logic**
    - Dynamically assigns leads to specific sales reps based on territory, company size, or lead score thresholds.
- **Data Enrichment & Hygiene**
    - Cleans and validates contact information during the qualification process to prevent duplicate or incomplete records.
- **Real-time Notification Triggers**
    - Alerts relevant stakeholders via Slack or email when a high-value lead is qualified and ready for immediate follow-up.

---

## Use Cases
**Pipeline Acceleration**
- Automatically flagging "Hot" leads for immediate outreach within 5 minutes of form submission.
- Updating lead status fields in HubSpot to reflect qualification stages without manual CRM updates.

**Lead Management**
- Filtering out low-quality or spam entries based on domain or job title patterns.
- Re-assigning stale leads to a general nurture queue if they fail to meet initial qualification criteria.

**Sales Operations**
- Balancing lead distribution across the sales team based on current capacity and performance metrics.
- Syncing lead qualification notes directly into the CRM activity log for better context during discovery calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Qualification Agent template from the marketplace.
3. Connect your HubSpot account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event from HubSpot webhooks containing lead data.
- **Agent**: Processes the lead information using your custom qualification instructions.
- **Composio Toolset**: Executes CRM actions like `update_lead_status` or `assign_owner`.
- **Chat Output**: Confirms the qualification result and logs the action taken.

### 3) Run the Flow
Use the Playground to test your logic with these example prompts:
- `Qualify this lead: { "email": "prospect@example.com", "company_size": 500, "industry": "SaaS" }`
- `Check if this lead meets the criteria for an Enterprise account and update the HubSpot status to 'Qualified'.`
- `Analyze the last 5 leads in the queue and route them based on the current lead scoring model.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your qualification logic.
- **Instruction Pattern:**
    - Define clear threshold values for "Hot," "Warm," and "Cold" leads.
    - Instruct the agent to extract specific fields (e.g., job title, company revenue) from the input.
    - Specify the exact CRM field names to update in HubSpot to ensure data mapping accuracy.

### 2) Composio Toolset Node
- Provide your HubSpot API Key or OAuth credentials within the Composio configuration.
- Set the connection scope to allow read/write access to `contacts`, `companies`, and `deals` objects.

### 3) Tool Availability
- `hubspot_get_contact`: Retrieve detailed lead information.
- `hubspot_update_contact`: Update lead status and qualification scores.
- `hubspot_assign_owner`: Reallocate leads to specific sales representatives.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and optimize sales pipeline stages and follow-ups.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple CRM platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and compliant CRM records through automated cleanup.
