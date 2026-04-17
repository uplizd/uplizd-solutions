# DeFi Protocol Health Dashboard (Uplizd) - Real-time blockchain risk and performance monitoring

## Summary
The DeFi Protocol Health Dashboard by Bitquery provides a centralized, automated monitoring system for decentralized finance protocols. By leveraging real-time blockchain data, this Uplizd AI workflow enables developers, analysts, and protocol managers to track liquidity, transaction volume, and smart contract anomalies, ensuring pipeline velocity and proactive risk mitigation in a single source of truth.

---

## Demo
![DeFi Protocol Health Dashboard interface showing real-time blockchain metrics and risk alert triggers](image.png)
**Alt text (SEO-ready):** DeFi Protocol Health Dashboard by Bitquery showing real-time blockchain analytics, risk monitoring, and automated protocol performance tracking on Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMJFR0W+7/35QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK04AAAAiSURBVEjHY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwChgBAAAGAAH5314AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/6852fa8f-228e-50f6-9c03-8aef8531ab61)

---

## Category
**Primary category:** Data integration
**Secondary tags:** blockchain, defi, bitquery, real-time analytics, risk management, smart contract, api, ai workflow
This solution bridges complex on-chain data with automated monitoring tools to provide actionable insights for decentralized finance ecosystems.

---

## Who is this for?
This workflow is designed for teams managing decentralized infrastructure who need to turn raw blockchain data into immediate operational intelligence.

* **Protocol Engineer**
    * Automates the detection of smart contract anomalies and potential security vulnerabilities before they escalate.
* **DeFi Analyst**
    * Streamlines the aggregation of liquidity and volume metrics across multiple chains into a unified dashboard.
* **Risk Manager**
    * Receives real-time alerts on protocol health, enabling faster decision-making during market volatility.
* **Community Manager**
    * Maintains transparency by providing accurate, up-to-date protocol performance data to stakeholders.

---

## Features
- **Real-time Blockchain Indexing**
  Leverages Bitquery’s high-speed indexing to pull live transaction and liquidity data directly into the workflow.
- **Automated Risk Alerting**
  Configurable thresholds trigger instant notifications when protocol health metrics deviate from established baselines.
- **Multi-Protocol Aggregation**
  Consolidates data from various decentralized exchanges and lending protocols into a single, cohesive view.
- **Smart Contract Monitoring**
  Tracks specific contract interactions and event logs to identify suspicious patterns or unexpected gas spikes.
- **Composio-Powered Integration**
  Uses the Composio Toolset to seamlessly connect blockchain data streams with external communication and reporting platforms.

---

## Use Cases
**Liquidity & Volume Tracking**
* Monitor total value locked (TVL) fluctuations across different liquidity pools in real-time.
* Track daily transaction volume to identify shifts in user adoption and protocol activity.

**Security & Anomaly Detection**
* Detect unusual whale movements or large-scale token transfers that may indicate market manipulation.
* Identify failed smart contract calls or high-frequency error logs that suggest potential exploit attempts.

**Operational Reporting**
* Generate automated daily summaries of protocol performance for internal stakeholder review.
* Sync key performance indicators (KPIs) to team communication channels for proactive incident response.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the DeFi Protocol Health Dashboard template from the marketplace.
3. Configure your Bitquery API credentials within the environment variables.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives user queries regarding specific protocol metrics or timeframes.
* **Agent**: Processes natural language requests and maps them to specific blockchain data queries.
* **Composio Toolset**: Executes the API calls to Bitquery and manages data formatting.
* **Chat Output**: Delivers the processed health report or alert summary back to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Check the current TVL and 24-hour volume for the Uniswap V3 pool on Ethereum.`
* `Are there any unusual transaction spikes in the last hour for our protocol contract?`
* `Generate a summary report of the top 5 liquidity providers for the current protocol.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the analytical engine, translating user intent into precise blockchain data requests.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are a DeFi data analyst. Use the provided tools to fetch real-time blockchain data and present it in a clear, professional format."
* Instruction: "Always prioritize accuracy; if data is unavailable, inform the user rather than hallucinating metrics."

### 2) Composio Toolset Node
* Requires a valid Bitquery API key with access to the GraphQL endpoints.
* Connection scope should be limited to read-only access for security.

### 3) Tool Availability
* **Bitquery Explorer**: For querying historical and real-time on-chain data.
* **Alert Manager**: For pushing notifications to Slack or email.
* **Data Formatter**: For converting raw JSON responses into human-readable tables or charts.

---

## Related Solutions
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks user engagement and platform activity metrics.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Aggregates external data for comprehensive account insights.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Ensures internal operational pipelines remain stable and performant.
