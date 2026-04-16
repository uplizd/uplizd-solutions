# Automated Bug Triage Agent (Uplizd) - Intelligent issue categorization and priority routing

## Summary
The Automated Bug Triage Agent streamlines software development lifecycles by automatically analyzing, categorizing, and prioritizing incoming bug reports from BugHerd. By leveraging AI to interpret report severity and context, this workflow eliminates manual backlog grooming, reduces response times for critical issues, and ensures engineering teams focus on the most impactful technical debt.

---

## Demo
![Automated Bug Triage Agent workflow interface showing BugHerd integration and AI-driven priority routing](image.png)
**Alt text (SEO-ready):** Automated Bug Triage Agent workflow interface showing BugHerd integration and AI-driven priority routing for Uplizd automated issue management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/385a5647-08bd-5e8a-b67e-198518493d31)

---

## Category
- **Primary category:** Support automation
- **Secondary tags:** bug tracking, bugherd, issue management, devops, automated triage, software quality, composio, ai workflow
- This solution bridges the gap between raw user feedback and engineering backlogs by automating the classification of technical issues.

---

## Who is this for?
This solution is designed for technical teams looking to optimize their issue resolution lifecycle.

- **QA Engineers**
    - Automate the initial screening of bug reports to filter out duplicates and non-reproducible issues.
- **Engineering Managers**
    - Gain real-time visibility into bug severity trends and ensure high-priority items are routed to the correct developers.
- **Product Managers**
    - Align bug resolution efforts with product roadmap priorities by categorizing issues based on feature impact.
- **Customer Support Leads**
    - Reduce the time spent manually tagging and assigning tickets, allowing for faster updates to end-users.

---

## Features
- **Intelligent Severity Scoring**
    - Uses LLM analysis to assign priority levels based on report descriptions, screenshots, and impact statements.
- **Automated BugHerd Routing**
    - Seamlessly pushes triaged bugs into specific BugHerd projects or status columns via the Composio Toolset.
- **Duplicate Detection**
    - Identifies and flags incoming reports that match existing open tickets to prevent redundant engineering work.
- **Context-Aware Summarization**
    - Generates concise, actionable summaries of complex bug reports for faster developer comprehension.
- **Customizable Triage Logic**
    - Allows for user-defined rules to handle specific bug types, such as security vulnerabilities or UI/UX regressions.

---

## Use Cases
**Backlog Hygiene**
- Automatically move low-priority or cosmetic bugs to a "Later" backlog folder.
- Flag incomplete bug reports that lack sufficient reproduction steps for immediate follow-up.

**Incident Response**
- Trigger instant notifications for high-severity bugs identified during the triage process.
- Route security-related reports directly to the security engineering team’s queue.

**Team Productivity**
- Standardize bug report formatting across the organization to ensure consistent data entry.
- Reduce the "noise" in development sprints by filtering out non-actionable feedback.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Automated Bug Triage Agent template from the solution library.
3. Connect your BugHerd account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw bug report data from external sources or manual entry.
- **Agent**: Analyzes the report content using custom instructions for severity and categorization.
- **Composio Toolset**: Executes API calls to BugHerd to update ticket status or assign labels.
- **Chat Output**: Confirms the triage action and provides a summary of the assigned priority.

### 3) Run the Flow
Test the triage logic in the Playground using these prompts:
- `Triage the latest bug report in BugHerd and assign it a priority based on the description.`
- `Find all unassigned bugs in the project and categorize them by UI vs. Backend issues.`
- `Summarize the high-priority bugs reported in the last 24 hours and post them to the engineering channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary decision-maker for issue classification.
- **Role:** Act as a Senior QA Lead with deep expertise in software development lifecycles.
- **Instruction Pattern:** 
    - Always analyze the provided bug description for reproduction steps before assigning priority.
    - If information is missing, flag the ticket for "Needs More Info" rather than guessing.
    - Maintain a consistent mapping between bug symptoms and internal team labels.

### 2) Composio Toolset Node
- **API Key:** Provide your BugHerd API key within the Composio connection manager.
- **Connection Scope:** Ensure the agent has read/write access to your specific BugHerd projects.

### 3) Tool Availability
- **Issue Retrieval:** Fetching open tickets and metadata from BugHerd.
- **Update Operations:** Modifying ticket status, priority fields, and assignee tags.
- **Search Capabilities:** Querying historical bugs to identify potential duplicates.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven support automation for customer queries.
- [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Automated prioritization for incident-related action items.
- [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Monitoring and reporting on team workflow efficiency.
