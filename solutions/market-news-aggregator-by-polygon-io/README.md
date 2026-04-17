# Market News Aggregator (Uplizd) - Intelligent financial news curation and sentiment analysis

## Summary
The Market News Aggregator is an automated Uplizd AI workflow designed to streamline financial intelligence gathering. By leveraging real-time data from Polygon.io, the agent autonomously fetches, summarizes, and performs sentiment analysis on market-moving news, providing investors and analysts with a single source of truth to drive faster, data-backed decision-making.

---

## Demo
![Market News Aggregator dashboard showing real-time sentiment analysis and ticker-specific news feed](image.png)
**Alt text (SEO-ready):** Market News Aggregator dashboard showing real-time sentiment analysis and ticker-specific news feed, powered by Uplizd AI and Polygon.io financial data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7987bfa5-5721-5a24-924d-231e7931803b)

---

## Category
**Primary category:** Financial Operations  
**Secondary tags:** market intelligence, polygon.io, sentiment analysis, financial data, news aggregation, ai workflow, composio, real-time analytics  
This solution bridges the gap between raw financial data streams and actionable market insights through automated AI processing.

---

## Who is this for?
This solution is designed for financial professionals who need to filter noise from market signals.

*   **Investment Analyst**
    *   Automates the daily grind of scanning multiple news sources for sentiment shifts on key tickers.
*   **Portfolio Manager**
    *   Receives summarized impact assessments to quickly evaluate the relevance of breaking news to current holdings.
*   **Day Trader**
    *   Gains a competitive edge by identifying market-moving headlines seconds after they hit the wire.
*   **Financial Researcher**
    *   Maintains a clean, historical log of news sentiment trends for backtesting and long-term strategy development.

---

## Features
- **Real-time News Ingestion**
  Connects directly to Polygon.io to pull the latest financial headlines as they are published.
- **Sentiment Analysis Engine**
  Uses advanced LLM reasoning to categorize news as bullish, bearish, or neutral based on market context.
- **Automated Summarization**
  Condenses long-form financial reports and news articles into concise, high-impact bullet points.
- **Composio-Powered Integration**
  Seamlessly bridges the gap between raw data providers and your preferred notification or CRM channels.
- **Ticker-Specific Filtering**
  Allows users to focus the agent on specific assets, sectors, or market indices for highly relevant output.

---

## Use Cases
**Market Sentiment Monitoring**
*   Tracking real-time sentiment shifts for high-volatility tech stocks during earnings season.
*   Aggregating news sentiment across an entire portfolio to gauge overall market exposure.

**Automated Research Briefings**
*   Generating a daily morning briefing document that summarizes the top 5 market-moving stories.
*   Extracting key financial metrics and forward-looking statements from press releases.

**Alerting and Triage**
*   Triggering instant notifications when a "Strong Buy" or "Strong Sell" sentiment is detected for a tracked ticker.
*   Filtering out non-impactful noise to ensure only significant regulatory or economic news reaches the analyst.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select 'Create New Flow'.
2. Import the Market News Aggregator template from the community library.
3. Connect your Polygon.io API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the ticker symbol or market sector query from the user.
*   **Agent**: Orchestrates the logic, interpreting the user's intent and invoking the correct data tools.
*   **Composio Toolset**: Executes the API calls to Polygon.io to fetch and parse financial news data.
*   **Chat Output**: Delivers the summarized news and sentiment analysis back to the user interface.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
* `Analyze the latest market sentiment for AAPL and summarize the top 3 news stories.`
* `Fetch the most recent financial news for the semiconductor sector and identify any bearish signals.`
* `Provide a sentiment summary for TSLA based on news from the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial analyst assistant. 
*   Prioritize factual accuracy over creative interpretation.
*   Maintain a professional, objective tone in all summaries.
*   Always cite the source or timestamp of the news when possible.

### 2) Composio Toolset Node
Requires a valid Polygon.io API key. Ensure the connection scope includes `read` access to market news and ticker data endpoints.

### 3) Tool Availability
*   `polygon_news_fetcher`: Retrieves raw headline and article data.
*   `sentiment_analyzer`: Processes text to determine market impact.
*   `data_formatter`: Structures the output for clear, readable presentation.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich your CRM with deep account and contact insights.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate the discovery of key company data and relationship maps.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Leverage ZoomInfo data to power your sales research workflows.
