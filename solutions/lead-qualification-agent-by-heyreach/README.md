# Lead Qualification Agent (Uplizd) - Automate lead scoring and outreach triage

## Summary
The Lead Qualification Agent streamlines your sales pipeline by automatically analyzing incoming leads from HeyReach campaigns, scoring them against your ideal customer profile, and routing high-intent prospects for immediate follow-up. By leveraging AI-driven assessment, this workflow eliminates manual data entry and ensures your sales team focuses their energy on the most promising opportunities, significantly increasing conversion velocity.

---

## Demo
![Lead Qualification Agent workflow showing HeyReach integration and automated scoring nodes](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent Uplizd workflow for HeyReach, automated sales lead scoring, and CRM pipeline integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/74eed13e-f908-5f09-9511-0f1732f9cfbe)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead qualification, heyreach, sales pipeline, crm, lead scoring, outreach, ai workflow, composio
- This solution bridges the gap between raw outreach data and actionable sales intelligence by automating the qualification lifecycle.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to scale their outreach efforts without sacrificing lead quality.

- **Sales Development Representative (SDR)**
    - Reduces time spent manually researching and qualifying incoming leads from outreach platforms.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent lead scoring criteria are applied across all inbound and outbound channels.
- **Growth Marketer**
    - Provides immediate feedback on campaign performance by identifying which lead segments convert fastest.
- **Sales Manager**
    - Increases pipeline velocity by ensuring the sales team only engages with prospects that meet predefined readiness thresholds.

---

## Features
- **Automated Lead Scoring**
    - Dynamically evaluates leads based on custom criteria such as company size, industry, and engagement signals.
- **HeyReach Integration**
    - Seamlessly pulls prospect data directly from HeyReach campaigns for real-time processing.
- **Intelligent Routing**
    - Automatically tags and routes qualified leads to the appropriate CRM pipeline or sales representative.
- **Customizable Qualification Criteria**
    - Easily adjust the Agent’s logic to match your evolving ideal customer profile (ICP) and market focus.
- **Real-time Data Sync**
    - Uses the Composio Toolset to push qualified lead status updates back to your CRM instantly.

---

## Use Cases
**Outreach Campaign Management**
- Automatically filter out low-intent leads from HeyReach before they reach your CRM.
- Update lead status in real-time based on prospect responsiveness and interaction history.

**Sales Pipeline Optimization**
- Prioritize daily outreach tasks by surfacing high-score leads to the top of the queue.
- Trigger automated follow-up sequences for leads that meet specific qualification benchmarks.

**Data Hygiene and Enrichment**
- Standardize lead information formatting during the qualification process to ensure clean CRM data.
- Append missing firmographic details to leads during the assessment phase to improve targeting accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the Lead Qualification Agent workflow.
3. Authenticate your HeyReach and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and data fields.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead data payload from your HeyReach campaigns.
- **Agent**: Analyzes the lead data against your ICP and assigns a qualification score.
- **Composio Toolset**: Executes the necessary API calls to update your CRM or outreach platform.
- **Chat Output**: Returns a summary of the qualification result and the action taken.

### 3) Run the Flow
Use the Playground to test your agent with sample lead data:
- `Qualify this lead: { "name": "Jane Doe", "company": "TechCorp", "title": "CTO", "intent": "high" }`
- `Assess the following prospect from HeyReach and update their status in Salesforce: { "email": "prospect@example.com", "engagement_score": 85 }`
- `Check if this lead meets our enterprise criteria and route to the account executive team: { "revenue": "50M+", "industry": "SaaS" }`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting lead signals and applying business logic.
- **Role:** Expert Sales Operations Analyst.
- **Instruction Pattern:** 
    - Evaluate lead data against the provided ICP parameters.
    - Assign a score from 1-100 based on the prospect's profile and intent.
    - Determine the next best action (e.g., "Route to Sales", "Nurture", or "Discard").

### 2) Composio Toolset Node
- **API Key:** Provide your unique Composio API key to enable secure connectivity.
- **Connection Scope:** Ensure the toolset has read/write permissions for your specific CRM and HeyReach instances.

### 3) Tool Availability
- **CRM Connectors:** Capability to update lead objects, change status fields, and add internal notes.
- **Outreach API:** Capability to fetch campaign metrics and prospect interaction history.
- **Data Validation:** Capability to format and clean incoming lead strings before processing.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-ups for high-value opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate data cleanup and formatting for your CRM database.
