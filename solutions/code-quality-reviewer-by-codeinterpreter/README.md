# Code Quality Reviewer (Uplizd) - Automated code analysis and technical debt reduction

## Summary
The Code Quality Reviewer is an automated AI workflow designed to streamline software development by providing real-time code analysis, security vulnerability detection, and style compliance. By leveraging the Composio Toolset to interface with code repositories and static analysis tools, this solution helps engineering teams maintain high code standards, reduce technical debt, and accelerate pull request reviews, serving as a single source of truth for repository health.

---

## Demo
![Code Quality Reviewer workflow interface showing automated analysis of a GitHub pull request](image.png)
**Alt text (SEO-ready):** Code Quality Reviewer Uplizd workflow showing automated static analysis, security scanning, and code improvement suggestions using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6431af58-8c0e-5561-bfd7-1005a7233a9a)

---

## Category
**Primary category:** Engineering Operations
**Secondary tags:** code quality, static analysis, devops, pull request, technical debt, automation, composio, ai workflow
This solution bridges the gap between raw code commits and production-ready standards by automating the review process.

---

## Who is this for?
This solution is designed for development teams looking to standardize code quality and reduce manual review overhead.

*   **Engineering Managers**
    *   Gain visibility into team-wide technical debt and code consistency across multiple repositories.
*   **Senior Developers**
    *   Automate the identification of common anti-patterns, allowing focus on complex architectural design.
*   **DevOps Engineers**
    *   Integrate automated quality gates directly into the CI/CD pipeline to prevent regressions.
*   **Security Analysts**
    *   Identify potential vulnerabilities and compliance issues early in the development lifecycle.

---

## Features
- **Automated Static Analysis**
  Detects syntax errors, code smells, and formatting inconsistencies using industry-standard linting rules.
- **Security Vulnerability Scanning**
  Identifies insecure coding practices and potential exploits before code is merged into the main branch.
- **Context-Aware Suggestions**
  Provides actionable refactoring advice based on the specific language and framework used in the repository.
- **Pull Request Integration**
  Automatically comments on PRs with summary reports, reducing the feedback loop between developers and reviewers.
- **Technical Debt Tracking**
  Monitors the accumulation of "TODOs" and legacy code patterns to prioritize refactoring efforts.

---

## Use Cases
**Automated Code Review**
*   Automatically flag non-compliant code formatting in new pull requests.
*   Provide immediate feedback on variable naming and function complexity to junior developers.

**Security & Compliance**
*   Scan for hardcoded secrets or sensitive API keys before code reaches production.
*   Ensure all new contributions adhere to internal security policies and dependency versioning.

**Technical Debt Management**
*   Generate reports on legacy modules that require refactoring based on complexity metrics.
*   Track the resolution of identified code smells over multiple release cycles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Code Quality Reviewer template using the provided solution ID.
3. Connect your preferred code repository provider (e.g., GitHub, GitLab) via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the repository URL, branch name, or specific file path for analysis.
*   **Agent**: Acts as the lead reviewer, interpreting analysis results and generating human-readable feedback.
*   **Composio Toolset**: Executes static analysis commands and fetches repository metadata.
*   **Chat Output**: Delivers the final review summary, including identified issues and suggested fixes.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Analyze the latest pull request in the 'main' branch and list all security vulnerabilities.`
* `Review the file 'src/auth_service.py' for code smells and suggest refactoring improvements.`
* `Generate a summary report of technical debt for the current repository.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent requires a high-reasoning model to interpret complex code structures.
*   **Instruction Pattern**: Define the persona as a "Senior Staff Engineer."
*   **Instruction Pattern**: Instruct the agent to prioritize security-critical issues over stylistic preferences.
*   **Instruction Pattern**: Ensure the output format is structured (e.g., Markdown tables) for readability.

### 2) Composio Toolset Node
*   **API Key**: Provide your Composio API key to enable secure repository access.
*   **Connection Scope**: Configure the toolset with read-only access to repositories to ensure security compliance.

### 3) Tool Availability
*   **Repository Access**: Fetching code content and file trees.
*   **Static Analysis Tools**: Running linters (e.g., ESLint, Pylint) via the toolset.
*   **PR Management**: Posting comments and status checks to GitHub/GitLab.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated auditing of cloud infrastructure and account configurations.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracking the operational efficiency and health of development workflows.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Managing and prioritizing tasks derived from technical reviews and incident reports.
