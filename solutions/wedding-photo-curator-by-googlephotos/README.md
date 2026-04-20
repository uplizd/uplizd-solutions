# Wedding Photo Curator (Uplizd) - Automated organization and smart selection for wedding photography

## Summary
The Wedding Photo Curator by Uplizd is an intelligent AI workflow designed to streamline the post-production process for professional photographers. By leveraging the Composio Toolset to interface with Google Photos, this solution automatically categorizes, filters, and organizes high-volume wedding image galleries, ensuring that photographers can deliver curated, high-quality collections to their clients with significantly reduced manual effort.

---

## Demo
![Workflow diagram showing the Wedding Photo Curator processing images from Google Photos into curated albums](image.png)
**Alt text (SEO-ready):** Uplizd workflow for wedding photo curation, featuring automated Google Photos integration, AI-driven image sorting, and client-ready gallery organization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0ab41a6b-900b-55ba-b2d4-267e4f2b7a53)

---

## Category
- **Primary category:** Media Operations
- **Secondary tags:** google photos, image curation, photography workflow, ai automation, asset management, client delivery, composio
- This solution optimizes the digital asset management lifecycle for creative professionals by automating the selection and organization of large-scale event photography.

---

## Who is this for?
This workflow is designed for creative professionals and studio managers who need to maintain high standards of client delivery while minimizing time spent on repetitive administrative tasks.

- **Wedding Photographers**
    - Automate the initial culling process to focus on high-impact artistic shots.
- **Studio Managers**
    - Standardize the organization of client galleries to ensure consistent delivery timelines.
- **Content Editors**
    - Quickly identify and group specific moments like ceremonies or receptions for social media highlights.
- **Freelance Retouchers**
    - Receive pre-sorted and categorized batches of images, reducing the time required to locate specific assets.

---

## Features
- **Intelligent Image Culling**
  Uses AI to identify and remove blurry or duplicate shots, ensuring only the highest quality images remain.
- **Automated Album Categorization**
  Automatically sorts photos into logical folders such as "Ceremony," "Reception," and "Portraits" using metadata and visual recognition.
- **Google Photos Integration**
  Seamlessly connects with your Google Photos library via the Composio Toolset for real-time asset management.
- **Client-Ready Organization**
  Prepares structured folders that are ready for direct sharing or final retouching workflows.
- **Time-Saving Batch Processing**
  Handles thousands of images in minutes, allowing photographers to focus on creative editing rather than file management.

---

## Use Cases
**Event Highlight Creation**
- Automatically extract the top 50 "best of" shots from a 2,000-image wedding gallery.
- Group candid shots from the dance floor into a dedicated "Reception Highlights" folder.

**Client Delivery Preparation**
- Organize raw uploads into chronological sub-folders to simplify the client review process.
- Filter out test shots and accidental captures before sending the gallery link to the client.

**Portfolio Maintenance**
- Identify and tag high-quality portraits for potential inclusion in your professional portfolio.
- Archive outtakes and low-quality images to a separate folder to keep your primary workspace clean.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Wedding Photo Curator template from the solution library.
3. Connect your Google Photos account via the Composio integration settings.
4. Ensure nodes are correctly mapped and all API permissions are authorized.

### 2) Setup the Nodes
- **Chat Input**: Receives the link or ID of the Google Photos album to be processed.
- **Agent**: Analyzes image metadata and visual content to categorize files based on event segments.
- **Composio Toolset**: Executes file movement, renaming, and album creation within Google Photos.
- **Chat Output**: Provides a summary report of the curated album and confirms completion.

### 3) Run the Flow
Use the Playground to test your curation logic with the following prompts:
- `Curate the album 'Smith Wedding 2023' and move all blurry photos to an 'Archive' folder.`
- `Organize the 'Johnson Wedding' album into sub-folders for Ceremony, Reception, and Portraits.`
- `Extract the best 20 photos from the 'Miller Wedding' album and place them in a 'Highlights' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine for image classification.
- Use a model capable of high-level reasoning to distinguish between event segments.
- Instruction pattern: "Analyze the timestamp and visual content of each image."
- Instruction pattern: "Maintain a strict folder structure for client delivery."
- Instruction pattern: "Prioritize clear, well-lit photos for the 'Highlights' category."

### 2) Composio Toolset Node
- Requires a valid Google Photos API key.
- Ensure the connection scope includes `photoslibrary.appendonly` and `photoslibrary.sharing` for full automation capabilities.

### 3) Tool Availability
- **Album Management**: Create, list, and modify album structures.
- **Media Filtering**: Query image metadata and visual attributes.
- **File Operations**: Move, copy, and delete assets within the library.

---

## Related Solutions
- [../247-customer-support-assistant-by-ai-ml-api/README.md](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support ticketing and inquiry management.
- [../workshop-template-curator-by-miro/README.md](../workshop-template-curator-by-miro/README.md) - Intelligent organization of creative workshop assets.
- [../you-tube-content-distribution-agent-by-youtube/README.md](../you-tube-content-distribution-agent-by-youtube/README.md) - Automated distribution and management of video assets.
