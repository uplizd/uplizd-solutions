# Bonsai Incident Response Assistant (Uplizd) - Automated Elasticsearch incident diagnosis and resolution

## Summary
The Bonsai Incident Response Assistant is an intelligent Uplizd workflow designed to streamline infrastructure reliability by automating the diagnosis and remediation of Elasticsearch incidents. By leveraging the Composio Toolset to interface with Bonsai and monitoring systems, this solution provides SREs and DevOps engineers with real-time root cause analysis and actionable mitigation steps, significantly reducing mean time to resolution (MTTR) and ensuring system uptime.

---

## Demo
![Bonsai Incident Response Assistant workflow dashboard showing automated alert analysis and remediation steps](image.png)
**Alt text (SEO-ready):** Bonsai Incident Response Assistant dashboard showing Uplizd AI workflow for automated Elasticsearch incident diagnosis, remediation, and Composio tool integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/f8ddf4f9-3234-5640-86fd-4390862c7a89)

---

## Category
**Primary category:** Operations  
**Secondary tags:** elasticsearch, bonsai, incident response, devops, sre, automation, composio, ai workflow  
This solution bridges the gap between infrastructure monitoring and automated incident response, providing a unified platform for managing cluster health.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining high-availability data infrastructure and rapid response protocols.

* **Site Reliability Engineer (SRE)**
    * Automates the initial triage process to identify cluster bottlenecks or node failures before they impact production.
* **DevOps Engineer**
    * Streamlines the execution of remediation scripts and configuration updates directly through the AI agent interface.
* **Infrastructure Manager**
    * Ensures consistent incident documentation and standardized response procedures across distributed Elasticsearch environments.
* **Cloud Operations Specialist**
    * Monitors real-time cluster health metrics and receives instant, context-aware summaries of complex system alerts.

---

## Features
- **Automated Incident Triage**
  Instantly parses incoming alerts to categorize the severity and scope of Elasticsearch cluster issues.
- **Real-time Cluster Diagnostics**
  Utilizes the Composio Toolset to query live cluster metrics, node status, and shard health for accurate root cause analysis.
- **Guided Remediation Workflows**
  Provides step-by-step resolution instructions or executes pre-approved maintenance tasks to restore service stability.
- **Context-Aware Alerting**
  Synthesizes raw log data into human-readable summaries, highlighting critical errors and performance regressions.
- **Seamless Integrations**
  Connects directly with Bonsai and external monitoring stacks to maintain a single source of truth for all infrastructure incidents.

---

## Use Cases
**Incident Management**
- Automatically generating incident tickets in Jira or PagerDuty based on detected cluster anomalies.
- Providing immediate context to on-call engineers by summarizing the last 30 minutes of cluster logs during an outage.

**Performance Optimization**
- Identifying long-running queries or resource-heavy shards that contribute to high latency.
- Suggesting index configuration changes based on current ingestion rates and search performance metrics.

**Compliance and Reporting**
- Maintaining a searchable audit trail of all incident responses and manual interventions performed by the agent.
- Generating weekly health reports that summarize cluster uptime, resolved incidents, and recurring performance trends.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd dashboard and select "Create New Workflow."
2. Import the Bonsai Incident Response Assistant template file.
3. Authenticate your Bonsai and monitoring tool credentials within the connection settings.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives incident alerts or manual troubleshooting requests from your team.
* **Agent**: Analyzes the input, queries the cluster state, and determines the appropriate remediation strategy.
* **Composio Toolset**: Executes authorized commands against your Elasticsearch/Bonsai environment.
* **Chat Output**: Delivers the final diagnosis and resolution summary back to the user.

### 3) Run the Flow
Use the Playground to test the assistant with the following prompts:
* `Analyze the current cluster health and report any nodes in a red state.`
* `Why is the search latency high for the 'customer-logs' index?`
* `Provide a summary of the last 5 critical incidents and their resolution status.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary orchestrator for infrastructure diagnostics.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) to ensure accurate interpretation of technical logs.
* Configure the system prompt to prioritize "safety-first" remediation steps.
* Set the temperature to 0.2 for consistent, fact-based output.

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure access to Bonsai and Elasticsearch APIs.
* Define the connection scope to include read-only access for diagnostics and restricted write access for remediation tasks.

### 3) Tool Availability
* **Cluster Metrics**: Retrieve node, shard, and index health.
* **Log Analysis**: Search and filter recent error logs.
* **Remediation Scripts**: Execute approved cluster maintenance commands.
* **Notification Tools**: Send updates to Slack or PagerDuty.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automates the cleanup and tracking of infrastructure action items.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Intelligent prioritization of technical debt and incident-related tasks.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and performance of automated workflows.
