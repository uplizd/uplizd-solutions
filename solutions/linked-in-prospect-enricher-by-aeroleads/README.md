# LinkedIn Prospect Enricher (Uplizd) - Automated lead enrichment with verified contact data

## Summary
The LinkedIn Prospect Enricher is an intelligent Uplizd workflow that automates the transition from LinkedIn profile discovery to actionable lead intelligence. By integrating LinkedIn data with the AeroLeads API via the Composio Toolset, this solution eliminates manual data entry, ensures high-accuracy contact verification, and accelerates pipeline velocity for sales teams by providing a single source of truth for prospect outreach.

---

## Demo
![LinkedIn Prospect Enricher workflow showing LinkedIn input, AeroLeads enrichment, and CRM output nodes](image.png)
**Alt text (SEO-ready):** LinkedIn Prospect Enricher workflow by Uplizd, featuring AeroLeads integration for automated lead data enrichment and CRM synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0695337e-8088-59b5-95f0-5fda53d6adb0)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** linkedin, aeroleads, lead enrichment, sales prospecting, data hygiene, crm, lead qualification, composio
- This solution streamlines the sales prospecting lifecycle by bridging the gap between social discovery and verified contact database management.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to scale their outbound efforts without sacrificing data quality.

- **Sales Development Representative (SDR)**
    - Reduces time spent manually searching for prospect emails and phone numbers.
- **Account Executive (AE)**
    - Ensures high-quality, verified contact data is ready for personalized outreach.
- **RevOps Manager**
    - Maintains CRM data hygiene by automating the ingestion of validated lead information.
- **Growth Marketer**
    - Increases conversion rates by targeting prospects with accurate, enriched contact profiles.

---

## Features
- **Automated Prospect Enrichment**
    - Instantly retrieves verified business emails and phone numbers from LinkedIn profiles using the AeroLeads API.
- **Real-time Data Validation**
    - Filters out invalid or low-confidence contact data before it reaches your CRM, ensuring high deliverability.
- **Seamless CRM Integration**
    - Automatically maps enriched data fields directly into your existing sales pipeline or lead management system.
- **Composio-Powered Connectivity**
    - Leverages the Composio Toolset to securely manage API authentication and tool execution between LinkedIn and AeroLeads.
- **Customizable Lead Scoring**
    - Triggers automated workflows based on the richness of the retrieved data, prioritizing high-intent prospects.

---

## Use Cases
**Outbound Sales Prospecting**
- Automatically enrich a list of LinkedIn prospects to prepare for multi-channel outreach campaigns.
- Sync verified contact data into your CRM immediately after identifying a target account.

**Lead Qualification & Hygiene**
- Clean up existing lead lists by cross-referencing LinkedIn profiles with AeroLeads to fill missing contact gaps.
- Flag prospects with incomplete data for manual review while auto-processing high-confidence matches.

**Account-Based Marketing (ABM)**
- Identify key decision-makers on LinkedIn and enrich their profiles to facilitate personalized ABM messaging.
- Maintain up-to-date contact information for target accounts to ensure marketing assets reach the right stakeholders.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the LinkedIn Prospect Enricher template from the solution library.
3. Connect your LinkedIn and AeroLeads accounts via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the LinkedIn profile URL or prospect name from the user.
- **Agent**: Analyzes the input and triggers the appropriate enrichment tool.
- **Composio Toolset**: Executes the AeroLeads lookup to fetch verified contact details.
- **Chat Output**: Displays the enriched contact profile and confirms successful CRM synchronization.

### 3) Run the Flow
Use the Playground to test your enrichment pipeline:
- `Enrich this LinkedIn profile: [LinkedIn URL]`
- `Find contact details for [Prospect Name] at [Company Name]`
- `Search for verified email and phone for this lead: [LinkedIn URL]`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between the user request and the enrichment tools.
- Focus on extracting profile identifiers from natural language inputs.
- Maintain a structured output format for CRM compatibility.
- Handle API errors gracefully by prompting the user for additional profile details.

### 2) Composio Toolset Node
- Requires a valid AeroLeads API key configured within the Composio dashboard.
- Ensure the connection scope includes `lead_enrichment` and `profile_search` permissions.

### 3) Tool Availability
- `aeroleads_search_profile`: Retrieves contact data based on LinkedIn URL.
- `aeroleads_verify_email`: Validates email deliverability for enriched leads.
- `crm_update_lead`: Pushes verified data to your connected CRM platform.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive intelligence for target accounts.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Automated contact enrichment and data cleaning.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Scoring and monitoring of new sales opportunities.
