# Automated Market Research Agent (Uplizd) - Real-time competitive intelligence and data gathering

## Summary
The Automated Market Research Agent leverages the Composio Toolset to perform deep web analysis and data extraction, providing businesses with a single source of truth for market trends and competitor activity. By automating the research pipeline, this workflow eliminates manual data collection, ensuring your team has high-velocity access to actionable insights and market hygiene.

---

## Demo
![Automated Market Research Agent workflow showing web scraping and data synthesis nodes](image.png)
**Alt text (SEO-ready):** Automated Market Research Agent by Scrape.do for real-time web data extraction, market intelligence, and AI-driven competitive analysis on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dfef8554-db2c-589b-aa59-3ab8ad06ffce)

---

## Category
- **Primary category:** Market intelligence
- **Secondary tags:** research, competitive analysis, data extraction, web scraping, market trends, composio, ai workflow, business intelligence
- This solution bridges the gap between raw web data and strategic decision-making by automating the collection and synthesis of market signals.

---

## Who is this for?
This agent is designed for professionals who need to maintain a competitive edge through data-driven insights.

- **Market Researchers**
    - Automate the discovery of emerging industry trends and competitor product launches.
- **Product Managers**
    - Gather real-time feedback and feature comparisons to inform roadmap prioritization.
- **Sales Operations**
    - Monitor account intelligence to identify new opportunities and market shifts.
- **Growth Marketers**
    - Aggregate competitor ad strategies and content performance metrics for campaign optimization.

---

## Features
- **Automated Web Scraping**
  Utilizes the Scrape.do integration to pull clean, structured data from target websites in real-time.
- **Intelligent Data Synthesis**
  The Agent node processes raw HTML or text data into concise, actionable executive summaries.
- **Multi-Source Aggregation**
  Consolidates information from various domains into a unified report format for immediate consumption.
- **Customizable Research Parameters**
  Allows users to define specific search queries, target URLs, and focus areas for tailored intelligence.
- **Seamless Workflow Integration**
  Connects directly to your existing CRM or communication tools via the Composio Toolset to push insights where they are needed most.

---

## Use Cases
**Competitive Benchmarking**
- Track competitor pricing changes and feature updates across multiple landing pages.
- Generate side-by-side comparison tables for product positioning analysis.

**Market Trend Analysis**
- Identify trending topics and keywords within your industry to guide content strategy.
- Monitor regulatory or news updates that impact your specific market vertical.

**Lead Intelligence Gathering**
- Automatically scrape company profiles to enrich lead data before sales outreach.
- Identify recent funding rounds or executive changes to time your engagement effectively.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Automated Market Research Agent.
2. Click "Import" to add the workflow to your workspace.
3. Configure your Scrape.do API credentials within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the research topic or target URL from the user.
- **Agent**: Analyzes the request and determines the necessary search or scraping actions.
- **Composio Toolset**: Executes the web extraction commands via Scrape.do.
- **Chat Output**: Delivers the synthesized research report back to the user.

### 3) Run the Flow
Use the Playground to test your research capabilities with these prompts:
- `Research the latest pricing tiers for [Competitor Name] and summarize their value proposition.`
- `Find recent news articles regarding [Industry Trend] and extract the key takeaways.`
- `Analyze the landing page at [URL] and identify the top 3 customer pain points mentioned.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary analyst, interpreting raw data into business-ready insights.
- Instruct the agent to prioritize accuracy and cite sources where possible.
- Configure the agent to ignore boilerplate text and focus on core value propositions.
- Set the output format to structured Markdown for readability.

### 2) Composio Toolset Node
- Provide your Scrape.do API key to enable secure access to web data.
- Define the connection scope to allow the agent to navigate and extract content from authorized domains.

### 3) Tool Availability
- **Web Scraper**: Capability to fetch and parse HTML content.
- **Data Parser**: Capability to convert unstructured text into JSON or Markdown.
- **Search Query Engine**: Capability to locate relevant URLs based on user-provided keywords.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive intelligence on specific business accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting on account activity and engagement.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) - Extracting market signals from video content and audience feedback.
