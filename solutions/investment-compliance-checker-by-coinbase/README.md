# Investment Compliance Checker (Uplizd) - Automated cryptocurrency policy verification and risk monitoring

## Summary
The Investment Compliance Checker is an intelligent Uplizd workflow designed to automate the verification of cryptocurrency holdings against predefined investment policies and regulatory frameworks. By leveraging the Composio Toolset to interface with financial data, this solution provides investment firms and compliance officers with a single source of truth, ensuring portfolio hygiene, mitigating regulatory risk, and accelerating audit readiness through real-time automated oversight.

---

## Demo
![Investment Compliance Checker workflow showing automated policy verification and risk reporting](image.png)
**Alt text (SEO-ready):** Uplizd Investment Compliance Checker workflow for automated cryptocurrency policy verification, risk monitoring, and financial data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/eac0fb94-841c-5152-9f69-22974fbbc4c6)

---

## Category
**Primary category:** Legal and Compliance
**Secondary tags:** crypto, investment, compliance, risk management, financial data, audit, composio, ai workflow
This solution bridges the gap between complex investment mandates and real-time asset tracking to ensure continuous regulatory adherence.

---

## Who is this for?
This solution is designed for financial professionals who need to maintain strict adherence to investment mandates while managing volatile digital assets.

*   **Compliance Officer**
    *   Automates the monitoring of portfolio holdings against internal risk thresholds and external regulatory requirements.
*   **Portfolio Manager**
    *   Receives real-time alerts when asset allocations drift outside of defined policy boundaries.
*   **Internal Auditor**
    *   Generates consistent, timestamped compliance reports for periodic reviews and regulatory filings.
*   **Operations Analyst**
    *   Reduces manual data reconciliation efforts by connecting disparate financial data sources into a unified verification pipeline.

---

## Features
- **Policy-Driven Verification**
    Automated logic that cross-references current cryptocurrency holdings against specific investment policy constraints.
- **Real-Time Risk Alerts**
    Instant notification triggers when portfolio deviations or policy breaches are detected within the monitored accounts.
- **Composio Toolset Integration**
    Seamless connectivity with financial APIs and data providers to fetch accurate, up-to-date asset information.
- **Audit-Ready Reporting**
    Structured output generation that logs verification results, providing a clear trail for compliance documentation.
- **Dynamic Threshold Monitoring**
    Configurable parameters that allow users to adjust risk tolerance levels and asset concentration limits as policies evolve.

---

## Use Cases
**Policy Enforcement**
*   Automatically flag portfolios that exceed maximum exposure limits for specific high-volatility tokens.
*   Verify that all held assets comply with the firm's approved "whitelist" of investable cryptocurrencies.

**Risk Management**
*   Monitor daily portfolio drift to identify potential breaches of diversification mandates.
*   Analyze historical compliance data to identify recurring patterns of policy non-adherence.

**Audit and Reporting**
*   Generate automated monthly compliance summaries for stakeholders and regulatory bodies.
*   Perform ad-hoc verification checks on new accounts before they are integrated into the primary investment pool.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the Investment Compliance Checker to your Uplizd workspace.
3. Connect your required financial data sources via the Composio Toolset configuration.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API credentials are active.

### 2) Setup the Nodes
*   **Chat Input**: Receives the portfolio data or specific compliance query from the user.
*   **Agent**: Processes the input, applies logic based on the investment policy, and determines if a breach has occurred.
*   **Composio Toolset**: Executes secure calls to fetch real-time asset data and market valuations.
*   **Chat Output**: Delivers the final compliance status report and any necessary risk alerts.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
* `Check current portfolio holdings against the Q3 investment policy constraints.`
* `Are there any assets in the portfolio that are not on the approved whitelist?`
* `Generate a risk compliance report for the last 30 days of trading activity.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the compliance engine, interpreting policy documents and comparing them against live data.
* Use a model with high reasoning capabilities to ensure accurate interpretation of complex policy language.
* Instruct the agent to prioritize "Safety First" when evaluating potential policy breaches.
* Configure the system prompt to output findings in a standardized JSON format for easier auditing.

### 2) Composio Toolset Node
* Provide the necessary API keys for your financial data providers.
* Ensure the connection scope is limited to read-only access for portfolio data to maintain security.

### 3) Tool Availability
* **Asset Retrieval**: Capability to fetch balance and transaction history from connected exchanges.
* **Policy Validator**: Logic module for comparing asset lists against the approved whitelist.
* **Alerting Service**: Ability to trigger notifications via email or internal messaging platforms.

---

## Related Solutions
* [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial data matching and ledger balancing.
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Track and maintain account status and regulatory health.
* [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Audit user permissions and access logs for security compliance.
