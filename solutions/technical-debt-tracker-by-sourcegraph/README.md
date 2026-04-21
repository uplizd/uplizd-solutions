# Technical Debt Tracker (Uplizd) - Automated code quality and debt prioritization

## Summary
The Technical Debt Tracker (Uplizd) is an automated AI workflow designed to identify, categorize, and prioritize technical debt within your codebase. By leveraging Sourcegraph’s powerful code search and analysis capabilities, this solution helps engineering teams maintain high code quality, reduce maintenance overhead, and ensure that architectural improvements are prioritized alongside new feature development.

---

## Demo
![Technical Debt Tracker workflow showing automated code analysis and issue prioritization](image.png)
**Alt text (SEO-ready):** Technical Debt Tracker workflow by Uplizd, demonstrating automated code analysis, Sourcegraph integration, and technical debt prioritization for engineering teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/602b6f34-f096-5ca0-aa0d-28cc4dbee10c)

---

## Category
**Primary category:** Operations
**Secondary tags:** devops, technical debt, code quality, sourcegraph, engineering management, automation, software maintenance, composio
This solution streamlines the identification of legacy code and architectural bottlenecks to improve long-term engineering velocity.

---

## Who is this for?
This solution is designed for engineering organizations looking to maintain a healthy, scalable codebase while balancing feature delivery.

* **Engineering Managers**
    * Gain visibility into the accumulation of technical debt to better plan sprint capacity and resource allocation.
* **Software Architects**
    * Identify systemic architectural issues and outdated patterns that require refactoring to ensure system stability.
* **DevOps Engineers**
    * Automate the monitoring of code health metrics to prevent performance regressions and security vulnerabilities.
* **Senior Developers**
    * Receive automated alerts regarding high-risk code segments, enabling proactive maintenance before debt becomes unmanageable.

---

## Features
- **Automated Debt Discovery**
  Utilizes Sourcegraph to scan repositories for patterns, TODOs, and deprecated code structures that signify technical debt.
- **Context-Aware Prioritization**
  Applies AI-driven logic to rank debt based on code complexity, frequency of access, and impact on system performance.
- **Composio Toolset Integration**
  Seamlessly connects with your version control and project management tools to log findings directly into your workflow.
- **Real-Time Reporting**
  Generates actionable insights and summaries, allowing teams to track the reduction of technical debt over time.
- **Customizable Thresholds**
  Allows users to define specific criteria for what constitutes "debt," ensuring the agent focuses on the most relevant areas of the codebase.

---

## Use Cases
**Codebase Health Monitoring**
* Automatically flag deprecated API calls or outdated library versions across microservices.
* Identify "code smells" and complex functions that deviate from established team standards.

**Sprint Planning & Backlog Management**
* Generate prioritized lists of refactoring tasks to be included in upcoming sprint cycles.
* Map technical debt items to specific project epics to justify refactoring time to stakeholders.

**Security & Compliance Audits**
* Detect hardcoded credentials or insecure patterns that represent critical technical debt.
* Ensure compliance with internal coding standards by flagging non-compliant patterns for immediate review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Technical Debt Tracker template from the solution library.
3. Configure your environment variables, including your Sourcegraph API key and repository access credentials.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives the repository path or specific codebase query from the user.
* **Agent**: Analyzes the input and orchestrates the search and categorization logic.
* **Composio Toolset**: Executes code search queries and interacts with project management tools to log issues.
* **Chat Output**: Delivers a structured report of identified debt and recommended remediation steps.

### 3) Run the Flow
* `Scan the 'core-api' repository for deprecated authentication patterns and prioritize them by impact.`
* `List all TODO comments in the 'frontend-ui' module that have been open for more than 30 days.`
* `Identify high-complexity functions in the 'data-processing' service that lack unit test coverage.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting code patterns and prioritizing findings based on engineering best practices.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate code interpretation.
* Instruct the agent to prioritize debt that impacts system security or performance.
* Maintain a consistent output format (e.g., Markdown tables) for all generated reports.

### 2) Composio Toolset Node
Requires a valid API key for your Sourcegraph instance and appropriate read-only scopes for your repositories. Ensure the connection is authorized to query code and, if applicable, write issues to your project management tool (e.g., Jira or GitHub Issues).

### 3) Tool Availability
* **Code Search**: Capability to perform deep semantic searches across the codebase.
* **Issue Tracker**: Capability to create or update tickets based on identified debt.
* **Documentation Parser**: Capability to read and interpret READMEs and internal engineering guidelines.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Automate security and configuration audits for your infrastructure.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the efficiency and performance of your team's operational workflows.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Organize and rank tasks from incident reports and team meetings.
