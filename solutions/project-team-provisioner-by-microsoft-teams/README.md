# Project Team Provisioner (Uplizd) - Automated Microsoft Teams workspace setup and configuration

## Summary
The Project Team Provisioner (Uplizd) streamlines the creation and lifecycle management of Microsoft Teams workspaces by automating channel setup, member provisioning, and resource allocation. This workflow eliminates manual administrative overhead, ensuring that project teams are ready to collaborate instantly with standardized structures and consistent access controls.

---

## Demo
![Project Team Provisioner workflow diagram showing automated Microsoft Teams workspace creation and channel configuration](image.png)
**Alt text (SEO-ready):** Project Team Provisioner workflow diagram showing automated Microsoft Teams workspace creation, channel configuration, and member provisioning using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9ff554f0-e89f-5725-a5c0-31890b46fb21)

---

## Category
**Primary category:** Operations automation  
**Secondary tags:** microsoft teams, team provisioning, workspace management, collaboration, automation, composio, ai workflow, project management  
This solution bridges the gap between project initiation and team collaboration by automating the technical setup of Microsoft Teams environments.

---

## Who is this for?
This solution is designed for technical and operational leaders who need to scale team onboarding without increasing administrative burden.

*   **IT Administrators**
    *   Standardize workspace creation to ensure compliance and consistent naming conventions across the organization.
*   **Project Managers**
    *   Reduce time-to-collaboration by having project-ready Teams environments provisioned automatically upon project approval.
*   **Operations Leads**
    *   Automate the onboarding of cross-functional teams to ensure all members have immediate access to necessary channels and resources.
*   **DevOps Engineers**
    *   Integrate team provisioning into existing CI/CD or project management workflows to maintain a single source of truth for team access.

---

## Features
- **Automated Workspace Creation**
  Instantly generate new Microsoft Teams workspaces based on predefined project templates.
- **Channel Structure Standardization**
  Automatically create required channels (e.g., General, Planning, Resources) to maintain consistent team organization.
- **Role-Based Member Provisioning**
  Programmatically assign users to teams with appropriate roles, reducing manual entry errors.
- **Integration with Composio Toolset**
  Leverages the Composio Toolset to securely interface with Microsoft Graph APIs for real-time team management.
- **Lifecycle Management**
  Easily archive or update team settings as project requirements evolve, ensuring workspace hygiene.

---

## Use Cases
**New Project Onboarding**
*   Automatically provision a new Team and invite core stakeholders the moment a project is marked as "Approved" in your CRM.
*   Populate new channels with pinned links to project documentation and shared project trackers.

**Departmental Scaling**
*   Standardize the onboarding process for new hires by automatically adding them to relevant department-wide Teams.
*   Sync team membership with external HR or project management tools to ensure access is always up-to-date.

**Resource & Access Governance**
*   Implement automated audits to ensure that team membership aligns with current project assignments.
*   Quickly spin up temporary "War Room" channels for urgent project milestones, complete with pre-configured notification settings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Authenticate your Microsoft Teams connection via the Composio Toolset.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives project details or team creation requests from the user.
*   **Agent**: Processes the request, extracts team parameters, and determines the necessary API calls.
*   **Composio Toolset**: Executes the Microsoft Teams API commands to provision workspaces and channels.
*   **Chat Output**: Confirms successful creation or reports any configuration errors to the user.

### 3) Run the Flow
Use the Playground to test your provisioning logic:
*   `Create a new project team named 'Q4 Marketing Campaign' and add the marketing-leads group.`
*   `Provision a new team for the 'Alpha Project' with channels: 'General', 'Design', and 'Development'.`
*   `Check the status of the 'Project Phoenix' team and list all current members.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for your team provisioning logic.
*   Instruction: You are a Microsoft Teams administration assistant.
*   Instruction: Extract project names, channel lists, and user emails from the input.
*   Instruction: Always confirm the successful creation of a team with a summary of the channels created.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Microsoft Graph API key is active in the Composio dashboard.
*   **Connection Scope**: Grant `Team.ReadWrite.All` and `Group.ReadWrite.All` permissions to allow the agent to create and manage teams.

### 3) Tool Availability
*   `teams_create_team`: Provisions a new Microsoft Team workspace.
*   `teams_add_channel`: Adds specific channels to an existing team.
*   `teams_add_member`: Adds users or groups to a team.
*   `teams_list_teams`: Retrieves existing team metadata for audit purposes.

---

## Related Solutions
*   [Account Relationship Builder (Dynamics 365)](../account-relationship-builder-by-dynamics365/README.md) — Manage CRM account relationships and data mapping.
*   [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) — Automate project-based workflows and status updates.
*   [Workforce Onboarding Automator (Connecteam)](../workforce-onboarding-automator-by-connecteam/README.md) — Streamline employee onboarding and task assignment.
