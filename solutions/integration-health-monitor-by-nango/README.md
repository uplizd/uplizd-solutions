# Integration Health Monitor (Uplizd) - Proactive API connectivity and sync reliability management

## Summary
The Integration Health Monitor (Uplizd) is an automated AI workflow designed to track, diagnose, and alert on the status of your third-party API connections. By leveraging the Composio Toolset, this solution identifies latency issues, authentication failures, and data sync gaps in real-time, ensuring your operational pipelines remain resilient and your cross-platform data remains a single source of truth.

---

## Demo
![Integration Health Monitor dashboard showing real-time API status, latency metrics, and automated alert triggers for Nango-connected services.](image.png)
**Alt text (SEO-ready):** Integration Health Monitor dashboard showing real-time API status, latency metrics, and automated alert triggers for Nango-connected services on Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhL7c6xCQAgEATB5/67tAQLQyDfzYJt8mYyM5MkSZI0y/wF8J69gO+9A161F/C9t8B79gK+9w541V7A994C79kL+N474FV7AQAA//8D9y1o21321QAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/28587742-59ad-544b-8b1d-7a062cbdf613)

---

## Category
**Primary category:** Data integration  
**Secondary tags:** api monitoring, nango, data sync, health check, automation, workflow reliability, composio, system observability  
This solution provides critical observability for complex integration stacks by automating the detection and reporting of API health metrics.

---

## Who is this for?
This solution is designed for technical teams managing high-volume data pipelines who need to minimize downtime and manual troubleshooting.

* **DevOps Engineer**
    * Automates the detection of API endpoint failures before they impact downstream business processes.
* **Data Architect**
    * Ensures data integrity across platforms by monitoring sync health and identifying stale connection states.
* **RevOps Manager**
    * Reduces pipeline velocity bottlenecks caused by broken CRM or marketing automation integrations.
* **Integration Specialist**
    * Centralizes error logs and connection status reports into a single, actionable dashboard.

---

## Features
- **Real-time Connection Auditing**
  Continuous polling of API endpoints to verify authentication tokens and connectivity status.
- **Automated Latency Tracking**
  Measures response times across your integration stack to identify performance degradation early.
- **Composio-Powered Diagnostics**
  Uses the Composio Toolset to execute targeted diagnostic requests against connected Nango services.
- **Intelligent Alerting**
  Triggers notifications when specific API thresholds are breached, allowing for rapid incident response.
- **Unified Health Reporting**
  Aggregates status data from multiple providers into a single, human-readable summary for stakeholders.

---

## Use Cases
**Proactive Maintenance**
* Automatically pinging critical API endpoints every hour to verify 200 OK status codes.
* Identifying and flagging expired OAuth tokens before they cause data sync failures.

**Performance Optimization**
* Tracking average latency for high-traffic CRM integrations to identify potential rate-limiting issues.
* Analyzing historical uptime data to determine if specific integrations require infrastructure scaling.

**Incident Triage**
* Generating summary reports of failed requests to assist developers in debugging integration errors.
* Automatically re-testing failed connections after a system update to confirm resolution.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and click "Import Flow."
3. Connect your required API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger command or scheduled interval request.
* **Agent**: Processes the health check logic and interprets API response codes.
* **Composio Toolset**: Executes the specific API diagnostic calls (e.g., Nango status checks).
* **Chat Output**: Returns a formatted report of system health and identified issues.

### 3) Run the Flow
* `Check the current health status of all active CRM integrations.`
* `Run a diagnostic test on the Nango connection and report any latency spikes.`
* `List all API endpoints that have returned 4xx or 5xx errors in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for diagnostic tasks, translating natural language requests into API calls.
* **Instruction Pattern**:
    * Always prioritize verifying the connection status before reporting latency.
    * Use the Composio Toolset to fetch the latest logs for identified problematic endpoints.
    * Summarize findings in a clear, bulleted format categorized by "Healthy," "Warning," and "Critical."

### 2) Composio Toolset Node
* **API Key**: Ensure your Nango or relevant integration provider API key is injected into the environment variables.
* **Connection Scope**: Grant the agent read-only access to integration logs and status endpoints to ensure security.

### 3) Tool Availability
* **Status Checkers**: Capability to ping endpoints and verify HTTP response codes.
* **Log Aggregators**: Capability to fetch recent error logs from connected platforms.
* **Latency Analyzers**: Capability to calculate average response times over a defined window.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate data cleanup and formatting to maintain high-quality records.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor general workflow execution health and team productivity metrics.
