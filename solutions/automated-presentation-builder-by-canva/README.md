# Automated Presentation Builder (Uplizd) - Transform data and outlines into professional presentations instantly

## Summary
The Automated Presentation Builder by Uplizd streamlines the creation of high-impact slide decks by leveraging AI to convert raw data, meeting notes, or project outlines into structured, visually professional presentations. This workflow eliminates manual formatting time, ensuring consistent branding and narrative flow across all corporate communications, ultimately increasing pipeline velocity and operational efficiency.

---

## Demo
![Automated Presentation Builder workflow interface showing data input to slide generation](image.png)
**Alt text (SEO-ready):** Automated Presentation Builder workflow in Uplizd showing AI-driven slide deck generation, Canva integration, and data-to-presentation automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/bb16a035-3980-5c98-b7a5-06128e3e3800)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** canva, presentation, automation, content creation, ai workflow, composio, sales enablement, deck builder  
This solution bridges the gap between raw business data and visual storytelling by automating the design process within the Canva ecosystem.

---

## Who is this for?
This solution is designed for professionals who need to produce high-quality visual content at scale without sacrificing time or design integrity.

*   **Sales Executives**
    *   Generate personalized pitch decks for prospect meetings in seconds.
*   **Marketing Managers**
    *   Maintain brand consistency across all team-generated presentation materials.
*   **Operations Leads**
    *   Automate the transformation of quarterly performance reports into stakeholder-ready slides.
*   **Content Strategists**
    *   Rapidly prototype visual concepts based on research and data-driven insights.

---

## Features
- **Intelligent Content Mapping**
  Automatically parses text inputs and maps key points to professional slide layouts.
- **Canva Integration**
  Leverages the Composio Toolset to push generated content directly into Canva templates.
- **Real-time Data Sync**
  Pulls the latest metrics or CRM data to ensure presentation content is always accurate.
- **Dynamic Template Selection**
  Selects the optimal slide structure based on the intent of the presentation (e.g., sales pitch vs. internal update).
- **Automated Formatting**
  Applies consistent styling, fonts, and imagery to maintain professional design standards.

---

## Use Cases
**Sales Enablement**
*   Creating custom pitch decks for high-value accounts using CRM-sourced opportunity data.
*   Generating follow-up presentations that summarize meeting outcomes and next steps.

**Marketing & Reporting**
*   Converting monthly marketing performance metrics into automated executive summary decks.
*   Standardizing internal project status updates to ensure clear communication across departments.

**Content Production**
*   Rapidly building slide decks from long-form research documents or whitepapers.
*   Scaling the creation of educational materials or webinar slides from existing blog content.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Paste the solution JSON or connect via the provided repository link.
3. Authenticate your Canva account within the Composio Toolset node.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw data, outline, or prompt for the presentation.
*   **Agent**: Processes the input, structures the narrative, and defines slide content.
*   **Composio Toolset**: Executes the API calls to Canva to generate and format the slides.
*   **Chat Output**: Confirms the presentation creation and provides a link to the draft.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Create a 5-slide pitch deck for a new CRM integration based on the attached project summary.`
* `Generate a quarterly performance presentation using the data from the Q3 sales report.`
* `Build a professional slide deck for a product launch announcement using the provided feature list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative director, ensuring the tone and structure meet professional standards.
*   Use a high-reasoning model to ensure logical flow between slides.
*   Instruct the agent to prioritize concise bullet points over long-form text.
*   Maintain a consistent brand voice by providing a style guide in the system prompt.

### 2) Composio Toolset Node
*   Requires a valid Canva API key and appropriate scope permissions to create and edit designs.
*   Ensure the connection is active in the Composio dashboard before triggering the flow.

### 3) Tool Availability
*   **Canva Create Design**: Initialize new presentations from templates.
*   **Canva Add Element**: Insert images, charts, and text blocks into slides.
*   **Canva Export**: Finalize and share the presentation link.

---

## Related Solutions
* [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) — Automate the setup of collaborative workshop environments.
* [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Analyze and improve video content strategy.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather and report on account-level insights for sales teams.
