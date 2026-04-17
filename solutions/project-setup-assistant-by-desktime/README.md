# Project Setup Assistant (Uplizd) - Automate project creation and task structuring

## Summary
The Project Setup Assistant by DeskTime is an AI-powered workflow that transforms unstructured project briefs into organized, actionable project structures. By leveraging the DeskTime integration via the Composio Toolset, this solution automates the creation of tasks, timelines, and resource assignments, ensuring team alignment and reducing manual administrative overhead for project managers and operational leads.

---

## Demo
![Project Setup Assistant workflow interface showing AI-driven task generation and DeskTime integration](image.png)
**Alt text (SEO-ready):** Project Setup Assistant (Uplizd) workflow interface showing AI-driven task generation and DeskTime integration for automated project management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/85a7f874-5759-59fe-bff9-65cfea1d9b89)

---

## Category
**Primary category:** Product management
**Secondary tags:** project management, desktime, task automation, workflow optimization, productivity, ai assistant, composio, resource planning.
This solution streamlines the transition from project ideation to execution by automating the setup of complex task hierarchies within DeskTime.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual data entry and standardize their project initiation process.

- **Project Managers**
    - Automate the creation of complex project boards and task lists directly from meeting notes.
- **Operations Leads**
    - Ensure consistent project structure and resource allocation across all internal departments.
- **Team Leads**
    - Reduce administrative friction by allowing AI to handle the initial setup of new client or internal initiatives.
- **Product Managers**
    - Quickly translate product requirements into actionable development tasks and milestones.

---

## Features
- **Automated Task Generation**
    - Instantly parses natural language briefs to generate granular, actionable tasks within DeskTime.
- **Intelligent Resource Mapping**
    - Automatically assigns tasks to appropriate team members based on project requirements and availability.
- **Structured Milestone Creation**
    - Defines project timelines and key milestones based on the scope provided in the initial project description.
- **Real-time DeskTime Sync**
    - Utilizes the Composio Toolset to push project structures directly to your DeskTime environment in real-time.
- **Context-Aware Formatting**
    - Ensures all generated tasks follow your organization's naming conventions and priority standards.

---

## Use Cases
**Project Initiation**
- Generate a full project roadmap from a single paragraph of project requirements.
- Automatically populate task descriptions with acceptance criteria and priority levels.

**Operational Efficiency**
- Standardize the onboarding of new clients by triggering a pre-defined project template.
- Sync project status updates across multiple internal tools to maintain a single source of truth.

**Resource Planning**
- Allocate tasks based on project complexity and team capacity insights.
- Adjust project timelines dynamically as new requirements are added to the workflow.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Import the workflow into your Uplizd workspace.
3. Authenticate your DeskTime account within the Composio Toolset node.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the project brief or raw notes from the user.
- **Agent**: Processes the input, extracts tasks, and formats them for the DeskTime API.
- **Composio Toolset**: Executes the API calls to create projects and tasks in DeskTime.
- **Chat Output**: Confirms the successful creation of the project and provides a summary of generated tasks.

### 3) Run the Flow
Use the Playground to test the flow with these prompts:
- `Create a new project named 'Q4 Marketing Campaign' with tasks for content creation, social media scheduling, and ad budget tracking.`
- `Set up a project for 'Website Redesign' including milestones for wireframing, development, and QA testing.`
- `Generate a task list for 'Client Onboarding' and assign the 'Initial Discovery' task to the design team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that parses intent and maps it to tool calls.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system instruction to prioritize task hierarchy and clear, actionable descriptions.
- Ensure the agent is instructed to ask for clarification if the project brief lacks essential details like deadlines.

### 2) Composio Toolset Node
- Provide your Composio API key in the node configuration.
- Ensure the connection scope includes `desktime:write` permissions to allow task and project creation.

### 3) Tool Availability
- `desktime_create_project`: Initializes the project container.
- `desktime_create_task`: Adds individual tasks to the project.
- `desktime_update_milestone`: Sets project deadlines and key performance indicators.

---

## Related Solutions
- [Workspace Setup Optimizer](../workspace-setup-optimizer-by-clockify/README.md) — Streamline team workspace configurations and time-tracking settings.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the efficiency and status of your team's automated workflows.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the creation and configuration of new accounts in your CRM.
