# Lead Qualification Agent (Uplizd) - Automate lead scoring and pipeline prioritization

## Summary
The Lead Qualification Agent by Close is an intelligent workflow designed to streamline sales operations by automatically evaluating, scoring, and routing incoming leads. By leveraging real-time data from your CRM, this solution ensures that high-intent prospects are prioritized, reducing manual data entry and accelerating pipeline velocity for sales teams.

---

## Demo
![Lead Qualification Agent workflow showing Chat Input, Agent node, Close CRM toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent by Close for Uplizd, automating CRM lead scoring, sales pipeline management, and prospect data enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/587aba72-c1d0-58f5-8816-60f6c1548dd2)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, close, lead qualification, lead scoring, sales pipeline, data enrichment, composio, ai workflow
- This solution integrates directly with Close to transform raw lead data into actionable sales intelligence.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual qualification bottlenecks and focus on high-value opportunities.

- **Sales Development Reps (SDRs)**
    - Instantly identify which inbound leads require immediate outreach versus those needing further nurturing.
- **Revenue Operations Managers**
    - Standardize lead scoring criteria across the organization to ensure consistent pipeline hygiene.
- **Account Executives**
    - Spend less time researching lead fit and more time conducting discovery calls with qualified prospects.
- **Sales Managers**
    - Gain real-time visibility into lead quality trends and team performance metrics.

---

## Features
- **Automated Lead Scoring**
    - Dynamically assigns scores to leads based on custom criteria and historical conversion data.
- **Real-time CRM Integration**
    - Seamlessly syncs qualification status and notes back to Close via the Composio Toolset.
- **Intelligent Data Enrichment**
    - Automatically pulls firmographic and intent data to provide a comprehensive view of the prospect.
- **Customizable Qualification Logic**
    - Easily adjust the Agent’s instruction set to match your specific Ideal Customer Profile (ICP).
- **Pipeline Routing**
    - Automatically updates lead stages or triggers follow-up tasks based on the qualification outcome.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads as "Hot" when they match specific budget and authority criteria.
- Move qualified leads to a dedicated "Discovery" stage in Close to alert the sales team.

**Data Hygiene & Enrichment**
- Populate missing lead fields by cross-referencing incoming data with external intelligence sources.
- Standardize lead formatting to ensure clean reporting and accurate attribution in your CRM.

**Sales Outreach Optimization**
- Trigger automated follow-up tasks for leads that meet the qualification threshold.
- Filter out low-intent leads and move them to a long-term nurture sequence to keep the pipeline clean.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Authenticate your Close CRM account within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger events from your web forms or CRM.
- **Agent**: Processes the lead information against your defined qualification criteria.
- **Composio Toolset**: Executes API calls to Close to update lead status, scores, and activity logs.
- **Chat Output**: Returns the qualification summary and confirmation of CRM updates.

### 3) Run the Flow
Use the Playground to test the agent with sample lead data:
- `Qualify this lead: Name: John Doe, Company: TechCorp, Role: CTO, Budget: $50k.`
- `Score this lead based on the provided company size and industry fit.`
- `Update the lead status to 'Qualified' and add a note about the meeting request.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your digital sales assistant, interpreting lead data and applying business rules.
- Maintain a professional, objective tone when evaluating lead fit.
- Strictly follow the qualification rubric provided in the system instructions.
- Ensure all CRM updates are formatted correctly for the Close API.

### 2) Composio Toolset Node
- Provide your Close API key within the Composio configuration.
- Set the connection scope to allow the agent to read lead details and write updates to the CRM.

### 3) Tool Availability
- **Lead Search**: Locate existing records to prevent duplicates.
- **Update Lead**: Modify status, custom fields, and lead scores.
- **Create Activity**: Log notes and qualification summaries directly to the lead timeline.

---

## Related Solutions
- [../account-research-agent-by-onepage/README.md](../account-research-agent-by-onepage/README.md) — Research and gather intelligence on target accounts.
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) — Automate the creation and configuration of new accounts in Salesforce.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) — Synchronize data across multiple CRM platforms to ensure a single source of truth.
