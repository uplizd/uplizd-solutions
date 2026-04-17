# Document Cleanup Assistant (Uplizd) - Automate file organization and storage hygiene

## Summary
The Document Cleanup Assistant is an intelligent Uplizd workflow designed to scan, identify, and manage outdated or duplicate files within your Dropbox storage. By automating the lifecycle of your digital assets, this solution helps teams maintain a single source of truth, reduce storage bloat, and improve pipeline velocity by ensuring critical documents are always easy to locate.

---

## Demo
![Document Cleanup Assistant workflow interface showing Dropbox integration and file scanning nodes](image.png)
**Alt text (SEO-ready):** Document Cleanup Assistant (Uplizd) workflow interface showing Dropbox file scanning, duplicate detection, and automated cleanup integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b0d38520-156f-5544-a406-2c031ababab3)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** dropbox, file management, document cleanup, automation, data storage, workflow optimization, ai agent, composio
- This solution streamlines digital asset management by leveraging AI to enforce storage policies and eliminate redundant files across your cloud infrastructure.

---

## Who is this for?
This solution is designed for teams and individuals looking to regain control over their cloud storage environments.

- **Operations Manager**
    - Automates the enforcement of data retention policies to maintain compliance and storage efficiency.
- **IT Administrator**
    - Reduces manual overhead by identifying and archiving stale documents without human intervention.
- **Project Lead**
    - Ensures team members are always accessing the latest version of project files by purging duplicates.
- **Content Strategist**
    - Maintains a clean and organized repository, making it easier to retrieve high-value assets for ongoing campaigns.

---

## Features
- **Intelligent File Scanning**
    - Uses the Composio Toolset to crawl Dropbox directories and analyze file metadata in real-time.
- **Duplicate Detection Engine**
    - Automatically identifies redundant files based on content hashes and naming conventions to prevent storage waste.
- **Automated Cleanup Policies**
    - Executes pre-defined actions such as moving, archiving, or deleting files based on age and usage frequency.
- **Real-time Reporting**
    - Generates summary logs of all cleanup activities, providing visibility into storage savings and file movements.
- **Seamless Dropbox Integration**
    - Leverages secure API connections to perform file operations directly within your existing Dropbox workspace.

---

## Use Cases
**Storage Optimization**
- Automatically move files older than 90 days to an 'Archive' folder to keep active workspaces lean.
- Identify and remove duplicate versions of project proposals to save cloud storage space.

**Compliance & Security**
- Scan for sensitive document types that have been stored in unauthorized public-facing folders.
- Ensure that outdated legal or financial documents are moved to secure, restricted-access storage locations.

**Workflow Efficiency**
- Clean up temporary 'Export' folders by deleting files that have not been accessed in over 30 days.
- Organize project assets by automatically categorizing files based on naming patterns and metadata tags.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the 'Document Cleanup Assistant' template.
2. Click 'Import' to load the workflow into your workspace.
3. Connect your Dropbox account via the Composio Toolset node.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives user commands to initiate a scan or cleanup task.
- **Agent**: Processes instructions and determines which file operations to execute.
- **Composio Toolset**: Connects to Dropbox to perform file listing, moving, and deletion.
- **Chat Output**: Returns a summary report of the files processed and actions taken.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Scan my 'Projects' folder and identify all duplicate files created in the last month.`
- `Move all files in the 'Drafts' folder older than 60 days to the 'Archive' directory.`
- `Provide a report of all files in the 'Marketing' folder that haven't been opened in 90 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your file management logic.
- Set the system prompt to prioritize file safety and data integrity.
- Define clear thresholds for what constitutes an "outdated" or "duplicate" file.
- Instruct the agent to provide a confirmation summary before performing bulk deletions.

### 2) Composio Toolset Node
- Provide your Dropbox API credentials within the Composio configuration.
- Ensure the connection scope includes read, write, and delete permissions for the target folders.

### 3) Tool Availability
- `dropbox_list_files`: Retrieves directory contents for analysis.
- `dropbox_move_file`: Transfers files to archive locations.
- `dropbox_delete_file`: Removes redundant or stale assets.
- `dropbox_get_metadata`: Fetches file creation and last-modified timestamps.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Audit and monitor account-level configurations and security settings.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational status and efficiency of your automated workflows.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean CRM records by identifying and merging duplicate entries.
