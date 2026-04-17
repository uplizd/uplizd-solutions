# Policy Data Enricher (Uplizd) - Automated insurance policy and driver intelligence

## Summary
The Policy Data Enricher by Uplizd automates the ingestion and enhancement of insurance policy records by synchronizing vehicle and driver details directly into your CRM. By leveraging the Composio Toolset to bridge AgencyZoom with your core data systems, this workflow eliminates manual entry, reduces data decay, and ensures that underwriting and sales teams have a single source of truth for every policyholder.

---

## Demo
![Policy Data Enricher workflow diagram showing AgencyZoom data flow into CRM](image.png)
**Alt text (SEO-ready):** Uplizd Policy Data Enricher workflow diagram showing automated AgencyZoom vehicle and driver data synchronization for insurance CRM enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7811f3a8-3f5e-57a3-b45a-e7a9a258af8c)

---

## Category
**Primary category:** Data integration
**Secondary tags:** insurance, agencyzoom, crm, data enrichment, policy management, automation, composio, ai workflow
This solution streamlines insurance operations by automating the enrichment of policy data, ensuring high-fidelity records across your entire sales and service stack.

---

## Who is this for?
This solution is designed for insurance professionals and operations teams looking to minimize manual data entry and improve record accuracy.

*   **Insurance Agents**
    *   Spend less time on administrative data entry and more time on client consultations.
*   **Operations Managers**
    *   Maintain high-quality, standardized policy data across all internal systems.
*   **Underwriting Assistants**
    *   Access real-time vehicle and driver profiles without switching between multiple platforms.
*   **RevOps Specialists**
    *   Ensure data hygiene and pipeline velocity by automating the flow of information from AgencyZoom.

---

## Features
- **Automated Data Enrichment**
  Instantly pull vehicle and driver details from AgencyZoom and map them to your CRM records.
- **Real-time Sync**
  Trigger updates automatically whenever a new policy is created or modified, ensuring zero latency in data availability.
- **Composio Toolset Integration**
  Utilizes robust API connectors to securely bridge AgencyZoom with your existing CRM and database infrastructure.
- **Data Hygiene Standardization**
  Automatically formats and validates incoming policy information to prevent duplicate entries and formatting errors.
- **Intelligent Agent Logic**
  The Agent node intelligently interprets policy documents and extracts key entities to populate the correct CRM fields.

---

## Use Cases
**Policy Lifecycle Management**
*   Automatically update driver history logs when a policy renewal or endorsement is processed in AgencyZoom.
*   Sync vehicle identification numbers (VIN) and safety ratings to CRM opportunity records for better risk assessment.

**Sales Pipeline Optimization**
*   Populate lead profiles with existing policy data to provide agents with immediate context during cross-sell opportunities.
*   Flag incomplete policy records for manual review when essential driver information is missing from the source.

**Operational Compliance**
*   Maintain an audit-ready database by ensuring every policy change is logged and enriched with current driver data.
*   Automate the reconciliation of policyholder information between AgencyZoom and secondary storage systems.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Policy Data Enricher template from the solution library.
3. Authenticate your AgencyZoom and CRM accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual request to enrich a specific policy.
*   **Agent**: Processes the raw data, identifies missing fields, and structures the update payload.
*   **Composio Toolset**: Executes the API calls to fetch AgencyZoom data and push updates to the CRM.
*   **Chat Output**: Confirms the successful enrichment and provides a summary of updated fields.

### 3) Run the Flow
Use the Playground to test your configuration with these example prompts:
* `Enrich policy #12345 with the latest driver and vehicle details from AgencyZoom.`
* `Check for missing driver information on all new policies created in the last 24 hours.`
* `Sync vehicle safety data for the current opportunity record in the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data mapping and validation.
*   **Instruction Pattern:**
    *   Identify the policy ID from the input and query the AgencyZoom API.
    *   Compare retrieved data against existing CRM fields to identify gaps.
    *   Format the output payload to match the CRM's schema requirements.

### 2) Composio Toolset Node
Requires a valid API key for AgencyZoom and your CRM. Ensure the connection scope includes read/write permissions for policy and contact objects.

### 3) Tool Availability
*   **AgencyZoom Connector**: Fetch policy, driver, and vehicle metadata.
*   **CRM Connector**: Update contact records, opportunity fields, and custom objects.
*   **Data Validator**: Ensure VINs and driver license formats meet standard requirements.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on accounts and leads.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize multi-platform data with conflict resolution.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex business processes across various platforms.
