# Snowflake Data Discovery Assistant (Uplizd) - Accelerate data cataloging and asset discovery

## Summary
The Snowflake Data Discovery Assistant is an intelligent AI workflow designed to automate the cataloging, search, and retrieval of data assets within Snowflake environments. By leveraging the Composio Toolset to interface directly with your data warehouse, this solution eliminates manual metadata lookup, ensuring data engineers and analysts have a single source of truth for schema definitions, table relationships, and data lineage, ultimately increasing pipeline velocity and data governance hygiene.

---

## Demo
![Snowflake Data Discovery Assistant workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Snowflake Data Discovery Assistant (Uplizd) workflow diagram showing automated data cataloging, schema retrieval, and AI-driven data asset discovery using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data)](https://uplizd.ai/solutions/36b5ff60-a5dd-59a9-9892-fad00d7c093b)

---

## Category
**Primary category:** Data integration
**Secondary tags:** snowflake, data discovery, metadata management, data engineering, composio, ai workflow, data governance, cataloging
This solution bridges the gap between raw Snowflake metadata and actionable insights for technical teams.

---

## Who is this for?
This assistant is built for data-driven professionals who need to navigate complex warehouse environments without manual SQL overhead.

- **Data Engineers**
    - Automate the documentation of new tables and schema changes across development and production environments.
- **Data Analysts**
    - Rapidly discover relevant datasets and understand column definitions without querying the information schema manually.
- **Analytics Engineers**
    - Maintain high data hygiene by identifying orphaned tables and verifying data lineage for downstream reporting.
- **Data Governance Leads**
    - Ensure compliance and visibility by auditing data access patterns and asset ownership directly through natural language.

---

## Features
- **Automated Metadata Retrieval**
    - Instantly fetch table schemas, column types, and constraints from Snowflake using natural language queries.
- **Intelligent Asset Search**
    - Semantic search capabilities that allow users to find tables based on business context rather than just exact naming conventions.
- **Composio-Powered Connectivity**
    - Secure, authenticated integration with Snowflake via the Composio Toolset, ensuring real-time access to warehouse metadata.
- **Context-Aware Documentation**
    - Automatically generate descriptive summaries for data assets, improving team-wide knowledge sharing.
- **Cross-Environment Visibility**
    - Seamlessly switch between databases and schemas to provide a unified view of the entire data ecosystem.

---

## Use Cases
**Data Cataloging & Documentation**
- Automatically generate data dictionaries for new warehouse schemas upon deployment.
- Identify and document table ownership and purpose for improved internal data literacy.

**Self-Service Data Discovery**
- Enable non-technical stakeholders to find relevant datasets for reporting without needing SQL expertise.
- Quickly retrieve sample data and column descriptions to validate data suitability for specific analysis tasks.

**Data Governance & Hygiene**
- Audit unused or deprecated tables to optimize storage and reduce data clutter.
- Verify that sensitive columns are correctly tagged and documented across the entire Snowflake instance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Snowflake Data Discovery Assistant template from the solution library.
3. Connect your Snowflake credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language queries regarding data assets.
- **Agent**: Processes intent and maps user requests to specific Snowflake metadata functions.
- **Composio Toolset**: Executes secure API calls to retrieve schema, table, and database information.
- **Chat Output**: Delivers clear, formatted responses containing the requested data insights.

### 3) Run the Flow
Use the Playground to test the assistant with these prompts:
- `Find all tables in the 'marketing' schema that contain 'customer' information.`
- `What is the schema definition for the 'orders_fact' table in the 'sales' database?`
- `List all tables created in the last 30 days that have no documentation.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the bridge between user intent and database metadata.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize accuracy when interpreting schema names.
- Ensure the agent is configured to provide context-rich explanations alongside raw metadata.

### 2) Composio Toolset Node
- Provide your Snowflake-authorized API key within the Composio connection settings.
- Scope the connection to the specific databases and schemas required for discovery.

### 3) Tool Availability
- `snowflake_list_tables`: Retrieve lists of tables within a specific schema.
- `snowflake_get_schema`: Fetch detailed column and type information.
- `snowflake_search_metadata`: Perform semantic searches across the data catalog.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and identify key business signals.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects and accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the performance and reliability of your automated data pipelines.
