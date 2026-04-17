# News Sentiment Monitor (Uplizd) - Automated brand tracking and sentiment analysis

## Summary
The News Sentiment Monitor is an automated AI workflow that tracks brand mentions and analyzes public sentiment across news sites and blogs. By leveraging the BrowseAI integration, this solution provides real-time insights into media coverage, enabling PR and marketing teams to maintain brand reputation, identify trending topics, and respond to public perception shifts with high pipeline velocity.

---

## Demo
![News Sentiment Monitor workflow showing BrowseAI data extraction and AI sentiment analysis](image.png)
**Alt text (SEO-ready):** News Sentiment Monitor workflow using Uplizd, BrowseAI, and AI-driven sentiment analysis for brand reputation tracking and media monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a269ddc7-148a-542d-90d7-642a52a91f0a)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** news monitoring, sentiment analysis, browseai, brand reputation, pr automation, web scraping, media intelligence, ai workflow
- This solution bridges the gap between raw web data and actionable PR intelligence by automating the extraction and analysis of news sentiment.

---

## Who is this for?
This workflow is designed for professionals who need to stay ahead of the news cycle and protect brand equity.

- **PR Manager**
    - Monitor brand mentions across global news outlets to manage public relations crises in real-time.
- **Marketing Analyst**
    - Quantify sentiment trends over time to measure the effectiveness of brand campaigns and press releases.
- **Content Strategist**
    - Identify trending industry topics and competitor coverage to inform future content creation and distribution.
- **Brand Reputation Specialist**
    - Receive automated alerts on negative sentiment spikes to ensure proactive brand defense and stakeholder communication.

---

## Features
- **Automated Web Extraction**
    - Uses BrowseAI to scrape news sites and blogs, ensuring consistent data collection without manual effort.
- **AI-Powered Sentiment Scoring**
    - Analyzes text polarity to categorize mentions as positive, negative, or neutral for clear reporting.
- **Real-Time Alerting**
    - Triggers notifications based on sentiment thresholds, allowing for immediate response to critical media coverage.
- **Cross-Platform Aggregation**
    - Consolidates fragmented news data into a single source of truth for comprehensive media intelligence.
- **Customizable Monitoring Rules**
    - Allows users to define specific keywords, domains, and frequency settings to tailor the monitor to their brand needs.

---

## Use Cases
**Brand Reputation Management**
- Track negative sentiment spikes following product launches or corporate announcements.
- Monitor competitor brand mentions to identify market share shifts and public perception gaps.

**Media Intelligence & PR**
- Compile daily summaries of news coverage for executive stakeholders using automated sentiment reports.
- Identify top-performing news outlets that consistently provide positive coverage for your brand.

**Market Trend Analysis**
- Extract industry-specific keywords from news articles to spot emerging trends before they become mainstream.
- Analyze the impact of industry news on brand perception to adjust marketing messaging accordingly.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and project where the flow should be deployed.
3. Authenticate your BrowseAI account within the integration settings.
4. Ensure nodes are correctly mapped and the connection to your notification channel is active.

### 2) Setup the Nodes
- **Chat Input**: Define the brand name, keywords, and target news domains to monitor.
- **Agent**: Processes the scraped text, performs sentiment analysis, and summarizes key findings.
- **Composio Toolset**: Executes the BrowseAI scraping tasks and fetches fresh article content.
- **Chat Output**: Delivers the sentiment report and actionable insights to your dashboard or Slack/Email.

### 3) Run the Flow
Use the Playground to test your monitor with these prompts:
- `Monitor sentiment for "Uplizd" across major tech news sites this week.`
- `Analyze the latest blog mentions for our competitor and summarize the general tone.`
- `Identify any negative news coverage regarding our brand in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized media analyst.
- Use a model with strong summarization and classification capabilities.
- Instruction: "Act as a PR analyst. Extract sentiment from the provided news text, categorize as positive/negative/neutral, and highlight key themes."
- Instruction: "Maintain a professional tone and focus on actionable insights for the marketing team."

### 2) Composio Toolset Node
- Provide your BrowseAI API key to enable the agent to trigger scrapers.
- Ensure the connection scope includes read access to your defined scraping robots.

### 3) Tool Availability
- **BrowseAI Scraper**: Fetches live content from specified URLs.
- **Sentiment Analyzer**: Classifies text polarity.
- **Data Formatter**: Structures output for reporting tools.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automate account-level research and reporting.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze video content sentiment and audience engagement.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gather deep intelligence on target accounts and prospects.
