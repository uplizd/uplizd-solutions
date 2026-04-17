# Portfolio Performance Monitor (Uplizd) - Automated financial tracking and asset analysis

## Summary
The Portfolio Performance Monitor is an intelligent Uplizd AI workflow designed to automate the tracking, analysis, and reporting of investment portfolios. By leveraging real-time data integration via the Finage API, this solution provides investors and financial analysts with a single source of truth for asset valuation, performance trends, and market volatility, significantly reducing manual data entry and increasing investment decision velocity.

---

## Demo
![Portfolio Performance Monitor dashboard showing real-time asset tracking and performance analytics](image.png)
**Alt text (SEO-ready):** Portfolio Performance Monitor dashboard showing real-time asset tracking, financial performance analytics, and automated market data reporting on Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQk45Q5QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAKYGBgYPhPBf9/YGBg+E8F/39gYGD4TwX/f2BgYPhPBf9/YGBg+E8F/39gYGD4TwUAAC48A0N255QAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/2ad614ad-45fe-59db-8317-b3b92beab7fb)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** portfolio, finance, finage, market data, asset tracking, investment analysis, composio, ai workflow
- This solution bridges the gap between raw market data feeds and actionable financial insights for modern portfolio management.

---

## Who is this for?
This workflow is designed for financial professionals and individual investors who require precise, automated oversight of their asset performance.

- **Portfolio Manager**
    - Automates daily performance reporting to stakeholders without manual spreadsheet updates.
- **Financial Analyst**
    - Gains immediate access to normalized market data for deeper trend analysis and risk assessment.
- **Individual Investor**
    - Monitors multi-asset performance in real-time to make informed buy/sell decisions.
- **Operations Lead**
    - Ensures data hygiene across financial tracking systems by syncing live market feeds directly to internal dashboards.

---

## Features
- **Real-time Market Data**
    - Integrates directly with Finage to pull live pricing, historical trends, and asset volatility metrics.
- **Automated Performance Reporting**
    - Generates summary reports on portfolio health, highlighting top-performing assets and potential risks.
- **Composio-Powered Connectivity**
    - Utilizes the Composio Toolset to securely bridge the AI agent with financial data APIs and reporting platforms.
- **Customizable Alerting**
    - Configures threshold-based notifications for significant price movements or portfolio rebalancing needs.
- **Unified Data Synchronization**
    - Maintains a consistent view of assets across multiple accounts, ensuring all reporting is based on the latest market data.

---

## Use Cases
**Portfolio Health Monitoring**
- Tracking daily percentage changes across diverse asset classes like stocks, ETFs, and crypto.
- Identifying underperforming assets that fall below predefined ROI thresholds.

**Market Intelligence Gathering**
- Aggregating historical price data to identify long-term growth patterns for specific tickers.
- Correlating portfolio performance against broader market indices to assess relative strength.

**Automated Financial Reporting**
- Creating end-of-day summary reports for automated delivery to team communication channels.
- Preparing audit-ready logs of asset valuations for compliance and tax reporting purposes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Portfolio Performance Monitor template from the solution library.
3. Connect your Finage API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding specific tickers or general portfolio status.
- **Agent**: Processes financial data and formulates analytical responses based on market inputs.
- **Composio Toolset**: Executes secure API calls to fetch real-time data from Finage.
- **Chat Output**: Delivers formatted performance insights and data summaries to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `What is the current performance trend for AAPL over the last 30 days?`
- `Compare the volatility of my current portfolio assets against the S&P 500.`
- `Generate a summary report of my top 5 assets by total value.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial analyst assistant capable of interpreting complex market data.
- Maintain a professional, data-driven tone in all responses.
- Prioritize accuracy by citing the specific data points retrieved from the Finage API.
- Use clear, structured formatting (tables or bullet points) for performance comparisons.

### 2) Composio Toolset Node
- Requires a valid Finage API key configured within the Composio platform.
- Connection scope should be limited to read-only access for market data retrieval to ensure security.

### 3) Tool Availability
- **Market Data Fetcher**: Retrieves live and historical price data.
- **Volatility Analyzer**: Calculates standard deviation and risk metrics for specified assets.
- **Report Generator**: Formats raw data into human-readable summaries.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automates financial ledger matching and reconciliation tasks.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks customer usage patterns and account health metrics.
- [Ad Trend Tracking Agent](../ad-trend-tracking-agent-by-adyntel/README.md) — Monitors advertising performance trends and market shifts.
