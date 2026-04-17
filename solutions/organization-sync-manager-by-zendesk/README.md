# Organization Sync Manager (Uplizd) - Automated cross-platform account data synchronization

## Summary
The Organization Sync Manager is an intelligent Uplizd workflow designed to maintain a single source of truth for customer organization data across your business systems. By leveraging the Composio Toolset to bridge Zendesk and your CRM, this solution eliminates manual data entry, reduces record duplication, and ensures that account-level information remains consistent and up-to-date across your entire operational stack.

---

## Demo
![Organization Sync Manager workflow showing data flow from Zendesk to CRM via Uplizd](image.png)
**Alt text (SEO-ready):** Uplizd Organization Sync Manager workflow automating data synchronization between Zendesk and CRM systems for improved data hygiene and pipeline velocity.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/461f2d92-ea5f-5866-8fb2-85dc3224358d)

---

## Category
**Primary category:** Data integration  
**Secondary tags:** crm, zendesk, data sync, data hygiene, operations, automation, composio, ai workflow  
This solution streamlines organizational data management by automating the bidirectional flow of account information between support and sales platforms.

---

## Who is this for?
This solution is designed for operations teams and account managers who need to maintain clean, synchronized customer data without manual intervention.

* **RevOps Manager**
    * Ensures data consistency across the tech stack to improve reporting accuracy and pipeline visibility.
* **Customer Success Lead**
    * Keeps account profiles updated in real-time, allowing for personalized support and proactive engagement.
* **Sales Operations Specialist**
    * Automates the reconciliation of organization records between Zendesk and CRM platforms to prevent fragmented account views.
* **Support Manager**
    * Reduces administrative overhead by syncing ticket-related organization updates back to the primary CRM automatically.

---

## Features
- **Real-time Data Sync**
  Automatically propagates organization updates from Zendesk to your CRM as soon as changes occur.
- **Conflict Resolution**
  Intelligently handles data discrepancies between systems to ensure the most accurate record is preserved.
- **Automated Hygiene**
  Detects and merges duplicate organization records, maintaining a clean and searchable database.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely authenticate and execute API calls across Zendesk and CRM environments.
- **Audit Logging**
  Tracks all synchronization events, providing transparency into data changes and system interactions.

---

## Use Cases
**Data Consistency**
* Syncing new organization names and domains from Zendesk tickets directly into the CRM.
* Updating account status fields across platforms when a support tier changes.

**Operational Efficiency**
* Automating the creation of CRM accounts for new organizations identified in Zendesk.
* Reducing manual data entry time by mapping custom fields between support and sales tools.

**Account Intelligence**
* Aggregating support interaction history into the CRM to provide a 360-degree view of the customer.
* Triggering alerts in the CRM when high-value organizations reach specific support milestones.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Organization Sync Manager template from the solution library.
3. Connect your Zendesk and CRM accounts via the integration settings.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives triggers or manual requests to initiate organization synchronization.
* **Agent**: Processes the data mapping logic and determines the necessary API actions.
* **Composio Toolset**: Executes the read/write operations between Zendesk and your CRM.
* **Chat Output**: Confirms the successful sync or reports any errors encountered during the process.

### 3) Run the Flow
Use the Playground to test the synchronization logic with these prompts:
* `Sync the organization details for domain 'example.com' from Zendesk to Salesforce.`
* `Check for and merge duplicate organization records between Zendesk and HubSpot.`
* `Update the account status for all organizations in the CRM based on recent Zendesk ticket activity.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer, interpreting data schemas and mapping fields.
* Use a model capable of structured JSON output for reliable data mapping.
* Instruction: "You are a data synchronization assistant. Map organization fields accurately between Zendesk and the CRM."
* Instruction: "Prioritize CRM data as the source of truth for account status, and Zendesk for contact-level updates."

### 2) Composio Toolset Node
* Provide your API keys for both Zendesk and your target CRM.
* Ensure the connection scope includes read/write permissions for Organizations, Accounts, and Contacts.

### 3) Tool Availability
* **Zendesk API**: Retrieve organization details, list tickets, and update organization metadata.
* **CRM API**: Create, update, and search for account records.
* **Data Mapping Utility**: Transform field formats to ensure compatibility between disparate systems.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize records across multiple CRM platforms.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate data cleanup and formatting for CRM records.
* [Account Research Agent](../account-research-agent/README.md) — Gather and enrich account intelligence from external sources.
