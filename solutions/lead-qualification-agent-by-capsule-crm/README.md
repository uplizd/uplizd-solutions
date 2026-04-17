# Lead Qualification Agent (Uplizd) - Automate lead scoring and CRM pipeline management

## Summary
The Lead Qualification Agent by Capsule CRM is an intelligent Uplizd workflow designed to streamline your sales pipeline by automatically vetting incoming leads. By leveraging real-time data enrichment and predefined scoring criteria, this solution ensures that your sales team focuses only on high-intent prospects, reducing manual data entry and accelerating lead-to-opportunity conversion rates.

---

## Demo
![Lead Qualification Agent workflow showing Chat Input, Agent node, Capsule CRM toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow in Uplizd for Capsule CRM, featuring automated lead scoring, data enrichment, and sales pipeline management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGwSgYBaNgFIyCUUADAAAEAAAB0mJkAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/518e8d1e-abac-52ee-aee9-749b64397006)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, capsule crm, lead qualification, sales pipeline, lead scoring, data enrichment, composio, ai workflow
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the qualification process within Capsule CRM.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead triage and improve pipeline velocity.

- **Sales Development Reps (SDRs)**
    - Spend less time on manual research and more time engaging with high-probability prospects.
- **Revenue Operations (RevOps) Managers**
    - Ensure consistent lead scoring logic and data hygiene across the entire sales funnel.
- **Account Executives (AEs)**
    - Receive pre-qualified leads with enriched context, allowing for more personalized outreach.
- **Sales Managers**
    - Gain visibility into lead quality trends and optimize team capacity based on real-time pipeline data.

---

## Features
- **Automated Lead Scoring**
    - Assigns dynamic scores to incoming leads based on custom criteria and interaction history.
- **Real-time CRM Integration**
    - Seamlessly syncs qualified lead data directly into Capsule CRM using the Composio Toolset.
- **Intelligent Data Enrichment**
    - Automatically fetches missing prospect details to provide a complete 360-degree view of the lead.
- **Custom Qualification Logic**
    - Allows users to define specific business rules for what constitutes a "Marketing Qualified Lead" (MQL) or "Sales Qualified Lead" (SQL).
- **Instant Notification Alerts**
    - Triggers immediate updates to the sales team when a high-priority lead is identified and qualified.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads with high engagement scores for immediate follow-up by the sales team.
- Route low-intent leads to automated nurture sequences to keep the pipeline clean.

**Data Hygiene & Enrichment**
- Standardize lead contact information formats across your Capsule CRM database.
- Automatically append company size and industry data to new lead records for better segmentation.

**Pipeline Velocity**
- Reduce the time from lead capture to first contact by automating the initial qualification phase.
- Eliminate manual data entry errors by syncing lead status changes directly from the agent to the CRM.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the Lead Qualification Agent workflow.
3. Authenticate your Capsule CRM connection within the Composio Toolset node.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger signals from your web forms.
- **Agent**: Analyzes lead information against your qualification criteria and determines the next action.
- **Composio Toolset**: Executes CRM operations like updating lead status, adding notes, or creating tasks in Capsule CRM.
- **Chat Output**: Provides a summary of the qualification result and any actions taken in the CRM.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Qualify the new lead from John Doe at Acme Corp based on the latest form submission.`
- `Check the lead score for the latest entry in Capsule CRM and update the status to 'Qualified' if the score is above 80.`
- `Enrich the contact information for the lead 'Sarah Smith' and notify the sales team if she is a decision-maker.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the decision engine for lead triage.
- Set the system prompt to define your specific qualification criteria (e.g., budget, authority, need, timeline).
- Configure the temperature to 0.2 for consistent, logic-driven qualification decisions.
- Ensure the agent has access to the latest lead schema from your CRM.

### 2) Composio Toolset Node
- Provide your Capsule CRM API key within the Composio configuration.
- Ensure the connection scope includes read/write permissions for Leads, Contacts, and Tasks.

### 3) Tool Availability
- **Lead Search**: Locate existing records to prevent duplicates.
- **Lead Update**: Modify status, scoring fields, and stage information.
- **Task Creation**: Automatically assign follow-up tasks to the appropriate sales rep.
- **Note Append**: Add qualification summaries directly to the lead profile.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your CRM data consistent across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and optimize your sales pipeline stages effectively.
