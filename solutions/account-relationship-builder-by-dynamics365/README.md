# Account Relationship Builder (Uplizd) - Automate CRM account mapping and profile enrichment

## Summary
The Account Relationship Builder is an intelligent Uplizd workflow designed to automate the discovery, mapping, and enrichment of complex account structures within Microsoft Dynamics 365. By leveraging the Composio Toolset, this solution eliminates manual data entry, ensuring that account hierarchies, stakeholder relationships, and firmographic data remain accurate and actionable, ultimately driving higher pipeline velocity and improved CRM hygiene for sales and operations teams.

---

## Demo
![Account Relationship Builder workflow diagram showing Dynamics 365 integration and automated data enrichment](../image.png)
**Alt text (SEO-ready):** Account Relationship Builder Uplizd workflow for Dynamics 365 CRM data enrichment, account mapping, and automated stakeholder relationship management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0379353c-4ffb-50a7-be2c-cc211c786094)

---

## Category
- **Primary category:** CRM data
- **Secondary tags:** dynamics365, account mapping, relationship management, data enrichment, sales operations, composio, ai workflow
- This solution bridges the gap between raw account data and strategic relationship intelligence through automated CRM synchronization.

---

## Who is this for?
This solution is built for revenue-focused teams managing complex B2B accounts and enterprise sales cycles.

- **Account Executive**
    - Spend less time on manual data entry and more time engaging with key stakeholders identified by the AI.
- **Sales Operations Manager**
    - Maintain high-quality CRM data hygiene by automating the reconciliation of account hierarchies and contact records.
- **Customer Success Manager**
    - Gain a holistic view of account health by automatically mapping new contacts and relationship touchpoints.
- **Revenue Operations (RevOps) Lead**
    - Standardize account profile enrichment processes across the organization to ensure consistent reporting and forecasting.

---

## Features
- **Automated Account Mapping**
    - Intelligently links disparate contacts to parent accounts in Dynamics 365, building a clear organizational structure.
- **Real-time Data Enrichment**
    - Automatically pulls firmographic data and updates account fields to ensure the CRM remains the single source of truth.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely execute read/write operations directly within your Microsoft Dynamics 365 environment.
- **Relationship Visualization**
    - Identifies and flags key decision-makers and influencers, helping teams prioritize their outreach efforts.
- **Proactive Hygiene Alerts**
    - Detects missing information or stale account profiles and triggers updates to maintain data integrity.

---

## Use Cases
**Enterprise Account Mapping**
- Automatically associate new leads with existing account hierarchies to prevent duplicate records.
- Map multi-subsidiary relationships to ensure comprehensive coverage of large enterprise clients.

**Sales Intelligence Enrichment**
- Populate empty CRM fields with verified firmographic data retrieved during the account research phase.
- Flag high-value stakeholders and add them to the account relationship map for better visibility.

**CRM Data Hygiene**
- Identify and merge redundant account entries that share similar domains or legal entities.
- Regularly audit account profiles to ensure contact information is current and aligned with recent interactions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Connect your Microsoft Dynamics 365 account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the account name or domain to be processed.
- **Agent**: Analyzes the input and determines the necessary CRM actions.
- **Composio Toolset**: Executes the specific Dynamics 365 API calls to fetch or update records.
- **Chat Output**: Returns a summary of the enrichment or mapping actions performed.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Map all contacts associated with the domain 'acme-corp.com' to the primary account in Dynamics 365.`
- `Enrich the profile for 'Global Tech Solutions' with the latest firmographic data.`
- `Identify and link all stakeholders for the 'Project Alpha' account.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for CRM data operations.
- Instruct the agent to prioritize data accuracy and verify account IDs before performing updates.
- Use a structured output format to ensure the Composio Toolset receives clean parameters.
- Enable "Tool Use" mode to allow the agent to autonomously select the correct CRM functions.

### 2) Composio Toolset Node
- Provide your valid Dynamics 365 API credentials within the Composio configuration.
- Set the connection scope to include read/write permissions for Accounts, Contacts, and Leads.

### 3) Tool Availability
- **Search Accounts**: Locate existing account records by name or domain.
- **Update Account Fields**: Modify specific CRM fields with enriched data.
- **Link Contact to Account**: Establish formal relationships between entities.
- **Fetch Account Hierarchy**: Retrieve existing parent-child account structures.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize account data across multiple platforms.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Streamline the creation of new account profiles in your CRM.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Track and manage deal stages and opportunity health.
