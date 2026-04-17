# Meeting Bot Fleet Manager (Uplizd) - Centralized control for automated meeting intelligence

## Summary
The Meeting Bot Fleet Manager by Uplizd provides a unified control plane for deploying, monitoring, and optimizing meeting bot agents across your organization. By integrating directly with Recall.ai, this workflow ensures consistent bot behavior, automates meeting attendance scheduling, and centralizes recording management, enabling RevOps and support teams to maintain high-quality data capture without manual intervention.

---

## Demo
![Meeting Bot Fleet Manager dashboard showing active bot status, meeting schedules, and recording synchronization logs](image.png)
**Alt text (SEO-ready):** Meeting Bot Fleet Manager dashboard showing active bot status, meeting schedules, and recording synchronization logs for Uplizd automated meeting workflows and Recall.ai integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/3cee1a72-a461-55e6-a2d9-a1363d4aa4c7)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meeting automation, recall.ai, bot management, revops, data capture, workflow orchestration, composio, ai agent
- This solution streamlines the lifecycle of automated meeting assistants, ensuring reliable data ingestion for downstream CRM and analytics platforms.

---

## Who is this for?
This solution is designed for teams managing high volumes of virtual meetings who require automated, reliable, and compliant data capture.

- **Revenue Operations Manager**
    - Ensures all client-facing calls are recorded and transcribed for accurate pipeline forecasting.
- **Customer Success Lead**
    - Automates the deployment of bots to support calls, ensuring action items are captured in real-time.
- **IT/Infrastructure Admin**
    - Manages bot permissions and fleet-wide settings to maintain security and compliance standards.
- **Sales Enablement Specialist**
    - Monitors bot performance to ensure high-quality data is available for coaching and training modules.

---

## Features
- **Automated Bot Deployment**
    - Instantly provision meeting bots for scheduled calendar events using the Composio Toolset.
- **Centralized Fleet Monitoring**
    - Track the status of all active and completed meeting bots from a single unified interface.
- **Recall.ai Integration**
    - Leverage robust API connectivity to handle diverse meeting platforms including Zoom, Google Meet, and Microsoft Teams.
- **Recording Sync Automation**
    - Automatically route meeting recordings and transcripts to your preferred storage or CRM destination.
- **Real-time Health Alerts**
    - Receive proactive notifications if a bot fails to join a meeting or encounters a connection error.

---

## Use Cases
**Meeting Compliance & Governance**
- Automatically enforce recording consent policies across all external client meetings.
- Audit bot participation logs to ensure coverage for sensitive high-stakes negotiations.

**Sales Pipeline Intelligence**
- Sync meeting transcripts directly to CRM opportunity records to identify key buying signals.
- Automate the extraction of action items from discovery calls to accelerate deal velocity.

**Support Operations Efficiency**
- Deploy bots to support triage calls to ensure technical issues are documented immediately.
- Streamline post-meeting follow-ups by auto-generating summaries from bot-captured transcripts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the "Meeting Bot Fleet Manager" template.
2. Click "Import" to load the workflow into your workspace.
3. Authenticate your Recall.ai and CRM credentials within the connection manager.
4. Ensure nodes are correctly mapped to your specific calendar and recording storage endpoints.

### 2) Setup the Nodes
- **Chat Input**: Accepts meeting invites, bot configuration parameters, or manual override commands.
- **Agent**: Processes meeting data, evaluates scheduling logic, and manages bot lifecycle events.
- **Composio Toolset**: Executes API calls to Recall.ai for bot joining, recording, and status retrieval.
- **Chat Output**: Delivers confirmation of bot deployment, error logs, or summary reports to the user.

### 3) Run the Flow
Use the Playground to test your fleet management logic:
- `Deploy a bot to all meetings on my calendar for the next 4 hours.`
- `Check the status of the bot currently in the meeting with Acme Corp.`
- `Sync the recording from the last sales discovery call to Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your meeting bot fleet.
- Use a model with strong function-calling capabilities (e.g., GPT-4o).
- **Recommended instruction pattern:**
    - "You are a fleet manager for meeting bots; prioritize reliability and accurate data routing."
    - "Always verify meeting availability before attempting to join."
    - "If a bot fails to connect, log the error and notify the admin immediately."

### 2) Composio Toolset Node
- Provide your Recall.ai API key to enable bot control.
- Ensure the connection scope includes `meetings:read`, `bots:write`, and `recordings:read`.

### 3) Tool Availability
- **Recall.ai Connector**: For bot join/leave and recording retrieval.
- **Calendar API**: For scanning upcoming meeting schedules.
- **Notification Service**: For sending status alerts to Slack or Email.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automate voice-based customer interactions.
- [account-research-assistant-by-zoominfo](../account-research-assistant-by-zoominfo/README.md) - Enrich account data for better meeting preparation.
- [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Track the operational health of your automated workflows.
