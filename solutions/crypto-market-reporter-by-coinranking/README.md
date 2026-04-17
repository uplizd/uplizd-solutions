# Crypto Market Reporter (Uplizd) - Automated cryptocurrency market intelligence and trend analysis

## Summary
The Crypto Market Reporter is an automated Uplizd AI workflow that aggregates real-time cryptocurrency data to provide actionable market insights and daily summaries. By leveraging the Coinranking API, this solution helps traders, analysts, and investors maintain pipeline velocity and data hygiene, ensuring they stay informed on price movements and market trends without manual tracking.

---

## Demo
![Crypto Market Reporter dashboard showing real-time price trends and automated AI-generated market summaries](image.png)
**Alt text (SEO-ready):** Crypto Market Reporter dashboard showing real-time price trends and automated AI-generated market summaries for Uplizd data integration workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3f10e946-1175-5bf7-989d-ef0e66ca3902)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** crypto, market intelligence, coinranking, data sync, financial analysis, ai workflow, composio, market trends
- This solution bridges the gap between raw blockchain market data and human-readable insights through automated AI processing.

---

## Who is this for?
This workflow is designed for professionals who need to monitor volatile digital asset markets with precision and speed.

- **Crypto Traders**
    - Receive instant alerts on significant price fluctuations and volume spikes.
- **Financial Analysts**
    - Generate automated daily reports on asset performance for client portfolios.
- **Market Researchers**
    - Track historical trends and comparative data across multiple digital assets.
- **DeFi Developers**
    - Monitor market health indicators to inform project development and integration strategies.

---

## Features
- **Real-time Data Aggregation**
    - Fetches live market data from Coinranking to ensure the agent always has the most current pricing information.
- **AI-Powered Summarization**
    - Translates complex numerical data into concise, human-readable market summaries and trend reports.
- **Automated Alerting**
    - Configures trigger-based notifications for specific asset movements or threshold breaches.
- **Composio Toolset Integration**
    - Seamlessly connects the Uplizd agent to external data APIs for expanded analytical capabilities.
- **Customizable Reporting**
    - Allows users to define the frequency and depth of market reports based on specific asset lists.

---

## Use Cases
**Market Monitoring**
- Track top-performing assets over a 24-hour window to identify breakout trends.
- Monitor specific altcoin price volatility to adjust trading strategies in real-time.

**Portfolio Reporting**
- Generate end-of-day summaries for a curated watchlist of digital assets.
- Compare current market performance against historical benchmarks for specific tokens.

**Data Hygiene & Sync**
- Ensure all internal tracking sheets are updated with accurate, verified market prices.
- Sync market intelligence data directly into CRM or project management tools for team visibility.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your Coinranking API credentials within the connection settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries or scheduled triggers for market data.
- **Agent**: Processes market data and generates natural language insights.
- **Composio Toolset**: Executes API calls to fetch real-time crypto market statistics.
- **Chat Output**: Delivers the final formatted report or alert to the user.

### 3) Run the Flow
Use the Playground to test your agent with these example prompts:
- `Summarize the top 5 gainers in the crypto market over the last 24 hours.`
- `What is the current market sentiment and price trend for Bitcoin and Ethereum?`
- `Create a daily market report for my watchlist: BTC, ETH, SOL, and ADA.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial analyst, synthesizing raw data into strategic insights.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate financial interpretation.
- Set the system instruction to prioritize objective data analysis over speculative advice.
- Configure the temperature to 0.2 to ensure consistent, fact-based reporting.

### 2) Composio Toolset Node
- Provide your Coinranking API key to enable secure data retrieval.
- Set the connection scope to read-only access for market data endpoints.

### 3) Tool Availability
- **Market Data Fetcher**: Retrieves real-time price, volume, and market cap.
- **Trend Analyzer**: Calculates percentage changes over defined time intervals.
- **Watchlist Manager**: Filters data based on user-defined asset lists.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated business intelligence and lead reporting.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research and data gathering for target accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Real-time monitoring of automated pipeline and workflow performance.
