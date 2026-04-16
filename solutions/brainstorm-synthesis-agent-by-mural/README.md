# Brainstorm Synthesis Agent (Uplizd) - Automate idea clustering and actionable concept generation

## Summary
The Brainstorm Synthesis Agent leverages AI to ingest raw brainstorming data, automatically clustering disparate ideas into coherent themes and prioritizing them for execution. By integrating directly with collaborative platforms like Mural, this workflow eliminates manual synthesis time, providing teams with a single source of truth for project ideation and accelerating the transition from raw brainstorming to concrete project roadmaps.

---

## Demo
![Brainstorm Synthesis Agent workflow showing idea clustering and prioritization in Mural](../image.png)
**Alt text (SEO-ready):** Brainstorm Synthesis Agent by Uplizd for automated idea clustering, concept prioritization, and Mural workflow integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/91e87771-7e3b-51b3-a075-a49dc8dec843)

---

## Category
**Primary category:** Operations
**Secondary tags:** brainstorming, mural, synthesis, ai workflow, project management, ideation, productivity, composio
This solution streamlines the post-brainstorming phase by transforming unstructured input into structured, actionable project data.

---

## Who is this for?
This agent is designed for teams looking to maximize the output of their collaborative sessions and reduce administrative overhead.

*   **Design Leads**
    *   Quickly identify high-impact design concepts from messy whiteboard sessions.
*   **Product Managers**
    *   Synthesize user feedback and feature ideas into prioritized product backlog items.
*   **Workshop Facilitators**
    *   Automate the post-session documentation process to provide stakeholders with immediate summaries.
*   **Operations Managers**
    *   Ensure that every brainstorming session results in trackable, assigned action items.

---

## Features
- **Automated Idea Clustering**
  Uses advanced LLM logic to group similar sticky notes and ideas based on semantic meaning.
- **Priority Scoring**
  Applies custom criteria to rank ideas based on feasibility, impact, and alignment with project goals.
- **Mural Integration**
  Directly reads from and writes to Mural boards via the Composio Toolset to maintain context.
- **Actionable Summary Generation**
  Converts raw brainstorming output into formatted reports ready for project management tools.
- **Real-time Synthesis**
  Processes large volumes of data instantly, allowing teams to move from ideation to planning in minutes.

---

## Use Cases
**Post-Workshop Analysis**
*   Consolidate hundreds of sticky notes from a design thinking session into 5–10 core themes.
*   Generate a summary document of key takeaways for executive stakeholders.

**Product Roadmap Planning**
*   Extract feature requests from customer discovery brainstorming boards.
*   Map identified ideas to existing product development initiatives.

**Strategic Alignment**
*   Filter out duplicate or low-value ideas from team brainstorming sessions.
*   Categorize ideas by department or project phase to streamline resource allocation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided JSON configuration file for the Brainstorm Synthesis Agent.
3. Connect your Mural account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the link or raw text data from your brainstorming session.
*   **Agent**: Analyzes the input, clusters themes, and applies prioritization logic.
*   **Composio Toolset**: Executes API calls to fetch board data and push synthesized results back to Mural.
*   **Chat Output**: Delivers the final summary and categorized list to the user.

### 3) Run the Flow
Use the Playground to test your synthesis logic with these prompts:
* `Synthesize the ideas from this Mural board link into three primary themes.`
* `Prioritize the extracted ideas based on high impact and low effort.`
* `Create a summary report of the brainstorming session and post it as a note on the board.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a strategic facilitator, focusing on pattern recognition and objective prioritization.
*   Maintain a neutral, analytical tone when clustering ideas.
*   Prioritize ideas that align with the provided project goal or objective.
*   Ensure all synthesized output is formatted as a structured list with clear headers.

### 2) Composio Toolset Node
Requires a valid Mural API key and appropriate workspace permissions to read board content and create new elements.

### 3) Tool Availability
*   **Board Reader**: Fetches text and metadata from specific Mural boards.
*   **Content Writer**: Creates new sticky notes or summary boxes on the board.
*   **Data Formatter**: Converts raw text into structured JSON for downstream reporting.

---

## Related Solutions
* [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automates the end-to-end management of collaborative workshop sessions.
* [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manages and deploys standardized templates for team brainstorming.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Ranks and assigns tasks derived from meeting and brainstorming outputs.
