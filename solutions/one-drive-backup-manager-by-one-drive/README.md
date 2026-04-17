# OneDrive Backup Manager (Uplizd) - Automated cloud file synchronization and data protection

## Summary
The OneDrive Backup Manager is an intelligent Uplizd workflow designed to automate file lifecycle management, ensuring critical documents are backed up, organized, and synchronized across your cloud infrastructure. By leveraging the Composio Toolset, this solution provides a single source of truth for your file storage, reducing manual overhead, preventing data loss through automated versioning, and maintaining strict folder hygiene for distributed teams.

---

## Demo
![OneDrive Backup Manager workflow interface showing file synchronization and automated backup triggers](image.png)
**Alt text (SEO-ready):** OneDrive Backup Manager Uplizd workflow for automated cloud file synchronization, data backup, and folder hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f22d252c-e41a-5c14-afde-f2db64c9ef90)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** onedrive, cloud storage, backup, data sync, automation, file management, composio, ai workflow
- This solution streamlines cloud storage operations by connecting OneDrive to intelligent agents for automated file organization and backup verification.

---

## Who is this for?
This solution is designed for professionals managing high-volume document workflows who need to ensure data integrity without manual intervention.

- **Operations Manager**
    - Automates routine file archiving to ensure compliance and storage efficiency.
- **IT Administrator**
    - Monitors backup status across organizational drives to prevent data silos.
- **Project Lead**
    - Ensures team assets are consistently synced and organized in designated project folders.
- **Data Analyst**
    - Maintains clean, version-controlled datasets for reporting and historical analysis.

---

## Features
- **Automated Sync Triggers**
  Real-time synchronization between local directories and OneDrive to ensure data redundancy.
- **Intelligent File Organization**
  Uses AI to categorize and move files into structured sub-folders based on metadata and naming conventions.
- **Version Control Management**
  Automatically tracks file iterations and archives older versions to prevent accidental data loss.
- **Composio-Powered Connectivity**
  Integrates seamlessly with the Microsoft Graph API via the Composio Toolset for secure, authenticated file operations.
- **Backup Health Monitoring**
  Generates automated reports on backup success rates and alerts users to sync conflicts or missing files.

---

## Use Cases
**Disaster Recovery & Redundancy**
- Automatically mirror critical project folders to a secure backup directory every 24 hours.
- Trigger immediate cloud uploads for new files created in local "Working" folders.

**Data Hygiene & Cleanup**
- Identify and move stale files older than 90 days to an "Archive" folder to optimize storage.
- Standardize file naming patterns across the team drive to improve searchability and retrieval.

**Cross-Platform Integration**
- Sync OneDrive attachments directly from email workflows into specific client-based folders.
- Automate the movement of finalized reports from OneDrive to external CRM storage locations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your OneDrive account within the Composio connection settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled commands to initiate backup tasks.
- **Agent**: Processes instructions to identify, move, or verify files based on defined logic.
- **Composio Toolset**: Executes secure API calls to OneDrive for file listing, moving, and deletion.
- **Chat Output**: Returns a summary of the backup operation, including files processed and any errors encountered.

### 3) Run the Flow
Use the Playground to test your backup logic with these prompts:
- `Backup all files in the 'Q3-Project' folder to the 'Archive-2023' directory.`
- `List all files in my OneDrive that haven't been modified in over 6 months.`
- `Sync the 'Client-Assets' folder and notify me if any file conflicts are detected.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for file operations, interpreting user intent into specific API actions.
- Use a model capable of high-precision instruction following (e.g., GPT-4o).
- Set the system prompt to prioritize data integrity and confirm destructive actions (like deletion).
- Ensure the agent has access to the full file path context for accurate directory management.

### 2) Composio Toolset Node
- Provide your Microsoft OneDrive API credentials within the Composio dashboard.
- Set the connection scope to include `Files.ReadWrite.All` to ensure the agent can perform necessary backup and organization tasks.

### 3) Tool Availability
- `onedrive_list_files`: Retrieve metadata for files within specific directories.
- `onedrive_move_file`: Relocate files to designated backup or archive locations.
- `onedrive_get_file_details`: Check timestamps and version information for hygiene tasks.
- `onedrive_delete_file`: Safely remove redundant files after successful backup verification.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial data reconciliation and ledger updates.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize customer records across multiple CRM platforms.
- [../account-health-usage-monitor-by-jotform/README.md](../account-health-usage-monitor-by-jotform/README.md) - Track user engagement and account health metrics.
