# Automated Bug Triager (Uplizd) - Intelligent issue categorization and assignment

## Summary
The Automated Bug Triager by Uplizd streamlines software development lifecycles by automatically analyzing, categorizing, and routing incoming bug reports from Jira. By leveraging AI to interpret issue descriptions and severity, this workflow reduces manual triage overhead, ensures critical bugs reach the right engineering teams instantly, and maintains high-quality issue tracking hygiene.

---

## Demo
![Automated Bug Triager workflow screenshot showing Jira integration, AI analysis, and ticket routing](image.png)
**Alt text (SEO-ready):** Automated Bug Triager workflow in Uplizd, showing Jira issue analysis, AI-driven categorization, and automated ticket routing for engineering teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/50ce2109-32b3-59ff-9d4e-fd3c04ac36c1)

---

## Category
- **Primary category:** Support operations
- **Secondary tags:** jira, bug tracking, issue management, ai workflow, engineering productivity, automation, composio, software development
- This solution bridges the gap between raw user feedback and engineering action, ensuring your Jira backlog remains organized and actionable.

---

## Who is this for?
This solution is designed for technical teams looking to eliminate manual backlog grooming and accelerate incident response times.

- **Engineering Manager**
    - Reduces time spent manually assigning tickets to developers, allowing for faster sprint planning.
- **QA Lead**
    - Ensures consistent bug classification and prioritization across all incoming reports.
- **Support Specialist**
    - Provides a seamless handoff from customer tickets to engineering tasks without manual data entry.
- **Product Manager**
    - Maintains a cleaner, more accurate view of product health by ensuring bugs are correctly tagged and tracked.

---

## Features
- **Intelligent Severity Scoring**
    - Automatically analyzes bug descriptions to assign priority levels based on impact and urgency.
- **Automated Jira Routing**
    - Instantly creates or updates Jira issues, assigning them to the correct project or component based on AI analysis.
- **Contextual Enrichment**
    - Pulls relevant metadata from incoming reports to provide developers with immediate context for faster debugging.
- **Real-time Sync**
    - Utilizes the Composio Toolset to maintain a bi-directional flow of information between your support channels and Jira.
- **Duplicate Detection**
    - Identifies similar existing bug reports to prevent ticket bloat and consolidate engineering efforts.

---

## Use Cases
**Backlog Grooming**
- Automatically sort incoming bug reports into the correct sprint or backlog based on project tags.
- Identify and merge duplicate bug reports to keep the Jira instance clean and manageable.

**Incident Response**
- Escalate high-severity bugs to the on-call engineer's queue immediately upon detection.
- Notify relevant stakeholders via Jira comments when a critical bug is triaged and assigned.

**Engineering Workflow Optimization**
- Automatically assign bugs to specific team members based on their historical expertise and current workload.
- Update bug status labels based on the AI-determined root cause or affected system component.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the template.
2. Select your workspace and import the Automated Bug Triager workflow.
3. Authenticate your Jira account within the Composio Toolset configuration.
4. Ensure nodes are correctly mapped to your specific Jira project keys and board IDs.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw bug report or support ticket data.
- **Agent**: Processes the input, performs sentiment analysis, and determines the appropriate Jira action.
- **Composio Toolset**: Executes the API calls to create, update, or search for issues within Jira.
- **Chat Output**: Confirms the triage action taken and provides a summary link to the Jira ticket.

### 3) Run the Flow
Use the Playground to test the triager with sample inputs:
- `Triage this: "Users are unable to log in via SSO on the mobile app, getting a 500 error."`
- `Analyze and assign: "The dashboard chart is rendering incorrectly on Safari browsers."`
- `Process this report: "Critical: Database connection timeout occurring during peak hours."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical triage assistant.
- **Instruction Pattern:**
    - Analyze the input for technical keywords, severity indicators, and affected components.
    - Map the findings to your predefined Jira project schema and priority levels.
    - Draft a concise summary for the Jira issue description including the user's environment details.

### 2) Composio Toolset Node
- Requires a valid Jira API key or OAuth connection.
- Ensure the connection scope includes `write:jira-work` and `read:jira-work` permissions.

### 3) Tool Availability
- **Jira Search**: Locate existing issues to prevent duplicates.
- **Jira Create**: Generate new tickets with populated fields.
- **Jira Update**: Modify existing tickets with new triage metadata.

---

## Related Solutions
- [Action Item Prioritizer (Rootly)](../action-item-prioritizer-by-rootly/README.md) — Automate the prioritization of technical action items.
- [Account Relationship Builder (Dynamics365)](../account-relationship-builder-by-dynamics365/README.md) — Manage complex account data and relationships.
- [Support Ticket Manager (Spoki)](../whats-app-support-ticket-manager-by-spoki/README.md) — Streamline support triage across messaging platforms.
