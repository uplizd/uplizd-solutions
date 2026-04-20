# Workshop Template Curator (Uplizd) - Automated board generation for collaborative sessions

## Summary
The Workshop Template Curator is an intelligent Uplizd workflow that instantly generates customized workshop boards in Miro based on specific learning objectives, participant profiles, and session constraints. By automating the structural setup of collaborative spaces, this solution eliminates manual board preparation, ensures consistency across team workshops, and significantly accelerates the time from planning to execution for facilitators and project managers.

---

## Demo
![Workshop Template Curator workflow showing automated Miro board generation based on user input](image.png)
**Alt text (SEO-ready):** Workshop Template Curator Uplizd workflow for automated Miro board generation, collaborative session planning, and team workshop automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3bbbb628-3fd7-5f58-abfb-9b63dfc0d619)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** miro, workshop, collaboration, productivity, automation, template, project management, ai workflow
- This solution streamlines operational workflows by bridging the gap between strategic planning and collaborative execution through intelligent template automation.

---

## Who is this for?
This solution is designed for professionals who manage collaborative environments and need to scale their workshop preparation efforts.

- **Facilitators**
  - Reduce manual setup time by instantly deploying standardized board structures for diverse meeting types.
- **Project Managers**
  - Ensure consistent project documentation and brainstorming frameworks across distributed remote teams.
- **Design Leads**
  - Maintain brand and process integrity by enforcing approved template layouts for all internal workshops.
- **Team Leads**
  - Accelerate team alignment by providing ready-to-use collaborative spaces tailored to specific project goals.

---

## Features
- **Dynamic Template Generation**
  - Automatically creates and populates Miro boards based on user-defined session objectives and participant counts.
- **Intelligent Content Mapping**
  - Maps workshop goals to specific Miro widgets, frames, and activity layouts using the Composio Toolset.
- **Customizable Participant Profiles**
  - Adjusts board complexity and tool availability based on the experience level and role of the workshop attendees.
- **Real-time Integration**
  - Leverages direct API connectivity to ensure boards are created and shared within your Miro workspace instantly.
- **Automated Hygiene Checks**
  - Cleans up redundant elements and organizes board assets to maintain a professional and clutter-free collaborative environment.

---

## Use Cases
**Strategic Planning Sessions**
- Generate comprehensive SWOT analysis templates tailored to specific industry market conditions.
- Create multi-phase roadmap boards that align team goals with quarterly project milestones.

**Design Thinking Workshops**
- Deploy empathy mapping and user journey templates based on provided customer persona data.
- Automate the creation of ideation frames for rapid brainstorming and cluster-based voting sessions.

**Team Retrospectives**
- Instantly set up "Start, Stop, Continue" boards customized for the specific team's recent sprint performance.
- Generate action-item tracking grids that automatically link to project management tools for follow-up.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Workshop Template Curator JSON configuration file.
3. Connect your Miro account via the Composio Toolset authentication prompt.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the workshop objectives, participant count, and desired board style.
- **Agent**: Processes the request to determine the optimal Miro template structure and layout.
- **Composio Toolset**: Executes the API calls to create the board and add specific widgets/frames.
- **Chat Output**: Confirms the successful creation of the board and provides a direct link to the Miro workspace.

### 3) Run the Flow
Use the Playground to test the workflow with prompts like:
- `Create a 2-hour design thinking workshop board for 10 participants focused on mobile app onboarding.`
- `Generate a SWOT analysis template for a Q3 marketing strategy session.`
- `Set up a retrospective board for a 5-person engineering team focusing on sprint velocity.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the architectural brain, translating natural language requirements into board layouts.
- Use a model capable of structured reasoning (e.g., GPT-4o).
- Instruction: "Act as a professional workshop facilitator. Analyze the user's input to select the most effective Miro template structure."
- Instruction: "Ensure all generated boards include clear instructions and designated areas for participant interaction."

### 2) Composio Toolset Node
- Requires a valid Miro API key with `boards:write` and `widgets:write` scopes.
- Ensure the connection is authorized within the Uplizd Integrations panel.

### 3) Tool Availability
- **Miro Create Board**: Initializes the workspace.
- **Miro Add Widget**: Places sticky notes, text blocks, and shapes.
- **Miro Add Frame**: Organizes the board into logical sections for different workshop activities.

---

## Related Solutions
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automates real-time facilitation and time-keeping for collaborative sessions.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manages stakeholder mapping and relationship health tracking.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlines cross-platform operational tasks and status updates.
