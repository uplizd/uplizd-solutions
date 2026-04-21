# Status Page Coordinator (Uplizd) - Automated incident communication and status page management

## Summary
The Status Page Coordinator automates the lifecycle of incident management by synchronizing system status updates with customer-facing communication channels. By leveraging the Better Stack API via the Composio Toolset, this Uplizd workflow ensures that stakeholders receive real-time notifications, reducing manual overhead and maintaining transparency during service disruptions.

---

## Demo
![Status Page Coordinator workflow showing incident detection, status update, and customer notification nodes](image.png)
**Alt text (SEO-ready):** Status Page Coordinator workflow in Uplizd, automating Better Stack incident updates and customer communication via AI-driven workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/99dbbadc-49e1-5ccc-a316-d0cdfa568b83)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** status page, incident management, better stack, automation, customer support, uptime, reliability, composio
- This solution streamlines operational reliability by bridging the gap between infrastructure monitoring and stakeholder transparency.

---

## Who is this for?
This solution is designed for technical teams and customer-facing organizations that need to maintain high service transparency during downtime.

- **Site Reliability Engineer (SRE)**
    - Automates the creation of incident reports to focus on root cause analysis rather than manual status updates.
- **Customer Support Manager**
    - Ensures support teams are instantly notified of system status changes to proactively manage customer inquiries.
- **DevOps Lead**
    - Maintains a single source of truth for system health across internal dashboards and public-facing status pages.
- **Product Operations Specialist**
    - Reduces the time-to-resolution communication gap by triggering automated updates across multiple channels simultaneously.

---

## Features
- **Automated Incident Lifecycle**
    - Automatically transitions status page components from operational to degraded or down based on incoming alerts.
- **Multi-Channel Notification Sync**
    - Broadcasts incident updates to integrated communication platforms to keep users informed in real-time.
- **Better Stack Integration**
    - Utilizes the Composio Toolset to securely interface with Better Stack APIs for precise status page control.
- **Intelligent Incident Summarization**
    - Uses the Agent node to draft clear, professional incident descriptions based on raw technical alert data.
- **Workflow Reliability**
    - Ensures consistent execution of status updates, preventing human error during high-pressure outage scenarios.

---

## Use Cases
**Incident Response Automation**
- Automatically set status page components to "Under Maintenance" when a deployment pipeline triggers a service restart.
- Update incident severity levels dynamically as monitoring tools detect changes in system health.

**Customer Communication**
- Send automated "Issue Resolved" notifications to subscribers once the system returns to healthy status.
- Draft and publish post-incident summaries to the status page to maintain long-term customer trust.

**Operational Reporting**
- Log all incident start and end times into a centralized database for monthly uptime reporting.
- Trigger internal alerts to Slack or Microsoft Teams whenever a status page update is published.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your Better Stack account within the Composio Toolset configuration.
3. Configure your notification channels (e.g., Email, Slack, or Webhooks) to receive updates.
4. Ensure nodes are correctly linked from Chat Input to the Agent, then to the Composio Toolset, and finally to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives incident triggers or manual status update requests.
- **Agent**: Processes alert data and generates professional status updates.
- **Composio Toolset**: Executes API calls to update the status page and notify subscribers.
- **Chat Output**: Confirms the successful publication of the status update to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Update the status page to show that the API service is currently experiencing high latency.`
- `Create a new incident report for the ongoing database connectivity issues.`
- `Mark the 'Payment Gateway' component as operational and notify all subscribers.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the communication layer between raw technical alerts and human-readable updates.
- Maintain a professional, empathetic, and transparent tone.
- Ensure all technical jargon is simplified for non-technical stakeholders.
- Always include a placeholder for the estimated time of resolution (ETR) when applicable.

### 2) Composio Toolset Node
- Requires a valid Better Stack API key with `status_page` write permissions.
- Ensure the connection scope allows for component management and incident creation.

### 3) Tool Availability
- **Status Page Management**: Create, update, and resolve incidents.
- **Component Control**: Toggle component status (Operational, Degraded, Down).
- **Subscriber Notification**: Trigger automated alerts to registered users.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven support for handling customer inquiries during incidents.
- [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Monitor internal workflow health and team productivity.
- [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Manage post-incident action items and technical debt.
