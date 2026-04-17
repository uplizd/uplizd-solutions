# Asset Cleanup Manager (Uplizd) - Automated media asset lifecycle and storage optimization

## Summary
The Asset Cleanup Manager is an intelligent Uplizd workflow designed to automate the identification, auditing, and deletion of redundant or outdated media assets within Cloudinary. By streamlining digital asset management, this solution helps marketing and operations teams reduce storage costs, maintain brand consistency, and improve pipeline velocity by ensuring only high-quality, relevant assets remain in the production environment.

---

## Demo
![Asset Cleanup Manager workflow showing Cloudinary integration for automated media asset auditing and deletion](../image.png)
**Alt text (SEO-ready):** Asset Cleanup Manager workflow for Cloudinary, showing automated media asset auditing, storage optimization, and redundant file deletion in the Uplizd AI platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c9c3f5c5-129a-5d61-b6c5-80d2e2c14155)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** cloudinary, digital asset management, data hygiene, storage optimization, automation, media management, composio, ai workflow
- This solution bridges the gap between raw cloud storage and organized marketing operations by automating the lifecycle of digital assets.

---

## Who is this for?
This solution is designed for teams managing high-volume media libraries who need to maintain storage efficiency and asset quality.

- **Marketing Operations Manager**
    - Automates the removal of expired campaign assets to keep storage costs predictable.
- **Digital Asset Manager**
    - Ensures the media library remains clean and compliant by purging duplicate or unused files.
- **Creative Director**
    - Maintains brand integrity by ensuring only approved, current assets are available for production.
- **Cloud Infrastructure Lead**
    - Reduces cloud storage overhead through automated, policy-driven cleanup cycles.

---

## Features
- **Automated Asset Auditing**
    - Scans Cloudinary repositories in real-time to identify assets that haven't been accessed or updated within a defined timeframe.
- **Intelligent Deletion Policies**
    - Uses AI-driven logic to distinguish between critical brand assets and temporary campaign files before triggering cleanup.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interface with Cloudinary APIs for granular control over media management.
- **Compliance-Aware Cleanup**
    - Ensures that assets tagged as 'permanent' or 'legal' are excluded from automated deletion cycles.
- **Execution Reporting**
    - Generates a summary report of all deleted assets, providing a clear audit trail for administrative review.

---

## Use Cases
**Storage Cost Optimization**
- Automatically purge high-resolution assets from completed seasonal campaigns to free up storage space.
- Identify and remove duplicate media files that are consuming unnecessary cloud capacity.

**Brand & Asset Hygiene**
- Clean up outdated product imagery that no longer aligns with current brand guidelines or visual identity.
- Archive or delete temporary assets created during the design process that were never moved to production.

**Operational Efficiency**
- Schedule weekly cleanup tasks to prevent media library bloat without manual intervention.
- Validate asset usage against active project lists to ensure only relevant files remain in the active directory.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the Asset Cleanup Manager template to your workspace.
3. Connect your Cloudinary account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives parameters such as date ranges or asset tags for the cleanup task.
- **Agent**: Processes instructions to evaluate asset metadata and apply deletion logic.
- **Composio Toolset**: Executes secure API calls to Cloudinary for listing, filtering, and deleting assets.
- **Chat Output**: Returns a confirmation log detailing the assets processed and successfully removed.

### 3) Run the Flow
- `Find and delete all assets in the 'Summer-2023' folder that have not been accessed in 90 days.`
- `List all duplicate images in the main repository and remove the older versions.`
- `Perform a cleanup of all temporary assets tagged as 'draft' created before January 1st.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for asset lifecycle management.
- Use a model with strong reasoning capabilities to interpret complex cleanup instructions.
- Recommended instruction pattern:
    - Define the scope of the search (folders, tags, or dates).
    - Specify the criteria for "unused" or "outdated" assets.
    - Require a confirmation step or summary report before finalizing deletions.

### 2) Composio Toolset Node
- Provide your Cloudinary API credentials within the Composio dashboard.
- Ensure the connection scope includes `media_library:read` and `media_library:delete` permissions.

### 3) Tool Availability
- `cloudinary_list_assets`: Retrieves metadata for files matching specific search criteria.
- `cloudinary_delete_asset`: Safely removes identified assets from the cloud storage.
- `cloudinary_get_asset_details`: Fetches usage statistics to verify if an asset is truly inactive.

---

## Related Solutions
- [../account-audit-agent-by-cloudflare/README.md](../account-audit-agent-by-cloudflare/README.md) - Automated security and configuration auditing for cloud environments.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain data quality and remove decay in CRM records.
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor and optimize the health of your automated operational workflows.
