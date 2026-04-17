# OneDrive Storage Optimizer (Uplizd) - Automated cloud storage cleanup and file lifecycle management

## Summary
The OneDrive Storage Optimizer is an intelligent Uplizd workflow designed to automate file lifecycle management, identify redundant data, and reclaim cloud storage space. By leveraging the Composio Toolset, this solution helps IT administrators and power users maintain digital hygiene, prevent storage overages, and ensure that critical business documents remain organized without manual intervention.

---

## Demo
![OneDrive Storage Optimizer dashboard showing file cleanup recommendations and storage usage metrics](image.png)
**Alt text (SEO-ready):** OneDrive Storage Optimizer dashboard showing file cleanup recommendations, cloud storage usage metrics, and automated file management workflows in Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ab15e2cf-a111-5041-8abe-a6a758063188)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** onedrive, cloud storage, data hygiene, file management, automation, storage optimization, composio, ai workflow
- This solution bridges the gap between cloud storage providers and automated cleanup policies to ensure efficient data lifecycle management.

---

## Who is this for?
This solution is designed for teams and individuals looking to streamline their cloud storage footprint and reduce manual file maintenance.

- **IT Administrators**
    - Automate bulk cleanup tasks across organizational drives to maintain compliance and storage limits.
- **Operations Managers**
    - Ensure team folders remain organized by identifying and archiving stale or duplicate project files.
- **Data Analysts**
    - Reclaim space by programmatically purging temporary datasets and outdated reports from shared environments.
- **Remote Workers**
    - Keep personal and shared workspaces clutter-free by automating the deletion of redundant local-to-cloud sync files.

---

## Features
- **Intelligent File Scanning**
    - Automatically traverses OneDrive directories to identify large, old, or duplicate files based on user-defined thresholds.
- **Automated Lifecycle Policies**
    - Executes pre-configured cleanup rules to move or delete files that meet specific age or size criteria.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely interface with the Microsoft Graph API for real-time file operations.
- **Storage Usage Reporting**
    - Generates summary insights on space reclaimed and current storage health directly within the chat interface.
- **Safe-Delete Verification**
    - Implements a confirmation step or "dry-run" mode to ensure critical documents are never accidentally removed.

---

## Use Cases
**Storage Cost Reduction**
- Automatically identify and flag files larger than 500MB that haven't been accessed in over 180 days.
- Batch-delete temporary cache files and duplicate document versions to stay within cloud storage quotas.

**Data Hygiene & Compliance**
- Audit shared folders to ensure sensitive or expired project documentation is moved to an archive location.
- Standardize file naming and folder structures by identifying orphaned files that do not match current naming conventions.

**Workflow Efficiency**
- Trigger cleanup routines automatically at the end of every fiscal quarter to prepare for new project cycles.
- Notify team leads via chat when specific shared folders exceed storage thresholds, providing a direct link to cleanup actions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Authenticate your OneDrive account within the Composio connection settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user commands for storage analysis or cleanup execution.
- **Agent**: Processes instructions and determines which file management tasks to trigger.
- **Composio Toolset**: Executes secure API calls to list, move, or delete files in OneDrive.
- **Chat Output**: Returns status updates, file summaries, and confirmation messages to the user.

### 3) Run the Flow
Open the Uplizd Playground and try these prompts:
- `List all files in the 'Projects' folder that haven't been modified in over 6 months.`
- `Find and delete all duplicate files in the 'Downloads' directory.`
- `How much storage space can I reclaim by deleting files older than 1 year in the 'Shared' folder?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for file management logic.
- Use a model capable of structured reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize safety by always confirming deletion actions.
- Ensure the system prompt includes clear definitions for "stale" or "redundant" file criteria.

### 2) Composio Toolset Node
- Provide your **Composio API Key** in the node configuration.
- Set the connection scope to `Files.ReadWrite.All` to allow the agent to manage file lifecycle tasks.

### 3) Tool Availability
- `list_files`: Retrieve metadata and paths for files within specific directories.
- `delete_file`: Securely remove identified redundant files.
- `move_file`: Transfer stale documents to an archive folder.
- `get_file_properties`: Fetch size and last-modified timestamps for analysis.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track usage metrics and account health across various platforms.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the performance and status of automated business workflows.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automate the removal and organization of stale task items.
