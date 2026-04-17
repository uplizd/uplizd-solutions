# Inventory Catalog Manager (Uplizd) - Streamline rental inventory organization and data synchronization

## Summary
The Inventory Catalog Manager by Booqable is an intelligent Uplizd workflow designed to automate the organization, categorization, and synchronization of rental inventory data. By leveraging the Composio Toolset, this solution enables operations teams to maintain a single source of truth for product availability, pricing, and stock levels, significantly reducing manual entry errors and improving pipeline velocity for rental businesses.

---

## Demo
![Inventory Catalog Manager workflow dashboard showing automated Booqable inventory updates and synchronization nodes](image.png)
**Alt text (SEO-ready):** Inventory Catalog Manager Uplizd workflow, Booqable inventory automation, rental data synchronization, and automated catalog management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/758815ef-5d35-5228-bbb0-a042f56db225)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** inventory, booqable, rental, data sync, catalog management, automation, composio, ai workflow
- This solution bridges the gap between raw rental product data and structured catalog management through automated AI-driven workflows.

---

## Who is this for?
This solution is designed for rental business owners and operations teams looking to scale their inventory management without increasing manual overhead.

- **Operations Manager**
    - Automates the synchronization of stock levels across multiple rental channels to prevent overbooking.
- **Inventory Specialist**
    - Ensures product descriptions, pricing, and availability metadata remain accurate and consistent.
- **Rental Business Owner**
    - Gains real-time visibility into high-performing assets to optimize procurement and maintenance cycles.
- **E-commerce Coordinator**
    - Streamlines the publishing of new rental items to the storefront with standardized formatting and categorization.

---

## Features
- **Automated Inventory Sync**
    - Real-time synchronization of rental items between your database and Booqable to ensure data integrity.
- **Intelligent Categorization**
    - Uses AI to automatically tag and group rental assets based on product attributes and usage patterns.
- **Dynamic Pricing Updates**
    - Adjusts rental pricing models automatically based on demand signals and seasonal inventory trends.
- **Stock Level Monitoring**
    - Proactive alerts and automated status updates when inventory levels fall below defined thresholds.
- **Composio-Powered Integration**
    - Seamless connectivity with the Booqable API to execute complex inventory operations without manual coding.

---

## Use Cases
**Inventory Lifecycle Management**
- Automatically archive discontinued rental items to keep the active catalog clean and searchable.
- Sync new product arrivals from procurement sheets directly into the Booqable rental platform.

**Operational Data Hygiene**
- Standardize naming conventions and descriptions for all rental assets to improve customer search experience.
- Detect and flag duplicate inventory entries or conflicting pricing data across different product categories.

**Performance & Analytics**
- Generate automated reports on inventory turnover rates to identify which assets require maintenance or replacement.
- Update availability calendars based on real-time booking data to maximize asset utilization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the **Inventory Catalog Manager**.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Booqable account via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives inventory update requests or catalog queries from users.
- **Agent**: Processes inventory logic and determines the necessary API actions.
- **Composio Toolset**: Executes secure calls to the Booqable API for data retrieval and updates.
- **Chat Output**: Returns the confirmation of inventory changes or requested catalog data to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your inventory automation:
- `Update the pricing for all 'Camera Gear' items to include a 10% seasonal markup.`
- `List all inventory items currently marked as 'Maintenance Required' in the catalog.`
- `Sync the latest stock levels from the warehouse spreadsheet to the Booqable storefront.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, interpreting inventory commands and translating them into API calls.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on handling inventory conflicts and data formatting.
- Ensure the system prompt includes constraints for updating pricing and stock status.

### 2) Composio Toolset Node
- Authenticate using your Booqable API key within the Composio dashboard.
- Set the connection scope to allow read/write access to inventory and product modules.

### 3) Tool Availability
- `booqable_get_products`: Fetch current catalog data.
- `booqable_update_product`: Modify pricing, descriptions, or stock status.
- `booqable_list_orders`: Cross-reference inventory usage with booking history.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose automation for job-based business workflows.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Financial data alignment for rental and service businesses.
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) — Data-driven insights for managing physical asset utilization.
