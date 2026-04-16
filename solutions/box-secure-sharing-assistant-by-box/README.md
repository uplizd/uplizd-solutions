# Box Secure Sharing Assistant (Uplizd) - Automated secure file sharing and permission management

## Summary
The Box Secure Sharing Assistant is an intelligent Uplizd workflow that automates file sharing, applies granular security controls, and enforces watermarking policies across your enterprise content. By integrating directly with the Box API via the Composio Toolset, this solution eliminates manual permission errors, ensures compliance with data governance standards, and accelerates secure collaboration for teams handling sensitive documents.

---

## Demo
![Box Secure Sharing Assistant workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Box Secure Sharing Assistant Uplizd workflow for automated file security, permission management, and secure document sharing via Composio and Box API.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/87e1975f-5375-52ef-8226-d6986f06f419)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** box, file security, data governance, access control, document management, composio, ai workflow, secure sharing
- This solution bridges the gap between manual file administration and automated security policy enforcement within the Box ecosystem.

---

## Who is this for?
This solution is designed for organizations that need to maintain strict control over sensitive digital assets while enabling seamless team collaboration.

- **IT Security Manager**
    - Automates the enforcement of file-level security policies and watermarking to prevent unauthorized data leakage.
- **Operations Coordinator**
    - Streamlines the process of granting secure access to external partners without manual folder configuration.
- **Compliance Officer**
    - Ensures all shared documents adhere to internal governance and regulatory standards through automated audit-ready workflows.
- **Project Manager**
    - Accelerates project velocity by instantly provisioning secure document access to team members based on defined project roles.

---

## Features
- **Automated Permission Provisioning**
    - Instantly assigns granular read/write/edit permissions to specific users or groups based on natural language requests.
- **Dynamic Watermark Enforcement**
    - Automatically applies visual watermarks to sensitive documents upon sharing to deter unauthorized distribution.
- **Secure Link Generation**
    - Generates time-limited, password-protected sharing links directly through the Box API to minimize exposure risk.
- **Real-time Access Auditing**
    - Logs all sharing activities and permission changes, providing a clear trail for compliance and security reviews.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to execute complex Box API calls, ensuring reliable and secure interaction with your file storage.

---

## Use Cases
**Secure External Collaboration**
- Automatically share project folders with external consultants using time-bound, restricted access links.
- Revoke access permissions instantly once a collaborative project phase reaches completion.

**Sensitive Data Governance**
- Apply mandatory watermarks to all files shared from a specific "Confidential" folder structure.
- Restrict file downloading capabilities for specific user roles to ensure data remains within the Box environment.

**Operational Efficiency**
- Onboard new team members by automatically granting access to relevant department folders based on their role metadata.
- Bulk-update permission levels for large document sets during organizational restructuring or project handovers.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Box Secure Sharing Assistant template from the solution library.
3. Connect your Box account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user requests for file sharing and permission changes.
- **Agent**: Processes instructions and determines the necessary Box API actions.
- **Composio Toolset**: Executes secure Box API calls for file management and permission updates.
- **Chat Output**: Confirms the successful execution of security policies and sharing actions.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Share the Q3 Financial Report with the Finance team and set permissions to viewer only.`
- `Apply a "Confidential" watermark to all files in the Marketing folder and generate a secure link.`
- `Revoke all external access to the Project Alpha folder immediately.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your security policies.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on permission hierarchy and watermarking triggers.
- Define strict fallback behaviors for when a requested file or user is not found.

### 2) Composio Toolset Node
- Authenticate using your Box API credentials within the Composio dashboard.
- Ensure the connection scope includes `root_readwrite` and `manage_enterprise_properties` for full functionality.

### 3) Tool Availability
- `box_create_shared_link`: Generate secure, time-limited access.
- `box_update_file_permissions`: Modify user access levels dynamically.
- `box_apply_watermark`: Enforce visual security on sensitive assets.
- `box_list_folder_contents`: Audit and verify file locations before sharing.

---

## Related Solutions
- [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automates user provisioning and CRM access management.
- [Admin User Access Auditor by Storeganise](../admin-user-access-auditor-by-storeganise/README.md) - Monitors and reports on user access rights across platforms.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlines cross-platform operational workflows and task triggers.
