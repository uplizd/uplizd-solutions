# Employee Offboarding Cleanup Agent (Uplizd) - Secure and automated offboarding for Google Admin

## Summary
The Employee Offboarding Cleanup Agent automates the critical security and administrative tasks required when a team member departs. By leveraging the Composio Toolset to interface with Google Admin, this workflow ensures that user accounts are suspended, access permissions are revoked, and data is migrated or archived instantly. This solution eliminates manual oversight, reduces the risk of orphaned accounts, and maintains organizational security hygiene across your Google Workspace environment.

---

## Demo
![Employee Offboarding Cleanup Agent workflow diagram showing Google Admin integration](image.png)
**Alt text (SEO-ready):** Employee Offboarding Cleanup Agent workflow for Google Admin, featuring automated account suspension, access revocation, and data migration using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=google-cloud)](https://uplizd.ai/solutions/8a7dd5e9-2a9c-5ed3-b27a-21233e027450)

---

## Category
**Primary category:** Operations
**Secondary tags:** google workspace, admin, offboarding, security, identity management, automation, composio, data hygiene.
This solution streamlines IT operations by automating the lifecycle management of user accounts within Google Workspace.

---

## Who is this for?
This workflow is designed for IT and HR professionals responsible for maintaining secure and compliant organizational access.

*   **IT Administrators**
    *   Automate the tedious process of revoking access across multiple Google services to prevent security gaps.
*   **Security Operations Managers**
    *   Ensure strict compliance by verifying that all offboarded accounts are fully suspended and data is secured.
*   **HR Operations Specialists**
    *   Coordinate with IT to trigger offboarding workflows immediately upon employee departure, ensuring a seamless transition.
*   **System Architects**
    *   Standardize offboarding protocols to reduce human error and ensure consistent application of security policies.

---

## Features
- **Automated Account Suspension**
    Instantly disable user access to Google Workspace accounts to prevent unauthorized entry post-departure.
- **Access Permission Revocation**
    Automatically remove group memberships and shared drive access to maintain the principle of least privilege.
- **Data Migration & Archiving**
    Transfer critical files and email data to a manager or shared repository before account deletion.
- **Audit Logging**
    Generate a comprehensive report of all actions taken during the offboarding process for compliance verification.
- **Real-time Integration**
    Utilize the Composio Toolset to execute commands directly within Google Admin without manual console intervention.

---

## Use Cases
**Security & Compliance**
*   Revoking OAuth tokens and third-party app access for departing employees to secure company data.
*   Ensuring all company-owned mobile devices are wiped or unlinked from the corporate MDM profile.

**Operational Efficiency**
*   Bulk offboarding of temporary contractors or seasonal staff at the end of their engagement period.
*   Automated cleanup of calendar resources and meeting ownership transfers to active team members.

**Data Governance**
*   Transferring ownership of Google Drive files and folders to a designated supervisor to prevent data loss.
*   Exporting user mailbox data to a secure archive before final account de-provisioning.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Google Admin credentials within the connection manager.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the employee email address and offboarding parameters.
*   **Agent**: Processes the request and determines the necessary security actions.
*   **Composio Toolset**: Executes Google Admin API calls to modify user status and permissions.
*   **Chat Output**: Returns a summary report of the completed offboarding actions.

### 3) Run the Flow
Use the Playground to test your offboarding logic with these prompts:
*   `"Offboard user john.doe@company.com, transfer drive files to manager, and suspend account."`
*   `"Revoke access for user jane.smith@company.com and remove from all distribution groups."`
*   `"Perform full offboarding for user alex.brown@company.com and send a summary report to IT."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for security operations.
*   Maintain a neutral, professional tone for audit logs.
*   Prioritize security-first logic (e.g., suspend before delete).
*   Always request confirmation for destructive actions if the input is ambiguous.

### 2) Composio Toolset Node
*   **API Key**: Provide your Google Admin service account credentials.
*   **Connection Scope**: Ensure the scope includes `admin.directory.user` and `admin.directory.group` permissions.

### 3) Tool Availability
*   `google_admin_suspend_user`: Disables the account immediately.
*   `google_admin_transfer_drive`: Moves file ownership to a specified user.
*   `google_admin_remove_group_member`: Cleans up group access lists.
*   `google_admin_get_user_info`: Validates user status before performing actions.

---

## Related Solutions
*   [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automates the creation and provisioning of new user accounts.
*   [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Monitors and audits user access and account configurations.
*   [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Manages the full lifecycle of employee onboarding and task assignment.
