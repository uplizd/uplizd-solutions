# Smart Widget Manager (Uplizd) - Automate CallPage widget lifecycle and customization

## Summary
The Smart Widget Manager by CallPage is an intelligent Uplizd AI workflow designed to streamline the creation, configuration, and lifecycle management of web widgets. By leveraging the Composio Toolset to interface with CallPage, this solution eliminates manual setup overhead, ensuring consistent widget performance and rapid deployment for marketing and support teams.

---

## Demo
![Smart Widget Manager workflow showing CallPage integration nodes and automated widget configuration](image.png)
**Alt text (SEO-ready):** Smart Widget Manager workflow for CallPage, automating widget creation, configuration, and lifecycle management via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/653238a6-7755-50e2-a828-86828b3b90b0)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** callpage, widget management, automation, conversion optimization, lead generation, composio, ai workflow
- This solution bridges the gap between marketing strategy and technical implementation by automating the deployment of interactive widgets.

---

## Who is this for?
This workflow is designed for teams looking to scale their conversion assets without increasing manual administrative burden.

- **Marketing Managers**
    - Rapidly deploy new widgets for seasonal campaigns without waiting for engineering resources.
- **Conversion Rate Optimization (CRO) Specialists**
    - Automate A/B testing configurations and widget adjustments to maximize lead capture.
- **Customer Success Leads**
    - Ensure support widgets are consistently updated with the latest contact information and availability.
- **Operations Analysts**
    - Maintain a clean, audited trail of widget configurations across multiple domains and landing pages.

---

## Features
- **Automated Widget Provisioning**
    - Instantly generate new CallPage widgets using predefined templates and business logic.
- **Dynamic Configuration Updates**
    - Programmatically adjust widget triggers, display rules, and styling based on real-time campaign performance.
- **Composio-Powered Integration**
    - Securely connect to the CallPage API to execute complex management tasks through natural language prompts.
- **Lifecycle Management**
    - Automatically archive or disable outdated widgets to maintain site performance and brand consistency.
- **Real-time Sync**
    - Ensure that widget settings remain synchronized across all connected platforms and internal databases.

---

## Use Cases
**Campaign Deployment**
- Automatically create and launch specific widgets for limited-time promotional landing pages.
- Update widget messaging dynamically based on the current marketing campaign theme.

**Performance Optimization**
- Trigger widget configuration changes based on A/B test results to improve visitor engagement.
- Adjust widget display frequency and timing to reduce bounce rates on high-traffic pages.

**Operational Hygiene**
- Batch-update contact details or support hours across all active widgets simultaneously.
- Audit and audit-log widget settings to ensure compliance with regional data privacy standards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Widget Manager JSON configuration file.
3. Authenticate your CallPage account within the Composio connection manager.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for widget creation or modification.
- **Agent**: Interprets intent and maps requirements to specific CallPage API parameters.
- **Composio Toolset**: Executes the authenticated API calls to manage widget states.
- **Chat Output**: Confirms the status of the operation and provides a summary of changes.

### 3) Run the Flow
Use the Playground to test your configuration with prompts like:
- `Create a new CallPage widget for the Summer Sale campaign with a 5-second delay.`
- `Update the primary contact number for all active widgets on the pricing page.`
- `Disable the 'Request a Demo' widget on the blog section immediately.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for all widget management tasks.
- Use a model with strong function-calling capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a CallPage expert. Always verify widget IDs before applying updates."
- Instruction: "If a requested configuration change is missing required parameters, ask the user for clarification."

### 2) Composio Toolset Node
- Provide your CallPage API key within the Composio dashboard.
- Set the connection scope to include `widget:write` and `widget:read` permissions.

### 3) Tool Availability
- `create_widget`: Initializes a new widget instance with specified settings.
- `update_widget_config`: Modifies existing parameters like display rules and styling.
- `list_widgets`: Retrieves a current inventory of all active and inactive widgets.
- `delete_or_archive_widget`: Manages the lifecycle and removal of legacy assets.

---

## Related Solutions
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) — Automate customer support interactions using AI-driven chatbots.
- [ab-test-optimizer-by-mixpanel](../ab-test-optimizer-by-mixpanel/README.md) — Optimize A/B testing workflows and analyze performance data.
- [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex operational workflows and task management.
