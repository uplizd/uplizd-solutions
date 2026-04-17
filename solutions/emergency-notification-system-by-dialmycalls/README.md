# Emergency Notification System (Uplizd) - Automated critical incident alerting and stakeholder communication

## Summary
The Emergency Notification System by DialMyCalls is an automated AI workflow designed to streamline incident response by instantly broadcasting critical alerts to stakeholders across multiple channels. By integrating real-time communication triggers with the Composio Toolset, this solution ensures that urgent updates reach the right people immediately, reducing downtime and improving organizational transparency during high-stakes events.

---

## Demo
![Emergency Notification System workflow dashboard showing incident trigger and multi-channel alert distribution](image.png)
**Alt text (SEO-ready):** Emergency Notification System workflow by Uplizd and DialMyCalls for automated incident alerting, stakeholder communication, and real-time notification management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhL7c5BDQAwDAOx/64+Mh+gQoIEe+y9A0mSJEiSpP8uSZIkeQ9JkiRJkiRJkiRJkiRJkiRJkiRJkiRJkvwVvQG35wE/9+w6YgAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/835fa010-5cd8-524b-b2f9-44f85cd1dd2b)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** incident response, emergency alerts, dialmycalls, communication automation, crisis management, composio, ai workflow, stakeholder notification.
This solution bridges the gap between incident detection and rapid team mobilization through automated multi-channel messaging.

---

## Who is this for?
This workflow is designed for teams responsible for maintaining uptime and clear communication during critical business disruptions.

- **Operations Manager**
    - Automates the dissemination of emergency protocols to prevent manual communication bottlenecks.
- **IT Support Lead**
    - Ensures rapid notification of technical outages to relevant engineering and support staff.
- **Crisis Communications Officer**
    - Maintains consistent messaging across voice, SMS, and email during organizational emergencies.
- **Facility Administrator**
    - Triggers site-wide safety alerts and status updates to all personnel in real-time.

---

## Features
- **Multi-Channel Broadcasting**
    - Simultaneously push alerts via SMS, voice calls, and email to ensure high-priority messages are seen.
- **Automated Incident Triggers**
    - Connects directly to monitoring tools to initiate notification sequences the moment an incident is detected.
- **Stakeholder Group Management**
    - Dynamically targets specific contact lists based on the severity or type of the incident.
- **Real-Time Delivery Tracking**
    - Monitors the status of sent notifications to confirm receipt and identify communication gaps.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interface with DialMyCalls APIs for reliable message dispatching.

---

## Use Cases
**Critical Infrastructure Outages**
- Automatically alert on-call engineering teams when server monitoring detects a service disruption.
- Broadcast status updates to internal stakeholders until the incident is marked as resolved.

**Emergency Safety Protocols**
- Trigger immediate voice alerts to all staff during facility-wide safety or security incidents.
- Send follow-up SMS instructions to ensure personnel follow established evacuation or lockdown procedures.

**Operational Crisis Management**
- Notify department heads of supply chain or logistics failures that require immediate decision-making.
- Coordinate cross-functional response teams by sending synchronized alerts across multiple communication platforms.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the Emergency Notification System workflow.
3. Connect your DialMyCalls API credentials within the integration settings.
4. Ensure nodes are correctly mapped to your preferred communication contact lists and trigger conditions.

### 2) Setup the Nodes
- **Chat Input**: Receives the incident details, severity level, and target audience group from the user.
- **Agent**: Analyzes the incident data and determines the appropriate notification template and channel priority.
- **Composio Toolset**: Executes the API calls to DialMyCalls to dispatch SMS, voice, or email alerts.
- **Chat Output**: Confirms the successful delivery of notifications and provides a summary of the incident response status.

### 3) Run the Flow
Use the Playground to test your notification triggers:
- `Alert the IT Support team: Server cluster 4 is experiencing 500 errors, send SMS and voice call.`
- `Send an emergency update to the Operations list: Facility maintenance scheduled for 2 PM has been delayed.`
- `Notify the Crisis Management group: Urgent security alert regarding unauthorized access in Zone B.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the incident commander, interpreting natural language input into structured API commands.
- **Recommended instruction pattern:**
    - Always verify the severity level before selecting the notification channel.
    - Use the provided contact list IDs to ensure alerts reach the correct stakeholder groups.
    - Maintain a professional, urgent tone in all outgoing message templates.

### 2) Composio Toolset Node
- **API Key**: Input your DialMyCalls API Key to authorize the workflow.
- **Connection Scope**: Ensure the agent has permission to access contact lists and trigger broadcast endpoints.

### 3) Tool Availability
- **Broadcast Dispatcher**: Sends mass notifications across selected channels.
- **Contact List Manager**: Retrieves and filters stakeholder contact information.
- **Delivery Status Monitor**: Queries the status of sent messages for audit logs.

---

## Related Solutions
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational health of your automated workflows.
- [../247-customer-support-voice-agent-by-bolna/README.md](../247-customer-support-voice-agent-by-bolna/README.md) - Deploy 24/7 voice-based support for customer inquiries.
- [../workplace-risk-early-warning-system-by-faceup/README.md](../workplace-risk-early-warning-system-by-faceup/README.md) - Proactively identify and manage workplace risks.
