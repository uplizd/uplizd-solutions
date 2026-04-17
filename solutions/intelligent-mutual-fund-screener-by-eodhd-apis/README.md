# Intelligent Mutual Fund Screener (Uplizd) - Automated financial data analysis and portfolio filtering

## Summary
The Intelligent Mutual Fund Screener is an AI-driven workflow that automates the extraction, filtering, and analysis of mutual fund performance data using the EODHD APIs. By leveraging the Composio Toolset, this solution enables financial analysts and investors to identify high-performing assets based on custom risk and return criteria, transforming raw market data into actionable investment intelligence with minimal manual effort.

---

## Demo
![Intelligent Mutual Fund Screener workflow interface showing EODHD API integration and data filtering nodes](image.png)
**Alt text (SEO-ready):** Intelligent Mutual Fund Screener workflow in Uplizd, featuring EODHD API data integration, automated financial analysis, and AI-driven portfolio filtering.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ae53b086-778f-5854-9b24-02d53774478a)

---

## Category
**Primary category:** Financial Operations
**Secondary tags:** mutual funds, eodhd, market data, investment analysis, financial automation, data integration, composio, ai workflow.
This solution streamlines the complex process of screening global mutual funds by connecting real-time market data APIs directly to an intelligent analysis engine.

---

## Who is this for?
This solution is designed for financial professionals and data-driven investors who need to scale their market research capabilities.

*   **Financial Analyst**
    *   Automate the screening of thousands of funds to identify those meeting specific alpha or volatility targets.
*   **Portfolio Manager**
    *   Maintain a real-time watch list of fund performance metrics to ensure alignment with client investment mandates.
*   **Investment Researcher**
    *   Rapidly extract and compare historical performance data across different asset classes and fund houses.
*   **FinTech Developer**
    *   Integrate structured financial data pipelines into internal dashboards using pre-built AI agent workflows.

---

## Features
- **Automated Data Extraction**
  Seamlessly pull comprehensive mutual fund datasets from EODHD APIs without writing custom integration code.
- **Customizable Screening Logic**
  Define complex filtering criteria—such as expense ratios, historical returns, and asset allocation—within the AI agent instructions.
- **Real-time Performance Analysis**
  Process live market data to generate immediate insights on fund health and comparative performance trends.
- **Composio Toolset Integration**
  Utilize the Composio framework to bridge the gap between the Uplizd agent and external financial data providers.
- **Scalable Pipeline Architecture**
  Deploy the workflow to handle bulk data requests, ensuring consistent data hygiene and reporting velocity.

---

## Use Cases
**Portfolio Optimization**
*   Filter mutual funds based on 5-year annualized returns and low expense ratios to improve long-term portfolio efficiency.
*   Compare fund performance against benchmark indices to identify underperforming assets for potential rebalancing.

**Market Research & Intelligence**
*   Generate weekly reports on top-performing funds within specific sectors like technology, healthcare, or ESG-focused assets.
*   Monitor fund house activity to detect shifts in asset allocation strategies across global markets.

**Risk Management**
*   Screen for funds with high Sharpe ratios to ensure investment choices align with risk-adjusted return requirements.
*   Identify funds with high volatility profiles to flag potential risks in a diversified client portfolio.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library.
2. Select the "Intelligent Mutual Fund Screener" and click "Import Flow."
3. Connect your EODHD API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives your specific screening criteria (e.g., "Find funds with >10% return").
*   **Agent**: Interprets the user request and formulates queries for the financial data provider.
*   **Composio Toolset**: Executes the API calls to EODHD to fetch the required mutual fund data.
*   **Chat Output**: Presents the filtered list of funds and analysis in a clear, readable format.

### 3) Run the Flow
Use the Playground to test your screening logic:
*   `"List the top 5 mutual funds with the lowest expense ratios in the technology sector."`
*   `"Analyze the performance of Vanguard funds over the last 3 years compared to the S&P 500."`
*   `"Find mutual funds with a 5-year return above 12% and a risk rating of low to medium."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial analyst assistant.
*   Adopt a professional, analytical tone focused on data accuracy.
*   Prioritize clear, tabular output for fund comparisons.
*   Always cite the data source (EODHD) when presenting performance metrics.

### 2) Composio Toolset Node
*   **API Key**: Provide your EODHD API key in the environment variables.
*   **Connection Scope**: Ensure the toolset has read-access to the mutual fund and historical data endpoints.

### 3) Tool Availability
*   `get_fund_performance`: Fetches historical return data for specific tickers.
*   `list_funds_by_criteria`: Filters funds based on user-defined parameters.
*   `compare_fund_metrics`: Aggregates and contrasts data points between multiple fund entities.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data for better financial prospecting.
*   [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial record matching and ledger cleanup.
*   [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational status of your automated data pipelines.
