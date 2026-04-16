# B2B Lead Generation Agent (Uplizd) - Automated prospecting and business data extraction

## Summary
The B2B Lead Generation Agent by Agenty is a powerful Uplizd workflow designed to automate the discovery and qualification of business prospects. By leveraging advanced web scraping and data extraction capabilities, this solution enables sales teams to populate their pipelines with high-intent leads, reducing manual research time and ensuring a consistent flow of actionable contact information directly into your CRM.

---

## Demo
![B2B Lead Generation Agent workflow showing web extraction nodes and CRM integration](image.png)
**Alt text (SEO-ready):** B2B Lead Generation Agent workflow by Agenty for automated sales prospecting, web scraping, and CRM data enrichment on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/6d16cc1a-d980-5a84-b70c-2bd0fd585677)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** b2b, lead generation, agenty, web scraping, sales prospecting, data enrichment, pipeline velocity, composio

This solution bridges the gap between raw web data and structured sales intelligence, enabling automated lead acquisition for modern RevOps teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outbound efforts without increasing manual overhead.

*   **Sales Development Representative (SDR)**
    *   Automates the tedious process of finding and validating contact information for target accounts.
*   **Growth Marketer**
    *   Identifies new market segments and prospect lists by scraping industry-specific directories.
*   **Revenue Operations (RevOps) Manager**
    *   Ensures data hygiene by standardizing lead inputs before they reach the CRM.
*   **Founder/CEO**
    *   Accelerates early-stage customer acquisition by surfacing high-quality leads with minimal manual effort.

---

## Features
- **Automated Web Extraction**
  Utilizes the Agenty engine to navigate business directories and extract structured data points in real-time.
- **Intelligent Lead Qualification**
  Uses the Agent node to filter prospects based on predefined criteria like company size, industry, or location.
- **CRM Integration**
  Seamlessly pushes validated leads into your existing CRM stack using the Composio Toolset for instant availability.
- **Data Standardization**
  Cleans and formats extracted contact details to ensure consistency across your sales database.
- **Real-time Pipeline Updates**
  Triggers immediate notifications or CRM updates as soon as a new high-value lead is identified.

---

## Use Cases
**Outbound Prospecting**
*   Extracting contact lists from industry-specific business directories or conference attendee pages.
*   Monitoring competitor websites for new partnership or client announcements to identify potential leads.

**Market Research**
*   Aggregating company data from public listings to build a target account list for new territory expansion.
*   Analyzing prospect website signals to score leads based on technological stack or recent hiring trends.

**CRM Enrichment**
*   Bulk-updating existing CRM records with missing contact information or updated business details.
*   Automating the creation of new lead objects in your CRM whenever a prospect meets specific qualification thresholds.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your Agenty and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped and all API keys are active before triggering the first run.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target search parameters or URL list.
*   **Agent**: Processes the input, executes the scraping logic, and qualifies the leads.
*   **Composio Toolset**: Connects the agent to Agenty and your CRM for data extraction and syncing.
*   **Chat Output**: Delivers the summary of extracted leads and confirmation of CRM entry.

### 3) Run the Flow
Use the Playground to test your lead generation parameters:
* `Find 10 software companies in the fintech sector based in London.`
* `Extract contact details from this directory URL: [insert URL] and add to my CRM.`
* `Identify potential leads from this list of companies and filter for those with over 50 employees.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your scraping logic.
*   Maintain a clear, instruction-heavy prompt defining the "ideal lead" profile.
*   Use the agent to perform multi-step reasoning: Search → Extract → Filter → Format.
*   Set the temperature to low (0.1–0.3) to ensure consistent data extraction and formatting.

### 2) Composio Toolset Node
*   Requires a valid Agenty API key for web scraping tasks.
*   Requires authorized CRM connection (e.g., Salesforce, HubSpot) to push leads.

### 3) Tool Availability
*   **Agenty Scraper**: Capability to parse HTML, extract tables, and follow pagination.
*   **CRM Connector**: Capability to create, update, and search for lead/account objects.
*   **Data Formatter**: Capability to normalize phone numbers, emails, and company names.

---

## Related Solutions
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive research into target accounts.
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automated reporting on account-level signals.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Multi-platform data synchronization for RevOps.
*   [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Tracking and scoring new sales opportunities.
