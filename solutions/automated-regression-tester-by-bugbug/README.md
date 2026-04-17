# Automated Regression Tester (Uplizd) - Streamline software quality with automated regression workflows

## Summary
The Automated Regression Tester (Uplizd) is an intelligent AI workflow designed to execute comprehensive regression test suites across your application deployments. By leveraging the Composio Toolset to interface with Bugbug, this solution ensures that new code changes do not compromise existing functionality, significantly reducing manual QA overhead and accelerating pipeline velocity.

---

## Demo
![Automated Regression Tester workflow diagram showing integration between Chat Input, AI Agent, Bugbug testing tools, and Chat Output](image.png)
**Alt text (SEO-ready):** Automated Regression Tester workflow for Uplizd, featuring Bugbug integration for continuous software testing, QA automation, and CI/CD pipeline validation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/db759f79-327b-5817-a337-d9be7900d4c1)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** qa, regression testing, bugbug, ci/cd, automation, software quality, devops, composio
- This solution bridges the gap between deployment and validation, ensuring high-quality software delivery through automated testing cycles.

---

## Who is this for?
This solution is designed for engineering and product teams focused on maintaining high-velocity deployment cycles without sacrificing stability.

- **QA Engineers**
    - Automate repetitive test suite execution to focus on complex edge-case exploration.
- **DevOps Engineers**
    - Integrate automated regression checks directly into the CI/CD pipeline to prevent production regressions.
- **Software Developers**
    - Receive immediate feedback on code changes, allowing for rapid iteration and debugging.
- **Product Managers**
    - Ensure consistent application performance and feature reliability throughout the release lifecycle.

---

## Features
- **Automated Test Execution**
    - Trigger full regression suites automatically upon code deployment or scheduled intervals using Bugbug.
- **Real-time Status Reporting**
    - Receive instant notifications and detailed logs via the Chat Output node regarding test pass/fail status.
- **Composio-Powered Integration**
    - Seamlessly connect the Uplizd agent to Bugbug's testing infrastructure for secure, authenticated command execution.
- **Smart Error Analysis**
    - Utilize the Agent node to interpret test failure logs and provide actionable insights for faster resolution.
- **Customizable Test Scenarios**
    - Configure specific test paths and user flows to mirror critical business logic within your application.

---

## Use Cases
**Continuous Integration Validation**
- Trigger regression tests automatically after every pull request merge to the staging environment.
- Validate critical user paths (e.g., login, checkout, profile update) before every production release.

**Automated QA Maintenance**
- Schedule daily regression runs to identify performance degradation or UI breakage early.
- Run targeted test suites for specific modules whenever underlying dependencies are updated.

**Incident Response & Debugging**
- Execute specific regression tests to verify if a reported production bug has been successfully patched.
- Compare test results across different environments to isolate environment-specific configuration issues.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Bugbug account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or test suite parameters.
- **Agent**: Processes instructions and determines which regression tests to execute.
- **Composio Toolset**: Executes the specific Bugbug commands to run tests and retrieve results.
- **Chat Output**: Delivers the final test summary and diagnostic report to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Run the full regression suite for the production environment.`
- `Execute the checkout flow test and report any failures.`
- `Check the status of the latest regression tests triggered for the staging branch.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your testing suite.
- Set the system prompt to prioritize clear, concise reporting of test outcomes.
- Enable tool-calling capabilities to allow the agent to interact with the Bugbug API.
- Configure the agent to summarize failure logs into human-readable action items.

### 2) Composio Toolset Node
- Provide your Bugbug API key within the Composio configuration settings.
- Ensure the connection scope includes permissions to trigger tests and read execution logs.

### 3) Tool Availability
- `bugbug_run_test_suite`: Initiates a predefined collection of tests.
- `bugbug_get_test_results`: Fetches detailed logs and status for a specific run.
- `bugbug_list_projects`: Retrieves available testing projects for selection.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational status of your automated workflows.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform automated security and configuration audits.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automate administrative workflows for new user setups.
