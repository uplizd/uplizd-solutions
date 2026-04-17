# NFT Deal Scout (Uplizd) - Real-time NFT market intelligence and asset discovery

## Summary
The NFT Deal Scout (Uplizd) is an automated AI workflow designed to monitor OpenSea marketplaces for undervalued digital assets. By leveraging the Composio Toolset to interface with real-time blockchain data, this solution enables collectors and traders to identify high-potential opportunities, track floor price fluctuations, and execute acquisition strategies with precision, ensuring users never miss a favorable market entry point.

---

## Demo
![NFT Deal Scout dashboard showing real-time OpenSea asset monitoring and price analysis](image.png)
**Alt text (SEO-ready):** NFT Deal Scout Uplizd workflow showing real-time OpenSea asset monitoring, price analysis, and automated deal detection for NFT traders.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge.svg)](https://uplizd.ai/solutions/6f4a3af8-cf7d-5fba-9f67-741bd34228d4)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** nft, opensea, market intelligence, asset discovery, web3, crypto trading, composio, ai workflow
- This solution bridges the gap between raw blockchain data and actionable trading insights, providing a competitive edge in volatile NFT markets.

---

## Who is this for?
This workflow is built for digital asset professionals and collectors who require automated, data-driven market surveillance.

- **NFT Traders**
    - Automate the discovery of undervalued assets to maximize portfolio ROI.
- **Market Analysts**
    - Track floor price trends and collection health across OpenSea in real-time.
- **Web3 Portfolio Managers**
    - Monitor specific collections for sudden liquidity events or price drops.
- **Digital Asset Collectors**
    - Receive instant alerts when rare items meet predefined valuation criteria.

---

## Features
- **Real-time Market Scanning**
    - Continuously monitors OpenSea listings to capture price changes as they happen.
- **Automated Valuation Logic**
    - Uses AI to compare current listing prices against historical floor data and rarity metrics.
- **Composio Toolset Integration**
    - Seamlessly connects to OpenSea APIs to fetch live metadata and transaction status.
- **Custom Alerting Thresholds**
    - Allows users to define specific price-to-value ratios for automated deal scouting.
- **Actionable Insights Output**
    - Delivers clear, formatted summaries of top-tier deals directly to your chat interface.

---

## Use Cases
**Market Opportunity Identification**
- Automatically flag NFTs listed at 20% below the 7-day rolling floor price.
- Identify "snipe-worthy" assets during high-volatility market periods.

**Portfolio Intelligence**
- Track the floor price movement of specific blue-chip collections over 24-hour windows.
- Generate daily reports on collection volume and unique owner distribution.

**Automated Trading Prep**
- Pre-verify asset metadata and contract safety before flagging a deal for the user.
- Aggregate multiple listing signals to confirm the legitimacy of a price dip.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the NFT Deal Scout template from the marketplace library.
3. Connect your OpenSea API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your specific collection search queries or market parameters.
- **Agent**: Processes market data and applies valuation logic to identify deals.
- **Composio Toolset**: Executes secure API calls to OpenSea to retrieve live listing data.
- **Chat Output**: Returns a curated list of actionable NFT opportunities to the user.

### 3) Run the Flow
Use the Playground to test your scouting parameters:
- `Find undervalued assets in the Bored Ape Yacht Club collection under 50 ETH.`
- `Monitor the floor price for Azuki and alert me if it drops below 10 ETH.`
- `List the top 5 most undervalued NFTs in the current market based on 24h volume.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your dedicated market analyst, interpreting raw data into trading signals.
- Use a high-reasoning model (e.g., GPT-4o) for accurate price comparison.
- Instruct the agent to prioritize volume-weighted floor prices over outliers.
- Maintain a neutral, data-first tone for all deal reporting.

### 2) Composio Toolset Node
- Provide your OpenSea API key to enable read-access to marketplace data.
- Set the connection scope to include `market_data_read` and `collection_metadata_fetch`.

### 3) Tool Availability
- `fetch_collection_floor`: Retrieves the current lowest listing price.
- `get_asset_metadata`: Pulls rarity and trait information for specific tokens.
- `list_market_activity`: Monitors recent sales and listing volume.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data for better lead qualification.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive research for high-value sales targets.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex operational tasks across platforms.
