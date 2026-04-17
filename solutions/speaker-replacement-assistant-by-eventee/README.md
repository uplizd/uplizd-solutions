# Speaker Replacement Assistant (Uplizd) - Automate event speaker discovery and booking

## Summary
The Speaker Replacement Assistant is an intelligent Uplizd workflow designed to minimize event disruption by automating the search, vetting, and outreach process for replacement speakers. By leveraging real-time data and AI-driven matching, event managers can instantly identify qualified candidates when cancellations occur, ensuring pipeline velocity for event programming and maintaining high-quality session delivery.

---

## Demo
![Speaker Replacement Assistant workflow showing automated speaker search and booking integration](image.png)
**Alt text (SEO-ready):** Speaker Replacement Assistant Uplizd workflow, automated speaker discovery, event management AI, Composio integration for speaker outreach, and session booking automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/02f3c299-a02f-570a-a341-e639c42afe48)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** event management, speaker sourcing, automation, workflow, ai agent, scheduling, composio, booking
- This solution streamlines event operations by connecting your speaker database with automated outreach tools to handle last-minute scheduling changes.

---

## Who is this for?
This solution is designed for event professionals and operations teams who need to maintain event quality under pressure.

- **Event Manager**
    - Automates the tedious process of sourcing and vetting replacement speakers during last-minute cancellations.
- **Conference Organizer**
    - Ensures session schedules remain intact and high-quality content delivery is maintained without manual intervention.
- **Operations Lead**
    - Reduces the administrative burden of manual outreach and contract coordination for speaker logistics.
- **Community Manager**
    - Quickly identifies subject matter experts within existing networks to fill speaker slots and maintain audience engagement.

---

## Features
- **Automated Speaker Matching**
    - Uses AI to scan your speaker database and professional networks to find candidates matching specific session topics.
- **Real-time Outreach**
    - Leverages the Composio Toolset to trigger personalized emails or messages to potential speakers instantly.
- **Availability Sync**
    - Cross-references speaker calendars and event time slots to ensure zero scheduling conflicts.
- **Vetting & Qualification**
    - Automatically summarizes speaker profiles and past performance data for quick review by the event team.
- **Seamless Booking Integration**
    - Updates event management software and session agendas automatically once a replacement is confirmed.

---

## Use Cases
**Emergency Speaker Sourcing**
- Automatically trigger a search for speakers with expertise in "Cloud Computing" when a keynote speaker cancels within 48 hours.
- Generate a shortlist of available speakers based on previous event attendance and feedback scores.

**Outreach & Coordination**
- Send automated, personalized invitation sequences to identified candidates via integrated communication platforms.
- Track outreach status and follow-up reminders directly within the workflow to ensure timely responses.

**Event Logistics Management**
- Update the event session description and speaker bio fields automatically upon successful booking confirmation.
- Notify the production team of the speaker change and trigger an automated request for the new speaker's presentation assets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Speaker Replacement Assistant.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your required CRM or event management platform via the Composio integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the session details and cancellation notification.
- **Agent**: Analyzes the requirements and executes the search logic.
- **Composio Toolset**: Connects to your speaker database and communication channels to perform outreach.
- **Chat Output**: Delivers a summary of the identified candidates and their current outreach status.

### 3) Run the Flow
Use the Playground to test the agent with prompts like:
- `Find a replacement speaker for the 'AI in Healthcare' session who has spoken at our events before.`
- `Search for experts in 'Sustainable Tech' and send an initial outreach email to the top 3 candidates.`
- `Check the status of current speaker outreach for the upcoming Q3 conference.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary decision-maker for speaker vetting and outreach strategy.
- **Role:** Act as a professional Event Operations Coordinator.
- **Instruction Pattern:**
    - Prioritize candidates with high historical feedback scores.
    - Maintain a professional and urgent tone in all outreach communications.
    - Only suggest candidates who have confirmed availability for the specific session time slot.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable secure connections.
- **Connection Scope:** Ensure the agent has read/write access to your speaker database and email/messaging platforms.

### 3) Tool Availability
- **Speaker Database Access:** Query and filter speaker profiles by expertise and availability.
- **Communication APIs:** Send automated emails or messages to potential candidates.
- **Calendar Integration:** Verify speaker availability against the event schedule.
- **CRM/Event Management:** Update session metadata and speaker records.

---

## Related Solutions
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Manage collaborative session logistics and participant engagement.
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline the onboarding of new event staff and support personnel.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather detailed intelligence on potential speakers or industry experts.
