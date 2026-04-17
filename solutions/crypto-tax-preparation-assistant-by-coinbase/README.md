# Crypto Tax Preparation Assistant (Uplizd) - Automated cryptocurrency transaction data collection and reporting

## Summary
The Crypto Tax Preparation Assistant streamlines the complex process of aggregating, categorizing, and reconciling digital asset transactions across multiple exchanges and wallets. By leveraging the Composio Toolset to interface with financial APIs, this Uplizd workflow reduces manual data entry, ensures tax compliance, and provides a single source of truth for crypto-asset holders and tax professionals.

---

## Demo
![Crypto Tax Preparation Assistant workflow interface showing data aggregation from Coinbase and wallet connections](image.png)
**Alt text (SEO-ready):** Crypto Tax Preparation Assistant Uplizd workflow for automated cryptocurrency transaction data collection and financial reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/278d961d-6cff-5e86-895d-fedb6fcc9089)

---

## Category
- **Primary category:** Finance
- **Secondary tags:** crypto, tax, coinbase, data reconciliation, financial reporting, asset management, composio, ai workflow
- This solution bridges the gap between decentralized exchange data and standardized tax reporting formats to simplify annual fiscal filings.

---

## Who is this for?
This solution is designed for individuals and organizations managing high-volume digital asset portfolios who require precision and audit-readiness.

- **Crypto Investors**
    - Automate the aggregation of trade history across multiple wallets to minimize manual errors during tax season.
- **Tax Professionals**
    - Streamline client data collection by pulling standardized transaction logs directly from exchange APIs.
- **DeFi Traders**
    - Maintain accurate cost-basis tracking for complex transactions, including swaps, staking rewards, and liquidity provision.
- **Financial Controllers**
    - Ensure corporate compliance by generating audit-ready reports for all digital asset holdings and movements.

---

## Features
- **Automated Data Aggregation**
    - Connects directly to exchange APIs to pull real-time transaction history without manual CSV uploads.
- **Transaction Categorization**
    - Automatically classifies transactions into taxable events, transfers, or staking rewards using intelligent agent logic.
- **Cost-Basis Calculation**
    - Calculates gains and losses based on historical price data at the time of each transaction.
- **Compliance-Ready Reporting**
    - Formats output data to align with standard tax filing requirements, reducing the time spent on manual reconciliation.
- **Multi-Wallet Support**
    - Orchestrates data retrieval across various platforms and wallets through the unified Composio Toolset.

---

## Use Cases
**Annual Tax Filing**
- Exporting a comprehensive summary of all capital gains and losses for the fiscal year.
- Generating itemized transaction reports for specific tax jurisdictions.

**Portfolio Auditing**
- Reconciling wallet balances against exchange-reported data to identify discrepancies.
- Tracking staking and airdrop rewards as taxable income throughout the quarter.

**Data Hygiene & Cleanup**
- Removing duplicate transaction entries caused by multi-platform syncing.
- Standardizing date and currency formats across disparate exchange data sources.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Crypto Tax Preparation Assistant template from the solution library.
3. Connect your preferred exchange API keys within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user requests for specific tax periods or asset reports.
- **Agent**: Processes financial queries and orchestrates the retrieval of transaction data.
- **Composio Toolset**: Executes secure API calls to fetch and normalize crypto transaction logs.
- **Chat Output**: Delivers the formatted tax report or summary to the user interface.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Generate a capital gains report for all transactions on Coinbase for the 2023 tax year.`
- `List all staking rewards received in my wallet during the last quarter.`
- `Identify any missing cost-basis information for my recent ETH trades.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial data analyst, prioritizing accuracy and chronological ordering.
- Instruction: "You are a crypto tax assistant; prioritize accuracy and clear categorization of transaction types."
- Instruction: "Always verify the date range provided by the user before querying the API."
- Instruction: "If data is missing for a specific transaction, flag it for manual review rather than estimating values."

### 2) Composio Toolset Node
- **API Key**: Input your unique exchange API credentials to enable read-only access to transaction history.
- **Connection Scope**: Limit the scope to `read_transactions` and `read_account_balance` to ensure security.

### 3) Tool Availability
- **Transaction Fetcher**: Retrieves raw trade data from connected exchanges.
- **Price Oracle**: Fetches historical asset pricing for accurate cost-basis calculation.
- **Report Formatter**: Converts raw JSON data into user-friendly summary reports.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate ledger balancing and financial data matching.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate and report on account-level data insights.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the status and performance of automated data pipelines.
