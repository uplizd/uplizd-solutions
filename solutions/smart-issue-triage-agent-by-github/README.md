# Smart Issue Triage Agent (Uplizd) - Automated GitHub issue categorization and prioritization

## Summary
The Smart Issue Triage Agent streamlines software development workflows by automatically analyzing, labeling, and prioritizing incoming GitHub issues. By leveraging AI to interpret intent and urgency, this Uplizd workflow ensures that engineering teams maintain high repository hygiene, reduce manual backlog grooming, and accelerate response times for critical bugs and feature requests.

---

## Demo
![Smart Issue Triage Agent dashboard showing automated label assignment and priority scoring for GitHub issues](image.png)
**Alt text (SEO-ready):** Smart Issue Triage Agent dashboard showing automated label assignment and priority scoring for GitHub issues using Uplizd AI workflow and GitHub integrations.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f9d28851-4da3-52bb-ac5f-bdc7c4bfc09f)

---

## Category
* **Primary category:** Support automation
* **Secondary tags:** github, issue tracking, devops, ai workflow, automation, triage, backlog management, composio
* This solution bridges the gap between raw issue intake and actionable engineering tasks through intelligent classification.

---

## Who is this for?
This solution is designed for engineering and product teams looking to eliminate manual overhead in repository management.

* **Engineering Managers**
    * Maintain a clean, prioritized backlog without spending hours manually labeling incoming issues.
* **Open Source Maintainers**
    * Quickly route community contributions and bug reports to the correct team members based on issue content.
* **Product Managers**
    * Gain real-time visibility into feature request trends and recurring user pain points through automated tagging.
* **DevOps Engineers**
    * Ensure that critical infrastructure alerts or security vulnerabilities are immediately escalated to the right stakeholders.

---

## Features
- **Automated Labeling**
  Uses AI to analyze issue descriptions and automatically apply relevant tags like 'bug', 'feature request', or 'documentation'.
- **Priority Scoring**
  Evaluates the urgency of incoming requests based on keywords and context to assign priority levels automatically.
- **Intelligent Routing**
  Identifies the appropriate team or developer to assign based on the issue's technical domain and historical context.
- **Duplicate Detection**
  Scans existing open issues to identify and flag potential duplicates, reducing noise in the repository.
- **Composio-Powered Integration**
  Seamlessly connects with GitHub APIs to perform real-time updates, comments, and status changes directly from the workflow.

---

## Use Cases
**Backlog Grooming**
* Auto-tagging incoming issues with specific technical modules (e.g., 'frontend', 'api', 'database').
* Closing stale issues that have been inactive for over 90 days with a polite automated comment.

**Incident Response**
* Escalating issues containing keywords like "crash", "security", or "outage" to a high-priority Slack channel or PagerDuty.
* Assigning 'urgent' labels to issues submitted by verified premium customers or enterprise accounts.

**Community Engagement**
* Automatically thanking contributors for new issues and requesting missing information (e.g., reproduction steps).
* Routing 'good first issue' tags to community-facing dashboards to encourage new developer participation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your GitHub account via the Composio integration settings.
3. Configure your target repository URL and authentication tokens.
4. Ensure nodes are correctly mapped to your specific GitHub project environment.

### 2) Setup the Nodes
* **Chat Input**: Receives the new GitHub issue payload or manual trigger.
* **Agent**: Analyzes the issue text, intent, and urgency using your preferred LLM.
* **Composio Toolset**: Executes GitHub API actions like `add_labels`, `assign_issue`, or `post_comment`.
* **Chat Output**: Returns a summary of the actions taken to the project dashboard or logs.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Analyze the latest issue in the repository and assign the 'bug' label if it describes a crash.`
* `Prioritize all open issues that mention 'security' as 'High' and assign them to the security team.`
* `Check for duplicate issues regarding the recent login error and comment on the newest one.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical triage assistant.
* **Instruction Pattern:**
    * "You are an expert GitHub repository manager. Analyze the issue body for technical intent."
    * "Always prioritize security-related keywords and categorize by feature area."
    * "If an issue is unclear, request more information from the author via a comment."

### 2) Composio Toolset Node
* **API Key:** Provide your GitHub Personal Access Token (PAT) with repository read/write permissions.
* **Connection Scope:** Ensure the scope includes `repo` and `issues` to allow the agent to read and modify issue metadata.

### 3) Tool Availability
* `github_get_issue`: Fetch details of incoming tickets.
* `github_add_issue_labels`: Apply categorization tags.
* `github_create_issue_comment`: Communicate with contributors.
* `github_update_issue`: Modify status, priority, or assignment.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automate the ranking and assignment of tasks.
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Ensure CRM and support data meets organizational standards.
* [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Provide 24/7 automated responses to user queries.
