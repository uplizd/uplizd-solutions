# Heartbeat Health Checker (Uplizd) - Automated uptime and system availability monitoring

## Summary
The Heartbeat Health Checker is an automated Uplizd AI workflow designed to monitor application health signals and uptime status in real-time. By integrating directly with StatusCake, this solution provides infrastructure teams and developers with a single source of truth for system availability, ensuring pipeline velocity by alerting stakeholders immediately when heartbeat signals fail or latency thresholds are breached.

---

## Demo
![Heartbeat Health Checker workflow dashboard showing real-time uptime status and alert triggers](image.png)
**Alt text (SEO-ready):** Heartbeat Health Checker Uplizd workflow dashboard for real-time uptime monitoring, StatusCake integration, and automated system health alerting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dffeb401-05d5-5693-b41d-72680977d1b5)

---

## Category
- **Primary category:** Infrastructure monitoring
- **Secondary tags:** uptime, statuscake, health check, devops, observability, automation, api monitoring, composio
- This solution bridges the gap between raw infrastructure signals and actionable operational intelligence for modern engineering teams.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining high-availability services and infrastructure reliability.

- **Site Reliability Engineer (SRE)**
  - Automates the detection and reporting of service outages to reduce mean time to recovery (MTTR).
- **DevOps Engineer**
  - Integrates heartbeat monitoring into existing CI/CD pipelines to validate deployment health.
- **Backend Developer**
  - Monitors specific API endpoints and microservices to ensure consistent performance under load.
- **IT Operations Manager**
  - Maintains a centralized dashboard for system uptime compliance and service level agreement (SLA) reporting.

---

## Features
- **Real-time Heartbeat Monitoring**
  - Continuous polling of application endpoints to verify active status and responsiveness.
- **Automated Alerting Logic**
  - Intelligent notification triggers that filter noise and escalate critical downtime events.
- **StatusCake Integration**
  - Seamless connectivity via the Composio Toolset to pull live metrics directly from your StatusCake account.
- **Latency Threshold Analysis**
  - Tracks response time trends to identify performance degradation before a total service failure occurs.
- **Unified Alert Reporting**
  - Aggregates health data into a readable format for instant team communication and incident response.

---

## Use Cases
**Incident Response Automation**
- Automatically trigger incident tickets in your issue tracker when a heartbeat signal returns a 5xx error.
- Notify on-call engineers via Slack or email the moment a critical service heartbeat fails to check in.

**Performance Benchmarking**
- Monitor response latency over 24-hour windows to identify peak usage times and potential bottlenecks.
- Compare heartbeat success rates across different geographical regions to detect localized network issues.

**SLA Compliance Tracking**
- Generate weekly uptime reports for stakeholders to demonstrate adherence to service level agreements.
- Audit historical heartbeat logs to verify that maintenance windows were correctly accounted for in uptime metrics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Connect your StatusCake account via the Composio Toolset.
3. Configure your target endpoints and alert notification channels.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the monitoring trigger or manual health check request.
- **Agent**: Processes the status data and determines if the current state requires an alert.
- **Composio Toolset**: Executes the API calls to fetch real-time heartbeat data from StatusCake.
- **Chat Output**: Delivers the summary report or incident alert to your preferred communication channel.

### 3) Run the Flow
Use the Playground to test your monitoring setup with these prompts:
- `Check the current heartbeat status for all production endpoints.`
- `List any services that have experienced downtime in the last 60 minutes.`
- `Generate a summary report of average latency for the primary API gateway.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the intelligent bridge between raw monitoring data and actionable insights.
- Instruct the agent to prioritize critical downtime events over minor latency fluctuations.
- Define specific escalation paths based on the severity of the heartbeat failure.
- Ensure the agent formats output clearly for quick reading by on-call engineers.

### 2) Composio Toolset Node
- Provide your StatusCake API key within the Composio configuration.
- Set the connection scope to allow read-only access to your uptime tests and monitoring logs.

### 3) Tool Availability
- `get_uptime_status`: Fetches the current pass/fail state of configured heartbeat tests.
- `list_test_results`: Retrieves historical performance data for specific endpoints.
- `get_alert_history`: Pulls recent alert logs to identify recurring infrastructure issues.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the execution health of your automated workflows.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor account activity and usage patterns for SaaS products.
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Ensure your account configurations remain within compliance standards.
