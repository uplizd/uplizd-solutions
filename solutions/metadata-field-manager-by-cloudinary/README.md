# Metadata Field Manager (Uplizd) - Automate and standardize asset metadata tagging

## Summary
The Metadata Field Manager (Uplizd) is an intelligent automation workflow designed to streamline asset organization by dynamically managing custom metadata fields within Cloudinary. By leveraging AI to enforce naming conventions, categorize assets, and populate descriptive tags, this solution eliminates manual data entry, ensures cross-departmental searchability, and maintains high-quality digital asset hygiene at scale.

---

## Demo
![Metadata Field Manager workflow interface showing automated tagging and field population in Cloudinary](image.png)
**Alt text (SEO-ready):** Metadata Field Manager Uplizd workflow automating Cloudinary asset tagging and custom field synchronization for digital asset management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/metadata-field-manager-by-cloudinary)

---

## Category
**Primary category:** Data integration
**Secondary tags:** cloudinary, digital asset management, metadata, data hygiene, automation, composio, ai workflow, tagging.
This solution bridges the gap between raw asset uploads and structured data management by automating the enrichment of metadata fields.

---

## Who is this for?
This workflow is designed for teams managing large-scale media libraries who need to maintain consistency across their digital assets.

*   **Digital Asset Managers**
    *   Automate the enforcement of taxonomy standards across thousands of assets.
*   **Marketing Operations Leads**
    *   Ensure campaign assets are tagged correctly for rapid retrieval and reporting.
*   **Creative Directors**
    *   Reduce time spent on manual administrative tasks during the asset upload pipeline.
*   **Data Engineers**
    *   Maintain clean, searchable metadata schemas within Cloudinary via automated API triggers.

---

## Features
- **Automated Tagging**
    AI-driven analysis of asset content to generate relevant, searchable tags automatically.
- **Naming Convention Enforcement**
    Standardizes file naming and metadata field values to ensure uniformity across the library.
- **Custom Field Mapping**
    Seamlessly maps AI-extracted insights into specific custom metadata fields within Cloudinary.
- **Real-time Sync**
    Utilizes the Composio Toolset to push updates to Cloudinary immediately upon asset ingestion.
- **Bulk Metadata Cleanup**
    Processes existing assets to retroactively apply standardized metadata, reducing technical debt.

---

## Use Cases
**Asset Library Organization**
*   Automatically categorize new uploads based on visual content (e.g., product type, color, or season).
*   Populate "Campaign ID" fields based on folder structure or file naming patterns.

**Searchability Optimization**
*   Generate descriptive alt-text and SEO tags for assets to improve internal search performance.
*   Sync asset metadata with external CRM or PIM systems to ensure cross-platform data consistency.

**Compliance and Hygiene**
*   Identify and flag assets missing mandatory metadata fields for manual review.
*   Standardize date formats and copyright information across global asset repositories.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Metadata Field Manager template from the solution library.
3. Connect your Cloudinary account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event (e.g., new asset upload or manual request).
*   **Agent**: Analyzes the asset and determines the appropriate metadata values.
*   **Composio Toolset**: Executes the API calls to update Cloudinary custom fields.
*   **Chat Output**: Confirms the successful update or reports any errors in the tagging process.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Analyze the latest uploaded asset in the 'Summer_Campaign' folder and apply the 'Seasonal' tag.`
* `Update the 'Product_Category' metadata field for all assets uploaded in the last 24 hours.`
* `Check for missing metadata on the most recent 10 assets and populate the 'Creator' field based on the file owner.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that interprets asset data and maps it to your schema.
*   **Role:** Metadata Classification Specialist.
*   **Instruction Pattern:**
    *   Extract key visual features and context from the asset description.
    *   Map extracted features to the predefined Cloudinary metadata schema.
    *   Validate values against the organization's naming convention policy.

### 2) Composio Toolset Node
*   **API Key:** Provide your Cloudinary API credentials within the Composio connection manager.
*   **Connection Scope:** Ensure the agent has `write` permissions for the `metadata` and `tags` endpoints.

### 3) Tool Availability
*   `cloudinary_update_metadata`: Updates custom fields for specific asset IDs.
*   `cloudinary_add_tags`: Appends new tags to existing assets.
*   `cloudinary_search_assets`: Retrieves asset details for validation and analysis.

---

## Related Solutions
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate data decay cleanup and formatting.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multi-platform CRM environments.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage pipeline stages and stalled deal follow-ups.
