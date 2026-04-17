# OneDrive Share Coordinator (Uplizd) - Automated file sharing and permission management

## Summary
The OneDrive Share Coordinator is an intelligent Uplizd AI workflow designed to automate file sharing and granular permission management across your organization. By leveraging the Composio Toolset, this solution eliminates manual administrative overhead, ensuring that team members receive secure, timely access to essential documents while maintaining strict data governance and pipeline velocity.

---

## Demo
![OneDrive Share Coordinator workflow interface showing file access automation and permission settings](image.png)
**Alt text (SEO-ready):** OneDrive Share Coordinator Uplizd workflow, automated file sharing, permission management, Composio integration, and cloud document security.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/4d509eb4-8609-59ce-a033-862b7ece46e8)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** onedrive, file management, automation, permissions, security, data sync, composio, ai workflow
- This solution streamlines cloud storage operations by connecting AI-driven logic to your OneDrive environment for intelligent file handling.

---

## Who is this for?
This solution is designed for operations teams and administrators who need to scale document distribution without compromising security.

- **IT Administrators**
    - Automate the provisioning of folder access to reduce manual ticket volume and human error.
- **Project Managers**
    - Ensure cross-functional teams have instant access to project assets without constant permission requests.
- **Operations Leads**
    - Maintain consistent data hygiene by enforcing standardized sharing protocols across the enterprise.
- **Compliance Officers**
    - Audit and manage document visibility to ensure sensitive files remain restricted to authorized personnel only.

---

## Features
- **Automated Permission Granting**
    - Dynamically assign read or write access to users based on project triggers or team membership.
- **Intelligent File Routing**
    - Automatically move or share files to designated OneDrive folders based on metadata or content analysis.
- **Composio-Powered Integration**
    - Utilizes secure API connectors to bridge the gap between your AI agent and the OneDrive ecosystem.
- **Real-time Access Auditing**
    - Monitor sharing activities through the agent to ensure compliance with internal data policies.
- **Bulk Sharing Capabilities**
    - Execute large-scale file distribution tasks efficiently, reducing the time spent on repetitive administrative workflows.

---

## Use Cases
**Document Lifecycle Management**
- Automatically revoke access to project folders once a contract or project phase is marked as complete.
- Sync updated policy documents to all relevant department folders simultaneously.

**Cross-Team Collaboration**
- Grant temporary access to external vendors for specific file sets with automated expiration timers.
- Streamline onboarding by automatically sharing a standard "New Hire" document package with new team members.

**Security and Compliance**
- Identify and restrict public links on sensitive files to prevent unauthorized data exposure.
- Generate automated reports on who has access to specific high-value directories within OneDrive.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the OneDrive Share Coordinator template from the library.
3. Connect your OneDrive account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the file path and target user/permission level.
- **Agent**: Processes the request and determines the appropriate OneDrive action.
- **Composio Toolset**: Executes the API calls to modify permissions or share files.
- **Chat Output**: Confirms the successful completion of the sharing task to the user.

### 3) Run the Flow
Use the Playground to test your automation with prompts like:
- `Share the 'Q4_Financials.xlsx' file with the Finance team with read-only access.`
- `Revoke all external sharing permissions for the 'Confidential' folder.`
- `List all users who currently have access to the 'Project Alpha' directory.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for all OneDrive operations.
- Use a model with high reasoning capabilities to interpret complex permission requests.
- **Recommended instruction pattern:**
    - Always verify the target user's identity before modifying permissions.
    - If a file path is ambiguous, ask the user for clarification before executing.
    - Provide a clear summary of the changes made after every successful operation.

### 2) Composio Toolset Node
- Provide your authorized OneDrive API key within the Composio configuration.
- Ensure the connection scope includes `Files.ReadWrite` and `Sites.ReadWrite.All` to allow for full management capabilities.

### 3) Tool Availability
- `onedrive_list_files`: Search for files and folders within the directory.
- `onedrive_update_permissions`: Modify access levels for specific users or groups.
- `onedrive_create_share_link`: Generate secure links for external distribution.
- `onedrive_get_file_metadata`: Retrieve current access logs and file details.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial data reconciliation and reporting.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline business processes and task management.
- [../admin-user-access-auditor-by-storeganise/README.md](../admin-user-access-auditor-by-storeganise/README.md) - Audit and manage user access rights across platforms.
