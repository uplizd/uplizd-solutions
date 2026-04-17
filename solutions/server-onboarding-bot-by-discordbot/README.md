# Server Onboarding Bot (Uplizd) - Automated member welcome and role assignment workflow

## Summary
The Server Onboarding Bot is an intelligent automation workflow designed to streamline the new member experience by automating welcome messages, role assignments, and initial community orientation. By leveraging the Composio Toolset to interface with Discord, this solution eliminates manual administrative overhead, ensures consistent onboarding protocols, and improves member retention through immediate, personalized engagement.

---

## Demo
![Server Onboarding Bot workflow interface showing Discord integration nodes and automated welcome sequence](image.png)
**Alt text (SEO-ready):** Server Onboarding Bot Uplizd workflow, automated Discord member welcome and role assignment integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/243f7436-a571-5933-9cd1-6f7011e8391b)

---

## Category
**Community Operations**
- `discord`, `onboarding`, `automation`, `community management`, `role assignment`, `member engagement`, `composio`, `ai workflow`
This solution optimizes community growth by automating repetitive administrative tasks and ensuring every new member receives a structured, welcoming introduction.

---

## Who is this for?
This solution is designed for community leaders and administrators who need to scale their server management without sacrificing the quality of the member experience.

- **Community Managers**
    - Automate the delivery of welcome resources and community guidelines to every new joiner.
- **Discord Server Admins**
    - Reduce manual moderation time by automating role assignments based on user interaction.
- **Growth Marketers**
    - Improve member retention rates by ensuring an immediate and professional first point of contact.
- **Operations Leads**
    - Standardize the onboarding process across multiple servers to maintain consistent community hygiene.

---

## Features
- **Automated Welcome Messaging**
    - Sends personalized greetings to new members immediately upon joining the server.
- **Dynamic Role Assignment**
    - Automatically assigns specific roles based on user input or pre-defined onboarding criteria.
- **Composio-Powered Discord Integration**
    - Utilizes secure API connections to interact with Discord channels and member data in real-time.
- **Customizable Onboarding Paths**
    - Allows for conditional logic to guide members through different onboarding tracks based on their interests.
- **Real-time Member Tracking**
    - Monitors onboarding progress to ensure no new member is left without a proper introduction.

---

## Use Cases
**Community Welcome Sequences**
- Automatically trigger a welcome message containing server rules and FAQ links.
- Assign a "New Member" role to restrict access until the user acknowledges the community guidelines.

**Role-Based Access Control**
- Assign specific interest-based roles automatically when a user selects preferences during onboarding.
- Update member permissions dynamically as they complete the initial orientation flow.

**Administrative Efficiency**
- Log new member join events to a secondary database or spreadsheet for community analytics.
- Notify human moderators when a new member requires manual assistance or verification.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your Discord account via the Composio Toolset node.
4. Ensure nodes are correctly mapped from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the new member join event trigger from Discord.
- **Agent**: Processes the member data and determines the appropriate welcome or role assignment action.
- **Composio Toolset**: Executes the API calls to Discord to update roles or send messages.
- **Chat Output**: Confirms the successful completion of the onboarding task to the server logs.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these example prompts:
- `Send a welcome message to the new user with ID 12345 and assign the 'Member' role.`
- `Check if the new user has completed the rules acknowledgment and assign the 'Verified' role.`
- `Post a welcome message in the #general channel for the user who just joined.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for your community interactions.
- Use a concise, welcoming tone for all automated messages.
- Define clear conditional rules for role assignment based on user attributes.
- Ensure the agent is instructed to verify user permissions before executing administrative actions.

### 2) Composio Toolset Node
- Provide your Discord API credentials within the Composio dashboard.
- Ensure the connection scope includes `Manage Roles` and `Send Messages` permissions.

### 3) Tool Availability
- **Discord Member Management**: Capabilities for adding/removing roles and updating nicknames.
- **Discord Messaging**: Capabilities for sending channel messages and direct messages.
- **Event Listeners**: Capabilities for monitoring member join and leave events.

---

## Related Solutions
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Automated support responses for community inquiries.
- [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Monitor the health and activity of your automated workflows.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Triage and manage support tickets across messaging platforms.
