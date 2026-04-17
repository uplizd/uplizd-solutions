# Design Sprint Facilitator (Uplizd) - Automated board setup and session management

## Summary
The Design Sprint Facilitator is an intelligent Uplizd workflow that automates the orchestration of design sprints by streamlining board creation, participant management, and session documentation. By integrating directly with Miro, this solution eliminates manual setup overhead, ensuring that design teams can focus on ideation and prototyping rather than administrative logistics, ultimately increasing team velocity and session productivity.

---

## Demo
![Design Sprint Facilitator workflow showing Miro board automation and session management nodes](image.png)
**Alt text (SEO-ready):** Design Sprint Facilitator Uplizd workflow, Miro board automation, design session management, and AI-driven team collaboration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/50195cbb-f01a-58bd-8f12-16a81292a403)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** miro, design sprint, workshop, collaboration, automation, productivity, ai workflow, composio
- This solution bridges the gap between creative planning and execution by automating the technical setup of collaborative design environments.

---

## Who is this for?
This solution is designed for teams looking to standardize their creative processes and reduce the manual effort required to launch high-impact design workshops.

- **Design Leads**
    - Automate the creation of standardized workshop templates to ensure consistency across all design sprints.
- **Product Managers**
    - Quickly provision collaborative workspaces to capture user feedback and feature requirements in real-time.
- **UX Researchers**
    - Streamline the organization of session artifacts and participant inputs into a centralized, actionable format.
- **Operations Managers**
    - Reduce administrative friction by automating the lifecycle of design sessions from board setup to final documentation.

---

## Features
- **Automated Board Provisioning**
    - Instantly generate new Miro boards from predefined templates to ensure every sprint starts with the correct structure.
- **Session Participant Management**
    - Automatically invite stakeholders and manage access permissions for seamless collaboration during live sessions.
- **Real-time Artifact Capture**
    - Use the Composio Toolset to sync sticky notes, sketches, and comments directly into your project management system.
- **Intelligent Session Summarization**
    - Leverage the Agent node to synthesize complex design discussions into concise summaries and actionable next steps.
- **Workflow Integration**
    - Connect design outputs with broader product roadmaps, ensuring that sprint outcomes are immediately visible to cross-functional teams.

---

## Use Cases
**Workshop Preparation**
- Automatically clone a master design sprint template board for new project kick-offs.
- Pre-populate boards with participant lists and agenda items based on calendar events.

**Session Documentation**
- Export finalized design concepts and user journey maps into documentation tools after the session ends.
- Categorize and tag feedback collected during brainstorming phases for easier post-sprint analysis.

**Cross-Functional Alignment**
- Sync high-priority design decisions directly to Jira or Slack to keep non-design stakeholders informed.
- Create automated follow-up tasks based on unresolved action items identified during the sprint.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Design Sprint Facilitator JSON template provided in the solution repository.
3. Connect your Miro account via the Composio Toolset node to enable board manipulation.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the sprint name, duration, and participant list from the user.
- **Agent**: Processes the request and determines the necessary Miro API calls to execute the setup.
- **Composio Toolset**: Executes the creation of boards, invites users, and manages board elements.
- **Chat Output**: Confirms the successful creation of the board and provides the direct access link to the user.

### 3) Run the Flow
Use the Playground to test your setup with these prompts:
- `Create a new design sprint board titled "Q3 Mobile App Redesign" using the "Standard Ideation" template.`
- `Invite the product team to the "Q3 Mobile App Redesign" board and set their permissions to editor.`
- `Summarize the key takeaways from the "Q3 Mobile App Redesign" board and post them to the project Slack channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for all design sprint logistics.
- Use a high-reasoning model (e.g., GPT-4o) to ensure accurate interpretation of complex workshop requirements.
- Instruct the agent to prioritize board security and template consistency.
- Configure the agent to verify board existence before attempting to add content.

### 2) Composio Toolset Node
- Provide your Miro API key within the Composio Toolset configuration.
- Set the connection scope to include `boards:read`, `boards:write`, and `members:read` to ensure full automation capability.

### 3) Tool Availability
- **Board Management**: Create, delete, and duplicate boards.
- **Content Manipulation**: Add sticky notes, shapes, and frames to existing boards.
- **User Management**: Invite participants and manage team-level permissions.
- **Export Capabilities**: Extract board metadata and content for external reporting.

---

## Related Solutions
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Automate the selection and deployment of workshop templates.
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Manage collaborative sessions specifically within Mural environments.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Gather intelligence to inform design sprint participant lists.
