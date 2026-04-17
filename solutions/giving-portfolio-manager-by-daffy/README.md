# Giving Portfolio Manager (Uplizd) - Automated donor-advised fund rebalancing and strategic giving optimization

## Summary
The Giving Portfolio Manager is an intelligent Uplizd workflow designed to streamline donor-advised fund (DAF) management by automating portfolio rebalancing and strategic grant distribution. By leveraging AI-driven insights, this solution helps philanthropic organizations and individual donors maintain optimal asset allocation, track charitable impact, and ensure timely grant execution, ultimately increasing pipeline velocity and operational hygiene for your giving portfolio.

---

## Demo
![Giving Portfolio Manager dashboard showing automated rebalancing and grant distribution status](image.png)
**Alt text (SEO-ready):** Giving Portfolio Manager Uplizd workflow dashboard for automated donor-advised fund rebalancing, grant distribution, and charitable impact tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7f610886-ea5f-5052-ac03-cc9fe7ce32d0)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** philanthropy, daf, asset management, grant distribution, data hygiene, composio, ai workflow
- This solution bridges the gap between financial portfolio management and charitable impact by automating the administrative overhead of donor-advised funds.

---

## Who is this for?
This solution is designed for professionals managing complex philanthropic portfolios who need to balance financial strategy with timely grant execution.

- **Philanthropy Managers**
    - Automate the recurring grant distribution process to ensure funds are deployed according to annual targets.
- **Financial Advisors**
    - Monitor donor-advised fund balances and trigger rebalancing alerts to maintain target asset allocations.
- **Non-Profit Operations Leads**
    - Streamline the verification of incoming grant data and maintain clean records across your donor database.
- **Individual Donors**
    - Gain real-time visibility into portfolio performance and receive proactive suggestions for strategic giving opportunities.

---

## Features
- **Automated Rebalancing**
    - Real-time monitoring of fund allocations with automated triggers to adjust holdings based on predefined strategic thresholds.
- **Grant Distribution Engine**
    - Seamless execution of grant requests via the Composio Toolset, ensuring compliance and timely delivery to recipient organizations.
- **Impact Tracking Dashboard**
    - Centralized view of all charitable contributions, providing a single source of truth for historical giving and future commitments.
- **Data Hygiene Automation**
    - Intelligent cleanup of donor and recipient records, ensuring that contact information and tax documentation remain accurate and audit-ready.
- **Strategic Insight Generation**
    - AI-powered analysis of giving patterns to suggest optimal timing and recipients for future charitable distributions.

---

## Use Cases
**Portfolio Optimization**
- Automatically rebalance DAF assets when market fluctuations cause a drift from the target investment strategy.
- Generate monthly performance reports that highlight the alignment between current holdings and philanthropic goals.

**Grant Lifecycle Management**
- Execute bulk grant distributions to pre-approved non-profit organizations at the end of each fiscal quarter.
- Track the status of pending grants from submission through to final disbursement and receipt acknowledgment.

**Donor & Recipient Data Hygiene**
- Sync donor contact details across CRM platforms to ensure all stakeholders receive accurate tax and impact reporting.
- Validate recipient non-profit status and banking information automatically before processing high-value grant requests.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your preferred CRM and financial data sources via the Composio Toolset.
3. Configure the environment variables for your specific DAF provider or financial API.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding portfolio status or grant requests.
- **Agent**: Processes instructions, evaluates portfolio data, and determines the necessary actions.
- **Composio Toolset**: Executes secure API calls to your financial and CRM platforms to fetch data or trigger transactions.
- **Chat Output**: Delivers a summary of actions taken, portfolio updates, or confirmation of grant execution.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Rebalance my portfolio to match the 60/40 growth strategy.`
- `List all pending grants for this quarter and verify the recipient status.`
- `Generate a summary of my total charitable impact for the current fiscal year.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical core, interpreting financial data and orchestrating tool usage.
- **Recommended instruction pattern:**
    - Act as a precise financial operations assistant focused on DAF management.
    - Always verify account balances before initiating any grant distribution commands.
    - Maintain a professional, objective tone when reporting on portfolio performance and impact metrics.

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and has the required scopes for your financial and CRM integrations.
- **Connection Scope**: Grant the agent access to read-only financial data and write-access for grant distribution endpoints.

### 3) Tool Availability
- **Financial Data Fetchers**: Retrieve real-time fund balances and asset allocation data.
- **CRM Connectors**: Update donor records and sync grant history.
- **Notification Services**: Send automated alerts for rebalancing events or grant status updates.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-ups for high-value opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize multi-platform data with conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate bulk data cleanup and compliance-aware formatting.
