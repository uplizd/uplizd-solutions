# Market Intelligence Analyst (Uplizd) - Real-time financial data insights and competitive research

## Summary
The Market Intelligence Analyst is a powerful Uplizd AI workflow designed to automate the collection and synthesis of financial market data using the Polygon.io API. By streamlining the retrieval of stock performance, historical trends, and competitive benchmarks, this solution provides financial analysts and researchers with a single source of truth, significantly reducing manual data gathering time and increasing the velocity of investment decision-making.

---

## Demo
![Market Intelligence Analyst workflow interface showing Polygon.io data integration and AI-driven financial reporting](image.png)
**Alt text (SEO-ready):** Market Intelligence Analyst Uplizd workflow, Polygon.io financial data integration, automated stock market research, and competitive intelligence reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9d8b8473-6776-5b3f-887a-044e0c828529)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** market intelligence, polygon.io, financial data, investment research, ai workflow, data analysis, composio, stock market
- This solution bridges the gap between raw financial market feeds and actionable investment insights through intelligent automation.

---

## Who is this for?
This workflow is designed for professionals who need to synthesize complex market data into clear, actionable intelligence.

- **Financial Analyst**
  - Automates the retrieval of historical stock data and performance metrics to support investment theses.
- **Investment Researcher**
  - Quickly aggregates competitive intelligence across multiple tickers to identify market trends and anomalies.
- **Portfolio Manager**
  - Monitors real-time market movements and asset performance to ensure alignment with portfolio strategy.
- **Growth Strategist**
  - Leverages market data signals to identify potential opportunities for capital allocation or risk mitigation.

---

## Features
- **Real-time Market Data Retrieval**
  - Connects directly to Polygon.io to pull live stock quotes, historical price action, and market volume data.
- **Automated Competitive Benchmarking**
  - Allows the agent to compare performance metrics across a basket of competitors within the same sector.
- **Intelligent Financial Summarization**
  - Uses advanced LLM reasoning to distill complex technical data into concise, executive-level summaries.
- **Composio Toolset Integration**
  - Seamlessly manages API authentication and request formatting through the Composio Toolset for reliable data fetching.
- **Customizable Reporting Logic**
  - Enables users to define specific time windows and data points, ensuring the output matches unique research requirements.

---

## Use Cases
**Competitive Market Analysis**
- Compare the quarterly performance of specific tech stocks against industry averages.
- Identify price volatility patterns for a target company over the last 12 months.

**Investment Opportunity Screening**
- Scan for stocks meeting specific volume and price growth criteria during market hours.
- Generate a summary of recent market sentiment based on price action and historical trends.

**Portfolio Performance Monitoring**
- Pull daily closing data for a curated list of assets to track portfolio health.
- Automate the generation of weekly market trend reports for internal stakeholder review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the Market Intelligence Analyst workflow to your workspace.
3. Connect your Polygon.io API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your research query or ticker symbols.
*   **Agent**: Processes the request and determines which financial data points to fetch.
*   **Composio Toolset**: Executes the API calls to Polygon.io to retrieve accurate market data.
*   **Chat Output**: Delivers the synthesized financial report and actionable insights.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Analyze the performance of AAPL and MSFT over the last 6 months and highlight key differences.`
- `What is the current market volume and price trend for TSLA compared to its 50-day moving average?`
- `Provide a summary of the top 3 performing stocks in the semiconductor sector for the current quarter.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial research assistant, prioritizing accuracy and clarity.
- Instruction: Act as a senior financial analyst providing objective, data-backed insights.
- Instruction: Always cite the specific time frames and data sources used in your analysis.
- Instruction: If data is unavailable for a specific ticker, clearly state the limitation rather than hallucinating values.

### 2) Composio Toolset Node
- API Key: Ensure your Polygon.io API key is active within your Composio account.
- Connection Scope: Grant the toolset read-only access to market data endpoints to ensure secure operations.

### 3) Tool Availability
- `get_stock_quote`: Fetches real-time pricing for specific tickers.
- `get_historical_data`: Retrieves time-series data for trend analysis.
- `get_market_status`: Verifies if the exchange is currently open or closed.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and identify key business signals.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on target accounts and prospects.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate comprehensive reports on account engagement and intent.
