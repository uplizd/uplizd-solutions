# Service Catalog Assistant (Uplizd) - Streamline IT and HR request fulfillment

## Summary
The Service Catalog Assistant is an intelligent Uplizd workflow that automates the intake, routing, and fulfillment of service catalog requests. By leveraging the Composio Toolset to interface directly with ServiceNow, this solution eliminates manual ticket entry, reduces response latency, and ensures a single source of truth for internal service requests, significantly improving operational throughput for IT and HR teams.

---

## Demo
![Service Catalog Assistant workflow UI showing automated request routing and ServiceNow integration](image.png)
**Alt text (SEO-ready):** Service Catalog Assistant Uplizd workflow automating ServiceNow ticket creation and request fulfillment via AI agent.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0dc81c94-b919-58a7-bfc0-82e250d27a3c)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** servicenow, it-service-management, itsm, workflow-automation, request-fulfillment, composio, ai-agent, enterprise-ops
- This solution bridges the gap between conversational AI and enterprise service management platforms to accelerate request resolution.

---

## Who is this for?
The Service Catalog Assistant is designed for organizations looking to modernize their internal service delivery and reduce administrative overhead.

- **IT Support Manager**
    - Automate ticket triage and reduce the manual burden of routing routine service requests.
- **HR Operations Specialist**
    - Streamline employee onboarding and document requests through automated form processing.
- **System Administrator**
    - Ensure consistent data entry and compliance across all service catalog submissions.
- **Operations Lead**
    - Improve pipeline velocity by providing instant, AI-driven responses to common internal queries.

---

## Features
- **Automated Request Intake**
    - Uses natural language processing to parse user requests and map them to the correct service catalog items.
- **ServiceNow Integration**
    - Seamlessly creates and updates tickets in ServiceNow using the secure Composio Toolset.
- **Real-time Status Updates**
    - Provides users with immediate feedback on their request status without requiring manual agent intervention.
- **Intelligent Routing**
    - Dynamically assigns tickets to the appropriate department or queue based on request intent and urgency.
- **Data Hygiene Enforcement**
    - Validates input fields against existing catalog schemas to ensure high-quality data entry.

---

## Use Cases
**IT Service Management**
- Automatically generate hardware request tickets when employees submit a new laptop or peripheral inquiry.
- Route software access requests to the correct approval groups based on the requested application.

**HR Operations**
- Handle employee document requests (e.g., employment verification) by querying internal databases and generating tickets.
- Automate the collection of onboarding information for new hires, ensuring all required fields are populated in the system.

**Operational Efficiency**
- Reduce "mean time to acknowledge" by providing instant AI responses to common service catalog questions.
- Minimize manual data entry errors by standardizing how requests are formatted before hitting the ServiceNow API.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Connect your ServiceNow account via the Composio Toolset integration.
3. Configure your environment variables for API authentication.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's natural language request.
- **Agent**: Processes the request and determines the necessary service catalog action.
- **Composio Toolset**: Executes the specific ServiceNow API call to create or update the record.
- **Chat Output**: Delivers the confirmation or status update back to the user.

### 3) Run the Flow
Use the Playground to test your assistant with these prompts:
- `I need to request a new MacBook Pro for my workstation.`
- `What is the status of my pending software access request?`
- `I need an employment verification letter for my bank.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for service requests.
- Use a model capable of structured output (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on mapping user intent to specific ServiceNow catalog IDs.
- Ensure the agent is configured to ask clarifying questions if the user request lacks mandatory fields.

### 2) Composio Toolset Node
- Authenticate using your ServiceNow instance URL and OAuth credentials.
- Set the connection scope to allow 'read' and 'write' access to the Service Catalog and Incident tables.

### 3) Tool Availability
- `servicenow_create_request`: For initiating new catalog items.
- `servicenow_get_ticket_status`: For querying existing ticket progress.
- `servicenow_update_record`: For adding comments or attachments to existing requests.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support ticket management for external customers.
- [account-setup-agent-by-salesforce](../account-setup-agent-by-salesforce/README.md) - Streamline CRM account creation and data entry.
- [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Manage and prioritize incident response action items.
- [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose workflow automation for operational tasks.
