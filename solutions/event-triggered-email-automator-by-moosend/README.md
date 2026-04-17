# Event-Triggered Email Automator (Uplizd) - Real-time personalized email workflows

## Summary
The Event-Triggered Email Automator (Uplizd) streamlines customer communication by automatically dispatching personalized emails in response to specific user actions or platform events. This solution empowers marketing and operations teams to maintain high engagement levels, reduce manual outreach overhead, and ensure timely delivery of relevant content, acting as a single source of truth for automated email lifecycle management.

---

## Demo
![Uplizd workflow diagram showing an event trigger connected to an email automation agent using Moosend](image.png)
**Alt text (SEO-ready):** Uplizd event-triggered email automation workflow using Moosend for personalized customer communication and pipeline engagement.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/62ccab70-9353-5462-89ad-8cc03ce0c511)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email automation, moosend, customer engagement, event-driven, workflow automation, marketing, personalization, composio
- This solution bridges the gap between raw user event data and actionable email communication to drive higher conversion rates.

---

## Who is this for?
This solution is designed for teams looking to automate their customer lifecycle and improve communication velocity.

- **Marketing Manager**
    - Automates personalized nurture sequences without manual intervention.
- **Customer Success Lead**
    - Triggers timely onboarding or check-in emails based on product usage events.
- **Growth Marketer**
    - Increases conversion rates by sending targeted offers immediately following user actions.
- **Operations Specialist**
    - Ensures consistent data hygiene and reliable delivery of transactional emails across platforms.

---

## Features
- **Real-time Event Processing**
    - Captures user actions instantly to trigger relevant email workflows without latency.
- **Dynamic Personalization**
    - Injects user-specific data into email templates to increase open and click-through rates.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely connect with Moosend and other marketing platforms.
- **Automated Lifecycle Management**
    - Orchestrates complex sequences based on user behavior, from welcome series to re-engagement.
- **Scalable Workflow Builder**
    - Easily modify or expand automation logic within the Uplizd visual builder as your business grows.

---

## Use Cases
**Customer Onboarding**
- Trigger a welcome email series immediately after a new user signs up.
- Send feature-specific educational content based on the user's initial setup actions.

**Engagement & Retention**
- Send automated re-engagement emails to users who have been inactive for a set period.
- Dispatch personalized milestone celebrations or usage summaries to power long-term loyalty.

**Conversion Optimization**
- Trigger follow-up emails with targeted discounts when a user abandons a specific workflow.
- Send personalized product recommendations based on recent user activity or browsing history.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Event-Triggered Email Automator template from the solution library.
3. Authenticate your Moosend account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the event payload or user action trigger.
- **Agent**: Processes the intent and determines the appropriate email template to use.
- **Composio Toolset**: Executes the API call to Moosend to send the personalized email.
- **Chat Output**: Confirms the delivery status and logs the interaction for audit purposes.

### 3) Run the Flow
Use the Playground to test your triggers with these example prompts:
- `Send a welcome email to user_id: 12345 using the 'New_Signup' template.`
- `Trigger a re-engagement email for user_id: 67890 who has been inactive for 30 days.`
- `Send an onboarding tip email to user_id: 55555 regarding the 'Advanced Analytics' feature.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision engine, mapping events to specific communication strategies.
- Instruction: "Identify the user event and select the correct Moosend template."
- Instruction: "Extract user details from the input to populate email variables."
- Instruction: "Verify email delivery status and report back any errors."

### 2) Composio Toolset Node
- Requires a valid Moosend API key configured within the Composio dashboard.
- Ensure the connection scope includes `campaigns:write` and `subscribers:read` permissions.

### 3) Tool Availability
- **Moosend API**: For managing subscriber lists and triggering email campaigns.
- **Data Parser**: For extracting user IDs and event metadata from incoming payloads.
- **Logger**: For tracking successful sends and handling delivery failures.

---

## Related Solutions
- [Abandoned Cart Recovery Agent (Klaviyo)](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automate recovery sequences for e-commerce platforms.
- [WhatsApp Lead Nurturing Agent (Spoki)](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Multi-channel lead engagement via WhatsApp.
- [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose business process automation.
