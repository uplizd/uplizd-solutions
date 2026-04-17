# Multi-Agency WhatsApp Coordinator (Uplizd) - Centralized cross-agency communication management

## Summary
The Multi-Agency WhatsApp Coordinator by Spoki enables businesses to manage and synchronize WhatsApp communication streams across multiple agencies from a single interface. By leveraging the Composio Toolset to bridge Spoki’s messaging infrastructure with Uplizd’s intelligent orchestration, this solution eliminates communication silos, ensures consistent brand messaging, and provides real-time visibility into multi-channel support and marketing operations.

---

## Demo
![Multi-Agency WhatsApp Coordinator workflow showing Spoki integration and automated message routing](image.png)
**Alt text (SEO-ready):** Multi-Agency WhatsApp Coordinator workflow on Uplizd, showcasing Spoki integration for automated cross-agency messaging and communication management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6m415WwAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeOeVIUAAAAJ0lEQVR42mP8z8AARkBCwEwGjP8zMDBgYmBgYJgA4v8fBAA0/wQBAwB63Qf/1Hk/1gAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/d8aaca44-4d5b-57fe-a03c-1d7df133324c)

---

## Category
- **Primary category:** Communication
- **Secondary tags:** whatsapp, spoki, multi-agency, messaging, automation, communication management, composio, ai workflow
- This solution streamlines complex multi-agency communication workflows by centralizing WhatsApp interactions into a unified, automated management layer.

---

## Who is this for?
This solution is designed for organizations that manage high-volume messaging across distributed teams and external partners.

- **Operations Manager**
    - Centralizes oversight of all agency communication channels to ensure consistent service levels.
- **Customer Support Lead**
    - Automates the triage and routing of incoming WhatsApp queries to the appropriate agency team.
- **Marketing Coordinator**
    - Synchronizes campaign messaging across multiple agency accounts to maintain brand alignment.
- **Agency Partner**
    - Gains secure, role-based access to specific messaging streams without compromising overall data integrity.

---

## Features
- **Centralized Message Routing**
    - Automatically directs incoming WhatsApp messages from various sources to the designated agency workspace.
- **Multi-Agency Synchronization**
    - Keeps communication history and status updates consistent across disparate agency accounts using Spoki.
- **Automated Response Management**
    - Deploys intelligent AI-driven responses to common inquiries, reducing manual overhead for support teams.
- **Unified Reporting Dashboard**
    - Aggregates performance metrics and response times across all connected agency channels into one view.
- **Composio-Powered Integration**
    - Seamlessly connects the Uplizd agent with Spoki APIs to execute real-time messaging actions and data retrieval.

---

## Use Cases
**Cross-Agency Support Triage**
- Automatically route customer support tickets to the specific agency responsible for that product line.
- Escalate high-priority WhatsApp messages to a human supervisor when sentiment analysis detects frustration.

**Brand-Consistent Marketing Outreach**
- Deploy standardized promotional templates across multiple agency-managed WhatsApp numbers simultaneously.
- Track engagement rates for marketing campaigns to identify which agency is delivering the highest ROI.

**Operational Communication Sync**
- Sync internal status updates between agencies to ensure everyone is aligned on client project timelines.
- Archive all WhatsApp interactions into a centralized database for compliance and quality assurance audits.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Multi-Agency WhatsApp Coordinator.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Spoki API credentials within the integration settings.
4. Ensure nodes are correctly linked from Chat Input through to the final Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming WhatsApp messages and metadata from Spoki.
- **Agent**: Analyzes message intent and determines the appropriate agency routing logic.
- **Composio Toolset**: Executes API calls to Spoki for message retrieval, sending, and status updates.
- **Chat Output**: Delivers the processed response or confirmation back to the user or system log.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Route the latest unread WhatsApp messages from the 'North America' agency queue.`
- `Send a status update template to all active leads managed by the 'Digital Marketing' agency.`
- `Generate a summary report of all support interactions handled by the 'Customer Success' agency today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for routing and response generation.
- Use a model capable of high-context reasoning for multi-agency logic.
- **Recommended instruction pattern:**
    - Identify the source agency from the incoming message metadata.
    - Select the appropriate response template based on the detected intent.
    - Route the action to the correct Spoki endpoint via the Composio Toolset.

### 2) Composio Toolset Node
- Provide your Spoki API key to enable secure communication.
- Set the connection scope to allow the agent to read and write messages across all authorized agency accounts.

### 3) Tool Availability
- **Message Retrieval**: Fetching incoming WhatsApp threads.
- **Message Dispatch**: Sending responses or automated templates.
- **Contact Enrichment**: Updating contact records based on conversation history.
- **Status Tracking**: Monitoring delivery and read receipts across agencies.

---

## Related Solutions
- [WhatsApp Support Ticket Manager](../whats-app-support-ticket-manager-by-spoki/README.md) — Streamline ticket resolution for WhatsApp-based support.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Automate lead engagement and follow-up sequences.
- [WhatsApp Contact Data Enricher](../whats-app-contact-data-enricher-by-spoki/README.md) — Automatically update CRM profiles from WhatsApp interactions.
