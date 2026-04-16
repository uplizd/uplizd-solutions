# Brand Crisis Monitor (Uplizd) - Real-time brand sentiment tracking and PR threat detection

## Summary
The Brand Crisis Monitor is an intelligent Uplizd workflow that leverages Tavily’s search capabilities to perform continuous, real-time monitoring of brand mentions across the web. By analyzing sentiment and identifying spikes in negative coverage, this solution enables communications and marketing teams to proactively manage their brand reputation, mitigate PR risks, and maintain a consistent brand narrative before issues escalate.

---

## Demo
![Brand Crisis Monitor workflow dashboard showing real-time web search integration and sentiment analysis alerts](image.png)
**Alt text (SEO-ready):** Brand Crisis Monitor Uplizd workflow for real-time PR sentiment tracking, web search automation, and brand reputation management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2ZmZiI+PHBhdGggZD0iTTEyIDJMMiAxMnYxMGgyMFYxMkwxMiAyem0wIDE4bC04LThWNGg4djhINHY0bDgtOHY4eiIvPjwvc3ZnPg==)](https://uplizd.ai/solutions/55dcdb09-7bc4-5645-af1a-b73f2e18bdce)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** brand monitoring, pr, sentiment analysis, tavily, web search, crisis management, ai workflow, reputation management
- This solution integrates advanced search intelligence to transform raw web data into actionable PR insights and brand health alerts.

---

## Who is this for?
This workflow is designed for teams responsible for maintaining public trust and brand integrity in a fast-paced digital environment.

- **PR Manager**
    - Automates the early detection of negative press, allowing for rapid response and narrative control.
- **Social Media Lead**
    - Tracks brand sentiment across diverse platforms to identify emerging trends and community concerns.
- **Marketing Director**
    - Provides high-level visibility into brand health and campaign reception without manual daily audits.
- **Crisis Communications Specialist**
    - Receives real-time alerts on potential PR threats, enabling data-driven decision-making during critical events.

---

## Features
- **Real-time Web Intelligence**
    - Utilizes Tavily search to aggregate the latest mentions and news coverage across the global web.
- **Sentiment Analysis Engine**
    - Automatically categorizes brand mentions as positive, neutral, or negative to prioritize urgent issues.
- **Automated Alerting**
    - Triggers notifications when negative sentiment spikes exceed predefined thresholds for your brand.
- **Contextual Reporting**
    - Summarizes the "who, what, and where" of brand mentions to provide actionable context for PR teams.
- **Seamless Composio Integration**
    - Connects search results directly to your existing communication stack for instant team notification.

---

## Use Cases
**Proactive PR Management**
- Automatically scan news outlets for brand mentions following a major product launch or company announcement.
- Identify and catalog potential misinformation or negative narratives before they gain significant traction.

**Competitor & Market Benchmarking**
- Monitor competitor brand sentiment to identify market gaps or successful PR strategies to emulate.
- Track industry-wide sentiment shifts that may indirectly impact your brand’s perception.

**Crisis Mitigation**
- Configure custom triggers to alert the team immediately if negative sentiment exceeds a 20% threshold in a 24-hour window.
- Generate rapid-response summaries that include source links and sentiment context for executive review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Brand Crisis Monitor template from the solution library.
3. Connect your Tavily API key and preferred notification channels (e.g., Slack or Email).
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the brand name and monitoring parameters.
- **Agent**: Analyzes search results and performs sentiment classification.
- **Composio Toolset**: Executes real-time web searches and fetches relevant metadata.
- **Chat Output**: Delivers the final summary report and alerts to the user.

### 3) Run the Flow
Use the Playground to test the monitoring capabilities:
- `Monitor sentiment for "Uplizd" over the last 24 hours.`
- `Are there any negative news articles regarding "Uplizd" published today?`
- `Summarize the current public perception of "Uplizd" based on recent web search results.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a PR analyst, synthesizing search data into human-readable insights.
- Instruct the agent to prioritize negative sentiment detection.
- Define specific keywords or brand variations to track.
- Set the output format to include source URLs and sentiment scores.

### 2) Composio Toolset Node
- Provide your Tavily API key to enable high-quality, context-aware web searching.
- Set the connection scope to allow the agent to perform broad web queries and extract specific snippets.

### 3) Tool Availability
- **Web Search**: Real-time retrieval of news, blog posts, and social mentions.
- **Sentiment Analyzer**: Logic-based assessment of text polarity.
- **Notification Dispatcher**: Integration with email or messaging platforms for instant alerts.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Deep-dive research for B2B account enrichment.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automated reporting on account activity and lead signals.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracking operational efficiency and system status updates.
