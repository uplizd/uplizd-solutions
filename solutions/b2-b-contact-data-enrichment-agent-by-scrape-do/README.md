# B2B Contact Data Enrichment Agent (Uplizd) - Automate lead intelligence and data hygiene

## Summary
The B2B Contact Data Enrichment Agent is an automated workflow designed to streamline lead management by fetching real-time contact details and professional insights. By leveraging the Scrape.do integration, this solution eliminates manual research, ensuring your CRM remains populated with accurate, high-quality data to accelerate pipeline velocity and improve outreach precision.

---

## Demo
![B2B Contact Data Enrichment Agent workflow showing input, Scrape.do processing, and CRM output](image.png)
**Alt text (SEO-ready):** B2B Contact Data Enrichment Agent workflow using Uplizd and Scrape.do for automated lead intelligence and CRM data synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ac76ee76-0e67-5496-a1f2-a2c297e37c7d)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** b2b, lead enrichment, crm, data hygiene, scrape.do, sales intelligence, lead qualification, composio
- This solution bridges the gap between raw lead lists and actionable intelligence by automating the enrichment process directly within your sales stack.

---

## Who is this for?
This solution is built for revenue teams looking to reduce manual data entry and improve lead targeting accuracy.

- **Sales Development Reps (SDRs)**
    - Instantly access verified contact details to reduce time spent on manual prospecting.
- **RevOps Managers**
    - Maintain high data hygiene standards across the CRM by automating the enrichment of incoming lead records.
- **Account Executives**
    - Gain deeper account intelligence before discovery calls to personalize outreach and increase conversion rates.
- **Marketing Operations Specialists**
    - Ensure lead scoring models are based on complete, up-to-date firmographic and contact data.

---

## Features
- **Automated Data Retrieval**
    - Uses Scrape.do to pull real-time professional contact information from public web sources.
- **CRM Integration Ready**
    - Seamlessly maps enriched data fields directly into your existing CRM workflows via the Composio Toolset.
- **Data Hygiene Enforcement**
    - Automatically identifies and fills missing contact fields, reducing record decay and duplicate entries.
- **Scalable Processing**
    - Handles bulk lead lists, allowing for high-volume enrichment without manual intervention.
- **Intelligent Formatting**
    - Standardizes contact data formats (e.g., job titles, company names) for consistent reporting and segmentation.

---

## Use Cases
**Lead Prospecting & Outreach**
- Automatically enrich raw email lists with LinkedIn profiles and company websites before launching a cold outreach campaign.
- Update lead records with current job titles and company sizes to ensure accurate lead scoring and routing.

**CRM Data Maintenance**
- Run periodic enrichment jobs to refresh stale contact data and remove outdated information from your database.
- Sync enriched firmographic data to segment accounts by industry or revenue tier for targeted account-based marketing.

**Sales Intelligence**
- Extract key decision-maker contact details from company websites to build high-intent account lists.
- Populate custom CRM fields with enriched data points to provide AEs with full context prior to initial outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to import the template into your workspace.
2. Connect your Scrape.do API key within the Composio Toolset node.
3. Map your CRM credentials to the output node to ensure data flows to the correct object.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead identifier (e.g., email or company URL).
- **Agent**: Orchestrates the enrichment logic and interprets the scraped results.
- **Composio Toolset**: Executes the web scraping and CRM update commands.
- **Chat Output**: Confirms the enrichment status and provides a summary of the updated fields.

### 3) Run the Flow
Use the Playground to test your enrichment logic with these prompts:
- `Enrich the contact record for john.doe@example.com.`
- `Find and update the company website and job title for the lead at acme-corp.com.`
- `Search for current contact information for the lead associated with this LinkedIn URL: [Insert URL].`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligence layer, parsing unstructured web data into structured CRM fields.
- Use a model capable of JSON extraction and structured output.
- Instruct the agent to prioritize verified contact sources over speculative data.
- Ensure the agent is configured to handle "not found" scenarios gracefully by flagging records for manual review.

### 2) Composio Toolset Node
- Provide your Scrape.do API key to enable web crawling capabilities.
- Define the connection scope to allow the agent to read/write to your specific CRM objects (e.g., Leads, Contacts, Accounts).

### 3) Tool Availability
- **Web Scraper**: For extracting professional contact details and firmographic data.
- **CRM Connector**: For pushing enriched data points into your database.
- **Data Formatter**: For standardizing strings and ensuring compliance with CRM field requirements.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain multi-platform data consistency and conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and standardize your CRM database for better reporting.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate comprehensive reports on account activity and intent.
