# NFT Collection Performance Tracker (Uplizd) - Real-time blockchain analytics and trading insights

## Summary
The NFT Collection Performance Tracker is an automated Uplizd AI workflow that monitors, analyzes, and reports on NFT collection metrics and trading patterns. By leveraging the Bitquery integration, this solution provides collectors and analysts with a single source of truth for floor prices, volume trends, and holder distribution, significantly increasing pipeline velocity for market research and data-driven decision-making.

---

## Demo
![NFT Collection Performance Tracker dashboard showing real-time floor price and volume trends](image.png)
**Alt text (SEO-ready):** NFT Collection Performance Tracker dashboard showing real-time floor price, trading volume, and holder distribution trends using Uplizd AI and Bitquery.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9c56d114-37df-547c-98e2-01f2213d4db8)

---

## Category
**Primary category:** Data integration
**Secondary tags:** nft, blockchain, bitquery, web3, market analysis, data hygiene, composio, ai workflow.
This solution bridges the gap between raw blockchain data and actionable market intelligence for web3 professionals.

---

## Who is this for?
This workflow is designed for professionals managing digital asset portfolios and those requiring deep-dive blockchain analytics.

*   **NFT Investor**
    *   Gain real-time visibility into floor price fluctuations and volume spikes to optimize entry and exit points.
*   **Web3 Data Analyst**
    *   Automate the collection of complex on-chain metrics, reducing manual research time by hours per week.
*   **Community Manager**
    *   Track collection health and holder sentiment to better inform community engagement strategies.
*   **Market Researcher**
    *   Identify emerging trading patterns and collection performance trends across multiple blockchain networks.

---

## Features
- **Real-time Market Monitoring**
  Connects directly to blockchain data sources to pull the latest floor prices and trading volumes as they happen.
- **Automated Trend Reporting**
  Uses the Composio Toolset to synthesize raw data into clear, natural language summaries for quick decision-making.
- **Multi-Collection Tracking**
  Monitor multiple NFT projects simultaneously, allowing for comparative analysis and portfolio-wide performance tracking.
- **Customizable Alerting**
  Configure the agent to trigger notifications based on specific price thresholds or volume anomalies.
- **Seamless Data Integration**
  Leverages the power of Bitquery to ensure high-fidelity, accurate data retrieval without manual API management.

---

## Use Cases
**Market Intelligence**
*   Analyze historical floor price trends to identify undervalued NFT collections.
*   Monitor daily trading volume to gauge the liquidity and health of specific projects.

**Portfolio Management**
*   Track the performance of held assets against broader market movements.
*   Receive automated updates on significant changes in holder distribution or "whale" activity.

**Strategic Research**
*   Compare performance metrics across different blockchain ecosystems to identify growth opportunities.
*   Generate weekly reports on collection performance to share with stakeholders or investment teams.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and click "Import Flow."
3. Connect your Bitquery API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your query regarding specific NFT collections or market trends.
*   **Agent**: Processes the request, determines the necessary data, and instructs the toolset.
*   **Composio Toolset**: Executes the Bitquery API calls to fetch real-time blockchain data.
*   **Chat Output**: Delivers a human-readable summary of the requested NFT performance metrics.

### 3) Run the Flow
Open the Playground and try these prompts:
* `What is the current floor price and 24-hour volume for the Bored Ape Yacht Club collection?`
* `Compare the trading volume of the top 3 NFT collections on Ethereum over the last 7 days.`
* `Are there any significant anomalies in the holder distribution for the Azuki collection today?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your specialized web3 analyst.
*   Instruction: "You are an expert NFT market analyst. Use the provided Bitquery tools to fetch accurate, real-time data."
*   Instruction: "Always summarize complex blockchain data into actionable insights for the user."
*   Instruction: "If data is unavailable, clearly state the limitation rather than hallucinating metrics."

### 2) Composio Toolset Node
*   **API Key**: Provide your Bitquery API key via the Composio dashboard.
*   **Connection Scope**: Ensure the toolset has read-only access to blockchain indexing endpoints.

### 3) Tool Availability
*   `bitquery_get_floor_price`: Fetches real-time floor price data for a given contract address.
*   `bitquery_get_trading_volume`: Retrieves historical and current volume metrics.
*   `bitquery_get_holder_stats`: Provides insights into wallet distribution and top holders.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automate business intelligence and account reporting.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Streamline deep-dive research on target accounts.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize the performance of your automated internal processes.
