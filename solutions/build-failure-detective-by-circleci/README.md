# Build Failure Detective (Uplizd) - Automated CI/CD error diagnosis and resolution

## Summary
The Build Failure Detective is an intelligent Uplizd AI workflow designed to streamline DevOps operations by automatically analyzing CI/CD build logs, identifying root causes, and suggesting actionable fixes. By integrating directly with CircleCI, this solution reduces mean time to recovery (MTTR), eliminates manual log parsing, and ensures engineering teams maintain high pipeline velocity without constant human intervention.

---

## Demo
![Build Failure Detective dashboard showing automated log analysis and suggested code fixes](image.png)
**Alt text (SEO-ready):** Build Failure Detective Uplizd workflow showing automated CI/CD log analysis, CircleCI error detection, and AI-driven resolution suggestions.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/36cf73f8-1e85-5de5-9432-96356db3c25e)

---

## Category
**Primary category:** DevOps automation  
**Secondary tags:** ci/cd, circleci, build failure, log analysis, devops, automation, error resolution, composio  
This solution bridges the gap between raw build logs and actionable engineering insights, providing a centralized hub for automated pipeline maintenance.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to minimize downtime and improve developer experience.

* **DevOps Engineer**
    * Automates the triage of recurring build failures to reduce manual ticket volume.
* **Software Developer**
    * Receives instant, context-aware suggestions for fixing broken builds without leaving the terminal.
* **Engineering Manager**
    * Gains visibility into common failure patterns to optimize team resource allocation and pipeline stability.
* **Site Reliability Engineer (SRE)**
    * Ensures high system availability by proactively identifying and resolving CI/CD bottlenecks.

---

## Features
- **Automated Log Parsing**
  Instantly scans complex CircleCI build logs to extract relevant error stacks and failure patterns.
- **Intelligent Root Cause Analysis**
  Uses AI to correlate current build failures with historical data to identify the specific commit or configuration change responsible.
- **Actionable Fix Suggestions**
  Provides concrete code snippets or configuration adjustments directly within the chat interface to resolve issues faster.
- **Composio Toolset Integration**
  Leverages secure, authenticated connections to CI/CD platforms to fetch logs and trigger re-runs programmatically.
- **Real-time Alerting**
  Delivers concise summaries of build failures to communication channels, keeping the entire team informed of pipeline health.

---

## Use Cases
**Pipeline Maintenance**
* Automatically identifying and flagging flaky tests that cause intermittent build failures.
* Suggesting environment variable updates when builds fail due to configuration drift.

**Incident Response**
* Providing immediate diagnostic reports to on-call engineers when a critical production build fails.
* Correlating build failures with recent deployment activity to speed up rollback decisions.

**Developer Productivity**
* Reducing the time developers spend debugging local environment issues by comparing them against CI/CD logs.
* Automating the creation of Jira or GitHub issues with pre-populated error logs and suggested fixes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your CircleCI account via the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the build ID or failure notification trigger.
* **Agent**: Processes the log data and generates a diagnostic summary.
* **Composio Toolset**: Executes API calls to fetch build logs and project metadata.
* **Chat Output**: Delivers the final root cause analysis and recommended fix to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Analyze the latest build failure for project 'core-api' and suggest a fix.`
* `Why did build #4521 fail in the staging environment?`
* `Summarize the last 5 build failures and identify common patterns.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized DevOps assistant. 
* Use a model with strong reasoning capabilities (e.g., GPT-4o).
* **Instruction pattern:**
    * "You are a CI/CD expert. Analyze the provided logs to find the specific error line."
    * "Compare the error against common failure patterns and suggest the most likely fix."
    * "Maintain a technical, concise tone and always provide a link to the relevant build."

### 2) Composio Toolset Node
* Provide your CircleCI API key within the Composio dashboard.
* Ensure the connection scope includes read access to project pipelines and build logs.

### 3) Tool Availability
* **Log Fetcher**: Retrieves raw build logs from CircleCI.
* **Project Metadata**: Queries project settings and environment variables.
* **Issue Tracker**: Optional capability to log findings to GitHub Issues or Jira.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Manage and prioritize engineering tasks and incident follow-ups.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the overall health and status of team workflows.
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform automated security and configuration audits.
