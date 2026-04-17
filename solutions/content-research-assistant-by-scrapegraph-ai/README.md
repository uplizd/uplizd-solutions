# Content Research Assistant (Uplizd) - Automated web intelligence and content compilation

## Summary
The Content Research Assistant is an intelligent Uplizd workflow that automates the discovery, extraction, and synthesis of web-based information. By leveraging ScrapeGraph AI, this solution empowers content creators and researchers to transform raw URLs into structured, high-quality research briefs, significantly reducing manual data gathering time and ensuring a single source of truth for content strategy.

---

## Demo
![Content Research Assistant workflow interface showing URL input and automated research output](image.png)
**Alt text (SEO-ready):** Content Research Assistant Uplizd workflow, automated web scraping and content research automation using ScrapeGraph AI and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKAAABAAAB)](https://uplizd.ai/solutions/455990e9-a4d6-5cd4-a50f-74f6893aa879)

---

## Category
*   **Primary category:** Marketing operations
*   **Secondary tags:** content research, web scraping, scrapegraph-ai, automated writing, data synthesis, marketing automation, composio, ai workflow
*   This solution bridges the gap between raw web data and actionable content assets, streamlining the research phase for modern marketing teams.

---

## Who is this for?
This solution is designed for professionals who need to synthesize large volumes of web data into coherent narratives.

*   **Content Marketers**
    *   Accelerate the drafting process by having primary research and competitor data summarized instantly.
*   **SEO Specialists**
    *   Extract key insights and metadata from top-ranking pages to inform content optimization strategies.
*   **Market Researchers**
    *   Monitor industry trends and competitor updates across multiple domains without manual browsing.
*   **Technical Writers**
    *   Gather documentation and reference material from disparate web sources into a unified research document.

---

## Features
- **Automated Web Extraction**
  Utilizes ScrapeGraph AI to navigate and parse complex web pages, converting unstructured HTML into clean, readable text.
- **Multi-Source Synthesis**
  Aggregates data from multiple URLs simultaneously, allowing the agent to identify common themes and conflicting information.
- **Composio Toolset Integration**
  Seamlessly connects the research agent to your preferred data storage and document creation tools via the Composio ecosystem.
- **Structured Output Formatting**
  Configures the agent to deliver research in specific formats, such as executive summaries, bulleted lists, or markdown-ready drafts.
- **Real-Time Data Retrieval**
  Ensures content is based on the latest available web information, maintaining relevance in fast-moving industries.

---

## Use Cases
**Competitive Intelligence**
*   Extracting key value propositions from competitor landing pages for SWOT analysis.
*   Monitoring competitor blog updates to identify new content pillars and topic gaps.

**Content Strategy Development**
*   Compiling research briefs for upcoming whitepapers by scraping industry reports and news sites.
*   Generating summaries of long-form articles to repurpose into social media content or newsletters.

**Data-Driven Reporting**
*   Aggregating product feature lists from multiple vendor websites to create comparison tables.
*   Collecting customer feedback and review snippets from public forums to inform product development.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Research Assistant JSON template provided in the repository.
3. Connect your ScrapeGraph AI and relevant storage integrations within the settings panel.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your research topic and target URLs.
*   **Agent**: Processes the request, orchestrates the scraping logic, and synthesizes findings.
*   **Composio Toolset**: Executes the web extraction and manages data flow to external apps.
*   **Chat Output**: Displays the final research brief or saves it to your connected workspace.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
*   `"Research the latest trends in AI marketing from these 3 URLs: [URL1], [URL2], [URL3] and summarize the key takeaways."`
*   `"Compare the pricing models found on these competitor pages: [URL1], [URL2] and create a structured table."`
*   `"Extract the main arguments from this article [URL] and draft a 300-word response for a blog post."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets raw scraped data.
*   Set the system instruction to prioritize accuracy and source attribution.
*   Configure the model to output in Markdown for easy copy-pasting.
*   Ensure the "Temperature" is set to 0.3 for more factual, less creative output.

### 2) Composio Toolset Node
*   Provide your API key to enable secure access to the ScrapeGraph AI and web-crawling connectors.
*   Define the connection scope to allow the agent to read and parse external web content.

### 3) Tool Availability
*   **Web Scraper**: For deep-link extraction and content parsing.
*   **Search Connector**: For finding supplementary information if URLs are insufficient.
*   **Document Writer**: For exporting the final research summary to your preferred cloud drive.

---

## Related Solutions
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on specific business accounts and prospects.
*   [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze video content and audience sentiment for content strategy.
*   [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) — Refine and polish research-heavy content for professional publication.
