# NFT Portfolio Optimizer (Uplizd) - Data-driven asset management and performance tracking

## Summary
The NFT Portfolio Optimizer is an intelligent Uplizd AI workflow designed to help digital asset collectors and investors maximize their returns through automated market analysis and portfolio hygiene. By leveraging the Composio Toolset to interface with OpenSea and other market data providers, this solution provides a single source of truth for asset valuation, floor price monitoring, and liquidity tracking, significantly reducing the time spent on manual market research.

---

## Demo
![NFT Portfolio Optimizer dashboard showing asset valuation and market trends](image.png)
**Alt text (SEO-ready):** NFT Portfolio Optimizer dashboard showing Uplizd AI workflow for asset valuation, market trend analysis, and OpenSea portfolio management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d837d108-7fc1-5c01-9017-ec5930bf9de7)

---

## Category
- **Primary category:** Financial operations
- **Secondary tags:** nft, portfolio management, opensea, web3, asset tracking, market intelligence, composio, ai workflow
- This solution bridges the gap between raw blockchain data and actionable investment insights for the modern digital asset manager.

---

## Who is this for?
This workflow is designed for professionals and enthusiasts who manage high-volume digital asset collections.

- **NFT Collectors**
    - Automate the tracking of floor prices across multiple collections to identify buying or selling opportunities.
- **Web3 Investors**
    - Gain a consolidated view of portfolio health and unrealized gains without manual spreadsheet updates.
- **Digital Asset Managers**
    - Streamline the auditing of asset provenance and liquidity status for large-scale wallets.
- **Market Analysts**
    - Generate real-time reports on collection performance and market sentiment shifts.

---

## Features
- **Real-time Valuation**
    - Automatically syncs current floor prices and market data to provide an accurate snapshot of your portfolio's total value.
- **Automated Market Alerts**
    - Monitors specific collections for price volatility and notifies you when assets hit your predefined target thresholds.
- **Composio-Powered Integration**
    - Seamlessly connects to OpenSea and other Web3 APIs to fetch metadata, transaction history, and collection statistics.
- **Liquidity Analysis**
    - Evaluates the trade volume and market depth of your holdings to assess how easily assets can be liquidated.
- **Portfolio Hygiene**
    - Identifies inactive or low-value assets that may be dragging down overall portfolio performance.

---

## Use Cases
**Portfolio Performance Tracking**
- Monitor daily fluctuations in total portfolio value based on live market floor prices.
- Generate weekly summaries of top-performing assets versus stagnant holdings.

**Market Opportunity Identification**
- Detect undervalued assets within a tracked collection when floor prices drop below historical averages.
- Receive alerts when high-demand collections show a sudden spike in trading volume.

**Asset Management & Auditing**
- Verify the metadata and rarity traits of newly acquired assets to ensure collection consistency.
- Audit wallet contents to distinguish between high-value investments and "dust" assets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the NFT Portfolio Optimizer template from the marketplace.
3. Connect your OpenSea API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language queries regarding portfolio status or market trends.
- **Agent**: Processes requests, interprets market data, and formulates strategic investment advice.
- **Composio Toolset**: Executes secure API calls to OpenSea to retrieve real-time NFT market data.
- **Chat Output**: Delivers clear, actionable summaries and insights back to the user interface.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `What is the current total estimated value of my connected NFT portfolio?`
- `Identify any assets in my collection that have dropped more than 10% in floor price today.`
- `Which collections in my portfolio are showing the highest liquidity and trading volume right now?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized financial analyst for digital assets.
- **Instruction Pattern:**
    - Always prioritize current floor price data over historical averages when calculating value.
    - Maintain a neutral, data-driven tone when providing investment insights.
    - Clearly distinguish between confirmed market data and AI-generated trend projections.

### 2) Composio Toolset Node
- Requires a valid OpenSea API key to access collection and asset metadata.
- Connection scope should be limited to "Read-Only" for portfolio analysis to ensure maximum security.

### 3) Tool Availability
- **Market Data Fetcher**: Retrieves real-time floor prices and volume metrics.
- **Asset Metadata Parser**: Extracts trait and rarity information from collection contracts.
- **Wallet Auditor**: Scans connected addresses for asset distribution and liquidity.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Comprehensive reporting for account-level data and intelligence.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automated research workflows for deep-dive account analysis.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracking the operational efficiency of your automated business processes.
