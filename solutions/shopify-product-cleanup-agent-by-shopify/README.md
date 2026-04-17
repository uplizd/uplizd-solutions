# Shopify Product Cleanup Agent (Uplizd) - Automated catalog hygiene and inventory optimization

## Summary
The Shopify Product Cleanup Agent is an intelligent workflow designed to automate the maintenance of your e-commerce catalog. By leveraging AI to identify outdated, low-performing, or incorrectly formatted product listings, this solution ensures your store remains optimized for search and customer experience. It helps store managers reduce manual data entry, improve site performance, and maintain a single source of truth for inventory data across the Shopify ecosystem.

---

## Demo
![Shopify Product Cleanup Agent workflow interface showing automated catalog audit and deletion of stale listings](image.png)
**Alt text (SEO-ready):** Shopify Product Cleanup Agent workflow for automated e-commerce catalog hygiene, inventory optimization, and AI-driven product management on Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQ1w10OQAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABkSURBVEjHY2AYBaNgFAwBAAABAAEAq91p7QAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/2d8d115f-0cd6-5698-9d7a-7d2a3165d025)

---

## Category
- **Primary category:** E-commerce operations
- **Secondary tags:** shopify, product management, catalog hygiene, data cleanup, inventory automation, ai workflow, composio, e-commerce
- This solution streamlines e-commerce backend management by automating the identification and removal of stale product data to maintain a healthy store catalog.

---

## Who is this for?
This solution is designed for e-commerce teams looking to scale their operations without the overhead of manual database maintenance.

- **E-commerce Manager**
    - Automates the removal of seasonal or discontinued items to keep the storefront relevant.
- **Inventory Specialist**
    - Ensures product data accuracy by flagging inconsistencies between Shopify and warehouse records.
- **SEO Specialist**
    - Maintains high site performance and search rankings by purging broken or low-quality product pages.
- **Store Administrator**
    - Reduces manual administrative burden by scheduling periodic catalog audits and cleanup tasks.

---

## Features
- **Automated Inventory Audit**
    - Scans your entire Shopify product catalog to identify items that have had zero sales or updates over a defined period.
- **Intelligent Data Cleanup**
    - Automatically archives or deletes products that meet specific "stale" criteria, preventing clutter in your admin dashboard.
- **Composio-Powered Shopify Integration**
    - Utilizes the Composio Toolset to securely execute read/write operations directly within your Shopify store environment.
- **Customizable Cleanup Rules**
    - Define granular logic for what constitutes a "stale" product, such as stock levels, last updated timestamps, or missing image tags.
- **Real-time Execution Logs**
    - Provides detailed reporting on every action taken by the agent, ensuring full transparency in your catalog management process.

---

## Use Cases
**Seasonal Catalog Refresh**
- Automatically archive holiday-specific collections once the season concludes to keep the storefront clean.
- Identify and remove discontinued product variants that no longer have active stock or supplier support.

**Data Hygiene Maintenance**
- Detect products missing essential metadata or images and flag them for immediate review by the content team.
- Standardize product naming conventions by identifying items that deviate from your store's established formatting rules.

**Inventory Optimization**
- Flag low-performing products that have not generated revenue in the last 180 days for potential liquidation or removal.
- Sync catalog status with internal warehouse data to ensure the online store only reflects currently available inventory.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the template.
2. Select "Import" to add the Shopify Product Cleanup Agent to your workspace.
3. Connect your Shopify account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the cleanup parameters or manual trigger commands.
- **Agent**: Processes instructions and determines which products require cleanup based on your logic.
- **Composio Toolset**: Executes the API calls to fetch, update, or delete products in Shopify.
- **Chat Output**: Returns a summary report of all actions performed during the cleanup session.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Find all products with zero sales in the last 6 months and generate a report.`
- `Archive all products tagged as 'Discontinued' that have zero inventory.`
- `Identify products missing images and list them for the content team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a catalog administrator, interpreting your cleanup criteria and mapping them to tool actions.
- Use a model with high reasoning capabilities (e.g., GPT-4o) for accurate data filtering.
- Instruction: "You are a Shopify catalog manager. Analyze product data provided by the toolset and execute cleanup tasks only when they meet the user's specific criteria."
- Instruction: "Always confirm the number of items to be deleted before executing the final removal command."

### 2) Composio Toolset Node
- Requires an active Shopify API key with `read_products` and `write_products` scopes.
- Ensure the connection is authorized within the Composio dashboard before running the flow.

### 3) Tool Availability
- `shopify_get_products`: Fetches product lists and metadata.
- `shopify_update_product`: Modifies product status or tags.
- `shopify_delete_product`: Removes stale items from the store catalog.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automates follow-ups for unpurchased items.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Syncs financial data and inventory records.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for business processes.
