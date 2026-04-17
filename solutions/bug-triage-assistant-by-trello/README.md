# Bug Triage Assistant (Uplizd) - Automated bug categorization and priority management

## Summary
The Bug Triage Assistant is an intelligent Uplizd workflow designed to streamline software development lifecycles by automatically analyzing, categorizing, and prioritizing incoming bug reports. By leveraging the Composio Toolset to interface with issue tracking platforms like Trello, this solution eliminates manual backlog grooming, ensures critical issues are escalated immediately, and maintains high pipeline velocity for engineering teams.

---

## Demo
![Bug Triage Assistant workflow showing automated issue categorization and Trello integration](image.png)

**Alt text (SEO-ready):** Bug Triage Assistant workflow for automated issue categorization, Trello bug prioritization, and Uplizd AI-driven software development pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d287305a-7f68-5548-8cdb-80462cfd15f5)

---

## Category
- **Primary category:** Support Operations
- **Secondary tags:** bug tracking, trello, issue management, devops, ai workflow, automation, software quality, composio
- This solution bridges the gap between raw user feedback and actionable engineering tasks by automating the triage process.

---

## Who is this for?
This solution is designed for technical teams looking to reduce the administrative burden of managing development backlogs.

- **Engineering Managers**
    - Ensure critical bugs are surfaced and assigned to the right sprint without manual intervention.
- **QA Leads**
    - Maintain consistent bug report hygiene and standardized priority levels across the team.
- **Product Managers**
    - Gain visibility into product stability by automatically grouping similar bug reports.
- **Support Specialists**
    - Reduce the time spent manually updating ticket statuses by automating the handoff to engineering.

---

## Features
- **Automated Categorization**
    - Uses AI to classify incoming reports by component, severity, and bug type automatically.
- **Intelligent Prioritization**
    - Analyzes report content to assign priority levels based on business impact and technical risk.
- **Trello Integration**
    - Seamlessly creates or updates cards in Trello using the Composio Toolset to keep boards in sync.
- **Real-time Escalation**
    - Identifies high-severity issues and triggers immediate notifications to the relevant engineering channels.
- **Duplicate Detection**
    - Scans existing tickets to prevent duplicate bug reports, keeping the backlog clean and actionable.

---

## Use Cases
**Backlog Grooming**
- Automatically move new bug reports into the appropriate "To Do" or "Sprint" lists based on priority.
- Tag reports with relevant technical keywords to assist developers in quick filtering.

**Incident Response**
- Flag critical production bugs for immediate review by the on-call engineering team.
- Route security-related reports to the dedicated security triage board automatically.

**Quality Assurance**
- Consolidate similar bug reports into a single parent card to reduce noise for developers.
- Update bug report status based on automated verification of fix deployment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your Trello account within the Composio Toolset configuration.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw bug report text from your support or feedback channel.
- **Agent**: Processes the text, determines the severity, and formats the data for Trello.
- **Composio Toolset**: Executes the API calls to create or update cards in your Trello board.
- **Chat Output**: Confirms the triage action and provides a link to the updated Trello card.

### 3) Run the Flow
Use the Playground to test the triage logic with these prompts:
- `Categorize this bug: "The login button on the mobile app is unresponsive after the latest update."`
- `Triage this issue: "Critical - Database timeout errors occurring during peak traffic hours."`
- `Check for duplicates and add to Trello: "User reports the search bar is missing on the dashboard page."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for parsing unstructured bug reports.
- Use a high-reasoning model to ensure accurate severity classification.
- Instruction: "Analyze the input for technical bugs, extract the component and severity, and map to the correct Trello board."
- Instruction: "If the report is vague, ask for clarification before creating a ticket."

### 2) Composio Toolset Node
- Provide your Trello API key and OAuth credentials to enable board access.
- Ensure the connection scope includes `read` and `write` permissions for the target project boards.

### 3) Tool Availability
- **Trello Create Card**: Adds new bug reports to the backlog.
- **Trello Update Card**: Modifies existing tickets based on new information.
- **Trello Search**: Queries existing cards to identify potential duplicates.
- **Trello Add Label**: Applies priority and component tags dynamically.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automates the ranking and assignment of tasks based on urgency.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Maintains project hygiene by archiving stale or resolved tasks.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Provides round-the-clock resolution for common user inquiries.
