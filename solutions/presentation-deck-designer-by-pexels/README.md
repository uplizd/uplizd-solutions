# Presentation Deck Designer (Uplizd) - Automated visual sourcing for professional pitch decks

## Summary
The Presentation Deck Designer is an intelligent Uplizd workflow that automates the sourcing of high-quality, professional imagery for business presentations and pitch decks. By integrating directly with visual asset libraries, this solution eliminates manual search time, ensuring your slides are consistently polished and aligned with your brand narrative, ultimately accelerating your presentation development pipeline.

---

## Demo
![Presentation Deck Designer workflow interface showing automated image search and asset integration](image.png)
**Alt text (SEO-ready):** Uplizd Presentation Deck Designer workflow for automated visual asset sourcing, pitch deck creation, and integration with Pexels for high-quality business imagery.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/60d7be7f-6997-5638-8c50-8b350c5d5a83)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** presentation, design, pexels, visual assets, pitch deck, content automation, composio, ai workflow.
This solution streamlines the visual design process by connecting AI-driven search capabilities directly to your presentation workflow.

---

## Who is this for?
This solution is designed for professionals who need to produce high-impact visual content rapidly without sacrificing quality.

*   **Sales Executives**
    *   Generate custom, professional pitch decks that resonate with specific client industries in minutes.
*   **Marketing Managers**
    *   Maintain consistent visual standards across all internal and external presentation assets.
*   **Startup Founders**
    *   Create compelling investor presentations with high-quality imagery sourced on-demand.
*   **Creative Agencies**
    *   Automate the initial asset-gathering phase of client presentation design to focus on high-level strategy.

---

## Features
- **Automated Visual Sourcing**
  Instantly query and retrieve high-resolution professional photography based on slide context.
- **Context-Aware Recommendations**
  The agent analyzes your slide topic to suggest the most relevant visual themes and styles.
- **Seamless Composio Integration**
  Leverages the Composio Toolset to securely connect with Pexels and other visual asset APIs.
- **Real-time Asset Retrieval**
  Fetch and preview images directly within the workflow, bypassing manual browser-based searches.
- **Workflow Pipeline Velocity**
  Drastically reduces the time spent on manual asset management, allowing for rapid iteration of presentation decks.

---

## Use Cases
**Pitch Deck Development**
*   Automatically source industry-specific imagery for investor presentations.
*   Update slide visuals based on real-time feedback during the design phase.

**Marketing Campaign Assets**
*   Quickly gather a library of relevant visuals for new product launch presentations.
*   Maintain a consistent visual language across multiple regional marketing decks.

**Sales Enablement**
*   Personalize sales collateral with imagery that reflects the prospect's specific business environment.
*   Streamline the creation of custom slide decks for high-stakes client meetings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Presentation Deck Designer template from the solution library.
3. Authenticate your Pexels account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your slide topic or visual requirements.
*   **Agent**: Processes the request and determines the optimal search parameters.
*   **Composio Toolset**: Executes the API call to fetch relevant imagery.
*   **Chat Output**: Delivers the selected image URLs and metadata to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
*   `Find professional images of modern office spaces for a tech startup pitch deck.`
*   `Search for high-quality photos of sustainable energy infrastructure for a quarterly report.`
*   `Get 5 images showing diverse team collaboration in a corporate setting.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a creative director, interpreting your design needs into effective search queries.
*   Focus on identifying the core visual theme of the user's prompt.
*   Translate abstract concepts into descriptive keywords for the Pexels API.
*   Filter results to ensure only high-resolution, professional-grade assets are returned.

### 2) Composio Toolset Node
Requires a valid Pexels API key to authorize the search and retrieval of visual assets. Ensure the connection scope allows for read-only access to the image library.

### 3) Tool Availability
*   **Search Engine**: Querying visual databases for relevant keywords.
*   **Image Metadata Parser**: Extracting URLs, photographer credits, and resolution data.
*   **Asset Categorization**: Organizing returned images by relevance to the slide topic.

---

## Related Solutions
*   [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) - Refine your written content for academic and professional standards.
*   [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Automate the selection and setup of collaborative workshop templates.
*   [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) - Manage and optimize your video asset distribution across platforms.
