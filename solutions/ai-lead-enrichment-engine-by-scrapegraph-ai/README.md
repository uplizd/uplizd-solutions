# AI Lead Enrichment Engine (Uplizd) - Automated web-scraping for high-fidelity lead data

## Summary
The AI Lead Enrichment Engine by ScrapeGraph AI streamlines your sales pipeline by automatically extracting and structuring critical lead data from company websites and social profiles. By leveraging intelligent scraping agents, this workflow eliminates manual data entry, ensuring your CRM is populated with accurate, real-time intelligence to improve lead scoring, personalization, and conversion rates.

---

## Demo
![AI Lead Enrichment Engine workflow showing data extraction from web sources to CRM](image.png)
**Alt text (SEO-ready):** Uplizd AI Lead Enrichment Engine workflow using ScrapeGraph AI for automated web scraping, CRM data synchronization, and sales lead intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5c79e36a-90b4-53b0-897c-32310dc777f1)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, lead enrichment, scrapegraph, data scraping, sales intelligence, pipeline velocity, lead qualification, ai workflow
This solution bridges the gap between raw web data and actionable CRM insights, enabling automated lead research at scale.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate the tedious research phase of the sales cycle.

*   **Sales Development Reps (SDRs)**
    *   Instantly gather prospect background info to craft hyper-personalized outreach sequences.
*   **Revenue Operations (RevOps) Managers**
    *   Maintain high-quality CRM hygiene by ensuring lead records are consistently updated with external data.
*   **Growth Marketers**
    *   Identify and qualify target accounts by scraping competitor or industry-specific web signals.
*   **Account Executives**
    *   Prepare for discovery calls with deep, automated insights into prospect company initiatives and recent news.

---

## Features
- **Automated Web Scraping**
  Utilizes ScrapeGraph AI to navigate and extract unstructured data from target websites and social profiles.
- **Intelligent Data Structuring**
  Transforms raw HTML and text into clean, structured JSON formats ready for CRM ingestion.
- **CRM Integration**
  Seamlessly pushes enriched data points into your existing CRM fields using the Composio Toolset.
- **Real-time Lead Intelligence**
  Provides up-to-date company insights, reducing reliance on stale, third-party lead databases.
- **Customizable Extraction Logic**
  Configure the agent to prioritize specific data points like funding rounds, key personnel, or product offerings.

---

## Use Cases
**Lead Qualification & Scoring**
*   Automatically scrape company "About" pages to verify if a lead matches your Ideal Customer Profile (ICP).
*   Extract recent press releases or blog posts to score leads based on company growth signals.

**Personalized Outreach**
*   Gather specific pain points mentioned on a prospect's website to tailor cold email openers.
*   Identify current tech stack components from a company's careers or engineering pages for targeted selling.

**CRM Data Hygiene**
*   Bulk-enrich existing lead records with missing website URLs or social media handles.
*   Update company descriptions and industry tags to ensure accurate segmentation in your CRM.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the AI Lead Enrichment Engine template from the library.
3. Connect your preferred CRM and ScrapeGraph AI credentials in the integration settings.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target company URL or lead identifier.
*   **Agent**: Orchestrates the extraction logic and processes the scraped content.
*   **Composio Toolset**: Executes the web scraping commands and pushes data to the CRM.
*   **Chat Output**: Confirms the enrichment status and displays the extracted lead data.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
* `Enrich the lead at https://example-company.com and update the CRM record.`
* `Find the latest news and key product offerings for https://tech-startup.io.`
* `Extract the company description and industry from https://enterprise-corp.com and save to lead notes.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for parsing and mapping scraped data.
*   Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: "Extract specific fields from the provided web content and map them to the CRM schema."
*   Instruction: "If data is missing, flag the lead for manual review rather than inserting incorrect values."

### 2) Composio Toolset Node
*   Provide your ScrapeGraph AI API key to enable web extraction capabilities.
*   Ensure the connection scope includes read access to target web domains and write access to your CRM.

### 3) Tool Availability
*   **Web Scraper**: Handles site navigation and HTML parsing.
*   **CRM Connector**: Manages data insertion and field updates.
*   **Data Formatter**: Cleans and normalizes extracted text for database compatibility.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate lead research using Dropcontact data.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive prospect research powered by ZoomInfo.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Track and score sales opportunities automatically.
