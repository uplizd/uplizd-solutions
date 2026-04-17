# Heartbeat Health Manager (Uplizd) - Intelligent service monitoring and uptime orchestration

## Summary
The Heartbeat Health Manager is an automated Uplizd workflow designed to provide real-time visibility into service availability and infrastructure health. By integrating with Better Stack, this solution enables DevOps and SRE teams to proactively monitor system pulses, automate incident response, and maintain high availability, ensuring that service interruptions are identified and addressed before they impact end-users.

---

## Demo
![Heartbeat Health Manager workflow showing Better Stack integration and automated alert routing](image.png)
**Alt text (SEO-ready):** Uplizd Heartbeat Health Manager workflow for automated service monitoring, uptime tracking, and incident response orchestration using Better Stack.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c60b6d6e-7ad1-5e5f-b20f-5c0ee06baacc)

---

## Category
**Primary category:** Infrastructure monitoring
**Secondary tags:** devops, sre, uptime, monitoring, better stack, incident management, automation, composio

This solution streamlines infrastructure reliability by connecting real-time heartbeat signals to intelligent automated notification and remediation pipelines.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining system uptime and infrastructure reliability.

*   **Site Reliability Engineer (SRE)**
    *   Automates the triage of heartbeat failures to reduce mean time to resolution (MTTR).
*   **DevOps Engineer**
    *   Integrates service health checks directly into existing notification and alerting workflows.
*   **System Administrator**
    *   Provides a centralized dashboard for monitoring the status of critical microservices and API endpoints.
*   **Technical Product Manager**
    *   Ensures service level objectives (SLOs) are met by tracking uptime trends and incident frequency.

---

## Features
- **Real-time Heartbeat Monitoring**
  Continuous polling of service endpoints to detect downtime or latency spikes immediately.
- **Automated Incident Routing**
  Intelligently routes alerts to the correct on-call personnel based on service ownership and incident severity.
- **Composio-Powered Integrations**
  Leverages the Composio Toolset to bridge Better Stack data with communication platforms like Slack or PagerDuty.
- **Historical Health Analytics**
  Aggregates uptime data to identify recurring patterns in service degradation or infrastructure instability.
- **Proactive Remediation Triggers**
  Executes automated scripts or restart commands when specific heartbeat failure conditions are met.

---

## Use Cases
**Incident Response Automation**
*   Automatically open tickets in your issue tracker when a heartbeat check returns a 5xx error.
*   Escalate critical alerts to on-call engineers via SMS or voice if the service remains down after 5 minutes.

**Service Level Monitoring**
*   Generate weekly reports on service availability percentages for internal stakeholder reviews.
*   Monitor third-party API dependencies to ensure external outages don't impact your core platform.

**Infrastructure Hygiene**
*   Identify and decommission "zombie" services that are no longer receiving traffic or heartbeat signals.
*   Sync heartbeat status labels across your monitoring stack to ensure consistent documentation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Better Stack API credentials within the integration settings.
3. Configure the destination channels for your heartbeat alerts (e.g., Slack, Email).
4. Ensure nodes are correctly mapped to your environment variables and save the workflow.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request for a health status report.
*   **Agent**: Processes the heartbeat data and determines the appropriate response or escalation path.
*   **Composio Toolset**: Executes the API calls to Better Stack to fetch logs or trigger incident updates.
*   **Chat Output**: Delivers the summary report or incident confirmation to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Check the current heartbeat status for the production API cluster.`
* `List all services that have experienced downtime in the last 24 hours.`
* `Create a summary report of all active incidents and send it to the engineering Slack channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for interpreting service health data.
*   Instruction: "Analyze the provided heartbeat data and identify any services currently reporting as down."
*   Instruction: "Prioritize incidents based on service criticality and notify the on-call engineer."
*   Instruction: "Summarize uptime metrics into a concise, actionable report for the DevOps team."

### 2) Composio Toolset Node
Requires a valid Better Stack API key with read/write permissions for monitoring and incident management scopes.

### 3) Tool Availability
*   **Service Discovery**: Fetching active heartbeat monitors.
*   **Incident Management**: Creating, updating, and closing incident tickets.
*   **Alerting**: Sending notifications to integrated communication channels.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize the performance of your automated workflows.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor account activity and usage metrics for better resource allocation.
* [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) - Proactive monitoring for organizational risk and compliance.
