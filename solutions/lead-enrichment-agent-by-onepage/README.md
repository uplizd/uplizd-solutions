# Lead Enrichment Agent (Uplizd) - Automate lead qualification with real-time company intelligence

## Summary
The Lead Enrichment Agent is an automated Uplizd workflow designed to streamline sales operations by instantly appending high-fidelity company and contact data to inbound leads. By leveraging the Composio Toolset to query OnePage CRM and external intelligence sources, this solution eliminates manual data entry, reduces research time, and ensures your sales team has the context required to personalize outreach and increase conversion rates.

---

## Demo
![Lead Enrichment Agent workflow showing Chat Input, Agent node, Composio Toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Enrichment Agent workflow in Uplizd, automating CRM data enrichment with OnePage CRM and AI-driven lead qualification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/85741132-1cc4-5596-b10a-bcd629f16125)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, onepage, lead enrichment, sales intelligence, data hygiene, lead qualification, composio, ai workflow
- This solution bridges the gap between raw lead capture and actionable sales intelligence by automating the enrichment process directly within your CRM ecosystem.

---

## Who is this for?
This solution is built for revenue-focused teams looking to maximize pipeline velocity through automated data hygiene and intelligence.

- **Sales Development Reps (SDRs)**
    - Spend less time on manual research and more time engaging with qualified prospects.
- **Revenue Operations (RevOps) Managers**
    - Ensure CRM data consistency and high-quality lead profiles across the entire sales funnel.
- **Account Executives (AEs)**
    - Receive enriched lead data immediately, allowing for highly personalized and effective discovery calls.
- **Sales Managers**
    - Improve team productivity by automating repetitive administrative tasks associated with lead management.

---

## Features
- **Automated Data Retrieval**
    - Instantly fetch firmographic and contact details from external sources to populate empty CRM fields.
- **OnePage CRM Integration**
    - Seamlessly sync enriched data back into your OnePage CRM environment using the Composio Toolset.
- **Intelligent Lead Scoring**
    - Apply AI logic to analyze enriched data and prioritize leads based on predefined ideal customer profile (ICP) criteria.
- **Real-time Processing**
    - Trigger enrichment workflows the moment a new lead enters the system to maintain a competitive response time.
- **Customizable Enrichment Logic**
    - Tailor the agent's instructions to prioritize specific data points like company size, industry, or funding status.

---

## Use Cases
**Lead Qualification & Prioritization**
- Automatically flag leads that match high-value industry segments for immediate follow-up.
- Filter out low-intent leads by cross-referencing contact data against your target market criteria.

**Sales Outreach Personalization**
- Inject company news or recent funding announcements into lead notes to fuel personalized email campaigns.
- Map contact roles and seniority levels to ensure the right messaging reaches the right decision-maker.

**CRM Data Hygiene**
- Standardize company names and address formats during the enrichment process to prevent duplicate records.
- Fill missing contact fields automatically to ensure your CRM remains a single source of truth for the sales team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Enrichment Agent template file provided in this repository.
3. Connect your OnePage CRM account via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead information or trigger event.
- **Agent**: Processes the lead data and determines which enrichment tools to query.
- **Composio Toolset**: Executes the API calls to OnePage CRM and external intelligence providers.
- **Chat Output**: Returns the enriched lead profile and qualification status to the user or CRM.

### 3) Run the Flow
Use the Uplizd Playground to test your enrichment logic with the following prompts:
- `Enrich the lead record for [Company Name] and update the CRM with their latest employee count.`
- `Analyze the incoming lead from [Email Address] and score them based on our enterprise ICP.`
- `Find the LinkedIn profile and industry sector for the contact associated with [Lead ID].`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data gathering and CRM updates.
- **Recommended instruction pattern:**
    - "You are a sales intelligence assistant; always prioritize accuracy when mapping external data to CRM fields."
    - "If data is missing from primary sources, search secondary intelligence tools before marking the field as 'unknown'."
    - "Maintain a professional tone when summarizing lead insights for the sales team."

### 2) Composio Toolset Node
- Provide your **OnePage CRM API Key** within the toolset configuration.
- Set the connection scope to allow read/write access to lead and contact objects.

### 3) Tool Availability
- **CRM Search**: Capability to query existing records to prevent duplicates.
- **Data Enrichment API**: Capability to fetch firmographic data based on domain or company name.
- **CRM Update**: Capability to write enriched data back into specific contact or company fields.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive research and intelligence gathering for target accounts.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automated account provisioning and configuration for sales teams.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Multi-platform synchronization to maintain data consistency across your stack.
