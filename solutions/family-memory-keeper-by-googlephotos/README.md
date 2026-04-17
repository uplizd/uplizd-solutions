# Family Memory Keeper (Uplizd) - Automated Monthly Photo Album and Memory Curation

## Summary
The Family Memory Keeper by Uplizd is an intelligent AI workflow designed to automate the organization of digital life by curating monthly photo albums and generating personalized memory summaries. By leveraging the Google Photos API, this solution helps families and individuals reclaim time spent manually sorting images, ensuring that precious moments are preserved, categorized, and summarized into a single source of truth for long-term digital hygiene.

---

## Demo
![Family Memory Keeper workflow showing automated photo curation and summary generation](image.png)
**Alt text (SEO-ready):** Uplizd Family Memory Keeper workflow for automated Google Photos album curation, memory summarization, and AI-driven digital media organization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d612ed57-62cc-52a1-93c5-f1dd973fdc75)

---

## Category
- **Primary category:** Personal Productivity
- **Secondary tags:** google photos, ai memory, photo curation, digital hygiene, automation, media management, composio, ai workflow
- This solution bridges the gap between massive photo libraries and meaningful storytelling by automating the categorization and summarization of your digital media.

---

## Who is this for?
This workflow is designed for anyone looking to transform chaotic photo galleries into organized, narrative-driven memories.

- **Busy Parents**
    - Automatically curate monthly highlights of children's growth without manual sorting.
- **Digital Archivists**
    - Maintain high-quality digital hygiene by organizing thousands of photos into structured, searchable albums.
- **Family Historians**
    - Generate descriptive summaries of family events that can be easily shared or preserved for future generations.
- **Content Creators**
    - Quickly identify and group visual assets from personal archives for social media or blog storytelling.

---

## Features
- **Automated Monthly Curation**
    - Uses AI to scan and group photos by date and context, creating monthly albums automatically.
- **Intelligent Memory Summarization**
    - Analyzes visual content to generate engaging, human-readable summaries of your family's monthly highlights.
- **Google Photos Integration**
    - Seamlessly connects with your existing Google Photos library via the Composio Toolset for secure, real-time access.
- **Smart Metadata Tagging**
    - Automatically applies descriptive tags to photos, making your library searchable and easy to navigate.
- **Customizable Narrative Styles**
    - Adjust the tone of your memory summaries, from sentimental and nostalgic to professional and concise.

---

## Use Cases
**Automated Family Archiving**
- Automatically move photos from a specific month into a dedicated "Monthly Highlights" album.
- Generate a "Year in Review" summary by aggregating monthly highlights into a single narrative document.

**Event-Based Memory Capture**
- Trigger an automatic album creation process immediately following a holiday or family vacation.
- Add descriptive captions to photos from a specific event based on visual analysis and location data.

**Digital Library Maintenance**
- Identify and flag duplicate or low-quality images to keep your storage usage optimized.
- Organize unsorted media into chronological folders to prevent digital clutter from accumulating.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the `Family Memory Keeper` template from the solution marketplace.
3. Connect your Google Photos account via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's request for a specific month or event to curate.
- **Agent**: Processes the request, identifies relevant photos, and drafts the memory summary.
- **Composio Toolset**: Executes API calls to Google Photos to create albums and fetch image metadata.
- **Chat Output**: Delivers the final link to the curated album and the generated memory summary.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Create a monthly album for July 2023 and write a summary of our beach trip.`
- `Find all photos from last weekend and organize them into a new album titled 'Weekend Fun'.`
- `Summarize the highlights from my 'Summer 2023' album and suggest a caption for the best photo.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your personal digital curator and storyteller.
- **Instruction Pattern**:
    - Focus on identifying key visual themes and emotional context within the photos.
    - Maintain a consistent, warm, and engaging tone for all generated summaries.
    - Prioritize accuracy when mapping dates and locations to specific photo sets.

### 2) Composio Toolset Node
- Requires a valid Google Photos API key configured within the Composio dashboard.
- Ensure the connection scope includes `photoslibrary.appendonly` and `photoslibrary.sharing` for full functionality.

### 3) Tool Availability
- **Album Management**: Create, list, and add media to Google Photos albums.
- **Media Search**: Query photos by date range, content type, or location metadata.
- **Metadata Extraction**: Retrieve and process EXIF data for accurate event timing.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support ticketing and response management.
- [you-tube-content-performance-optimizer-by-youtube](../you-tube-content-performance-optimizer-by-youtube/README.md) - AI-driven insights for optimizing video content distribution.
- [account-research-assistant-by-zoominfo](../account-research-assistant-by-zoominfo/README.md) - Automated research and intelligence gathering for sales accounts.
