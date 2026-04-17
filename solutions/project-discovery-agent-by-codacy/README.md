# Project Discovery Agent (Uplizd) - Intelligent repository and project insights

## Summary
The Project Discovery Agent leverages the Codacy API to automate the discovery, analysis, and monitoring of software projects across your organization. By integrating real-time repository data into your Uplizd workflow, this solution provides engineering teams and managers with a single source of truth for project health, code quality metrics, and development velocity, significantly reducing the manual overhead of tracking repository status.

---

## Demo
![Project Discovery Agent workflow showing Codacy API integration and repository analysis](image.png)
**Alt text (SEO-ready):** Project Discovery Agent workflow for Codacy repository analysis, automated project tracking, and engineering metrics integration on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/afd001a1-68b7-50f2-909f-ca67a5521405)

---

## Category
**Primary category:** Engineering operations
**Secondary tags:** codacy, repository management, devops, code quality, engineering metrics, automation, composio, ai workflow

This solution streamlines engineering oversight by connecting your development environment directly to intelligent analysis tools.

---

## Who is this for?
This agent is designed for technical leaders and operations teams who need granular visibility into their development lifecycle.

*   **Engineering Manager**
    *   Gain automated visibility into repository health and team productivity bottlenecks.
*   **DevOps Engineer**
    *   Standardize repository discovery and monitoring across large-scale organizational structures.
*   **Technical Lead**
    *   Identify technical debt and code quality trends before they impact release cycles.
*   **Product Operations**
    *   Track project progress and development velocity to align engineering output with product roadmaps.

---

## Features
- **Automated Repository Discovery**
  Instantly scan and index active repositories within your organization using the Codacy API.
- **Code Quality Monitoring**
  Track critical quality metrics and security vulnerabilities across multiple projects in real-time.
- **Unified Engineering Dashboard**
  Aggregate disparate repository data into a single, actionable stream for better decision-making.
- **Composio-Powered Integration**
  Utilize the Composio Toolset to bridge the gap between AI reasoning and live Codacy repository data.
- **Trend Analysis & Reporting**
  Generate automated summaries of development activity and code health trends over specific time windows.

---

## Use Cases
**Engineering Health Audits**
*   Automate weekly reports on code coverage and security issues across all active repositories.
*   Identify stalled projects or repositories with declining quality metrics for immediate intervention.

**Onboarding & Resource Allocation**
*   Quickly map project ownership and repository access levels during team scaling phases.
*   Discover legacy repositories that require maintenance or decommissioning based on activity data.

**Development Velocity Tracking**
*   Correlate repository commit frequency with project milestones to measure team output.
*   Monitor pull request turnaround times to identify bottlenecks in the code review process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import to Workspace" to load the pre-configured workflow into your builder.
3. Connect your Codacy API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your natural language queries regarding repository status.
*   **Agent**: Processes requests and determines which Codacy data points to retrieve.
*   **Composio Toolset**: Executes secure API calls to fetch real-time repository and project metrics.
*   **Chat Output**: Delivers formatted insights and summaries back to your dashboard.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
* `List all repositories that have had no commits in the last 30 days.`
* `Summarize the code quality and security health of the 'core-api' project.`
* `Identify all repositories with a code coverage score below 70%.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your technical research assistant, translating complex API data into human-readable insights.
*   Focus on identifying anomalies in repository health data.
*   Maintain a professional, data-driven tone for all engineering reports.
*   Prioritize actionable metrics like security vulnerabilities and coverage gaps.

### 2) Composio Toolset Node
*   **API Key**: Provide your Codacy API token with read-only access to your organization's repositories.
*   **Connection Scope**: Ensure the toolset is authorized to access the specific organizations or projects you wish to monitor.

### 3) Tool Availability
*   `codacy_get_repositories`: Fetch list of all active projects.
*   `codacy_get_repository_metrics`: Retrieve detailed health and quality data for specific repositories.
*   `codacy_list_issues`: Identify security and code style violations.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Comprehensive audit and monitoring for cloud infrastructure accounts.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize team workflow efficiency and daily standup data.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and gather intelligence for sales and engineering alignment.
