# Dividend Income Tracker (Uplizd) - Automated portfolio dividend monitoring and income forecasting

## Summary
The Dividend Income Tracker is an intelligent Uplizd workflow that automates the monitoring of stock portfolios and dividend payout schedules. By integrating real-time financial data via the Polygon.io API, this solution provides investors and financial analysts with a single source of truth for upcoming dividend payments, yield calculations, and historical income tracking, significantly reducing manual spreadsheet maintenance and improving investment pipeline velocity.

---

## Demo
![Dividend Income Tracker dashboard showing portfolio yield and upcoming payout schedule](image.png)
**Alt text (SEO-ready):** Dividend Income Tracker Uplizd workflow dashboard showing portfolio yield, stock market data integration, and automated dividend payout forecasting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b326e00e-5a2a-5878-884d-caab92334e54)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** `dividend`, `portfolio`, `polygon`, `investing`, `data sync`, `finance`, `composio`, `ai workflow`
- This solution bridges the gap between raw market data and actionable financial insights, streamlining dividend management for modern investors.

---

## Who is this for?
This solution is designed for financial professionals and individual investors who require automated oversight of their income-generating assets.

- **Portfolio Manager**
    - Automates the tracking of dividend yields across diverse asset classes to ensure portfolio targets are met.
- **Financial Analyst**
    - Eliminates manual data entry by pulling real-time payout schedules directly into reporting workflows.
- **Individual Investor**
    - Provides proactive alerts for upcoming dividend payments, allowing for better reinvestment planning.
- **Wealth Advisor**
    - Delivers consistent, data-backed income forecasts to clients without the overhead of legacy spreadsheet management.

---

## Features
- **Real-time Market Data**
    - Leverages the Polygon.io API to fetch live stock prices and dividend payout information instantly.
- **Automated Income Forecasting**
    - Calculates projected dividend income based on current holdings and historical payout trends.
- **Composio Toolset Integration**
    - Seamlessly connects the Uplizd agent to financial data providers for secure and authenticated data retrieval.
- **Customizable Alerting**
    - Configures automated notifications for upcoming ex-dividend dates and payment distributions.
- **Historical Performance Tracking**
    - Maintains a clean audit trail of past dividend receipts to analyze long-term portfolio growth.

---

## Use Cases
**Portfolio Optimization**
- Automatically identify underperforming assets based on current dividend yield vs. market benchmarks.
- Rebalance holdings by analyzing the impact of dividend reinvestment on total portfolio growth.

**Income Forecasting**
- Generate monthly or quarterly income projections to assist in cash flow planning for retirement or reinvestment.
- Track upcoming ex-dividend dates to ensure timely execution of buy/sell strategies.

**Data Hygiene & Reporting**
- Sync dividend data into centralized dashboards to eliminate discrepancies between brokerage statements.
- Automate the generation of tax-ready dividend income reports for annual financial reviews.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Dividend Income Tracker template via the provided solution URL.
3. Connect your Polygon.io API credentials to the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your portfolio ticker symbols or specific query requests.
- **Agent**: Analyzes the request and determines the necessary financial data to retrieve.
- **Composio Toolset**: Executes the API calls to Polygon to fetch dividend and stock data.
- **Chat Output**: Returns a formatted summary of dividend yields, payout dates, and income forecasts.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `What is the projected dividend income for my current portfolio over the next quarter?`
- `List all upcoming ex-dividend dates for the stocks in my portfolio.`
- `Compare the dividend yield of my current holdings against the S&P 500 average.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial assistant capable of interpreting market data and summarizing complex investment metrics.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Act as a financial analyst. Retrieve dividend data, calculate projections, and present findings in a clear, professional format."
- Ensure the agent is instructed to cite sources for all financial figures provided.

### 2) Composio Toolset Node
- **API Key**: Input your Polygon.io API key in the secure credentials manager.
- **Connection Scope**: Limit the scope to read-only access for stock market and dividend data endpoints.

### 3) Tool Availability
- **Stock Price Fetcher**: Retrieves real-time and historical pricing.
- **Dividend Schedule API**: Queries upcoming and historical payout dates.
- **Portfolio Calculator**: Performs mathematical operations on holdings data.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial ledger matching and reconciliation.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with external intelligence signals.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational status and performance of your automated workflows.
