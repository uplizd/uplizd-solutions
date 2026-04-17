# Account Mapping Agent (Uplizd) - Automate account hierarchy and relationship data synchronization

## Summary
The Account Mapping Agent is an intelligent Uplizd workflow designed to automate the discovery, mapping, and synchronization of complex account hierarchies and business relationships. By leveraging the Composio Toolset to interface with your CRM, this solution eliminates manual data entry, ensures a single source of truth for organizational structures, and significantly improves pipeline velocity by surfacing hidden cross-sell opportunities within parent-child account networks.

---

## Demo
![Account Mapping Agent workflow diagram showing CRM data integration and hierarchy visualization](image.png)
**Alt text (SEO-ready):** Account Mapping Agent workflow diagram showing CRM data integration and hierarchy visualization for Uplizd automated account relationship management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLFj4Q89245QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZ4AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfoCxQWDiQ5V15WAAAALUlEQVQ4y2P8z8AARkBCwAATQhYfA0YNGDUg1IBRA0YNGDUg1IBRA0YNGDUg1IAAAJ5uBf8y6/4AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/f95d161b-ccd8-50be-b604-f8c12059c173)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, account mapping, data sync, pipeline, relationship management, composio, ai workflow, data hygiene
- This solution streamlines the complex process of mapping organizational structures, ensuring your CRM data remains accurate and actionable for sales and operations teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maintain clean, interconnected account data across their enterprise tech stack.

- **Sales Operations Manager**
    - Automates the maintenance of account hierarchies, reducing manual data cleanup time by hours each week.
- **Account Executive**
    - Gains immediate visibility into parent-child relationships to identify upsell and cross-sell opportunities.
- **RevOps Analyst**
    - Ensures data integrity across CRM platforms by standardizing how account relationships are recorded and synced.
- **Sales Manager**
    - Monitors account health and coverage across large enterprise organizations with automated reporting and alerts.

---

## Features
- **Automated Hierarchy Discovery**
    - Uses AI to scan and map complex organizational structures, identifying parent-child relationships automatically.
- **Real-time CRM Synchronization**
    - Leverages the Composio Toolset to push relationship updates directly into your CRM, ensuring data is always current.
- **Conflict Resolution Engine**
    - Intelligent logic to detect and resolve discrepancies in account data, preventing duplicate entries or broken hierarchies.
- **Cross-Platform Integration**
    - Seamlessly connects with leading CRM platforms to pull and push account intelligence without manual intervention.
- **Relationship Scoring**
    - Analyzes account activity to score the strength of relationships, helping teams prioritize high-value engagement.

---

## Use Cases
**Enterprise Account Expansion**
- Automatically link subsidiary accounts to a parent record to consolidate total addressable market (TAM) views.
- Trigger alerts for sales teams when a new subsidiary is identified within an existing enterprise account network.

**CRM Data Hygiene**
- Identify and merge orphaned account records that lack proper hierarchy associations.
- Standardize naming conventions and relationship fields across global account databases.

**Pipeline Intelligence**
- Map key stakeholders and decision-makers across multiple linked accounts to improve deal closure rates.
- Surface hidden connections between accounts to facilitate warm introductions and multi-threaded sales strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Account Mapping Agent to your workspace.
3. Configure your API credentials within the integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives account names or CRM record IDs to initiate the mapping process.
- **Agent**: Processes the account hierarchy logic and determines necessary data updates.
- **Composio Toolset**: Executes read/write operations to your CRM to fetch and update account data.
- **Chat Output**: Returns a summary of the mapped hierarchy and any actions taken in the CRM.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Map the hierarchy for 'Global Tech Corp' and link all identified subsidiaries.`
- `Find and resolve any orphaned accounts associated with the 'Acme Inc' parent record.`
- `Identify cross-sell opportunities within the 'Beta Solutions' account network based on current hierarchy data.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst and CRM administrator.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are an expert CRM data administrator. Your goal is to map account hierarchies accurately and maintain data integrity."
- Instruction: "Always verify existing relationships before creating new links to prevent duplication."

### 2) Composio Toolset Node
- Provide your CRM API key (e.g., Salesforce, HubSpot, or Dynamics 365).
- Ensure the connection scope includes read/write access to Account and Contact objects.

### 3) Tool Availability
- **CRM Search**: Capability to query account records by name, domain, or ID.
- **Relationship Update**: Ability to modify parent-child fields and link records.
- **Data Validation**: Logic to check for existing records before performing bulk updates.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into target accounts and organizational structures.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms to maintain a single source of truth.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-ups to optimize sales pipeline velocity.
