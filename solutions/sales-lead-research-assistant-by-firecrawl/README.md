# Sales Lead Research Assistant (Uplizd) - Automated prospect intelligence and company data enrichment

## Summary
The Sales Lead Research Assistant is an intelligent Uplizd workflow designed to automate the manual burden of prospect research and company background analysis. By leveraging the Firecrawl integration, this solution crawls target websites, extracts key business intelligence, and synthesizes actionable insights for sales teams. It serves as a single source of truth for lead qualification, significantly increasing pipeline velocity by providing SDRs and AEs with pre-researched, high-quality data before they even initiate contact.

---

## Demo
![Sales Lead Research Assistant workflow diagram showing Firecrawl data extraction and AI analysis](image.png)
**Alt text (SEO-ready):** Sales Lead Research Assistant workflow diagram showing Firecrawl data extraction, AI-driven prospect analysis, and Uplizd integration for automated lead intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-878fe6b8-blue?logo=uplizd)](https://uplizd.ai/solutions/878fe6b8-50bd-5781-9fe5-952ebf9baeec)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** sales, lead research, firecrawl, prospect intelligence, data enrichment, pipeline, composio, ai workflow

This solution bridges the gap between raw web data and sales-ready insights, streamlining the research phase of the modern RevOps stack.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual research bottlenecks and improve lead quality.

- **Sales Development Representative (SDR)**
  - Accelerates daily prospecting by automating the collection of company news and firmographic data.
- **Account Executive (AE)**
  - Prepares for discovery calls with synthesized research summaries that highlight pain points and growth signals.
- **Revenue Operations Manager**
  - Ensures consistent data hygiene and research depth across the sales organization by standardizing the enrichment process.
- **Growth Marketer**
  - Identifies ideal customer profile (ICP) alignment by analyzing website content and messaging for target accounts.

---

## Features
- **Automated Web Crawling**
  - Uses Firecrawl to scrape target prospect websites in real-time, capturing current product offerings and company messaging.
- **AI-Driven Insight Synthesis**
  - Processes unstructured web data into structured summaries, identifying key value propositions and potential sales triggers.
- **CRM-Ready Data Formatting**
  - Normalizes research findings into a standardized format that can be pushed directly into your CRM or sales engagement platform.
- **Real-Time Signal Detection**
  - Monitors for specific keywords or business events (e.g., new funding, product launches) that indicate high-intent buying signals.
- **Composio Toolset Integration**
  - Seamlessly connects the research agent to external tools and APIs, ensuring the workflow remains extensible and scalable.

---

## Use Cases
**Prospect Qualification**
- Automatically verify if a prospect's current tech stack aligns with your product's integration capabilities.
- Summarize a prospect's "About Us" page to identify their core business mission and target audience.

**Account Strategy**
- Generate a "Pre-Call Brief" containing the latest company news and recent blog post topics for upcoming meetings.
- Identify potential pain points based on the prospect's current website messaging and service offerings.

**Sales Pipeline Hygiene**
- Enrich existing CRM records with missing firmographic details extracted directly from the prospect's primary domain.
- Flag accounts that no longer match your ICP based on recent changes in their web-based business focus.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the solution JSON file provided in the repository.
3. Connect your Firecrawl API key and CRM credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company URL or prospect name from the user.
- **Agent**: Analyzes the input and triggers the research logic based on the provided instructions.
- **Composio Toolset**: Executes the Firecrawl web-scraping tasks to retrieve live data.
- **Chat Output**: Delivers the synthesized research report and actionable sales insights to the user.

### 3) Run the Flow
Open the Uplizd Playground and test the workflow with these prompts:
- `Research the company at https://example-prospect.com and summarize their core value proposition.`
- `Find recent news or product updates for the company at https://target-account.com.`
- `Based on the website content at https://prospect-site.com, list 3 potential pain points our solution can address.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary research analyst, responsible for interpreting scraped data and drafting professional summaries.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data extraction.
- Instruct the agent to prioritize "Sales-Ready" information over generic company history.
- Ensure the agent maintains a professional, objective tone suitable for sales briefings.

### 2) Composio Toolset Node
- Provide a valid API key for the Firecrawl integration.
- Set the connection scope to allow read-only access to web content for research purposes.

### 3) Tool Availability
- **Firecrawl**: For deep-crawling and scraping website content.
- **Search API**: For fetching supplemental news or social signals.
- **CRM Connector**: For pushing enriched data back into your sales pipeline.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Comprehensive account intelligence and background research.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automated reporting on account activity and lead signals.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Multi-platform synchronization for consistent lead data.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Scoring and tracking high-value sales opportunities.
