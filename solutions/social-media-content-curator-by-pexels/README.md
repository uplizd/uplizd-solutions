# Social Media Content Curator (Uplizd) - Automated visual asset discovery and scheduling

## Summary
The Social Media Content Curator is an intelligent Uplizd workflow that automates the discovery, selection, and organization of high-quality visual assets from Pexels for your social media campaigns. By integrating real-time search with AI-driven curation, this solution eliminates manual asset hunting, ensuring your content pipeline remains stocked with relevant, high-resolution media that aligns with your brand’s visual identity and posting schedule.

---

## Demo
![Social Media Content Curator workflow dashboard showing Pexels integration and asset selection nodes](image.png)
**Alt text (SEO-ready):** Uplizd social media content curator workflow, automated Pexels image search, AI-powered content scheduling, and marketing asset management integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8d986894-9a3f-5f70-9f9b-0636f0a18133)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** social media, content curation, pexels, digital assets, marketing automation, composio, ai workflow, visual content.
This solution streamlines the creative workflow by bridging the gap between raw visual stock and curated social media content strategy.

---

## Who is this for?
This solution is designed for marketing teams and creative professionals looking to scale their visual content output without increasing manual labor.

* **Social Media Manager**
    * Reduces time spent searching for high-quality stock photography for daily posts.
* **Content Strategist**
    * Ensures visual assets consistently match campaign themes and brand guidelines.
* **Digital Marketing Specialist**
    * Accelerates the production pipeline by automating the retrieval of relevant visual media.
* **Creative Director**
    * Maintains a high standard of visual quality across all social channels through automated filtering.

---

## Features
- **Automated Pexels Discovery**
  Leverages the Composio Toolset to query Pexels in real-time based on specific campaign keywords and aesthetic requirements.
- **AI-Driven Asset Filtering**
  The Agent node evaluates search results to select the most relevant images, filtering out low-quality or off-brand visuals.
- **Seamless Integration Workflow**
  Connects directly to your content management stack, allowing for instant hand-off of curated assets to scheduling tools.
- **Dynamic Prompting**
  Supports complex search parameters including orientation, color palettes, and specific subject matter to refine asset selection.
- **Real-Time Content Pipeline**
  Reduces the latency between content planning and asset acquisition, ensuring your team is always ready to publish.

---

## Use Cases
**Campaign Asset Preparation**
* Automatically sourcing a library of images for a month-long product launch campaign.
* Filtering search results by specific color codes to match brand-approved visual styles.

**Social Media Trend Response**
* Rapidly finding and curating high-resolution images to match trending topics or viral hashtags.
* Batch-processing visual assets for multi-platform distribution across Instagram, LinkedIn, and Twitter.

**Brand Consistency Management**
* Ensuring all sourced images meet specific resolution and aspect ratio requirements for professional social media layouts.
* Curating a recurring "weekly inspiration" feed by automating searches for niche industry topics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Pexels API credentials within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your campaign theme or visual keywords.
* **Agent**: Processes the request and instructs the toolset on what visual criteria to prioritize.
* **Composio Toolset**: Executes the Pexels API search and retrieves metadata for relevant images.
* **Chat Output**: Displays the curated list of image URLs and descriptions for your review.

### 3) Run the Flow
Open the Playground and try these prompts:
* `Find 5 high-resolution images of modern office spaces with a minimalist aesthetic for a LinkedIn post.`
* `Search for vibrant, outdoor summer lifestyle photography suitable for an Instagram campaign.`
* `Curate a set of professional tech-focused images that feature blue and white color schemes.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative director, interpreting your marketing needs and translating them into precise search queries.
* Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Set the system prompt to prioritize high-resolution and visually diverse results.
* Ensure the agent is instructed to provide image links and brief descriptions for each selected asset.

### 2) Composio Toolset Node
* Requires a valid Pexels API key configured within the Composio dashboard.
* Ensure the connection scope allows for read-only access to the Pexels library.

### 3) Tool Availability
* **Pexels Search**: Capability to query images by keyword, orientation, and size.
* **Metadata Extraction**: Ability to pull image source links, photographer credits, and resolution data.

---

## Related Solutions
* [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) - Automates the syndication and management of video assets across social channels.
* [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Analyzes and improves the reach of your visual content strategy.
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensures all curated visual assets meet accessibility standards with automated alt-text generation.
