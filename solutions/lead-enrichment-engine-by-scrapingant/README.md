# Lead Enrichment Engine (Uplizd) - Automated B2B data enrichment via web scraping

## Summary
The Lead Enrichment Engine is an intelligent Uplizd workflow that automates the discovery and verification of lead data by leveraging real-time web scraping. By connecting directly to public business sources via ScrapingAnt, this solution eliminates manual research, ensuring your CRM is populated with accurate, high-fidelity prospect information to accelerate pipeline velocity and improve lead qualification accuracy.

---

## Demo
![Lead Enrichment Engine workflow showing Chat Input, ScrapingAnt agent, and CRM output](image.png)
**Alt text (SEO-ready):** Lead Enrichment Engine workflow on Uplizd using ScrapingAnt for automated B2B data scraping, CRM integration, and sales pipeline hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/b1f35c7f-bdf7-53ab-bd8b-74515fadc16c)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead enrichment, web scraping, scrapingant, crm, data hygiene, sales operations, prospecting, composio
- This solution bridges the gap between raw web data and actionable CRM records, providing a scalable way to maintain clean, enriched lead profiles.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate the tedious process of manual lead research.

- **Sales Development Reps (SDRs)**
    - Spend less time researching prospect details and more time engaging with qualified leads.
- **Revenue Operations (RevOps) Managers**
    - Ensure CRM data integrity by automating the ingestion of verified company firmographics.
- **Growth Marketers**
    - Quickly build targeted lead lists by scraping relevant industry data from public web sources.
- **Account Executives (AEs)**
    - Receive enriched account intelligence directly in their workflow before initiating high-value outreach.

---

## Features
- **Automated Web Scraping**
    - Leverages ScrapingAnt to extract real-time firmographic data from company websites and public directories.
- **CRM Data Sync**
    - Seamlessly maps scraped data points to your CRM fields, ensuring consistent and updated lead records.
- **Intelligent Data Parsing**
    - Uses the Agent node to clean, format, and validate raw scraped HTML into structured business intelligence.
- **Composio Toolset Integration**
    - Orchestrates the flow between web extraction tools and your CRM platform for a unified automation pipeline.
- **Scalable Enrichment**
    - Processes bulk lead lists or individual entries with high concurrency to maintain pipeline momentum.

---

## Use Cases
**Prospect Intelligence Gathering**
- Automatically extract key decision-maker contact details from company "About Us" pages.
- Identify current tech stacks and industry focus areas to personalize initial outreach emails.

**CRM Data Hygiene**
- Periodically refresh existing lead records with the latest company descriptions and location data.
- Detect and flag outdated lead information for manual review or automated archival.

**Sales Pipeline Acceleration**
- Trigger enrichment workflows immediately upon new lead creation to prioritize high-intent prospects.
- Populate missing firmographic fields to improve lead scoring accuracy within your CRM.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Enrichment Engine template from the solution gallery.
3. Configure your API credentials for ScrapingAnt and your target CRM within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company URL or lead identifier.
- **Agent**: Analyzes the request and directs the scraping logic.
- **Composio Toolset**: Executes the ScrapingAnt API calls to fetch data.
- **Chat Output**: Returns the enriched lead profile or confirms the CRM update.

### 3) Run the Flow
Use the Playground to test your enrichment logic:
- `Enrich the lead at https://example-company.com and update the CRM.`
- `Scrape the latest company description for the lead in row 45.`
- `Find the primary industry and location for the company at https://tech-startup.io.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for data extraction and mapping.
- Use a model capable of structured data extraction (e.g., GPT-4o).
- Instruct the agent to prioritize accuracy and handle empty fields gracefully.
- Define the specific CRM schema mapping in the system prompt.

### 2) Composio Toolset Node
- Provide your ScrapingAnt API key to enable web extraction capabilities.
- Set the connection scope to allow the agent to read web content and write to your CRM.

### 3) Tool Availability
- **ScrapingAnt**: For fetching raw web content and metadata.
- **CRM Connector**: For updating lead records (e.g., Salesforce, HubSpot).
- **Data Parser**: For cleaning and normalizing extracted text.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate deep account research and contact discovery.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and account data across multiple platforms.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Leverage ZoomInfo data for comprehensive account profiling.
