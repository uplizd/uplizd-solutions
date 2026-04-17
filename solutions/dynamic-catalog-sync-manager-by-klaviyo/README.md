# Dynamic Catalog Sync Manager (Uplizd) - Real-time inventory and product catalog synchronization

## Summary
The Dynamic Catalog Sync Manager automates the bidirectional flow of product data between your inventory systems and Klaviyo, ensuring your email marketing campaigns always reflect accurate stock levels and pricing. By leveraging intelligent agents to monitor changes and trigger updates, this workflow eliminates manual data entry, prevents overselling, and maintains high-quality product catalogs for personalized marketing automation.

---

## Demo
![Dynamic Catalog Sync Manager workflow showing inventory data flowing from source to Klaviyo via an AI agent](image.png)
**Alt text (SEO-ready):** Dynamic Catalog Sync Manager workflow for automated inventory updates, Klaviyo catalog synchronization, and real-time product data hygiene using Uplizd AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d1f713ad-c73c-56b5-83ac-6dc496273e12)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** klaviyo, catalog sync, inventory management, ecommerce, data automation, product data, composio, ai workflow
- This solution bridges the gap between backend inventory databases and customer-facing marketing platforms to ensure seamless data consistency.

---

## Who is this for?
This workflow is designed for teams managing high-volume ecommerce catalogs who need to maintain perfect alignment between their store inventory and marketing assets.

- **Ecommerce Manager**
    - Ensures that marketing emails never promote out-of-stock items or incorrect pricing.
- **Email Marketing Specialist**
    - Gains confidence that dynamic product blocks in Klaviyo are always populated with live, accurate data.
- **Operations Analyst**
    - Reduces the time spent on manual catalog updates and troubleshooting inventory-related campaign errors.
- **Growth Marketer**
    - Leverages real-time inventory signals to trigger personalized "back in stock" or "low stock" automated flows.

---

## Features
- **Automated Sync Engine**
    - Triggers real-time updates to Klaviyo catalogs whenever inventory levels or product details change in your source system.
- **Intelligent Data Mapping**
    - Uses the Composio Toolset to intelligently map complex product attributes between disparate database schemas.
- **Error Handling & Validation**
    - Automatically flags and reports synchronization conflicts or missing product metadata for manual review.
- **Bulk Update Capability**
    - Efficiently processes large-scale catalog changes without hitting API rate limits or causing performance bottlenecks.
- **Real-time Inventory Monitoring**
    - Maintains a single source of truth for stock status, preventing discrepancies between your store and your marketing platform.

---

## Use Cases
**Inventory Accuracy**
- Automatically update product availability status in Klaviyo when items sell out in the primary database.
- Sync real-time price adjustments across all marketing templates to ensure promotional consistency.

**Marketing Automation**
- Trigger personalized "Back in Stock" email flows immediately upon inventory replenishment.
- Dynamically update "Trending Products" blocks based on the latest stock levels and sales velocity data.

**Data Hygiene**
- Clean up legacy product entries in Klaviyo that no longer exist in the master inventory system.
- Standardize product naming conventions and categories across all marketing channels during the sync process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Connect your Klaviyo and Inventory system accounts via the Composio integration settings.
4. Ensure nodes are correctly mapped and all required API credentials are authenticated.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to initiate a catalog sync.
- **Agent**: Processes the inventory data and determines which product fields require updates.
- **Composio Toolset**: Executes the API calls to push updates directly into the Klaviyo catalog.
- **Chat Output**: Provides a summary report of the sync status, including successful updates and any encountered errors.

### 3) Run the Flow
Use the Playground to test your sync logic:
- `Sync all products with inventory status 'low_stock' to Klaviyo.`
- `Update the price for product SKU 'ABC-123' in the main catalog.`
- `Perform a full catalog audit and sync between the database and Klaviyo.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic layer for data transformation and decision-making.
- Prioritize accuracy when mapping product identifiers between systems.
- Use the provided context to determine if an update is a partial field change or a full product refresh.
- Maintain a neutral, professional tone when reporting sync logs in the output.

### 2) Composio Toolset Node
Requires a valid Klaviyo API key with `catalog:write` and `catalog:read` scopes, along with read access to your inventory database.

### 3) Tool Availability
- **Klaviyo API**: For managing product catalogs and item properties.
- **Inventory Connector**: For fetching live stock levels and pricing data.
- **Data Transformer**: For normalizing field formats between the source and target systems.

---

## Related Solutions
- [Abandoned Cart Recovery Agent (Klaviyo)](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automates personalized follow-ups for users who leave items in their cart.
- [Account Reconciliation Helper (Quickbooks)](../account-reconciliation-helper-by-quickbooks/README.md) — Simplifies financial data matching and ledger balancing.
- [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) — Streamlines cross-platform task management and project updates.
