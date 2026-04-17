# Market News Intelligence Agent (Uplizd) - Real-time market news analysis with sentiment and impact scoring

## Summary
The Market News Intelligence Agent is an automated Uplizd workflow designed to monitor, ingest, and analyze global financial news in real-time. By leveraging the Polygon.io API via the Composio Toolset, this solution transforms raw news feeds into actionable intelligence, providing sentiment analysis and impact scoring to help analysts and traders maintain a competitive edge in fast-moving markets.

---

## Demo
![Market News Intelligence Agent dashboard showing real-time news sentiment analysis and impact scoring](image.png)
**Alt text (SEO-ready):** Market News Intelligence Agent dashboard showing real-time news sentiment analysis, financial data integration, and impact scoring on the Uplizd workflow platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/382f35a9-a463-57d3-aa4b-9903919a2ee0)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** polygon, news analysis, sentiment, financial data, real-time, market trends, composio, ai workflow
- This solution bridges the gap between raw financial news feeds and strategic decision-making through automated AI-driven sentiment analysis.

---

## Who is this for?
This solution is designed for financial professionals and market researchers who need to synthesize vast amounts of news data into clear, actionable insights.

- **Financial Analyst**
    - Rapidly identify market-moving events without manual news scanning.
- **Portfolio Manager**
    - Assess the potential impact of global news on specific asset classes or holdings.
- **Day Trader**
    - Receive real-time sentiment signals to inform high-frequency trading decisions.
- **Market Researcher**
    - Aggregate historical news sentiment to build comprehensive trend reports.

---

## Features
- **Real-time News Ingestion**
    - Connects directly to live market feeds to ensure the agent is always processing the latest headlines.
- **Sentiment Scoring Engine**
    - Automatically categorizes news as bullish, bearish, or neutral using advanced LLM reasoning.
- **Impact Assessment**
    - Evaluates the potential volatility or market influence of specific news items based on historical patterns.
- **Composio Toolset Integration**
    - Seamlessly bridges the Uplizd agent with Polygon.io for high-fidelity market data retrieval.
- **Automated Alerting**
    - Configurable output triggers that notify users when high-impact or high-sentiment news is detected.

---

## Use Cases
**Market Sentiment Tracking**
- Monitor sector-wide sentiment shifts during earnings season.
- Track the impact of geopolitical headlines on specific currency pairs.

**Portfolio Risk Management**
- Identify news-driven risks to specific equity positions in real-time.
- Automate the flagging of news items that contradict current portfolio strategy.

**Competitive Intelligence**
- Track news sentiment regarding key competitors to anticipate market moves.
- Aggregate daily news summaries for specific industries to identify emerging trends.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace and project destination.
3. Configure your API credentials for the Polygon.io integration.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your specific market queries or ticker symbols.
- **Agent**: Processes news data, performs sentiment analysis, and calculates impact scores.
- **Composio Toolset**: Executes secure API calls to fetch real-time news from Polygon.io.
- **Chat Output**: Delivers the summarized intelligence and sentiment report to your dashboard.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze the latest market sentiment for NVDA and provide an impact score.`
- `What are the top 3 news stories impacting the tech sector today?`
- `Summarize the sentiment of recent news regarding global oil prices.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a financial analyst, synthesizing news data into structured insights.
- Instruct the agent to prioritize recent data over historical context.
- Use a neutral, professional tone for all sentiment summaries.
- Ensure the agent explicitly cites the news source for every impact score provided.

### 2) Composio Toolset Node
- Provide your Polygon.io API key within the Composio configuration panel.
- Set the connection scope to allow read-only access to news and ticker data.

### 3) Tool Availability
- `polygon_get_news`: Fetches the latest articles for specific tickers or sectors.
- `polygon_get_market_status`: Verifies if the market is open to contextualize news impact.
- `polygon_get_ticker_details`: Retrieves background information on entities mentioned in news.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md): Aggregate account-level data for deeper sales insights.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md): Analyze video content to track competitor market positioning.
- [Account Research Agent](../account-research-agent-by-onepage/README.md): Automate the gathering of deep research on target accounts.
