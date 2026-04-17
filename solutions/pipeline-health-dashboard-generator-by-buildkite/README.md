# Pipeline Health Dashboard Generator (Uplizd) - Automated CI/CD performance and reliability insights

## Summary
The Pipeline Health Dashboard Generator is an intelligent Uplizd workflow that aggregates CI/CD metrics to provide real-time visibility into software delivery performance. By leveraging the Buildkite API, this solution automates the synthesis of build status, deployment frequency, and failure rates, enabling engineering teams to maintain high pipeline velocity and system hygiene through a single source of truth.

---

## Demo
![Pipeline Health Dashboard Generator workflow interface showing Buildkite data integration and automated reporting](image.png)
**Alt text (SEO-ready):** Pipeline Health Dashboard Generator (Uplizd) workflow showing CI/CD metrics, Buildkite integration, and automated engineering performance reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a6fcba7f-8548-5f9c-9635-f75dd48ceb79)

---

## Category
- **Primary category:** DevOps automation
- **Secondary tags:** ci/cd, buildkite, pipeline, engineering metrics, dashboard, automation, composio, devops
- This solution bridges the gap between raw CI/CD logs and executive-level performance reporting for modern engineering organizations.

---

## Who is this for?
This solution is designed for engineering leaders and operations teams focused on optimizing software delivery lifecycles.

- **Engineering Manager**
    - Gain immediate visibility into team velocity and identify bottlenecks in the deployment pipeline.
- **DevOps Engineer**
    - Automate the generation of reliability reports to focus on infrastructure improvements rather than manual data collection.
- **CTO / VP of Engineering**
    - Access a high-level dashboard of system health to make data-driven decisions regarding release frequency and stability.
- **Release Coordinator**
    - Monitor build success rates across multiple environments to ensure smooth and predictable production deployments.

---

## Features
- **Automated Data Aggregation**
    - Connects directly to Buildkite to pull real-time build logs and status updates without manual intervention.
- **Performance Metric Synthesis**
    - Calculates key DORA metrics including deployment frequency and mean time to recovery (MTTR) automatically.
- **Intelligent Alerting**
    - Triggers notifications when pipeline health scores drop below defined thresholds, ensuring rapid incident response.
- **Customizable Reporting**
    - Generates structured summaries of pipeline performance tailored for stakeholder review or internal engineering syncs.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely manage API authentication and data mapping between Buildkite and your reporting tools.

---

## Use Cases
**Pipeline Performance Monitoring**
- Track build success rates over 30-day windows to identify recurring infrastructure instability.
- Generate weekly reports on deployment frequency to measure the impact of recent process optimizations.

**Incident & Failure Analysis**
- Automatically correlate build failures with specific commit authors to streamline root cause analysis.
- Monitor MTTR for critical production pipelines to ensure compliance with internal service level objectives.

**Engineering Resource Planning**
- Identify "stalled" pipelines that require maintenance or dependency updates before they impact delivery.
- Visualize the distribution of build times across different microservices to allocate optimization efforts effectively.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the Pipeline Health Dashboard Generator to your workspace.
3. Connect your Buildkite API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language request for pipeline status or metric reports.
- **Agent**: Processes the request, interprets CI/CD data, and formats the dashboard output.
- **Composio Toolset**: Executes secure API calls to Buildkite to fetch specific build and pipeline metadata.
- **Chat Output**: Delivers the synthesized health report or dashboard visualization to your interface.

### 3) Run the Flow
Use the Playground to test your pipeline reporting:
- `Generate a summary of our pipeline health for the last 7 days.`
- `Which microservices have the highest failure rate in Buildkite this week?`
- `Create a performance report for the production deployment pipeline.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, translating raw JSON data into actionable engineering insights.
- Instruct the agent to prioritize DORA metrics (Deployment Frequency, Lead Time for Changes).
- Set the tone to be objective, data-driven, and concise for executive stakeholders.
- Define the output format (e.g., Markdown tables or bulleted lists) for better readability.

### 2) Composio Toolset Node
- Provide your Buildkite API Key with read-only access to your organization's pipelines.
- Configure the connection scope to include `pipelines`, `builds`, and `jobs` for comprehensive data retrieval.

### 3) Tool Availability
- **Buildkite Pipeline Fetcher**: Retrieves status and configuration for specific build pipelines.
- **Buildkite Metrics Analyzer**: Calculates success/failure ratios and duration statistics.
- **Data Formatter**: Converts raw API responses into user-friendly dashboard summaries.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor general team workflow health and daily stand-up metrics.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track account-level usage and health signals for customer success.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Audit user permissions and access logs for security compliance.
