# Investment Research Analyst (Uplizd) - Automated Financial Data Synthesis and Market Intelligence

## Summary
The Investment Research Analyst workflow automates the collection and synthesis of complex financial data, providing investors and analysts with a single source of truth for stock performance, analyst consensus, and dividend insights. By leveraging the Composio Toolset to query real-time financial APIs, this agent eliminates manual data gathering, significantly increasing research velocity and ensuring decision-makers have access to accurate, up-to-date market intelligence.

---

## Demo
![Investment Research Analyst workflow dashboard showing stock data extraction and analyst consensus reporting](image.png)
**Alt text (SEO-ready):** Investment Research Analyst Uplizd workflow showing automated stock analysis, financial data retrieval, and market intelligence reporting via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d937c2c5-8dc6-5458-b84e-b31991549c84)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** finance, stock analysis, market intelligence, data retrieval, investment research, composio, ai workflow, financial reporting
- This solution bridges the gap between raw financial data streams and actionable investment insights for modern research teams.

---

## Who is this for?
This solution is designed for financial professionals and research teams who need to synthesize large volumes of market data into clear, actionable reports.

- **Equity Research Analyst**
    - Automates the aggregation of consensus estimates and dividend history across multiple tickers.
- **Portfolio Manager**
    - Provides real-time updates on asset performance to support rapid rebalancing decisions.
- **Financial Advisor**
    - Generates concise, data-backed summaries for client investment reviews and portfolio updates.
- **Investment Operations Associate**
    - Ensures data hygiene and consistency by pulling verified financial metrics directly from source APIs.

---

## Features
- **Automated Market Data Retrieval**
  Connects to financial data providers via Composio to fetch real-time stock quotes and historical performance metrics.
- **Analyst Consensus Aggregation**
  Synthesizes buy, sell, and hold ratings from major financial institutions into a unified sentiment score.
- **Dividend Insight Engine**
  Tracks dividend yield, payout ratios, and upcoming ex-dividend dates to inform income-focused investment strategies.
- **Customizable Research Reports**
  Transforms complex technical data into plain-language summaries tailored for specific investment mandates.
- **Real-time Alerting**
  Monitors specific ticker symbols for significant price movements or changes in analyst outlooks.

---

## Use Cases
**Portfolio Monitoring**
- Tracking daily performance fluctuations across a diversified equity portfolio.
- Identifying stocks approaching key support or resistance levels based on historical data.

**Investment Due Diligence**
- Comparing dividend sustainability metrics across multiple competitors in the same sector.
- Aggregating historical earnings surprise data to evaluate management performance.

**Client Reporting**
- Generating automated "Market Snapshot" documents for quarterly client performance reviews.
- Summarizing recent analyst sentiment shifts to justify portfolio allocation changes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Investment Research Analyst template from the marketplace.
3. Connect your preferred financial data API keys within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the ticker symbol or research query from the user.
- **Agent**: Processes the request, determines the necessary financial metrics, and orchestrates tool calls.
- **Composio Toolset**: Executes secure API calls to retrieve real-time market data and analyst consensus.
- **Chat Output**: Delivers the synthesized research report back to the user interface.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Analyze the current analyst consensus and dividend yield for AAPL.`
- `Compare the recent financial performance of TSLA against its primary sector competitors.`
- `Provide a summary of the latest market sentiment and price trends for MSFT.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial research assistant, prioritizing accuracy and objective data synthesis.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for complex financial calculations.
- Instruct the agent to cite data sources clearly in all generated reports.
- Configure the system prompt to maintain a professional, analytical tone suitable for investment documentation.

### 2) Composio Toolset Node
- Provide your API keys for the selected financial data providers (e.g., Yahoo Finance, Alpha Vantage).
- Set the connection scope to "Read-Only" to ensure data integrity during the research process.

### 3) Tool Availability
- **Market Data Fetcher**: Real-time price, volume, and volatility metrics.
- **Analyst Consensus Tool**: Aggregated rating data and price targets.
- **Dividend Tracker**: Historical payout data and yield calculations.
- **News Sentiment Analyzer**: Summarizes recent headlines affecting ticker performance.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive intelligence gathering for corporate accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automated reporting for lead and account insights.
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) — Research-focused data aggregation and impact analysis.
