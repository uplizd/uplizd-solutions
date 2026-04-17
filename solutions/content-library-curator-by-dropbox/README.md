# Content Library Curator (Uplizd) - Automate asset organization and discovery

## Summary
The Content Library Curator by Dropbox is an intelligent Uplizd AI workflow designed to streamline digital asset management by automatically categorizing, tagging, and indexing files within your Dropbox storage. It eliminates manual filing bottlenecks, ensuring that marketing and creative teams maintain a single source of truth for their collateral while significantly increasing pipeline velocity through improved searchability and data hygiene.

---

## Demo
![Content Library Curator workflow showing file ingestion, AI-driven tagging, and Dropbox organization](image.png)
**Alt text (SEO-ready):** Content Library Curator Uplizd workflow for automated Dropbox file tagging, asset organization, and AI-driven content discovery.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/09412395-bf76-5a0f-832c-010be67df0cb)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** dropbox, content management, asset library, ai workflow, data hygiene, composio, automation, file organization
- This solution bridges the gap between raw cloud storage and structured content libraries, enabling automated governance for marketing teams.

---

## Who is this for?
This workflow is designed for teams managing high volumes of creative assets who need to maintain order without manual administrative overhead.

- **Content Manager**
    - Automates the filing of new assets into the correct project folders based on metadata.
- **Creative Director**
    - Ensures all team members can instantly locate the latest versions of approved brand assets.
- **Marketing Operations Lead**
    - Maintains strict data hygiene across cloud storage to prevent duplicate or mislabeled files.
- **Digital Asset Librarian**
    - Reduces time spent on manual tagging and metadata entry by leveraging AI-driven classification.

---

## Features
- **Automated Metadata Tagging**
    - Uses AI to analyze file content and apply relevant tags, making every asset searchable by context rather than just filename.
- **Intelligent Folder Routing**
    - Automatically moves or copies files into specific Dropbox directories based on project status, asset type, or campaign association.
- **Duplicate Detection & Cleanup**
    - Identifies redundant files within the library to ensure storage efficiency and prevent versioning confusion.
- **Composio-Powered Dropbox Integration**
    - Leverages the Composio Toolset to perform real-time read/write operations on your Dropbox account securely.
- **Customizable Classification Logic**
    - Allows users to define specific rules for how the agent should interpret and categorize different file formats.

---

## Use Cases
**Asset Lifecycle Management**
- Automatically archive outdated campaign assets into a "Legacy" folder once a project end date has passed.
- Move new creative drafts from an "Inbox" folder to a "Review" folder upon detection.

**Brand Compliance & Governance**
- Scan files for specific naming conventions and flag non-compliant assets for administrative review.
- Ensure all public-facing assets are tagged with mandatory "Approved" or "Draft" status labels.

**Search & Discovery Optimization**
- Generate descriptive summaries for long-form documents to improve internal search relevance.
- Map assets to specific campaign IDs to allow for rapid retrieval of all collateral related to a single marketing initiative.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Dropbox account via the Composio Toolset node.
3. Configure your target folder paths in the Agent instructions.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger or manual command to scan specific folders.
- **Agent**: Processes file metadata and determines the appropriate organizational action.
- **Composio Toolset**: Executes the Dropbox API calls to move, tag, or rename files.
- **Chat Output**: Provides a summary report of the files processed and actions taken.

### 3) Run the Flow
Use the Playground to test your curator with prompts like:
- `Organize all files in the 'Q3-Campaign' folder by asset type.`
- `Find all untagged images in the 'Drafts' folder and apply the 'Pending-Review' tag.`
- `Move all files older than 30 days from 'Active' to 'Archive' and notify me via the output.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for your library structure.
- Define your folder taxonomy clearly in the system prompt.
- Set the agent to prioritize accuracy over speed for sensitive file movements.
- Use structured output to ensure the Composio Toolset receives precise file paths.

### 2) Composio Toolset Node
- Provide your Dropbox API credentials within the Composio dashboard.
- Ensure the connection scope includes `files.metadata.read` and `files.content.write` permissions.

### 3) Tool Availability
- **Dropbox List Files**: To scan directory contents.
- **Dropbox Move/Rename**: To execute organizational changes.
- **Dropbox Update Metadata**: To apply tags and descriptions.

---

## Related Solutions
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) — Organize and manage collaborative design templates.
- [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) — Automate the deployment of video assets across channels.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and structured data across your CRM platforms.
