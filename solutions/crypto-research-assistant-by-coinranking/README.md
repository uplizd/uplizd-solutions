# Crypto Research Assistant (Uplizd) - Real-time market intelligence and trend analysis

## Summary
The Crypto Research Assistant by Coinranking is an automated AI workflow designed to streamline digital asset analysis, providing investors and analysts with a single source of truth for market data. By integrating real-time cryptocurrency metrics with intelligent agentic processing, this solution eliminates manual data gathering, increases pipeline velocity for research teams, and ensures high-fidelity market insights are delivered instantly.

---

## Demo
![Crypto Research Assistant dashboard showing real-time token price trends and market sentiment analysis](image.png)
**Alt text (SEO-ready):** Crypto Research Assistant by Uplizd workflow showing real-time token price trends, market sentiment analysis, and Coinranking data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8935da66-d6e2-5c3c-a54c-2b5f1b8002e7)

---

## Category
- **Primary category:** Financial Research
- **Secondary tags:** crypto, coinranking, market intelligence, trend analysis, data integration, ai agent, financial data, blockchain
- This solution leverages the Coinranking API to transform raw blockchain data into actionable investment intelligence for professional and retail researchers.

---

## Who is this for?
This solution is designed for professionals who need to monitor volatile market conditions and extract meaningful signals from complex datasets.

- **Crypto Analyst**
    - Automates the extraction of historical price data and market cap trends to support investment theses.
- **Portfolio Manager**
    - Monitors asset performance across multiple chains to ensure portfolio alignment with market shifts.
- **BDR / Growth Lead**
    - Identifies emerging token trends to prioritize outreach and partnership opportunities in the Web3 space.
- **Research Researcher**
    - Synthesizes fragmented market reports into concise summaries, saving hours of manual data aggregation.

---

## Features
- **Real-time Market Data**
    - Fetches live price, volume, and market cap data directly from Coinranking to ensure decision-making is based on the latest blockchain state.
- **Automated Trend Identification**
    - Uses AI to scan for significant price movements and volume anomalies, highlighting potential opportunities before they reach mainstream news.
- **Composio-Powered Integration**
    - Seamlessly connects the agent to external tools and APIs, allowing for complex multi-step research workflows without manual intervention.
- **Customizable Research Reports**
    - Generates structured summaries tailored to specific asset classes or watchlist requirements, improving data hygiene and readability.
- **Intelligent Alerting**
    - Configures the agent to monitor specific triggers, ensuring users receive timely notifications on critical market events.

---

## Use Cases
**Market Sentiment Analysis**
- Aggregating price action data to correlate with broader market sentiment shifts.
- Identifying top-performing assets within specific sectors like DeFi or Layer-2 protocols.

**Portfolio Performance Tracking**
- Automating the daily reporting of asset price changes for a predefined watchlist.
- Comparing historical performance metrics across different time windows to identify growth patterns.

**Opportunity Scouting**
- Scanning for new token listings or significant volume spikes that signal early-stage market interest.
- Filtering market data to find undervalued assets based on specific technical or fundamental criteria.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the **Crypto Research Assistant**.
2. Click "Import" to add the workflow template to your workspace.
3. Configure your API credentials within the environment settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your research queries or market monitoring requests.
- **Agent**: Processes the intent and determines the necessary data retrieval steps.
- **Composio Toolset**: Executes secure API calls to Coinranking and other integrated financial tools.
- **Chat Output**: Delivers the synthesized research report or market insight back to the user.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Analyze the current market performance of the top 5 DeFi tokens by volume.`
- `What are the recent price trends for Ethereum over the last 7 days?`
- `Identify any significant volume anomalies in the current crypto market.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting user requests and orchestrating tool usage.
- **Recommended instruction pattern:**
    - Always verify the timestamp of the data retrieved from the API.
    - Prioritize clear, concise summaries over raw data dumps.
    - Cite the source (Coinranking) for all price and market cap figures.

### 2) Composio Toolset Node
- Requires a valid Coinranking API key configured within the Composio dashboard.
- Connection scope should be set to 'Read-Only' for market data retrieval.

### 3) Tool Availability
- **Market Data Fetcher**: Retrieves real-time token prices and market statistics.
- **Historical Analysis Engine**: Processes time-series data for trend identification.
- **Report Generator**: Formats raw findings into professional, readable summaries.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research on corporate accounts and business entities.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Aggregates lead intelligence to improve sales pipeline quality.
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) — Monitors research trends and publication metrics for academic analysis.
