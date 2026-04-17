# NFT Portfolio Tracker (Uplizd) - Automated asset monitoring and valuation

## Summary
The NFT Portfolio Tracker is an intelligent Uplizd workflow that provides real-time visibility into digital asset holdings by leveraging the Alchemy API. This solution enables users to automate the valuation, tracking, and reporting of NFT collections, ensuring that collectors and investors maintain a single source of truth for their portfolio performance without manual data entry.

---

## Demo
![NFT Portfolio Tracker dashboard showing real-time asset valuation and collection analytics](image.png)

**Alt text (SEO-ready):** NFT portfolio tracker dashboard displaying real-time asset valuation, collection analytics, and blockchain data synchronization using Uplizd and Alchemy.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/998ec7fb-47bb-5db4-b874-b5007232e91b)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** nft, alchemy, blockchain, portfolio, asset tracking, web3, composio, data sync
- This solution bridges the gap between raw blockchain data and actionable financial insights for digital asset management.

---

## Who is this for?
This workflow is designed for professionals and enthusiasts managing complex digital asset portfolios who require automated oversight.

- **NFT Collectors**
    - Monitor floor prices and total portfolio valuation across multiple wallets in real-time.
- **Web3 Investors**
    - Track asset performance trends and historical growth without manual spreadsheet updates.
- **Portfolio Managers**
    - Generate automated reports on asset distribution and liquidity for client portfolios.
- **Blockchain Developers**
    - Integrate live NFT metadata into custom dashboards using the Alchemy-powered Composio toolset.

---

## Features
- **Real-time Valuation**
    - Automatically fetch the latest market prices for NFTs held in your connected wallets.
- **Multi-Wallet Aggregation**
    - Consolidate data from various addresses into a unified view for comprehensive portfolio analysis.
- **Alchemy API Integration**
    - Utilize high-fidelity blockchain data via the Composio Toolset to ensure accurate asset identification.
- **Automated Reporting**
    - Generate summary snapshots of your collection's performance and rarity distribution.
- **Dynamic Sync**
    - Keep your portfolio records updated automatically as new transactions occur on the blockchain.

---

## Use Cases
**Portfolio Monitoring**
- Track the total value of your NFT holdings across Ethereum and Polygon networks.
- Receive alerts when the floor price of your key assets shifts significantly.

**Asset Research**
- Query specific NFT metadata to verify ownership history and current market status.
- Compare the performance of different collections within your portfolio.

**Financial Reporting**
- Export portfolio snapshots for tax documentation or personal financial planning.
- Create recurring summaries of asset appreciation to inform future buying decisions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Configure your Alchemy API credentials within the Composio Toolset node.
4. Ensure nodes are connected correctly: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your wallet address or specific NFT collection queries.
- **Agent**: Processes natural language requests and orchestrates the data retrieval.
- **Composio Toolset**: Executes the Alchemy API calls to fetch real-time blockchain data.
- **Chat Output**: Displays the formatted portfolio valuation and asset details.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Show me the total valuation of my NFT portfolio for wallet address 0x...`
- `List all NFTs in my collection and their current floor prices.`
- `Compare the performance of my Bored Ape collection against my Azuki holdings.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a blockchain data analyst, translating user intent into precise API queries.
- Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are an expert NFT analyst. Use the Composio Toolset to fetch accurate blockchain data."
- Instruction: "Always summarize portfolio values clearly and highlight significant changes in asset pricing."

### 2) Composio Toolset Node
- Provide your Alchemy API key to enable connection to the blockchain.
- Set the connection scope to allow read-only access to NFT metadata and wallet balances.

### 3) Tool Availability
- **Alchemy NFT API**: Fetch asset metadata, floor prices, and collection stats.
- **Wallet Balance Checker**: Retrieve current token and NFT holdings for specific addresses.
- **Market Data Parser**: Normalize raw blockchain data into readable financial summaries.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate business contact enrichment and data gathering.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Streamline deep-dive research on target accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize the performance of your automated internal processes.
