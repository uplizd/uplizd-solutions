# Inventory Cleanup Agent (Uplizd) - Automated E-commerce Product and Category Lifecycle Management

## Summary
The Inventory Cleanup Agent is an intelligent automation workflow designed to maintain e-commerce store hygiene by identifying and removing outdated products, stale categories, and orphaned inventory items. By leveraging the Composio Toolset to interface with your store backend, this agent ensures your catalog remains accurate and optimized, reducing manual overhead for operations teams and improving the end-user shopping experience.

---

## Demo
![Inventory Cleanup Agent dashboard showing automated product removal workflow](image.png)
**Alt text (SEO-ready):** Inventory Cleanup Agent dashboard showing automated product removal workflow for e-commerce stores using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIVDxcQ6y39LwAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZ4AAAA+SURBVEjHY2AYBaNgFIyCUUAHAAABAAAB)](https://uplizd.ai/solutions/889db0e7-c0da-5fe6-a016-20cdd0165493)

---

## Category
*   **Primary category:** Operations
*   **Secondary tags:** e-commerce, inventory management, data hygiene, automation, cloudcart, composio, catalog optimization, workflow automation.
This solution streamlines e-commerce backend maintenance by automating the identification and deletion of obsolete inventory data.

---

## Who is this for?
This agent is built for teams managing high-volume product catalogs who need to maintain data integrity without manual intervention.

*   **E-commerce Operations Manager**
    *   Reduces time spent manually auditing and cleaning up expired product listings.
*   **Inventory Analyst**
    *   Ensures stock levels and product availability remain accurate across all sales channels.
*   **Catalog Administrator**
    *   Automates the removal of legacy categories and discontinued items to keep the storefront organized.
*   **Store Owner**
    *   Improves site performance and customer trust by eliminating broken links and "out of stock" clutter.

---

## Features
- **Automated Inventory Audit**
    Real-time scanning of your product database to flag items that have been inactive or out of stock beyond a defined threshold.
- **Intelligent Category Pruning**
    Automatically detects and removes empty or orphaned categories that no longer contain active product associations.
- **Composio-Powered Execution**
    Seamlessly integrates with your e-commerce platform via the Composio Toolset to execute secure, authenticated cleanup actions.
- **Configurable Cleanup Rules**
    Define custom logic for what constitutes "outdated," such as specific date ranges, inventory counts, or product tags.
- **Audit Logging & Reporting**
    Generates a summary report of all removed items, providing a clear trail of actions taken for compliance and record-keeping.

---

## Use Cases
**Seasonal Inventory Rotation**
*   Automatically archive or delete holiday-specific collections once the promotional period concludes.
*   Flag seasonal items that have zero sales velocity after the season ends for batch removal.

**Discontinued Product Management**
*   Identify products marked as "discontinued" in the backend and remove them from public storefront visibility.
*   Clean up associated media assets and metadata for products that are no longer supported.

**Catalog Hygiene Maintenance**
*   Remove duplicate or test product entries created during development or staging phases.
*   Consolidate fragmented categories to ensure a clean, navigable structure for store visitors.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Inventory Cleanup Agent template via the provided solution URL.
3. Connect your e-commerce platform credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup process.
*   **Agent**: Processes the cleanup logic based on your defined criteria and business rules.
*   **Composio Toolset**: Executes the specific API calls to read and delete inventory records from your store.
*   **Chat Output**: Delivers a summary notification confirming the number of items processed and removed.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
* `Identify and remove all products with zero stock and no sales for the last 180 days.`
* `Scan the catalog for empty categories and delete them to improve store navigation.`
* `Generate a report of all items flagged for removal before executing the final cleanup.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine that interprets your cleanup rules.
*   Maintain a strict, objective tone to ensure only intended items are flagged.
*   Prioritize safety by requiring confirmation for bulk delete operations.
*   Use clear, structured reasoning to explain why specific items were selected for removal.

### 2) Composio Toolset Node
*   **API Key**: Provide your platform-specific API key to authorize read/write access.
*   **Connection Scope**: Ensure the connection has `read_products`, `delete_products`, and `manage_categories` permissions.

### 3) Tool Availability
*   `list_products`: Fetches current inventory data.
*   `delete_product_by_id`: Executes the removal of specific items.
*   `get_category_details`: Audits category contents.
*   `delete_category`: Removes empty or obsolete categories.

---

## Related Solutions
*   [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Re-engage customers with automated follow-ups for unpurchased items.
*   [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Maintain security and integrity across your digital infrastructure.
*   [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex operational tasks across multiple business platforms.
