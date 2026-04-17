# Event Attendee Enricher (Uplizd) - Automate lead qualification and profile enrichment for event registrations

## Summary
The Event Attendee Enricher is an automated Uplizd workflow designed to transform raw event registration data into high-value prospect profiles. By leveraging the Dropcontact integration, the agent automatically validates contact information, appends professional details, and updates your CRM in real-time. This ensures your sales team receives enriched, actionable lead data immediately after sign-up, significantly reducing manual data entry and increasing pipeline velocity.

---

## Demo
![Event Attendee Enricher workflow showing data flow from registration input to Dropcontact enrichment and CRM update](image.png)
**Alt text (SEO-ready):** Uplizd Event Attendee Enricher workflow, automated lead qualification, Dropcontact data enrichment, CRM synchronization, and sales pipeline automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6cb1177e-9104-55fe-b112-c6299d41b48a)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, dropcontact, lead enrichment, data hygiene, sales operations, event marketing, lead qualification, composio
- This solution bridges the gap between event registration platforms and CRM systems, ensuring every attendee is fully researched and ready for outreach.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maximize the ROI of their event marketing efforts.

- **Sales Development Rep (SDR)**
    - Receives enriched lead data instantly, allowing for faster, more personalized outreach to event attendees.
- **Marketing Operations Manager**
    - Ensures that registration data is clean, standardized, and automatically synced to the CRM without manual intervention.
- **Event Coordinator**
    - Gains visibility into the quality of event registrants, helping to tailor follow-up strategies based on attendee seniority and company size.
- **RevOps Lead**
    - Maintains a single source of truth for lead data, preventing data decay and ensuring high-quality pipeline hygiene.

---

## Features
- **Automated Data Enrichment**
    - Uses the Dropcontact API to automatically find missing professional details like job titles, company websites, and verified email addresses.
- **Real-Time CRM Sync**
    - Seamlessly pushes enriched profiles into your CRM, ensuring your sales team has the most current information available.
- **Intelligent Lead Qualification**
    - Evaluates attendee data against your ideal customer profile (ICP) to prioritize high-value leads for immediate follow-up.
- **Standardized Data Hygiene**
    - Automatically formats and cleans incoming registration strings to ensure consistent naming conventions across your database.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to manage secure, authenticated connections between your event platforms and CRM vendors.

---

## Use Cases
**Post-Event Lead Prioritization**
- Automatically flag attendees from target accounts for immediate outreach by the sales team.
- Score leads based on enriched company size and industry data provided by the enrichment agent.

**Data Hygiene & Maintenance**
- Correct formatting errors in registration forms, such as inconsistent casing or missing company domains.
- Deduplicate attendee records by matching incoming leads against existing CRM contacts using verified email addresses.

**Sales Pipeline Acceleration**
- Trigger automated follow-up sequences in your CRM as soon as an attendee profile is enriched and qualified.
- Update lead status fields based on the enrichment results to keep the sales funnel moving efficiently.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace and project to import the workflow.
3. Authenticate your CRM and Dropcontact credentials within the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw attendee registration data (e.g., name, email, company).
- **Agent**: Processes the data, triggers the enrichment logic, and determines the next best action.
- **Composio Toolset**: Executes the API calls to Dropcontact and your CRM to fetch and write data.
- **Chat Output**: Confirms the enrichment status and provides a summary of the updated lead profile.

### 3) Run the Flow
Use the Playground to test the enrichment process with sample data:
- `Enrich attendee: John Doe, john.doe@example.com, Acme Corp`
- `Find company details for registration: Jane Smith, jane@techcorp.io`
- `Process and sync new event registration for: Michael Scott, m.scott@dundermifflin.com`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data transformation and tool selection.
- **Recommended instruction pattern:**
    - "You are an expert sales operations assistant tasked with enriching event attendee data."
    - "Always prioritize accuracy when mapping data from Dropcontact to the CRM fields."
    - "If enrichment fails, flag the lead for manual review rather than creating an incomplete record."

### 2) Composio Toolset Node
- **API Key**: Ensure your Dropcontact and CRM API keys are securely stored in your environment variables.
- **Connection Scope**: Grant the toolset read/write access to your CRM's lead/contact objects and the Dropcontact enrichment endpoint.

### 3) Tool Availability
- **Dropcontact API**: For email verification and professional profile lookup.
- **CRM Connector**: For searching, updating, and creating lead records.
- **Data Transformer**: For standardizing input strings and formatting contact fields.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Deep-dive research for target accounts using Dropcontact.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and deduplication for CRM databases.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automated account profiling and research workflows.
