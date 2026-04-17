# Project Cleanup Manager (Uplizd) - Automate error tracking hygiene and obsolete data management

## Summary
The Project Cleanup Manager is an intelligent Uplizd AI workflow designed to maintain pristine error tracking environments by automatically identifying and purging obsolete data, stale configurations, and resolved issue logs. By leveraging the Bugsnag integration, this solution reduces technical debt, optimizes storage usage, and ensures engineering teams focus only on active, high-priority stability issues.

---

## Demo
![Project Cleanup Manager dashboard showing automated issue archival and stale data removal workflows](image.png)
**Alt text (SEO-ready):** Project Cleanup Manager Uplizd workflow for Bugsnag error tracking, automated data hygiene, and technical debt reduction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/679a7edc-33f9-5f5c-ab44-98f7b8823e2f)

---

## Category
- **Primary category:** Data Hygiene
- **Secondary tags:** bugsnag, technical debt, error tracking, automation, data cleanup, devops, workflow optimization, composio
- This solution streamlines software maintenance by automating the lifecycle management of error logs and project configurations.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to maintain high-signal error tracking environments.

- **Engineering Manager**
  - Reduces noise in error reports to ensure team velocity is spent on critical bugs rather than stale issues.
- **DevOps Engineer**
  - Automates the cleanup of obsolete project configurations and environment-specific data to optimize storage.
- **QA Lead**
  - Ensures that bug tracking dashboards remain accurate by purging resolved or irrelevant issue data automatically.
- **Site Reliability Engineer (SRE)**
  - Maintains system health by enforcing data retention policies across multiple Bugsnag projects.

---

## Features
- **Automated Issue Archival**
  - Automatically moves resolved or stale error reports to archives based on customizable age thresholds.
- **Obsolete Data Purging**
  - Identifies and removes orphaned project configurations that no longer map to active application environments.
- **Custom Retention Policies**
  - Allows users to define specific time-to-live (TTL) settings for error logs to ensure compliance and storage efficiency.
- **Real-time Bugsnag Sync**
  - Uses the Composio Toolset to interface directly with Bugsnag APIs for instant, reliable data updates.
- **Intelligent Noise Reduction**
  - Filters out recurring low-priority exceptions, keeping the primary error feed clean and actionable.

---

## Use Cases
**Environment Maintenance**
- Automatically archive error logs older than 90 days to maintain a clean Bugsnag dashboard.
- Remove stale environment configurations that are no longer referenced by active deployment pipelines.

**Technical Debt Management**
- Identify and flag high-frequency, low-impact errors that should be suppressed or grouped.
- Batch-process the closure of resolved issues that have remained open in the system for over a month.

**Compliance and Storage Optimization**
- Enforce data retention policies to ensure sensitive error data is purged according to internal security guidelines.
- Reduce Bugsnag storage costs by programmatically deleting non-essential diagnostic metadata.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Project Cleanup Manager template from the solution library.
3. Connect your Bugsnag API credentials via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled cleanup commands.
- **Agent**: Processes instructions to identify stale data based on defined logic.
- **Composio Toolset**: Executes API calls to Bugsnag to archive or delete targeted items.
- **Chat Output**: Returns a summary report of all cleaned items and actions taken.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Clean up all resolved issues in the 'Production' project older than 30 days.`
- `List all stale project configurations and remove those not updated in 6 months.`
- `Run a full environment audit and report back on the number of items archived.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for data lifecycle management.
- Use a model with high reasoning capabilities to interpret cleanup criteria accurately.
- Instructions should emphasize safety: "Always verify the project scope before executing deletion commands."
- Ensure the agent provides a clear audit log of every action performed in the output.

### 2) Composio Toolset Node
- Provide a valid Bugsnag API key with `read` and `write` permissions.
- Set the connection scope to include project management and error reporting modules.

### 3) Tool Availability
- `bugsnag_list_projects`: Fetch active project IDs.
- `bugsnag_get_errors`: Retrieve error logs based on status and timestamp.
- `bugsnag_archive_issue`: Move specific issues to the archive state.
- `bugsnag_delete_config`: Remove obsolete environment settings.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automate the resolution and cleanup of stale action items.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform comprehensive security and configuration audits.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track and maintain the operational health of your automated workflows.
