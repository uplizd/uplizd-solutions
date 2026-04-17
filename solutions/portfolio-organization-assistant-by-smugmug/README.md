# Portfolio Organization Assistant (Uplizd) - Automate and structure your photography portfolio

## Summary
The Portfolio Organization Assistant is an intelligent Uplizd workflow designed to streamline the management and categorization of photography assets within SmugMug. By leveraging AI-driven metadata extraction and automated folder structuring, this solution helps photographers and creative agencies maintain a single source of truth for their visual libraries, significantly reducing manual sorting time and improving searchability across large-scale portfolios.

---

## Demo
![Portfolio Organization Assistant workflow showing SmugMug integration and AI-driven asset categorization](image.png)
**Alt text (SEO-ready):** Portfolio Organization Assistant by Uplizd, automated photography asset management, SmugMug AI integration, and creative workflow optimization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6m+s8/gAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVHjaY2BgYPhPAwJgqGg8GoaGgQGj0TAYNBoNg0EjAAAM/wQk19+01gAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/ec8e878c-411f-5166-bdb9-f1d2ac5f104b)

---

## Category
**Primary category:** Creative Operations  
**Secondary tags:** `smugmug`, `photography`, `asset management`, `ai workflow`, `composio`, `data organization`, `automation`  
This solution bridges the gap between raw photography uploads and structured portfolio management by automating metadata tagging and folder placement.

---

## Who is this for?
This solution is designed for creative professionals and teams who need to manage high-volume visual content with precision.

*   **Professional Photographers**
    *   Automate the tedious process of sorting thousands of raw images into client-ready galleries.
*   **Creative Directors**
    *   Ensure brand consistency by enforcing standardized folder structures across all team portfolios.
*   **Studio Managers**
    *   Reduce administrative overhead by automating the metadata enrichment of archived assets.
*   **Digital Asset Librarians**
    *   Maintain high-quality data hygiene by ensuring every image is correctly tagged and indexed upon upload.

---

## Features
- **Automated Metadata Tagging**
  Uses AI to analyze image content and automatically apply descriptive tags for improved searchability.
- **Intelligent Folder Routing**
  Dynamically moves images into specific SmugMug folders based on date, event type, or custom metadata attributes.
- **Composio Toolset Integration**
  Seamlessly connects with SmugMug APIs to perform real-time file operations and account updates.
- **Batch Processing Engine**
  Handles large volumes of assets in a single workflow execution, ensuring consistent organization across entire shoots.
- **Customizable Logic Rules**
  Allows users to define unique sorting criteria that adapt to specific client requirements or project workflows.

---

## Use Cases
**Client Gallery Management**
*   Automatically move client-selected images into "Final Selection" folders immediately after tagging.
*   Trigger notifications when a new gallery is fully organized and ready for client review.

**Archival Data Hygiene**
*   Identify and move older, unorganized assets into a structured "Archive" hierarchy based on year and location.
*   Standardize file naming conventions across legacy portfolios to match current studio branding.

**Project-Based Organization**
*   Sort images by specific project codes or event names extracted from file metadata or input prompts.
*   Sync portfolio updates across multiple SmugMug sub-folders to ensure a clean, professional presentation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Portfolio Organization Assistant template from the marketplace.
3. Connect your SmugMug account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives instructions regarding the specific portfolio or folder to be organized.
*   **Agent**: Interprets the intent and determines the necessary file operations based on the user's prompt.
*   **Composio Toolset**: Executes the API calls to SmugMug to categorize, tag, or move assets.
*   **Chat Output**: Confirms the successful organization of assets and provides a summary of actions taken.

### 3) Run the Flow
Access the Playground to test your organization logic:
*   `"Organize all images from the 'Summer Wedding' shoot into the '2023 Weddings' folder."`
*   `"Tag all photos in the 'Nature' gallery with 'landscape' and 'outdoor' keywords."`
*   `"Move all unorganized assets from the root directory into the 'Pending Review' folder."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your asset management logic.
*   Focus on identifying the target directory and the specific organization rule (e.g., date-based or tag-based).
*   Maintain a neutral, professional tone when reporting back on file operations.
*   Prioritize accuracy when mapping image metadata to folder structures to prevent misfiling.

### 2) Composio Toolset Node
*   **API Key**: Ensure your SmugMug API credentials are securely stored in the Composio dashboard.
*   **Connection Scope**: Grant read/write permissions to the specific folders you intend to manage.

### 3) Tool Availability
*   `smugmug_list_folders`: Retrieve current directory structures.
*   `smugmug_move_image`: Execute the transfer of assets between folders.
*   `smugmug_add_tags`: Apply metadata labels to selected images.
*   `smugmug_get_image_info`: Fetch existing metadata for decision-making.

---

## Related Solutions
*   [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data for better client targeting.
*   [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate records across your CRM.
*   [../you-tube-content-performance-optimizer-by-youtube/README.md](../you-tube-content-performance-optimizer-by-youtube/README.md) — Optimize video content and metadata for better reach.
