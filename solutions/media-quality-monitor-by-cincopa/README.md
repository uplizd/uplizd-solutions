# Media Quality Monitor (Uplizd) - Automated asset integrity and recovery for digital media

## Summary
The Media Quality Monitor is an intelligent Uplizd workflow designed to automate the detection, validation, and remediation of corrupted or missing media assets within your digital library. By leveraging the Cincopa integration, this solution ensures your content remains accessible and high-performing, reducing manual audit time and preventing broken user experiences across your web properties.

---

## Demo
![Media Quality Monitor workflow showing automated asset validation and re-upload process](image.png)
**Alt text (SEO-ready):** Media Quality Monitor workflow for automated asset validation, corruption detection, and media re-upload using Uplizd and Cincopa.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b2bd10e2-2fe5-5d4c-aa21-1eb92de842d0)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** media management, cincopa, data hygiene, asset integrity, automated recovery, content delivery, composio, ai workflow.
This solution bridges the gap between raw media storage and live web performance by automating the maintenance of high-quality digital assets.

---

## Who is this for?
This solution is designed for teams managing high-volume media libraries who need to maintain consistent asset availability without manual oversight.

* **Digital Asset Managers**
    * Ensures all hosted media files are healthy and accessible to end-users.
* **Web Operations Specialists**
    * Automates the identification of broken links or corrupted files across landing pages.
* **Content Producers**
    * Reduces downtime for media assets by triggering instant re-uploads upon error detection.
* **Marketing Technologists**
    * Maintains brand consistency by ensuring high-quality, non-corrupted media is always served.

---

## Features
- **Automated Health Audits**
    Real-time scanning of media assets to identify corruption or missing file headers.
- **Intelligent Re-upload Logic**
    Automatically triggers a fresh upload process via the Cincopa API when an asset fails validation.
- **Composio-Powered Integration**
    Seamlessly connects the Uplizd agent to Cincopa’s management tools for secure file manipulation.
- **Error Logging & Reporting**
    Captures detailed logs of failed assets and successful recoveries for audit trails.
- **Proactive Notification**
    Alerts the team via the Chat Output node when an asset cannot be automatically recovered.

---

## Use Cases
**Asset Integrity Management**
* Scanning large media libraries for broken file references during scheduled maintenance.
* Verifying that all uploaded videos meet specific compression and format requirements.

**Automated Recovery Workflows**
* Triggering a re-upload of a corrupted image file directly from the source repository.
* Replacing missing media assets in web galleries without manual intervention.

**Operational Reporting**
* Generating a summary report of all media assets that required automated intervention.
* Monitoring the frequency of asset corruption to identify underlying storage issues.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Import the workflow into your workspace.
3. Connect your Cincopa API credentials to the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger command or scheduled audit request.
* **Agent**: Analyzes the media status and decides whether to trigger a repair.
* **Composio Toolset**: Executes the API calls to Cincopa for file validation and re-upload.
* **Chat Output**: Returns the status of the audit and any successful recovery actions.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Run a full audit on the 'Q3 Marketing Assets' folder and report any corrupted files.`
* `Check the status of all media in the 'Hero Banners' gallery and re-upload any that fail validation.`
* `List all assets that were successfully recovered during the last automated scan.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for media validation logic.
* Use a model capable of logical reasoning (e.g., GPT-4o or Claude 3.5).
* Instruction: "You are a media integrity expert. Your goal is to validate asset health via Cincopa tools and trigger re-uploads for any corrupted files."
* Instruction: "Always provide a clear summary of which files were checked, which were found corrupted, and which were successfully repaired."

### 2) Composio Toolset Node
* Provide your Cincopa API key within the Composio configuration.
* Set the connection scope to allow read/write access to your media galleries.

### 3) Tool Availability
* `cincopa_list_assets`: Fetch current media library contents.
* `cincopa_validate_file`: Check file integrity and metadata.
* `cincopa_upload_file`: Perform the re-upload of corrupted assets.

---

## Related Solutions
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure media assets meet accessibility standards.
* [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Manage and optimize video content distribution.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational status of your automated workflows.
