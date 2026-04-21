# Sprint Story Generator (Uplizd) - Automate technical requirements and user story creation

## Summary
The Sprint Story Generator is an AI-powered workflow that transforms high-level product requirements into detailed, sprint-ready user stories. By leveraging the Shortcut integration, this solution bridges the gap between conceptual planning and execution, ensuring engineering teams maintain high pipeline velocity and consistent documentation hygiene without manual overhead.

---

## Demo
![Sprint Story Generator workflow interface showing requirement input and Shortcut integration](image.png)
**Alt text (SEO-ready):** Sprint Story Generator Uplizd workflow showing automated user story creation and Shortcut integration for agile project management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fd71a177-a717-597e-b053-4a4dfa983152)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** shortcut, agile, project management, sprint planning, user stories, engineering productivity, ai workflow, devops
- This solution streamlines the agile development lifecycle by automating the translation of product requirements into actionable tickets.

---

## Who is this for?
This workflow is designed for product and engineering teams looking to reduce administrative burden during sprint planning.

- **Product Managers**
    - Rapidly convert feature requests into structured user stories with clear acceptance criteria.
- **Engineering Leads**
    - Ensure all sprint tasks are well-defined and aligned with technical requirements before development begins.
- **Scrum Masters**
    - Maintain consistent documentation standards across all backlog items to improve team velocity.
- **Developers**
    - Receive clear, context-rich tasks that reduce ambiguity and context switching during the sprint.

---

## Features
- **Automated Story Generation**
    - Uses advanced LLMs to draft comprehensive user stories including titles, descriptions, and acceptance criteria.
- **Shortcut Integration**
    - Seamlessly pushes generated stories directly into your Shortcut workspace using the Composio Toolset.
- **Context-Aware Mapping**
    - Automatically maps incoming requirements to the correct project and epic within your Shortcut environment.
- **Standardized Formatting**
    - Enforces consistent formatting for all backlog items to improve readability and searchability.
- **Real-time Sync**
    - Updates project boards instantly, ensuring the entire team has visibility into new sprint tasks.

---

## Use Cases
**Sprint Planning Automation**
- Convert meeting notes into prioritized backlog items during weekly planning sessions.
- Generate acceptance criteria for complex features to ensure alignment between design and engineering.

**Backlog Refinement**
- Bulk-process raw feature requests into structured tickets to keep the backlog organized.
- Update existing stories with technical details gathered from team discussions or documentation.

**Engineering Workflow Optimization**
- Automate the creation of sub-tasks for large epics to improve sprint tracking.
- Sync requirement changes from external documents directly into active Shortcut tickets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your preferred workspace and project destination.
3. Authenticate your Shortcut account via the Composio connection prompt.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw requirement or feature description.
- **Agent**: Processes the input to generate structured agile stories.
- **Composio Toolset**: Executes the creation of the ticket within Shortcut.
- **Chat Output**: Confirms the successful creation of the story with a link to the ticket.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Create a user story for a new 'Dark Mode' toggle in the settings menu with 3 acceptance criteria.`
- `Generate a ticket for an API performance improvement based on the requirement: 'Reduce latency on the user profile endpoint by 200ms'.`
- `Draft a sprint story for the 'Password Reset' feature including security requirements and edge case handling.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an Agile Product Owner, focusing on clarity and technical precision.
- Use a system prompt that enforces the "As a [user], I want to [action], so that [benefit]" format.
- Instruct the agent to always include a "Definition of Done" section.
- Configure the agent to extract and categorize priority levels from the input text.

### 2) Composio Toolset Node
- Provide your Shortcut API key within the Composio integration settings.
- Ensure the connection scope allows for `create_story` and `update_story` permissions.

### 3) Tool Availability
- `shortcut_create_story`: For generating new backlog items.
- `shortcut_get_projects`: To fetch valid project IDs for mapping.
- `shortcut_search_epics`: To associate new stories with existing epics.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate cross-platform task management and status updates.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage complex stakeholder data and project associations.
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Track and update operational task statuses in real-time.
