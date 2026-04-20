# Visual Meeting Documenter (Uplizd) - Transform meeting insights into structured Mural boards

## Summary
The Visual Meeting Documenter is an AI-powered workflow that automatically captures, synthesizes, and maps meeting discussions directly into Mural boards. By leveraging the Composio Toolset to interface with collaboration platforms, this solution eliminates manual documentation overhead, ensuring that brainstorming sessions, action items, and strategic decisions are instantly visualized for distributed teams to drive alignment and project velocity.

---

## Demo
![Visual Meeting Documenter workflow diagram showing Chat Input, AI Agent, Mural integration, and final board output](image.png)
**Alt text (SEO-ready):** Visual Meeting Documenter workflow diagram showing Chat Input, AI Agent, Mural integration, and final board output for Uplizd automation and real-time collaboration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/53958dda-0191-5263-b97b-21f09532a625)

---

## Category
**Primary category:** Operations
**Secondary tags:** mural, collaboration, meeting notes, visual documentation, ai workflow, composio, productivity, team alignment.
This solution bridges the gap between verbal communication and visual project management by automating the creation of structured meeting artifacts.

---

## Who is this for?
This workflow is designed for teams that rely on visual collaboration to turn abstract discussions into actionable project roadmaps.

*   **Project Managers**
    *   Automatically convert meeting transcripts into organized Kanban boards or project timelines.
*   **Design Leads**
    *   Capture design feedback and user requirements directly into visual brainstorming templates.
*   **Product Owners**
    *   Maintain a single source of truth by syncing stakeholder meeting outcomes with product roadmaps.
*   **Workshop Facilitators**
    *   Reduce post-session administrative work by auto-populating Mural boards with captured insights.

---

## Features
- **Automated Synthesis**
  The AI agent parses raw meeting transcripts to extract key themes, decisions, and action items.
- **Mural Integration**
  Utilizes the Composio Toolset to create, update, and organize sticky notes and shapes on your Mural boards.
- **Real-time Mapping**
  Instantly maps extracted data points to specific board coordinates or predefined template sections.
- **Action Item Tracking**
  Identifies owners and deadlines from meeting discussions and logs them as distinct visual tasks.
- **Template-Aware Processing**
  Recognizes specific meeting types (e.g., Retrospectives, Sprint Planning) to apply the appropriate visual structure.

---

## Use Cases
**Strategic Planning**
*   Mapping quarterly goals and OKRs directly from leadership strategy sessions to a visual roadmap.
*   Converting SWOT analysis discussions into categorized quadrants on a shared board.

**Sprint Retrospectives**
*   Grouping team feedback into "Start, Stop, Continue" columns automatically after a sprint review.
*   Visualizing team sentiment and blockers by mapping recurring themes to color-coded sticky notes.

**Client Discovery**
*   Documenting client requirements and pain points into a structured discovery canvas in real-time.
*   Creating visual project briefs that align client expectations with internal delivery milestones.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Mural account within the Composio connection settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the meeting transcript or summary notes from the user.
*   **Agent**: Processes the text, identifies key insights, and formats them for visual representation.
*   **Composio Toolset**: Executes the API calls to create and position elements on the target Mural board.
*   **Chat Output**: Confirms the successful creation of the visual documentation with a direct link to the board.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
*   `"Create a new Mural board from these meeting notes: [Paste Transcript] and organize them into a project roadmap."`
*   `"Add the following action items to the existing 'Q3 Planning' board: [List Items]."`
*   `"Synthesize this retrospective transcript into a 'Start, Stop, Continue' format on my team board."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a structured data extractor and visual mapper.
*   Instruction: Focus on identifying actionable items and thematic groupings.
*   Instruction: Maintain a neutral, professional tone when summarizing meeting discussions.
*   Instruction: Ensure all output adheres to the schema required by the Mural API integration.

### 2) Composio Toolset Node
*   **API Key**: Provide your Mural API key within the Composio configuration.
*   **Connection Scope**: Ensure the agent has 'Write' permissions for your target workspaces and boards.

### 3) Tool Availability
*   `mural_create_board`: Initializes new visual workspaces.
*   `mural_add_sticky_note`: Adds content to specific board coordinates.
*   `mural_update_element`: Modifies existing notes or shapes based on agent feedback.
*   `mural_list_templates`: Retrieves available board layouts for structured documentation.

---

## Related Solutions
*   [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automates the management and flow of interactive workshop sessions.
*   [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manages and deploys standardized templates across collaborative workspaces.
*   [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organizes and ranks tasks extracted from meeting logs and incident reports.
