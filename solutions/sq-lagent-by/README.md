# SQL Agent (Uplizd) - Intelligent database querying and data analysis workflow

## Summary
The SQL Agent by Uplizd streamlines database interactions by enabling natural language querying, automated schema analysis, and real-time data retrieval. This workflow empowers technical and non-technical users to extract actionable insights from complex relational databases without writing manual code, ensuring pipeline velocity and data-driven decision-making across the organization.

---

## Demo
![SQL Agent workflow interface showing natural language input and database query execution](image.png)
**Alt text (SEO-ready):** SQL Agent by Uplizd for natural language database querying, automated schema analysis, and real-time data integration workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4890bbec-ae0b-5c28-9e92-ccbcf17c1eff)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** sql, database, data analysis, automation, ai workflow, composio, business intelligence, schema management
- This solution bridges the gap between raw database infrastructure and business intelligence by automating the translation of natural language requests into executable SQL queries.

---

## Who is this for?
This solution is designed for teams managing high-volume data environments who need to democratize access to database insights.

- **Data Analysts**
    - Automate routine query generation and schema exploration to focus on complex modeling tasks.
- **Product Managers**
    - Retrieve real-time usage metrics and user behavior data without waiting for engineering support.
- **Sales Operations**
    - Query CRM-linked databases to pull custom reports on deal velocity and pipeline health instantly.
- **Software Engineers**
    - Safely expose database read-only access to non-technical stakeholders through a secure, AI-governed interface.

---

## Features
- **Natural Language to SQL**
    - Translates complex business questions into optimized SQL queries using advanced LLM reasoning.
- **Schema Context Awareness**
    - Automatically maps database table structures and relationships to ensure accurate query generation.
- **Secure Execution Environment**
    - Leverages the Composio Toolset to execute queries within defined permission scopes, preventing unauthorized data access.
- **Real-time Data Retrieval**
    - Connects directly to live production or staging databases for up-to-the-minute reporting and analysis.
- **Iterative Query Refinement**
    - Allows users to clarify or adjust results through conversational follow-ups, improving accuracy over time.

---

## Use Cases
**Operational Reporting**
- Generate daily summaries of active users or transaction volumes directly from the production database.
- Create custom performance dashboards by querying specific time-windowed metrics.

**Data Exploration**
- Identify trends in customer behavior by querying event logs and user activity tables.
- Perform ad-hoc analysis on database fields to validate hypotheses without manual scripting.

**Administrative Audits**
- Quickly audit user access logs or system activity records to ensure compliance and security.
- Extract filtered lists of system records based on specific status or timestamp criteria.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the **SQL Agent** solution.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your database credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language request or database question.
- **Agent**: Processes the intent and generates the corresponding SQL syntax.
- **Composio Toolset**: Executes the generated query against your connected database.
- **Chat Output**: Returns the structured data results or human-readable summary to the user.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Show me the total number of new user signups from the last 30 days.`
- `List the top 5 products by revenue generated in the current quarter.`
- `Identify all accounts that have not logged in for more than 60 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary translator between user intent and database logic.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear system instructions regarding the database schema and read-only constraints.
- Enable "Tool Use" mode to allow the agent to invoke the Composio SQL execution functions.

### 2) Composio Toolset Node
- Authenticate using your database-specific API key or connection string.
- Define the connection scope to limit the agent to specific read-only schemas or tables.

### 3) Tool Availability
- **SQL Query Executor**: Capability to run `SELECT` statements against the database.
- **Schema Inspector**: Capability to fetch table definitions and column names for context.
- **Data Formatter**: Capability to convert raw SQL result sets into readable tables or JSON.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into account profiles and firmographics.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistency across multiple CRM platforms and data sources.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the performance and reliability of your automated data pipelines.
