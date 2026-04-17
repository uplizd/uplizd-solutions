# Incident Alert Dispatcher (Uplizd) - Automated real-time incident notification and team routing

## Summary
The Incident Alert Dispatcher (Uplizd) is an intelligent automation workflow designed to bridge the gap between system monitoring and team response. By leveraging the Composio Toolset to integrate with Pushbullet, this solution automatically routes critical system alerts to the right team members, ensuring reduced mean time to acknowledge (MTTA) and maintaining operational continuity through proactive, real-time communication.

---

## Demo
![Incident Alert Dispatcher workflow showing system monitoring integration and Pushbullet notification routing](image.png)

**Alt text (SEO-ready):** Incident Alert Dispatcher workflow in Uplizd, featuring automated system monitoring, Pushbullet notification routing, and real-time incident management for DevOps and IT teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-43b641a2--afb2--554b--9cef--23ad2e2c43ec-blue)](https://uplizd.ai/solutions/43b641a2-afb2-554b-9cef-23ad2e2c43ec)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** incident management, pushbullet, devops, alert routing, automation, real-time, composio, system monitoring
- This solution streamlines incident response by automating the delivery of critical system alerts to mobile and desktop devices.

---

## Who is this for?
This solution is designed for technical teams that require immediate visibility into system health and rapid incident response.

- **DevOps Engineer**
    - Automate the escalation of critical server errors to ensure zero-latency response times.
- **Site Reliability Engineer (SRE)**
    - Reduce alert fatigue by filtering and routing only high-priority system incidents to relevant channels.
- **IT Operations Manager**
    - Maintain a centralized audit trail of incident alerts and team notifications for post-mortem analysis.
- **System Administrator**
    - Receive instant push notifications for unauthorized access attempts or resource threshold breaches.

---

## Features
- **Real-time Alert Routing**
    - Instantly dispatches system alerts via Pushbullet to ensure stakeholders are notified the moment an incident occurs.
- **Intelligent Filtering**
    - Uses the Agent node to parse incoming logs and prioritize alerts based on severity levels.
- **Multi-Platform Delivery**
    - Seamlessly pushes notifications across mobile and desktop devices connected to the Pushbullet ecosystem.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely manage API connections and execute notification commands.
- **Automated Escalation Logic**
    - Configurable logic to route different incident types to specific team members or on-call groups.

---

## Use Cases
**Critical System Outages**
- Automatically dispatch alerts when server CPU or memory usage exceeds predefined safety thresholds.
- Notify the on-call engineer immediately if a primary database connection fails or becomes unresponsive.

**Security and Access Monitoring**
- Send instant push notifications when unauthorized login attempts are detected on sensitive administrative accounts.
- Alert security teams regarding unexpected changes to firewall configurations or security group policies.

**Operational Workflow Updates**
- Notify the product team when a deployment pipeline fails during the staging or production release process.
- Dispatch status updates to stakeholders when long-running batch jobs complete or encounter unexpected errors.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and import the Incident Alert Dispatcher workflow.
3. Connect your Pushbullet account within the Composio Toolset configuration.
4. Ensure nodes are correctly mapped from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw system alert data or monitoring trigger.
- **Agent**: Processes the alert, determines priority, and formats the notification message.
- **Composio Toolset**: Executes the Pushbullet API calls to deliver the notification to the target device.
- **Chat Output**: Confirms the successful dispatch of the alert and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your dispatch logic with these example prompts:
- `Send a critical alert to the DevOps team: Database connection timeout on production server.`
- `Notify the security team: Multiple failed login attempts detected on the admin console.`
- `Dispatch a warning notification: Disk space usage on the primary file server has exceeded 90%.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for alert routing.
- **Recommended instruction pattern:**
    - Analyze the incoming alert for severity and urgency.
    - Select the appropriate notification channel based on the incident type.
    - Format the message to include the incident timestamp, source, and error description.

### 2) Composio Toolset Node
- Requires a valid Pushbullet API key to authenticate and send push notifications.
- Ensure the connection scope includes `pushbullet:send_push` permissions.

### 3) Tool Availability
- **Pushbullet API**: For sending notifications, managing devices, and retrieving device lists.
- **Logging Utilities**: For tracking alert history and successful delivery confirmations.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automates the resolution and cleanup of stale action items.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Intelligent prioritization of tasks and incident action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitors the health and efficiency of automated internal workflows.
