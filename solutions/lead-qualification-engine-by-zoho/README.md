# Lead Qualification Engine (Uplizd) - Automate lead scoring and conversion with Zoho CRM

## Summary
The Lead Qualification Engine is an intelligent Uplizd workflow that automates the assessment, scoring, and routing of incoming leads within Zoho CRM. By leveraging AI-driven analysis, this solution ensures that sales teams focus their efforts on high-intent prospects, reducing manual data entry and accelerating pipeline velocity through real-time CRM synchronization.

---

## Demo
![Lead Qualification Engine workflow diagram showing Zoho CRM integration](image.png)
**Alt text (SEO-ready):** Lead Qualification Engine workflow for Zoho CRM using Uplizd AI and Composio for automated lead scoring and sales pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6e3d5f2e-8106-5fbb-b607-496c8814de3a)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, zoho, lead scoring, sales pipeline, data sync, composio, ai workflow, lead qualification
- This solution streamlines the sales funnel by integrating AI-powered qualification logic directly into your Zoho CRM ecosystem.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead triage and improve conversion rates.

- **Sales Development Representative (SDR)**
    - Immediately identifies high-intent leads to prioritize daily outreach efforts.
- **Sales Operations Manager**
    - Standardizes lead scoring criteria across the organization to ensure consistent data quality.
- **Revenue Operations (RevOps) Lead**
    - Reduces pipeline friction by automating the handoff between marketing and sales.
- **Account Executive (AE)**
    - Receives pre-qualified opportunities with summarized context, allowing for faster discovery calls.

---

## Features
- **Automated Lead Scoring**
    - Assigns dynamic scores to incoming leads based on custom criteria and historical conversion data.
- **Zoho CRM Integration**
    - Seamlessly pushes qualified lead data and status updates back into Zoho using the Composio Toolset.
- **Real-time Data Enrichment**
    - Automatically fetches and appends missing lead information to provide a complete 360-degree view.
- **Intelligent Routing**
    - Routes high-value leads to the appropriate account owner based on territory or industry tags.
- **Customizable Qualification Logic**
    - Easily adjust the AI agent’s decision-making parameters to match your specific business requirements.

---

## Use Cases
**Lead Prioritization**
- Automatically flags leads with high engagement scores for immediate follow-up by the sales team.
- Filters out low-quality leads and moves them to a nurture sequence to maintain a clean pipeline.

**CRM Data Hygiene**
- Standardizes lead formatting and contact details upon entry to ensure accurate reporting in Zoho.
- Detects and merges duplicate lead entries to prevent conflicting outreach efforts.

**Pipeline Velocity**
- Triggers instant notifications to sales reps when a lead meets the "Sales Ready" threshold.
- Updates lead stages in real-time, ensuring the CRM reflects the most current prospect status.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Connect your Zoho CRM account via the Composio Toolset node.
4. Ensure nodes are correctly mapped and all API credentials are saved before activating.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger events from your web forms or CRM.
- **Agent**: Analyzes lead information against your qualification criteria to determine readiness.
- **Composio Toolset**: Executes actions within Zoho CRM to update fields, create tasks, or change lead status.
- **Chat Output**: Returns a summary of the qualification result and the action taken in the CRM.

### 3) Run the Flow
Use the Playground to test your qualification logic with these prompts:
- `Qualify the latest lead from Zoho and assign a score based on company size.`
- `Check if the new lead has a valid email and update their status to 'Qualified' in Zoho.`
- `Summarize the lead's intent and create a follow-up task for the assigned sales rep.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for evaluating prospect data.
- Use a model capable of structured data extraction and logical reasoning.
- Instruct the agent to prioritize specific lead attributes like budget, authority, and timeline.
- Maintain a neutral, professional tone for all CRM-related summaries.

### 2) Composio Toolset Node
- Provide your Zoho CRM API key to enable secure read/write access.
- Set the connection scope to allow lead management and task creation permissions.

### 3) Tool Availability
- **Zoho CRM Lead Search**: Locate existing records to prevent duplication.
- **Zoho CRM Update Lead**: Modify fields based on AI qualification results.
- **Zoho CRM Task Creation**: Automate follow-up reminders for the sales team.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on prospective accounts.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and optimize your end-to-end sales pipeline stages.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple platforms.
