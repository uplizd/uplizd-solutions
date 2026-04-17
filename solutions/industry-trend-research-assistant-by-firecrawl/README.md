# Industry Trend Research Assistant (Uplizd) - Automated market intelligence and web-based trend discovery

## Summary
The Industry Trend Research Assistant is an automated AI workflow designed to streamline market intelligence gathering by leveraging Firecrawl for real-time web data extraction. This solution empowers business analysts and strategists to synthesize complex market signals into actionable insights, ensuring your organization maintains a competitive edge through data-driven decision-making and continuous environmental scanning.

---

## Demo
![Industry Trend Research Assistant workflow dashboard showing web data extraction and trend analysis nodes](image.png)
**Alt text (SEO-ready):** Industry Trend Research Assistant Uplizd workflow using Firecrawl for automated web data extraction, market intelligence, and trend analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bf944741-b0e0-5be3-b5e5-66cae1375a5a)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** research, firecrawl, web scraping, trend analysis, competitive intelligence, data extraction, ai workflow, business strategy
- This solution bridges the gap between raw web data and strategic planning by automating the discovery and synthesis of industry-specific trends.

---

## Who is this for?
This assistant is designed for professionals who need to stay ahead of rapidly shifting market dynamics.

- **Market Researchers**
    - Automate the collection of industry reports and news to reduce manual search time.
- **Strategic Planners**
    - Synthesize disparate web signals into coherent long-term growth strategies.
- **Competitive Intelligence Leads**
    - Monitor competitor activities and market shifts in real-time to adjust positioning.
- **Product Managers**
    - Identify emerging customer needs and feature trends by analyzing industry-wide discussions.

---

## Features
- **Automated Web Extraction**
    - Uses Firecrawl to convert complex web pages into clean, LLM-ready markdown for precise analysis.
- **Real-time Trend Synthesis**
    - Aggregates data across multiple sources to identify patterns, anomalies, and emerging market opportunities.
- **Customizable Research Scope**
    - Allows users to define specific industries, keywords, or competitor domains for highly targeted intelligence gathering.
- **Intelligent Summarization**
    - Distills massive amounts of web content into concise executive summaries and bulleted insight reports.
- **Seamless Integration**
    - Connects directly with the Composio Toolset to trigger downstream actions based on research findings.

---

## Use Cases
**Competitive Benchmarking**
- Track competitor product launches and pricing strategy shifts across their official documentation.
- Compare industry-wide sentiment regarding specific technology stacks or service offerings.

**Market Opportunity Discovery**
- Identify underserved niches by scraping industry forums and news outlets for recurring pain points.
- Monitor regulatory changes and their potential impact on current business operations.

**Content & Thought Leadership**
- Generate data-backed blog posts and whitepapers based on the latest industry statistics.
- Curate weekly trend newsletters for internal stakeholders using automated web-sourced summaries.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Industry Trend Research Assistant" template.
2. Click "Import" to load the workflow into your workspace.
3. Configure your API credentials for Firecrawl and your preferred LLM provider.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Define the industry or trend topic you wish to research.
*   **Agent**: Processes the input and directs the research strategy.
*   **Composio Toolset**: Executes the Firecrawl web scraping and data retrieval tasks.
*   **Chat Output**: Delivers the synthesized research report and actionable insights.

### 3) Run the Flow
Use the Playground to test your research prompts:
- `Analyze the current trends in generative AI for enterprise software for Q3 2024.`
- `Scrape the latest news on sustainable supply chain logistics and summarize the top 5 emerging technologies.`
- `Compare the recent product announcements from major CRM providers and identify common strategic themes.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research lead, interpreting web data and synthesizing findings.
- Use a high-context model (e.g., GPT-4o or Claude 3.5 Sonnet) for better reasoning.
- Set the system prompt to prioritize objective analysis over speculative content.
- Configure the temperature to 0.3 to ensure factual accuracy in reports.

### 2) Composio Toolset Node
- Provide your Firecrawl API key to enable high-quality web data extraction.
- Define the connection scope to allow the agent to crawl specific domains or broad search queries.

### 3) Tool Availability
- **Firecrawl**: For full-page scraping, markdown conversion, and site crawling.
- **Search API**: For initial discovery of relevant URLs and industry news sources.
- **Data Parser**: For cleaning and structuring extracted web content.

---

## Related Solutions
- [Account Research Assistant by Zoominfo](../account-research-assistant-by-zoominfo/README.md) - Deep-dive intelligence on specific target accounts.
- [Account Intelligence Reporter by Leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting on account-level engagement and signals.
- [YouTube Competitor Intelligence Agent by YouTube](../you-tube-competitor-intelligence-agent-by-youtube/README.md) - Video-based competitive analysis and trend tracking.
