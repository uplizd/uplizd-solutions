# Database Naming Auditor (Uplizd) - Enforce schema consistency and naming standards across Baserow databases

## Summary
The Database Naming Auditor is an automated Uplizd workflow designed to enforce strict naming conventions across your Baserow databases. By leveraging the Composio Toolset to scan table and field labels, the agent identifies deviations from your organization's style guide, ensuring data hygiene, improving developer velocity, and maintaining a single source of truth for your data architecture.

---

## Demo
![Database Naming Auditor workflow showing Baserow integration and naming validation](image.png)
**Alt text (SEO-ready):** Uplizd Database Naming Auditor workflow for Baserow, automating schema validation, data hygiene, and naming convention enforcement.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f6ef103f-d922-5c53-822a-99483f714114)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** baserow, data hygiene, schema management, naming conventions, data governance, composio, ai workflow
- This solution bridges the gap between raw database creation and enterprise-grade data governance by automating the audit of naming patterns.

---

## Who is this for?
This solution is designed for technical teams and data stewards responsible for maintaining clean, scalable database architectures.

- **Data Engineers**
    - Automate the enforcement of naming standards to prevent technical debt in database schemas.
- **Database Administrators**
    - Ensure consistent field and table labels across multiple Baserow instances without manual oversight.
- **Product Managers**
    - Maintain clear, predictable data structures that allow for faster reporting and analytics.
- **DevOps Leads**
    - Integrate automated naming audits into the development lifecycle to ensure compliance with company-wide data policies.

---

## Features
- **Automated Schema Scanning**
    - Uses the Composio Toolset to programmatically fetch all table and field names from your Baserow databases.
- **Customizable Naming Rules**
    - Define your organization’s specific naming patterns (e.g., snake_case, camelCase) for the AI agent to validate against.
- **Real-time Deviation Alerts**
    - Receive immediate notifications or logs when a new field or table violates established naming conventions.
- **Bulk Correction Suggestions**
    - The agent provides actionable recommendations for renaming non-compliant elements to match your standard.
- **Compliance Reporting**
    - Generate periodic reports summarizing the health and consistency of your database naming architecture.

---

## Use Cases
**Standardizing Development Environments**
- Automatically flag tables created by developers that do not follow the internal `project_feature_name` format.
- Ensure all primary key fields are consistently labeled as `id` across new and legacy databases.

**Data Governance and Hygiene**
- Identify and report on orphaned or poorly named fields that complicate data integration pipelines.
- Enforce character limits and forbidden character policies to ensure compatibility with downstream BI tools.

**Onboarding and Migration**
- Audit imported databases during migration projects to ensure they align with your existing naming conventions.
- Provide automated feedback to team members on how to structure new databases for better long-term maintainability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Database Naming Auditor template from the solution library.
3. Connect your Baserow account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target database ID or workspace scope for the audit.
- **Agent**: Analyzes the schema against your defined naming policy instructions.
- **Composio Toolset**: Executes API calls to fetch and validate Baserow schema metadata.
- **Chat Output**: Returns a summary of naming violations and suggested corrections.

### 3) Run the Flow
Use the Playground to trigger the audit with prompts like:
- `Audit the 'Marketing_Leads' database for naming convention violations.`
- `List all fields in the 'Sales_Pipeline' table that do not follow snake_case.`
- `Check the entire 'Customer_Data' workspace for non-compliant table names.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data governance officer.
- **Instruction Pattern:**
    - "You are a database auditor. Your goal is to enforce naming conventions defined in the system prompt."
    - "Always compare table and field labels against the required format (e.g., snake_case)."
    - "Provide clear, actionable renaming suggestions for every violation found."

### 2) Composio Toolset Node
- Requires a valid Baserow API Key with read/write access to the target workspaces.
- Ensure the connection scope includes `list_tables` and `list_fields` permissions.

### 3) Tool Availability
- `baserow_list_tables`: Retrieves the list of tables in a specified database.
- `baserow_list_fields`: Fetches field definitions for a specific table.
- `baserow_update_field`: (Optional) Allows the agent to apply suggested renaming changes.

---

## Related Solutions
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) - Monitor and optimize Baserow workspace storage and activity.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track usage metrics to ensure data platform health.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Audit user permissions and access logs for security compliance.
