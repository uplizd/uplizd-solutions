# Feature Rollback Guardian (Uplizd) - Automated feature flag safety and instant rollback

## Summary
The Feature Rollback Guardian is an intelligent Uplizd workflow designed to monitor deployment health and trigger automated rollbacks via LaunchDarkly when anomalies are detected. By integrating real-time observability with feature management, this solution minimizes downtime, reduces manual intervention during incidents, and ensures that high-risk feature releases do not compromise system stability.

---

## Demo
![Feature Rollback Guardian workflow showing monitoring, anomaly detection, and automated LaunchDarkly flag toggling](image.png)
**Alt text (SEO-ready):** Feature Rollback Guardian Uplizd workflow, automated LaunchDarkly feature flag rollback, incident response automation, and deployment safety monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0b995b05-5ac5-57e1-be45-8f15cb4b451c)

---

## Category
- **Primary category**: Operations
- **Secondary tags**: devops, launchdarkly, feature-flags, incident-response, automation, site-reliability, deployment, composio
- This solution bridges the gap between observability tools and feature management to provide automated safety nets for modern CI/CD pipelines.

---

## Who is this for?
This workflow is designed for engineering and operations teams focused on maintaining high availability and rapid deployment cycles.

- **Site Reliability Engineers (SREs)**
    - Automate incident mitigation by triggering rollbacks before manual intervention is required.
- **DevOps Engineers**
    - Standardize deployment safety protocols across microservices using centralized feature flag controls.
- **Product Managers**
    - Reduce the fear of deployment-related outages, allowing for faster feature iteration and testing.
- **Engineering Managers**
    - Improve system reliability metrics and reduce the "Mean Time to Recovery" (MTTR) for feature-related bugs.

---

## Features
- **Automated Anomaly Detection**
    - Integrates with monitoring signals to identify performance regressions immediately after a feature flag is enabled.
- **Instant Rollback Execution**
    - Utilizes the Composio Toolset to communicate directly with LaunchDarkly, toggling flags to a "safe" state in milliseconds.
- **Context-Aware Notifications**
    - Automatically alerts the relevant Slack or PagerDuty channels with the specific flag name and reason for the rollback.
- **Audit Trail Logging**
    - Maintains a comprehensive log of every automated rollback event, including the trigger event and the resulting flag status.
- **Configurable Safety Thresholds**
    - Allows teams to define custom error rates or latency thresholds that trigger the guardian workflow.

---

## Use Cases
**Deployment Safety**
- Automatically disable a new feature flag if the error rate exceeds 5% within the first 10 minutes of a canary release.
- Roll back a UI component flag if latency metrics spike above the defined SLA threshold for the production environment.

**Incident Response**
- Trigger a global rollback of all experimental flags during a confirmed system-wide outage to reduce complexity.
- Revert a specific configuration flag when a critical bug is reported by the customer support team via the ticketing system.

**Environment Hygiene**
- Automatically disable stale feature flags that have been active for more than 30 days without usage.
- Ensure that "kill-switch" flags are correctly toggled during emergency maintenance windows without manual dashboard access.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Feature Rollback Guardian JSON template provided in this repository.
3. Connect your LaunchDarkly API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal from your monitoring tool or manual user request.
- **Agent**: Analyzes the incoming alert, determines the appropriate flag to target, and formulates the rollback command.
- **Composio Toolset**: Executes the API call to LaunchDarkly to update the flag status.
- **Chat Output**: Confirms the rollback action and logs the status update to your team's communication channel.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Roll back the 'new-checkout-flow' flag in the production environment immediately.`
- `Check the status of all active flags and disable any that are causing high error rates.`
- `Revert the 'beta-dashboard-ui' flag to the last known stable state.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for the rollback process.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on identifying flag names from natural language input.
- Define strict constraints to prevent unauthorized or accidental flag toggling.

### 2) Composio Toolset Node
- Provide a valid LaunchDarkly API Key with "Writer" permissions for the target environments.
- Ensure the connection scope is limited to the specific project and environment keys required for the workflow.

### 3) Tool Availability
- **LaunchDarkly Flag Manager**: List, update, and toggle feature flags.
- **Monitoring Integration**: Query error rates and latency metrics from your observability provider.
- **Notification Service**: Send alerts to Slack, Microsoft Teams, or PagerDuty.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automate security and configuration audits for cloud infrastructure.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and report on the status of automated business processes.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and prioritize incident response tasks automatically.
