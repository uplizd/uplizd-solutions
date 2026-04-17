# Lead Generation Scraper (Uplizd) - Automated business lead extraction and enrichment

## Summary
The Lead Generation Scraper (Uplizd) is an automated AI workflow designed to identify, extract, and qualify business leads from target websites and directories at scale. By leveraging the Composio Toolset to interface with web scraping engines, this solution eliminates manual data entry, accelerates pipeline velocity, and ensures your CRM is populated with high-intent, verified prospect data.

---

## Demo
![Lead Generation Scraper workflow showing web extraction and CRM sync](image.png)
**Alt text (SEO-ready):** Lead Generation Scraper workflow for automated business lead extraction, data enrichment, and CRM synchronization using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d34d5cb4-6f39-5d11-be90-2658d03dbefd)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead generation, web scraping, crm, data enrichment, sales prospecting, composio, ai workflow, pipeline growth
- This solution bridges the gap between raw web data and actionable sales intelligence, streamlining the transition from prospect discovery to CRM entry.

---

## Who is this for?
This solution is designed for revenue teams looking to automate top-of-funnel activities and maintain a consistent flow of qualified leads.

- **Sales Development Rep (SDR)**
    - Automates the time-consuming process of manual list building and contact research.
- **Growth Marketer**
    - Enables rapid identification of target accounts for high-volume outreach campaigns.
- **Revenue Operations (RevOps) Manager**
    - Ensures data hygiene by standardizing how lead information is captured and formatted before CRM ingestion.
- **Founder / Small Business Owner**
    - Provides enterprise-grade lead acquisition capabilities without the need for dedicated data entry staff.

---

## Features
- **Automated Web Extraction**
    - Uses advanced scraping logic to pull contact details, company names, and job titles directly from target URLs.
- **Intelligent Lead Qualification**
    - Employs AI to filter scraped data against your specific Ideal Customer Profile (ICP) criteria in real-time.
- **Seamless CRM Integration**
    - Automatically pushes enriched lead data into your CRM, mapping fields correctly to reduce manual cleanup.
- **Real-time Data Enrichment**
    - Connects with external data providers via Composio to append missing contact information or social profiles.
- **Scalable Pipeline Velocity**
    - Processes hundreds of prospects in minutes, significantly reducing the time-to-contact for new opportunities.

---

## Use Cases
**Targeted Prospecting**
- Extracting contact lists from industry-specific directories or competitor partner pages.
- Identifying key decision-makers on corporate "About Us" or "Team" pages.

**Data Enrichment & Hygiene**
- Updating existing CRM records with the latest website-derived contact information.
- Standardizing lead formatting to ensure consistent data quality across your sales database.

**Market Research**
- Monitoring competitor website updates to track new service offerings or regional expansions.
- Aggregating public business data to build custom market intelligence reports.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Generation Scraper template from the solution library.
3. Connect your preferred CRM and web scraping API keys within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target URL or search parameters from the user.
- **Agent**: Analyzes the input, triggers the scraper, and validates the extracted data.
- **Composio Toolset**: Executes the web scraping and CRM write operations.
- **Chat Output**: Delivers a summary of the extracted leads and confirmation of CRM status.

### 3) Run the Flow
Use the Playground to test your scraping logic with these prompts:
- `Extract all contact emails and names from [URL] and add them to my 'New Leads' CRM list.`
- `Find the LinkedIn profiles of the leadership team listed on [URL] and save them to a spreadsheet.`
- `Scrape the company details from [URL] and check if they match our target ICP criteria.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for web navigation and data parsing.
- **Instruction Pattern:**
    - "You are an expert lead generation assistant; extract only high-quality business contact data."
    - "Validate all scraped data against the provided ICP criteria before attempting a CRM write."
    - "If a website structure is complex, use the Composio toolset to perform a deep-crawl of the page."

### 2) Composio Toolset Node
- Provide your API key to authorize the agent to perform web scraping and CRM write actions.
- Ensure the connection scope includes read access for web scraping and write access for your CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- **Web Scraper**: For parsing HTML and extracting structured data.
- **CRM Connector**: For creating or updating lead/contact objects.
- **Data Validator**: For verifying email formats and company domain validity.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact details.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research for high-value enterprise accounts.
