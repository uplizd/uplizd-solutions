# Content Research Assistant (Uplizd) - Automated web intelligence and trend analysis

## Summary
The Content Research Assistant is an automated Uplizd AI workflow designed to streamline the gathering of web-based insights, competitive trends, and industry data. By leveraging the ZenRows integration, this solution empowers marketing and research teams to eliminate manual scraping, ensuring a consistent, high-quality stream of data for content strategy, market analysis, and audience intelligence.

---

## Demo
![Content Research Assistant workflow showing automated web data extraction and analysis](image.png)
**Alt text (SEO-ready):** Content Research Assistant (Uplizd) workflow for automated web data extraction, competitive trend analysis, and market intelligence using ZenRows and AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/97090146-5be9-5b5a-b462-5763f6f2a97b)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content research, web scraping, zenrows, competitive intelligence, trend analysis, market research, data automation, ai workflow
- This solution bridges the gap between raw web data and actionable content strategy by automating the retrieval and synthesis of online information.

---

## Who is this for?
This solution is designed for professionals who need to maintain a competitive edge through data-driven content.

- **Content Strategists**
    - Automate the collection of competitor blog topics and trending keywords to inform editorial calendars.
- **Market Researchers**
    - Extract real-time industry data and sentiment from diverse web sources without manual browsing.
- **SEO Specialists**
    - Monitor search landscape changes and competitor backlink profiles to refine optimization tactics.
- **Growth Marketers**
    - Identify emerging market opportunities by tracking product mentions and feature updates across the web.

---

## Features
- **Automated Web Extraction**
    - Uses the ZenRows toolset to bypass anti-bot measures and retrieve clean, structured data from any URL.
- **Intelligent Summarization**
    - The Agent node processes raw HTML or text into concise, actionable insights tailored to your specific research goals.
- **Real-Time Trend Tracking**
    - Configure the workflow to monitor specific domains or search queries, providing updates on industry shifts as they happen.
- **Seamless Integration**
    - Connects directly with your existing marketing stack via the Composio Toolset to push findings into CRM or project management tools.
- **Customizable Research Parameters**
    - Define specific extraction logic to filter out noise and focus only on the metrics or content types that matter to your business.

---

## Use Cases
**Competitive Intelligence**
- Monitor competitor product launches and pricing updates by scraping their dedicated landing pages.
- Analyze competitor content frequency and topic coverage to identify gaps in your own strategy.

**Market Trend Analysis**
- Aggregate industry news and expert commentary from multiple sources to create weekly market intelligence reports.
- Track sentiment and public perception of specific industry technologies across forums and news outlets.

**Content Strategy Optimization**
- Research high-performing content formats and headlines within your niche to guide your creative direction.
- Automatically compile lists of relevant influencers or expert sources for upcoming content collaborations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the workflow in your builder.
3. Connect your ZenRows API key within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your research topic, target URLs, or specific questions.
- **Agent**: Analyzes the request and determines the necessary web scraping or search actions.
- **Composio Toolset**: Executes the ZenRows connection to fetch data from the target web sources.
- **Chat Output**: Delivers the synthesized research report or data summary back to the user.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Research the latest trends in AI-driven marketing for Q3 and summarize the top 5 findings.`
- `Scrape the following URL: [insert URL] and extract the main value propositions mentioned.`
- `Find recent articles about sustainable tech and list the key industry challenges identified.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your research analyst, interpreting raw data into human-readable reports.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on the desired output format (e.g., Markdown tables, bulleted lists).
- Set the temperature to a lower value (0.2–0.3) for more factual, data-oriented responses.

### 2) Composio Toolset Node
- Ensure your ZenRows API key is active and authorized within the Composio dashboard.
- Set the connection scope to allow the agent to perform GET requests on the target domains.

### 3) Tool Availability
- **Web Scraper**: For deep extraction of page content.
- **Search Engine API**: For finding relevant URLs based on keywords.
- **Data Parser**: For cleaning and structuring unstructured HTML content.

---

## Related Solutions
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) - Analyze video engagement and audience demographics.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Gather intelligence on specific business accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed reports on account activity and intent.
