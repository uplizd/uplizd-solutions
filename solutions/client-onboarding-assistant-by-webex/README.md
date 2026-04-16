# Client Onboarding Assistant (Uplizd) - Streamline new client setup and communication workflows

## Summary
The Client Onboarding Assistant automates the complex process of initializing new customer relationships by creating personalized communication spaces, provisioning access, and guiding clients through their first steps. By leveraging the Composio Toolset to integrate with Webex and other collaboration platforms, this Uplizd AI workflow ensures a consistent, high-touch onboarding experience that reduces administrative overhead and accelerates time-to-value for new accounts.

---

## Demo
![Client Onboarding Assistant workflow interface showing automated Webex space creation and welcome message dispatch](image.png)

**Alt text (SEO-ready):** Client Onboarding Assistant Uplizd workflow, automated Webex space creation, customer onboarding automation, AI-driven client setup, Composio integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/874be03b-3404-513c-8f6a-1fc48b78a858)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** onboarding, webex, client success, automation, workflow, customer experience, composio, saas
- This solution bridges the gap between CRM data and collaboration tools to ensure seamless, automated handoffs during the client lifecycle.

---

## Who is this for?
This assistant is designed for teams looking to standardize their customer journey and eliminate manual setup tasks.

- **Customer Success Manager**
    - Automates the creation of dedicated communication channels for every new account.
- **Implementation Specialist**
    - Ensures all onboarding documentation and welcome materials are delivered instantly.
- **Sales Operations Lead**
    - Maintains consistent onboarding standards across the entire client base.
- **Account Executive**
    - Facilitates a smooth transition from contract signature to active project kickoff.

---

## Features
- **Automated Space Provisioning**
    - Automatically creates dedicated Webex spaces for new clients upon trigger.
- **Personalized Welcome Flows**
    - Dispatches tailored welcome messages and project links to client stakeholders.
- **Composio-Powered Integration**
    - Seamlessly connects your CRM data to collaboration platforms for real-time updates.
- **Task Tracking & Milestones**
    - Automatically populates initial onboarding checklists within the collaboration space.
- **Real-time Status Sync**
    - Updates internal systems as soon as the client joins the provided communication channel.

---

## Use Cases
**Client Kickoff Automation**
- Automatically generate a Webex space immediately after a deal is marked as "Closed Won" in your CRM.
- Send a standardized welcome packet including meeting links and project timelines to the primary client contact.

**Account Management Efficiency**
- Sync client contact lists from your CRM to the appropriate Webex space members list.
- Trigger automated follow-up reminders if a client has not joined the communication space within 48 hours.

**Onboarding Compliance**
- Ensure all new clients receive the mandatory security and support documentation during the initial setup phase.
- Log the timestamp of space creation and welcome message delivery for internal audit and reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `client-onboarding-assistant-by-webex` configuration file.
3. Authenticate your Webex and CRM accounts via the Composio connection manager.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the new client data and CRM trigger event.
- **Agent**: Processes the onboarding logic and determines the necessary communication steps.
- **Composio Toolset**: Executes the API calls to Webex and CRM to provision resources.
- **Chat Output**: Confirms successful space creation and notifies the internal team.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these prompts:
- `Create a new onboarding space for Acme Corp and send the welcome template.`
- `Check the status of the onboarding space for client ID 98765 and list the current members.`
- `Send a follow-up message to the project lead in the Webex space for account 'Global Tech'.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your onboarding logic.
- Use a model with strong instruction-following capabilities (e.g., GPT-4o).
- **Recommended instruction pattern:**
    - "You are a professional onboarding assistant; always maintain a helpful and welcoming tone."
    - "When creating spaces, ensure the naming convention follows: [Client Name] - Onboarding."
    - "If a tool call fails, log the error and notify the internal team via the Chat Output node."

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure access to Webex and CRM endpoints.
- Ensure the connection scope includes `webex:spaces:write` and `crm:contacts:read` permissions.

### 3) Tool Availability
- **Webex API**: For creating spaces, adding members, and sending messages.
- **CRM Connector**: For retrieving client contact details and deal status.
- **Notification Service**: For alerting internal stakeholders of onboarding progress.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamlines internal employee onboarding processes.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates CRM account creation and field population.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - Provides 24/7 automated support for existing clients.
