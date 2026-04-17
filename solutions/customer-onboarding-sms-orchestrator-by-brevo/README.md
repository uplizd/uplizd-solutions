# Customer Onboarding SMS Orchestrator (Uplizd) - Automated SMS journeys for seamless user activation

## Summary
The Customer Onboarding SMS Orchestrator is an intelligent Uplizd workflow designed to automate personalized SMS communication throughout the critical customer activation phase. By leveraging real-time triggers and the Composio Toolset, this solution ensures that users receive timely tips, documentation links, and progress reminders, significantly reducing churn and accelerating time-to-value for new sign-ups.

---

## Demo
![Customer Onboarding SMS Orchestrator workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Uplizd Customer Onboarding SMS Orchestrator workflow diagram showing automated SMS messaging, Brevo integration, and user activation sequences.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/161aa1bb-1434-5781-b298-181ca13efcee)

---

## Category
**Primary category:** Customer Onboarding
**Secondary tags:** sms, brevo, customer success, automation, user activation, engagement, composio, ai workflow

This solution streamlines the customer lifecycle by automating high-touch SMS interactions that guide users through their initial product experience.

---

## Who is this for?
This workflow is designed for teams focused on improving user retention and reducing onboarding friction through proactive communication.

*   **Customer Success Manager**
    *   Automates personalized check-ins to ensure users reach their "Aha!" moment faster.
*   **Growth Marketer**
    *   Increases activation rates by delivering timely, context-aware SMS tips during the first 48 hours.
*   **Product Operations Lead**
    *   Standardizes the onboarding journey across all new sign-ups without manual intervention.
*   **Support Specialist**
    *   Reduces ticket volume by proactively providing SMS-based documentation and setup guides.

---

## Features
- **Automated SMS Sequencing**
    Trigger personalized SMS messages based on specific user milestones or time-based intervals.
- **Brevo Integration**
    Seamlessly connect with Brevo via the Composio Toolset to manage contact lists and send high-deliverability SMS campaigns.
- **Context-Aware Personalization**
    Utilize the Agent node to tailor message content based on user profile data and previous interaction history.
- **Real-time Engagement Tracking**
    Monitor the effectiveness of onboarding sequences to identify bottlenecks in the user journey.
- **Dynamic Content Delivery**
    Automatically include relevant links, tutorial videos, or support documentation directly within the SMS body.

---

## Use Cases
**Proactive User Activation**
*   Send a "Welcome" SMS with a link to the quick-start guide immediately after account creation.
*   Trigger a follow-up tip if a user has not completed their profile setup within 24 hours.

**Churn Mitigation**
*   Identify users who haven't logged in for 3 days and send a re-engagement SMS with a helpful feature highlight.
*   Send personalized check-ins to users who are stuck on a specific onboarding step.

**Support & Education**
*   Deliver bite-sized "Pro Tips" via SMS to help users discover advanced product features.
*   Provide instant SMS status updates for users awaiting account verification or setup approval.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your dashboard.
3. Connect your Brevo account within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives user event triggers (e.g., "New User Registered").
*   **Agent**: Processes the event and determines the appropriate SMS content.
*   **Composio Toolset**: Executes the SMS dispatch via the Brevo API.
*   **Chat Output**: Confirms the successful delivery of the SMS to the user.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these prompts:
* `Send a welcome SMS to user +15550123456 with the link to our onboarding video.`
* `Check if user +15550123456 has completed setup; if not, send a reminder SMS.`
* `Send a 'Pro Tip' about our dashboard features to the list of new users from today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for your communication strategy.
*   Maintain a helpful, encouraging, and professional tone.
*   Ensure the agent only sends messages when specific criteria (e.g., "not activated") are met.
*   Use clear, concise language suitable for SMS character limits.

### 2) Composio Toolset Node
*   Requires a valid Brevo API Key with SMS and Contact management permissions.
*   Ensure the connection scope allows for reading user status and writing SMS messages.

### 3) Tool Availability
*   **Brevo SMS API**: For sending transactional and promotional messages.
*   **Brevo Contact API**: For retrieving user attributes and segmenting onboarding lists.

---

## Related Solutions
* [Account Health Usage Monitor by Jotform](../account-health-usage-monitor-by-jotform/README.md) - Track user engagement and health metrics.
* [WhatsApp Lead Nurturing Agent by Spoki](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Alternative messaging channel for lead engagement.
* [Admin User Onboarding Assistant by Storeganise](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamline administrative user setup workflows.
