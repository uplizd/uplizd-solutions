# CI/CD Health Monitor (Uplizd) - Automated pipeline performance tracking and incident response

## Summary
The CI/CD Health Monitor is an intelligent Uplizd workflow that provides real-time visibility into your deployment pipelines by tracking build status, failure rates, and deployment latency. By integrating directly with CircleCI, this solution acts as a single source of truth for engineering teams, reducing mean time to recovery (MTTR) and ensuring pipeline hygiene through automated reporting and proactive alerting.

---

## Demo
![CI/CD Health Monitor dashboard showing real-time pipeline status and incident alerts](image.png)
**Alt text (SEO-ready):** CI/CD Health Monitor dashboard showing real-time pipeline status, build failure alerts, and deployment metrics powered by Uplizd and CircleCI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f99ca3ae-dec5-5cc6-91cf-7120563d2f04)

---

## Category
**Primary category:** DevOps automation
**Secondary tags:** cicd, circleci, pipeline, monitoring, incident response, devops, automation, engineering efficiency.
This solution streamlines DevOps operations by bridging the gap between raw CI/CD telemetry and actionable engineering insights.

---

## Who is this for?
This solution is designed for engineering and DevOps teams looking to maintain high-velocity deployment cycles without sacrificing stability.

* **DevOps Engineer**
    * Automates the identification of stalled or failing deployment pipelines to minimize downtime.
* **Engineering Manager**
    * Gains high-level visibility into team deployment frequency and overall pipeline health metrics.
* **Site Reliability Engineer (SRE)**
    * Receives instant notifications on critical build failures to trigger rapid incident response.
* **Full-Stack Developer**
    * Reduces context switching by receiving automated feedback on build status directly within the workflow.

---

## Features
- **Real-time Pipeline Monitoring**
  Continuous tracking of build statuses and deployment events via CircleCI integration.
- **Automated Failure Alerts**
  Instant notifications triggered when build pipelines enter a failed or stalled state.
- **Performance Analytics**
  Aggregated reporting on deployment duration and success rates to identify bottlenecks.
- **Composio-Powered Tooling**
  Seamless execution of CI/CD commands and status checks using the robust Composio Toolset.
- **Proactive Incident Triage**
  Intelligent categorization of build errors to route issues to the correct engineering squad.

---

## Use Cases
**Pipeline Reliability**
* Automatically restart stalled build jobs that exceed expected execution time.
* Generate daily summaries of pipeline success rates for team retrospectives.

**Incident Response**
* Trigger immediate Slack or email alerts when critical production deployments fail.
* Correlate recent code commits with build failures to accelerate root cause analysis.

**Operational Hygiene**
* Identify and prune long-running or redundant CI/CD workflows to optimize resource usage.
* Monitor environment-specific deployment health across staging and production clusters.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your CircleCI account within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives natural language queries regarding pipeline status or specific build IDs.
* **Agent**: Analyzes the request and determines the necessary CI/CD diagnostic steps.
* **Composio Toolset**: Executes authorized API calls to CircleCI to fetch logs and status data.
* **Chat Output**: Delivers a human-readable summary of the pipeline health or incident details.

### 3) Run the Flow
Use the Uplizd Playground to test the agent with these prompts:
* `Check the current status of the production deployment pipeline.`
* `List all failed builds from the last 24 hours and summarize the error messages.`
* `Identify which developer triggered the most recent build failure in the staging environment.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a DevOps assistant capable of interpreting technical logs and pipeline metadata.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are a DevOps expert. Analyze CircleCI data to provide concise, actionable insights on pipeline health."
* Instruction: "If a build fails, prioritize identifying the commit hash and the specific error log snippet."

### 2) Composio Toolset Node
* Provide your CircleCI API key within the Composio configuration panel.
* Ensure the connection scope includes read/write access to your project pipelines and build logs.

### 3) Tool Availability
* `circleci_get_build_status`: Retrieves the current state of a specific build.
* `circleci_list_recent_pipelines`: Fetches a summary of recent deployment activity.
* `circleci_get_job_logs`: Extracts detailed logs for failed build steps.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks general workflow efficiency and team productivity metrics.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Monitors account-level usage patterns to ensure operational compliance.
* [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Audits user permissions and access logs to maintain system security.
