# Text2Cypher Agent (Uplizd) - Natural language graph database querying and analysis

## Summary
The Text2Cypher Agent enables seamless interaction with graph databases by translating natural language queries into executable Cypher statements. By leveraging advanced LLMs and the Composio Toolset, this workflow empowers technical and non-technical users to extract complex relationship insights, visualize data connections, and perform graph-based analytics without requiring deep knowledge of query syntax, ultimately accelerating data discovery and pipeline velocity.

---

## Demo
![Text2Cypher Agent workflow diagram showing natural language input processing into Cypher queries via Composio and graph database execution](image.png)
**Alt text (SEO-ready):** Text2Cypher Agent workflow for Uplizd, enabling natural language to graph database query conversion, Cypher automation, and AI-driven data insights.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6ddcdd7d-1528-5cad-b71e-b37e120d07b0)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** graph database, cypher, neo4j, data analysis, ai workflow, composio, natural language processing, database management
- This solution bridges the gap between human intent and graph database architecture, simplifying complex data retrieval tasks.

---

## Who is this for?
This agent is designed for teams managing highly connected datasets who need to derive intelligence from complex relationships.

- **Data Analysts**
    - Rapidly query graph structures to uncover hidden patterns without writing manual Cypher code.
- **Database Administrators**
    - Automate routine data verification and relationship audits across large-scale graph environments.
- **Product Managers**
    - Gain immediate insights into user journey maps and feature adoption paths stored in graph databases.
- **Software Engineers**
    - Accelerate development cycles by using natural language to prototype and test complex graph queries.

---

## Features
- **Natural Language to Cypher**
    - Automatically converts conversational prompts into precise, syntactically correct Cypher queries for graph databases.
- **Composio Toolset Integration**
    - Seamlessly connects the agent to your database infrastructure, ensuring secure and authenticated query execution.
- **Real-time Data Exploration**
    - Enables immediate feedback loops, allowing users to iterate on queries and refine data insights instantly.
- **Complex Relationship Mapping**
    - Simplifies the retrieval of multi-hop connections and deep network dependencies within your graph data.
- **Context-Aware Querying**
    - Maintains schema awareness to ensure generated queries align with your specific node and relationship definitions.

---

## Use Cases
**Graph Data Exploration**
- Querying multi-hop relationships between entities to identify central influencers or bottlenecks.
- Visualizing user behavior paths by translating intent into specific graph traversal commands.

**Database Maintenance**
- Performing bulk audits of node properties to ensure data hygiene and consistency across the graph.
- Identifying orphaned nodes or disconnected sub-graphs that require cleanup or re-linking.

**Business Intelligence**
- Generating executive reports on network density and connectivity metrics using simple natural language prompts.
- Extracting specific sub-graphs for downstream analysis in external BI tools or data pipelines.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Text2Cypher Agent template from the solution library.
3. Connect your preferred graph database credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language request regarding the graph data.
- **Agent**: Interprets the intent and generates the corresponding Cypher query.
- **Composio Toolset**: Executes the generated query against the connected graph database.
- **Chat Output**: Returns the query results or a human-readable summary of the findings.

### 3) Run the Flow
Use the Playground to test your agent with prompts like:
- `Find all users who are connected to the 'Premium' tier and have purchased more than 3 items.`
- `List the shortest path between node A and node B in the current network.`
- `Show me all nodes that have no outgoing relationships to other entities.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a translation layer between human language and graph query logic.
- Use a high-reasoning model (e.g., Claude 3.5 Sonnet) for optimal Cypher syntax generation.
- Provide the agent with your database schema in the system prompt to improve query accuracy.
- Instruct the agent to explain the query logic before executing it to ensure transparency.

### 2) Composio Toolset Node
- Authenticate the node using your database API keys or connection strings.
- Define the scope of the connection to restrict the agent to read-only or read-write access as needed.

### 3) Tool Availability
- **Query Execution**: Ability to run read/write Cypher commands.
- **Schema Inspection**: Ability to fetch node labels and relationship types.
- **Result Formatting**: Ability to parse raw JSON responses into readable text.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on accounts and leads.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain data consistency across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Track and optimize sales pipeline stages and deal health.
