# Snowflake Performance Monitor (Uplizd) - Automated query optimization and resource management

## Summary
The Snowflake Performance Monitor by Uplizd is an intelligent automation workflow designed to track, analyze, and optimize database query performance in real-time. By leveraging the Composio Toolset to interface directly with Snowflake, this solution provides database administrators and data engineers with actionable insights to reduce compute costs, identify slow-running queries, and maintain optimal warehouse health without manual intervention.

---

## Demo
![Snowflake Performance Monitor dashboard showing query latency trends and automated optimization alerts](image.png)
**Alt text (SEO-ready):** Snowflake Performance Monitor dashboard displaying query latency trends, automated optimization alerts, and database resource usage metrics within the Uplizd AI workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b9d35722-c6d3-5a71-93f5-ee9d4402aa0a)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** snowflake, database, performance monitoring, query optimization, data engineering, cloud infrastructure, composio, ai workflow
- This solution bridges the gap between raw database telemetry and automated performance tuning to ensure efficient cloud data operations.

---

## Who is this for?
This solution is designed for technical teams managing high-scale data environments who need to maintain performance while controlling cloud spend.

- **Database Administrator**
    - Automates the identification and termination of runaway queries that consume excessive credits.
- **Data Engineer**
    - Receives real-time alerts on warehouse bottlenecks to proactively scale resources.
- **FinOps Analyst**
    - Tracks query-level cost attribution to identify inefficient code patterns and optimize spend.
- **Cloud Architect**
    - Ensures consistent database performance across complex, multi-warehouse Snowflake deployments.

---

## Features
- **Real-time Query Analysis**
  Continuously monitors active query execution to detect latency spikes and performance degradation.
- **Automated Resource Scaling**
  Triggers warehouse resizing or suspension based on workload intensity and predefined performance thresholds.
- **Cost-Efficiency Insights**
  Analyzes query history to identify expensive, long-running operations that impact the monthly budget.
- **Composio-Powered Integration**
  Uses secure, authenticated connections to interact directly with Snowflake metadata and warehouse controls.
- **Proactive Alerting**
  Delivers summarized performance reports and critical alerts directly to your preferred communication channels.

---

## Use Cases
**Query Performance Optimization**
- Automatically flag queries exceeding execution time thresholds for immediate developer review.
- Suggest index or clustering key improvements based on historical query execution patterns.

**Warehouse Resource Management**
- Dynamically suspend idle warehouses to prevent unnecessary compute credit consumption.
- Scale up warehouse sizes during peak usage periods to maintain low latency for critical BI dashboards.

**Database Health Auditing**
- Generate weekly reports on top-consuming users and roles to enforce better data access hygiene.
- Monitor for "zombie" queries that persist after application-level timeouts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Snowflake credentials via the Composio integration portal.
3. Configure your target warehouse and monitoring frequency in the workflow settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled performance check requests.
- **Agent**: Processes database telemetry data and decides on optimization actions.
- **Composio Toolset**: Executes Snowflake SQL commands and retrieves system metadata.
- **Chat Output**: Returns a summary of performance findings and actions taken.

### 3) Run the Flow
Use the Playground to test your monitoring logic:
- `Analyze the top 5 most expensive queries from the last 24 hours.`
- `Check the current status of the production warehouse and identify any idle time.`
- `List all queries that took longer than 30 seconds to execute today.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a database performance analyst.
- Use a model with strong SQL reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize cost-saving actions during off-peak hours.
- Configure the agent to provide clear, human-readable explanations for every optimization action taken.

### 2) Composio Toolset Node
- Provide your Snowflake API credentials within the Composio dashboard.
- Ensure the connection scope includes `MONITOR` and `OPERATE` permissions for the target warehouses.

### 3) Tool Availability
- `snowflake_query_history`: Retrieve and filter past execution logs.
- `snowflake_warehouse_status`: Check current load and active sessions.
- `snowflake_warehouse_resize`: Adjust compute resources dynamically.
- `snowflake_query_cancel`: Terminate specific long-running or problematic processes.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track and optimize platform usage and account health metrics.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor the operational status and efficiency of your automated workflows.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security and performance audits on cloud infrastructure accounts.
