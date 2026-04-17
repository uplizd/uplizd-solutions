# Project Workspace Setup Agent (Uplizd) - Automate SharePoint project workspace provisioning

## Summary
The Project Workspace Setup Agent streamlines the administrative overhead of project management by automating the creation of SharePoint project workspaces. By leveraging the Composio Toolset to interface with Microsoft SharePoint, this Uplizd workflow ensures consistent folder structures, list initialization, and team access permissions, allowing project managers to focus on delivery rather than manual configuration.

---

## Demo
![Project Workspace Setup Agent workflow showing automated SharePoint folder and list creation](image.png)
**Alt text (SEO-ready):** Project Workspace Setup Agent workflow for automated SharePoint folder creation, list initialization, and team access management using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/46b99dc2-f839-5d3d-8906-71c7ebc816d8)

---

## Category
**Primary category:** Data integration
**Secondary tags:** sharepoint, project management, automation, workspace provisioning, microsoft 365, composio, ai workflow, data hygiene
This solution bridges the gap between project initiation and technical infrastructure by automating repetitive SharePoint setup tasks.

---

## Who is this for?
This solution is designed for teams looking to standardize their project environments and reduce manual setup time.

*   **Project Managers**
    *   Eliminate manual folder creation and ensure every project starts with a standardized document repository.
*   **IT Administrators**
    *   Enforce organizational compliance by automating the application of consistent permission sets across new workspaces.
*   **Operations Leads**
    *   Standardize project tracking by automatically generating predefined lists and metadata fields upon workspace creation.
*   **Team Leads**
    *   Reduce onboarding friction by ensuring team members have immediate, structured access to project resources.

---

## Features
- **Automated Folder Provisioning**
    Automatically generates a standardized directory tree within SharePoint for every new project.
- **Dynamic List Initialization**
    Pre-populates project lists with required columns, views, and tracking fields to ensure data consistency.
- **Permission Management**
    Applies predefined security groups and access levels to the workspace, ensuring data security from day one.
- **Composio-Powered Integration**
    Uses the Composio Toolset to securely execute API calls to Microsoft SharePoint without manual intervention.
- **Real-time Status Reporting**
    Provides immediate feedback through the Chat Output node, confirming successful workspace creation and resource links.

---

## Use Cases
**Standardized Project Onboarding**
*   Automatically create a "Project Charter," "Budget," and "Deliverables" folder structure for every new project request.
*   Initialize a standard "Task Tracker" list with custom status fields for all new project workspaces.

**Compliance and Governance**
*   Apply consistent naming conventions to all new SharePoint sites to simplify long-term document retrieval and auditing.
*   Ensure that sensitive project folders are automatically restricted to authorized project team members upon creation.

**Operational Efficiency**
*   Reduce the time spent on manual site configuration by triggering the setup agent directly from a project intake form.
*   Sync project metadata from external tools into the newly created SharePoint workspace to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Project Workspace Setup Agent template from the solution library.
3. Connect your Microsoft 365 account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives project details (Name, ID, Lead).
*   **Agent**: Processes the request and maps project requirements to SharePoint actions.
*   **Composio Toolset**: Executes the API calls to create folders, lists, and set permissions.
*   **Chat Output**: Returns the URL of the newly created workspace and a summary of actions taken.

### 3) Run the Flow
Use the Playground to test your setup with these prompts:
* `Create a new project workspace for 'Q4 Marketing Campaign' with standard folders.`
* `Initialize a new project site for 'Alpha-2024' and add the 'Project Tracker' list.`
* `Setup a workspace for 'Client-X-Migration' and grant access to the 'Engineering' team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for SharePoint operations.
*   Focus on extracting project metadata from natural language inputs.
*   Maintain a strict mapping between project types and their required folder structures.
*   Handle error reporting gracefully if a site or list name already exists.

### 2) Composio Toolset Node
*   Requires a valid Microsoft SharePoint API key or OAuth connection.
*   Ensure the connection scope includes `Sites.ReadWrite.All` and `Files.ReadWrite.All` permissions.

### 3) Tool Availability
*   **SharePoint Create Folder**: Automates directory creation.
*   **SharePoint List Manager**: Handles list creation and schema definition.
*   **SharePoint Permission Manager**: Manages user group access and site-level security.

---

## Related Solutions
* [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automates CRM account provisioning and data synchronization.
* [Workforce Onboarding Automator by Connecteam](../workforce-onboarding-automator-by-connecteam/README.md) - Streamlines employee onboarding and resource access management.
* [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Orchestrates multi-step business processes across various platforms.
