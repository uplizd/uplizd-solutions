# Team Recognition Amplifier (Uplizd) - Automate team morale and kudos distribution

## Summary
The Team Recognition Amplifier is an intelligent Uplizd workflow designed to boost team morale by automating the identification, drafting, and distribution of peer-to-peer recognition. By integrating with communication platforms via the Composio Toolset, this solution ensures consistent team appreciation, reducing management overhead while fostering a culture of gratitude and high engagement.

---

## Demo
![Team Recognition Amplifier workflow showing automated kudos generation and distribution](image.png)
**Alt text (SEO-ready):** Team Recognition Amplifier Uplizd workflow for automated kudos, employee morale boosting, and team engagement via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/991ead1c-d7dc-5a95-b5b0-23ba7d009b61)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** team engagement, morale, automation, kudos, culture, internal communications, composio, ai workflow
- This solution streamlines internal culture building by automating the recognition lifecycle, ensuring every contribution is acknowledged.

---

## Who is this for?
This solution is designed for leaders and HR professionals focused on maintaining high team engagement and positive workplace culture.

- **People Managers**
    - Automate the process of acknowledging team milestones and individual contributions without manual tracking.
- **HR Business Partners**
    - Standardize recognition programs across distributed teams to ensure equitable and frequent positive feedback.
- **Team Leads**
    - Foster a culture of appreciation that improves retention and boosts overall team morale.
- **Operations Managers**
    - Integrate recognition workflows into existing communication channels to maintain high-velocity team engagement.

---

## Features
- **Automated Kudos Drafting**
    - Uses AI to generate personalized, meaningful recognition messages based on specific project achievements.
- **Multi-Channel Distribution**
    - Seamlessly pushes recognition messages to Slack, Microsoft Teams, or email via the Composio Toolset.
- **Milestone Tracking**
    - Automatically identifies work anniversaries, project completions, and goal attainment for timely praise.
- **Sentiment-Aware Messaging**
    - Ensures all generated messages align with company tone and values for authentic team interaction.
- **Engagement Analytics**
    - Tracks recognition frequency to ensure balanced participation and identify team members who deserve extra spotlight.

---

## Use Cases
**Peer-to-Peer Recognition**
- Automatically trigger a kudos message when a team member completes a task in a project management tool.
- Facilitate a "shout-out" channel where employees can submit raw notes that the agent refines into professional praise.

**Milestone Celebrations**
- Send automated, personalized congratulatory messages for work anniversaries or internal promotions.
- Coordinate team-wide recognition for hitting quarterly KPIs or major product launch milestones.

**Culture & Engagement Audits**
- Generate weekly reports on recognition activity to identify teams that may need more engagement support.
- Monitor the distribution of kudos to ensure all departments receive equitable recognition for their efforts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the Team Recognition Amplifier JSON configuration file.
3. Connect your required communication and project management accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw recognition data or trigger events from your project management system.
- **Agent**: Processes input, applies tone-of-voice instructions, and drafts the recognition message.
- **Composio Toolset**: Executes the delivery of the message to the designated team communication channel.
- **Chat Output**: Confirms successful delivery and logs the recognition event for future analytics.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Draft a congratulatory message for Sarah for completing the Q3 migration project ahead of schedule.`
- `Send a kudos message to the design team for their work on the new brand identity.`
- `Identify upcoming work anniversaries for the engineering team and draft personalized recognition notes.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a culture-focused copywriter.
- Use a professional yet warm tone consistent with your company culture.
- Instruct the agent to highlight specific contributions rather than generic praise.
- Ensure the agent maintains a neutral and inclusive perspective in all generated content.

### 2) Composio Toolset Node
- Provide the necessary API keys for your communication platforms (e.g., Slack, Teams).
- Set the connection scope to allow the agent to post messages to specific channels or direct messages.

### 3) Tool Availability
- **Messaging APIs**: Capability to post to public channels or individual DMs.
- **Project Management Connectors**: Ability to read task completion status and project metadata.
- **Calendar/HRIS Integrations**: Access to milestone dates and team member details.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize your internal operational workflows.
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Streamline new hire integration and documentation.
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automate session planning and team collaboration activities.
