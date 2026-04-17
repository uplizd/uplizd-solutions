# Inventory Reorder Advisor (Uplizd) - Automate stock replenishment with intelligent sales velocity analysis

## Summary
The Inventory Reorder Advisor is an intelligent Uplizd workflow that monitors sales velocity and current stock levels to generate proactive purchase order recommendations. By integrating real-time inventory data via the Composio Toolset, this solution helps operations teams prevent stockouts, optimize capital allocation, and maintain seamless supply chain continuity.

---

## Demo
![Inventory Reorder Advisor workflow dashboard showing automated stock level alerts and purchase order generation](image.png)

**Alt text (SEO-ready):** Inventory Reorder Advisor Uplizd workflow for automated stock replenishment, sales velocity analysis, and purchase order management using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e13e7c34-4e96-5dd4-9f5b-85b25a17025a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** inventory, supply chain, procurement, baselinker, automation, sales velocity, stock management, composio, ai workflow
- This solution bridges the gap between real-time sales performance and procurement logistics to ensure optimal inventory levels.

---

## Who is this for?
This solution is designed for teams managing high-volume product catalogs who need to move from reactive manual ordering to data-driven replenishment.

- **Operations Manager**
    - Automates the identification of low-stock items to reduce manual oversight and human error.
- **Procurement Specialist**
    - Receives prioritized purchase order suggestions based on actual sales trends rather than static thresholds.
- **E-commerce Business Owner**
    - Minimizes capital tied up in overstock while preventing revenue loss from stockouts.
- **Supply Chain Analyst**
    - Leverages historical sales velocity data to forecast future demand more accurately.

---

## Features
- **Real-time Inventory Sync**
    - Connects directly to your inventory management system to pull live stock levels and pending order data.
- **Sales Velocity Calculation**
    - Analyzes recent sales trends to determine the exact rate at which products are moving off the shelves.
- **Automated Reorder Alerts**
    - Triggers intelligent notifications when stock levels fall below the calculated safety threshold for specific SKUs.
- **Purchase Order Generation**
    - Drafts ready-to-review purchase orders, including suggested quantities and vendor details, via the Composio Toolset.
- **Multi-Channel Integration**
    - Aggregates data from various sales channels to provide a unified view of inventory health across your entire business.

---

## Use Cases
**Stockout Prevention**
- Automatically flags high-velocity items that will reach zero stock within the next 7 days.
- Generates replenishment orders for seasonal best-sellers before supply chain lead times impact availability.

**Capital Optimization**
- Identifies slow-moving inventory to prevent unnecessary capital expenditure on products with low turnover.
- Adjusts reorder quantities based on current warehouse capacity and storage cost constraints.

**Procurement Efficiency**
- Consolidates reorder requests from multiple suppliers into a single, optimized purchase order.
- Updates internal procurement logs automatically once a suggested order is approved and sent to the vendor.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and import the Inventory Reorder Advisor workflow.
3. Authenticate your inventory management and procurement tool connections via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific API endpoints and data fields.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled requests to analyze inventory status.
- **Agent**: Processes sales velocity data and applies replenishment logic to determine order needs.
- **Composio Toolset**: Executes API calls to fetch stock data and create draft purchase orders.
- **Chat Output**: Delivers a summary report of recommended actions and generated purchase orders.

### 3) Run the Flow
Use the Uplizd Playground to test your workflow with these prompts:
- `Analyze current stock levels for all items in the 'Electronics' category and suggest reorders.`
- `Which products have a high sales velocity but are currently below the 14-day safety stock level?`
- `Generate a purchase order for all items identified as 'Critical' in the latest inventory audit.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting sales data and applying business rules.
- Instruction: "Act as an inventory expert; analyze sales velocity and current stock to determine optimal reorder quantities."
- Instruction: "Prioritize items with the highest sales growth and shortest lead times."
- Instruction: "Maintain a professional tone when reporting stock status and purchase order recommendations."

### 2) Composio Toolset Node
- Provide your API key for your inventory platform (e.g., BaseLinker).
- Ensure the connection scope includes read access to inventory levels and write access to purchase order modules.

### 3) Tool Availability
- **Inventory Fetcher**: Retrieves real-time SKU counts and warehouse locations.
- **Sales Analytics Engine**: Calculates daily/weekly sales velocity per product.
- **Procurement Manager**: Creates and updates purchase order drafts in your ERP or store backend.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automate financial data matching and ledger updates.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline cross-platform business processes and task management.
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) — Monitor data usage and optimize resource allocation across your workspaces.
