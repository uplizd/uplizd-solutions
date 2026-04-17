# Employee Onboarding Automation Agent (Uplizd) - Automated SharePoint access and resource provisioning

## Summary
The Employee Onboarding Automation Agent leverages the Composio Toolset to orchestrate seamless SharePoint access provisioning for new hires. By automating the creation of user permissions, folder access, and departmental resource assignment, this workflow eliminates manual administrative bottlenecks, ensures consistent onboarding hygiene, and accelerates time-to-productivity for HR and IT teams.

---

## Demo
![Employee Onboarding Automation Agent workflow diagram showing SharePoint integration](image.png)
**Alt text (SEO-ready):** Employee Onboarding Automation Agent workflow diagram showing Uplizd AI-driven SharePoint access provisioning and automated resource assignment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ebacaf09-c041-5dc8-b16d-0a26eb26e4ec)

---

## Category
**Primary category:** Operations
**Secondary tags:** sharepoint, onboarding, automation, hr-tech, user-provisioning, composio, ai-workflow, identity-management

This solution bridges the gap between HR onboarding processes and IT infrastructure management by automating SharePoint access rights.

---

## Who is this for?
This solution is designed for organizations looking to standardize and accelerate the digital onboarding experience for new staff.

*   **IT Administrators**
    *   Automate repetitive user permission tasks and reduce manual ticket volume for SharePoint access requests.
*   **HR Operations Managers**
    *   Ensure new hires have immediate access to necessary departmental documentation and collaborative workspaces on day one.
*   **Department Heads**
    *   Maintain consistent security protocols by ensuring team members are only provisioned with relevant project-specific resources.
*   **Onboarding Specialists**
    *   Reduce the administrative burden of cross-departmental coordination during the employee lifecycle setup.

---

## Features
- **Automated Permission Mapping**
    Automatically assign SharePoint site access based on the new hire's department and role metadata.
- **Real-time Resource Provisioning**
    Utilize the Composio Toolset to trigger SharePoint API actions instantly upon employee record creation.
- **Compliance-Ready Audit Logs**
    Maintain a clear, automated trail of all access grants and resource assignments for internal security audits.
- **Dynamic Folder Assignment**
    Intelligently route new users to specific project folders and collaborative document libraries based on project tags.
- **Error-Resilient Workflow**
    Built-in validation steps ensure that user accounts exist in the directory before attempting to provision SharePoint access.

---

## Use Cases
**New Hire Setup**
*   Automatically provision access to the "General Onboarding" and "Departmental Resources" SharePoint sites for new employees.
*   Trigger welcome email notifications containing direct links to assigned SharePoint project hubs.

**Departmental Transfers**
*   Update SharePoint permissions automatically when an employee changes departments or project assignments.
*   Revoke access to legacy project folders while granting new access to current team repositories.

**Security & Compliance**
*   Audit and clean up stale permissions for users who have transitioned roles or left the organization.
*   Enforce "Least Privilege" access by ensuring users are only added to necessary SharePoint groups via automated policy checks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to navigate to the solution page.
2. Select "Import Workflow" to load the agent template into your Uplizd dashboard.
3. Connect your SharePoint account via the Composio integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the new hire's details (Name, Email, Department, Project ID).
*   **Agent**: Processes the request and determines the necessary SharePoint permission levels.
*   **Composio Toolset**: Executes the API calls to SharePoint to manage user groups and site permissions.
*   **Chat Output**: Confirms successful provisioning or alerts the administrator of any configuration conflicts.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these prompts:
* `Provision SharePoint access for John Doe in the Marketing department for the Q3 Campaign project.`
* `Add new hire Sarah Smith to the Engineering Team site and the DevOps documentation folder.`
* `Update permissions for user id 1024 to grant access to the Finance-2024 project site.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that interprets HR data and maps it to SharePoint actions.
*   Use a structured instruction set to define permission levels per department.
*   Configure the agent to prioritize security by verifying user identity before executing API calls.
*   Enable "Chain of Thought" reasoning to allow the agent to handle complex multi-site provisioning requests.

### 2) Composio Toolset Node
*   **API Key**: Provide your SharePoint/Microsoft Graph API credentials within the Composio dashboard.
*   **Connection Scope**: Ensure the connection has `Sites.ReadWrite.All` and `Directory.Read.All` permissions to manage users and site access effectively.

### 3) Tool Availability
*   `sharepoint_add_user_to_group`: Adds a user to a specific SharePoint security group.
*   `sharepoint_get_site_details`: Retrieves site IDs and metadata for accurate provisioning.
*   `sharepoint_list_permissions`: Validates existing access levels before modifying user rights.

---

## Related Solutions
* [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automates administrative user setup and access management.
* [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamlines general workforce onboarding tasks and communication.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for business process workflows.
