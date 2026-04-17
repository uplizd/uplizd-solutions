# Dynamic Group Management Agent (Uplizd) - Automate Google Workspace group membership and lifecycle

## Summary
The Dynamic Group Management Agent by Google Admin streamlines organizational identity management by automating the addition, removal, and synchronization of users within Google Groups. By leveraging real-time organizational changes, this Uplizd workflow eliminates manual administrative overhead, ensures consistent access control, and maintains directory hygiene, providing a single source of truth for your team's communication and resource access.

---

## Demo
![Dynamic Group Management Agent workflow interface showing automated Google Workspace group updates](image.png)
**Alt text (SEO-ready):** Dynamic Group Management Agent by Google Admin showing automated Google Workspace group updates, user synchronization, and directory management workflow in Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=google)](https://uplizd.ai/solutions/adf8d459-7cbe-5805-99f5-a57f63c0ef3a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** google workspace, group management, identity access, automation, directory sync, admin, composio, ai workflow
- This solution bridges the gap between HR-driven organizational changes and technical group access, ensuring seamless directory maintenance.

---

## Who is this for?
This agent is designed for IT and Operations teams managing complex user lifecycles across large organizations.

- **IT Administrators**
  - Reduces manual ticket volume for group membership requests and access provisioning.
- **HR Operations Managers**
  - Ensures new hires and departing employees are automatically added to or removed from relevant communication channels.
- **Security Compliance Officers**
  - Maintains strict access control by ensuring only authorized personnel remain in sensitive distribution lists.
- **Department Leads**
  - Keeps team distribution lists updated without needing to request manual intervention from the helpdesk.

---

## Features
- **Automated Membership Sync**
  - Automatically updates Google Group membership based on triggers from organizational data sources.
- **Lifecycle Management**
  - Triggers removal actions for offboarded users to ensure security and prevent unauthorized access.
- **Intelligent Triage**
  - Uses AI to interpret organizational change requests and map them to the correct Google Workspace groups.
- **Composio Toolset Integration**
  - Seamlessly connects with the Google Admin SDK to execute group updates in real-time.
- **Audit Logging**
  - Tracks all membership changes, providing a clear history of group modifications for compliance reporting.

---

## Use Cases
**Onboarding and Offboarding**
- Automatically add new employees to department-specific groups based on their job title.
- Remove departing employees from all company-wide and project-specific distribution lists instantly.

**Access Control and Security**
- Sync sensitive project groups with authorized personnel lists to prevent data leakage.
- Regularly audit group membership to ensure alignment with current organizational structure.

**Communication Efficiency**
- Dynamically update mailing lists when employees change departments or project roles.
- Ensure cross-functional teams always have the correct members for project-based collaboration.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Dynamic Group Management Agent.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your Google Workspace account within the Composio connection settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the organizational change event or admin command.
- **Agent**: Processes the request and determines the necessary group membership adjustments.
- **Composio Toolset**: Executes the specific Google Admin API calls to modify group membership.
- **Chat Output**: Confirms the successful update or flags errors for manual review.

### 3) Run the Flow
Use the Playground to test your group management logic with the following prompts:
- `Add user john.doe@company.com to the Engineering-All group.`
- `Remove all users from the Marketing-Interns group who have been inactive for 90 days.`
- `Sync the Sales-Team group membership with the current list of active employees in the Sales department.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine that translates natural language requests into structured API commands.
- Use a model capable of high-precision instruction following (e.g., GPT-4o).
- Instruct the agent to verify the user's identity before executing group changes.
- Ensure the agent is configured to handle errors gracefully when a group or user is not found.

### 2) Composio Toolset Node
- Provide your Google Admin API credentials via the Composio dashboard.
- Set the connection scope to include `admin.directory.group.member` permissions.

### 3) Tool Availability
- **List Groups**: Retrieve current group configurations.
- **Add Member**: Add a specified user to a group.
- **Remove Member**: Remove a specified user from a group.
- **Get Group Members**: Audit existing membership lists.

---

## Related Solutions
- [../admin-user-onboarding-assistant-by-storeganise/README.md](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automate new user account provisioning and onboarding tasks.
- [../admin-user-access-auditor-by-storeganise/README.md](../admin-user-access-auditor-by-storeganise/README.md) - Monitor and audit user access levels across your organization.
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Streamline CRM account creation and setup processes.
