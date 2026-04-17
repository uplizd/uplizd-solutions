# Dynamic Scheduling Assistant (Uplizd) - Automate custom meeting link generation and calendar management

## Summary
The Dynamic Scheduling Assistant is an intelligent Uplizd workflow that automates the creation of personalized scheduling links based on specific meeting requirements. By integrating directly with Calendly, this solution eliminates manual calendar coordination, reduces scheduling friction, and ensures that meeting parameters—such as duration, buffer times, and availability—are dynamically configured for every interaction.

---

## Demo
![Dynamic Scheduling Assistant workflow interface showing automated link generation via Calendly integration](image.png)
**Alt text (SEO-ready):** Dynamic Scheduling Assistant workflow for automated Calendly link generation, Uplizd AI scheduling automation, and meeting management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/137041fb-7fb4-5811-b09f-4c11deadc7df)

---

## Category
**Primary category:** Operations
**Secondary tags:** calendly, scheduling, automation, calendar management, meeting operations, sales operations, composio, ai workflow.

This solution streamlines appointment setting by bridging the gap between conversational AI and calendar availability management.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meeting cadences and require automated, error-free scheduling.

*   **Sales Representatives**
    *   Instantly generate unique booking links for prospects during live conversations to maintain momentum.
*   **Customer Success Managers**
    *   Automate the scheduling of recurring check-ins and onboarding sessions without manual calendar cross-referencing.
*   **Executive Assistants**
    *   Reduce administrative overhead by deploying intelligent agents to handle complex scheduling requests across multiple time zones.
*   **Recruiters**
    *   Seamlessly coordinate interview slots by generating tailored scheduling links based on candidate availability and role requirements.

---

## Features
- **Dynamic Link Generation**
  Creates unique, context-aware Calendly scheduling links on-the-fly based on the specific meeting type or duration requested.
- **Intelligent Availability Mapping**
  Leverages the Composio Toolset to query real-time calendar availability, ensuring links only offer viable time slots.
- **Automated Buffer Management**
  Automatically applies pre-configured buffer times to meetings, preventing back-to-back scheduling conflicts.
- **Multi-Platform Integration**
  Connects seamlessly with Calendly via Composio, allowing the agent to perform actions directly within your scheduling ecosystem.
- **Conversational Scheduling**
  Allows users to trigger scheduling actions using natural language prompts, removing the need for manual dashboard navigation.

---

## Use Cases
**Sales Pipeline Acceleration**
*   Generate a 15-minute discovery call link immediately after a successful lead qualification chat.
*   Create custom demo links for high-priority opportunities with specific time-zone constraints.

**Customer Support & Success**
*   Automate the booking of follow-up support sessions based on ticket severity and agent availability.
*   Sync recurring account review meetings directly to the customer's calendar via generated booking links.

**Operational Efficiency**
*   Standardize meeting durations across the team by enforcing scheduling rules through the AI agent.
*   Reduce "scheduling tag" by providing instant booking options during initial outreach or follow-up communications.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the solution JSON file to initialize the node structure.
3. Connect your Calendly account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the user's scheduling request (e.g., "Schedule a 30-min demo with John").
*   **Agent**: Processes the intent and determines the necessary parameters for the scheduling link.
*   **Composio Toolset**: Executes the API calls to Calendly to generate or retrieve the booking link.
*   **Chat Output**: Delivers the finalized scheduling link back to the user for immediate sharing.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
*   `"Generate a 30-minute scheduling link for a discovery call with a new lead."`
*   `"Create a link for a 60-minute technical deep-dive meeting for next Tuesday."`
*   `"I need a scheduling link for a quick 15-minute sync with the client."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator, interpreting scheduling intent and mapping it to tool parameters.
*   Maintain a professional, helpful tone for all scheduling interactions.
*   Always confirm the duration and meeting type before triggering the link generation tool.
*   If availability is restricted, instruct the agent to offer alternative time windows or escalate to manual scheduling.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Calendly API key is active within the Composio dashboard.
*   **Connection Scope**: Grant the agent permission to read availability and create event types.

### 3) Tool Availability
*   `calendly_create_link`: Generates a unique booking URL based on specified parameters.
*   `calendly_get_availability`: Checks current calendar slots to ensure the agent proposes realistic times.
*   `calendly_list_event_types`: Retrieves existing meeting templates to match the user's request.

---

## Related Solutions
*   [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Automate prospect intelligence gathering.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage sales stages and follow-up cadences.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your CRM and scheduling data in perfect alignment.
