# BART Service Status Monitor (Uplizd) - Real-time transit disruption tracking and automated alerts

## Summary
The BART Service Status Monitor is an intelligent Uplizd AI workflow designed to provide real-time visibility into Bay Area Rapid Transit (BART) operations. By leveraging the Composio Toolset to interface with live transit data, this solution empowers commuters and operations teams to stay ahead of service disruptions, delays, and station closures, ensuring pipeline velocity for daily travel and logistics planning.

---

## Demo
![BART Service Status Monitor dashboard showing real-time transit delays and station alerts](image.png)
**Alt text (SEO-ready):** BART Service Status Monitor dashboard showing real-time transit delays, service alerts, and Uplizd AI workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/ce7b85a5-b9f7-52ab-bbc7-3f7ec9e18dce)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** transit, bart, monitoring, real-time, alerts, automation, composio, ai workflow
- This solution bridges the gap between raw transit data feeds and actionable user notifications, serving as a critical tool for operational awareness.

---

## Who is this for?
This workflow is designed for professionals and commuters who rely on timely information to maintain their daily schedules.

- **Operations Managers**
    - Receive automated alerts on transit bottlenecks that impact team arrival times and site logistics.
- **Daily Commuters**
    - Get proactive notifications about service delays, allowing for immediate route adjustments.
- **Logistics Coordinators**
    - Track regional transit health to ensure time-sensitive deliveries and personnel movements remain on schedule.
- **Transit Enthusiasts**
    - Utilize real-time data streams for personal analysis and monitoring of regional infrastructure performance.

---

## Features
- **Real-time Status Polling**
    - Automatically fetches the latest service advisories from BART APIs to ensure data accuracy.
- **Intelligent Disruption Filtering**
    - Uses the Agent node to parse complex transit messages and highlight only the most relevant delays.
- **Composio-Powered Integration**
    - Seamlessly connects the Uplizd workflow to external transit data providers via the Composio Toolset.
- **Custom Alert Logic**
    - Configurable triggers that notify users only when specific lines or stations experience active issues.
- **Automated Reporting**
    - Generates concise summaries of transit health, ready for delivery via chat or email channels.

---

## Use Cases
**Commute Planning**
- Automatically check the status of your primary line 30 minutes before your scheduled departure.
- Receive instant rerouting suggestions if your preferred station reports a major service delay.

**Operational Logistics**
- Monitor station closures that might impact the arrival of field staff or site contractors.
- Maintain a log of transit reliability trends to optimize team meeting times throughout the week.

**System Monitoring**
- Aggregate status updates across multiple transit lines to identify regional infrastructure bottlenecks.
- Trigger alerts for maintenance windows that could impact late-night or early-morning travel.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the BART Service Status Monitor template file provided in this repository.
3. Connect your required API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your query regarding specific BART lines or general system status.
- **Agent**: Interprets the intent and queries the transit data via the toolset.
- **Composio Toolset**: Executes the API calls to fetch live BART service status data.
- **Chat Output**: Delivers a human-readable summary of the current transit conditions.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `What is the current service status for the Richmond-Millbrae line?`
- `Are there any major delays reported at the Embarcadero station right now?`
- `Summarize all active BART service alerts for the next 2 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that translates user natural language into specific API requests.
- Set the system prompt to prioritize "Real-time accuracy" and "Concise reporting."
- Enable tool-calling capabilities to allow the agent to fetch external data.
- Configure the temperature to 0.2 to ensure factual, non-hallucinated transit updates.

### 2) Composio Toolset Node
- Provide your API key for the transit data provider within the Composio configuration.
- Set the connection scope to allow read-only access to public transit status endpoints.

### 3) Tool Availability
- **BART Status Fetcher**: Retrieves current line-by-line service health.
- **Station Alert Parser**: Extracts specific delay information for requested stations.
- **Notification Dispatcher**: Formats the final status update for the end-user.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support workflows for high-volume customer inquiries.
- [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Track and monitor the operational status of internal business workflows.
- [work-order-status-tracker-by-maintainx](../work-order-status-tracker-by-maintainx/README.md) - Manage and track the status of maintenance and field service orders.
