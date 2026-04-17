# Database Cleanup Optimizer (Uplizd) - Intelligent database maintenance and resource optimization

## Summary
The Database Cleanup Optimizer is an automated Uplizd workflow designed to streamline database hygiene by identifying redundant records, optimizing storage allocation, and purging stale data. By leveraging the Composio Toolset to interface directly with your database infrastructure, this solution ensures high pipeline velocity and data integrity, providing a single source of truth for engineering and data operations teams.

---

## Demo
![Database Cleanup Optimizer workflow dashboard showing automated record deletion and storage optimization tasks](image.png)
**Alt text (SEO-ready):** Database Cleanup Optimizer workflow dashboard showing automated record deletion, data hygiene, and storage optimization tasks using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1953c2dc-3ed0-5d90-9dec-6f0517154958)

---

## Category
**Primary category:** Data integration
**Secondary tags:** database, cleanup, data hygiene, prisma, sql, automation, composio, data optimization
This solution automates the lifecycle management of database records to reduce storage costs and improve query performance.

---

## Who is this for?
This solution is designed for technical teams managing high-volume data environments who need to maintain system performance without manual intervention.

*   **Database Administrators**
    *   Automate routine maintenance tasks and index optimization to ensure peak database health.
*   **Data Engineers**
    *   Implement reliable data retention policies that scale across complex schemas.
*   **DevOps Engineers**
    *   Reduce cloud storage overhead by identifying and purging stale or redundant log data.
*   **Backend Developers**
    *   Ensure application performance by keeping production tables lean and query-efficient.

---

## Features
- **Automated Stale Data Detection**
    Real-time identification of records exceeding retention thresholds using intelligent query logic.
- **Resource Optimization Engine**
    Automatically reclaims storage space by purging deprecated entries and cleaning up orphaned relations.
- **Composio-Powered Execution**
    Seamlessly connects to your database via the Composio Toolset for secure, authenticated CRUD operations.
- **Compliance-Aware Purging**
    Configurable rules to ensure data deletion adheres to internal governance and privacy policies.
- **Execution Reporting**
    Detailed logs and summaries generated after every cleanup cycle to track storage savings and record counts.

---

## Use Cases
**Storage Cost Reduction**
*   Automatically identify and archive logs older than 90 days to secondary cold storage.
*   Purge temporary session data that has expired to keep primary tables performant.

**Data Hygiene Maintenance**
*   Remove orphaned records that lack valid foreign key associations after bulk migration tasks.
*   Standardize formatting for legacy fields to ensure consistency across the entire database.

**Performance Optimization**
*   Identify and remove duplicate entries that slow down indexing and search operations.
*   Clear out "soft-deleted" records that are no longer required for reporting or audit purposes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the builder.
2. Connect your database credentials via the Composio Toolset integration.
3. Configure your specific table schemas and retention policies in the Agent node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup process.
*   **Agent**: Analyzes the database state and determines which records meet the criteria for deletion or optimization.
*   **Composio Toolset**: Executes the validated SQL or ORM commands to perform the cleanup actions.
*   **Chat Output**: Returns a summary report of the cleanup operation, including total records processed and storage reclaimed.

### 3) Run the Flow
Use the Playground to test your cleanup logic with the following prompts:
* `Run a cleanup on the 'sessions' table for records older than 30 days.`
* `Identify and delete all orphaned user profiles that have no associated activity logs.`
* `Generate a report on current storage usage and suggest tables for optimization.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making layer for your database maintenance.
*   Instruct the agent to prioritize safety by requiring confirmation for bulk deletions.
*   Define clear retention policies within the system prompt to guide the agent's logic.
*   Ensure the agent is configured to output structured JSON reports for the Chat Output node.

### 2) Composio Toolset Node
*   Provide your database API key or connection string within the Composio configuration.
*   Limit the connection scope to "Read/Write" access only on the specific tables required for the cleanup task.

### 3) Tool Availability
*   **Query Execution**: Ability to run safe `SELECT` and `DELETE` queries.
*   **Schema Inspection**: Capability to read table structures to identify dependencies.
*   **Logging Utility**: Access to write operation summaries to your preferred monitoring tool.

---

## Related Solutions
* [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automated security and configuration auditing for cloud accounts.
* [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Real-time tracking and alerting for automated workflow performance.
* [Admin User Access Auditor by Storeganise](../admin-user-access-auditor-by-storeganise/README.md) - Auditing and managing user permissions across administrative environments.
