# School Closure Announcer (Uplizd) - Automated emergency notification and school status alerts

## Summary
The School Closure Announcer is an intelligent Uplizd workflow that streamlines emergency communication by automating notifications to parents, students, and staff. By integrating directly with DialMyCalls, this solution ensures that critical updates regarding school closures, delays, or emergency alerts are disseminated instantly across voice, SMS, and email, reducing administrative burden and ensuring 100% reach during time-sensitive events.

---

## Demo
![School Closure Announcer workflow diagram showing Chat Input, Agent, DialMyCalls toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** School Closure Announcer workflow on Uplizd, automating emergency notifications via DialMyCalls for school districts and educational institutions.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/a35ebc9b-5a9a-5513-ba35-57405dcd4628)

---

## Category
**Primary category:** Operations
**Secondary tags:** school administration, emergency alert, dialmycalls, automated messaging, crisis communication, notification system, composio, ai workflow.
This solution bridges the gap between administrative decision-making and rapid community outreach through automated communication channels.

---

## Who is this for?
This workflow is designed for educational administrators and communications teams who need to manage high-stakes information flow during unpredictable events.

* **School Administrators**
    * Rapidly deploy district-wide closure notices without manual calling trees.
* **Communications Directors**
    * Ensure consistent messaging across voice, SMS, and email platforms during emergencies.
* **Operations Managers**
    * Maintain operational continuity by automating status updates for staff and faculty.
* **IT/Support Staff**
    * Reduce technical overhead by using pre-configured AI-driven notification triggers.

---

## Features
- **Multi-Channel Delivery**
    Leverage DialMyCalls to broadcast alerts simultaneously via voice calls, text messages, and email.
- **Intelligent Message Drafting**
    Use the Agent node to generate clear, professional, and urgent closure notifications based on simple input.
- **Real-Time Execution**
    Trigger notifications immediately upon input, ensuring the community receives updates the moment a decision is made.
- **Composio Integration**
    Seamlessly connect the Uplizd workflow to your DialMyCalls account for secure and authenticated message dispatching.
- **Audit-Ready Logging**
    Capture all sent notifications through the Chat Output to maintain a record of emergency communications for compliance.

---

## Use Cases
**Emergency Crisis Management**
* Sending immediate district-wide alerts during severe weather events or power outages.
* Notifying specific school zones of localized incidents requiring immediate attention.

**Scheduled Operational Updates**
* Automating reminders for early dismissal days or planned maintenance closures.
* Managing staff-only notifications for professional development days or emergency meetings.

**Community Outreach**
* Distributing non-emergency school event reminders to parent contact lists.
* Providing status updates on school bus delays or transportation disruptions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the template in the Uplizd builder.
2. Connect your DialMyCalls API credentials within the Composio Toolset node.
3. Configure your target contact groups or phone lists in the DialMyCalls dashboard.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the closure details, school name, and urgency level.
* **Agent**: Processes the input and formats the notification content for the broadcast.
* **Composio Toolset**: Executes the API call to DialMyCalls to initiate the notification broadcast.
* **Chat Output**: Confirms the successful dispatch of the alert to the designated audience.

### 3) Run the Flow
Use the Playground to test your alerts:
* `Send an emergency alert to the 'All Parents' group: School is closed tomorrow due to heavy snow.`
* `Notify the 'Staff' group that the school will have a 2-hour delay starting at 10:00 AM.`
* `Broadcast a message to 'High School' group: All after-school activities are canceled today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the communication coordinator, ensuring tone and clarity.
* Maintain a professional, urgent, and empathetic tone suitable for emergency alerts.
* Extract key variables (School Name, Time, Reason) from the user's natural language input.
* Ensure the output strictly adheres to the parameters required by the DialMyCalls API.

### 2) Composio Toolset Node
* Requires a valid DialMyCalls API key.
* Connection scope should be set to "Broadcast" or "Messaging" to allow the agent to trigger alerts.

### 3) Tool Availability
* `dialmycalls_send_broadcast`: Triggers the multi-channel notification.
* `dialmycalls_get_contact_groups`: Retrieves available lists for targeted messaging.
* `dialmycalls_get_account_balance`: Monitors credit usage for high-volume alerts.

---

## Related Solutions
* [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Advanced voice-based customer support automation.
* [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Automated support ticket triage and management.
* [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlining operational workflows for service-based businesses.
