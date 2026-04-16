# Code Reference Tracker (Uplizd) - Automate feature flag monitoring and code repository auditing

## Summary
The Code Reference Tracker is an intelligent Uplizd AI workflow designed to scan, track, and report on feature flag usage across your codebase. By automating the discovery of stale or active flags, this solution provides engineering teams with a single source of truth for code hygiene, significantly reducing technical debt and improving deployment velocity through real-time repository visibility.

---

## Demo
![Code Reference Tracker dashboard showing active and stale feature flag usage across repositories](image.png)
**Alt text (SEO-ready):** Code Reference Tracker dashboard showing active and stale feature flag usage across repositories for Uplizd automated code auditing and feature flag management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQ5X5l/JgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQ4ucJ6AAAAElJREFUOE9jYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/347a00de-50f3-5efe-a395-27dc1138c5f9)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** code audit, feature flags, launchdarkly, engineering productivity, technical debt, repository management, automation, composio
- This solution streamlines engineering operations by integrating code repository insights with automated tracking workflows.

---

## Who is this for?
This solution is designed for engineering and product teams focused on maintaining a clean, efficient, and scalable codebase.

- **Engineering Manager**
    - Gain visibility into technical debt by identifying long-standing or abandoned feature flags.
- **DevOps Engineer**
    - Automate the auditing process to ensure environment configurations match production code states.
- **Full-Stack Developer**
    - Quickly locate where specific feature flags are referenced to safely perform cleanup tasks.
- **Product Operations Lead**
    - Track the lifecycle of feature releases to ensure timely deprecation of experimental code paths.

---

## Features
- **Automated Repository Scanning**
    - Leverages the Composio Toolset to crawl repositories and map feature flag implementations in real-time.
- **Stale Flag Detection**
    - Identifies flags that have remained inactive or unchanged beyond a defined threshold, flagging them for removal.
- **Cross-Platform Integration**
    - Connects seamlessly with LaunchDarkly and Git providers to synchronize flag status with actual code references.
- **Actionable Reporting**
    - Generates concise summaries of flag usage, providing developers with the exact file paths requiring attention.
- **Compliance & Hygiene Monitoring**
    - Ensures that feature flag usage adheres to internal coding standards and security best practices.

---

## Use Cases
**Technical Debt Reduction**
- Automatically generate a list of "zombie" flags that are no longer referenced in the active codebase.
- Trigger alerts for flags that have been enabled for production for longer than the standard release cycle.

**Release Management**
- Audit codebases before a major release to ensure all temporary feature flags are correctly configured.
- Verify that feature flag naming conventions are consistent across multiple microservices.

**Operational Auditing**
- Perform weekly automated scans to maintain high code quality and prevent configuration drift.
- Export flag usage reports to project management tools to prioritize cleanup tasks in the next sprint.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Code Reference Tracker" template.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Git repository and LaunchDarkly credentials via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the repository URL or specific flag ID to audit.
- **Agent**: Analyzes the request and determines the necessary search parameters for the repository.
- **Composio Toolset**: Executes the search and retrieval commands across your connected development tools.
- **Chat Output**: Delivers a structured report detailing flag status, locations, and recommended actions.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Scan the main branch of the 'frontend-app' repo and list all feature flags that haven't been modified in 30 days.`
- `Find all references to the 'beta-checkout-flow' flag in the current repository.`
- `Generate a cleanup report for all stale feature flags found in the 'api-service' repository.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for repository analysis.
- **Instruction Pattern:**
    - Focus on identifying code references and flag status accurately.
    - Prioritize clear, actionable output for developers.
    - Maintain context across multiple repository files to ensure comprehensive coverage.

### 2) Composio Toolset Node
- **API Key:** Ensure your Composio API key is active and has read-only access to your repositories.
- **Connection Scope:** Configure the scope to include relevant repositories and the LaunchDarkly environment.

### 3) Tool Availability
- **Repository Search:** Capability to grep or index code for specific string patterns.
- **Flag Metadata Retrieval:** Ability to fetch status, creation date, and last-modified timestamps from LaunchDarkly.
- **Report Formatting:** Ability to structure findings into Markdown or JSON for easy consumption.

---

## Related Solutions
- [../account-audit-agent-by-cloudflare/README.md](Account Audit Agent) — Automate security and configuration audits for your infrastructure.
- [../workflow-health-monitor-by-dailybot/README.md](Workflow Health Monitor) — Track the operational efficiency of your team's internal processes.
- [../admin-user-access-auditor-by-storeganise/README.md](Admin User Access Auditor) — Monitor and report on user permissions and access logs.
