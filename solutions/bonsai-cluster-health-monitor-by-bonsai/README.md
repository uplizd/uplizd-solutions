# Bonsai Cluster Health Monitor (Uplizd) - Automated Elasticsearch infrastructure observability

## Summary
The Bonsai Cluster Health Monitor is an intelligent Uplizd AI workflow designed to provide real-time observability and automated alerting for your Elasticsearch clusters. By leveraging the Composio Toolset to interface with infrastructure metrics, this solution enables DevOps and SRE teams to maintain high availability, proactively identify performance bottlenecks, and ensure data integrity without manual intervention.

---

## Demo
![Bonsai Cluster Health Monitor dashboard showing real-time node status and latency alerts](image.png)
**Alt text (SEO-ready):** Bonsai Cluster Health Monitor dashboard showing real-time node status, latency alerts, and infrastructure performance metrics within the Uplizd AI workflow.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bonsai-cluster-health-monitor)

---

## Category
**Primary category:** DevOps & Infrastructure
**Secondary tags:** elasticsearch, observability, monitoring, sre, infrastructure, automation, composio, ai workflow

This solution bridges the gap between raw cluster telemetry and actionable infrastructure insights, streamlining the maintenance of complex data environments.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining high-performance data clusters and ensuring system reliability.

* **Site Reliability Engineer (SRE)**
    * Automates incident response and reduces mean time to resolution (MTTR) for cluster latency issues.
* **DevOps Engineer**
    * Streamlines infrastructure monitoring by centralizing health checks across multiple Elasticsearch environments.
* **Database Administrator**
    * Ensures data integrity and node availability through proactive monitoring of shard distribution and disk usage.
* **System Architect**
    * Gains visibility into resource utilization patterns to optimize cluster scaling and cost-efficiency.

---

## Features
- **Real-time Health Monitoring**
  Continuously polls cluster status to detect node failures or connectivity issues before they impact end-users.
- **Automated Latency Alerts**
  Identifies performance degradation in query execution times and triggers notifications via the Composio Toolset.
- **Infrastructure Insight Generation**
  Synthesizes complex metric data into human-readable summaries for rapid decision-making.
- **Proactive Resource Management**
  Tracks disk space and memory usage trends to prevent capacity-related outages.
- **Seamless Composio Integration**
  Connects directly to your infrastructure stack to execute diagnostic commands and retrieve live cluster state.

---

## Use Cases
**Incident Response**
* Automatically trigger alerts when node heartbeat signals are lost or latency exceeds defined thresholds.
* Generate diagnostic reports during outages to provide immediate context to on-call engineers.

**Performance Optimization**
* Analyze query execution patterns to identify slow-running requests that impact cluster throughput.
* Monitor shard allocation efficiency to ensure balanced data distribution across all available nodes.

**Capacity Planning**
* Track long-term storage consumption trends to forecast hardware or cloud resource requirements.
* Identify underutilized nodes to consolidate workloads and reduce operational overhead.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project environment.
3. Authenticate your Elasticsearch and notification service credentials within the integration manager.
4. Ensure nodes are correctly mapped to your specific cluster endpoints and notification channels.

### 2) Setup the Nodes
* **Chat Input**: Receives natural language queries or manual health check triggers.
* **Agent**: Processes infrastructure data and interprets cluster health status.
* **Composio Toolset**: Executes API calls to fetch metrics and perform diagnostic tasks.
* **Chat Output**: Delivers clear, actionable health summaries and incident reports.

### 3) Run the Flow
Use the Playground to test your monitor with these prompts:
* `Check the current health status of the production cluster and list any nodes with high latency.`
* `Analyze disk usage trends for the last 24 hours and alert if we are approaching capacity.`
* `Run a diagnostic check on the primary shard distribution and report any unassigned shards.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your infrastructure data.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Provide system instructions to prioritize critical errors over informational logs.
* Configure the temperature to 0.2 for consistent, fact-based infrastructure reporting.

### 2) Composio Toolset Node
Connect your Elasticsearch API keys and ensure the scope includes read-only access to cluster metrics and health endpoints.

### 3) Tool Availability
* **Cluster Metrics API**: Fetches node status, CPU, and memory usage.
* **Shard Management API**: Monitors shard health and rebalancing tasks.
* **Alerting Service**: Dispatches notifications via Slack, PagerDuty, or email.

---

## Related Solutions
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks account activity and usage metrics.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitors the operational status of automated workflows.
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Audits infrastructure access and security configurations.
