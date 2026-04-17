# Product Catalog Management Agent (Uplizd) - Automated inventory synchronization and archival

## Summary
The Product Catalog Management Agent streamlines e-commerce operations by automating the lifecycle of product data within your HubSpot environment. By leveraging intelligent agents to monitor inventory status and trigger archival workflows, this solution ensures your storefront remains accurate, reduces manual data entry, and maintains high-quality product hygiene for better customer experiences.

---

## Demo
![Product Catalog Management Agent workflow interface showing HubSpot integration nodes](image.png)
**Alt text (SEO-ready):** Product Catalog Management Agent by Uplizd for HubSpot, featuring automated inventory synchronization, product archival, and AI-driven data hygiene workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9e03943c-7972-5cdd-a8b1-9e0d1972858f)

---

## Category
**Primary category:** E-commerce operations
**Secondary tags:** hubspot, product management, inventory, data hygiene, automation, catalog, composio, ai workflow

This solution bridges the gap between raw inventory data and clean, actionable product catalogs by automating routine maintenance tasks.

---

## Who is this for?
This agent is designed for teams looking to eliminate manual catalog updates and ensure their CRM reflects real-time inventory availability.

*   **E-commerce Managers**
    *   Automate the archival of out-of-stock or discontinued items to prevent customer friction.
*   **Operations Specialists**
    *   Maintain a single source of truth for product data across multiple sales channels.
*   **Sales Enablement Leads**
    *   Ensure sales teams are only referencing active, sellable products in their outreach.
*   **Data Analysts**
    *   Reduce data decay by enforcing consistent formatting and status updates across the product database.

---

## Features
- **Automated Archival**
  Automatically move discontinued or legacy products to an archived status based on inventory thresholds.
- **Real-time Sync**
  Utilize the Composio Toolset to trigger immediate updates between your inventory management system and HubSpot.
- **Data Hygiene Enforcement**
  Standardize product naming conventions and metadata fields during the ingestion and update process.
- **Inventory Monitoring**
  Continuous background scanning of stock levels to identify products that require status changes.
- **Intelligent Reporting**
  Generate summary logs of all catalog changes, providing visibility into automated maintenance actions.

---

## Use Cases
**Inventory Lifecycle Management**
*   Automatically archive products when stock levels hit zero for a defined period.
*   Update product availability status in HubSpot based on real-time warehouse data.

**Catalog Data Hygiene**
*   Standardize product descriptions and SKU formats across the entire catalog.
*   Identify and flag duplicate product entries for manual review or automated merging.

**Sales Operations Efficiency**
*   Remove outdated seasonal items from active sales views to streamline the quoting process.
*   Sync new product launches directly into HubSpot with pre-configured status and categorization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Product Catalog Management Agent template from the marketplace.
3. Connect your HubSpot account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives triggers or manual commands to initiate catalog audits.
*   **Agent**: Processes logic to determine if a product should be archived or updated.
*   **Composio Toolset**: Executes API calls to HubSpot to perform read/write operations.
*   **Chat Output**: Confirms the completion of the sync or reports any errors found during processing.

### 3) Run the Flow
Use the Playground to test your catalog management logic:
*   `Archive all products in the 'Legacy' category that have zero stock.`
*   `Sync the latest inventory levels for all active products in HubSpot.`
*   `Generate a report of all products updated in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your catalog rules.
*   Prioritize accuracy when interpreting inventory status codes.
*   Maintain a neutral, professional tone for all generated logs and reports.
*   Strictly follow the defined schema for product properties during updates.

### 2) Composio Toolset Node
Configure the node with your HubSpot API key and ensure the following scopes are enabled: `crm.objects.products.read`, `crm.objects.products.write`.

### 3) Tool Availability
*   **Product Search**: Locate specific items by SKU or name.
*   **Property Update**: Modify status, price, or inventory fields.
*   **Bulk Archival**: Perform batch operations on identified product sets.
*   **Log Generation**: Create audit trails for all automated changes.

---

## Related Solutions
*   [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate new account creation and data entry.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize records across multiple CRM platforms.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and standardize CRM data records.
