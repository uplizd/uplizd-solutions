# Smart Test Scheduler (Uplizd) - Intelligent test execution and prioritization

## Summary
The Smart Test Scheduler (Uplizd) automates the prioritization and execution of software tests by analyzing recent code changes and system health. By integrating directly with your CI/CD pipeline and testing frameworks, this workflow ensures that critical paths are validated immediately after commits, reducing feedback loops and improving overall deployment velocity for engineering teams.

---

## Demo
![Smart Test Scheduler workflow dashboard showing automated test prioritization based on code commit analysis](image.png)
**Alt text (SEO-ready):** Smart Test Scheduler workflow in Uplizd for automated test prioritization, CI/CD pipeline integration, and Bugbug testing automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/bc893d76-c70e-5b5e-a2c1-53a3ecdaf39e)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** qa, testing, ci/cd, bugbug, automation, software engineering, pipeline, devops
- This solution streamlines quality assurance by dynamically mapping code changes to relevant test suites, ensuring high-coverage testing without manual intervention.

---

## Who is this for?
This workflow is designed for engineering and QA teams looking to optimize their testing cycles and reduce build times.

- **QA Engineer**
    - Automates the selection of regression test suites based on the specific modules impacted by new code.
- **DevOps Engineer**
    - Reduces CI/CD pipeline bottlenecks by triggering only the necessary tests for each deployment.
- **Software Developer**
    - Receives faster feedback on code changes, allowing for quicker iteration and fewer production bugs.
- **Engineering Manager**
    - Gains visibility into test coverage and pipeline health through automated reporting and status tracking.

---

## Features
- **Intelligent Change Analysis**
    - Automatically parses git diffs to identify which application components were modified.
- **Dynamic Test Prioritization**
    - Uses the Composio Toolset to interface with Bugbug and rank tests by criticality and relevance.
- **Automated Execution Trigger**
    - Initiates targeted test runs immediately upon code merge or pull request creation.
- **Real-time Status Sync**
    - Updates testing status and results back into your project management or communication tools.
- **Failure Impact Reporting**
    - Provides concise summaries of failed tests, highlighting the specific code changes that likely caused the regression.

---

## Use Cases
**Regression Testing Optimization**
- Automatically run a subset of high-priority smoke tests for minor UI changes.
- Skip irrelevant test suites when documentation or non-functional code is updated.

**CI/CD Pipeline Acceleration**
- Trigger specific Bugbug test scenarios immediately after a successful build in your CI environment.
- Prevent deployment to staging if critical path tests fail during the automated scheduling phase.

**Quality Assurance Hygiene**
- Schedule comprehensive full-suite regression tests during off-peak hours to save compute resources.
- Generate daily reports on test flakiness and execution trends to inform future development sprints.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your Bugbug and Git provider connections within the integration settings.
4. Ensure nodes are correctly mapped to your specific environment variables and API endpoints.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event (e.g., Pull Request ID or Commit Hash).
- **Agent**: Analyzes the input and determines which test suites are required.
- **Composio Toolset**: Executes the specific test commands via the Bugbug API.
- **Chat Output**: Delivers the test execution report and status summary to your team.

### 3) Run the Flow
Use the Playground to test the scheduler with the following prompts:
- `Run all critical smoke tests for the latest commit on the develop branch.`
- `Analyze the recent changes in PR #402 and trigger relevant regression tests.`
- `Provide a status report on the last scheduled test execution for the payment module.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for test selection.
- Analyze the scope of code changes provided by the input.
- Map changes to specific test tags or categories defined in Bugbug.
- Format the final execution report for clear readability by the development team.

### 2) Composio Toolset Node
- Requires a valid Bugbug API key with permissions to trigger and monitor test runs.
- Ensure the connection scope includes read access to your repository metadata.

### 3) Tool Availability
- **Bugbug API**: For triggering test suites and fetching execution logs.
- **Git Provider API**: For retrieving commit diffs and PR metadata.
- **Notification Service**: For sending alerts on test failures or completion.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for complex business processes.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor system health and usage metrics.
- [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) - Automated quality checks for design and UI components.
