# Intelligent Stock Screener (Uplizd) - Automated market discovery and real-time financial data analysis

## Summary
The Intelligent Stock Screener by Finage is an automated AI workflow designed to streamline market research and asset discovery. By leveraging real-time financial data feeds, this solution enables investors and analysts to filter stocks based on custom criteria, monitor market volatility, and identify high-potential opportunities without manual spreadsheet management.

---

## Demo
![Intelligent Stock Screener workflow interface showing real-time market data filtering and AI-driven analysis](image.png)
**Alt text (SEO-ready):** Intelligent Stock Screener Uplizd workflow, automated financial data analysis, Finage API integration, real-time stock market filtering, AI-powered investment research.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b1e8b522-0371-5022-a620-fb4f38a8ebf3)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** finance, stock market, finage, data analysis, investment, market intelligence, composio, ai workflow
- This solution bridges the gap between raw financial data streams and actionable investment insights through intelligent automation.

---

## Who is this for?
This solution is designed for finance professionals and individual investors who need to process large volumes of market data efficiently.

- **Financial Analyst**
  - Automates the extraction and filtering of ticker data to focus on high-alpha opportunities.
- **Portfolio Manager**
  - Monitors specific asset classes and sector performance in real-time to maintain portfolio health.
- **Day Trader**
  - Rapidly identifies stocks meeting specific volatility and volume criteria during active trading hours.
- **Investment Researcher**
  - Aggregates historical and current market trends to support data-driven investment theses.

---

## Features
- **Real-time Data Integration**
  - Connects directly to Finage market feeds to ensure all screening criteria are evaluated against current price action.
- **Customizable Screening Logic**
  - Allows users to define complex filters including market cap, P/E ratios, and daily percentage changes.
- **AI-Driven Market Insights**
  - Uses an LLM to interpret filtered results and provide context on why specific stocks meet the defined criteria.
- **Automated Reporting**
  - Generates concise summaries of market movers, reducing the time spent manually scanning ticker lists.
- **Composio Toolset Connectivity**
  - Seamlessly bridges the AI agent with financial data APIs to execute queries and retrieve structured market information.

---

## Use Cases
**Market Opportunity Identification**
- Scanning for stocks hitting new 52-week highs with high relative volume.
- Identifying undervalued assets based on custom P/E and dividend yield thresholds.

**Portfolio Monitoring**
- Tracking daily performance of specific watchlists against broader market indices.
- Setting up alerts for significant price movements in tech or energy sectors.

**Data-Driven Research**
- Generating daily briefings on market volatility and sector-specific trends.
- Comparing historical performance metrics for a basket of stocks to support long-term investment strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Intelligent Stock Screener template from the marketplace.
3. Configure your Finage API credentials within the environment variables.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language screening criteria (e.g., "Find tech stocks under $50").
- **Agent**: Interprets the request and translates it into specific API calls for the Finage toolset.
- **Composio Toolset**: Executes the financial data retrieval and filtering logic.
- **Chat Output**: Delivers the formatted list of stocks and AI-generated market commentary.

### 3) Run the Flow
Use the Playground to test your screening logic:
- `Find all stocks in the S&P 500 with a P/E ratio under 15 and positive growth.`
- `Show me the top 5 most volatile stocks in the energy sector today.`
- `List stocks that have increased by more than 5% in the last hour.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial research assistant, translating user intent into structured data queries.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system instruction to prioritize accuracy and financial context.
- Ensure the agent is instructed to ask for clarification if screening criteria are ambiguous.

### 2) Composio Toolset Node
- Provide your Finage API key in the toolset configuration.
- Set the connection scope to allow read-only access to market data endpoints.

### 3) Tool Availability
- **Market Data Retrieval**: Fetching real-time quotes and historical price data.
- **Ticker Filtering**: Applying mathematical filters to large datasets.
- **Sector Analysis**: Categorizing and comparing stocks within specific industries.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate account-level data for sales and research.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research into company profiles and firmographics.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial data matching and reconciliation tasks.
