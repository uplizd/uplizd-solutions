# News Aggregator (Uplizd) - Real-time automated content curation and intelligence

## Summary
The News Aggregator (Uplizd) workflow automates the discovery, extraction, and synthesis of web-based information, transforming fragmented online content into a structured, single source of truth. By leveraging AI-driven parsing and real-time data integration, this solution eliminates manual browsing, accelerates content pipeline velocity, and ensures your team stays informed with high-fidelity, actionable insights.

---

## Demo
![News Aggregator workflow interface showing automated content extraction and summary generation](image.png)
**Alt text (SEO-ready):** News Aggregator workflow in Uplizd for automated web content extraction, data parsing, and AI-driven news synthesis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b523f0db-fb2c-5d91-bc85-9aa955fa862e)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** news aggregation, web scraping, content curation, ai workflow, data pipeline, research automation, composio
- This solution bridges the gap between raw web data and structured intelligence, enabling automated content workflows for research and monitoring.

---

## Who is this for?
This solution is designed for professionals who need to monitor digital landscapes and synthesize information at scale.

- **Market Researchers**
    - Automate the collection of industry news to identify emerging trends and competitive shifts without manual monitoring.
- **Content Strategists**
    - Curate high-quality source material for newsletters and blog posts by filtering through vast amounts of real-time web data.
- **Sales Intelligence Leads**
    - Track prospect-related news and company announcements to time outreach efforts perfectly based on external triggers.
- **Data Analysts**
    - Ingest unstructured web content into structured formats for downstream analysis and reporting within existing CRM or BI tools.

---

## Features
- **Automated Web Extraction**
    - Utilizes advanced parsing to pull relevant text and metadata from diverse web sources in real-time.
- **AI-Powered Synthesis**
    - Employs LLMs to summarize, categorize, and extract key entities from aggregated content streams.
- **Composio Toolset Integration**
    - Connects seamlessly with web browsing and search tools to ensure data freshness and accuracy.
- **Customizable Filtering**
    - Defines specific keywords and source parameters to ensure only high-signal information reaches your dashboard.
- **Pipeline Velocity**
    - Reduces the time from content publication to internal team notification, enabling faster decision-making.

---

## Use Cases
**Competitive Intelligence**
- Monitor competitor press releases and product launch pages to update internal battlecards automatically.
- Track industry-specific news outlets to identify shifts in market sentiment or regulatory changes.

**Content Curation**
- Aggregate daily headlines from niche industry blogs to populate a centralized internal research database.
- Filter and summarize long-form articles into concise executive briefs for internal stakeholder distribution.

**Lead & Account Monitoring**
- Track news mentions of target accounts to trigger personalized outreach sequences in your CRM.
- Identify funding announcements or executive changes within your target market to prioritize high-value prospects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the News Aggregator workflow to your Uplizd workspace.
3. Configure your API keys for the required Composio toolsets within the integration settings.
4. Ensure nodes are correctly mapped and the agent is connected to your preferred LLM provider.

### 2) Setup the Nodes
- **Chat Input:** Receives the target URLs or search topics from the user.
- **Agent:** Processes the input, determines the search strategy, and analyzes the retrieved content.
- **Composio Toolset:** Executes web searches and content extraction tasks based on agent instructions.
- **Chat Output:** Delivers the synthesized summary and key takeaways to the user.

### 3) Run the Flow
Open the Uplizd Playground and test the workflow with these prompts:
- `Summarize the latest news regarding AI integration in CRM platforms from the last 24 hours.`
- `Extract key product updates from the following URL: [Insert URL]`
- `Find and summarize recent competitor announcements for [Company Name].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary intelligence layer for parsing and summarizing web data.
- **Recommended instruction pattern:**
    - Act as a professional research assistant specializing in real-time data synthesis.
    - Prioritize factual accuracy and extract only the most relevant information based on the user's focus.
    - Format output clearly, highlighting key entities, dates, and actionable insights.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable web browsing and search capabilities.
- **Connection Scope:** Ensure the connection is authorized to access public web data and search engines.

### 3) Tool Availability
- **Web Search:** Real-time query execution for finding current news and articles.
- **Content Parser:** Capability to strip boilerplate and extract core content from target web pages.
- **Data Formatter:** Ability to output results in structured formats like JSON or Markdown tables.

---

## Related Solutions
- [YouTube Insight Agent](../you-tube-analysis-by/README.md) — Analyze video content and audience engagement metrics.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather and report on account-level intelligence for sales teams.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into target accounts.
