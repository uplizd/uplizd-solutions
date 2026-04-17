# Market Research Agent (Uplizd) - Automated business intelligence and company data extraction

## Summary
The Market Research Agent is an Uplizd AI workflow designed to automate the discovery and synthesis of corporate intelligence. By leveraging the Composio Toolset to query live web and database sources, it transforms raw company information into structured, actionable insights, significantly reducing the manual effort required for competitive analysis and lead qualification.

---

## Demo
![Market Research Agent workflow interface showing automated data extraction and structured output generation](image.png)
**Alt text (SEO-ready):** Market Research Agent (Uplizd) workflow for automated business intelligence, company data extraction, and competitive analysis using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/39448e84-d821-5304-801f-dc40ce01b5c4)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** research, business intelligence, data extraction, competitive analysis, lead enrichment, composio, ai workflow, market insights
- This solution streamlines the collection of external business data, providing a centralized source of truth for market research and strategic planning.

---

## Who is this for?
This workflow is designed for professionals who need to synthesize vast amounts of company data into clear, actionable reports.

- **Market Researchers**
    - Automate the aggregation of competitor data and industry trends to save hours of manual browsing.
- **Sales Development Reps (SDRs)**
    - Instantly enrich lead profiles with verified business data before initiating outreach.
- **Strategy Consultants**
    - Generate structured company summaries and SWOT analysis points from disparate web sources.
- **Product Managers**
    - Monitor competitor feature sets and market positioning to inform product roadmap decisions.

---

## Features
- **Automated Data Extraction**
    - Uses advanced agents to scrape and parse relevant business information from target company websites.
- **Structured Output Generation**
    - Formats unstructured web data into clean, readable tables and summaries for immediate use.
- **Composio Toolset Integration**
    - Connects seamlessly with search and data tools to fetch real-time information from the web.
- **Customizable Research Parameters**
    - Allows users to define specific data points to track, such as funding rounds, employee count, or tech stacks.
- **Real-time Synthesis**
    - Processes multiple data sources concurrently to provide a comprehensive view of a target entity.

---

## Use Cases
**Competitive Intelligence**
- Researching competitor product launches and pricing updates across multiple regions.
- Comparing market positioning between two or more industry rivals based on public data.

**Lead Enrichment**
- Automatically pulling key firmographic data for high-value accounts during the prospecting phase.
- Identifying recent company news or press releases to personalize outbound sales messaging.

**Strategic Planning**
- Aggregating industry-wide news to identify emerging market threats or opportunities.
- Compiling quarterly reports on target account health and growth trajectories.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Market Research Agent template from the solution library.
3. Authenticate your required API keys within the Composio Toolset node.
4. Ensure nodes are correctly connected from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company name or URL from the user.
- **Agent**: Orchestrates the research process and synthesizes findings.
- **Composio Toolset**: Executes search queries and data extraction tasks.
- **Chat Output**: Delivers the structured research report to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Research the current market positioning and recent funding news for [Company Name].`
- `Find the top 3 competitors for [Company Name] and summarize their main value propositions.`
- `Create a structured summary of [Company Name] including their industry, headquarters, and key product offerings.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary analyst, responsible for interpreting search results and formatting the final output.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data synthesis.
- Set the system instruction to prioritize factual accuracy and structured formatting.
- Ensure the agent is configured to handle missing data gracefully by noting "Information not found" rather than hallucinating.

### 2) Composio Toolset Node
- Provide a valid API key for the search and web-scraping tools.
- Set the connection scope to allow the agent to access public web data and search engines.

### 3) Tool Availability
- **Web Search**: For retrieving the latest company news and public records.
- **Data Parser**: For extracting specific text elements from company landing pages.
- **Summarization Engine**: For distilling long-form articles into bulleted insights.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive research and intelligence gathering for specific accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automated reporting on account activity and lead signals.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Analyzing competitor video content and market presence.
