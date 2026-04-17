# Lead Qualification Assistant (Uplizd) - Automate lead scoring and CRM pipeline routing

## Summary
The Lead Qualification Assistant is an intelligent Uplizd workflow designed to streamline your sales pipeline by automatically evaluating, scoring, and tagging incoming leads from Zoho Bigin. By leveraging AI-driven analysis, this solution ensures that high-intent prospects are prioritized for immediate follow-up, reducing manual data entry and increasing pipeline velocity for sales teams.

---

## Demo
![Lead Qualification Assistant workflow diagram showing Zoho Bigin lead ingestion, AI scoring, and CRM tag updates](image.png)
**Alt text (SEO-ready):** Lead Qualification Assistant workflow for Zoho Bigin, featuring automated AI lead scoring, CRM data synchronization, and pipeline management via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/abaee49e-a71b-5350-860f-496df5f91031)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, zoho bigin, lead qualification, sales pipeline, lead scoring, ai workflow, composio, revenue operations
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the qualification process within your CRM.

---

## Who is this for?
This assistant is designed for revenue-focused teams looking to eliminate manual lead triage and focus on high-conversion opportunities.

- **Sales Development Representative (SDR)**
    - Spend less time manually researching prospects and more time engaging with qualified leads.
- **Revenue Operations Manager**
    - Maintain consistent data hygiene and qualification standards across the entire sales funnel.
- **Sales Manager**
    - Ensure your team is always working on the highest-priority deals with accurate, AI-generated scores.
- **Small Business Owner**
    - Automate the initial lead vetting process to ensure no potential customer falls through the cracks.

---

## Features
- **Automated Lead Scoring**
    - Uses AI to assign a numerical value to leads based on custom criteria and historical conversion data.
- **Zoho Bigin Integration**
    - Seamlessly reads and writes lead data directly to your Zoho Bigin environment using the Composio Toolset.
- **Dynamic Tagging**
    - Automatically applies CRM tags (e.g., "Hot," "Cold," "Qualified") based on the agent's qualification logic.
- **Real-time Pipeline Updates**
    - Updates lead status in real-time, ensuring the sales team has the most current information available.
- **Customizable Qualification Criteria**
    - Easily adjust the agent's instructions to match your specific industry requirements and buyer personas.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads as "Priority" if they match specific job title or company size parameters.
- Move leads to a "Nurture" stage if they do not meet initial qualification thresholds.

**Data Enrichment & Hygiene**
- Standardize lead entry formatting to ensure consistent reporting across the sales dashboard.
- Append missing contact context by cross-referencing lead information during the qualification flow.

**Sales Pipeline Velocity**
- Trigger instant notifications for the sales team when a "High Intent" lead is identified.
- Reduce the time-to-first-contact by automating the initial triage of incoming web-to-lead submissions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Assistant template from the solution library.
3. Connect your Zoho Bigin account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead data payload from your CRM or web form.
- **Agent**: Analyzes the lead data against your predefined qualification rules.
- **Composio Toolset**: Executes CRM updates, such as tagging or status changes, in Zoho Bigin.
- **Chat Output**: Confirms the qualification result and logs the action taken.

### 3) Run the Flow
Use the Uplizd Playground to test your qualification logic with these prompts:
- `Qualify the latest lead from Zoho Bigin and tag as 'Hot' if they are a Director or above.`
- `Review the last 5 leads in the system and update their status based on the provided qualification rubric.`
- `Identify any leads missing company information and tag them as 'Incomplete' for manual review.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your automated sales assistant, interpreting lead data and making qualification decisions.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate lead scoring.
- Define clear "if-then" rules for lead status updates in the system instructions.
- Include specific persona instructions to ensure the agent understands your target market.

### 2) Composio Toolset Node
- Authenticate your Zoho Bigin account within the Composio dashboard.
- Ensure the agent has read/write access to the `Leads` and `Contacts` modules.

### 3) Tool Availability
- `zoho_bigin_get_lead`: Retrieve lead details for analysis.
- `zoho_bigin_update_lead`: Apply tags, change status, or update lead fields.
- `zoho_bigin_list_leads`: Fetch recent entries for bulk qualification.

---

## Related Solutions
- [Account Research Assistant (ZoomInfo)](../account-research-assistant-by-zoominfo/README.md) - Automate deep-dive research on prospects.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up cadences.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and standardize your CRM lead database.
