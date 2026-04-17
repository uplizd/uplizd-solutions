# Lead Enrichment Agent (Uplizd) - Automated B2B lead data enrichment and intelligence

## Summary
The Lead Enrichment Agent is an intelligent Uplizd workflow designed to automate the gathering of firmographic and contact intelligence. By integrating with high-fidelity data providers via the Composio Toolset, this agent transforms sparse lead information into a comprehensive profile, significantly increasing pipeline velocity and ensuring sales teams have the necessary context for personalized outreach.

---

## Demo
![Lead Enrichment Agent workflow diagram showing data flow from input to CRM enrichment](image.png)
**Alt text (SEO-ready):** Lead Enrichment Agent workflow diagram showing data flow from input to CRM enrichment using Uplizd and Composio for automated sales intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9c114f93-7a7c-5f02-90a5-0e71204ca886)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead enrichment, crm, sales intelligence, data hygiene, composio, b2b sales, pipeline, sales operations
- This solution streamlines the sales qualification process by automatically appending verified business data to incoming leads.

---

## Who is this for?
This agent is built for revenue-focused teams looking to eliminate manual research and improve lead quality.

- **Sales Development Representative (SDR)**
    - Reduces time spent on manual research, allowing for faster lead qualification and personalized outreach.
- **Revenue Operations (RevOps) Manager**
    - Ensures data consistency and hygiene across the CRM by standardizing lead information automatically.
- **Account Executive (AE)**
    - Provides deep account intelligence before discovery calls, increasing the likelihood of successful deal progression.
- **Marketing Operations Specialist**
    - Improves lead scoring accuracy by ensuring that inbound leads are enriched with firmographic data immediately upon arrival.

---

## Features
- **Automated Data Retrieval**
    - Fetches real-time firmographic data including company size, industry, and revenue directly from trusted data providers.
- **CRM Synchronization**
    - Automatically updates lead and account objects in your CRM with enriched fields to maintain a single source of truth.
- **Intelligent Contextualization**
    - Uses the Agent node to synthesize raw data into actionable insights, highlighting key triggers for sales engagement.
- **Composio Toolset Integration**
    - Leverages secure, pre-built connectors to interact with CRM platforms and third-party data APIs without custom code.
- **Real-time Processing**
    - Triggers enrichment workflows the moment a new lead is captured, ensuring sales teams act on the freshest intelligence.

---

## Use Cases
**Lead Qualification**
- Automatically verify company size and industry to prioritize high-value inbound leads.
- Flag leads that do not meet ideal customer profile (ICP) criteria for immediate routing to nurture tracks.

**Sales Outreach Preparation**
- Compile recent company news and funding information to create hyper-personalized opening emails.
- Identify key decision-makers within an account to assist in multi-threading sales opportunities.

**CRM Data Hygiene**
- Fill in missing fields like job titles or company websites to prevent data decay in your CRM.
- Standardize formatting for contact data to ensure clean reporting and accurate lead attribution.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Enrichment Agent template from the marketplace.
3. Connect your preferred CRM and data provider accounts via the Composio settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead email or company domain to initiate the enrichment process.
- **Agent**: Analyzes the input and determines which data points are missing or require verification.
- **Composio Toolset**: Executes API calls to fetch external data and write updates back to the CRM.
- **Chat Output**: Returns a summary of the enriched data and confirmation of the CRM update.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Enrich the lead details for the domain: acme-corp.com`
- `Find the latest funding news for the company associated with this email: contact@techstartup.io`
- `Update the CRM record for the lead at domain: cloud-services.com with current employee count`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence, parsing lead data and deciding which tools to invoke.
- Set the system prompt to prioritize accuracy and data completeness.
- Enable "Tool Use" mode to allow the agent to select the correct enrichment tool based on the input.
- Configure the temperature to 0.2 for consistent, factual data extraction.

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure authentication with your CRM and data providers.
- Define the scope of access to ensure the agent can only modify relevant lead and account fields.

### 3) Tool Availability
- **CRM Connector**: Read/Write access to Lead and Account objects.
- **Data Enrichment API**: Access to firmographic and contact intelligence endpoints.
- **Search Utility**: Capability to perform web lookups for company-specific news.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research for target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms.
- [Account Mapping Agent](../account-mapping-agent-by-bigpicture-io/README.md) - Map organizational structures for complex B2B deals.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate automated reports on account activity and intent.
