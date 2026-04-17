# Smart Fee Manager (Uplizd) - Dynamic proposal fee optimization and automated pricing adjustments

## Summary
The Smart Fee Manager by Uplizd is an intelligent workflow designed to automate the calculation and adjustment of proposal fees based on real-time market data and client parameters. By integrating directly with Bidsketch, this solution eliminates manual pricing errors, ensures competitive fee structures, and accelerates the proposal-to-close pipeline by providing a single source of truth for sales operations teams.

---

## Demo
![Smart Fee Manager workflow dashboard showing automated pricing adjustments and Bidsketch integration](image.png)
**Alt text (SEO-ready):** Smart Fee Manager Uplizd workflow, automated proposal pricing, Bidsketch fee optimization, sales operations automation, and dynamic fee management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bea3061a-af7e-57e1-9a60-9fc2d95c6833)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** bidsketch, pricing, proposal management, sales operations, revenue operations, automation, ai workflow, data sync
- This solution streamlines the quote-to-cash process by leveraging AI to align proposal fees with current market intelligence and business logic.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to standardize their pricing strategy and reduce administrative overhead in the proposal process.

- **Sales Managers**
    - Ensure consistent pricing policies across the team while allowing for data-driven adjustments.
- **Account Executives**
    - Reduce time spent on manual fee calculations and focus on closing deals with accurate, optimized quotes.
- **Revenue Operations (RevOps) Leads**
    - Maintain high data hygiene and pricing compliance within Bidsketch and connected CRM systems.
- **Finance Analysts**
    - Monitor fee trends and ensure that proposal pricing remains profitable against fluctuating market conditions.

---

## Features
- **Dynamic Fee Calculation**
    - Automatically adjust proposal line items based on predefined business rules and real-time market inputs.
- **Bidsketch Integration**
    - Seamlessly push optimized fee structures directly into Bidsketch proposals via the Composio Toolset.
- **Market-Aware Adjustments**
    - Incorporate external data signals to suggest price adjustments that maximize win rates without sacrificing margins.
- **Automated Compliance Checks**
    - Validate every fee calculation against organizational pricing floors and ceilings before proposal generation.
- **Real-time Sync**
    - Maintain a synchronized state between your pricing strategy and active client proposals to prevent outdated quotes.

---

## Use Cases
**Proposal Optimization**
- Automatically update service fees based on the complexity of the project scope defined in the client brief.
- Apply volume-based discounts dynamically when specific client tiers are identified in the CRM.

**Sales Pipeline Velocity**
- Reduce the turnaround time for proposal revisions by automating the re-calculation of fees during negotiations.
- Trigger automated fee alerts to sales leadership when a proposal deviates from standard profit margins.

**Data Hygiene & Reporting**
- Standardize fee naming conventions and categorization across all Bidsketch documents for cleaner financial reporting.
- Audit historical proposal data to identify pricing trends and improve future fee strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Fee Manager template file provided in this repository.
3. Connect your Bidsketch account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the project scope and client details from the user.
- **Agent**: Processes the input, applies pricing logic, and determines the optimal fee.
- **Composio Toolset**: Executes the API calls to update or create the fee structure in Bidsketch.
- **Chat Output**: Confirms the fee adjustment and provides a summary of the proposal status.

### 3) Run the Flow
Use the Playground to test your pricing logic with these prompts:
- `Calculate the fee for a standard web design project with 3 additional landing pages.`
- `Adjust the proposal fee for Client X based on the current high-tier pricing strategy.`
- `Review the current Bidsketch draft and apply a 10% discount for the annual contract option.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the pricing engine, interpreting business requirements and applying logic.
- **Recommended instruction pattern:**
    - Define the pricing floor and ceiling constraints clearly in the system prompt.
    - Instruct the agent to prioritize margin protection while remaining competitive.
    - Require the agent to output a structured JSON summary of all fee changes for audit purposes.

### 2) Composio Toolset Node
- **API Key**: Ensure your Bidsketch API key is securely stored in the Uplizd environment variables.
- **Connection Scope**: Grant the toolset read/write permissions for "Proposals" and "Clients" to allow for accurate data retrieval and updates.

### 3) Tool Availability
- **Bidsketch.get_proposal**: Retrieve current fee details for existing drafts.
- **Bidsketch.update_proposal_fees**: Push calculated adjustments to the platform.
- **CRM.get_client_data**: Fetch client-specific pricing tiers or historical contract data.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) — Automate financial reconciliation and ledger updates.
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) — Streamline new account creation and CRM data entry.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) — Manage deal stages and follow-up automation for sales teams.
