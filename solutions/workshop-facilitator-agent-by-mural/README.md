# Workshop Facilitator Agent (Uplizd) - Streamline design thinking and collaborative sessions on Mural

## Summary
The Workshop Facilitator Agent is an intelligent automation workflow designed to orchestrate design thinking sessions, team brainstorms, and collaborative workshops directly within Mural. By leveraging the Composio Toolset to interface with Mural’s API, this solution eliminates manual setup time, structures agenda items, and manages participant activities, ensuring that facilitators can focus on high-value team engagement rather than administrative overhead.

---

## Demo
![Workshop Facilitator Agent interface showing automated Mural board setup and agenda management](image.png)
**Alt text (SEO-ready):** Workshop Facilitator Agent for Mural, Uplizd AI workflow, automated design thinking session management, and collaborative board setup.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e77d67d6-e26e-5eea-b20f-519f0fd832b3)

---

## Category
**Primary category:** Operations  
**Secondary tags:** mural, design thinking, workshop automation, collaboration, team productivity, ai workflow, composio, project management.  
This solution bridges the gap between structured workshop planning and real-time execution, providing a seamless operational layer for remote and hybrid teams.

---

## Who is this for?
This solution is designed for professionals who manage complex collaborative sessions and need to maintain high engagement levels during workshops.

*   **Design Leads**
    *   Automate the creation of complex workshop templates and ideation canvases.
*   **Product Managers**
    *   Standardize feedback collection and prioritization exercises across cross-functional teams.
*   **Agile Coaches**
    *   Ensure consistent retrospective formats and action item tracking in every session.
*   **Operations Managers**
    *   Reduce the time spent on manual board configuration and participant onboarding.

---

## Features
- **Automated Board Creation**
  Instantly provision new Mural boards from pre-defined templates to ensure session readiness.
- **Dynamic Agenda Management**
  Programmatically add, update, and sequence agenda items and time-boxed activities.
- **Participant Activity Tracking**
  Monitor engagement levels and capture contributions directly from the board into your workflow.
- **Real-time Tool Integration**
  Utilize the Composio Toolset to trigger Mural actions based on inputs from other enterprise tools.
- **Structured Output Generation**
  Automatically synthesize workshop outcomes into summaries or action items for post-session follow-up.

---

## Use Cases
**Session Preparation**
*   Automatically generate a new Mural board based on a specific project template when a meeting is scheduled.
*   Pre-populate boards with participant names and assigned breakout areas before the session begins.

**During the Workshop**
*   Trigger real-time updates to the board layout based on live feedback or changing session requirements.
*   Automate the creation of sticky notes or cards based on verbal input provided during the brainstorming phase.

**Post-Workshop Synthesis**
*   Export all sticky note content to a structured document or CRM record once the session concludes.
*   Identify and flag action items generated during the session for immediate assignment in project management tools.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Workshop Facilitator Agent template provided in the repository.
3. Connect your Mural API credentials within the integration settings.
4. Ensure nodes are correctly mapped to your specific Mural workspace and board IDs.

### 2) Setup the Nodes
*   **Chat Input**: Receives the workshop objective or agenda details from the facilitator.
*   **Agent**: Processes the request and determines the necessary Mural board operations.
*   **Composio Toolset**: Executes the API calls to create, update, or retrieve data from Mural.
*   **Chat Output**: Confirms the action taken and provides a link to the updated board.

### 3) Run the Flow
Use the Playground to test your agent with prompts like:
* `Create a new design thinking board using the 'Sprint Retrospective' template.`
* `Add an agenda item for 'User Journey Mapping' at 10:00 AM on the current board.`
* `Summarize all sticky notes from the 'Ideation' section and send them to my email.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for all board interactions.
* Use a model capable of structured JSON output for reliable API calls.
* Set the system prompt to prioritize clarity and adherence to Mural's board structure.
* Ensure the agent has access to the latest workshop template IDs.

### 2) Composio Toolset Node
* Requires a valid Mural API Key with read/write permissions for your workspace.
* Connection scope should include `boards:read`, `boards:write`, and `content:manage`.

### 3) Tool Availability
* `mural_create_board`: Provision new canvases.
* `mural_add_sticky_note`: Add content dynamically.
* `mural_get_board_content`: Retrieve data for synthesis.
* `mural_update_agenda`: Modify session timing and flow.

---

## Related Solutions
* [Workshop Template Curator (Miro)](../workshop-template-curator-by-miro/README.md) — Manage and organize collaborative templates in Miro.
* [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline operational workflows for field services.
* [Account Research Agent (OnePage)](../account-research-agent-by-onepage/README.md) — Automate account intelligence gathering for sales teams.
