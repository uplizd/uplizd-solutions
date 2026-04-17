# Lead Data Extractor (Uplizd) - Automated prospect intelligence and web data harvesting

## Summary
The Lead Data Extractor (Uplizd) is an intelligent AI workflow designed to automate the harvesting of prospect information from LinkedIn and company websites. By leveraging the Composio Toolset to navigate web content and extract structured data, this solution eliminates manual entry, accelerates lead qualification, and ensures your CRM is populated with high-quality, real-time contact intelligence.

---

## Demo
![Lead Data Extractor workflow interface showing browser-based data extraction and CRM mapping](image.png)
**Alt text (SEO-ready):** Uplizd Lead Data Extractor workflow showing browser-based prospect data harvesting and CRM integration for sales automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/22235d69-8558-5055-9b27-c0934a062c68)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead generation, web scraping, crm, sales intelligence, prospect data, automation, composio, ai workflow
- This solution bridges the gap between raw web presence and actionable CRM data, streamlining the top-of-funnel research process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual research time and improve lead data accuracy.

- **Sales Development Representative (SDR)**
    - Automates the tedious process of scraping prospect contact details and company background info from LinkedIn.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent data hygiene by standardizing how lead information is captured and formatted before entering the CRM.
- **Growth Marketer**
    - Quickly gathers intelligence on target accounts to personalize outreach campaigns at scale.
- **Account Executive (AE)**
    - Reduces pre-call research time by having key prospect data and company insights ready in the CRM before the first meeting.

---

## Features
- **Automated Web Extraction**
    - Uses browser-based tools to navigate and pull relevant prospect data from LinkedIn profiles and company websites.
- **Intelligent Data Parsing**
    - Employs AI to identify, clean, and structure unstructured web text into standardized contact fields.
- **CRM Integration**
    - Seamlessly pushes extracted data into your CRM, ensuring that lead records are created or updated without manual input.
- **Real-Time Processing**
    - Operates on-demand to fetch the most current information, reducing the risk of working with stale or outdated contact data.
- **Customizable Extraction Logic**
    - Allows users to define specific data points to capture, such as job titles, company size, or recent professional milestones.

---

## Use Cases
**Lead Prospecting**
- Automatically extract contact details from a list of LinkedIn profile URLs to populate your sales pipeline.
- Gather company background information to score leads based on industry fit and recent growth signals.

**CRM Enrichment**
- Update existing CRM records with the latest job titles and company affiliations found on the web.
- Fill in missing contact fields like professional email addresses or direct phone numbers discovered during web research.

**Sales Intelligence**
- Monitor target company websites for new leadership announcements or product launches to time your outreach perfectly.
- Compile a summary of a prospect's professional history to create highly personalized cold-outreach emails.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Configure your API credentials for the browser-based extraction tools.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target URL or company name from the user.
- **Agent**: Processes the intent and directs the extraction logic.
- **Composio Toolset**: Executes browser commands to scrape and parse the requested web data.
- **Chat Output**: Returns the structured prospect data to the user or confirms the CRM update.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Extract contact details from this LinkedIn profile: [URL]`
- `Find the current company size and industry for [Company Name] from their website.`
- `Scrape the latest professional updates from this prospect's profile: [URL]`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator, translating user requests into specific browser actions.
- Use a model capable of complex reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on how to handle missing data or non-standard page layouts.
- Define the output schema to ensure the extracted data matches your CRM field requirements.

### 2) Composio Toolset Node
- Connect your Composio API key to enable secure access to browser automation tools.
- Ensure the connection scope includes permissions for web navigation and data extraction.

### 3) Tool Availability
- **Browser Navigation**: Allows the agent to visit specific URLs.
- **Content Extraction**: Enables the agent to parse text, tables, and metadata from web pages.
- **Data Formatting**: Provides the ability to convert raw scrapes into JSON or CSV formats.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data using external intelligence providers.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research assistant for target account profiling.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your CRM records synchronized across multiple platforms.
