# NFT Market Intelligence Agent (Uplizd) - Real-time blockchain trend analysis and asset tracking

## Summary
The NFT Market Intelligence Agent is an automated workflow designed to provide real-time insights into NFT collections, floor prices, and market trends. By leveraging the Alchemy API through the Uplizd platform, this solution empowers collectors, investors, and project managers to maintain a competitive edge through data-driven decision-making, eliminating the need for manual dashboard monitoring and fragmented research.

---

## Demo
![NFT Market Intelligence Agent dashboard showing real-time floor price tracking and collection volume analysis](image.png)

**Alt text (SEO-ready):** NFT Market Intelligence Agent dashboard showing real-time floor price tracking and collection volume analysis using Uplizd and Alchemy for blockchain data insights.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDSEq9+58YgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAKYGBgYPhPBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf9fBf8AAL4yBf+5l6+wAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/dbcdc8ee-4ce3-5c53-8e65-9670b2907511)

---

## Category
**Primary category:** Data Intelligence
**Secondary tags:** nft, blockchain, alchemy, market research, web3, asset tracking, data analytics, composio

This solution bridges the gap between raw blockchain data and actionable market intelligence for web3 operations.

---

## Who is this for?
This agent is built for professionals who need to synthesize complex blockchain data into clear market signals.

* **NFT Investor**
    * Access real-time floor price movements and collection volume spikes to optimize buy/sell timing.
* **Web3 Project Manager**
    * Monitor competitor collection performance and community engagement metrics to refine project strategy.
* **Data Analyst**
    * Automate the extraction of historical NFT transaction data for custom reporting and trend forecasting.
* **Growth Marketer**
    * Identify trending collections and high-value wallet activity to inform targeted outreach and partnership efforts.

---

## Features
- **Real-time Floor Tracking**
  Monitor live floor price fluctuations for specific NFT collections using high-fidelity Alchemy data streams.
- **Automated Trend Analysis**
  Automatically process market volume and sales velocity to identify emerging NFT trends before they peak.
- **Composio Toolset Integration**
  Seamlessly connect the agent to blockchain APIs via the Composio Toolset for secure, authenticated data retrieval.
- **Custom Alerting Logic**
  Configure the agent to trigger notifications based on specific price thresholds or volume anomalies.
- **Historical Data Synthesis**
  Aggregate historical transaction logs into concise summaries to provide context for current market movements.

---

## Use Cases
**Market Monitoring**
* Track the floor price of top-tier collections across multiple marketplaces to identify arbitrage opportunities.
* Receive automated daily summaries of volume changes for tracked NFT projects.

**Competitive Intelligence**
* Analyze the minting patterns and secondary market activity of competitor collections.
* Compare holder distribution and unique wallet counts to gauge project health and community sentiment.

**Portfolio Management**
* Automate the valuation of personal or institutional NFT portfolios based on the latest market data.
* Generate performance reports for specific assets to support long-term investment strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your Alchemy API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your natural language queries regarding NFT collections or market trends.
* **Agent**: Processes the request, determines the necessary blockchain data, and orchestrates the tool calls.
* **Composio Toolset**: Executes secure API calls to Alchemy to fetch real-time and historical NFT data.
* **Chat Output**: Delivers a human-readable summary or data table directly to your chat interface.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
* `What is the current floor price and 24-hour volume for the Bored Ape Yacht Club collection?`
* `Identify any significant volume spikes in the top 10 trending NFT collections today.`
* `Compare the floor price trends of Azuki and Doodles over the last 7 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain, translating user intent into precise API queries.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Set system instructions to prioritize data accuracy and concise, professional reporting.
* Ensure the agent is instructed to cite data sources when presenting market statistics.

### 2) Composio Toolset Node
* Provide your valid Alchemy API key within the Composio configuration.
* Set the connection scope to include read-only access to NFT and blockchain metadata endpoints.

### 3) Tool Availability
* **NFT Metadata Fetcher**: Retrieves collection details, floor prices, and contract information.
* **Market Volume Analyzer**: Aggregates sales data over user-defined time windows.
* **Wallet Activity Monitor**: Tracks high-value transactions and whale movements within specific collections.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data for better sales targeting.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate detailed reports on account engagement and intent.
* [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Track competitor performance and content trends.
