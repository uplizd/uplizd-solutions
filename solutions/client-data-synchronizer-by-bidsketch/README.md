# Client Data Synchronizer (Uplizd) - Automated cross-platform client information management

## Summary
The Client Data Synchronizer (Uplizd) is an intelligent automation workflow designed to maintain a single source of truth for client records across disparate business systems. By leveraging the Composio Toolset to bridge Bidsketch and your primary CRM, this solution eliminates manual data entry, reduces record discrepancies, and ensures your sales and operations teams are always working with the most current client information.

---

## Demo
![Client Data Synchronizer workflow diagram showing Bidsketch integration with CRM systems](image.png)
**Alt text (SEO-ready):** Client Data Synchronizer (Uplizd) workflow diagram showing Bidsketch and CRM data integration for automated client record synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6757415d-865d-5b23-aded-cbb13d5f8c60)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** crm, bidsketch, data sync, automation, client management, composio, ai workflow, data hygiene
- This solution bridges the gap between proposal software and CRM platforms to ensure consistent client data across your entire tech stack.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual administrative overhead and improve data accuracy.

- **Sales Operations Manager**
    - Automates the flow of client data from proposals to the CRM to ensure pipeline visibility.
- **Account Executive**
    - Reduces time spent on manual data entry, allowing more focus on closing deals.
- **RevOps Specialist**
    - Maintains high-quality data hygiene by preventing duplicate records across integrated platforms.
- **Customer Success Lead**
    - Ensures that client contact information is always up-to-date for seamless onboarding and support.

---

## Features
- **Bidsketch-to-CRM Sync**
    - Automatically maps client details from finalized proposals directly into your CRM database.
- **Real-time Data Updates**
    - Triggers synchronization immediately upon proposal acceptance to keep records current.
- **Intelligent Conflict Resolution**
    - Uses AI logic to identify and merge duplicate records based on email or company identifiers.
- **Custom Field Mapping**
    - Allows for granular control over which data points are synced between Bidsketch and your CRM.
- **Audit Logging**
    - Tracks every synchronization event to ensure compliance and easy troubleshooting of data flows.

---

## Use Cases
**Proposal-to-CRM Automation**
- Automatically create new CRM accounts when a Bidsketch proposal is marked as 'Accepted'.
- Update existing client contact details in the CRM whenever a proposal is updated with new information.

**Data Hygiene & Maintenance**
- Identify and merge duplicate client entries created by manual entry errors.
- Standardize address and phone number formatting across all synced client records.

**Sales Pipeline Enrichment**
- Populate CRM opportunity fields with data extracted from signed proposal documents.
- Sync proposal value and expiration dates to keep sales forecasts accurate in real-time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and click "Import Flow."
3. Authenticate your Bidsketch and CRM accounts within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event from Bidsketch or manual sync requests.
- **Agent**: Processes the data mapping and determines the necessary CRM update actions.
- **Composio Toolset**: Executes the API calls to read Bidsketch data and write to the CRM.
- **Chat Output**: Confirms the successful synchronization of client records.

### 3) Run the Flow
Use the Playground to test the synchronization:
- `Sync the latest accepted proposal from Bidsketch to Salesforce.`
- `Check for duplicate client records between Bidsketch and HubSpot.`
- `Update the primary contact email for client ID 12345 based on the latest proposal.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data transformation and API selection.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Extract client name, email, and company from the Bidsketch payload and map them to the corresponding CRM fields."
- Instruction: "If a conflict is detected, prioritize the most recently updated record."

### 2) Composio Toolset Node
- Provide your API keys for both Bidsketch and your target CRM.
- Set the connection scope to allow 'Read' access for Bidsketch and 'Write' access for the CRM.

### 3) Tool Availability
- **Bidsketch API**: For fetching proposal and client data.
- **CRM API (Salesforce/HubSpot)**: For creating, updating, and searching client records.
- **Data Transformer**: For normalizing string formats and mapping fields.

---

## Related Solutions
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - General purpose multi-platform CRM synchronization.
- [Account Research Agent](../account-research-agent/README.md) - Enriches client records with external intelligence.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages deal stages and follow-up automation.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and deduplication for CRM databases.
