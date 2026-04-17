# Lead Qualification Assistant (Uplizd) - Automated lead scoring and routing for sales teams

## Summary
The Lead Qualification Assistant is an intelligent Uplizd workflow that automates the evaluation of incoming leads, ensuring your sales team focuses on high-intent prospects. By integrating directly with your CRM, this agent scores leads based on predefined criteria, filters out unqualified entries, and routes qualified opportunities to the appropriate account executive, significantly reducing manual data entry and increasing pipeline velocity.

---

## Demo
![Lead Qualification Assistant workflow diagram showing CRM integration and automated routing](image.png)
**Alt text (SEO-ready):** Lead Qualification Assistant Uplizd workflow, automated CRM lead scoring, sales pipeline routing, and Composio integration for sales operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6m3V2kQAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZkAAACjSURBVHjzY/z//z8DJgBxgJqB...)] (https://uplizd.ai/solutions/54b0c31f-47e1-59a5-befe-db4a9e1d65ce)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, lead scoring, salesforce, hubspot, pipeline, lead qualification, composio, ai workflow  
This solution streamlines the RevOps lifecycle by automating the transition from raw lead capture to actionable sales opportunity.

---

## Who is this for?
This assistant is designed for revenue-focused teams looking to eliminate manual lead triage and improve response times.

- **Sales Development Representative (SDR)**
    - Automates the initial screening process so you can focus on high-value conversations rather than data entry.
- **Revenue Operations Manager**
    - Ensures consistent lead scoring logic across the entire organization, improving data hygiene and pipeline accuracy.
- **Account Executive**
    - Receives only pre-qualified, high-intent leads directly in the CRM, increasing your win rate and focus.
- **Marketing Operations Lead**
    - Bridges the gap between lead generation campaigns and sales execution by ensuring lead quality meets defined thresholds.

---

## Features
- **Automated Lead Scoring**
    - Dynamically evaluates incoming leads against custom business rules to assign priority levels instantly.
- **Real-time CRM Routing**
    - Automatically updates lead status and assigns owners in Salesforce or HubSpot based on qualification outcomes.
- **Intelligent Data Enrichment**
    - Uses the Composio Toolset to pull additional firmographic data, ensuring the agent has full context before routing.
- **Conflict Resolution**
    - Detects duplicate entries and merges lead information to maintain a single source of truth in your CRM.
- **Customizable Thresholds**
    - Easily adjust qualification criteria within the Agent node to match changing market conditions or product focus.

---

## Use Cases
**Lead Prioritization**
- Automatically flag "Hot" leads for immediate outreach when they match ICP criteria.
- Deprioritize or archive leads that fail to meet minimum budget or company size requirements.

**Pipeline Management**
- Sync qualified leads directly into the CRM pipeline with pre-populated notes and priority tags.
- Trigger automated follow-up tasks for sales reps when a lead is moved to a "Qualified" stage.

**Data Hygiene**
- Standardize lead contact information formats (e.g., phone numbers, job titles) before they enter the CRM.
- Identify and flag incomplete lead profiles for marketing re-engagement campaigns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Assistant template from the solutions library.
3. Connect your preferred CRM (e.g., Salesforce, HubSpot) via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data from webhooks or manual uploads.
- **Agent**: Processes lead data, applies scoring logic, and determines qualification status.
- **Composio Toolset**: Executes CRM API calls to update lead records and fetch enrichment data.
- **Chat Output**: Returns a summary of the qualification result and the routing action taken.

### 3) Run the Flow
Use the Playground to test the agent with sample data:
- `Qualify this lead: Name: John Doe, Company: TechCorp, Budget: $50k, Industry: SaaS`
- `Check for duplicates and update the status for lead ID 98765 in Salesforce`
- `Score this lead based on the provided company size and industry criteria`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized sales analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- **Recommended instruction pattern:**
    - "You are a lead qualification expert. Evaluate the input against the defined ICP criteria."
    - "Always check for existing records in the CRM before creating new entries."
    - "If a lead is qualified, output the specific routing destination and the reasoning for the score."

### 2) Composio Toolset Node
- Provide your API key to enable secure CRM authentication.
- Set the connection scope to include read/write access for Leads, Contacts, and Opportunities.

### 3) Tool Availability
- **CRM Search**: Locate existing leads or accounts.
- **Lead Update**: Modify lead fields, status, and owner assignments.
- **Data Enrichment**: Query external tools for company firmographics.
- **Task Creation**: Generate follow-up reminders for sales representatives.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich lead profiles with deep firmographic data.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track opportunities through the sales funnel.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep lead data synchronized across multiple platforms.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automate deep-dive research on target accounts.
