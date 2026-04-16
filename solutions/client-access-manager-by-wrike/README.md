# Client Access Manager (Uplizd) - Automate workspace onboarding and permission management

## Summary
The Client Access Manager by Wrike is an intelligent Uplizd workflow designed to automate the provisioning of client workspaces and the granular assignment of permissions. By integrating directly with Wrike, this solution eliminates manual administrative overhead, ensures consistent security protocols across all client projects, and accelerates pipeline velocity by reducing the time from contract signature to project kickoff.

---

## Demo
![Client Access Manager workflow diagram showing Wrike integration for automated workspace provisioning and permission assignment](../image.png)
**Alt text (SEO-ready):** Client Access Manager workflow for Wrike, automating workspace setup, user permission management, and client onboarding via Uplizd AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5d3b15ec-fc84-530a-b01b-9ff130c3d07d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** wrike, project management, onboarding, access control, automation, workflow, saas, client management
- This solution bridges the gap between sales and project delivery by automating the technical setup of client environments within Wrike.

---

## Who is this for?
This solution is designed for operations teams and project managers who need to maintain high security standards while scaling client onboarding.

- **Project Managers**
    - Automate the creation of standardized project folders and permission sets for new clients.
- **IT Administrators**
    - Enforce consistent access control policies across all external-facing workspaces.
- **Account Executives**
    - Reduce the time-to-value for new clients by triggering workspace setup immediately upon deal closure.
- **Operations Leads**
    - Eliminate manual configuration errors and ensure all client data is siloed correctly within Wrike.

---

## Features
- **Automated Workspace Provisioning**
    - Instantly generate new project folders and structures in Wrike based on predefined templates.
- **Dynamic Permission Assignment**
    - Automatically assign user roles and access levels to client stakeholders based on project requirements.
- **Real-time Sync via Composio**
    - Leverage the Composio Toolset to execute Wrike API calls securely and in real-time.
- **Audit-Ready Logging**
    - Maintain a clear record of all access changes and workspace creations for compliance reporting.
- **Standardized Onboarding Logic**
    - Ensure every client onboarding follows the same security and organizational best practices.

---

## Use Cases
**Client Onboarding**
- Automatically create a dedicated Wrike folder for a new client upon receipt of a signed contract.
- Provision specific access permissions for external stakeholders to ensure they only see relevant project tasks.

**Security & Compliance**
- Revoke or audit access permissions for clients who have completed their project lifecycle.
- Standardize folder naming conventions and permission hierarchies to prevent data leakage between client accounts.

**Operational Efficiency**
- Trigger workspace setup workflows directly from CRM status changes to minimize manual hand-offs.
- Sync project team assignments with client-specific access requirements to keep project data secure.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the template.
2. Connect your Wrike account via the Composio Toolset node.
3. Configure your project template IDs within the Agent instructions.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives client details and project scope.
- **Agent**: Processes instructions and determines the necessary Wrike API actions.
- **Composio Toolset**: Executes the Wrike commands to create folders and update permissions.
- **Chat Output**: Confirms the successful creation of the workspace and permission status.

### 3) Run the Flow
Use the Playground to test your automation with prompts like:
- `Create a new client workspace for 'Acme Corp' using the standard onboarding template.`
- `Update permissions for user 'jane.doe@acme.com' to 'Editor' in the 'Q3 Marketing' folder.`
- `Provision a new project folder for 'Global Logistics' and assign the 'Client-External' access group.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your Wrike operations.
- Use a model capable of structured JSON output for reliable API calls.
- Define clear instructions for mapping client names to folder naming conventions.
- Include logic for handling permission conflict resolution.

### 2) Composio Toolset Node
- Provide your Wrike API Key and ensure the connection scope includes `folders:write` and `permissions:write`.
- Authenticate the connection via the Uplizd integration dashboard.

### 3) Tool Availability
- **Folder Management**: Create, rename, and archive project folders.
- **User Management**: Add users to workspaces and modify access roles.
- **Permission Control**: Granularly update access levels for specific project entities.

---

## Related Solutions
- [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate CRM account provisioning and data entry.
- [Work Order Status Tracker by MaintainX](../work-order-status-tracker-by-maintainx/README.md) - Manage and track status updates for field work orders.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline business processes across project management platforms.
