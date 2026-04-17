# Smart Metadata Compressor (Uplizd) - Automated image optimization with metadata preservation

## Summary
The Smart Metadata Compressor (Uplizd) is an intelligent AI workflow designed to automate image compression while ensuring critical EXIF and IPTC metadata remains intact. By leveraging the Composio Toolset and TinyPNG integration, this solution provides a seamless pipeline for content creators, photographers, and digital asset managers to reduce file sizes without sacrificing the integrity of essential image data, ensuring high-performance web delivery and organized asset hygiene.

---

## Demo
![Smart Metadata Compressor workflow interface showing image upload, compression node, and metadata preservation logic](image.png)
**Alt text (SEO-ready):** Smart Metadata Compressor Uplizd workflow, automated image optimization, metadata preservation, and Composio integration for digital asset management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0d325cc1-c4dd-57fc-bbd5-1d571e0a3a1c)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** image optimization, tinypng, metadata, data hygiene, asset management, composio, automation, workflow
- This solution bridges the gap between high-performance web optimization and the need for rigorous data retention in professional media workflows.

---

## Who is this for?
This workflow is built for professionals who manage large volumes of visual assets and require a balance between site speed and data traceability.

- **Digital Asset Managers**
    - Automate the compression of thousands of assets while maintaining compliance with internal metadata standards.
- **Web Developers**
    - Improve page load speeds by integrating automated, metadata-aware compression into the content deployment pipeline.
- **Professional Photographers**
    - Protect copyright and camera setting information during the delivery of client-ready, web-optimized images.
- **Marketing Operations Specialists**
    - Ensure that marketing collateral is lightweight for email and social campaigns without losing tracking or campaign-specific metadata.

---

## Features
- **Intelligent Compression Engine**
    - Utilizes advanced algorithms to significantly reduce file size while maintaining visual fidelity for web use.
- **Metadata Preservation Logic**
    - Ensures that critical EXIF, IPTC, and XMP data fields are protected during the compression process.
- **Composio-Powered Integration**
    - Seamlessly connects with image processing tools via the Composio Toolset for reliable, real-time execution.
- **Automated Workflow Triggers**
    - Processes images immediately upon upload, reducing manual overhead in content management pipelines.
- **Batch Processing Capability**
    - Handles multiple image files in a single execution, ensuring consistent optimization across entire project folders.

---

## Use Cases
**Web Performance Optimization**
- Automatically compress hero images and product thumbnails to improve Core Web Vitals.
- Strip unnecessary data while keeping essential color profiles and copyright info for high-traffic landing pages.

**Digital Asset Hygiene**
- Standardize metadata across a library of assets to ensure searchability and proper attribution.
- Clean up bloated image files from legacy systems without losing the historical context stored in metadata tags.

**Content Pipeline Automation**
- Integrate image compression directly into the CMS upload workflow to prevent manual optimization steps.
- Sync compressed assets back to cloud storage providers with full metadata integrity for downstream marketing use.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Metadata Compressor template from the solution library.
3. Connect your preferred cloud storage or local upload trigger to the **Chat Input** node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the image file and user instructions for compression.
- **Agent**: Analyzes the image requirements and directs the compression engine.
- **Composio Toolset**: Executes the TinyPNG API calls to compress the file while preserving metadata.
- **Chat Output**: Returns the optimized image link and a summary of the metadata preserved.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Compress the uploaded image and ensure all EXIF data remains intact.`
- `Optimize this batch of product photos for web use while keeping copyright metadata.`
- `Process the image in the current folder and report the total size reduction achieved.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for the compression logic.
- Use a model capable of high-precision tool calling.
- Ensure the system prompt emphasizes metadata retention as a priority.
- Configure the agent to verify file types before sending them to the compression tool.

### 2) Composio Toolset Node
- Provide your TinyPNG API key within the Composio configuration.
- Set the connection scope to allow read/write access to your image storage directories.

### 3) Tool Availability
- **Image Compression API**: Handles the core reduction logic.
- **Metadata Extraction Tool**: Reads existing tags to verify preservation.
- **File System Connector**: Manages the retrieval and storage of processed assets.

---

## Related Solutions
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data while maintaining database hygiene.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Automate the cleanup of legacy CRM records and metadata.
- [../you-tube-content-performance-optimizer-by-youtube/README.md](../you-tube-content-performance-optimizer-by-youtube/README.md) - Optimize video metadata and performance metrics for YouTube.
