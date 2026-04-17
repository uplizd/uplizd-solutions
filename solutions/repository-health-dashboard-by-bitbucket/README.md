# Repository Health Dashboard (Uplizd) - Automated code quality and repository maintenance

## Summary
The Repository Health Dashboard by Uplizd provides a centralized, automated AI workflow to monitor, analyze, and maintain the integrity of your Bitbucket repositories. By leveraging real-time data ingestion and intelligent analysis, this solution ensures your codebase remains clean, compliant, and performant, effectively reducing technical debt and improving developer velocity through proactive health reporting.

---

## Demo
![Repository Health Dashboard interface showing automated code quality metrics and repository status alerts](image.png)
**Alt text (SEO-ready):** Repository Health Dashboard by Uplizd, automated code quality monitoring, Bitbucket repository analytics, and AI-driven software development lifecycle management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/d24f92fa-0eab-513b-847c-510ba636f86a)

---

## Category
**Primary category:** DevOps automation
**Secondary tags:** bitbucket, repository health, code quality, technical debt, automation, developer productivity, composio, ai workflow

This solution streamlines DevOps operations by providing actionable insights into repository health and automating routine maintenance tasks.

---

## Who is this for?
This solution is designed for technical teams looking to optimize their development lifecycle and maintain high standards of code hygiene.

- **Engineering Manager**
    - Gain visibility into team velocity and identify bottlenecks in repository maintenance.
- **DevOps Engineer**
    - Automate compliance checks and ensure repository configurations meet organizational standards.
- **Software Developer**
    - Receive automated feedback on code quality and reduce time spent on manual repository cleanup.
- **Technical Lead**
    - Monitor technical debt trends and enforce consistent coding standards across multiple projects.

---

## Features
- **Automated Health Monitoring**
    - Continuously track repository metrics and status updates using real-time API integrations.
- **Intelligent Issue Detection**
    - Identify stalled PRs, stale branches, and documentation gaps using AI-driven analysis.
- **Composio Toolset Integration**
    - Seamlessly connect with Bitbucket and other development tools to execute corrective actions.
- **Customizable Alerting**
    - Configure automated notifications for critical repository health events and compliance violations.
- **Actionable Reporting**
    - Generate comprehensive summaries of repository health to inform sprint planning and resource allocation.

---

## Use Cases
**Repository Maintenance**
- Automatically archive or prune stale branches that have been inactive for over 30 days.
- Flag repositories missing essential documentation files like README.md or CONTRIBUTING.md.

**Code Quality Assurance**
- Trigger automated code reviews for pull requests that exceed defined complexity thresholds.
- Identify and report on high-risk code segments that lack sufficient unit test coverage.

**Compliance & Security**
- Audit repository access permissions to ensure adherence to internal security policies.
- Detect and alert on hardcoded secrets or sensitive information accidentally committed to the codebase.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Repository Health Dashboard to your workspace.
3. Connect your Bitbucket account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries or scheduled triggers for repository analysis.
- **Agent**: Processes repository data and applies logic to evaluate health metrics.
- **Composio Toolset**: Executes API calls to Bitbucket for data retrieval and repository management.
- **Chat Output**: Delivers actionable reports and status summaries to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Analyze the health of the 'main' repository and list any stale branches.`
- `Generate a report on pull request turnaround time for the last 14 days.`
- `Identify repositories that are missing a security policy file.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary orchestrator for repository analysis.
- Use a model with high reasoning capabilities to interpret complex repository metadata.
- Configure the system prompt to prioritize security, performance, and maintainability metrics.
- Ensure the agent is instructed to format output as clear, actionable bullet points.

### 2) Composio Toolset Node
- Provide your Bitbucket API credentials within the Composio dashboard.
- Set the connection scope to include read/write access for repository metadata and pull request management.

### 3) Tool Availability
- **Repository Metadata Fetcher**: Retrieves branch status, commit history, and contributor data.
- **Pull Request Manager**: Analyzes PR lifecycle and identifies bottlenecks.
- **Compliance Scanner**: Audits repository settings against predefined security benchmarks.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize general team workflow efficiency.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform comprehensive security and configuration audits.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Manage and rank tasks derived from repository and incident data.
