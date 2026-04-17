# Intelligent Sales SMS Follow-up Agent (Uplizd) - Automated personalized SMS engagement for sales pipelines

## Summary
The Intelligent Sales SMS Follow-up Agent is an Uplizd AI workflow designed to automate personalized SMS outreach based on real-time sales pipeline triggers. By integrating directly with your CRM and messaging platforms, this solution ensures timely, context-aware follow-ups that increase lead conversion rates, reduce manual outreach fatigue, and maintain consistent communication hygiene across the entire customer journey.

---

## Demo
![Intelligent Sales SMS Follow-up Agent workflow diagram showing CRM triggers, AI personalization, and SMS delivery](image.png)
**Alt text (SEO-ready):** Intelligent Sales SMS Follow-up Agent workflow diagram showing CRM triggers, AI personalization, and SMS delivery via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKYGBgYPhPBf9fQJgB/08wGgYjYBRMAhIMBgwMDAwM/0k0GgYjYBRMAhIMBgwAAL/aJ9g2X4eHAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/9f609e3e-2bb8-5349-8dcb-2a7cfb4e0c9c)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** `sms`, `crm`, `lead nurturing`, `sales pipeline`, `automation`, `ai workflow`, `composio`, `customer engagement`

This solution bridges the gap between CRM pipeline status changes and high-conversion SMS communication, enabling automated yet personalized sales interactions.

---

## Who is this for?
This solution is designed for high-velocity sales teams looking to scale personalized outreach without increasing headcount.

*   **Sales Development Rep (SDR):**
    *   Automates initial lead outreach to ensure no prospect is left uncontacted during peak interest windows.
*   **Account Executive (AE):**
    *   Maintains consistent touchpoints with stalled opportunities to nudge deals toward closure.
*   **RevOps Manager:**
    *   Standardizes communication cadences across the team to ensure brand voice and compliance in every message.
*   **Growth Marketer:**
    *   Leverages behavioral triggers to send timely SMS follow-ups that improve conversion rates from marketing-qualified leads.

---

## Features
- **Pipeline-Triggered Outreach**
  Automatically initiates SMS sequences when a lead moves to a specific stage, ensuring immediate engagement.
- **AI-Driven Personalization**
  Uses LLMs to craft unique, context-aware messages based on lead data, CRM history, and recent interactions.
- **Composio Toolset Integration**
  Seamlessly connects with CRM platforms and SMS gateways to execute actions without manual intervention.
- **Real-Time Sync**
  Updates CRM records instantly with message delivery status and recipient responses for a single source of truth.
- **Compliance-Aware Messaging**
  Ensures all automated follow-ups adhere to pre-defined opt-out and frequency settings for professional outreach.

---

## Use Cases
**Lead Qualification & Nurturing**
*   Send a personalized welcome SMS immediately after a prospect fills out a demo request form.
*   Automate follow-up messages for leads who haven't responded to email sequences within 48 hours.

**Stalled Deal Recovery**
*   Trigger an SMS nudge when an opportunity remains in the "Negotiation" stage for more than 7 days.
*   Send a "check-in" message to prospects who have gone silent after a product demonstration.

**Event & Webinar Engagement**
*   Send automated SMS reminders 1 hour before a scheduled sales call or product webinar.
*   Follow up with attendees post-event with a personalized summary and a direct link to book a discovery session.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your CRM and SMS provider credentials within the integration settings.
4. Ensure nodes are correctly mapped and all API connections are active before deploying.

### 2) Setup the Nodes
*   **Chat Input:** Receives the trigger event from your CRM pipeline or manual request.
*   **Agent:** Analyzes lead context and drafts the personalized SMS content.
*   **Composio Toolset:** Executes the SMS dispatch and logs the activity back to the CRM.
*   **Chat Output:** Confirms the message delivery status and provides a summary of the interaction.

### 3) Run the Flow
Use the Playground to test your agent with these example prompts:
* `Send a follow-up SMS to John Doe regarding his stalled demo request in the 'Discovery' stage.`
* `Draft a personalized check-in message for a lead who hasn't replied to our last three emails.`
* `Notify the lead about the upcoming webinar and include the registration link in the SMS.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional sales assistant focused on brevity and conversion.
*   Maintain a helpful, non-intrusive, and professional tone.
*   Reference specific CRM data points (e.g., company name, last interaction) to increase relevance.
*   Always include a clear, low-friction call to action (CTA) in every message.

### 2) Composio Toolset Node
Connect your preferred CRM (e.g., Salesforce, HubSpot) and SMS provider (e.g., Twilio, MessageBird) via the Composio Toolset node to grant the agent read/write access to your communication stack.

### 3) Tool Availability
*   **CRM Read/Write:** Fetch lead details and update activity logs.
*   **SMS Gateway:** Dispatch messages and track delivery receipts.
*   **Calendar Integration:** Check availability for scheduling follow-up calls.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead data across multiple platforms for unified visibility.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and optimize sales pipeline stages and follow-up cadences.
* [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Extend your automated outreach strategy to WhatsApp channels.
