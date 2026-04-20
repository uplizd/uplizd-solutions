# Test Failure Analyzer (Uplizd) - Automated root cause analysis for software testing

## Summary
The Test Failure Analyzer (Uplizd) is an intelligent automation workflow designed to ingest test logs, identify failure patterns, and provide actionable remediation insights. By integrating directly with your testing infrastructure via the Composio Toolset, this solution eliminates manual log parsing, reduces mean time to resolution (MTTR), and ensures engineering teams can focus on fixing code rather than diagnosing infrastructure noise.

---

## Demo
![Test Failure Analyzer workflow dashboard showing automated log ingestion and error classification](image.png)
**Alt text (SEO-ready):** Test Failure Analyzer workflow dashboard showing automated log ingestion, error classification, and Uplizd AI-driven root cause analysis for software testing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dba62a02-aa17-5c76-b8d5-02787b4fb834)

---

## Category
**Primary category:** Operations
**Secondary tags:** qa, testing, automation, bugbug, log analysis, devops, root cause, composio, ai workflow.
This solution streamlines the software quality assurance lifecycle by automating the diagnostic process for failed test suites.

---

## Who is this for?
This solution is designed for engineering and QA teams looking to accelerate their CI/CD pipelines through intelligent automation.

* **QA Automation Engineer**
    * Reduces time spent manually triaging flaky tests and infrastructure-related failures.
* **DevOps Engineer**
    * Automatically correlates test failures with deployment events to identify environment regressions.
* **Software Developer**
    * Receives clear, actionable summaries of code-level errors directly from test logs.
* **Engineering Manager**
    * Gains visibility into recurring failure patterns to prioritize technical debt and stability improvements.

---

## Features
- **Automated Log Ingestion**
  Seamlessly pulls raw test output from your CI/CD pipeline or testing tools like Bugbug for immediate analysis.
- **Intelligent Error Classification**
  Uses LLM-powered reasoning to distinguish between genuine code bugs, environment instability, and flaky test assertions.
- **Actionable Remediation Insights**
  Provides clear, human-readable explanations of why a test failed and suggests specific code changes to resolve the issue.
- **Real-time Alerting**
  Triggers notifications via integrated communication channels as soon as a critical failure pattern is detected.
- **Historical Trend Analysis**
  Maintains a record of failure types to help teams identify long-term stability trends across different modules.

---

## Use Cases
**Pipeline Health Monitoring**
* Automatically flagging tests that fail due to network timeouts or environment configuration issues.
* Generating daily reports on test suite stability to identify modules requiring refactoring.

**Bug Triage & Resolution**
* Mapping stack traces from failed tests to specific pull requests or recent code commits.
* Providing developers with a "fix-it" summary that highlights the exact line of code causing the regression.

**QA Process Optimization**
* Reducing the manual overhead of investigating "flaky" tests by automatically re-running and comparing results.
* Categorizing failures into "Infrastructure," "Logic Error," or "Data Mismatch" for faster routing to the correct team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Test Failure Analyzer template from the marketplace.
3. Connect your testing tool API keys within the integration settings.
4. Ensure nodes are correctly mapped to your specific log source and notification channels.

### 2) Setup the Nodes
* **Chat Input**: Receives the raw test log data or failure report link.
* **Agent**: Processes logs to identify root causes and generate remediation steps.
* **Composio Toolset**: Executes diagnostic queries and retrieves historical context from your testing environment.
* **Chat Output**: Delivers the final failure analysis and recommended fix to your team.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
* `Analyze the latest test failure logs from the 'checkout-service' pipeline and summarize the root cause.`
* `Compare the current test failure with yesterday's logs to see if this is a recurring issue.`
* `Generate a Jira ticket summary based on the identified failure in the authentication module.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized QA analyst that interprets technical logs.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate log parsing.
* Instruction: "Act as a Senior QA Automation Engineer; prioritize identifying the difference between environment noise and code regressions."
* Instruction: "Format all output with a clear 'Root Cause' section followed by 'Recommended Fix'."

### 2) Composio Toolset Node
* Provide your API key for the relevant testing platform (e.g., Bugbug, GitHub Actions, or Jenkins).
* Ensure the connection scope includes read-only access to test results and logs.

### 3) Tool Availability
* **Log Retrieval**: Fetching logs from CI/CD providers.
* **Issue Tracking**: Creating or updating tickets in Jira/Linear based on findings.
* **Notification**: Sending summaries to Slack or Microsoft Teams.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track overall pipeline performance and team productivity.
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security and configuration audits on your infrastructure.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Organize and rank technical tasks based on urgency and impact.
