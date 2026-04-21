# Wallet Activity Tracker (Uplizd) - Real-time blockchain transaction monitoring and analysis

## Summary
The Wallet Activity Tracker (Uplizd) is an automated AI workflow designed to monitor, analyze, and report on blockchain wallet transactions in real-time. By leveraging the Composio Toolset to interface with Alchemy’s robust blockchain APIs, this solution provides financial analysts, developers, and crypto-asset managers with a single source of truth for on-chain activity, ensuring pipeline velocity and data hygiene for complex digital asset portfolios.

---

## Demo
![Wallet Activity Tracker dashboard showing real-time transaction monitoring and transaction history analysis](image.png)
**Alt text (SEO-ready):** Wallet Activity Tracker (Uplizd) workflow showing real-time blockchain transaction monitoring, Alchemy API integration, and automated wallet analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2d197640-844c-5f7b-80eb-4a92f71415a8)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** blockchain, wallet tracking, alchemy, crypto, transaction analysis, web3, composio, ai workflow
- This solution bridges the gap between raw blockchain data and actionable financial intelligence, streamlining the way users track and interpret on-chain movements.

---

## Who is this for?
This workflow is built for professionals who require precise, automated oversight of digital asset movements.

- **Financial Analyst**
    - Automates the reconciliation of wallet inflows and outflows against expected ledger entries.
- **Crypto-Asset Manager**
    - Receives real-time alerts on significant transaction events to manage portfolio risk effectively.
- **Web3 Developer**
    - Simplifies the integration of blockchain event data into existing operational dashboards.
- **Compliance Officer**
    - Maintains a clean audit trail of wallet activity for regulatory reporting and internal hygiene.

---

## Features
- **Real-time Transaction Monitoring**
    - Tracks incoming and outgoing transfers across multiple chains with sub-second latency.
- **Alchemy API Integration**
    - Utilizes the Composio Toolset to query high-fidelity blockchain data directly from Alchemy.
- **Automated Activity Summarization**
    - Synthesizes complex transaction logs into human-readable reports and executive summaries.
- **Custom Alerting Logic**
    - Triggers notifications based on specific transaction thresholds or wallet address activity.
- **Historical Data Sync**
    - Enables bulk retrieval of past transaction history for deep-dive audits and trend analysis.

---

## Use Cases
**Portfolio Oversight**
- Monitor daily balance fluctuations across high-value cold and hot wallets.
- Generate weekly summaries of asset movement for stakeholder reporting.

**Risk Management**
- Detect anomalous transaction patterns that deviate from standard wallet behavior.
- Automate immediate notification workflows when large-scale transfers occur.

**Operational Auditing**
- Reconcile on-chain transaction hashes with internal accounting software entries.
- Maintain a persistent, searchable database of all wallet interactions for compliance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Wallet Activity Tracker template from the solution library.
3. Connect your Alchemy API credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Accepts the target wallet address and the desired time range for analysis.
- **Agent**: Processes the request and determines which blockchain data points to retrieve.
- **Composio Toolset**: Executes precise API calls to Alchemy to fetch transaction logs and metadata.
- **Chat Output**: Delivers a structured, formatted report of the wallet's activity directly to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Analyze the last 24 hours of transactions for wallet 0x123...abc and summarize the top three largest transfers.`
- `Check for any anomalous activity in the provided wallet address over the last week.`
- `Generate a report of all token inflows for this wallet and categorize them by asset type.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized blockchain analyst.
- Use a model with strong reasoning capabilities to interpret raw transaction data.
- Instruction: "You are a blockchain data expert. Always verify the transaction hash and timestamp before reporting."
- Instruction: "Format all financial data into clear, easy-to-read tables for the end user."

### 2) Composio Toolset Node
- Provide your Alchemy API Key to enable secure, authenticated access to blockchain nodes.
- Set the connection scope to allow read-only access to transaction history and account balances.

### 3) Tool Availability
- `alchemy_get_transaction_history`: Retrieves chronological logs of wallet activity.
- `alchemy_get_balance`: Fetches current token and ETH/MATIC balances.
- `alchemy_get_asset_transfers`: Filters specific token movements for detailed auditing.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enhances account data with deep intelligence and contact insights.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automates the matching of financial transactions with accounting records.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks the performance and status of automated operational pipelines.
