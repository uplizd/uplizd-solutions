# Event Update Broadcaster (Uplizd) - Real-time event communication and attendee notification

## Summary
The Event Update Broadcaster is an automated workflow designed to streamline event management by instantly pushing schedule changes, venue updates, or urgent announcements to attendees. By leveraging the DialMyCalls integration, this solution ensures that critical information reaches participants via SMS or voice broadcast, reducing manual communication overhead and ensuring high message visibility for event organizers and operations teams.

---

## Demo
![Event Update Broadcaster workflow showing Chat Input, Agent, DialMyCalls toolset, and Chat Output nodes](image.png)

**Alt text (SEO-ready):** Event Update Broadcaster workflow in Uplizd using DialMyCalls for real-time attendee notifications and automated event updates.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ac473e19-be73-5544-a69c-5690e5f26f16)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** event management, dialmycalls, notifications, sms marketing, real-time communication, workflow automation, attendee engagement, composio
- This solution bridges the gap between event management platforms and mass communication tools to ensure seamless attendee coordination.

---

## Who is this for?
This workflow is designed for professionals managing large-scale events who need to maintain clear communication channels under pressure.

- **Event Coordinators**
    - Automate the dissemination of schedule changes to prevent attendee confusion.
- **Operations Managers**
    - Ensure critical venue or logistics updates are delivered instantly to all registered participants.
- **Customer Success Leads**
    - Improve attendee satisfaction by providing proactive, real-time communication during live events.
- **Marketing Managers**
    - Utilize SMS and voice broadcasts to drive engagement and event participation through timely reminders.

---

## Features
- **Real-time Broadcast Engine**
    - Instantly trigger SMS or voice messages to attendee lists via the DialMyCalls integration.
- **Dynamic Content Personalization**
    - Automatically inject event-specific details into outgoing messages using AI-driven templates.
- **Multi-Channel Delivery**
    - Choose between voice or text delivery methods based on the urgency and nature of the event update.
- **Automated List Management**
    - Seamlessly pull contact information from your CRM or event database to ensure the right audience receives the update.
- **Delivery Status Tracking**
    - Monitor the success of your broadcasts directly through the workflow to ensure high reach and engagement.

---

## Use Cases
**Urgent Schedule Adjustments**
- Notify attendees immediately if a keynote speaker is delayed or a session room has changed.
- Send last-minute venue updates to ensure participants arrive at the correct location without delay.

**Event Engagement & Reminders**
- Send automated "15 minutes until start" reminders to boost session attendance.
- Broadcast exclusive event offers or networking opportunities to attendees via SMS during the event.

**Logistics & Operational Alerts**
- Communicate emergency weather or safety protocols to all event participants simultaneously.
- Provide parking or shuttle service updates to manage attendee flow during high-traffic periods.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Connect your DialMyCalls account within the Composio Toolset node.
3. Configure your attendee contact lists and message templates in the Agent node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the event update details or trigger command.
- **Agent**: Processes the update and formats the message for the target audience.
- **Composio Toolset**: Executes the broadcast via the DialMyCalls API.
- **Chat Output**: Confirms the broadcast status and provides a summary of sent notifications.

### 3) Run the Flow
Use the Playground to test your broadcasts with prompts like:
- `Send an SMS to the 'Morning Session' list: 'The keynote has been moved to Hall B due to high attendance.'`
- `Broadcast a voice message to all attendees: 'Reminder: The networking mixer starts in 30 minutes at the main lobby.'`
- `Notify the 'VIP' group: 'Your exclusive workshop session is now starting in Room 204.'`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the communication orchestrator, ensuring tone and clarity.
- Maintain a professional and urgent tone for operational updates.
- Ensure all placeholders in templates are correctly mapped to dynamic event data.
- Validate that the message length adheres to SMS character limits when applicable.

### 2) Composio Toolset Node
- Provide your DialMyCalls API key to authorize the workflow.
- Set the connection scope to allow the agent to read contact lists and initiate broadcasts.

### 3) Tool Availability
- **List Retrieval**: Fetch existing attendee groups from DialMyCalls.
- **SMS Broadcast**: Send text-based updates to selected contact lists.
- **Voice Broadcast**: Initiate automated voice calls for critical announcements.
- **Delivery Reporting**: Query the status of sent messages to confirm reach.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automated voice support for handling customer inquiries.
- [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Manage support tickets via WhatsApp for improved response times.
- [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline business processes and task management across platforms.
