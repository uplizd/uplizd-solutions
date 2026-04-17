# OneDrive SharePoint Bridge (Uplizd) - Seamless document synchronization and file management

## Summary
The OneDrive SharePoint Bridge by Uplizd automates the movement and synchronization of files between personal OneDrive storage and shared SharePoint document libraries. This workflow eliminates manual file transfers, ensures team-wide access to critical assets, and maintains consistent folder structures, providing a single source of truth for organizational content and improving pipeline velocity for collaborative projects.

---

## Demo
![OneDrive SharePoint Bridge workflow showing file transfer automation between OneDrive and SharePoint](image.png)
**Alt text (SEO-ready):** OneDrive SharePoint Bridge workflow automation by Uplizd for real-time file synchronization and document management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/d5b7c062-a681-5147-aaa9-c7051da774b4)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** sharepoint, onedrive, file management, document sync, automation, cloud storage, composio, ai workflow
- This solution bridges the gap between individual productivity storage and enterprise-grade collaborative document management systems.

---

## Who is this for?
This solution is designed for teams looking to centralize their digital assets and reduce manual file handling overhead.

- **Operations Manager**
    - Automates the migration of project files from individual drives to shared team repositories to ensure data visibility.
- **IT Administrator**
    - Enforces standardized file storage policies by automatically routing documents to designated SharePoint libraries.
- **Project Lead**
    - Ensures all team members have real-time access to the latest versions of documents without manual sharing steps.
- **Content Creator**
    - Simplifies the hand-off process by triggering automated syncs from personal drafts to official team publishing folders.

---

## Features
- **Automated File Routing**
    - Intelligent detection of new files in OneDrive triggers immediate movement or copying to specific SharePoint paths.
- **Version Consistency**
    - Ensures that the latest iterations of documents are synced across platforms, preventing version fragmentation.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely authenticate and interact with both Microsoft 365 environments.
- **Real-time Sync Monitoring**
    - Provides continuous oversight of file transfer status, ensuring no critical documents are left in personal storage.
- **Customizable Folder Mapping**
    - Allows users to define specific source-to-destination rules based on file metadata or naming conventions.

---

## Use Cases
**Document Centralization**
- Automatically move finalized project deliverables from personal OneDrive folders to the central SharePoint project library.
- Sync incoming client attachments from OneDrive to a dedicated SharePoint folder for cross-departmental review.

**Team Collaboration**
- Aggregate shared resources from multiple individual drives into a single, accessible SharePoint repository for team meetings.
- Maintain a master folder structure in SharePoint that mirrors active project work occurring in personal OneDrive spaces.

**Data Hygiene & Compliance**
- Periodically clear out personal OneDrive workspaces by archiving completed project files into long-term SharePoint storage.
- Standardize file naming and location protocols by enforcing automated transfer rules for all incoming documents.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your dashboard.
3. Authenticate your OneDrive and SharePoint accounts via the Composio connection prompt.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives commands or triggers for file transfer operations.
- **Agent**: Interprets the file path and destination requirements using your instructions.
- **Composio Toolset**: Executes the API calls to read from OneDrive and write to SharePoint.
- **Chat Output**: Confirms the successful transfer and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your file management automation:
- `Move all files from my 'Project Alpha' folder in OneDrive to the 'Project Alpha' SharePoint library.`
- `Sync new documents from my 'Inbox' folder to the 'Team Assets' SharePoint folder.`
- `Check for any files older than 30 days in my OneDrive and move them to the SharePoint archive.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for your file management logic.
- **Recommended instruction pattern:**
    - Always verify the source and destination paths before initiating a file move.
    - If a file name conflict occurs, append a timestamp to the filename in SharePoint.
    - Provide a clear confirmation message detailing the number of files moved and their new locations.

### 2) Composio Toolset Node
- **API Key**: Ensure your Microsoft 365 API key is active within the Composio dashboard.
- **Connection Scope**: Grant read/write permissions for both `Files.ReadWrite` and `Sites.ReadWrite.All` to allow seamless cross-platform interaction.

### 3) Tool Availability
- **OneDrive Connector**: Capability to list, read, move, and delete files in personal storage.
- **SharePoint Connector**: Capability to list document libraries and upload/manage files within site collections.

---

## Related Solutions
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Synchronize account data and relationship insights across your CRM.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Automate complex business processes and task hand-offs.
- [../account-audit-agent-by-cloudflare/README.md](../account-audit-agent-by-cloudflare/README.md) - Monitor and audit account activity for security and compliance.
