# Lead Response Assistant (Uplizd) - Automate personalized sales inquiry replies

## Summary
The Lead Response Assistant is an intelligent Uplizd workflow designed to accelerate sales velocity by automatically drafting personalized, context-aware responses to incoming leads. By integrating directly with Gmail, this solution eliminates manual drafting time, ensures consistent brand messaging, and maintains high engagement rates by providing immediate, relevant follow-ups to potential customers.

---

## Demo
![Lead Response Assistant workflow showing Gmail trigger, AI agent processing, and draft generation](image.png)
**Alt text (SEO-ready):** Uplizd Lead Response Assistant workflow for automated Gmail sales inquiry drafting and lead engagement.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUADAAABAAABAAAA//8DABgA/v8DAAABAAAA//8DABgA/v8DAAABAAAA//8DABgA/v8DAAABAAAA/wA=)](https://uplizd.ai/solutions/44b05d8d-fe10-5ef9-85df-efe1ca5a1cf4)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** gmail, lead response, sales, email automation, composio, ai workflow, lead nurturing, productivity.
This solution streamlines the sales pipeline by automating the initial communication layer between your team and incoming leads.

---

## Who is this for?
This solution is built for revenue-focused teams looking to reduce response latency and improve lead conversion rates.

- **Sales Development Reps (SDRs)**
    - Drastically reduce time spent drafting initial outreach emails for new inbound leads.
- **Account Executives**
    - Ensure every prospect receives a professional, personalized response even during high-volume periods.
- **RevOps Managers**
    - Standardize communication quality and response speed across the entire sales organization.
- **Small Business Owners**
    - Maintain 24/7 responsiveness to customer inquiries without needing a dedicated support staff.

---

## Features
- **Intelligent Context Analysis**
    - The agent parses incoming email content to identify lead intent, pain points, and specific product interests.
- **Gmail Integration**
    - Seamlessly connects to your inbox via the Composio Toolset to read inquiries and save drafts automatically.
- **Personalized Tone Matching**
    - Dynamically adjusts the email style based on the lead's industry and the urgency of their request.
- **Automated Draft Creation**
    - Pre-populates high-quality, ready-to-send responses in your Gmail drafts folder for final human review.
- **Real-time Lead Prioritization**
    - Flags high-intent leads for immediate attention while drafting standard replies for general inquiries.

---

## Use Cases
**Lead Qualification**
- Automatically draft responses for leads that meet specific BANT criteria (Budget, Authority, Need, Timing).
- Filter out spam or irrelevant inquiries before they reach your primary sales queue.

**Sales Follow-up**
- Send immediate acknowledgment emails to prospects who request demos or pricing information.
- Schedule follow-up reminders within the email draft for the account owner to review.

**Customer Engagement**
- Provide instant answers to frequently asked questions regarding product features or service availability.
- Maintain a consistent brand voice across all initial touchpoints with new prospects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the builder.
2. Connect your Gmail account via the Composio integration settings.
3. Configure your LLM provider (e.g., OpenAI, Anthropic) in the Agent node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw email content and sender metadata from your inbox.
- **Agent**: Processes the inquiry, determines the appropriate response strategy, and generates the email body.
- **Composio Toolset**: Executes the `gmail_create_draft` action to save the response securely.
- **Chat Output**: Confirms the draft creation and logs the interaction for your records.

### 3) Run the Flow
Test the workflow using the Playground with these example prompts:
- `Draft a professional response to this inquiry asking for our enterprise pricing.`
- `Write a friendly follow-up email for a lead interested in our onboarding services.`
- `Create a response acknowledging receipt of this support request and promising a reply within 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your digital sales assistant. Use the following instructions:
- Analyze the incoming email for key intent and urgency.
- Maintain a professional, helpful, and brand-aligned tone.
- Ensure the draft includes a clear call-to-action (CTA) based on the lead's request.

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure authentication.
- Set the connection scope to `gmail.send` and `gmail.readonly` to allow the agent to read and draft emails.

### 3) Tool Availability
- `gmail_get_thread`: Retrieve full conversation context for existing leads.
- `gmail_create_draft`: Save the AI-generated response directly into your Gmail drafts.
- `gmail_list_messages`: Identify new, unread inquiries in your inbox.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track sales pipeline stages and stalled opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple CRM platforms.
- [Account Research Assistant](../account-research-assistant/README.md) - Gather intelligence on prospects to personalize outreach efforts.
