# WhatsApp Campaign Manager (Uplizd) - Automate and scale personalized messaging campaigns

## Summary
The WhatsApp Campaign Manager by Landbot is an intelligent automation workflow designed to streamline the deployment, management, and tracking of marketing campaigns across WhatsApp. By leveraging the Composio Toolset to interface with Landbot, this solution enables marketing teams to maintain high engagement rates, ensure timely message delivery, and achieve consistent pipeline velocity through automated, data-driven communication.

---

## Demo
![WhatsApp Campaign Manager workflow interface showing Landbot integration nodes and automated message flow](image.png)
**Alt text (SEO-ready):** WhatsApp Campaign Manager workflow automation, Landbot integration, Uplizd marketing campaign orchestration, automated messaging pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8d97e326-145e-5a3e-a347-ee7996e43dbc)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** whatsapp, landbot, campaign management, marketing automation, customer engagement, lead nurturing, composio, ai workflow
- This solution bridges the gap between marketing strategy and execution by automating the delivery of personalized WhatsApp campaigns via Landbot.

---

## Who is this for?
This solution is designed for teams looking to optimize their conversational marketing efforts and reduce manual outreach overhead.

- **Marketing Manager**
    - Automates the scheduling and execution of multi-stage WhatsApp marketing campaigns.
- **Growth Marketer**
    - Increases conversion rates by delivering personalized, timely messages to segmented leads.
- **Customer Success Lead**
    - Ensures consistent communication touchpoints throughout the customer lifecycle.
- **Sales Operations Specialist**
    - Maintains data hygiene by syncing campaign interaction logs directly into the CRM.

---

## Features
- **Automated Campaign Deployment**
    - Trigger and manage WhatsApp message sequences directly through the Uplizd workflow engine.
- **Dynamic Personalization**
    - Inject CRM data into message templates to ensure every interaction feels tailored to the recipient.
- **Real-time Interaction Tracking**
    - Capture delivery and engagement metrics automatically to refine future campaign performance.
- **Landbot Integration**
    - Utilize the Composio Toolset to securely authenticate and execute commands within the Landbot platform.
- **Scalable Message Queuing**
    - Handle high-volume outreach without manual intervention, ensuring consistent delivery windows.

---

## Use Cases
**Campaign Orchestration**
- Automate the launch of product announcement sequences to segmented user lists.
- Schedule follow-up messages based on user interaction triggers within the Landbot ecosystem.

**Lead Nurturing**
- Deploy personalized drip campaigns to move prospects through the sales funnel via WhatsApp.
- Trigger re-engagement messages for inactive leads based on specific time-window criteria.

**Performance Optimization**
- Aggregate campaign response data to identify high-performing message templates.
- Sync engagement status back to your primary database for real-time reporting and analysis.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import to Workspace" to load the workflow into your Uplizd dashboard.
3. Connect your Landbot API credentials within the Composio Toolset node.
4. Ensure nodes are correctly mapped and all required environment variables are configured before activation.

### 2) Setup the Nodes
- **Chat Input**: Accepts campaign parameters, target audience segments, and message content triggers.
- **Agent**: Processes the campaign logic, determines the optimal delivery time, and personalizes content.
- **Composio Toolset**: Executes the API calls to Landbot to push messages and retrieve interaction status.
- **Chat Output**: Confirms successful campaign deployment and logs any delivery errors for review.

### 3) Run the Flow
Use the Uplizd Playground to test your campaign logic with these example prompts:
- `Launch the 'Summer Sale' campaign template to the 'Active Leads' segment.`
- `Send a personalized follow-up message to all users who clicked the link in the last 24 hours.`
- `Retrieve the delivery status report for the most recent WhatsApp broadcast.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the campaign strategist, interpreting marketing goals and mapping them to specific Landbot actions.
- Use a clear, instruction-based prompt to define campaign constraints.
- Enable structured output to ensure the Composio Toolset receives valid JSON parameters.
- Set the temperature to a lower value (0.2–0.3) for consistent, reliable campaign execution.

### 2) Composio Toolset Node
- Provide your Landbot API key to authorize the workflow.
- Define the connection scope to allow the agent to read campaign templates and send messages.

### 3) Tool Availability
- **Template Retrieval**: Access and validate available WhatsApp marketing templates.
- **Message Dispatch**: Send individual or bulk messages to target phone numbers.
- **Analytics Fetching**: Query interaction logs to track delivery and read status.

---

## Related Solutions
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Automate lead follow-ups and nurturing sequences.
- [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) — Route incoming support queries to the appropriate team.
- [WhatsApp Order Status Tracker](../whats-app-order-status-tracker-by-timelinesai/README.md) — Provide real-time shipping and order updates to customers.
