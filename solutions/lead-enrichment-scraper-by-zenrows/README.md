# Lead Enrichment Scraper (Uplizd) - Automated prospect data gathering and enrichment

## Summary
The Lead Enrichment Scraper (Uplizd) is an automated AI workflow designed to streamline the prospecting process by extracting and enriching lead data from public web sources. By leveraging the ZenRows integration via the Composio Toolset, this solution eliminates manual research, providing sales and marketing teams with a single source of truth for high-quality prospect information, ultimately increasing pipeline velocity and data hygiene.

---

## Demo
![Lead Enrichment Scraper workflow showing Chat Input, Agent, ZenRows scraper, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Enrichment Scraper workflow in Uplizd using ZenRows for automated prospect data gathering and CRM enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1ca521c2-ee54-54c0-aa48-36f3cf2dec36)

---

## Category
*   **Primary category:** Sales automation
*   **Secondary tags:** lead enrichment, web scraping, zenrows, sales intelligence, data hygiene, prospect research, composio, ai workflow
*   This solution bridges the gap between raw web data and actionable CRM insights, ensuring your sales team spends less time researching and more time closing.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate manual data entry and improve lead quality.

*   **Sales Development Representative (SDR)**
    *   Automate the collection of prospect contact details and company background to prioritize outreach.
*   **Marketing Operations Manager**
    *   Ensure lead databases remain accurate and enriched with real-time data from public web sources.
*   **Account Executive (AE)**
    *   Gain instant access to deep-dive prospect intelligence before high-stakes discovery calls.
*   **Growth Marketer**
    *   Scale lead generation efforts by scraping and structuring public data at a fraction of the manual time.

---

## Features
- **Automated Web Extraction**
  Uses the ZenRows integration to bypass anti-bot measures and extract clean data from target websites.
- **Intelligent Data Parsing**
  The Agent node processes raw HTML/text into structured formats like JSON or CSV for immediate use.
- **CRM-Ready Formatting**
  Automatically maps scraped fields to standard CRM attributes, ensuring seamless integration with your existing sales stack.
- **Real-Time Enrichment**
  Fetches up-to-date company information and professional profiles on-demand, reducing data decay.
- **Composio Toolset Integration**
  Provides a robust framework for the agent to execute complex scraping tasks securely and reliably.

---

## Use Cases
**Prospect Intelligence Gathering**
*   Extracting key decision-maker contact information from company "About Us" or "Team" pages.
*   Aggregating recent company news or press releases to personalize cold outreach emails.

**Market Research & Analysis**
*   Scraping competitor pricing pages to maintain a real-time competitive landscape dashboard.
*   Collecting industry-specific event attendee lists to identify potential networking opportunities.

**CRM Data Hygiene**
*   Verifying existing lead data by cross-referencing public web profiles against CRM records.
*   Filling in missing company firmographics like industry, location, and employee count automatically.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Connect your ZenRows API key within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input:** Receives the target URL or company name from the user.
*   **Agent:** Orchestrates the scraping logic and interprets the extracted data.
*   **Composio Toolset:** Executes the ZenRows scraping function to retrieve web content.
*   **Chat Output:** Presents the enriched lead data in a structured, readable format.

### 3) Run the Flow
Open the Playground and try these prompts:
* `Scrape the contact page of [Company URL] and extract the names and titles of the leadership team.`
* `Find the latest company news for [Company Name] and summarize how it impacts their business.`
* `Extract the company description and primary industry from [Company URL] and format it for a CRM import.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the data analyst, translating user intent into specific scraping instructions.
*   Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: "You are a professional data researcher. Extract only relevant business information and ignore marketing fluff."
*   Instruction: "Always format the output as a clean table or structured JSON object."

### 2) Composio Toolset Node
*   Requires a valid ZenRows API key to handle complex web requests.
*   Ensure the connection scope is set to allow HTTP requests and data extraction.

### 3) Tool Availability
*   `zenrows_scrape`: Fetches raw content from public URLs.
*   `data_parser`: Converts unstructured text into structured fields.
*   `crm_formatter`: Maps extracted data to standard CRM schema.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data using professional contact databases.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Perform deep-dive research on target accounts for personalized sales outreach.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Leverage ZoomInfo data to build comprehensive account profiles.
