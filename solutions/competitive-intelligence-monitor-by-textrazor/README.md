# Competitive Intelligence Monitor (Uplizd) - Automated market tracking and competitor analysis

## Summary
The Competitive Intelligence Monitor is an automated Uplizd workflow designed to track competitor mentions, news, and market positioning in real-time. By leveraging the TextRazor API, this solution transforms unstructured web data into actionable insights, helping product and marketing teams maintain a competitive edge without manual research.

---

## Demo
![Competitive Intelligence Monitor dashboard showing real-time competitor mention tracking and sentiment analysis](../image.png)
**Alt text (SEO-ready):** Competitive Intelligence Monitor dashboard showing real-time competitor mention tracking, market sentiment analysis, and Uplizd workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a761e42f-11a9-5a0f-bea3-b2507f98b51a)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** competitive analysis, market research, textrazor, web scraping, data extraction, ai workflow, business intelligence
- This solution bridges the gap between raw web data and strategic decision-making by automating the collection and synthesis of competitor activity.

---

## Who is this for?
This workflow is designed for professionals who need to stay ahead of market shifts and competitor movements.

- **Product Manager**
    - Identify feature gaps and market trends by monitoring competitor product announcements.
- **Marketing Strategist**
    - Track brand sentiment and messaging shifts across the competitive landscape.
- **Sales Operations Lead**
    - Equip the sales team with up-to-date battle cards based on real-time competitive intelligence.
- **Business Analyst**
    - Aggregate disparate news sources into a single source of truth for quarterly market reporting.

---

## Features
- **Automated Web Monitoring**
    - Continuous scanning of target URLs and news feeds to capture competitor mentions as they happen.
- **Advanced NLP Processing**
    - Utilizes TextRazor to extract entities, topics, and sentiment from complex web content.
- **Structured Data Extraction**
    - Converts unstructured text into clean, actionable JSON formats ready for CRM or spreadsheet integration.
- **Real-time Alerting**
    - Triggers notifications or updates to your internal tools the moment significant competitor activity is detected.
- **Customizable Intelligence Filters**
    - Define specific keywords, industries, or competitor lists to ensure the agent focuses only on high-value data.

---

## Use Cases
**Market Positioning Analysis**
- Monitor competitor pricing changes and promotional campaigns across their official channels.
- Analyze press releases to identify strategic shifts in target demographics or product focus.

**Brand Sentiment Tracking**
- Aggregate customer reviews and forum mentions to compare brand perception against key rivals.
- Detect negative sentiment spikes early to proactively adjust marketing or support strategies.

**Sales Enablement**
- Automatically populate internal "Battle Cards" with the latest competitor feature launches.
- Generate weekly summaries of competitor activity to keep the sales team informed during prospect calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Library and search for "Competitive Intelligence Monitor".
2. Click "Import" to add the workflow to your workspace.
3. Connect your TextRazor API credentials and any destination CRM or notification channels.
4. Ensure nodes are correctly linked from the **Chat Input** to the **Agent** and finally to the **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target competitor URLs or search queries.
- **Agent**: Processes the raw text using the TextRazor toolset to extract key intelligence.
- **Composio Toolset**: Executes the extraction and data formatting tasks.
- **Chat Output**: Delivers the summarized report to your preferred communication channel.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Analyze the latest press releases from [Competitor Name] and summarize their new product focus.`
- `Extract all mentions of pricing changes from the provided competitor blog URL.`
- `Compare the sentiment of recent articles regarding [Competitor A] versus [Competitor B].`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting the structured data returned by the toolset.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment analysis.
- Set the system prompt to prioritize objective, data-driven summaries.
- Configure the temperature to 0.2 to ensure consistent, factual output.

### 2) Composio Toolset Node
- Provide your TextRazor API key within the Composio configuration panel.
- Ensure the connection scope includes read access to web content and entity extraction capabilities.

### 3) Tool Availability
- **TextRazor Entity Extraction**: Identifies key competitors, products, and organizations.
- **Sentiment Analysis Module**: Evaluates the tone of the extracted content.
- **Web Content Parser**: Cleans and normalizes HTML data for processing.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automate the gathering of account-level insights and firmographic data.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Streamline deep-dive research into target accounts and prospects.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Monitor and analyze competitor video content and audience engagement.
