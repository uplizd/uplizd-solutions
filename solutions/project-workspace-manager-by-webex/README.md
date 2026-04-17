# Project Workspace Manager (Uplizd) - Automate Webex team and room creation for streamlined project collaboration

## Summary
The Project Workspace Manager is an intelligent Uplizd workflow that automates the provisioning of Webex teams and rooms, ensuring project-based communication channels are ready for action the moment a new initiative is launched. By integrating directly with Webex via the Composio Toolset, this agent eliminates manual setup time, enforces organizational naming conventions, and maintains pipeline velocity by centralizing project assets from day one.

---

## Demo
![Project Workspace Manager workflow showing Chat Input, Agent, Composio Webex Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Project Workspace Manager Uplizd workflow, Webex team automation, automated room provisioning, and project collaboration integration using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ef31462a-2c73-5637-9067-9a6036874a27)

---

## Category
**Primary category:** Collaboration automation  
**Secondary tags:** webex, project management, workflow automation, team provisioning, composio, ai agent, productivity, digital workspace  
This solution bridges the gap between project initiation and team communication by automating the technical setup of digital workspaces.

---

## Who is this for?
This solution is designed for operations teams and project leads who need to scale their collaboration infrastructure without manual overhead.

* **Project Managers**
    * Rapidly spin up dedicated communication hubs for new project stakeholders.
* **IT Operations Managers**
    * Standardize workspace naming and security settings across all active projects.
* **Team Leads**
    * Ensure all team members are invited to the correct rooms immediately upon project kickoff.
* **RevOps Specialists**
    * Sync project-based communication channels with CRM opportunity data to maintain a single source of truth.

---

## Features
- **Automated Team Provisioning**
  Instantly create new Webex teams based on project triggers or manual inputs.
- **Dynamic Room Creation**
  Generate specific rooms for different project workstreams (e.g., "General," "Design," "Dev") automatically.
- **Standardized Naming Conventions**
  Enforce consistent naming patterns across all Webex spaces to simplify search and organization.
- **Smart Member Invitation**
  Automatically add relevant project stakeholders and team members to newly created spaces.
- **Real-time Webex Integration**
  Leverage the Composio Toolset to execute API calls to Webex in real-time, ensuring seamless environment setup.

---

## Use Cases
**Project Kickoff Automation**
* Automatically trigger a new Webex team setup when a project status changes to "Active" in your project management tool.
* Populate the new team with pre-defined members based on the project's department or region.

**Workstream Organization**
* Create specialized sub-rooms within a Webex team for distinct project phases or functional groups.
* Archive or move older project rooms to maintain a clean and focused collaboration environment.

**Cross-Platform Sync**
* Map project metadata from your CRM or task manager directly to Webex team descriptions.
* Update Webex room membership automatically when project roles or assignments change in your primary management platform.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Project Workspace Manager template from the solution library.
3. Connect your Webex account via the Composio Toolset configuration.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives project details, team names, and member lists from the user.
* **Agent**: Processes intent and maps project requirements to Webex API parameters.
* **Composio Toolset**: Executes the authenticated requests to create teams, rooms, and add members.
* **Chat Output**: Confirms the successful creation of the workspace with direct links to the new Webex spaces.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Create a new Webex team named 'Project Alpha' and add the design team members.`
* `Setup a new project workspace for 'Q4 Marketing' with rooms for 'Strategy' and 'Creative'.`
* `Initialize a Webex team for 'Client X Onboarding' and invite the account manager.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your Webex environment.
* Use a model capable of structured output (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are an expert Webex administrator. Extract project names and member lists from the input to trigger the correct API calls."
* Instruction: "Always verify if a team with the requested name already exists before attempting creation."

### 2) Composio Toolset Node
* Provide your Webex API credentials via the Composio dashboard.
* Ensure the connection scope includes `team:write`, `room:write`, and `membership:write` permissions.

### 3) Tool Availability
* `webex_create_team`: Provisions a new team container.
* `webex_create_room`: Generates specific workstream rooms.
* `webex_add_member`: Adds users to teams or rooms via email.
* `webex_list_teams`: Checks existing infrastructure to prevent duplicates.

---

## Related Solutions
* [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Automate project-based workflows and task management.
* [../workspace-setup-optimizer-by-clockify/README.md](../workspace-setup-optimizer-by-clockify/README.md) - Optimize time tracking and workspace setup for project teams.
* [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Streamline CRM account setup and data synchronization.
