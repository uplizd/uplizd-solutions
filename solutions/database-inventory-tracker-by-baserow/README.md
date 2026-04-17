# Database Inventory Tracker (Uplizd) - Automated real-time synchronization and cataloging of database assets

## Summary
The Database Inventory Tracker is an intelligent Uplizd workflow designed to maintain a single source of truth for your data infrastructure. By leveraging the Composio Toolset to interface with Baserow, the agent automatically discovers, maps, and updates database tables and schemas, ensuring your team has constant visibility into data assets, reducing manual documentation overhead, and preventing configuration drift.

---

## Demo
![Database Inventory Tracker workflow showing Baserow integration and automated schema mapping](image.png)
**Alt text (SEO-ready):** Database Inventory Tracker Uplizd workflow for automated Baserow data synchronization, schema mapping, and infrastructure cataloging.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/23280ba1-dbf1-5513-a5e9-9fc0e253bc36)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** baserow, database, inventory, data sync, schema management, automation, composio, ai workflow
- This solution streamlines data governance by automating the discovery and tracking of database tables within Baserow environments.

---

## Who is this for?
This solution is designed for technical teams and data stewards responsible for maintaining organized and accessible data architectures.

- **Data Engineers**
    - Automate the documentation of table schemas and database structures without manual entry.
- **Database Administrators**
    - Monitor inventory changes in real-time to ensure compliance and prevent unauthorized schema modifications.
- **Product Managers**
    - Gain immediate visibility into available data assets to accelerate feature development and reporting.
- **Operations Leads**
    - Maintain a centralized, up-to-date catalog of all active databases to improve cross-departmental data discovery.

---

## Features
- **Automated Discovery**
  Scans connected Baserow instances to identify new tables and fields automatically.
- **Real-time Sync**
  Updates your inventory catalog immediately whenever a structural change is detected in the source database.
- **Schema Mapping**
  Translates complex database structures into human-readable formats for better team collaboration.
- **Centralized Reporting**
  Aggregates inventory data into a single, searchable dashboard for high-level infrastructure oversight.
- **Composio Integration**
  Utilizes the Composio Toolset to securely execute read/write operations across your Baserow environment.

---

## Use Cases
**Infrastructure Auditing**
- Perform automated weekly audits of all database tables to identify unused or deprecated assets.
- Generate compliance reports detailing current table structures and data ownership.

**Data Onboarding**
- Quickly map new database environments during project kickoffs to reduce setup time.
- Standardize naming conventions across multiple Baserow workspaces through automated inventory checks.

**Operational Visibility**
- Trigger alerts when critical database schemas are modified or deleted by unauthorized users.
- Provide non-technical stakeholders with a clear, live view of available data tables and their purposes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the workflow template.
2. Connect your Baserow account via the Composio Toolset integration.
3. Configure your preferred LLM in the Agent node to handle schema interpretation.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your request to scan or report on database inventory.
- **Agent**: Processes instructions and queries the database structure.
- **Composio Toolset**: Executes API calls to fetch metadata from Baserow.
- **Chat Output**: Displays the formatted inventory report or confirmation of sync.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Scan all tables in my primary Baserow workspace and generate a summary report.`
- `List all fields currently active in the 'Customer_Data' table.`
- `Check for any new tables added to the database in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your inventory logic.
- Use a model capable of structured data output (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a database administrator assistant. Use the provided tools to fetch schema information and present it in a clear, organized table format."
- Instruction: "Always verify the workspace ID before executing discovery commands."

### 2) Composio Toolset Node
- Provide your Baserow API key within the Composio connection settings.
- Ensure the connection scope includes read-only access to your specific workspaces for security.

### 3) Tool Availability
- `list_tables`: Retrieves a list of all tables in the connected workspace.
- `get_table_schema`: Fetches field definitions and data types for a specific table.
- `search_inventory`: Queries the existing catalog for specific table names or field types.

---

## Related Solutions
- [Workspace Usage Analyzer (Baserow)](../workspace-usage-analyzer-by-baserow/README.md) — Monitor and optimize your Baserow workspace resource consumption.
- [Account Reconciliation Helper (Quickbooks)](../account-reconciliation-helper-by-quickbooks/README.md) — Automate financial data matching and inventory verification.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize and maintain data hygiene across multiple CRM platforms.
