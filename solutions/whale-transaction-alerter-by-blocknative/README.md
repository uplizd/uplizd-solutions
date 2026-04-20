# Whale Transaction Alerter (Uplizd) - Real-time monitoring for high-value blockchain movements

## Summary
The Whale Transaction Alerter is an automated Uplizd workflow designed to monitor blockchain mempools for significant asset movements. By leveraging the Blocknative API, this solution provides real-time visibility into large-scale transactions, enabling traders, analysts, and security teams to react instantly to market-moving events and whale activity.

---

## Demo
![Uplizd Whale Transaction Alerter workflow showing Blocknative integration and real-time alert routing](image.png)
**Alt text (SEO-ready):** Uplizd Whale Transaction Alerter workflow, real-time blockchain monitoring, Blocknative API integration, crypto whale tracking, and automated transaction alerts.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/96e3fa7a-aff8-5965-a893-c7ed18b1ee07)

---

## Category
**Primary category:** Financial Operations
**Secondary tags:** blockchain, crypto, whale tracking, mempool, real-time alerts, blocknative, data monitoring, ai workflow.
This solution bridges the gap between raw blockchain data streams and actionable intelligence for financial monitoring.

---

## Who is this for?
This solution is built for professionals who need to stay ahead of market volatility and monitor large-scale capital flows.

- **Crypto Traders**
    - Gain a competitive edge by identifying large buy or sell orders before they impact market liquidity.
- **Market Analysts**
    - Track institutional movement and whale behavior to inform long-term portfolio strategies.
- **Security Researchers**
    - Monitor for suspicious or anomalous transaction patterns that may indicate exploits or hacks.
- **DeFi Developers**
    - Integrate real-time transaction monitoring into custom dashboards or automated trading infrastructure.

---

## Features
- **Real-time Mempool Monitoring**
    - Connects directly to Blocknative to capture pending transactions before they are confirmed on-chain.
- **Customizable Whale Thresholds**
    - Define specific transaction value triggers to filter out noise and focus only on significant capital movements.
- **Composio Toolset Integration**
    - Seamlessly bridges blockchain data streams with your communication channels or CRM tools.
- **Automated Alert Routing**
    - Automatically pushes high-value transaction data to Slack, Discord, or email for immediate team visibility.
- **Context-Aware Analysis**
    - Uses AI to interpret transaction data and provide human-readable summaries of the whale's activity.

---

## Use Cases
**Market Intelligence**
- Monitor large stablecoin movements between exchanges to predict potential sell pressure.
- Track whale accumulation patterns in specific tokens to identify emerging market trends.

**Risk Management**
- Receive instant alerts when large amounts of assets move from cold storage to hot wallets.
- Detect unusual transaction spikes that could signal a potential protocol exploit or security breach.

**Operational Efficiency**
- Automate the logging of significant transaction events into a centralized spreadsheet for historical analysis.
- Streamline reporting by summarizing daily whale activity into a concise executive brief.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace to import the Whale Transaction Alerter workflow.
3. Authenticate your Blocknative API credentials within the integration settings.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your monitoring parameters (e.g., token address, value threshold).
- **Agent**: Processes transaction data and determines if the event meets your alert criteria.
- **Composio Toolset**: Executes the Blocknative data fetch and external notification triggers.
- **Chat Output**: Delivers the formatted whale alert to your preferred destination.

### 3) Run the Flow
Use the Playground to test your alerts with these prompts:
- `Monitor all transactions over $1,000,000 for the USDC contract address.`
- `Alert me whenever a whale moves more than 500 ETH to a centralized exchange.`
- `Summarize the last 5 high-value transactions for the WBTC token.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that filters raw blockchain data into actionable insights.
- **Recommended instruction pattern:**
    - Act as a blockchain intelligence analyst monitoring mempool data.
    - Only trigger alerts when transaction values exceed the user-defined threshold.
    - Provide a concise summary including the sender, receiver, and estimated USD value.

### 2) Composio Toolset Node
- **API Key**: Ensure your Blocknative API key is active and scoped for mempool stream access.
- **Connection Scope**: Grant the toolset read access to blockchain transaction streams and write access to your notification channels.

### 3) Tool Availability
- **Blocknative Mempool Stream**: Real-time transaction data ingestion.
- **Notification Connectors**: Slack, Discord, or Email for alert delivery.
- **Data Formatter**: Converts hexadecimal blockchain data into human-readable reports.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Track and report on account-level intelligence and signals.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor usage metrics to maintain account health and compliance.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Ensure your automated workflows are running optimally and error-free.
