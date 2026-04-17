# Social Media Content Manager (Uplizd) - Streamline photo curation and social media content distribution

## Summary
The Social Media Content Manager is an intelligent Uplizd workflow designed to bridge the gap between your personal photo library and your social media presence. By leveraging the Composio Toolset to interface with Google Photos, this solution automates the extraction, selection, and preparation of visual assets, ensuring marketing teams and creators maintain a consistent content pipeline without manual file management.

---

## Demo
![Social Media Content Manager workflow dashboard showing Google Photos integration and content extraction nodes](image.png)
**Alt text (SEO-ready):** Uplizd Social Media Content Manager workflow dashboard showing Google Photos integration and automated content extraction for social media marketing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/57941a38-0611-5422-8ff4-778d2462c72e)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** social media, google photos, content curation, asset management, automation, digital marketing, composio, ai workflow

This solution optimizes the marketing lifecycle by transforming raw photo storage into a structured, ready-to-publish content library.

---

## Who is this for?
This workflow is built for professionals who need to move visual assets from private storage to public-facing channels with speed and precision.

* **Social Media Manager**
    * Reduces the time spent manually browsing and exporting photos for daily posts.
* **Content Creator**
    * Ensures high-quality visual assets are identified and organized for multi-platform distribution.
* **Marketing Coordinator**
    * Maintains a consistent flow of visual content by automating the retrieval of approved media.
* **Brand Strategist**
    * Streamlines the asset pipeline, allowing for faster response times to trending visual topics.

---

## Features
- **Automated Asset Retrieval**
  Connects directly to Google Photos to pull images based on specific search criteria or date ranges.
- **Intelligent Content Filtering**
  Uses AI to identify the best-performing or most relevant images from your library for social media use.
- **Composio Toolset Integration**
  Seamlessly bridges the gap between cloud storage APIs and the Uplizd agentic workflow.
- **Real-time Processing**
  Reduces latency in content preparation by executing extraction and metadata tagging in a single pass.
- **Centralized Workflow Control**
  Provides a single source of truth for all social media visual assets, preventing file duplication and loss.

---

## Use Cases
**Content Calendar Preparation**
* Automatically extract photos from a specific event folder for upcoming weekly social media posts.
* Filter and organize images by date to ensure seasonal content is ready for scheduled campaigns.

**Brand Asset Management**
* Identify and export high-resolution images from Google Photos for use in brand-aligned marketing materials.
* Audit existing photo libraries to ensure only approved, high-quality visuals are accessible for social media distribution.

**Rapid Response Campaigns**
* Quickly pull recent photos from a live event to share real-time updates on social platforms.
* Curate visual responses to trending topics by searching through archived photo collections via the agent.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Social Media Content Manager template from the solution library.
3. Authenticate your Google Photos account within the Composio connection settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives your natural language request for specific photo categories or dates.
* **Agent**: Interprets the intent and orchestrates the search parameters for the Google Photos API.
* **Composio Toolset**: Executes the secure API calls to retrieve and prepare the requested image data.
* **Chat Output**: Delivers the curated list of image links or metadata back to the user for final review.

### 3) Run the Flow
Use the Playground to test your content retrieval:
* `Find all photos from the 'Summer Campaign' album and prepare them for social media.`
* `Extract the latest 5 photos from last week and generate a summary for Instagram.`
* `Search for landscape photos taken in July and provide the direct access links.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the bridge between user intent and API execution.
* Use a model capable of high-reasoning to interpret complex search queries.
* Instruct the agent to prioritize image quality and relevance based on the user's prompt.
* Ensure the agent is configured to handle empty search results gracefully by notifying the user.

### 2) Composio Toolset Node
* Provide a valid API key with read-only access to your Google Photos library.
* Define the connection scope to include `photoslibrary.readonly` to ensure secure and limited access.

### 3) Tool Availability
* **Photo Search**: Capability to query albums, dates, and media types.
* **Metadata Extraction**: Ability to pull file names, timestamps, and descriptions.
* **Asset Retrieval**: Secure generation of temporary access links for selected media.

---

## Related Solutions
* [you-tube-content-distribution-agent-by-youtube](../you-tube-content-distribution-agent-by-youtube/README.md) - Automate the distribution of video assets across social channels.
* [you-tube-content-performance-optimizer-by-youtube](../you-tube-content-performance-optimizer-by-youtube/README.md) - Analyze and improve the reach of your visual content.
* [you-tube-audience-research-agent-by-youtube](../you-tube-audience-research-agent-by-youtube/README.md) - Gather insights to inform your social media content strategy.
