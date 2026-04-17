# GitLab CI/CD Job Monitor (Uplizd) - Automated pipeline oversight and maintenance

## Summary
The GitLab CI/CD Job Monitor is an intelligent Uplizd workflow designed to track, analyze, and manage pipeline execution status in real-time. By leveraging the Composio Toolset to interface with GitLab APIs, this solution enables DevOps teams to maintain pipeline velocity, identify stalled jobs, and automate cleanup tasks, ensuring a reliable and efficient continuous integration environment.

---

## Demo
![GitLab CI/CD Job Monitor dashboard showing active pipeline status and automated cleanup logs](image.png)
**Alt text (SEO-ready):** GitLab CI/CD Job Monitor dashboard showing active pipeline status, automated cleanup logs, and Uplizd workflow integration for DevOps pipeline management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=git)](https://uplizd.ai/solutions/33b30a65-7dfa-5946-b305-ea3667b49d95)

---

## Category
**Primary category:** DevOps automation
**Secondary tags:** gitlab, ci/cd, pipeline, automation, devops, workflow, composio, monitoring
This solution streamlines software delivery by providing automated oversight of CI/CD pipelines, reducing manual intervention in build management.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to optimize their software delivery lifecycle.

- **DevOps Engineer**
    - Automates the identification and resolution of stalled or failed pipeline jobs.
- **Engineering Manager**
    - Gains visibility into pipeline health and resource utilization across multiple projects.
- **QA Automation Lead**
    - Ensures consistent test execution by monitoring job status and triggering re-runs when necessary.
- **Site Reliability Engineer (SRE)**
    - Reduces mean time to recovery (MTTR) by proactively managing CI/CD pipeline bottlenecks.

---

## Features
- **Real-time Pipeline Monitoring**
    - Automatically polls GitLab for active job statuses to provide instant visibility into build health.
- **Automated Job Cleanup**
    - Triggers intelligent cleanup routines for stale or redundant jobs to optimize runner usage.
- **Intelligent Failure Analysis**
    - Uses AI to categorize common build errors and suggest remediation steps for developers.
- **Composio-Powered Integration**
    - Seamlessly connects with GitLab APIs to execute commands securely without manual authentication overhead.
- **Customizable Alerting**
    - Routes pipeline status updates and critical failure notifications to preferred communication channels.

---

## Use Cases
**Pipeline Health Management**
- Automatically detect and alert on jobs that have exceeded their expected execution time.
- Trigger automated retries for transient network-related build failures.

**Resource Optimization**
- Identify and cancel orphaned jobs that are consuming unnecessary runner minutes.
- Archive logs from completed pipelines to maintain a clean and searchable history.

**DevOps Workflow Integration**
- Sync pipeline status updates directly into project management tools for better visibility.
- Generate weekly reports on pipeline success rates and common failure patterns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the CI/CD monitor workflow.
3. Connect your GitLab account via the Composio Toolset configuration.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries or trigger signals for pipeline status checks.
- **Agent**: Processes logic to interpret pipeline data and determine necessary actions.
- **Composio Toolset**: Executes authorized GitLab API calls to fetch job data or trigger pipeline actions.
- **Chat Output**: Delivers actionable summaries and status reports back to the user.

### 3) Run the Flow
Use the Uplizd Playground to test the workflow with the following prompts:
`"List all currently running jobs in the main repository."`
`"Identify and cancel any jobs that have been stuck for more than 30 minutes."`
`"Summarize the failure rate for the last 10 pipelines in the staging environment."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for pipeline analysis.
- Use a high-reasoning model to ensure accurate interpretation of API responses.
- Instruct the agent to prioritize critical pipeline failures over routine status updates.
- Configure the system prompt to maintain a professional, DevOps-focused tone.

### 2) Composio Toolset Node
- Provide your GitLab Personal Access Token with `api` and `read_repository` scopes.
- Ensure the connection is scoped to the specific GitLab groups or projects you intend to monitor.

### 3) Tool Availability
- `gitlab_list_jobs`: Retrieve status and metadata for pipeline jobs.
- `gitlab_cancel_job`: Terminate specific jobs based on ID or status.
- `gitlab_retry_job`: Restart failed jobs automatically.
- `gitlab_get_pipeline_details`: Fetch comprehensive logs and performance metrics.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track and optimize general team workflow performance.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security and configuration audits across infrastructure.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Manage and prioritize incident response action items.
