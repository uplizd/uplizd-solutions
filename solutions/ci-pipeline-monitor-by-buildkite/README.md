# CI Pipeline Monitor (Uplizd) - Proactive CI/CD health tracking and automated alerting

## Summary
The CI Pipeline Monitor (Uplizd) is an intelligent workflow designed to provide real-time visibility into your Buildkite CI/CD pipelines. By automating the monitoring of build statuses and surfacing critical failures, this solution helps DevOps and engineering teams maintain high deployment velocity, reduce mean time to recovery (MTTR), and ensure pipeline hygiene through proactive, AI-driven insights.

---

## Demo
![CI Pipeline Monitor dashboard showing real-time build status and automated Slack alerts](image.png)
**Alt text (SEO-ready):** CI Pipeline Monitor dashboard showing real-time build status and automated Slack alerts for Uplizd CI/CD workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/be5cec33-69ee-5a48-948a-825246d833f7)

---

## Category
**Primary category:** DevOps automation
**Secondary tags:** ci/cd, buildkite, pipeline monitoring, devops, automation, incident response, composio, ai workflow

This solution streamlines software delivery by integrating CI/CD telemetry directly into your team's communication and incident management stack.

---

## Who is this for?
This solution is designed for technical teams looking to minimize downtime and optimize their continuous integration processes.

*   **DevOps Engineer**
    *   Automates the detection of stalled or failing builds to reduce manual oversight.
*   **Engineering Manager**
    *   Provides high-level visibility into pipeline health and deployment frequency metrics.
*   **Software Developer**
    *   Receives instant, actionable feedback on build failures directly in their preferred chat tool.
*   **SRE (Site Reliability Engineer)**
    *   Integrates CI/CD health signals into broader incident management and alerting workflows.

---

## Features
- **Real-Time Pipeline Monitoring**
  Continuously polls Buildkite for build status updates to ensure immediate visibility into pipeline health.
- **Automated Failure Alerting**
  Triggers instant notifications when a build fails, providing context and links to the specific failed job.
- **Intelligent Build Analysis**
  Uses AI to summarize failure logs, helping developers identify the root cause faster without digging through raw logs.
- **Composio Toolset Integration**
  Leverages the Composio Toolset to securely connect with Buildkite APIs and external notification channels.
- **Customizable Thresholds**
  Configures specific alert triggers based on pipeline importance, branch names, or failure frequency.

---

## Use Cases
**Incident Response**
*   Automatically notify the on-call engineer via Slack when a production deployment pipeline fails.
*   Create a Jira ticket automatically for every critical build failure detected during the release cycle.

**Pipeline Optimization**
*   Identify and report on "flaky" tests that frequently cause pipeline instability over a 24-hour window.
*   Summarize weekly pipeline performance trends to identify bottlenecks in the CI/CD process.

**Developer Productivity**
*   Provide developers with a summary of build errors directly in their IDE or chat interface upon failure.
*   Automate the retry logic for transient network-related build failures to reduce manual intervention.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the CI Pipeline Monitor template from the solution library.
3. Connect your Buildkite API credentials via the Composio integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives manual triggers or scheduled polling signals to initiate the monitor.
*   **Agent**: Analyzes build status data and determines if an alert or summary report is required.
*   **Composio Toolset**: Executes API calls to fetch build logs and trigger external notifications.
*   **Chat Output**: Delivers the final status report or failure alert to the designated team channel.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Check the status of the 'main' branch pipeline in Buildkite.`
* `Summarize the last 5 failed builds and identify common error patterns.`
* `Alert the team if any critical pipeline has been failing for more than 10 minutes.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for interpreting CI/CD telemetry.
*   Prioritize concise, actionable summaries for build failures.
*   Maintain a neutral, professional tone when reporting pipeline health.
*   Focus on extracting error codes and commit hashes from raw log data.

### 2) Composio Toolset Node
Requires a valid Buildkite API key with read-only access to your pipeline data. Ensure the connection scope includes `read_builds` and `read_pipelines`.

### 3) Tool Availability
*   **Buildkite API**: Fetching build status, job logs, and pipeline metadata.
*   **Notification Connectors**: Sending alerts to Slack, Microsoft Teams, or PagerDuty.
*   **Issue Tracker API**: Creating tickets for persistent pipeline failures.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks general workflow health and team productivity metrics.
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Ensures account configurations remain within defined compliance standards.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically ranks and assigns tasks based on urgency and impact.
