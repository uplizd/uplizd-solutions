# Lead Intelligence Agent (Uplizd) - Automate lead enrichment and qualification with ZoomInfo data

## Summary
The Lead Intelligence Agent by ZoomInfo is an automated workflow designed to streamline the sales prospecting process by instantly enriching raw lead data with deep firmographic and contact insights. By leveraging real-time data from ZoomInfo via the Composio Toolset, this solution enables sales teams to eliminate manual research, improve lead scoring accuracy, and accelerate pipeline velocity through a single, automated source of truth.

---

## Demo
![Lead Intelligence Agent workflow diagram showing Chat Input, Agent, ZoomInfo Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Lead Intelligence Agent workflow for automated lead enrichment, ZoomInfo data integration, sales prospecting, and CRM qualification using Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5bc7ca2d-40b2-52d2-aa50-33b7e62e1b6f)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead enrichment, zoominfo, sales prospecting, crm, data intelligence, pipeline velocity, composio, ai workflow
- This solution bridges the gap between raw lead capture and actionable sales intelligence by automating the enrichment process directly within your CRM workflow.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maximize the efficiency of their outbound and inbound sales motions.

- **Sales Development Representatives (SDRs)**
    - Instantly qualify incoming leads without leaving their primary communication interface.
- **Account Executives (AEs)**
    - Access deep account intelligence to personalize outreach and increase conversion rates.
- **RevOps Managers**
    - Ensure data hygiene and consistency by automating the enrichment of lead records at the point of entry.
- **Sales Managers**
    - Improve team productivity by reducing the time spent on manual research and data entry tasks.

---

## Features
- **Real-time Lead Enrichment**
  Automatically pull comprehensive company and contact profiles from ZoomInfo the moment a lead is identified.
- **Intelligent Qualification**
  Apply custom business logic to score leads based on firmographic data, ensuring only high-intent prospects reach the sales team.
- **Composio-Powered Integration**
  Seamlessly connect your agent to ZoomInfo and your CRM using the Composio Toolset for secure, authenticated data exchange.
- **Automated Data Sync**
  Push enriched insights directly into your CRM fields, maintaining a clean and updated database without manual intervention.
- **Context-Aware Agent Logic**
  Utilize advanced LLM reasoning to summarize complex company data into actionable insights for sales representatives.

---

## Use Cases
**Outbound Prospecting**
- Automatically enrich cold lead lists with verified contact information and company size data.
- Identify key decision-makers within target accounts to tailor personalized outreach sequences.

**Inbound Lead Triage**
- Instantly score incoming web leads based on industry, revenue, and technology stack markers.
- Route high-value leads to senior account executives while auto-tagging lower-tier leads for automated nurturing.

**CRM Data Hygiene**
- Periodically refresh existing account records to ensure contact details remain accurate and up-to-date.
- Detect and flag duplicate or incomplete lead records for manual review by the operations team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the provided Lead Intelligence Agent template configuration.
3. Connect your ZoomInfo API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead information or company domain.
- **Agent**: Processes the data and determines which ZoomInfo queries to execute.
- **Composio Toolset**: Executes the API calls to fetch and parse external lead data.
- **Chat Output**: Returns the enriched lead profile and qualification status to the user.

### 3) Run the Flow
Open the Playground and test the agent with the following prompts:
- `Enrich the lead record for company: acme-corp.com`
- `Find contact details for the VP of Sales at Salesforce`
- `Qualify this lead based on company revenue and industry: tech-solutions.io`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence hub, interpreting user requests and mapping them to specific tool functions.
- Use a high-reasoning model (e.g., GPT-4o) for accurate data interpretation.
- Set the system prompt to prioritize data accuracy and concise formatting.
- Configure the agent to handle missing data gracefully by requesting clarification from the user.

### 2) Composio Toolset Node
- Provide your ZoomInfo API key within the secure credentials manager.
- Define the connection scope to allow read-access to contact and company search endpoints.

### 3) Tool Availability
- **Company Search**: Retrieve firmographic data including revenue, headcount, and industry.
- **Contact Search**: Locate verified emails and phone numbers for specific roles.
- **Data Parsing**: Extract and format raw JSON responses into human-readable summaries.

---

## Related Solutions
- [Account Research Assistant by ZoomInfo](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research for target account planning.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
- [Account Intelligence Gatherer by Dropcontact](../account-intelligence-gatherer-by-dropcontact/README.md) - Alternative enrichment focused on email verification and contact data.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score sales opportunities throughout the pipeline.
