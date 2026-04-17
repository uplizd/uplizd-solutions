# Account Setup Agent (Uplizd) - Automated CRM account creation and relationship mapping

## Summary
The Account Setup Agent streamlines the complex process of initializing new business accounts within your CRM. By leveraging the Composio Toolset, this Uplizd AI workflow automatically populates account records, links key contacts, and establishes organizational hierarchies, ensuring data hygiene and accelerating pipeline velocity for sales and operations teams.

---

## Demo
![Account Setup Agent workflow showing automated CRM record creation and contact mapping](image.png)

**Alt text (SEO-ready):** Account Setup Agent workflow for automated CRM data entry, contact mapping, and account initialization using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bc6d7f8a-0a81-5702-b4ac-a982439945b1)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, salesforce, account management, data entry, pipeline, sales operations, composio, ai workflow
- This solution bridges the gap between raw prospect data and structured CRM records to eliminate manual administrative overhead.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to standardize their account entry processes.

- **Sales Operations Manager**
    - Ensures consistent data formatting and mandatory field completion across all new account records.
- **Account Executive**
    - Reduces time spent on manual data entry, allowing more focus on high-value discovery and relationship building.
- **Business Development Representative**
    - Automatically maps new leads to existing parent accounts to maintain a clean and organized sales hierarchy.
- **Revenue Operations Analyst**
    - Improves pipeline reporting accuracy by ensuring every account is correctly categorized and linked from day one.

---

## Features
- **Automated Record Creation**
    - Instantly generates new account profiles in your CRM based on provided company details.
- **Intelligent Contact Mapping**
    - Automatically associates individual contacts with the correct parent account to maintain relationship integrity.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely interface with leading CRM platforms like Salesforce and HubSpot.
- **Real-time Data Validation**
    - Checks for duplicate entries and missing information before finalizing the account setup process.
- **Customizable Field Mapping**
    - Allows for flexible configuration of CRM fields to match your organization's specific data requirements.

---

## Use Cases
**New Customer Onboarding**
- Automatically create a new account record when a contract is signed.
- Populate key firmographic data points such as industry, employee count, and annual revenue.

**Account Hierarchy Management**
- Link subsidiary offices to a global parent account automatically.
- Assign specific account owners based on territory or industry rules defined in the agent.

**Data Hygiene & Enrichment**
- Standardize address and contact formatting during the initial account creation phase.
- Flag incomplete account records for manual review by the sales operations team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your CRM connection via the Composio Toolset node.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives company name, website, and contact details from the user.
- **Agent**: Processes input data, performs entity resolution, and formats the CRM payload.
- **Composio Toolset**: Executes the API calls to create or update the account in your CRM.
- **Chat Output**: Confirms successful account creation and provides a link to the new record.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Create a new account for 'Acme Corp' with website 'acme.com' and assign it to the Enterprise sales team.`
- `Add 'Jane Doe' as a primary contact for the newly created 'Global Tech' account.`
- `Initialize a new account for 'Innovate Solutions' and map it as a subsidiary of 'Tech Holdings'.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data extraction and CRM interaction.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate field mapping.
- Instruction: "Extract company details, validate against CRM schema, and trigger creation tools."
- Instruction: "If information is missing, prompt the user for specific required fields before proceeding."

### 2) Composio Toolset Node
- Provide your Composio API key in the node settings.
- Ensure the connection scope includes `write` permissions for your target CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- `crm_create_account`: Creates the primary account record.
- `crm_add_contact`: Links contacts to the account.
- `crm_search_account`: Checks for existing records to prevent duplicates.
- `crm_update_field`: Modifies specific account attributes post-creation.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates deep-dive research on target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintains data consistency across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Tracks and manages opportunity stages and follow-ups.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriches account data with external signals.
