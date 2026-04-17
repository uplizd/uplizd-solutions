# Bulk Media Processor (Uplizd) - Automated image optimization and cloud storage management

## Summary
The Bulk Media Processor is an intelligent Uplizd workflow designed to automate high-volume image compression and storage tasks. By leveraging the TinyPNG API through the Composio Toolset, this solution enables teams to maintain website performance and storage efficiency without manual intervention. It serves as a single source of truth for media hygiene, ensuring that all assets are optimized for web delivery while maintaining high visual fidelity.

---

## Demo
![Bulk Media Processor workflow diagram showing image input, TinyPNG compression, and cloud storage output](image.png)
**Alt text (SEO-ready):** Bulk Media Processor Uplizd workflow for automated image compression, TinyPNG integration, and cloud storage synchronization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFAwS38jN9QAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAIklEQVR42mP8z8AARsB0wJgGjBoY1YBpDpgGgGkAmB4AAL2kC/3F1n+AAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/bdb8ed55-8405-5738-8790-8a7afd62dbce)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** media processing, tinypng, image optimization, data hygiene, automation, cloud storage, composio, ai workflow  
This solution streamlines digital asset management by automating the compression and organization of media files across your cloud infrastructure.

---

## Who is this for?
This solution is designed for teams managing large-scale digital assets who need to reduce manual overhead and improve site performance.

*   **Web Developers**
    *   Automate image optimization pipelines to ensure faster page load times and better Core Web Vitals.
*   **Content Managers**
    *   Maintain consistent image quality and file sizes across massive content libraries without manual resizing.
*   **Digital Marketers**
    *   Ensure all campaign assets are web-ready and stored in the correct cloud folders automatically.
*   **Operations Managers**
    *   Reduce cloud storage costs by implementing automated compression and cleanup protocols for media assets.

---

## Features
- **Automated Batch Compression**
  Processes hundreds of images in a single run, significantly reducing file sizes while preserving visual quality using the TinyPNG engine.
- **Intelligent Cloud Sync**
  Automatically routes processed images to designated cloud storage buckets, ensuring a clean and organized file structure.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely connect the Uplizd agent with your media storage and compression APIs.
- **Real-time Processing Logs**
  Provides detailed feedback on every image processed, including compression ratios and storage status, directly in the Chat Output.
- **Customizable Compression Thresholds**
  Allows users to define specific quality settings or file size limits to meet unique project requirements.

---

## Use Cases
**Website Performance Optimization**
*   Automatically compress high-resolution hero images before they are uploaded to the production server.
*   Batch process legacy media folders to reclaim storage space and improve site loading speeds.

**E-commerce Asset Management**
*   Standardize product image sizes and weights across multiple storefronts to ensure a consistent user experience.
*   Sync optimized product photos to your CDN or cloud storage provider immediately upon upload.

**Marketing Campaign Workflow**
*   Process bulk uploads of social media assets to ensure they meet platform-specific file size requirements.
*   Automate the transition of raw campaign photography into web-optimized assets for landing pages.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Bulk Media Processor to your workspace.
3. Connect your required API credentials for TinyPNG and your cloud storage provider.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the batch of image URLs or file paths for processing.
*   **Agent**: Orchestrates the logic, determining which images require compression and where they should be stored.
*   **Composio Toolset**: Executes the API calls to TinyPNG and your storage provider.
*   **Chat Output**: Confirms successful processing and provides a summary report of the batch.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Compress all images in the 'marketing-assets' folder and save them to the 'optimized-web' bucket.`
* `Check the current storage usage and optimize any images larger than 2MB.`
* `Process the list of image URLs provided in the attached file and confirm when finished.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, managing the sequence of compression and storage tasks.
*   Use a model capable of handling structured data and API orchestration.
*   Ensure the system instruction emphasizes accuracy in file path handling.
*   Maintain a professional, reporting-oriented tone for all output logs.

### 2) Composio Toolset Node
*   **API Key**: Ensure your TinyPNG and Cloud Storage API keys are active in the Composio dashboard.
*   **Connection Scope**: Grant the agent read/write access to the specific media folders intended for processing.

### 3) Tool Availability
*   **TinyPNG API**: For high-efficiency image compression.
*   **Cloud Storage Connector**: For file retrieval and upload operations.
*   **File System Utilities**: For path validation and batch management.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data for better targeting.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate CRM records.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex operational workflows.
