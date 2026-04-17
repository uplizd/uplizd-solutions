# Chat with PostgreSQL Database (Uplizd) - Natural language SQL querying and data insights

## Summary
The Chat with PostgreSQL Database solution enables users to interact with their relational data using natural language, transforming complex SQL queries into intuitive conversational insights. By leveraging the Composio Toolset, this Uplizd workflow bridges the gap between technical database management and business intelligence, allowing stakeholders to extract, analyze, and visualize PostgreSQL data without writing manual code, thereby increasing data accessibility and pipeline velocity.

---

## Demo
![Chat with PostgreSQL Database interface showing natural language query execution and data output](image.png)
**Alt text (SEO-ready):** Chat with PostgreSQL Database interface showing natural language query execution, SQL data retrieval, and Uplizd AI workflow integration for database management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6Y3J9LwAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAMklEQVR42mP8z8AARkBxYI0B4v9/kP8/gP//g/8/gP//g/8/gP//g/8/gP//g/8/gP8A+7sQ33t/H/wAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/b47ef751-4603-529e-aa52-09babded70d8)

---

## Category
- **Primary category:** Data Integration
- **Secondary tags:** postgresql, sql, database, data analysis, ai workflow, composio, business intelligence, query automation
- This solution streamlines database operations by allowing non-technical users to perform complex data analysis directly through an AI-driven conversational interface.

---

## Who is this for?
This solution is designed for teams that need to democratize data access and reduce the burden on engineering resources for routine database queries.

- **Data Analysts**
    - Accelerate ad-hoc reporting and data exploration without writing repetitive SQL scripts.
- **Product Managers**
    - Retrieve real-time user metrics and feature adoption data directly from the production database.
- **Operations Leads**
    - Monitor system health and operational logs through simple conversational prompts.
- **Software Engineers**
    - Offload routine data retrieval tasks to an automated agent, allowing more focus on core infrastructure.

---

## Features
- **Natural Language to SQL**
    - Automatically translates user intent into optimized PostgreSQL queries using advanced LLM reasoning.
- **Secure Database Connectivity**
    - Connects to your PostgreSQL instances via the Composio Toolset with granular read-only access controls.
- **Real-time Data Retrieval**
    - Fetches live data from your tables, ensuring that insights are always based on the most current database state.
- **Context-Aware Schema Mapping**
    - The agent understands your specific table structures and relationships to provide accurate and relevant data results.
- **Automated Data Formatting**
    - Converts raw query results into readable summaries, tables, or JSON formats for immediate business use.

---

## Use Cases
**Operational Reporting**
- Generate daily summaries of new user sign-ups or transaction volumes directly from the database.
- Extract specific error logs or system performance metrics to troubleshoot production issues.

**Business Intelligence**
- Query customer lifetime value (CLV) or churn metrics by joining multiple relational tables.
- Perform cohort analysis by filtering database records based on specific time windows or user attributes.

**Data Hygiene & Auditing**
- Identify orphaned records or inconsistent data entries across related tables to maintain database integrity.
- Audit user access logs or recent modifications to ensure compliance with internal data policies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the "Chat with PostgreSQL Database" template from the solution library.
3. Configure your environment variables to include your database connection string.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language question about the database.
- **Agent**: Interprets the intent and determines the necessary SQL query logic.
- **Composio Toolset**: Executes the generated SQL commands against your PostgreSQL instance.
- **Chat Output**: Presents the retrieved data or summary back to the user in a clear format.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Show me the top 10 customers by total order value from the last 30 days.`
- `How many active users do we have in the 'US' region based on the users table?`
- `List all pending support tickets that have been open for more than 48 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the bridge between the user and the database, requiring clear instructions to ensure query safety.
- **System Prompt:** Define the agent as a helpful SQL assistant with read-only access.
- **Constraint Logic:** Explicitly instruct the agent to avoid destructive commands (e.g., DROP, DELETE).
- **Output Formatting:** Request that the agent summarizes results in a Markdown table for better readability.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to authenticate the toolset.
- **Connection Scope:** Ensure the PostgreSQL integration is authorized with the necessary host, port, and credentials.

### 3) Tool Availability
- **SQL Query Executor:** Capability to run SELECT statements on authorized schemas.
- **Schema Inspector:** Ability to fetch table metadata to understand column names and types.
- **Data Formatter:** Utility to transform raw database rows into human-readable text.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automate financial data matching and ledger balancing.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the status and performance of automated business processes.
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) — Gain insights into database and workspace activity patterns.
