# Portfolio Risk Monitor (Uplizd) - Automated market risk assessment and financial intelligence

## Summary
The Portfolio Risk Monitor is an intelligent Uplizd workflow that automates the assessment of financial portfolio exposure by synthesizing real-time market data and technical indicators. By leveraging the Polygon.io API via the Composio Toolset, this solution enables investment analysts and portfolio managers to maintain a single source of truth for risk metrics, significantly increasing pipeline velocity and data hygiene in financial reporting.

---

## Demo
![Portfolio Risk Monitor dashboard showing automated risk assessment and market data integration](image.png)
**Alt text (SEO-ready):** Portfolio Risk Monitor dashboard showing automated risk assessment, financial data integration, Uplizd AI workflow, and market analysis using Polygon.io.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bcab2d91-e09e-5f05-ad38-999b287e9179)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** finance, portfolio management, risk assessment, polygon, market data, data integration, composio, ai workflow
- This solution bridges the gap between raw market data feeds and actionable risk intelligence for financial professionals.

---

## Who is this for?
This solution is designed for finance professionals who need to move beyond manual spreadsheet tracking to automated, real-time risk monitoring.

- **Portfolio Manager**
    - Automates daily risk exposure reports to ensure alignment with investment mandates.
- **Investment Analyst**
    - Quickly pulls technical indicators for specific assets to support data-driven decision-making.
- **Financial Operations Lead**
    - Maintains high-fidelity data hygiene across reporting pipelines by removing manual entry errors.
- **Risk Compliance Officer**
    - Monitors portfolio volatility thresholds to ensure adherence to internal risk policies.

---

## Features
- **Real-time Market Integration**
    - Seamlessly connects to Polygon.io to fetch live price, volume, and volatility data.
- **Automated Risk Scoring**
    - Calculates portfolio risk metrics dynamically based on current market conditions and asset allocation.
- **Intelligent Data Synthesis**
    - Uses the Agent node to interpret complex financial datasets and provide human-readable summaries.
- **Customizable Alerting**
    - Triggers notifications when specific portfolio assets breach predefined risk or volatility thresholds.
- **Composio-Powered Execution**
    - Leverages the Composio Toolset to securely manage API authentication and data retrieval workflows.

---

## Use Cases
**Portfolio Health Monitoring**
- Automatically flagging assets that deviate from target volatility ranges.
- Generating daily summary reports of total portfolio exposure across multiple sectors.

**Market Intelligence Gathering**
- Fetching historical price trends for specific tickers to inform rebalancing strategies.
- Correlating portfolio performance against broader market indices using real-time data.

**Compliance and Reporting**
- Automating the audit trail for risk assessment logs to satisfy regulatory requirements.
- Standardizing the format of risk reports for stakeholders using consistent AI-driven templates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Portfolio Risk Monitor solution.
2. Click "Import" to add the workflow template to your workspace.
3. Configure your environment variables, including your Polygon.io API key.
4. Ensure nodes are correctly connected in the builder: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the ticker symbols or portfolio parameters from the user.
- **Agent**: Processes market data and applies risk assessment logic.
- **Composio Toolset**: Executes secure API calls to retrieve financial data.
- **Chat Output**: Returns the final risk assessment and actionable insights to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Analyze the current risk profile for a portfolio containing AAPL, TSLA, and NVDA.`
- `What is the 30-day volatility trend for the current portfolio assets?`
- `Generate a risk summary report for my tech-heavy portfolio based on today's market close.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a financial analyst interpreting market data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate financial calculations.
- Instruct the agent to prioritize data accuracy and cite the technical indicators used.
- Configure the system prompt to maintain a professional, analytical tone.

### 2) Composio Toolset Node
- Provide your Polygon.io API key within the Composio configuration settings.
- Ensure the connection scope is limited to read-only access for market data endpoints.

### 3) Tool Availability
- **Market Data Fetcher**: Retrieves real-time price and volume.
- **Technical Indicator Calculator**: Computes moving averages, RSI, and volatility.
- **Portfolio Aggregator**: Consolidates individual asset data into a unified risk view.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automates financial account matching and reconciliation tasks.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enriches account data with external intelligence for better decision-making.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks the operational performance and status of automated business workflows.
