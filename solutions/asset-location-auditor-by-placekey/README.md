# Asset Location Auditor (Uplizd) - Automated physical asset verification and inventory compliance

## Summary
The Asset Location Auditor is an intelligent Uplizd workflow that automates the verification of physical asset locations by cross-referencing real-time data with Placekey. Designed for operations teams and facility managers, this solution ensures data hygiene, reduces manual audit overhead, and maintains a single source of truth for distributed inventory, significantly increasing pipeline velocity for asset management tasks.

---

## Demo
![Asset Location Auditor workflow diagram showing Placekey integration for physical inventory verification](../image.png)
**Alt text (SEO-ready):** Uplizd Asset Location Auditor workflow, automated inventory verification, Placekey data integration, physical asset tracking, and operations data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f8e95288-2b1a-5ded-ac64-6f43402a17cc)

---

## Category
**Primary category:** Operations
**Secondary tags:** inventory, placekey, data hygiene, asset management, compliance, automation, composio, ai workflow.
This solution streamlines physical asset tracking by leveraging geospatial intelligence to ensure location data remains accurate and audit-ready.

---

## Who is this for?
This workflow is designed for professionals responsible for maintaining accurate physical records and operational oversight.

* **Operations Manager**
    * Automates the reconciliation of asset locations to reduce manual audit time and human error.
* **Inventory Controller**
    * Maintains a real-time, accurate ledger of distributed assets across multiple physical sites.
* **Compliance Officer**
    * Ensures all physical assets meet regulatory location requirements through automated verification logs.
* **Facilities Coordinator**
    * Identifies discrepancies in asset placement quickly to prevent loss and optimize resource allocation.

---

## Features
- **Automated Location Verification**
  Uses Placekey to standardize and validate physical addresses against global location databases.
- **Real-time Data Sync**
  Integrates with your existing inventory management systems via the Composio Toolset to push updates instantly.
- **Discrepancy Alerting**
  Automatically flags assets that do not match recorded location data for immediate human review.
- **Audit-Ready Reporting**
  Generates clean, formatted logs of all verification activities for compliance and internal reporting.
- **Scalable Batch Processing**
  Handles large volumes of asset records efficiently, ensuring consistent data hygiene across the entire organization.

---

## Use Cases
**Physical Inventory Audits**
* Automate the verification of warehouse asset locations during quarterly stock takes.
* Flag missing or misplaced items by comparing real-time site data against the master inventory list.

**Compliance & Regulatory Reporting**
* Ensure all high-value equipment is logged at authorized locations to meet insurance and safety standards.
* Generate automated location history reports for assets subject to strict regulatory oversight.

**Operational Data Hygiene**
* Standardize inconsistent location naming conventions across disparate facility databases.
* Enrich existing asset records with precise Placekey identifiers to improve spatial analysis accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Asset Location Auditor template from the marketplace.
3. Connect your required API credentials (Placekey and Inventory CRM) within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the asset ID and current location data for verification.
* **Agent**: Analyzes the input, triggers the verification logic, and interprets the Placekey response.
* **Composio Toolset**: Executes the API calls to validate coordinates and update the inventory database.
* **Chat Output**: Returns the verification status and any necessary correction actions to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Verify the current location of asset ID #99283 and update the record if the address is malformed.`
* `Run a compliance audit on all assets currently assigned to the North Warehouse.`
* `Check for location discrepancies for the latest batch of imported inventory items.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for your audit process.
* Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5).
* Instruction: "You are an asset auditor. Use the provided tools to verify location accuracy and report discrepancies."
* Instruction: "If an asset location is ambiguous, prioritize Placekey standardization before flagging for manual review."

### 2) Composio Toolset Node
* Provide your API key for the relevant inventory management platform.
* Ensure the connection scope includes read/write permissions for asset location fields.

### 3) Tool Availability
* **Placekey API**: For address standardization and geospatial verification.
* **Inventory CRM Connector**: For fetching and updating asset location records.
* **Logging Tool**: For recording audit results and discrepancy flags.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Automates security and configuration audits for cloud infrastructure.
* [Address Verification Agent](../address-verification-agent-by-addresszen/README.md) — Validates and cleans customer address data for shipping and billing.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks the performance and status of automated operational workflows.
