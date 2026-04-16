# Brand News Sentiment Tracker (Uplizd) - Automated real-time brand monitoring and sentiment analysis

## Summary
The Brand News Sentiment Tracker is an intelligent Uplizd workflow that automates the discovery and analysis of brand mentions across global news outlets. By leveraging ScrapeGraph AI and advanced LLMs, this solution transforms raw web data into actionable sentiment reports, enabling PR teams and brand managers to maintain brand hygiene, track public perception, and respond to market shifts with unprecedented pipeline velocity.

---

## Demo
![Brand News Sentiment Tracker dashboard showing real-time news mentions and sentiment scores](../image.png)
**Alt text (SEO-ready):** Brand News Sentiment Tracker dashboard showing real-time news mentions and sentiment scores for Uplizd AI workflow automation and media monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ab3e88cd-9862-54b6-8502-b6a77a900da0)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** brand monitoring, sentiment analysis, scrapegraph, news tracking, pr automation, media intelligence, ai workflow, data integration
- This solution bridges the gap between raw web-based news data and strategic marketing insights through automated sentiment processing.

---

## Who is this for?
This solution is designed for teams that need to maintain a pulse on their public reputation without manual research.

- **Brand Manager**
    - Automates daily reputation tracking to ensure brand consistency across news outlets.
- **PR Specialist**
    - Identifies negative sentiment spikes instantly to facilitate proactive crisis management.
- **Market Researcher**
    - Aggregates competitor news mentions to derive actionable intelligence for strategic planning.
- **Communications Director**
    - Provides a single source of truth for media coverage impact and overall brand health.

---

## Features
- **Automated News Scraping**
    - Utilizes ScrapeGraph AI to extract relevant brand mentions from diverse news sources in real-time.
- **Sentiment Scoring Engine**
    - Processes text data through an Agent node to categorize mentions as positive, negative, or neutral.
- **Centralized Reporting**
    - Consolidates fragmented news data into a structured format for easy review and internal distribution.
- **Real-Time Alerting**
    - Triggers notifications based on sentiment thresholds to ensure immediate awareness of critical brand news.
- **Composio Toolset Integration**
    - Seamlessly connects extracted insights with existing CRM or communication tools for streamlined team workflows.

---

## Use Cases
**Crisis Management & PR**
- Automatically flag negative news articles to the PR team within minutes of publication.
- Generate daily summaries of brand sentiment trends to prepare for stakeholder meetings.

**Competitor Intelligence**
- Monitor competitor press releases and news coverage to identify market positioning shifts.
- Compare your brand's sentiment scores against industry benchmarks to refine messaging.

**Brand Health Monitoring**
- Track the impact of new product launches on public perception across major news outlets.
- Maintain a historical archive of brand sentiment to evaluate long-term marketing campaign effectiveness.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Brand News Sentiment Tracker template file.
3. Authenticate your ScrapeGraph AI and relevant CRM/Notification tool connections.
4. Ensure nodes are correctly linked from the **Chat Input** to the **Agent**, through the **Composio Toolset**, and finally to the **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Defines the brand keywords and target news domains to monitor.
- **Agent**: Analyzes the scraped content for sentiment and contextual relevance.
- **Composio Toolset**: Executes the web scraping tasks and pushes data to external platforms.
- **Chat Output**: Delivers the final sentiment report and actionable alerts to your team.

### 3) Run the Flow
Open the Playground and test the workflow with the following prompts:
- `Monitor mentions for "Uplizd" in the last 24 hours and summarize the overall sentiment.`
- `Scrape news articles for "AI automation" and identify any negative sentiment trends.`
- `Generate a report on brand sentiment for our top 3 competitors based on today's news.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain, interpreting scraped text and determining sentiment polarity.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment classification.
- Set the system instruction to prioritize objective analysis over subjective interpretation.
- Configure the output format to JSON for consistent integration with downstream tools.

### 2) Composio Toolset Node
- Provide your ScrapeGraph AI API key to enable web extraction capabilities.
- Ensure the connection scope includes read access to news aggregators and search APIs.

### 3) Tool Availability
- **Web Scraper**: For fetching real-time news content.
- **Sentiment Analyzer**: For evaluating text polarity and emotion.
- **Notification Service**: For sending alerts to Slack, Email, or CRM platforms.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather deep account insights and news for sales teams.
- [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Analyze video engagement and audience sentiment.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the operational status of your automated business processes.
