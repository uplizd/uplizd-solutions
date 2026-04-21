# Visual Bug Reporter (Uplizd) - Automated UI issue documentation and evidence capture

## Summary
The Visual Bug Reporter (Uplizd) is an automated AI workflow designed to streamline the quality assurance process by capturing, documenting, and categorizing UI bugs in real-time. By integrating screenshot capture tools with issue tracking systems, this solution eliminates manual reporting friction, ensuring engineering teams receive high-fidelity, actionable evidence for every reported defect.

---

## Demo
![Visual Bug Reporter workflow capturing a UI defect and logging it to a project management tool](image.png)
**Alt text (SEO-ready):** Visual Bug Reporter Uplizd workflow, automated UI bug documentation, screenshot-based issue tracking, and Composio integration for QA teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/93e2c044-4866-53b2-b343-420920ae348f)

---

## Category
**Primary category:** Quality Assurance & Testing
**Secondary tags:** `qa`, `bug tracking`, `ui testing`, `screenshotone`, `composio`, `automation`, `engineering productivity`, `issue management`

This solution bridges the gap between visual UI defects and technical issue tracking to accelerate the bug resolution lifecycle.

---

## Who is this for?
This workflow is designed for product and engineering teams looking to reduce the time spent on manual bug reproduction.

* **QA Engineer**
    * Automatically generates detailed bug tickets with visual evidence, reducing time spent on manual documentation.
* **Frontend Developer**
    * Receives precise, annotated screenshots and environment context to reproduce and fix UI issues faster.
* **Product Manager**
    * Maintains a cleaner, more accurate backlog by ensuring all reported bugs are standardized and verified.
* **Customer Support Lead**
    * Enables frontline staff to report visual glitches directly from the user interface without needing technical expertise.

---

## Features
- **Automated Screenshot Capture**
    Instantly capture the current state of a web element or page upon triggering the workflow.
- **Visual Evidence Annotation**
    Automatically highlight or mark the specific UI area where the bug occurred for immediate developer clarity.
- **Contextual Metadata Injection**
    Automatically attach browser version, URL, and timestamp to every bug report for easier debugging.
- **Seamless Issue Integration**
    Use the Composio Toolset to push reports directly into Jira, GitHub Issues, or Linear.
- **Real-time Notification Alerts**
    Instantly notify the relevant engineering channel in Slack or Microsoft Teams once a bug is logged.

---

## Use Cases
**Bug Reporting & Triage**
* Automatically convert user-reported visual glitches into structured tickets in your project management tool.
* Route high-priority UI bugs to the correct frontend squad based on the page URL or component tag.

**QA Automation Cycles**
* Trigger the reporter during automated regression tests to document visual regressions.
* Compare current UI states against baseline screenshots to identify layout shifts or broken components.

**Customer Feedback Loops**
* Allow beta testers to submit visual bug reports directly from the application interface.
* Consolidate feedback from multiple channels into a single, searchable source of truth for the development team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in your workspace.
2. Connect your preferred issue tracking provider (e.g., Jira, GitHub) via the Composio Toolset.
3. Configure the trigger mechanism (e.g., API webhook or manual button).
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives the bug description and trigger signal from the user or system.
* **Agent**: Analyzes the visual data and formats the bug report with technical context.
* **Composio Toolset**: Executes the API calls to create the issue in your tracking platform.
* **Chat Output**: Confirms the successful creation of the ticket and provides a link to the issue.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Report a visual bug on the checkout page: the submit button is overlapping the footer.`
* `Capture the current screen and create a high-priority bug ticket in GitHub for the navigation menu.`
* `Document the layout shift observed on the dashboard and assign it to the frontend team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the technical translator between visual input and structured issue data.
* Use a model capable of vision processing to interpret screenshot content.
* Instruct the agent to extract specific UI elements and describe the visual discrepancy.
* Ensure the agent enforces a consistent schema for ticket titles and severity levels.

### 2) Composio Toolset Node
* Provide your API key for the target issue tracking platform (e.g., Jira or GitHub).
* Set the connection scope to allow the agent to create issues and attach files.

### 3) Tool Availability
* **ScreenshotOne**: For high-fidelity page captures.
* **Jira/GitHub/Linear API**: For ticket creation and management.
* **Slack/Teams API**: For automated status updates and team alerts.

---

## Related Solutions
* [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) — Automate UI accessibility checks and compliance reporting.
* [AB Test Visual Documenter](../ab-test-visual-documenter-by-apiflash/README.md) — Capture and document visual states for A/B test variations.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the status and performance of your automated engineering workflows.
