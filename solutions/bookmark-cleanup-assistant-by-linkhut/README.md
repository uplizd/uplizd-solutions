# Bookmark Cleanup Assistant (Uplizd) - Intelligent organization and link hygiene for your browser bookmarks

## Summary
The Bookmark Cleanup Assistant is an AI-powered workflow designed to restore order to cluttered digital workspaces by automatically auditing, categorizing, and validating saved URLs. By leveraging the Composio Toolset to interface with browser and cloud-based bookmark managers, this solution eliminates dead links, removes duplicates, and applies consistent tagging, ensuring your research and resources remain a reliable single source of truth for improved productivity.

---

## Demo
![Bookmark Cleanup Assistant interface showing automated URL validation and categorization workflow](image.png)
**Alt text (SEO-ready):** Bookmark Cleanup Assistant workflow in Uplizd, showing automated URL validation, link hygiene, and bookmark categorization using the Composio Toolset.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6o3995QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVHjaY2BgYPjP////fxhQAsZgYGBg+A8Xw4gGjEEDAA44CgE+T9/BAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/b0adbb30-c822-5537-8bff-63b002c3733d)

---

## Category
**Primary category:** Operations  
**Secondary tags:** bookmark management, data hygiene, link validation, productivity, automation, composio, ai workflow, digital organization  
This solution streamlines digital asset management by automating the maintenance of bookmark libraries through intelligent agent-based categorization.

---

## Who is this for?
This solution is designed for power users and professionals who rely on extensive bookmark collections to manage their daily research and project workflows.

*   **Research Analysts**
    *   Maintains a clean, searchable database of industry reports and competitive intelligence links.
*   **Content Creators**
    *   Organizes inspiration and reference material into structured, easily accessible folders.
*   **Knowledge Managers**
    *   Ensures long-term link integrity by identifying and removing broken or outdated URLs.
*   **Project Managers**
    *   Centralizes team-wide resource links to ensure all stakeholders are accessing the most current documentation.

---

## Features
- **Automated Link Validation**
  Real-time verification of URL status to identify and flag 404 errors or dead pages.
- **Intelligent Categorization**
  Uses AI to analyze page content and automatically move bookmarks into relevant, predefined folders.
- **Duplicate Detection**
  Scans your entire collection to identify and merge redundant entries, saving storage and reducing clutter.
- **Metadata Enrichment**
  Automatically adds descriptive tags and summaries to bookmarks for faster retrieval and better searchability.
- **Composio-Powered Integration**
  Seamlessly connects with browser-based bookmark APIs to execute cleanup actions directly within your existing workflow.

---

## Use Cases
**Link Maintenance**
*   Identify and remove broken links from research archives to maintain high data quality.
*   Consolidate multiple versions of the same resource into a single, canonical bookmark entry.

**Workflow Optimization**
*   Automatically sort new bookmarks into project-specific folders based on keywords in the page title.
*   Flag bookmarks that haven't been accessed in over 90 days for archival or deletion.

**Knowledge Management**
*   Apply consistent naming conventions across large bookmark libraries for improved team collaboration.
*   Generate summary reports of your most-used resources to identify key information sources.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Bookmark Cleanup Assistant.
2. Click "Import" to load the workflow into your workspace.
3. Connect your preferred bookmark manager via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your cleanup commands or scan triggers.
*   **Agent**: Processes the logic for link validation and content categorization.
*   **Composio Toolset**: Executes the API calls to read, update, and delete bookmarks.
*   **Chat Output**: Delivers a summary report of the cleanup actions performed.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Scan my 'Research' folder for broken links and remove them.`
* `Categorize all uncategorized bookmarks based on their page content.`
* `Find and merge duplicate entries in my 'Work' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary decision-maker for link organization and validation logic.
*   Prioritize accuracy when identifying broken links.
*   Maintain consistent folder naming conventions based on provided categories.
*   Ensure the agent provides a clear, bulleted summary of all changes made after each run.

### 2) Composio Toolset Node
*   **API Key**: Provide your authorized Composio API key to enable secure access to your bookmark manager.
*   **Connection Scope**: Ensure the toolset has read/write permissions for the specific browser or cloud bookmark folders you intend to manage.

### 3) Tool Availability
*   `list_bookmarks`: Retrieve current bookmark structures.
*   `validate_url`: Check the HTTP status of saved links.
*   `update_bookmark`: Modify titles, tags, or folder locations.
*   `delete_bookmark`: Remove redundant or broken entries.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Automate the collection of account-level data for improved CRM hygiene.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate records across your sales and marketing databases.
*   [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Streamline task management by identifying and resolving stale action items.
