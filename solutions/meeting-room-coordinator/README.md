# Meeting Room Coordinator (Uplizd) - Automate Office Scheduling & Bookings

## Summary
The Meeting Room Coordinator is an Uplizd AI workflow designed to streamline office management by automating room bookings and conflict resolution directly within Slack. By leveraging real-time data from your calendar and Slack environment, it eliminates manual scheduling friction, ensures optimal space utilization, and provides a seamless, self-service experience for employees.

---

## Demo

![Uplizd Meeting Room Coordinator flow managing Slack bookings and resolving room conflicts](image.png)

**Alt text (SEO-ready):** Uplizd Meeting Room Coordinator integrating Slackbot toolsets to automate office scheduling, booking notifications, and meeting room conflict resolution.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/31b18695-cee2-51d8-b510-a8c612b15b4b/)

---

## Category

**Primary category:** Workplace Operations

**Secondary tags:** slack, office management, scheduling, automation, booking, facility management, composio, ai workflow

This solution bridges the gap between conversational chat interfaces and physical office infrastructure to automate administrative scheduling tasks.

---

## Who is this for?

This workflow is built for workplace operations and administrative teams who want to eliminate the manual overhead of room management:

- **Office Managers & Facility Leads**
    - Scalably manage multiple meeting rooms across different floors or locations without constant manual oversight.
- **Administrative Assistants**
    - Free up time spent on the back-and-forth of coordinating room availability and handling last-minute cancellations.
- **Team Leads & Project Managers**
    - Ensure your team always has a space to collaborate without the frustration of double-bookings or "meeting room hopping."
- **Workplace Experience Teams**
    - Provide a modern, frictionless self-service booking experience for all employees within their existing Slack workflow.

---

## Features

- **Natural Language Booking Monitoring**
  Continuously scans designated Slack channels for booking requests, converting chat into confirmed events.

- **Proactive Conflict Detection**
  Instantly identifies double-bookings and suggests the best available alternatives, including different rooms or nearby time slots.

- **Automated Lifecycle Communication**
  Handles all confirmations, attendee alerts, and cancellation notifications via integrated messaging tools.

- **Smart Reminders & Reducing "No-Shows"**
  Automatically sets meeting reminders to notify organizers 15 minutes before the start time to ensure high attendance.

- **Immediate Visual Feedback**
  Uses status emojis and reactions to acknowledge requests with clear indicators like ✅ Confirmed or ⚠️ Conflict.

---

## Use Cases

**Self-Service Office Booking**
- Employees can book rooms without leaving Slack, receiving instant confirmation and dial-in details.
- Reduce the "shadow IT" problem of employees using rooms without formal booking.

**Conflict-Free Rescheduling**
- When a scheduling overlap is detected, the bot provides actionable alternatives, allowing the user to resolve the issue with one click.
- Automate the notification process to all affected parties when a meeting is moved or cancelled.

**Efficient Room Reclamation**
- When meeting cancellations are processed, the bot immediately notifies the channel that a room has opened up.
- Maximize office space utilization by automatically releasing unused rooms back into the available pool.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected correctly: Chat Input, Agent, Composio Toolset, and Chat Output.

### 2) Setup the Nodes
- **Chat Input** → Receives human booking requests or cancellation alerts.
- **Agent** → Coordinates the management workflow (Monitoring, Detection, Confirmation, and Reminders).
- **Composio Toolset** → Provides the interface for Slack messaging, calendar operations, and channel management.
- **Chat Output** → Summarizes the coordination actions and provides final booking details.

### 3) Run the Flow
1. Click **Playground** to open the Chat Interface.
2. Enter a request such as:
   - `"Book the Quiet Room at 3pm today for a 1-hour brainstorming session"`
   - `"Is the Boardroom free tomorrow morning?"`
   - `"Cancel my 4pm booking in the Gallery"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is pre-configured with a specialized workflow for facility management and professional communication.
- Maintain a helpful, polite, and efficient tone.
- Prioritize conflict resolution to save time for administration teams.
- Ensure all confirmation messages include clear location and time details.

### 2) Composio Toolset Node
Requires your **Composio API Key** and a synchronized connection to your **Slackbot** instance with appropriate permissions for messaging and channel creation.

### 3) Tool Availability
- Message posting and reactions
- Reminder management
- Private and public channel creation

---

## Related Solutions

* [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md)  
  Streamline new hire setup and group assignments for deskless workers.
* [Team Productivity Monitor](../team-productivity-monitor/README.md)  
  Analyze team performance and identify productivity patterns across workspaces.
* [CRM Data Sync Manager](../crm-data-sync-manager/README.md)  
  Orchestrate and monitor data flows across your entire enterprise tech stack.
