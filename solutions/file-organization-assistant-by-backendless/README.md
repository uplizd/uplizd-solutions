# File Organization Assistant (Uplizd) - Automated backend storage management and file hygiene

## Summary
The File Organization Assistant is an intelligent Uplizd workflow designed to automate the categorization, renaming, and archival of assets within Backendless storage. By leveraging AI-driven logic, it eliminates manual file maintenance, ensures a consistent directory structure, and improves data discoverability for development and operations teams.

---

## Demo
![File Organization Assistant workflow showing automated file sorting and categorization in Backendless storage](image.png)
**Alt text (SEO-ready):** File Organization Assistant Uplizd workflow for automated backend file management, categorization, and storage hygiene using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/30a4fb4d-0c18-5783-bb58-2db569b0c876)

---

## Category
- **Primary category:** Data Operations
- **Secondary tags:** backendless, file management, data hygiene, automation, storage optimization, composio, ai workflow
- This solution provides a robust framework for maintaining clean, searchable, and organized cloud storage environments through automated AI intervention.

---

## Who is this for?
This solution is designed for technical teams looking to reduce storage clutter and improve asset retrieval efficiency.

- **Backend Developers**
    - Automates the cleanup of temporary files and organizes assets into logical directory structures.
- **System Administrators**
    - Ensures compliance with naming conventions and storage policies across production environments.
- **Product Managers**
    - Improves development velocity by ensuring that design assets and documentation are always easy to locate.
- **Operations Leads**
    - Reduces cloud storage costs by identifying and archiving stale or redundant data automatically.

---

## Features
- **Intelligent Categorization**
    - Automatically sorts files into folders based on metadata, file type, or content analysis.
- **Dynamic Renaming**
    - Enforces standardized naming conventions to ensure consistency across your entire backend storage.
- **Automated Archival**
    - Identifies and moves aged or unused files to cold storage, optimizing primary storage performance.
- **Composio-Powered Execution**
    - Utilizes the Composio Toolset to securely interact with Backendless APIs for real-time file operations.
- **Customizable Logic**
    - Easily adjust the Agent instructions to define specific organizational rules that match your project requirements.

---

## Use Cases
**Storage Hygiene**
- Automatically move files older than 90 days into an 'Archive' directory to maintain a clean workspace.
- Identify and delete duplicate files based on hash comparisons to save storage bandwidth.

**Asset Management**
- Automatically rename uploaded images with descriptive tags based on their content or associated user ID.
- Sort incoming user-generated content into specific folders based on the file extension or upload source.

**Workflow Optimization**
- Trigger a cleanup process whenever a specific storage threshold is reached to prevent system bottlenecks.
- Organize project documentation and logs into dated sub-directories for easier historical auditing.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Connect your Backendless account via the Composio Toolset integration.
3. Configure the trigger settings to define which storage buckets the assistant should monitor.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the file path or storage bucket trigger signal.
- **Agent**: Analyzes the file metadata and determines the appropriate organizational action.
- **Composio Toolset**: Executes the move, rename, or delete commands within Backendless.
- **Chat Output**: Confirms the successful completion of the file organization task.

### 3) Run the Flow
Use the Playground to test your organization logic with these prompts:
- `Organize all files in the 'uploads' folder into sub-folders by file type.`
- `Rename all files in the 'assets' directory to follow the format 'YYYY-MM-DD-filename'.`
- `Move all files older than 6 months from the 'main' bucket to the 'archive' bucket.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your storage logic.
- Instruct the agent to prioritize file safety and avoid deleting files without explicit confirmation.
- Define clear naming conventions (e.g., lowercase, hyphens instead of spaces) in the system prompt.
- Set a clear hierarchy for folder structures to ensure the agent follows your specific taxonomy.

### 2) Composio Toolset Node
- Provide your Backendless API credentials within the Composio dashboard.
- Ensure the connection scope includes read/write permissions for the specific storage buckets you intend to manage.

### 3) Tool Availability
- **File Metadata Reader**: Retrieves file size, creation date, and type.
- **Storage Operations Manager**: Executes move, rename, and delete commands.
- **Bucket Scanner**: Lists contents of specific directories for bulk processing.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex business processes and task triggers.
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) - Monitor and report on data usage patterns across your workspace.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Audit and secure user permissions within your backend environment.
