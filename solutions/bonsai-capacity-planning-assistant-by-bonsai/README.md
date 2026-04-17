# Bonsai Capacity Planning Assistant (Uplizd) - Intelligent Elasticsearch resource optimization

## Summary
The Bonsai Capacity Planning Assistant is an automated Uplizd workflow designed to streamline infrastructure management for Elasticsearch clusters. By leveraging the Composio Toolset to interface with Bonsai, this solution provides real-time resource analysis, predictive scaling recommendations, and automated cluster health monitoring, ensuring optimal performance and cost-efficiency for DevOps and SRE teams.

---

## Demo
![Bonsai Capacity Planning Assistant workflow dashboard showing resource utilization metrics and automated scaling recommendations](image.png)
**Alt text (SEO-ready):** Bonsai Capacity Planning Assistant dashboard showing Uplizd workflow, Elasticsearch resource utilization metrics, and automated scaling recommendations for DevOps teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0f034720-261c-55ff-8995-d7d75b272da0)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** elasticsearch, bonsai, capacity planning, devops, infrastructure, resource optimization, composio, ai workflow
- This solution bridges the gap between raw cluster metrics and actionable infrastructure decisions, enabling proactive resource management.

---

## Who is this for?
This assistant is designed for technical teams managing high-scale search and analytics infrastructure.

- **Site Reliability Engineer (SRE)**
    - Automates cluster health monitoring and reduces manual intervention for capacity adjustments.
- **DevOps Engineer**
    - Provides data-driven insights for right-sizing Elasticsearch nodes to balance performance and cost.
- **Database Administrator**
    - Simplifies the identification of resource bottlenecks and index performance degradation.
- **Engineering Manager**
    - Ensures infrastructure spend aligns with actual usage patterns through automated reporting and alerts.

---

## Features
- **Real-time Resource Monitoring**
    - Continuously pulls cluster health and utilization metrics directly from Bonsai to maintain an accurate state of your infrastructure.
- **Predictive Scaling Analysis**
    - Uses historical data trends to suggest optimal node counts and storage allocations before performance issues occur.
- **Automated Health Audits**
    - Performs routine checks on shard distribution and index health to ensure high availability and query efficiency.
- **Composio-Powered Integration**
    - Seamlessly connects to the Bonsai API via the Composio Toolset, allowing the agent to execute management commands securely.
- **Actionable Insight Reporting**
    - Translates complex cluster logs into human-readable summaries and actionable recommendations for immediate implementation.

---

## Use Cases
**Cluster Performance Optimization**
- Identifying and rebalancing hot nodes to prevent query latency spikes.
- Automating the cleanup of unassigned shards to restore cluster green status.

**Cost Management & Forecasting**
- Analyzing long-term storage growth to predict future hardware requirements.
- Right-sizing instance types based on actual CPU and memory consumption patterns.

**Infrastructure Reliability**
- Detecting anomalous resource consumption patterns that indicate potential service degradation.
- Generating automated incident reports when cluster thresholds are breached.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Bonsai Capacity Planning Assistant JSON template.
3. Connect your Bonsai API credentials via the integrated Composio Toolset.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and click "Deploy."

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding cluster status or scaling requests.
- **Agent**: Processes infrastructure data and generates optimization strategies.
- **Composio Toolset**: Executes authorized API calls to the Bonsai platform.
- **Chat Output**: Delivers clear, actionable summaries and recommendations back to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your assistant with these prompts:
- `Analyze the current resource utilization of my production cluster and suggest scaling actions.`
- `Are there any unassigned shards or performance bottlenecks in my Bonsai cluster?`
- `Generate a report on storage growth trends over the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an infrastructure expert, focusing on precision and technical accuracy.
- Use a model with strong logical reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide system instructions to prioritize cluster stability and cost-efficiency.
- Ensure the agent is restricted to read-only analysis unless explicit scaling permissions are granted.

### 2) Composio Toolset Node
- Authenticate using your Bonsai API Key within the Composio connection manager.
- Scope the connection to allow access only to the specific clusters required for monitoring.

### 3) Tool Availability
- **Cluster Metrics Fetcher**: Retrieves real-time CPU, RAM, and Disk usage.
- **Index Health Auditor**: Scans for shard status and index replication issues.
- **Scaling Recommendation Engine**: Calculates optimal node configurations based on load.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize the performance of your automated workflows.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform comprehensive security and resource audits on your cloud infrastructure.
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) - Analyze data usage patterns to optimize workspace resource allocation.
