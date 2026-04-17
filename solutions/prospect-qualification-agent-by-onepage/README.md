# Prospect Qualification Agent (Uplizd) - Automate lead scoring and qualification workflows

## Summary
The Prospect Qualification Agent by OnePage streamlines your sales pipeline by automatically scoring and qualifying incoming leads using real-time enriched company data. By integrating directly with your CRM, this Uplizd AI workflow eliminates manual data entry, reduces qualification latency, and ensures your sales team focuses only on high-intent prospects, ultimately increasing pipeline velocity and conversion rates.

---

## Demo
![Prospect Qualification Agent workflow interface showing lead scoring and CRM data enrichment nodes](image.png)
**Alt text (SEO-ready):** Prospect Qualification Agent (Uplizd) workflow for automated CRM lead scoring, data enrichment, and sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d143df86-ade0-5702-b06c-6bc9597df8b1)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, onepage, lead scoring, sales pipeline, data enrichment, ai workflow, composio, qualification
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the qualification process.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to standardize their lead evaluation process and improve sales efficiency.

- **Sales Development Representative (SDR)**
    - Immediately identifies high-priority leads to reach out to first, reducing time spent on unqualified prospects.
- **Revenue Operations (RevOps) Manager**
    - Standardizes the qualification criteria across the entire organization, ensuring consistent data hygiene in the CRM.
- **Account Executive (AE)**
    - Receives pre-qualified opportunities with enriched context, allowing for more personalized and effective discovery calls.
- **Sales Manager**
    - Gains visibility into lead quality trends and pipeline health, enabling data-driven coaching and resource allocation.

---

## Features
- **Automated Lead Scoring**
    - Calculates lead readiness scores based on enriched firmographic data and predefined business rules.
- **Real-time Data Enrichment**
    - Automatically fetches and updates prospect company details via the Composio Toolset to ensure accuracy.
- **Seamless CRM Integration**
    - Syncs qualification status and score updates directly back to your CRM, maintaining a single source of truth.
- **Customizable Qualification Logic**
    - Easily adjust thresholds and scoring weights within the Agent node to match your specific Ideal Customer Profile (ICP).
- **Instant Notification Triggers**
    - Alerts the assigned sales owner via the Chat Output node when a lead meets high-intent qualification criteria.

---

## Use Cases
**Lead Prioritization**
- Automatically flag "Hot" leads for immediate follow-up based on company size and recent funding news.
- Filter out low-intent leads to prevent SDRs from wasting time on non-ICP prospects.

**Pipeline Hygiene**
- Update lead status fields in the CRM automatically based on the agent's qualification assessment.
- Ensure all lead records are enriched with up-to-date website and industry data before reaching the sales team.

**Sales Velocity Optimization**
- Reduce the time between lead submission and first contact by automating the initial research phase.
- Provide AEs with a summary of prospect research directly in the CRM notes for faster deal progression.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project to import the workflow.
3. Connect your CRM and OnePage API credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead information or trigger event from your CRM.
- **Agent**: Analyzes the lead data against your ICP criteria and determines the qualification score.
- **Composio Toolset**: Executes the enrichment calls to OnePage and updates the CRM records.
- **Chat Output**: Delivers the final qualification summary and score to your dashboard or notification channel.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Qualify the lead from Acme Corp and update their status in the CRM.`
- `Score the latest batch of inbound leads based on the current ICP settings.`
- `Fetch company details for the new lead in the queue and provide a qualification summary.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for evaluating lead fit and intent.
- **Role**: Act as an expert Sales Operations Assistant.
- **Instruction Pattern**:
    - Analyze the provided lead data against the established Ideal Customer Profile (ICP).
    - Use the Composio Toolset to fetch missing firmographic data if the lead is incomplete.
    - Output a clear qualification score and a brief justification for the sales team.

### 2) Composio Toolset Node
- **API Key**: Ensure your OnePage and CRM API keys are active in the Composio dashboard.
- **Connection Scope**: Grant read/write access to lead objects and company profile endpoints.

### 3) Tool Availability
- **CRM Connector**: For reading lead details and updating status fields.
- **OnePage Enrichment**: For fetching company size, industry, and contact intelligence.
- **Notification Service**: For sending alerts to sales channels (e.g., Slack or Email).

---

## Related Solutions
- [Account Research Agent (OnePage)](../account-research-agent-by-onepage/README.md) - Automates deep-dive research into target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes lead and contact data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker-by-salesforce/README.md) - Monitors and scores sales opportunities for better pipeline management.
