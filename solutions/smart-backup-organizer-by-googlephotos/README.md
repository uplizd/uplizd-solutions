# Smart Backup Organizer (Uplizd) - Intelligent photo categorization and duplicate management

## Summary
The Smart Backup Organizer is an Uplizd AI workflow designed to streamline digital asset management by automatically categorizing, deduplicating, and archiving photos. By leveraging the Composio Toolset to interface with Google Photos, this solution helps users maintain a single source of truth for their media libraries, significantly reducing manual cleanup time and ensuring long-term data hygiene.

---

## Demo
![Smart Backup Organizer workflow showing automated photo categorization and duplicate detection in Google Photos](image.png)
**Alt text (SEO-ready):** Smart Backup Organizer Uplizd workflow for automated Google Photos categorization, duplicate detection, and media library cleanup.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/608b91cf-f5e2-5369-8e70-bdfbded49a1d)

---

## Category
**Data Operations**
- `google-photos`, `data-hygiene`, `automation`, `media-management`, `ai-workflow`, `composio`, `storage-optimization`
This solution provides a robust framework for automating complex photo library maintenance tasks through intelligent AI-driven categorization.

---

## Who is this for?
This solution is designed for individuals and teams looking to reclaim storage space and improve the searchability of their digital media assets.

- **Digital Archivists**
    - Automate the classification of historical photo collections into structured, searchable folders.
- **Content Creators**
    - Quickly identify and remove duplicate assets to keep project media libraries lean and organized.
- **Operations Managers**
    - Maintain strict data hygiene standards across shared company media accounts.
- **Personal Productivity Enthusiasts**
    - Reduce the cognitive load of manual photo sorting with an always-on automated assistant.

---

## Features
- **Intelligent Deduplication**
    - Automatically scans and identifies duplicate images based on metadata and visual similarity to save storage space.
- **Automated Categorization**
    - Uses AI to sort photos into relevant albums based on content, date, and location tags.
- **Composio Toolset Integration**
    - Seamlessly executes API calls to Google Photos to perform bulk operations without manual intervention.
- **Real-time Sync Monitoring**
    - Tracks the status of backup tasks and provides instant alerts upon completion or if errors occur.
- **Customizable Archiving Rules**
    - Define specific logic for moving, tagging, or deleting media based on user-defined retention policies.

---

## Use Cases
**Library Maintenance**
- Automatically move photos older than one year into a dedicated "Archive" album.
- Identify and flag blurry or low-quality images for manual review or deletion.

**Asset Organization**
- Sort vacation photos into specific albums based on location metadata extracted from the image files.
- Group professional headshots and event photos into a "Work" category for easier access.

**Storage Optimization**
- Run a weekly cleanup script to remove duplicate screenshots and temporary images from the primary library.
- Consolidate media from multiple sources into a single, organized master repository.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Backup Organizer template from the library.
3. Configure your Google Photos API credentials within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user commands for library organization tasks.
- **Agent**: Processes instructions and determines the necessary actions for photo management.
- **Composio Toolset**: Executes precise API commands to interact with Google Photos.
- **Chat Output**: Returns a summary of the actions taken and any remaining tasks.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Find and delete all duplicate photos from the last 30 days.`
- `Organize all photos from my 'Summer 2023' trip into a new album.`
- `Move all screenshots to a folder named 'Temporary Screenshots' and delete files older than 6 months.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for all photo management logic.
- Use a model capable of high-precision instruction following (e.g., GPT-4o).
- Instruct the agent to prioritize data integrity and confirm deletions before execution.
- Maintain a clear mapping between user intent and specific Google Photos API endpoints.

### 2) Composio Toolset Node
- Provide a valid Google Photos API key with `photoslibrary.readonly` and `photoslibrary.appendonly` scopes.
- Ensure the connection is authorized for the specific account being managed.

### 3) Tool Availability
- `google_photos_list_media_items`: Fetch current library state.
- `google_photos_create_album`: Organize assets into new categories.
- `google_photos_delete_media`: Safely remove identified duplicates.
- `google_photos_move_to_album`: Relocate files based on AI classification.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial data matching and cleanup.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize the performance of your automated processes.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate records across your CRM platforms.
