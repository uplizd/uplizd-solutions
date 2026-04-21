# WhatsApp Lead Qualifier (Uplizd) - Automated lead qualification and routing for WhatsApp

## Summary
The WhatsApp Lead Qualifier (Uplizd) is an intelligent automation workflow designed to streamline sales operations by instantly qualifying incoming leads from WhatsApp. By leveraging the Composio Toolset to interface with your CRM, this solution filters high-intent prospects, captures essential contact data, and routes qualified leads to the appropriate sales representative, significantly reducing manual data entry and increasing pipeline velocity.

---

## Demo
![WhatsApp Lead Qualifier workflow diagram showing automated message processing, CRM qualification, and routing](image.png)
**Alt text (SEO-ready):** WhatsApp Lead Qualifier workflow diagram showing automated message processing, CRM qualification, and routing via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cbca2a0b-72ee-556e-a396-fd8c45494cf6)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** whatsapp, lead qualification, crm, sales ops, lead routing, composio, ai workflow, data sync
This solution bridges the gap between instant messaging and CRM management to ensure no lead goes unvetted.

---

## Who is this for?
This solution is designed for revenue teams looking to eliminate manual lead triage and accelerate response times.

- **Sales Development Representative (SDR)**
  - Receives only pre-qualified leads, allowing focus on high-value conversations rather than manual data entry.
- **RevOps Manager**
  - Standardizes the lead intake process across WhatsApp channels to ensure consistent data hygiene and pipeline reporting.
- **Sales Manager**
  - Gains visibility into lead quality and response speed, enabling better coaching and resource allocation.
- **Growth Marketer**
  - Optimizes conversion rates by ensuring that leads generated from social campaigns are engaged immediately.

---

## Features
- **Automated Lead Qualification**
  - Uses AI to analyze incoming WhatsApp messages against predefined criteria to determine lead readiness.
- **Real-time CRM Integration**
  - Automatically creates or updates lead records in your CRM via the Composio Toolset upon successful qualification.
- **Intelligent Routing**
  - Dynamically assigns qualified leads to the correct sales representative based on territory, industry, or lead score.
- **Instant Response Automation**
  - Triggers personalized follow-up messages to prospects, keeping them engaged while the sales team is notified.
- **Data Hygiene & Enrichment**
  - Cleans and formats contact information automatically, ensuring your CRM remains a single source of truth.

---

## Use Cases
**Lead Intake & Triage**
- Automatically categorize incoming WhatsApp inquiries as "Sales Ready" or "Support" based on intent.
- Extract key contact details like company name and job title directly from the chat thread.

**Sales Pipeline Acceleration**
- Trigger an immediate notification to the assigned account executive when a high-intent lead is identified.
- Sync qualified lead data to the CRM to ensure the pipeline reflects real-time interest.

**Operational Efficiency**
- Reduce the time spent on manual lead entry by automating the transfer of WhatsApp conversations to CRM fields.
- Standardize lead qualification criteria across multiple WhatsApp business accounts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the WhatsApp Lead Qualifier template via the provided solution URL.
3. Connect your WhatsApp business account and CRM credentials within the integration settings.
4. Ensure nodes are correctly mapped and all API connections are authorized before activating the flow.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming WhatsApp messages and extracts raw customer data.
- **Agent**: Analyzes the message content to determine qualification status based on your business logic.
- **Composio Toolset**: Executes CRM actions such as searching for existing contacts or creating new lead records.
- **Chat Output**: Sends a confirmation or follow-up response back to the prospect via WhatsApp.

### 3) Run the Flow
Test the workflow in the Uplizd Playground using these example prompts:
- `Qualify this lead: "Hi, I'm interested in a demo for my team of 50."`
- `Check if this contact exists in Salesforce and update their status to 'Qualified'.`
- `Extract the company name from this message: "We are looking for a solution at Acme Corp."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary decision engine for lead qualification.
- Use a clear, concise system prompt defining your "Ideal Customer Profile."
- Instruct the agent to prioritize data extraction accuracy over conversational filler.
- Define specific fallback actions for ambiguous messages (e.g., "Ask for clarification").

### 2) Composio Toolset Node
- Provide your CRM API key to enable secure read/write access.
- Set the connection scope to include "Lead Management" and "Contact Search" permissions.

### 3) Tool Availability
- **CRM Search**: Locates existing records to prevent duplicate entries.
- **Lead Creation**: Populates new records with extracted data.
- **Notification Trigger**: Alerts the sales team via Slack or Email.
- **Data Validation**: Ensures phone numbers and email formats meet CRM requirements.

---

## Related Solutions
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automated follow-up sequences for WhatsApp leads.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Multi-platform synchronization for consistent CRM data.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-ups for high-velocity sales.
- [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by2chat/README.md) - Route support-related WhatsApp messages to the correct team.
