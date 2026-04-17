# Product Catalog Synchronizer (Uplizd) - Automate inventory and product data synchronization

## Summary
The Product Catalog Synchronizer by Omnisend is an intelligent Uplizd workflow designed to bridge the gap between your inventory management system and your marketing platform. By automating the flow of product data, it ensures that your marketing campaigns always reflect real-time stock levels, pricing, and product availability, eliminating manual entry errors and ensuring a consistent customer experience across all sales channels.

---

## Demo
![Product Catalog Synchronizer workflow showing inventory data flowing from source to Omnisend via Uplizd](image.png)
**Alt text (SEO-ready):** Uplizd Product Catalog Synchronizer workflow automating inventory data sync between product databases and Omnisend for real-time marketing updates.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b9f49877-c481-57db-a0fc-7dd6b28b5e15)

---

## Category
**Primary category:** Data integration
**Secondary tags:** product catalog, omnisend, inventory sync, e-commerce, data automation, marketing operations, composio, ai workflow.
This solution streamlines e-commerce operations by ensuring your product catalog remains the single source of truth across your marketing and sales stack.

---

## Who is this for?
This solution is designed for teams managing high-volume e-commerce catalogs who need to maintain perfect alignment between backend inventory and frontend marketing assets.

*   **E-commerce Manager**
    *   Ensures marketing campaigns never promote out-of-stock items, protecting brand reputation.
*   **Marketing Operations Specialist**
    *   Reduces manual data entry time by automating the synchronization of product attributes and pricing.
*   **Inventory Analyst**
    *   Maintains data integrity across platforms, ensuring that stock counts are reflected accurately in customer-facing emails.
*   **Growth Marketer**
    *   Leverages real-time product data to trigger personalized, high-converting automated product recommendations.

---

## Features
- **Real-time Inventory Sync**
  Automatically pushes stock level changes from your database to Omnisend to prevent overselling.
- **Automated Attribute Mapping**
  Uses the Composio Toolset to map complex product fields, including SKU, price, and description, between disparate systems.
- **Dynamic Catalog Updates**
  Updates product images and metadata instantly when changes are detected in your primary product information system.
- **Error Handling & Logging**
  Provides automated alerts if a sync fails, allowing for rapid intervention before marketing campaigns are impacted.
- **Scalable Data Processing**
  Handles bulk catalog updates efficiently, ensuring performance remains stable even during high-traffic seasonal sales.

---

## Use Cases
**Inventory Accuracy**
*   Syncing real-time stock levels to prevent marketing emails from featuring out-of-stock products.
*   Updating product availability status across multiple regions or warehouses simultaneously.

**Marketing Personalization**
*   Refreshing product pricing in automated abandoned cart flows to reflect current promotional discounts.
*   Injecting updated product descriptions into personalized recommendation blocks based on the latest catalog data.

**Operational Efficiency**
*   Automating the onboarding of new product lines from the central database to the marketing platform.
*   Cleaning up legacy product data to ensure only active, sellable items are visible to the marketing engine.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Omnisend and source database connections via the Composio dashboard.
4. Ensure nodes are correctly mapped and the workflow is enabled in your Uplizd dashboard.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request to initiate a catalog sync.
*   **Agent**: Interprets the sync request and manages the logic for data transformation and validation.
*   **Composio Toolset**: Executes the API calls to read from your product source and write updates to Omnisend.
*   **Chat Output**: Confirms the successful completion of the sync or reports any data discrepancies found.

### 3) Run the Flow
Use the Playground to test your synchronization:
*   `Sync all products with stock levels less than 5 to the 'Low Stock' segment in Omnisend.`
*   `Update the price of all items in the 'Summer Collection' category from the database to Omnisend.`
*   `Verify that the product catalog in Omnisend matches the current inventory database records.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data validation and tool selection.
*   Prioritize data accuracy and field-mapping consistency.
*   Use structured output to ensure the Composio Toolset receives clean, formatted JSON.
*   Maintain a neutral tone for reporting sync status and error logs.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Omnisend API key is configured with `products:write` and `inventory:read` scopes.
*   **Connection**: Connect your primary product database (e.g., Shopify, BigCommerce, or custom SQL) to the Composio toolset to enable bi-directional data flow.

### 3) Tool Availability
*   `omnisend_update_product`: Updates specific product attributes.
*   `inventory_fetch_all`: Retrieves current stock counts and pricing.
*   `catalog_validate_schema`: Ensures data formats match Omnisend requirements before transmission.

---

## Related Solutions
*   [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automates follow-up sequences for recovered revenue.
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gathers intelligence for personalized sales outreach.
*   [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose automation for complex business processes.
