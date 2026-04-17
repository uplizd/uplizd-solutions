# Design Feedback Orchestrator (Uplizd) - Streamline design review cycles and consolidate stakeholder feedback

## Summary
The Design Feedback Orchestrator is an intelligent Uplizd AI workflow designed to centralize, categorize, and route design feedback from multiple stakeholders directly into your design environment. By automating the intake and organization of comments, this solution eliminates manual tracking, reduces communication silos, and accelerates design iteration velocity, ensuring a single source of truth for all creative revisions.

---

## Demo
![Design Feedback Orchestrator workflow showing automated feedback routing from stakeholders to Figma via Composio](image.png)
**Alt text (SEO-ready):** Design Feedback Orchestrator workflow showing automated feedback routing from stakeholders to Figma via Composio, Uplizd AI automation, and design operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/22d524db-4683-53a0-98f6-4050b666daf9)

---

## Category
- **Primary category:** Design Operations
- **Secondary tags:** figma, design, feedback, workflow automation, stakeholder management, product design, composio, ai workflow
- This solution bridges the gap between stakeholder input and design execution, providing a structured pipeline for creative feedback management.

---

## Who is this for?
This solution is built for teams looking to eliminate feedback fragmentation and improve design quality through structured communication.

- **Product Designers**
    - Automatically sync stakeholder comments into Figma frames to maintain context and reduce manual copy-pasting.
- **Design Managers**
    - Gain visibility into the status of design revisions and ensure all feedback is addressed before final handoff.
- **Product Managers**
    - Provide clear, actionable feedback directly within the design tool, ensuring alignment between product requirements and visual output.
- **Creative Leads**
    - Standardize the feedback collection process across cross-functional teams to maintain brand consistency and design hygiene.

---

## Features
- **Automated Feedback Intake**
  Centralize comments from Slack, email, or project management tools directly into the relevant design project.
- **Intelligent Context Mapping**
  Use AI to associate feedback with specific design elements, artboards, or components within Figma.
- **Composio-Powered Integration**
  Leverage the Composio Toolset to securely authenticate and interact with your design software APIs in real-time.
- **Actionable Task Generation**
  Automatically convert high-level feedback into actionable design tasks or Jira tickets for the development team.
- **Revision Tracking**
  Maintain a clear history of design iterations and stakeholder approvals to prevent scope creep and missed requirements.

---

## Use Cases
**Design Review Cycles**
- Automatically route feedback from client meetings into the active design file to ensure no request is overlooked.
- Group similar feedback items into "Revision Sprints" to optimize the designer's workflow and focus time.

**Stakeholder Collaboration**
- Enable non-designers to provide feedback in plain language that the AI translates into precise design instructions.
- Notify stakeholders automatically when their requested changes have been implemented and are ready for review.

**Design Quality Assurance**
- Flag design feedback that conflicts with established design system guidelines to maintain visual consistency.
- Generate summary reports of all feedback received during a project phase to facilitate final stakeholder sign-off.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the Design Feedback Orchestrator flow.
3. Connect your Figma account and any relevant communication channels (Slack/Email) via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw feedback text or screenshots from stakeholders.
- **Agent**: Processes feedback, identifies the target design element, and formats the instruction.
- **Composio Toolset**: Executes the API calls to update comments or tasks in your design platform.
- **Chat Output**: Confirms the successful routing and logging of the feedback to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Route the feedback "The button needs to be more prominent" to the login screen design.`
- `Summarize all pending feedback for the mobile navigation component.`
- `Create a task in Jira based on the latest feedback regarding the hero section color palette.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent bridge, interpreting stakeholder intent and mapping it to technical design actions.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate intent classification.
- Instruction: "Extract the design element, the requested change, and the urgency level from the user input."
- Instruction: "Map the request to the correct Figma file ID and frame name using the available tools."

### 2) Composio Toolset Node
- Provide your Figma API key and ensure the connection scope includes read/write access to project files.
- Configure the toolset to allow the agent to fetch file structures and post comments/tasks.

### 3) Tool Availability
- **Figma API**: For retrieving file metadata and posting design comments.
- **Jira/Asana API**: For converting feedback into tracked development tasks.
- **Notification Service**: For alerting designers and stakeholders of status updates.

---

## Related Solutions
- [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) - Automate accessibility compliance checks within your design files.
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manage and deploy collaborative workshop templates for design teams.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose workflow orchestration for cross-functional project management.
