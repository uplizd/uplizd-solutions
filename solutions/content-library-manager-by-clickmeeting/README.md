# Content Library Manager (Uplizd) - Automate and optimize your meeting resource organization

## Summary
The Content Library Manager by ClickMeeting is an intelligent Uplizd workflow designed to streamline the organization, retrieval, and distribution of meeting assets. By automating the categorization and management of your digital library, this solution eliminates manual filing bottlenecks, ensures your team has a single source of truth for meeting materials, and significantly improves pipeline velocity for content-heavy sales and support operations.

---

## Demo
![Content Library Manager workflow interface showing automated file categorization and ClickMeeting integration](image.png)
**Alt text (SEO-ready):** Content Library Manager Uplizd workflow, ClickMeeting asset organization, automated file management, and digital library optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/73e85304-9cc7-56cb-9b0e-f5125cbb4d2f)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content management, clickmeeting, digital assets, file organization, automation, workflow, composio, data hygiene
- This solution bridges the gap between your meeting platform and content repository to ensure high-value assets are always accessible and correctly categorized.

---

## Who is this for?
This solution is designed for teams managing high volumes of meeting recordings, slide decks, and collateral who need to maintain strict organizational standards.

- **Marketing Managers**
    - Ensure all meeting collateral is tagged and filed according to campaign standards without manual intervention.
- **Sales Enablement Leads**
    - Provide AEs with instant access to the latest approved meeting assets, reducing time spent searching for resources.
- **Customer Success Managers**
    - Automatically archive and categorize client-specific meeting recordings for improved account history tracking.
- **Operations Specialists**
    - Maintain data hygiene across the content library, ensuring no duplicate or outdated files clutter the workspace.

---

## Features
- **Automated Asset Categorization**
    - Uses AI to analyze meeting metadata and content, automatically assigning files to the correct library folders.
- **ClickMeeting Integration**
    - Leverages the Composio Toolset to directly interact with ClickMeeting APIs for seamless file retrieval and management.
- **Real-Time Sync**
    - Ensures that as soon as a meeting concludes, assets are processed and moved to the designated storage location.
- **Intelligent Search Indexing**
    - Automatically generates descriptive tags and summaries for files, making your library searchable and intuitive.
- **Compliance & Hygiene Monitoring**
    - Identifies and flags outdated or redundant files, keeping your content library lean and compliant with company policies.

---

## Use Cases
**Meeting Asset Archiving**
- Automatically move post-webinar slide decks into project-specific folders.
- Archive client-facing meeting recordings to secure, categorized storage buckets.

**Sales Enablement Support**
- Sync the latest product demo recordings to the central sales enablement portal.
- Update shared team drives with new collateral generated during internal strategy sessions.

**Content Lifecycle Management**
- Flag meeting assets that have exceeded their retention period for archival or deletion.
- Standardize naming conventions for all uploaded meeting files across the organization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Library Manager template using the provided JSON configuration.
3. Connect your ClickMeeting account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers for new meeting assets or manual organization requests.
- **Agent**: Processes file metadata and determines the appropriate destination folder.
- **Composio Toolset**: Executes the API calls to ClickMeeting for file movement and tagging.
- **Chat Output**: Confirms the successful organization and storage of the assets.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Organize the latest recordings from the Q3 product launch webinar.`
- `Move all slide decks from last week's sales meetings to the 'Q4 Collateral' folder.`
- `Scan the library and flag any meeting assets older than 6 months for review.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine for file classification and metadata extraction.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruction: "Analyze the meeting metadata, identify the content type, and move the file to the corresponding folder in the library."
- Ensure the agent is configured to handle errors gracefully if a file path is missing.

### 2) Composio Toolset Node
- Provide your ClickMeeting API credentials within the Composio dashboard.
- Set the connection scope to allow read/write access to your meeting library and file management endpoints.

### 3) Tool Availability
- `clickmeeting_list_files`: Retrieve current assets from the meeting platform.
- `clickmeeting_move_file`: Update the storage location of specific assets.
- `clickmeeting_update_metadata`: Apply tags and descriptions to files for better searchability.

---

## Related Solutions
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed account intelligence reports for sales teams.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate CRM data through automated cleanup.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage and optimize your sales pipeline stages and follow-ups.
