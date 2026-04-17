# Content Research Assistant (Uplizd) - Automate market intelligence and competitor content analysis

## Summary
The Content Research Assistant is an AI-powered workflow designed to streamline the gathering of trending topics and competitor insights. By leveraging the Apify integration, this solution enables marketing and research teams to transform raw web data into actionable content strategies, ensuring your brand stays ahead of industry trends with minimal manual effort.

---

## Demo
![Content Research Assistant workflow showing Apify data extraction and AI analysis](image.png)
**Alt text (SEO-ready):** Content Research Assistant (Uplizd) workflow for automated web scraping, competitor content analysis, and market intelligence gathering using Apify and AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge.svg)](https://uplizd.ai/solutions/0dbb7620-1e42-59fd-8eea-a2202a8c1c71)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content research, apify, web scraping, market intelligence, competitive analysis, ai workflow, data extraction, trend monitoring
- This solution bridges the gap between raw web data and strategic content planning by automating the research lifecycle.

---

## Who is this for?
This assistant is built for professionals who need to maintain a constant pulse on market dynamics without the overhead of manual research.

- **Content Marketers**
    - Quickly identify high-performing topics and content gaps to inform editorial calendars.
- **SEO Specialists**
    - Monitor competitor backlink profiles and keyword ranking shifts in real-time.
- **Market Researchers**
    - Aggregate large-scale industry data into summarized reports for stakeholder review.
- **Growth Managers**
    - Track competitor product launches and messaging pivots to refine positioning strategies.

---

## Features
- **Automated Web Scraping**
  Utilizes the Apify platform to extract structured data from target websites and search engines.
- **Intelligent Content Summarization**
  Processes raw scraped text through LLMs to distill complex articles into key takeaways.
- **Competitor Trend Tracking**
  Identifies recurring themes and sentiment shifts across competitor content channels.
- **Real-time Data Integration**
  Seamlessly pipes research findings into your existing documentation or project management tools.
- **Customizable Research Parameters**
  Allows users to define specific domains, keywords, and frequency for automated data collection.

---

## Use Cases
**Competitor Content Monitoring**
- Track daily updates on competitor blogs to identify new product announcements.
- Analyze competitor social media engagement to spot trending industry narratives.

**SEO & Keyword Discovery**
- Scrape search result pages to identify content gaps for high-volume keywords.
- Monitor competitor meta-descriptions and headers to refine your own on-page strategy.

**Market Trend Reporting**
- Aggregate industry news from multiple sources into a weekly executive summary.
- Detect emerging industry buzzwords to keep your brand voice relevant and authoritative.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Content Research Assistant.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Apify API key and preferred LLM provider in the integration settings.
4. Ensure nodes are correctly mapped and the workflow is toggled to "Active."

### 2) Setup the Nodes
- **Chat Input**: Define the research topic, target domains, or specific competitor URLs.
- **Agent**: Analyzes the input and orchestrates the Apify scraping tasks.
- **Composio Toolset**: Executes the web extraction and data retrieval operations.
- **Chat Output**: Delivers the synthesized research report or content brief.

### 3) Run the Flow
Open the Playground and test the assistant with these prompts:
- `Research the top 5 trending topics in AI marketing for this week based on recent blog posts.`
- `Scrape the latest articles from [Competitor URL] and summarize their core messaging strategy.`
- `Identify common content themes across these three industry news sites: [Site 1], [Site 2], [Site 3].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research analyst, prioritizing accuracy and synthesis.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to cite sources for every claim made in the summary.
- Configure the system prompt to filter out noise and focus on high-intent content.

### 2) Composio Toolset Node
- Provide a valid Apify API key to enable web scraping capabilities.
- Set the connection scope to allow the agent to read and parse public web content.

### 3) Tool Availability
- **Apify Scraper**: For targeted extraction of web pages and search results.
- **Search API**: For broad discovery of trending industry topics.
- **Data Parser**: For converting unstructured HTML/Text into clean JSON/Markdown.

---

## Related Solutions
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze video performance and viewer sentiment.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gather deep intelligence on target B2B accounts.
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) — Monitor research trends and citation metrics.
