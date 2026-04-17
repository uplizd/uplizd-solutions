# Commodity Price Monitor (Uplizd) - Real-time market tracking and automated trading alerts

## Summary
The Commodity Price Monitor is an intelligent Uplizd workflow designed to track volatile market assets and deliver actionable price alerts directly to your team. By leveraging the Alpha Vantage API via the Composio Toolset, this solution eliminates manual market monitoring, ensuring traders and analysts receive real-time data updates to optimize their decision-making pipeline and maintain a competitive edge.

---

## Demo
![Uplizd Commodity Price Monitor workflow showing Alpha Vantage integration and automated alert triggers](image.png)
**Alt text (SEO-ready):** Uplizd Commodity Price Monitor workflow, Alpha Vantage market data integration, automated trading alerts, and real-time price tracking pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/abbbf21f-00bc-52eb-9276-9f887346c7f0)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** commodity, trading, alpha vantage, market data, price alerts, automation, composio, ai workflow
- This solution bridges the gap between raw financial data streams and human-readable insights, streamlining how organizations monitor market fluctuations.

---

## Who is this for?
This workflow is built for financial professionals and operations teams who require high-frequency data awareness without the overhead of manual dashboard monitoring.

- **Financial Trader**
    - Receives instant notifications on price breakouts to execute trades with higher precision.
- **Market Analyst**
    - Automates the collection of commodity trends, allowing more time for strategic forecasting.
- **Operations Manager**
    - Ensures the team stays informed on supply chain cost fluctuations that impact procurement.
- **FinTech Developer**
    - Rapidly integrates market data triggers into existing internal communication channels.

---

## Features
- **Real-time Data Fetching**
    - Connects directly to Alpha Vantage to pull the latest commodity pricing, ensuring data accuracy and latency-free updates.
- **Intelligent Alerting**
    - Configures custom thresholds that trigger notifications only when significant market movements occur.
- **Composio-Powered Integration**
    - Utilizes the robust Composio Toolset to securely authenticate and manage API requests to financial data providers.
- **Automated Reporting**
    - Summarizes complex price trends into concise, actionable insights delivered via your preferred chat interface.
- **Workflow Scalability**
    - Easily adapts to track multiple commodities or asset classes simultaneously within a single, unified Uplizd flow.

---

## Use Cases
**Market Volatility Tracking**
- Monitor sudden price spikes in precious metals or energy commodities during geopolitical events.
- Automatically log daily closing prices to a centralized database for historical trend analysis.

**Procurement Cost Optimization**
- Receive alerts when raw material costs drop below a target threshold to trigger bulk purchasing.
- Compare current market rates against internal budget benchmarks to identify cost-saving opportunities.

**Automated Trading Signals**
- Generate pre-market summaries for traders based on overnight commodity price movements.
- Trigger real-time alerts for technical support or resistance levels reached by specific assets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Commodity Price Monitor template from the solution library.
3. Authenticate your Alpha Vantage API key within the Composio Toolset settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the commodity ticker symbol or user request for market data.
- **Agent**: Processes the request and determines the necessary API calls to fetch current pricing.
- **Composio Toolset**: Executes the secure connection to Alpha Vantage to retrieve requested market metrics.
- **Chat Output**: Formats the retrieved data into a clear, concise response for the user.

### 3) Run the Flow
Open the Uplizd Playground and test the workflow with these prompts:
- `Check the current price of Gold (XAU) and alert me if it moves by more than 1%.`
- `What is the latest market trend for Crude Oil (WTI) today?`
- `Compare the current price of Silver against its 30-day average.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting user queries and mapping them to specific API functions.
- **Instruction Pattern:**
    - Always verify the ticker symbol provided by the user before executing the API call.
    - Summarize complex financial data into bullet points for readability.
    - Maintain a professional, objective tone when reporting market fluctuations.

### 2) Composio Toolset Node
- Requires a valid Alpha Vantage API key configured within your Uplizd environment.
- Connection scope should be set to "Read-Only" for market data access to ensure security.

### 3) Tool Availability
- `get_commodity_price`: Fetches real-time pricing for specified assets.
- `get_market_trend`: Retrieves historical data points to calculate trends.
- `send_alert_notification`: Triggers an outbound message when price thresholds are met.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automates the gathering of account-level intelligence and reporting.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Streamlines deep-dive research into target accounts and market entities.
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) — Monitors for operational risks and provides automated early warnings.
