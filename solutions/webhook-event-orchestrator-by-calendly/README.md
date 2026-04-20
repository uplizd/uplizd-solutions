# Webhook Event Orchestrator (Uplizd) - Automate downstream actions from Calendly booking events

## Summary
The Webhook Event Orchestrator by Calendly is an intelligent automation workflow that captures real-time scheduling data to trigger downstream business processes. By leveraging the Composio Toolset, this solution eliminates manual data entry and ensures that every new booking, cancellation, or reschedule is immediately reflected across your CRM, communication platforms, and project management tools, providing a single source of truth for your team's pipeline velocity.

---

## Demo
![Webhook Event Orchestrator workflow diagram showing Calendly trigger connecting to an AI agent and Composio tools](image.png)
**Alt text (SEO-ready):** Webhook Event Orchestrator by Calendly workflow diagram showing Uplizd AI agent integration with Composio toolset for automated scheduling and CRM data synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f6d18c81-3954-5da9-8c8a-ade592a24f70)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** calendly, webhooks, automation, scheduling, crm, workflow, composio, ai agent
- This solution bridges the gap between scheduling events and operational execution by automating the hand-off from Calendly to your core business systems.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual administrative overhead following client interactions.

- **Sales Operations Manager**
    - Automates lead routing and CRM record creation immediately after a discovery call is booked.
- **Customer Success Lead**
    - Ensures onboarding workflows and support tickets are triggered the moment a client schedules a training session.
- **Executive Assistant**
    - Reduces scheduling friction by syncing meeting details and attendee information across disparate team calendars.
- **Revenue Operations (RevOps) Analyst**
    - Maintains data hygiene by ensuring meeting outcomes and attendee metadata are consistently logged in the central database.

---

## Features
- **Real-time Event Capture**
    - Instantly processes incoming Calendly webhooks to trigger automated workflows without polling delays.
- **Intelligent Data Parsing**
    - Uses AI to extract key attendee information, meeting types, and custom field data from raw webhook payloads.
- **Composio Toolset Integration**
    - Seamlessly connects with hundreds of third-party APIs to execute actions like updating CRM records or sending Slack notifications.
- **Customizable Logic Routing**
    - Enables conditional branching based on meeting type, attendee seniority, or specific custom form responses.
- **Automated Error Handling**
    - Provides robust logging and retry mechanisms to ensure no booking event is missed or improperly synced.

---

## Use Cases
**Lead Management**
- Automatically create a new lead or contact in your CRM when a prospect books a discovery call.
- Update lead status to "Scheduled" and assign the account owner based on the meeting type.

**Client Onboarding**
- Trigger an automated email sequence or project setup task when a client books a kickoff meeting.
- Sync meeting notes and attendee details into project management tools like Jira or Asana.

**Operational Efficiency**
- Send instant notifications to internal Slack or Microsoft Teams channels when high-value meetings are booked.
- Automatically log meeting attendance and duration in your data warehouse for performance reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Solution."
2. Paste the solution URL or upload the provided JSON configuration file.
3. Map your Calendly webhook endpoint to the trigger node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw JSON payload from the Calendly webhook.
- **Agent**: Analyzes the event payload and determines the necessary downstream actions.
- **Composio Toolset**: Executes the API calls to your integrated platforms (CRM, Slack, etc.).
- **Chat Output**: Confirms the successful execution of the workflow or logs any processing errors.

### 3) Run the Flow
Use the Playground to test your configuration with these example prompts:
- `Process the latest booking payload and update the contact record in Salesforce.`
- `If the meeting type is 'Demo', send a notification to the #sales-alerts channel.`
- `Extract attendee email and add them to the 'New Leads' list in HubSpot.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain, interpreting the webhook data to execute the correct business logic.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instruction: "Extract the attendee name, email, and meeting type from the payload."
- Instruction: "Map the extracted data to the required fields for the target CRM tool."

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure authentication with your external tools.
- Configure the connection scope to include read/write access for your CRM and communication platforms.

### 3) Tool Availability
- **CRM Connectors**: Create/Update records in Salesforce, HubSpot, or Pipedrive.
- **Communication Tools**: Send messages via Slack, Microsoft Teams, or Gmail.
- **Data Utilities**: Format dates and normalize attendee names for consistent database entry.

---

## Related Solutions
- [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate account creation and record mapping.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex business processes across multiple platforms.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensure multi-platform data consistency and conflict resolution.
