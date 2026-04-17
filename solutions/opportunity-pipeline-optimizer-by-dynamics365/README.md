# Opportunity Pipeline Optimizer (Uplizd) - Accelerate sales velocity with automated Dynamics 365 pipeline management

## Summary
The Opportunity Pipeline Optimizer is an intelligent Uplizd workflow designed to streamline sales operations by automating the tracking, qualification, and stage progression of opportunities within Microsoft Dynamics 365. By leveraging AI-driven insights, this solution helps RevOps teams and Account Executives maintain a clean, high-velocity pipeline, ensuring that stalled deals are identified and active opportunities are updated in real-time to provide a single source of truth for sales forecasting.

---

## Demo
![Opportunity Pipeline Optimizer dashboard showing automated stage progression and deal health scoring in Dynamics 365](image.png)
**Alt text (SEO-ready):** Uplizd Opportunity Pipeline Optimizer workflow automating Dynamics 365 sales pipeline updates, deal tracking, and CRM data hygiene.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQ45115QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZ4AAAA+SURBVEjHY2AYBaNgFIyCUUAAwAABAAAB)](https://uplizd.ai/solutions/99c03dfd-e540-5152-b584-768a25c99898)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, dynamics365, pipeline, sales operations, revenue operations, ai workflow, composio, data hygiene
- This solution bridges the gap between manual CRM entry and automated pipeline management to improve forecast accuracy.

---

## Who is this for?
This solution is built for revenue-focused teams looking to reduce administrative overhead and increase win rates.

- **Sales Operations Manager**
    - Automates pipeline hygiene and ensures consistent data entry across the entire sales organization.
- **Account Executive**
    - Reduces time spent on manual CRM updates, allowing more focus on high-value prospect interactions.
- **Revenue Operations (RevOps) Lead**
    - Provides real-time visibility into deal health and pipeline velocity to improve quarterly forecasting.
- **Sales Director**
    - Identifies stalled opportunities early to implement corrective coaching and strategy adjustments.

---

## Features
- **Automated Stage Progression**
    - Automatically updates opportunity stages in Dynamics 365 based on predefined activity triggers and milestone completion.
- **Real-time Pipeline Health Scoring**
    - Analyzes deal movement and engagement data to assign health scores, highlighting at-risk opportunities for immediate attention.
- **Composio-Powered CRM Integration**
    - Utilizes the Composio Toolset to securely execute read/write operations directly within your Dynamics 365 environment.
- **Stalled Deal Alerts**
    - Proactively notifies the sales team when an opportunity remains stagnant in a stage beyond the expected duration.
- **Data Hygiene Enforcement**
    - Standardizes field inputs and ensures mandatory data points are captured before an opportunity can progress to the next stage.

---

## Use Cases
**Pipeline Velocity Optimization**
- Automatically advance opportunities to the "Negotiation" stage once a contract draft is uploaded to the CRM.
- Flag deals that have not seen activity in over 14 days for immediate follow-up by the assigned Account Executive.

**Sales Data Integrity**
- Validate that all required fields, such as "Budget" and "Decision Maker," are populated before moving a lead to "Qualified."
- Sync meeting notes from external calendars into the relevant Dynamics 365 opportunity records to maintain a complete history.

**Forecasting Accuracy**
- Aggregate weighted revenue projections based on current opportunity stages and historical close rates.
- Generate weekly summaries of pipeline movement to identify trends in deal conversion and cycle time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Opportunity Pipeline Optimizer template file.
3. Connect your Microsoft Dynamics 365 account via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language commands or automated triggers from your CRM.
- **Agent**: Interprets the intent, evaluates the deal status, and determines the necessary CRM action.
- **Composio Toolset**: Executes the specific Dynamics 365 API calls to update records or fetch opportunity data.
- **Chat Output**: Returns a confirmation message or summary of the action performed to the user.

### 3) Run the Flow
Use the Playground to test your workflow with the following prompts:
- `Update the opportunity 'Acme Corp' to stage 'Proposal Sent' and add a note about the meeting.`
- `List all stalled opportunities in the 'Discovery' stage that haven't been updated in 10 days.`
- `What is the total weighted pipeline value for the current quarter?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for your CRM operations.
- Use a model capable of structured reasoning (e.g., GPT-4o).
- Instruction: "You are a CRM assistant. Always verify the opportunity ID before performing updates."
- Instruction: "If a required field is missing, ask the user to provide the data before proceeding with the pipeline update."

### 2) Composio Toolset Node
- Provide your Dynamics 365 API key within the Composio configuration.
- Set the connection scope to allow read/write access to `Opportunities`, `Accounts`, and `Contacts`.

### 3) Tool Availability
- `dynamics365_get_opportunity`: Fetch current deal status and metadata.
- `dynamics365_update_opportunity_stage`: Modify the pipeline stage of a specific record.
- `dynamics365_add_note`: Attach context or meeting summaries to the CRM record.
- `dynamics365_list_stalled_deals`: Query the CRM for opportunities exceeding defined time-in-stage limits.

---

## Related Solutions
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Build and maintain deep relationships with key accounts.
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Automate the onboarding and setup process for new CRM accounts.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms and tools.
