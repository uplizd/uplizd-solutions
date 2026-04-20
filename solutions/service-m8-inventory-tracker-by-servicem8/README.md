# ServiceM8 Inventory Tracker (Uplizd) - Automated real-time stock management and material usage tracking

## Summary
The ServiceM8 Inventory Tracker is an intelligent Uplizd AI workflow designed to automate stock reconciliation and material usage updates. By bridging real-time field data with your ServiceM8 inventory, this solution eliminates manual entry errors, ensures accurate stock levels, and accelerates operational velocity for field service businesses.

---

## Demo
![ServiceM8 Inventory Tracker workflow showing automated stock level updates and material usage logging](image.png)
**Alt text (SEO-ready):** ServiceM8 Inventory Tracker Uplizd workflow, automated stock management, material usage tracking, field service inventory automation, Composio ServiceM8 integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/service-m8-inventory-tracker-by-servicem8)

---

## Category
**Primary category:** Field service operations
**Secondary tags:** servicem8, inventory, stock management, field service, automation, composio, data sync, operational efficiency.
This solution streamlines inventory management by automating the synchronization of material usage between field activities and the central ServiceM8 database.

---

## Who is this for?
This workflow is designed for field service organizations looking to reduce administrative overhead and improve inventory accuracy.

* **Operations Manager**
    * Maintains real-time visibility into stock levels across multiple service vehicles.
* **Field Technician**
    * Reduces manual paperwork by automatically logging material usage upon job completion.
* **Warehouse Coordinator**
    * Receives automated alerts for low-stock items to trigger timely procurement.
* **Business Owner**
    * Increases profit margins by minimizing inventory shrinkage and billing discrepancies.

---

## Features
- **Real-time Stock Synchronization**
  Automatically updates inventory counts in ServiceM8 the moment a technician logs material usage in the field.
- **Automated Usage Logging**
  Eliminates manual data entry by capturing material consumption directly from completed work orders.
- **Low-Stock Alerts**
  Triggers notifications when specific inventory items fall below defined thresholds to prevent project delays.
- **Discrepancy Reporting**
  Identifies variances between expected stock levels and actual counts to improve audit accuracy.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely interface with ServiceM8 APIs for reliable, authenticated data exchange.

---

## Use Cases
**Inventory Reconciliation**
* Automatically adjusting stock levels after a technician completes a site visit or installation.
* Syncing warehouse inventory counts with mobile van stock to ensure accurate availability reporting.

**Material Usage Tracking**
* Linking specific material consumption to individual work orders for precise customer billing.
* Tracking high-value assets and consumables to monitor project costs in real-time.

**Operational Efficiency**
* Automating the replenishment process by generating purchase requests when stock hits minimum levels.
* Reducing the time spent on end-of-day administrative tasks by automating inventory logs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the ServiceM8 Inventory Tracker JSON configuration file.
3. Connect your ServiceM8 account via the Composio integration portal.
4. Ensure nodes are correctly mapped to your specific ServiceM8 workspace and inventory categories.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger event or manual request for inventory updates.
* **Agent**: Processes the request, interprets material usage data, and determines the necessary ServiceM8 API calls.
* **Composio Toolset**: Executes the authenticated commands to update stock levels or retrieve inventory data.
* **Chat Output**: Confirms the successful update or provides a summary of current stock availability.

### 3) Run the Flow
Use the Uplizd Playground to test your workflow with these example prompts:
* `Update inventory for Job #12345: deduct 2 units of 'Copper Pipe' and 1 'Pipe Fitting'.`
* `What is the current stock level for 'Standard Valve' in the main warehouse?`
* `Generate a report of all material usage logged for today's completed jobs.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic layer between your input and the ServiceM8 API.
* Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are a ServiceM8 inventory assistant. Extract material names and quantities from the input and map them to the correct ServiceM8 inventory IDs."
* Instruction: "Always verify the current stock level before confirming a deduction to prevent negative inventory values."

### 2) Composio Toolset Node
* Provide your ServiceM8 API key within the Composio connection settings.
* Ensure the connection scope includes `read` and `write` permissions for inventory and work order modules.

### 3) Tool Availability
* `servicem8_get_inventory`: Retrieve current stock levels and item details.
* `servicem8_update_stock`: Adjust inventory counts based on field usage.
* `servicem8_get_work_order`: Fetch details of specific jobs to link material usage.

---

## Related Solutions
* [../crm-data-sync-agent/README.md](CRM Data Sync Agent) — Synchronize customer and product data across platforms.
* [../work-order-status-tracker/README.md](Work Order Status Tracker) — Monitor and update field service job progress in real-time.
* [../account-reconciliation-helper/README.md](Account Reconciliation Helper) — Automate financial data matching and cleanup.
