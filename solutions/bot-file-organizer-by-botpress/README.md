# Bot File Organizer (Uplizd) - Automated asset management and cleanup for Botpress workflows

## Summary
The Bot File Organizer (Uplizd) is an intelligent automation workflow designed to streamline digital asset management by automatically categorizing, renaming, and archiving files within Botpress environments. By leveraging AI-driven logic to maintain folder hygiene and metadata consistency, this solution eliminates manual file maintenance, reduces storage clutter, and ensures that development teams maintain a single source of truth for their bot assets.

---

## Demo
![Bot File Organizer dashboard showing automated file categorization and cleanup logs](image.png)
**Alt text (SEO-ready):** Bot File Organizer dashboard showing automated file categorization and cleanup logs for Uplizd AI workflows and Botpress asset management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a422710e-2a19-57d4-af55-31a714f5a3a5)

---

## Category
**Primary category:** Operations  
**Secondary tags:** botpress, file management, automation, asset cleanup, data hygiene, workflow optimization, composio, ai agent  
This solution automates the lifecycle of bot assets, ensuring your development environment remains organized and performant through intelligent file handling.

---

## Who is this for?
This solution is designed for technical teams and bot developers who need to maintain clean, scalable project environments.

* **Bot Developer**
    * Reduces time spent on manual file sorting and directory maintenance.
* **Operations Manager**
    * Ensures compliance and consistent naming conventions across all bot assets.
* **Technical Lead**
    * Prevents storage bloat and improves project navigation for the entire team.
* **QA Engineer**
    * Simplifies the testing process by ensuring all required assets are correctly located and accessible.

---

## Features
- **Automated Asset Categorization**
  Intelligently sorts files into designated folders based on content type, date, or project-specific tags.
- **Intelligent File Renaming**
  Applies standardized naming conventions to all uploaded assets to ensure searchability and consistency.
- **Cleanup and Archival Logic**
  Automatically identifies and moves stale or unused files to an archive folder, optimizing project storage.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely interact with file systems and cloud storage providers in real-time.
- **Metadata Enrichment**
  Automatically extracts and attaches relevant metadata to files, making it easier to track asset usage and origin.

---

## Use Cases
**Project Hygiene**
* Automatically moving temporary test logs to an archive directory after 24 hours.
* Renaming raw image uploads to match the project's specific asset naming schema.

**Asset Management**
* Categorizing media assets into sub-folders based on their file extension (e.g., .png, .json, .pdf).
* Syncing local bot assets with cloud storage buckets to ensure redundancy and accessibility.

**Workflow Optimization**
* Flagging missing or orphaned assets that are referenced in the bot flow but not found in the directory.
* Generating a summary report of all file changes performed during the weekly cleanup cycle.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Bot File Organizer template via the provided solution URL.
3. Connect your Botpress account and storage provider via the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger command or scheduled event to start the organization process.
* **Agent**: Analyzes the file directory and determines the appropriate action based on defined rules.
* **Composio Toolset**: Executes the file system operations (move, rename, delete) securely.
* **Chat Output**: Provides a summary report of all files organized or archived during the run.

### 3) Run the Flow
Use the Playground to test your organization rules:
* `Organize all files in the /assets folder by file type.`
* `Rename all files in /uploads to follow the YYYY-MM-DD-filename format.`
* `Archive all files older than 30 days into the /archive folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for file operations.
* Use a model capable of logical reasoning to interpret file metadata.
* Set instructions to prioritize file safety and prevent accidental deletion.
* Configure the agent to report errors if it encounters restricted system files.

### 2) Composio Toolset Node
* Provide your API key to authorize the agent to perform read/write operations on your file system.
* Set the connection scope to only include the directories required for bot asset management.

### 3) Tool Availability
* **File System Read**: Allows the agent to index current files.
* **File System Write**: Enables renaming and moving of assets.
* **Directory Management**: Permits the creation of new folders for archiving.
* **Metadata Extraction**: Allows the agent to read file properties for smarter categorization.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the performance and uptime of your automated bot workflows.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Manage and resolve pending tasks and action items across your development stack.
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform comprehensive security and configuration audits on your connected accounts.
