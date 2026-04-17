# Project Document Manager (Uplizd) - Automated organization and sharing for project assets

## Summary
The Project Document Manager is an intelligent Uplizd workflow that automates the lifecycle of project documentation within Google Drive. By leveraging the Composio Toolset, the agent categorizes, organizes, and shares files with relevant stakeholders in real-time, ensuring a single source of truth and eliminating manual file management overhead for project teams.

---

## Demo
![Project Document Manager workflow showing Google Drive integration and automated file sorting](image.png)
**Alt text (SEO-ready):** Uplizd Project Document Manager workflow for automated Google Drive file organization, document sharing, and project data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/47d76743-7d7c-58c5-8067-cebd017cdca5)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** google drive, document management, automation, file organization, project management, workflow, composio, ai agent
- This solution bridges the gap between unstructured project files and organized storage, providing a scalable way to maintain document hygiene.

---

## Who is this for?
This solution is designed for teams looking to reduce administrative friction and ensure project assets are always accessible.

- **Project Manager**
    - Automates the distribution of project briefs and status reports to stakeholders without manual email attachments.
- **Operations Lead**
    - Maintains strict folder structures and naming conventions across the organization's Google Drive.
- **Content Strategist**
    - Ensures that final assets are automatically moved to approved project folders upon completion.
- **Team Lead**
    - Provides instant access to the latest project documentation for new team members during onboarding.

---

## Features
- **Automated File Categorization**
    - Uses AI to analyze document content and move files into the correct project-specific Google Drive folders.
- **Smart Stakeholder Sharing**
    - Automatically grants view or edit permissions to designated team members based on project metadata.
- **Real-time Sync**
    - Monitors incoming uploads and triggers organizational workflows the moment a new document is detected.
- **Naming Convention Enforcement**
    - Standardizes file names to ensure searchability and consistency across all project repositories.
- **Composio-Powered Integration**
    - Seamlessly connects with the Google Drive API to perform complex file operations with high reliability.

---

## Use Cases
**Project Lifecycle Management**
- Automatically move finalized design assets from a "Drafts" folder to a "Client-Ready" folder.
- Generate and share summary documents with project stakeholders immediately after a meeting transcript is uploaded.

**Administrative Data Hygiene**
- Identify and relocate orphaned files in the root directory to their respective project folders.
- Clean up duplicate documents by comparing file metadata and keeping the most recent version.

**Team Collaboration**
- Automatically provision access to a new "Project Alpha" folder for all members of the assigned project group.
- Sync project documentation updates to a shared team dashboard or notification channel.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Authenticate your Google Drive account via the Composio connection prompt.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the file path or project command from the user.
- **Agent**: Processes the request and determines the appropriate folder destination or sharing action.
- **Composio Toolset**: Executes the specific Google Drive API calls to move, rename, or share files.
- **Chat Output**: Confirms the successful organization or sharing of the document to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Organize the latest files in my 'Project Alpha' folder by date.`
- `Share the 'Q3 Budget' document with the marketing team lead.`
- `Move all files containing 'Draft' in the title to the 'Archive' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for all file operations.
- Use a model capable of high-reasoning to interpret file naming patterns.
- Set the system instruction to prioritize folder structure integrity.
- Ensure the agent has access to the full file list context for accurate sorting.

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure Google Drive connectivity.
- Define the connection scope to include `drive.file` and `drive.metadata` permissions.

### 3) Tool Availability
- **List Files**: Retrieves directory contents for analysis.
- **Move/Rename**: Handles file organization and structure updates.
- **Share/Permissions**: Manages stakeholder access control.
- **Search**: Locates specific documents based on natural language queries.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automate deep-dive research into client accounts.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform business process automation.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent data across your CRM and storage platforms.
