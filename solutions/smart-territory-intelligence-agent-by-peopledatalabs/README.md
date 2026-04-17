# Smart Territory Intelligence Agent (Uplizd) - Optimize sales coverage with PeopleDataLabs insights

## Summary
The Smart Territory Intelligence Agent is an automated workflow designed to map, analyze, and optimize sales territories by leveraging real-time company and professional data. By integrating PeopleDataLabs with your CRM, this agent provides revenue teams with a single source of truth for market penetration, ensuring pipeline velocity and data hygiene through automated territory assignment and account intelligence.

---

## Demo
![Smart Territory Intelligence Agent workflow showing data enrichment from PeopleDataLabs to CRM](image.png)
**Alt text (SEO-ready):** Smart Territory Intelligence Agent workflow using Uplizd, PeopleDataLabs, and CRM integrations for automated sales territory mapping and account data enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f718f1d7-eabf-50a8-9c75-d4a55678d074)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, peopledatalabs, territory management, sales operations, data enrichment, account intelligence, composio, ai workflow
This solution bridges the gap between raw market data and actionable sales assignments to streamline territory planning.

---

## Who is this for?
This agent is built for revenue-focused teams looking to eliminate manual territory mapping and improve lead-to-account matching.

- **Sales Operations Manager**
    - Automates the distribution of accounts based on real-time firmographic data and rep capacity.
- **Account Executive**
    - Receives enriched account insights directly in their workflow to prioritize high-value prospects.
- **Revenue Operations (RevOps) Lead**
    - Ensures consistent data hygiene across territories by syncing PeopleDataLabs intelligence with the CRM.
- **Sales Director**
    - Gains visibility into territory coverage gaps and identifies untapped market segments for growth.

---

## Features
- **Automated Territory Mapping**
    - Dynamically assigns accounts to territories based on custom logic and real-time firmographic triggers.
- **PeopleDataLabs Integration**
    - Fetches deep professional and company insights to enrich CRM records with high-accuracy data.
- **Real-time Data Sync**
    - Ensures that territory assignments and account profiles are updated instantly as market conditions change.
- **Intelligent Lead Scoring**
    - Uses enriched data to rank accounts within a territory, helping reps focus on the most promising opportunities.
- **Composio-Powered Execution**
    - Leverages the Composio Toolset to safely interact with CRM APIs and external data providers without manual coding.

---

## Use Cases
**Territory Balancing**
- Automatically reassigning accounts when a sales rep leaves or joins the team.
- Balancing account load based on company size, industry, and geographic location.

**Account Enrichment**
- Automatically appending missing firmographic data to new CRM entries using PeopleDataLabs.
- Identifying key decision-makers within a territory to streamline outbound prospecting.

**Pipeline Optimization**
- Flagging stalled accounts that lack recent engagement or updated intelligence.
- Prioritizing high-intent accounts that match the ideal customer profile (ICP) for specific territories.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your CRM and PeopleDataLabs connections via the Composio dashboard.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the territory query or account update trigger.
- **Agent**: Processes the request using the provided instructions and context.
- **Composio Toolset**: Executes the API calls to PeopleDataLabs and your CRM.
- **Chat Output**: Returns the enriched account data or territory assignment confirmation.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Map all unassigned accounts in the 'North America' territory using PeopleDataLabs data.`
- `Enrich the profile for company 'Acme Corp' and assign it to the appropriate sales rep.`
- `Identify high-growth potential accounts in the 'Fintech' sector within the 'EMEA' territory.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a strategic analyst that interprets territory rules and executes data lookups.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system prompt to prioritize accuracy in data matching and adherence to territory rules.
- Ensure the agent is instructed to handle missing data gracefully by flagging accounts for manual review.

### 2) Composio Toolset Node
- Provide your PeopleDataLabs API key and CRM credentials within the Composio connection manager.
- Define the scope to allow read/write access to account and lead objects in your CRM.

### 3) Tool Availability
- **PeopleDataLabs API**: For company firmographics and professional contact details.
- **CRM Connector**: For reading account lists and updating territory/assignment fields.
- **Data Validation Tool**: To ensure formatting consistency before syncing to the CRM.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data using Dropcontact.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep research on target accounts for sales teams.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate the creation and configuration of new accounts in Salesforce.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage and map complex account hierarchies in Dynamics 365.
