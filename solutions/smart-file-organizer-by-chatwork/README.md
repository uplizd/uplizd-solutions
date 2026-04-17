# Smart File Organizer (Uplizd) - Automated file categorization and team asset management

## Summary
The Smart File Organizer by Chatwork is an intelligent Uplizd workflow designed to streamline digital asset management by automatically categorizing, renaming, and tracking shared files across team communication channels. By leveraging AI to parse file metadata and context, this solution eliminates manual filing overhead, ensures consistent naming conventions, and provides a single source of truth for team documentation, ultimately boosting pipeline velocity and organizational hygiene.

---

## Demo
![Smart File Organizer workflow interface showing automated file categorization and Chatwork integration](image.png)
**Alt text (SEO-ready):** Smart File Organizer Uplizd workflow for automated file categorization, Chatwork integration, and team asset management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-193034d8--607e--5588--9e8b--48652d88d8df-blue)](https://uplizd.ai/solutions/193034d8-607e-5588-9e8b-48652d88d8df)

---

## Category
*   **Primary category:** Data integration
*   **Secondary tags:** chatwork, file management, automation, data hygiene, ai workflow, document organization, productivity, composio
*   This solution bridges the gap between unstructured team communication and organized storage, ensuring that every shared file is indexed and searchable.

---

## Who is this for?
This solution is designed for teams struggling with fragmented file storage and manual administrative tasks.

*   **Operations Manager**
    *   Ensures team compliance with file naming standards and storage protocols across all communication channels.
*   **Project Lead**
    *   Maintains visibility over project-critical documents without needing to manually search through chat history.
*   **IT Administrator**
    *   Reduces data clutter and improves security by automating the archival and categorization of sensitive shared files.
*   **Executive Assistant**
    *   Saves hours of weekly manual sorting by automating the organization of incoming assets from team discussions.

---

## Features
- **Automated File Categorization**
  Uses AI to analyze file content and context to automatically assign files to the correct project folders.
- **Intelligent Naming Conventions**
  Standardizes file names based on project codes, dates, and document types for instant retrieval.
- **Chatwork Integration**
  Seamlessly monitors team rooms via the Composio Toolset to trigger organization workflows the moment a file is uploaded.
- **Real-time Syncing**
  Ensures that files shared in chat are immediately mirrored and organized in your primary cloud storage provider.
- **Audit Trail Logging**
  Maintains a clear history of file movements and categorizations for compliance and transparency.

---

## Use Cases
**Project Documentation Management**
*   Automatically move design assets shared in Chatwork to the corresponding project folder in Google Drive.
*   Rename project briefs and meeting notes to include the date and version number upon upload.

**Team Communication Hygiene**
*   Flag duplicate files shared across different rooms to prevent storage bloat.
*   Archive files older than 90 days from active chat rooms to long-term storage automatically.

**Compliance and Security**
*   Detect and move sensitive documents containing PII to restricted, encrypted storage folders.
*   Generate a weekly report of all files processed and categorized by the agent for administrative review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Chatwork and storage provider connections via the Composio dashboard.
4. Ensure nodes are correctly mapped and all API keys are validated in the settings panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives file metadata and message context from Chatwork.
*   **Agent**: Analyzes the file type and content to determine the appropriate destination and naming format.
*   **Composio Toolset**: Executes the file move, rename, and organization commands in your storage platform.
*   **Chat Output**: Sends a confirmation message back to the Chatwork room with a link to the organized file.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Organize all files uploaded in the 'Marketing' room into the 'Q3 Assets' folder.`
* `Rename all PDF files shared today to follow the format: YYYY-MM-DD_ProjectName_Filename.`
* `Scan the 'General' channel for any unorganized documents and move them to the 'Inbox' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for file classification and decision-making.
*   Prioritize accuracy in file type identification.
*   Strictly adhere to the naming convention schema provided in the system prompt.
*   Flag any files with ambiguous context for manual human review.

### 2) Composio Toolset Node
Requires an active connection to both Chatwork and your target cloud storage (e.g., Google Drive, Dropbox). Ensure the agent has 'Read' access to chat rooms and 'Write' access to destination folders.

### 3) Tool Availability
*   **File Retrieval**: Ability to fetch file binaries and metadata from chat messages.
*   **Storage Management**: Ability to create folders, move files, and rename assets.
*   **Notification**: Ability to post status updates and confirmation messages to specific chat threads.

---

## Related Solutions
*   [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for job management workflows.
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automated research and data gathering for sales accounts.
*   [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automated tracking and resolution of team action items.
