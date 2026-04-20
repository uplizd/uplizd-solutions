# User Onboarding Chat Flow (Uplizd) - Automated registration and channel assignment

## Summary
The User Onboarding Chat Flow by Sendbird automates the complex process of welcoming new users, collecting essential profile information, and assigning them to the correct communication channels. By leveraging Uplizd's AI-driven orchestration, this solution eliminates manual data entry, reduces onboarding friction, and ensures that every new user is instantly integrated into your support or community ecosystem, providing a seamless first-time experience.

---

## Demo
![User Onboarding Chat Flow interface showing automated welcome message and profile data collection](image.png)
**Alt text (SEO-ready):** User Onboarding Chat Flow by Sendbird, Uplizd AI workflow, automated user registration, chat-based profile assignment, and onboarding automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bd357d20-c2de-533d-bbc0-e9a4f2c15030)

---

## Category
- **Primary category:** Customer Support Automation
- **Secondary tags:** chat, onboarding, sendbird, user-experience, automation, workflow, ai-agent, customer-success
- This solution bridges the gap between initial user sign-up and active platform engagement through intelligent, automated chat interactions.

---

## Who is this for?
This solution is designed for teams looking to scale their user acquisition and support operations without increasing headcount.

- **Customer Success Managers**
    - Automate the initial welcome sequence to ensure users reach their "Aha!" moment faster.
- **Product Managers**
    - Collect structured user feedback and profile data directly during the onboarding phase.
- **Support Operations Leads**
    - Reduce ticket volume by routing users to the correct support channels based on their specific needs.
- **Growth Marketers**
    - Improve conversion rates by providing personalized, real-time assistance during the critical sign-up window.

---

## Features
- **Automated Welcome Sequences**
    - Instantly trigger personalized greetings and guided tours for new users as soon as they connect.
- **Dynamic Profile Collection**
    - Use AI to query and store user preferences, roles, and interests directly into your CRM.
- **Intelligent Channel Routing**
    - Automatically assign users to specific Sendbird channels based on their intent or subscription tier.
- **Real-time Data Sync**
    - Seamlessly pass onboarding data to external databases or CRM platforms via the Composio Toolset.
- **Error-Resilient Logic**
    - Built-in fallback mechanisms to handle incomplete user inputs or unexpected chat responses gracefully.

---

## Use Cases
**Streamlined User Registration**
- Automatically capture user email, intent, and company size during the first chat interaction.
- Sync collected profile data to your backend system to trigger personalized follow-up emails.

**Smart Channel Assignment**
- Route enterprise users to a dedicated "VIP Support" channel while directing standard users to general help.
- Segment new users into interest-based community channels based on their initial chat responses.

**Proactive Support Triage**
- Identify common onboarding blockers through sentiment analysis and escalate to human agents when necessary.
- Provide instant answers to FAQs regarding account setup to reduce initial support friction.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Configure your Sendbird API credentials within the integration settings.
4. Ensure nodes are correctly mapped and the agent is connected to your target Sendbird instance.

### 2) Setup the Nodes
- **Chat Input**: Receives the initial user message or registration trigger.
- **Agent**: Processes user intent and determines the necessary onboarding steps.
- **Composio Toolset**: Executes API calls to Sendbird for channel assignment and user profile updates.
- **Chat Output**: Delivers the personalized welcome message and confirmation of account status.

### 3) Run the Flow
Use the Playground to test the flow with the following prompts:
- `Hi, I just signed up and need help setting up my profile.`
- `I am an enterprise user looking to join the technical support channel.`
- `What are the next steps to get started with my account?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary orchestrator for the onboarding conversation.
- Maintain a helpful, professional, and welcoming tone.
- Prioritize data collection accuracy while keeping the conversation conversational.
- Use the provided toolset to verify user status before assigning channels.

### 2) Composio Toolset Node
- Ensure your Sendbird API key is active and has permissions for channel management.
- Set the connection scope to allow the agent to read user metadata and write to channel attributes.

### 3) Tool Availability
- `sendbird_list_channels`: Identify available support or community channels.
- `sendbird_create_user_profile`: Update user details in the Sendbird system.
- `sendbird_join_channel`: Assign the user to the appropriate communication channel.

---

## Related Solutions
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) — Automated 24/7 customer support via Botstar.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) — Intelligent ticket triage for WhatsApp support channels.
- [workforce-onboarding-automator-by-connecteam](../workforce-onboarding-automator-by-connecteam/README.md) — Streamline internal employee onboarding workflows.
