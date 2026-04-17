# Bulk LinkedIn Profile Processor (Uplizd) - Automated lead enrichment and contact data extraction

## Summary
The Bulk LinkedIn Profile Processor is an intelligent Uplizd workflow that automates the extraction and enrichment of contact data from LinkedIn profiles at scale. By leveraging the AeroLeads integration via the Composio Toolset, this solution eliminates manual data entry, providing sales and recruitment teams with a single source of truth for prospect information, significantly increasing pipeline velocity and data hygiene.

---

## Demo
![Bulk LinkedIn Profile Processor workflow showing data extraction from LinkedIn to CRM](image.png)
**Alt text (SEO-ready):** Uplizd workflow for bulk LinkedIn profile processing, contact data extraction, and lead enrichment using AeroLeads and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2706f7e6-716a-520c-8d8e-bb76a338dca1)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** linkedin, aeroleads, lead enrichment, data extraction, sales prospecting, crm, composio, ai workflow
- This solution streamlines the transition from raw LinkedIn profile URLs to actionable contact records within your sales stack.

---

## Who is this for?
This solution is designed for professionals who need to scale their outreach efforts without sacrificing data quality.

- **Sales Development Representative (SDR)**
    - Accelerates lead qualification by instantly populating CRM fields with verified contact details.
- **Recruitment Manager**
    - Simplifies candidate sourcing by extracting professional history and contact info from multiple profiles in one batch.
- **Growth Marketer**
    - Enables rapid audience building for targeted campaigns by automating the collection of prospect data.
- **RevOps Specialist**
    - Maintains high data hygiene standards by ensuring all imported LinkedIn data is standardized and formatted correctly.

---

## Features
- **Automated Data Extraction**
  Uses the AeroLeads API to pull structured contact data directly from LinkedIn profile URLs.
- **Bulk Processing Engine**
  Handles multiple profile requests in a single workflow execution to maximize throughput.
- **CRM Integration Ready**
  Seamlessly maps extracted data points like email, phone, and company name to your preferred CRM.
- **Real-time Enrichment**
  Validates and enriches profile data on-the-fly, ensuring only high-quality information enters your pipeline.
- **Composio-Powered Connectivity**
  Utilizes the Composio Toolset to manage secure authentication and API communication with AeroLeads.

---

## Use Cases
**Lead Prospecting**
- Extracting contact information from a list of target accounts for outbound cold outreach.
- Identifying key decision-makers within a specific industry to populate a new sales campaign.

**Talent Acquisition**
- Aggregating candidate contact details from LinkedIn to streamline the initial screening process.
- Building a talent pool database by processing bulk lists of potential hires from professional networks.

**Data Enrichment**
- Updating existing CRM records with missing contact data by cross-referencing LinkedIn profiles.
- Cleaning up outdated lead lists by verifying current professional details through automated lookups.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the template.
2. Import the workflow into your Uplizd dashboard.
3. Configure your AeroLeads API credentials within the Composio Toolset node.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the list of LinkedIn profile URLs from the user.
- **Agent**: Orchestrates the logic, interprets the request, and triggers the extraction tool.
- **Composio Toolset**: Executes the AeroLeads API calls to fetch and parse profile data.
- **Chat Output**: Returns the enriched contact data in a clean, readable format.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Process these LinkedIn profiles and extract contact emails: [URL1], [URL2], [URL3]`
- `Find the professional contact details for the following list of LinkedIn profiles.`
- `Extract data for these profiles and format the output as a CSV-ready list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent bridge between your input and the AeroLeads API.
- Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize data accuracy and handle empty results gracefully.
- Configure the system prompt to output data in a consistent JSON or table format.

### 2) Composio Toolset Node
- Provide your **AeroLeads API Key** in the integration settings.
- Set the connection scope to allow read access to profile data.

### 3) Tool Availability
- **Profile Lookup**: Capability to fetch data based on LinkedIn URL.
- **Data Parsing**: Capability to extract email, phone, and job title fields.
- **Error Handling**: Capability to report invalid URLs or missing profile data.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data using Dropcontact.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep research and intelligence gathering via ZoomInfo.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize and manage data across multiple CRM platforms.
