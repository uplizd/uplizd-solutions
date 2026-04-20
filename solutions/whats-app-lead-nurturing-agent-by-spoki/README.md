# WhatsApp Lead Nurturing Agent (Uplizd) - Automate personalized lead engagement and conversion

## Summary
The WhatsApp Lead Nurturing Agent (Uplizd) is an intelligent workflow designed to automate personalized communication sequences with prospects directly via WhatsApp. By leveraging the Spoki integration, this solution enables sales and marketing teams to maintain consistent engagement, move leads through the funnel, and improve conversion rates without manual intervention, serving as a single source of truth for your lead nurturing pipeline.

---

## Demo
![WhatsApp Lead Nurturing Agent workflow diagram showing Chat Input, Agent, Spoki integration, and Chat Output](image.png)
**Alt text (SEO-ready):** WhatsApp Lead Nurturing Agent workflow by Uplizd, featuring automated lead engagement, Spoki integration, and AI-driven pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4bc1f2e0-0a82-5019-b626-fc1fd83869e6)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** whatsapp, spoki, lead nurturing, sales pipeline, crm, ai workflow, conversion, engagement
- This solution bridges the gap between CRM lead data and real-time messaging platforms to ensure timely, high-impact prospect interactions.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach while maintaining a human touch.

- **Sales Development Representative (SDR)**
    - Automates follow-ups to stalled leads, ensuring no prospect falls through the cracks.
- **Marketing Manager**
    - Orchestrates personalized drip campaigns via WhatsApp to increase engagement rates compared to traditional email.
- **Revenue Operations (RevOps) Lead**
    - Standardizes the lead nurturing process across the organization to improve pipeline velocity and data hygiene.
- **Customer Success Manager**
    - Proactively engages new sign-ups with onboarding sequences to drive product adoption and satisfaction.

---

## Features
- **Automated Sequence Triggering**
    - Automatically initiates nurturing flows based on specific CRM status changes or lead scoring thresholds.
- **Personalized Message Generation**
    - Uses advanced LLMs to tailor content based on prospect industry, job title, and previous interactions.
- **Spoki Integration**
    - Seamlessly connects with Spoki to manage WhatsApp message delivery, templates, and conversation tracking.
- **Real-time Engagement Monitoring**
    - Captures response data to update lead status in your CRM, ensuring the agent always has the latest context.
- **Dynamic Content Adaptation**
    - Adjusts tone and call-to-action based on the prospect's stage in the buying journey.

---

## Use Cases
**Lead Qualification & Follow-up**
- Automatically send a personalized greeting and discovery questions to new inbound leads within 5 minutes.
- Re-engage leads who haven't interacted with your brand in over 30 days with a tailored value-add message.

**Event & Webinar Promotion**
- Send automated reminders and session details to registered attendees via WhatsApp to boost show-up rates.
- Follow up with event participants post-session to share resources and schedule discovery calls.

**Sales Pipeline Acceleration**
- Nudge prospects who have been in the "Proposal Sent" stage for more than 3 days with a helpful check-in.
- Trigger automated "thank you" and next-step sequences immediately after a demo is marked as completed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and click "Import Flow."
3. Configure your Spoki API credentials within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives lead data and trigger events from your CRM or webhooks.
- **Agent**: Processes the lead context and determines the appropriate nurturing message.
- **Composio Toolset**: Executes the WhatsApp message dispatch via the Spoki API.
- **Chat Output**: Logs the interaction status and confirms delivery to the user.

### 3) Run the Flow
Test your workflow in the Uplizd Playground:
- `Send a personalized follow-up message to lead John Doe regarding the recent demo.`
- `Initiate the standard onboarding sequence for the new lead in the 'Qualified' stage.`
- `Check the status of the last nurturing message sent to the prospect with phone number +1234567890.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your nurturing strategy.
- Maintain a professional, helpful, and concise tone suitable for WhatsApp.
- Use the provided context to reference specific pain points or interests mentioned in the CRM.
- Always include a clear, low-friction call-to-action (CTA) in every message.

### 2) Composio Toolset Node
- Provide your Spoki API key to authorize the agent to send messages on your behalf.
- Ensure the connection scope includes `whatsapp_send_message` and `whatsapp_get_contact_info` permissions.

### 3) Tool Availability
- **Spoki Messaging**: Ability to send text, template-based messages, and media attachments.
- **CRM Lookup**: Ability to fetch lead details, current pipeline stage, and interaction history.
- **Data Logger**: Ability to update lead activity logs upon successful message delivery.

---

## Related Solutions
- [WhatsApp Lead Qualifier by Wati](../whats-app-lead-qualifier-by-wati/README.md) - Automate lead qualification and scoring via WhatsApp.
- [WhatsApp Support Ticket Manager by Spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Manage customer support inquiries directly in WhatsApp.
- [WhatsApp Contact Data Enricher by Spoki](../whats-app-contact-data-enricher-by-spoki/README.md) - Automatically enrich lead profiles using WhatsApp conversation data.
