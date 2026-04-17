# Content Research Curator (Uplizd) - Automated trend discovery and knowledge synthesis

## Summary
The Content Research Curator is an intelligent Uplizd workflow designed to automate the discovery, aggregation, and synthesis of trending topics and industry insights. By leveraging the Composio Toolset to interface with live search and data platforms, this solution enables content creators and marketers to maintain a competitive edge, ensuring their editorial calendars are backed by real-time data rather than guesswork.

---

## Demo
![Content Research Curator workflow diagram showing automated search, data synthesis, and content output generation](image.png)
**Alt text (SEO-ready):** Content Research Curator Uplizd workflow, automated trend discovery, Composio search integration, and AI-powered content research pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c854eb38-09de-5412-a8b9-093d10db352e)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content strategy, research, trend analysis, composio, ai workflow, data synthesis, marketing automation
- This solution streamlines the research phase of content creation by connecting AI agents directly to live web intelligence tools.

---

## Who is this for?
This solution is built for professionals who need to turn vast amounts of web data into actionable content strategies.

- **Content Strategist**
    - Reduces time spent on manual topic research and competitive benchmarking.
- **Social Media Manager**
    - Identifies trending hashtags and viral topics to increase engagement.
- **SEO Specialist**
    - Gathers keyword-rich insights to inform long-form content production.
- **Digital Marketer**
    - Ensures brand messaging stays relevant by tracking industry-specific news cycles.

---

## Features
- **Automated Trend Discovery**
    - Uses real-time search tools to scan for high-performing topics and emerging industry trends.
- **Intelligent Synthesis**
    - The Agent node processes raw search results into structured, readable summaries for immediate use.
- **Composio Toolset Integration**
    - Seamlessly connects to search APIs to fetch verified, up-to-date information from the web.
- **Customizable Output Formats**
    - Configurable prompts allow the agent to draft outlines, blog posts, or social media captions.
- **Workflow Pipeline Velocity**
    - Reduces the research-to-drafting cycle from hours to minutes through automated data gathering.

---

## Use Cases
**Trend Monitoring**
- Automatically generate a weekly report on top-performing topics within a specific niche.
- Track competitor content releases to identify gaps in your own editorial calendar.

**Content Ideation**
- Brainstorm unique article angles based on current search volume and trending social discussions.
- Create data-backed content briefs that include relevant statistics and source links.

**Market Intelligence**
- Monitor industry news to provide timely updates for newsletters or LinkedIn thought leadership posts.
- Aggregate expert opinions on new product launches to inform your marketing positioning.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Research Curator template file into the builder.
3. Connect your preferred LLM and the Composio Toolset API keys in the settings panel.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your research topic or industry keyword.
- **Agent**: Processes the request and determines which search queries to execute.
- **Composio Toolset**: Executes live web searches and retrieves relevant data points.
- **Chat Output**: Delivers the synthesized research report or content draft to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Research the latest trends in generative AI for marketing and provide a 5-point summary.`
- `Find top-performing blog topics related to sustainable fashion for Q3.`
- `Identify 3 emerging challenges in remote team management based on recent industry articles.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research analyst, interpreting search results and synthesizing them into professional content.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system instruction to prioritize credible sources and data-backed insights.
- Configure the temperature to 0.3 for factual accuracy and concise reporting.

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure access to search and web-scraping tools.
- Ensure the connection scope includes `search_api` and `web_browser` permissions.

### 3) Tool Availability
- **Search Engine API**: For fetching real-time web results.
- **Web Scraper**: For extracting key text from identified industry articles.
- **Data Formatter**: For structuring research into Markdown or bulleted lists.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research into target accounts.
- [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) — Manages the distribution and SEO optimization of video content.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Aggregates business intelligence for sales and marketing teams.
