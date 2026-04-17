# Portfolio Health Monitor (Uplizd) - Real-time financial tracking and automated asset performance alerts

## Summary
The Portfolio Health Monitor is an intelligent Uplizd AI workflow designed to provide real-time visibility into investment performance and asset volatility. By leveraging the Polygon.io API, this solution automates the tracking of market data, enabling investors and financial analysts to maintain a single source of truth for their portfolios, reduce manual oversight, and react instantly to market shifts.

---

## Demo
![Portfolio Health Monitor workflow dashboard showing real-time asset tracking and automated alert triggers](image.png)
**Alt text (SEO-ready):** Uplizd Portfolio Health Monitor workflow dashboard showing real-time asset tracking, financial data integration, and automated market alert triggers.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAK+P///38GgAEEA0Y1Gg0jDRgNGA0YDRgNGA0YDRgNGA0YDRgNGA0YDRgNGA0YDQAAw6YF/02120MAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/f74ea1ed-7d9c-5790-b324-56113ec78172)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** portfolio management, polygon.io, market data, asset tracking, financial alerts, ai workflow, data integration, composio
- This solution bridges the gap between raw market data and actionable financial intelligence, streamlining portfolio oversight for modern investors.

---

## Who is this for?
This workflow is built for professionals who require precise, automated monitoring of complex financial portfolios.

- **Financial Analyst**
  - Automates the aggregation of daily market performance reports across multiple asset classes.
- **Portfolio Manager**
  - Receives instant, AI-driven alerts when specific assets hit volatility thresholds or target price points.
- **Individual Investor**
  - Maintains a clean, automated view of investment health without needing to manually check trading platforms.
- **FinTech Developer**
  - Integrates real-time market data pipelines into custom reporting dashboards using the Composio Toolset.

---

## Features
- **Real-time Market Data**
  - Fetches live pricing and historical trends directly from Polygon.io to ensure data accuracy.
- **Automated Alerting**
  - Triggers proactive notifications based on user-defined performance thresholds and market movements.
- **Composio Toolset Integration**
  - Seamlessly connects AI agents to financial APIs, enabling complex data retrieval and analysis.
- **Portfolio Health Scoring**
  - Calculates asset performance metrics to provide a quick summary of overall portfolio stability.
- **Customizable Reporting**
  - Generates structured summaries of portfolio changes, ready for export or immediate review.

---

## Use Cases
**Market Volatility Monitoring**
- Automatically track high-beta assets and receive alerts during significant market swings.
- Monitor specific ticker symbols for breakout patterns or sudden price drops.

**Portfolio Performance Tracking**
- Aggregate daily gains and losses across a diversified set of holdings.
- Compare current asset values against historical performance benchmarks.

**Automated Financial Reporting**
- Generate end-of-day portfolio summaries to identify underperforming assets.
- Sync market data updates into internal tracking systems for consistent record-keeping.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your Polygon.io API credentials within the Composio Toolset configuration.
3. Review the Agent instructions to ensure they align with your specific portfolio tracking needs.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your request for portfolio status or specific asset data.
- **Agent**: Processes financial queries and determines which market data to fetch.
- **Composio Toolset**: Executes secure API calls to Polygon.io to retrieve real-time data.
- **Chat Output**: Delivers the analyzed insights and performance summaries back to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check the current performance of my tech portfolio and alert me if any asset dropped by more than 5%.`
- `Get the latest market data for AAPL and TSLA and summarize the volatility over the last 24 hours.`
- `Provide a health report for my current holdings and identify the top 3 gainers today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your financial research assistant, interpreting market data and summarizing findings.
- Focus on identifying anomalies and trends rather than just raw numbers.
- Maintain a professional, objective tone in all financial summaries.
- Prioritize clear, actionable insights over verbose data dumps.

### 2) Composio Toolset Node
- Requires a valid Polygon.io API key.
- Connection scope should be limited to "Read-Only" market data access for security.

### 3) Tool Availability
- **Market Data Fetcher**: Retrieves real-time quotes, historical candles, and ticker details.
- **Volatility Analyzer**: Calculates percentage changes and identifies threshold breaches.
- **Summary Generator**: Formats complex financial data into readable, user-friendly reports.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automates the gathering of account-level intelligence and reporting.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks and monitors account health metrics for improved retention.
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) — Provides proactive monitoring and alerts for organizational risk factors.
