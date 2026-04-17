# Lead Qualification Agent (Uplizd) - Automate lead scoring and routing for Kommo CRM

## Summary
The Lead Qualification Agent is an intelligent automation workflow designed to streamline your sales pipeline by automatically evaluating incoming leads in Kommo CRM. By leveraging AI-driven analysis, this solution scores leads based on your specific business criteria, ensuring that high-intent prospects are prioritized and routed to the correct sales representatives instantly, thereby increasing conversion rates and reducing manual data entry.

---

## Demo
![Lead Qualification Agent workflow in Uplizd builder showing Kommo CRM integration](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow in Uplizd builder showing Kommo CRM integration for automated sales pipeline management and lead scoring.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fe28da9e-526d-5cad-8ad4-b5f85818d557)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, kommo, lead qualification, sales pipeline, lead scoring, automation, ai workflow, composio
- This solution bridges the gap between raw lead capture and actionable sales intelligence within the Kommo ecosystem.

---

## Who is this for?
This agent is built for revenue-focused teams looking to eliminate manual lead triage and accelerate response times.

- **Sales Managers**
    - Ensure consistent lead qualification standards across the entire team to improve forecast accuracy.
- **BDRs / SDRs**
    - Focus efforts on high-intent prospects by receiving pre-qualified leads directly in their CRM.
- **RevOps Specialists**
    - Maintain pipeline hygiene by automating the categorization and routing of incoming lead data.
- **Small Business Owners**
    - Capture and nurture every lead without the need for a dedicated manual administrative team.

---

## Features
- **Automated Lead Scoring**
    - Assigns numerical values to leads based on custom parameters like company size, industry, or engagement level.
- **Intelligent CRM Routing**
    - Automatically updates lead status and assigns owners in Kommo based on the qualification outcome.
- **Real-time Data Enrichment**
    - Uses the Composio Toolset to fetch external context, ensuring the agent makes decisions based on the latest prospect data.
- **Custom Qualification Logic**
    - Easily configure the Agent node to reflect your specific "Ideal Customer Profile" (ICP) and disqualification triggers.
- **Seamless Kommo Integration**
    - Leverages native API connectivity to perform bulk updates and status changes without leaving the Uplizd environment.

---

## Use Cases
**Pipeline Acceleration**
- Automatically move "Hot" leads to the "Discovery Call" stage in Kommo.
- Send instant Slack or email notifications to account executives when a high-value lead is qualified.

**Lead Hygiene & Cleanup**
- Flag incomplete lead profiles for manual review instead of cluttering the active sales pipeline.
- Archive or tag leads that do not meet minimum qualification criteria to keep the database focused.

**Sales Efficiency**
- Standardize the lead intake process across multiple inbound channels (web forms, chat, email).
- Reduce the "Speed to Lead" metric by automating the initial qualification handshake.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Connect your Kommo CRM account via the Composio integration settings.
4. Ensure nodes are correctly mapped: verify the **Chat Input**, **Agent**, **Composio Toolset**, and **Chat Output** are linked in the correct sequence.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger events from your CRM.
- **Agent**: Processes the data against your qualification instructions.
- **Composio Toolset**: Executes API calls to update lead fields and statuses in Kommo.
- **Chat Output**: Returns a summary of the qualification result and the action taken.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Qualify the new lead from Kommo ID 98765 based on the provided company size and industry.`
- `Review all leads in the 'New' stage and assign them to the 'Qualified' pipeline if they meet our ICP criteria.`
- `Identify any stalled leads in the pipeline and update their status to 'Nurture' if no activity is detected for 7 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your sales process.
- Define your ICP clearly in the system prompt (e.g., "Only qualify leads with >50 employees").
- Set the tone for internal logging or notifications.
- Instruct the agent to output structured data for the Composio Toolset to consume.

### 2) Composio Toolset Node
- Provide your Kommo API credentials within the Composio connection manager.
- Ensure the agent has "Write" permissions for lead fields and "Read" permissions for pipeline stages.

### 3) Tool Availability
- **Lead Retrieval**: Fetching lead details from Kommo.
- **Field Update**: Modifying lead status, tags, and owner fields.
- **Note Creation**: Adding qualification summaries to the lead activity feed.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects before outreach.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep lead data consistent across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage stages and follow-ups for active sales opportunities.
