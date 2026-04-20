# WhatsApp Lead Qualifier (Uplizd) - Automated lead qualification and routing for WhatsApp

## Summary
The WhatsApp Lead Qualifier (Uplizd) automates the intake, qualification, and routing of incoming WhatsApp leads directly into your CRM. By leveraging AI to analyze prospect intent and business requirements in real-time, this workflow eliminates manual data entry, reduces response latency, and ensures high-intent leads are prioritized for your sales team, resulting in increased pipeline velocity and improved lead hygiene.

---

## Demo
![WhatsApp Lead Qualifier workflow interface showing automated message parsing and CRM routing](image.png)
**Alt text (SEO-ready):** WhatsApp Lead Qualifier workflow interface showing automated message parsing, lead qualification, and CRM routing using Uplizd and WATI integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/99b892cd-3a1d-5dae-ba17-36caa6cf31a1)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** whatsapp, wati, lead qualification, crm, sales ops, lead routing, ai workflow, composio
- This solution bridges the gap between conversational messaging platforms and CRM systems to streamline the lead-to-opportunity lifecycle.

---

## Who is this for?
This solution is designed for revenue teams looking to capture and convert mobile-first prospects with speed and precision.

- **Sales Development Reps (SDRs)**
    - Eliminates manual qualification tasks, allowing focus on high-value conversations.
- **Revenue Operations Managers**
    - Ensures standardized lead data entry and consistent routing logic across the sales funnel.
- **Marketing Managers**
    - Increases conversion rates by providing immediate, relevant responses to inbound WhatsApp inquiries.
- **Customer Success Leads**
    - Facilitates rapid triage of incoming messages to ensure inquiries reach the correct support or sales queue.

---

## Features
- **Automated Intent Analysis**
    - Uses AI to parse incoming WhatsApp messages for buying signals, budget, and timeline.
- **Real-time CRM Sync**
    - Automatically creates or updates lead records in your CRM using the Composio Toolset.
- **Intelligent Lead Routing**
    - Assigns leads to specific sales representatives based on predefined territory or industry rules.
- **Instant Response Generation**
    - Triggers personalized, context-aware replies to keep prospects engaged while the lead is processed.
- **Data Hygiene Enforcement**
    - Standardizes lead formatting and contact information before syncing to your database.

---

## Use Cases
**Lead Qualification & Enrichment**
- Automatically extract contact details and company size from initial WhatsApp inquiries.
- Score leads based on specific keywords or intent markers detected in the conversation.

**Sales Pipeline Acceleration**
- Instantly route qualified leads to the appropriate account executive's calendar or queue.
- Reduce response time from hours to seconds by automating the initial qualification handshake.

**CRM Data Management**
- Sync WhatsApp conversation history directly to the lead record for a 360-degree view.
- Prevent duplicate entries by checking existing CRM records before creating new leads.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Connect your WATI and CRM accounts via the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and environment variables.

### 2) Setup the Nodes
- **Chat Input**: Captures the incoming WhatsApp message and sender metadata.
- **Agent**: Analyzes the message content to determine lead intent and qualification status.
- **Composio Toolset**: Executes CRM search, lead creation, and update actions.
- **Chat Output**: Sends a confirmation or follow-up message back to the WhatsApp user.

### 3) Run the Flow
Open the Playground to test your configuration with these example prompts:
- `Qualify this lead: "Hi, I'm interested in your enterprise pricing for 50 users."`
- `Check if this phone number exists in Salesforce and update the lead status to 'Qualified'.`
- `Extract company name and role from this message: "Hi, I'm Sarah from Acme Corp, looking for a demo."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the qualification process, summarizing intent and deciding the next action.
- Use a high-reasoning model (e.g., GPT-4o) for accurate intent classification.
- Set the system prompt to prioritize lead qualification criteria specific to your business.
- Ensure the agent is instructed to output JSON for seamless CRM integration.

### 2) Composio Toolset Node
- Provide your API key within the Composio Toolset node to authorize CRM access.
- Define the connection scope to include read/write permissions for Leads, Contacts, and Accounts.

### 3) Tool Availability
- **CRM Search**: Look up existing prospects to prevent duplicates.
- **Lead Creation**: Generate new records for qualified inquiries.
- **Field Update**: Modify status, lead score, or owner fields based on AI analysis.
- **Communication**: Send automated follow-up messages via WATI.

---

## Related Solutions
- [../whats-app-lead-qualifier-by-timelinesai/README.md](../whats-app-lead-qualifier-by-timelinesai/README.md) - Alternative WhatsApp lead qualification using TimelinesAI.
- [../whats-app-lead-qualifier-by2chat/README.md](../whats-app-lead-qualifier-by2chat/README.md) - WhatsApp lead qualification and routing via 2Chat.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - General-purpose CRM data synchronization and conflict resolution.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Automated CRM data cleanup and formatting agent.
