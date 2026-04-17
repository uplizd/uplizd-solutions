# Lead Data Enrichment Agent (Uplizd) - Automate prospect profile completion using PeopleDataLabs

## Summary
The Lead Data Enrichment Agent by Uplizd automates the process of transforming sparse lead information into comprehensive prospect profiles. By integrating real-time data lookups via the PeopleDataLabs API, this workflow empowers sales and marketing teams to eliminate manual research, improve lead scoring accuracy, and accelerate pipeline velocity through a single source of truth for prospect intelligence.

---

## Demo
![Lead Data Enrichment Agent workflow showing input, PeopleDataLabs enrichment, and output](image.png)
**Alt text (SEO-ready):** Uplizd Lead Data Enrichment Agent workflow for automated CRM prospect profile completion using PeopleDataLabs integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b9b8228c-f05c-5733-8a17-bc10b5edeb6b)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, peopledatalabs, lead enrichment, sales intelligence, data hygiene, prospect research, composio, ai workflow  
This solution bridges the gap between raw lead capture and actionable sales intelligence by automating data enrichment at scale.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their lead qualification process and improve outreach personalization.

*   **Sales Development Representative (SDR)**
    *   Reduces time spent on manual prospect research, allowing for higher volume outreach.
*   **Marketing Operations Manager**
    *   Ensures CRM data hygiene by automatically filling missing fields for incoming leads.
*   **Account Executive (AE)**
    *   Provides deeper context on incoming opportunities to tailor discovery calls and demos.
*   **RevOps Analyst**
    *   Standardizes lead data across the pipeline to improve the accuracy of lead scoring models.

---

## Features
- **Automated Data Enrichment**
  Instantly append professional titles, company details, and social profiles to leads using PeopleDataLabs.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely connect the Uplizd agent to your CRM and data enrichment APIs.
- **Real-Time Processing**
  Triggers enrichment the moment a new lead enters the system, ensuring data is ready before the first touchpoint.
- **Intelligent Data Mapping**
  Automatically maps enriched data fields to your existing CRM schema for seamless integration.
- **Customizable Logic**
  Configure the agent to prioritize specific data points or skip enrichment for leads that already meet a quality threshold.

---

## Use Cases
**Lead Qualification & Scoring**
*   Automatically populate missing industry and company size fields to trigger high-intent lead scores.
*   Filter out low-quality leads by verifying professional email addresses and current employment status.

**Personalized Sales Outreach**
*   Inject enriched prospect data into email templates to create hyper-personalized cold outreach sequences.
*   Provide sales teams with a "cheat sheet" of prospect background info before scheduled discovery meetings.

**CRM Data Hygiene**
*   Run bulk enrichment jobs on legacy database records to refresh outdated contact information.
*   Standardize job titles and company names to ensure clean reporting and accurate territory assignment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your PeopleDataLabs and CRM connections within the integration settings.
4. Ensure nodes are correctly connected in the order: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the lead email or identifier from your CRM or web form.
*   **Agent**: Processes the data and instructs the enrichment tool to fetch missing details.
*   **Composio Toolset**: Executes the API call to PeopleDataLabs to retrieve the prospect profile.
*   **Chat Output**: Returns the enriched data object back to your CRM or displays it in the dashboard.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Enrich the lead profile for john.doe@example.com`
* `Find the current company and job title for the lead with email contact@techcorp.com`
* `Update the CRM record for this lead with the latest professional data from PeopleDataLabs`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your input data and the enrichment API.
*   Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: "Extract the email address, query the PeopleDataLabs tool, and format the response as a JSON object."
*   Ensure the agent is configured to handle null values gracefully if no data is found.

### 2) Composio Toolset Node
*   Requires a valid PeopleDataLabs API Key configured within your Composio account.
*   Scope: Ensure the connection has `read` access to person and company enrichment endpoints.

### 3) Tool Availability
*   `peopledatalabs_person_enrichment`: Fetches detailed professional profiles.
*   `peopledatalabs_company_enrichment`: Retrieves firmographic data for prospect companies.
*   `crm_update_record`: Writes the enriched data back to your specific CRM fields.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data using Dropcontact.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep research on target accounts using ZoomInfo.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
