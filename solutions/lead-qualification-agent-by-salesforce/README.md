# Lead Qualification Agent (Uplizd) - Automate lead scoring and routing for Salesforce

## Summary
The Lead Qualification Agent is an intelligent Uplizd workflow designed to streamline the sales funnel by automatically evaluating incoming leads against your specific business criteria. By leveraging the Composio Toolset to interface with Salesforce, this agent ensures that only high-intent prospects reach your sales team, significantly increasing pipeline velocity and reducing manual data entry for BDRs and Account Executives.

---

## Demo
![Lead Qualification Agent workflow diagram showing Chat Input, Agent, Composio Salesforce Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Uplizd Lead Qualification Agent workflow for Salesforce lead scoring, automated routing, and CRM data synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cd0281c0-d90a-5652-a383-58cb704069d6)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, salesforce, lead qualification, lead scoring, pipeline, sales operations, composio, ai workflow
- This solution bridges the gap between raw lead ingestion and CRM hygiene by automating the qualification process using AI-driven logic.

---

## Who is this for?
This agent is built for sales and revenue teams looking to eliminate manual lead triage and focus on high-value opportunities.

- **Sales Development Representative (SDR)**
    - Spend less time on manual qualification and more time engaging with high-intent prospects.
- **Revenue Operations Manager**
    - Standardize lead scoring criteria across the organization to ensure consistent data quality in Salesforce.
- **Sales Manager**
    - Improve team performance by ensuring that only qualified leads are routed to the appropriate account owners.
- **Growth Marketer**
    - Gain immediate feedback on lead quality to optimize top-of-funnel acquisition strategies.

---

## Features
- **Automated Lead Scoring**
    - Dynamically assign scores to leads based on firmographic data and engagement signals retrieved from Salesforce.
- **Intelligent Routing Logic**
    - Automatically update lead status and assign owners in Salesforce based on qualification outcomes.
- **Real-time CRM Integration**
    - Utilize the Composio Toolset to perform real-time read/write operations on Salesforce objects without leaving the workflow.
- **Custom Qualification Criteria**
    - Easily configure the Agent node instructions to match your unique ICP (Ideal Customer Profile) and disqualification rules.
- **Actionable Output Summaries**
    - Receive clear, concise summaries of qualification decisions directly in the Chat Output for immediate review.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads that match your ICP for immediate outreach by the sales team.
- Move low-intent leads to a "nurture" status in Salesforce to keep the active pipeline clean.

**Salesforce Data Hygiene**
- Standardize lead field formatting during the qualification process to ensure consistent CRM reporting.
- Automatically enrich lead records with missing information identified during the AI analysis phase.

**Pipeline Velocity Optimization**
- Reduce the time-to-first-contact by automating the transition from "New" to "Qualified" status.
- Trigger automated follow-up tasks in Salesforce for leads that meet specific engagement thresholds.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your Salesforce account via the Composio integration settings.
3. Configure your specific qualification criteria within the Agent node instructions.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger events from your lead capture forms.
- **Agent**: Processes lead data against your ICP rules and determines qualification status.
- **Composio Toolset**: Executes API calls to update lead fields, statuses, and owners in Salesforce.
- **Chat Output**: Displays the qualification result and any actions taken within the CRM.

### 3) Run the Flow
Use the Playground to test your qualification logic with these example prompts:
- `Qualify the new lead from Acme Corp based on the provided company size and industry.`
- `Check the latest lead in Salesforce and update the status to 'Qualified' if they have a corporate email.`
- `Review the lead record for John Doe and assign him to the Enterprise sales queue if the budget exceeds $50k.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your qualification logic.
- Define your ICP clearly, including specific industries, company sizes, and job titles.
- Instruct the agent to prioritize leads that meet at least 3 of your 5 core qualification criteria.
- Set a fallback instruction for leads that do not meet criteria, such as tagging them as "Nurture" in Salesforce.

### 2) Composio Toolset Node
- Provide your Salesforce API credentials within the Composio dashboard.
- Ensure the connection scope includes `read` and `write` permissions for Lead and Opportunity objects.

### 3) Tool Availability
- **Salesforce Search**: Locate existing lead records by email or company name.
- **Salesforce Update**: Modify lead status, owner, and custom scoring fields.
- **Salesforce Create**: Generate new tasks or follow-up activities for qualified leads.

---

## Related Solutions
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate data cleanup and formatting for your CRM records.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage deal stages and follow-up cadences for active opportunities.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Enrich account data to support better lead qualification.
