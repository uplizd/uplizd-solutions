# Bug Triager (Uplizd) - Automated bug categorization and prioritization

## Summary
The Bug Triager (Uplizd) workflow streamlines software development lifecycles by automatically ingesting, categorizing, and prioritizing incoming bug reports from platforms like Linear. By leveraging AI to analyze report severity and context, this solution ensures engineering teams maintain high pipeline velocity and data hygiene, transforming raw support tickets into actionable development tasks without manual intervention.

---

## Demo
![Bug Triager workflow dashboard showing automated ticket categorization and Linear integration](image.png)
**Alt text (SEO-ready):** Bug Triager workflow dashboard showing automated ticket categorization and Linear integration for software development teams on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0bebb850-f4aa-5d60-9cb2-6183ee729f39)

---

## Category
* **Primary category:** Support Operations
* **Secondary tags:** linear, bug tracking, software development, ticketing, automation, ai workflow, composio, issue management
* This solution bridges the gap between customer-reported issues and engineering backlogs, optimizing issue resolution workflows.

---

## Who is this for?
This solution is designed for technical teams looking to reduce manual triage overhead and improve response times.

* **Engineering Managers**
    * Ensures critical bugs are surfaced immediately to prevent production downtime.
* **QA Leads**
    * Automates the initial classification of incoming reports to maintain a clean, organized backlog.
* **Support Specialists**
    * Reduces the time spent manually tagging and routing tickets to the correct development squads.
* **Product Managers**
    * Provides real-time visibility into product stability and recurring user-reported issues.

---

## Features
- **Automated Severity Scoring**
  Uses AI to analyze bug descriptions and assign priority levels based on business impact.
- **Linear Integration**
  Seamlessly creates or updates issues in Linear using the Composio Toolset for real-time synchronization.
- **Intelligent Categorization**
  Automatically routes bugs to the appropriate product area or team based on keywords and context.
- **Duplicate Detection**
  Identifies and links similar bug reports to prevent redundant work and consolidate engineering effort.
- **Actionable Summary Generation**
  Condenses long-form user reports into concise technical summaries for developers.

---

## Use Cases
**Backlog Management**
* Automatically move high-priority bugs to the "Sprint" column in Linear.
* Close out duplicate reports by linking them to an existing master issue.

**Support-to-Engineering Handoff**
* Route UI-related bugs directly to the frontend team's project board.
* Flag security-related keywords for immediate escalation to the DevOps team.

**Data Hygiene**
* Standardize bug report formatting across all incoming support channels.
* Archive stale or incomplete bug reports that lack sufficient reproduction steps.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Linear account within the Composio connection prompt.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives raw bug report text from your support platform.
* **Agent**: Analyzes the report, determines severity, and maps it to the correct Linear project.
* **Composio Toolset**: Executes the creation or update of the issue within Linear.
* **Chat Output**: Confirms the successful triage and provides a link to the created issue.

### 3) Run the Flow
Use the Playground to test the triage logic with these prompts:
* `Triage this: User reports a 404 error on the checkout page when using Safari.`
* `Analyze this report: The mobile app crashes immediately after login on Android 14.`
* `Process this: Users are complaining that the dark mode toggle is not saving preferences.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent filter for your incoming stream.
* Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Act as a technical lead; analyze the input for severity, product area, and reproduction steps."
* Instruction: "If the input is missing critical information, flag it for follow-up rather than creating a ticket."

### 2) Composio Toolset Node
* Provide your Linear API key via the Composio dashboard.
* Ensure the connection scope includes `issue:create` and `issue:update` permissions.

### 3) Tool Availability
* `linear_create_issue`: For generating new tickets in the backlog.
* `linear_search_issues`: For checking existing tickets to prevent duplicates.
* `linear_update_issue`: For adding labels or changing priority on existing reports.

---

## Related Solutions
* [Action Item Prioritizer (Rootly)](../action-item-prioritizer-by-rootly/README.md) - Automates the prioritization of incoming action items and tasks.
* [Action Item Cleanup Agent (Rootly)](../action-item-cleanup-agent-by-rootly/README.md) - Maintains hygiene by cleaning up stale or resolved action items.
* [Workflow Health Monitor (DailyBot)](../workflow-health-monitor-by-dailybot/README.md) - Tracks the efficiency and health of your team's development workflows.
