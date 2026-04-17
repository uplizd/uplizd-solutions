# Product Catalog Management Agent (Uplizd) - Automate Salesmate inventory and pricing updates

## Summary
The Product Catalog Management Agent streamlines inventory operations by automating the synchronization and maintenance of your Salesmate product catalog. This Uplizd AI workflow eliminates manual data entry, ensures pricing accuracy across your sales channels, and maintains a single source of truth for your product data, significantly reducing pipeline friction and administrative overhead for sales teams.

---

## Demo
![Product Catalog Management Agent workflow showing automated sync between Salesmate and inventory data sources](image.png)
**Alt text (SEO-ready):** Product Catalog Management Agent workflow for Salesmate, showing automated inventory updates, pricing synchronization, and Uplizd AI data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/02b5e5fe-8bec-530d-a3f9-1fe435009ff4)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** `salesmate`, `product catalog`, `inventory management`, `data sync`, `automation`, `crm`, `ai workflow`, `composio`  
This solution bridges the gap between your inventory systems and Salesmate, ensuring your sales team always has access to real-time product data.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to eliminate manual catalog maintenance and improve data hygiene.

*   **Sales Operations Manager**
    *   Automates bulk updates to product pricing and descriptions, saving hours of manual spreadsheet work.
*   **Inventory Coordinator**
    *   Ensures that stock levels in the CRM accurately reflect real-time warehouse or e-commerce availability.
*   **Account Executive**
    *   Provides confidence that quotes and proposals are generated using the most current and accurate product information.
*   **Revenue Operations Lead**
    *   Maintains data integrity across the sales stack, reducing errors in reporting and forecasting.

---

## Features
- **Automated Catalog Sync**
  Real-time synchronization of product details between external databases and Salesmate using the Composio Toolset.
- **Dynamic Pricing Updates**
  Automatically adjust product pricing based on pre-defined business rules or external market triggers.
- **Bulk Data Validation**
  Intelligent verification of product attributes to ensure compliance with internal naming and formatting standards.
- **Inventory Level Monitoring**
  Proactive alerts and updates when stock levels fall below thresholds, preventing the sale of unavailable items.
- **Error Handling & Logging**
  Comprehensive tracking of sync failures with automated notifications to ensure no product data is left in an inconsistent state.

---

## Use Cases
**Pricing Strategy Execution**
*   Update regional pricing tiers in Salesmate based on seasonal discount schedules.
*   Sync promotional price changes from your e-commerce platform to the CRM instantly.

**Inventory Lifecycle Management**
*   Automatically archive or deprecate discontinued products to keep the sales catalog clean.
*   Refresh stock availability fields every hour to prevent overselling during high-demand periods.

**Data Hygiene & Quality**
*   Standardize product descriptions and SKU naming conventions across the entire catalog.
*   Detect and flag duplicate product entries or missing mandatory fields for manual review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your Salesmate account credentials within the integration settings.
4. Ensure nodes are correctly mapped to your specific Salesmate instance and data sources.

### 2) Setup the Nodes
*   **Chat Input**: Receives manual triggers or scheduled sync requests from the user.
*   **Agent**: Processes instructions to fetch, validate, and update product data.
*   **Composio Toolset**: Executes API calls to Salesmate for reading and writing catalog records.
*   **Chat Output**: Confirms the number of products updated and highlights any errors found.

### 3) Run the Flow
Use the Playground to test your catalog sync:
*   `Sync all product prices from the master inventory sheet to Salesmate.`
*   `Identify and flag all products in Salesmate that have missing SKU numbers.`
*   `Update the 'Status' field to 'Discontinued' for all items with zero stock.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic controller for data transformation and API orchestration.
*   Instruction: "You are a data management assistant; prioritize accuracy and data integrity."
*   Instruction: "When updating products, always verify the SKU exists before applying changes."
*   Instruction: "Report a summary of changes made, including any records that failed validation."

### 2) Composio Toolset Node
*   **API Key**: Provide your Salesmate API key in the secure configuration panel.
*   **Connection Scope**: Ensure the connection has read/write permissions for the Product and Inventory modules.

### 3) Tool Availability
*   `salesmate_get_product`: Fetch current product details.
*   `salesmate_update_product`: Apply changes to existing catalog items.
*   `salesmate_list_products`: Retrieve bulk lists for audit purposes.
*   `data_validator_tool`: Perform schema and format checks on incoming data.

---

## Related Solutions
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize customer and lead data across multiple CRM platforms.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage sales stages and follow-up tasks for active opportunities.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate the cleanup of stale or malformed CRM records.
