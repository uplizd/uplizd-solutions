# Snowflake Cost Optimization Agent (Uplizd) - Automated cloud spend reduction and resource management

## Summary
The Snowflake Cost Optimization Agent is an intelligent Uplizd workflow designed to analyze, monitor, and optimize your Snowflake compute and storage usage. By leveraging real-time data from the Composio Toolset, the agent identifies idle warehouses, runaway queries, and inefficient storage patterns, providing FinOps teams and data engineers with a single source of truth to maximize cloud ROI and maintain pipeline velocity.

---

## Demo
![Snowflake Cost Optimization Agent dashboard showing real-time compute usage and cost-saving recommendations](image.png)
**Alt text (SEO-ready):** Snowflake Cost Optimization Agent dashboard showing real-time compute usage, Uplizd AI workflow, cloud cost management, and automated FinOps data analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7b824efe-b0ef-5d4d-9109-30113a02496d)

---

## Category
**Primary category:** Data Operations
**Secondary tags:** snowflake, finops, cloud cost, data engineering, automation, composio, cost optimization, sql analysis.
This solution bridges the gap between raw cloud infrastructure logs and actionable financial intelligence for data-driven organizations.

---

## Who is this for?
This agent is built for technical teams responsible for maintaining cloud efficiency and infrastructure health.

* **FinOps Analyst**
    * Automates the identification of cost-saving opportunities across complex warehouse environments.
* **Data Engineer**
    * Reduces manual overhead by proactively flagging inefficient queries and resource-heavy processes.
* **Cloud Infrastructure Manager**
    * Ensures budget compliance through real-time monitoring and automated alerts on spend spikes.
* **CTO / Engineering Lead**
    * Provides high-level visibility into cloud expenditure to support strategic resource allocation.

---

## Features
- **Automated Warehouse Auditing**
    Identify and suspend idle compute resources to prevent unnecessary consumption of credits.
- **Query Performance Analysis**
    Detect long-running or expensive SQL queries that contribute to high compute costs.
- **Storage Lifecycle Management**
    Analyze table usage patterns to suggest archiving or deletion of stale, high-cost data sets.
- **Real-time Cost Alerting**
    Receive instant notifications when daily spend thresholds are exceeded or anomalies are detected.
- **Composio-Powered Execution**
    Seamlessly execute management commands directly within Snowflake via the secure Composio Toolset.

---

## Use Cases
**Warehouse Efficiency**
* Automatically pause warehouses that have been inactive for more than 30 minutes.
* Resize underutilized warehouses to match actual workload requirements during off-peak hours.

**Query Optimization**
* Flag queries that exceed a specific credit consumption threshold for manual review.
* Identify recurring "expensive" queries that could be optimized through materialized views.

**Budget & Compliance**
* Generate weekly reports on total compute spend segmented by department or project.
* Monitor storage growth trends to forecast future capacity needs and budget requirements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Snowflake Cost Optimization template from the marketplace.
3. Connect your Snowflake credentials via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives user queries regarding cost status or optimization requests.
* **Agent:** Processes natural language instructions and maps them to specific Snowflake management tasks.
* **Composio Toolset:** Executes secure SQL commands and administrative actions within your Snowflake instance.
* **Chat Output:** Delivers clear, actionable summaries and cost-saving recommendations to the user.

### 3) Run the Flow
Use the Playground to test your agent with these example prompts:
* `Show me the top 5 most expensive warehouses from the last 7 days.`
* `Identify any idle warehouses that can be suspended to save costs.`
* `List all queries that consumed more than 10 credits in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a FinOps assistant, translating natural language into technical optimization tasks.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Set the system prompt to prioritize cost-saving and efficiency metrics.
* Ensure the agent is instructed to provide context for every recommendation made.

### 2) Composio Toolset Node
* Provide your Snowflake API credentials within the Composio connection settings.
* Scope the connection to allow read-only access for analytics and specific administrative permissions for warehouse management.

### 3) Tool Availability
* **Warehouse Management:** Ability to list, describe, and modify warehouse states.
* **Query History:** Access to metadata regarding execution time and credit consumption.
* **Storage Analytics:** Tools to scan table sizes and last-accessed timestamps.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Monitor and secure cloud account configurations.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the operational status of your automated pipelines.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Analyze platform usage and resource consumption patterns.
