# Client Gallery Curator (Uplizd) - Intelligent automated asset organization for professional photography

## Summary
The Client Gallery Curator by Uplizd automates the organization and preparation of professional photography assets, streamlining the transition from raw upload to client-ready presentation. By leveraging AI to categorize, select, and structure albums, this workflow eliminates manual sorting bottlenecks, ensuring photographers and creative agencies maintain high pipeline velocity and consistent brand hygiene across all client deliverables.

---

## Demo
![Workflow diagram showing the Client Gallery Curator processing raw image uploads into structured SmugMug albums](image.png)
**Alt text (SEO-ready):** Uplizd Client Gallery Curator workflow automating SmugMug album organization, asset categorization, and professional photography delivery.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ed041d55-9f37-5f2e-baca-7d37ae1b019d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** photography, smugmug, asset management, workflow automation, creative ops, data organization, composio, ai workflow
- This solution optimizes creative operations by automating the administrative overhead of gallery management and asset curation.

---

## Who is this for?
This solution is designed for creative professionals and studio managers who need to scale their delivery process without sacrificing quality.

- **Professional Photographers**
    - Automate the tedious task of sorting and uploading thousands of raw images into client-specific albums.
- **Creative Agency Leads**
    - Ensure consistent naming conventions and folder structures across all client projects for better brand alignment.
- **Studio Managers**
    - Reduce turnaround time from shoot to delivery, allowing the team to focus on editing rather than file management.
- **Digital Asset Librarians**
    - Maintain high data hygiene by ensuring every asset is correctly tagged and archived within the SmugMug ecosystem.

---

## Features
- **Intelligent Asset Categorization**
    - Automatically identifies and groups images based on metadata, content type, or shoot date to simplify album creation.
- **Automated SmugMug Integration**
    - Uses the Composio Toolset to push curated selections directly to SmugMug, bypassing manual upload interfaces.
- **Standardized Naming Protocols**
    - Enforces consistent file and album naming conventions to ensure professional presentation and easy searchability.
- **Real-time Sync & Updates**
    - Monitors incoming asset streams to trigger gallery updates instantly as new files become available.
- **Customizable Curation Logic**
    - Allows users to define specific rules for "best-of" selections, ensuring only high-quality assets reach the client gallery.

---

## Use Cases
**Client Delivery Automation**
- Automatically generate private client galleries immediately after a shoot is uploaded to the staging server.
- Notify clients via automated triggers once their specific gallery has been curated and published.

**Archive & Library Management**
- Sort archived shoots into categorized folders based on event type, location, or client name for long-term storage.
- Identify and flag duplicate or low-quality assets during the curation process to save storage space.

**Brand Consistency Enforcement**
- Apply uniform watermarking and metadata tags to all images before they are moved into a public-facing gallery.
- Sync project status updates between SmugMug and internal project management tools to keep stakeholders informed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Client Gallery Curator template from the solution library.
3. Connect your SmugMug account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives instructions regarding the shoot folder and curation criteria.
- **Agent**: Processes natural language commands to determine which images to curate and how to structure the gallery.
- **Composio Toolset**: Executes API calls to SmugMug to create albums and upload assets.
- **Chat Output**: Confirms successful gallery creation and provides a direct link to the client.

### 3) Run the Flow
Use the Playground to test your curation logic with these prompts:
- `Create a new SmugMug album named 'Wedding_Smith_2023' and upload all images from the 'Selected' folder.`
- `Sort all images in the 'Raw_Uploads' directory by date and move them into their respective monthly folders.`
- `Identify the top 20 images from the latest shoot and add them to the 'Highlights' gallery.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your gallery logic.
- Use a model capable of high-reasoning to interpret complex file-naming instructions.
- Recommended instruction pattern:
    - "Act as a professional photography assistant specialized in SmugMug gallery management."
    - "Prioritize accuracy in file sorting and strictly follow the provided naming convention."
    - "If an asset is ambiguous, flag it for human review rather than misplacing it."

### 2) Composio Toolset Node
- Provide your SmugMug API credentials within the Composio configuration.
- Set the connection scope to allow "Read/Write" access to your albums and media library.

### 3) Tool Availability
- **Album Management**: Create, rename, and delete gallery containers.
- **Asset Upload**: Transfer image files from local or cloud storage to specific albums.
- **Metadata Editor**: Update image descriptions, tags, and visibility settings.

---

## Related Solutions
- [../account-research-agent-by-onepage/README.md](../account-research-agent-by-onepage/README.md) - Automate account research and lead intelligence gathering.
- [../you-tube-content-distribution-agent-by-youtube/README.md](../you-tube-content-distribution-agent-by-youtube/README.md) - Streamline video asset distribution and platform management.
- [../accessibility-compliance-monitor-by-alttext-ai/README.md](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure image assets meet accessibility standards through automated alt-text generation.
