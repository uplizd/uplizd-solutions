# Storage Site Performance Monitor (Uplizd) - Automated facility uptime and latency tracking

## Summary
The Storage Site Performance Monitor is an intelligent Uplizd workflow that automates the tracking, analysis, and reporting of storage facility web performance. By leveraging the Composio Toolset to interface with site monitoring services, this solution provides real-time visibility into site uptime, latency, and operational health, enabling facility managers to maintain a seamless digital experience for their tenants.

---

## Demo
![Storage Site Performance Monitor dashboard showing real-time uptime metrics and latency alerts](image.png)
**Alt text (SEO-ready):** Storage Site Performance Monitor dashboard showing real-time uptime metrics, latency alerts, and facility health status in the Uplizd workflow automation platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0c141913-33a5-585e-99fb-3040389a720c)

---

## Category
**Primary category:** Operations
**Secondary tags:** storage, performance monitoring, uptime, site reliability, web scrapers, automation, composio, ai workflow.
This solution streamlines facility management by providing automated oversight of digital infrastructure performance.

---

## Who is this for?
This solution is designed for operations teams and facility managers who need to ensure high availability for their digital storage platforms.

- **Facility Operations Manager**
    - Proactively identifies site outages before they impact tenant access or payments.
- **IT Infrastructure Lead**
    - Monitors latency trends to optimize server response times across multiple facility locations.
- **Customer Success Manager**
    - Receives automated alerts to communicate site status updates to tenants during maintenance windows.
- **Digital Transformation Officer**
    - Integrates site performance data into broader business intelligence dashboards for data-driven decision-making.

---

## Features
- **Real-Time Uptime Tracking**
    - Continuous monitoring of site availability with instant notification triggers for downtime events.
- **Latency Analysis**
    - Automated performance benchmarking to identify bottlenecks in site loading speeds.
- **Composio-Powered Integrations**
    - Seamless connectivity with web performance tools to pull live diagnostic data into the Uplizd agent.
- **Automated Incident Reporting**
    - Generates concise summaries of performance issues, including error codes and duration, for technical teams.
- **Customizable Alert Thresholds**
    - Configurable sensitivity settings to distinguish between minor latency spikes and critical service interruptions.

---

## Use Cases
**Proactive Maintenance**
- Automatically trigger a support ticket when site latency exceeds a defined threshold for more than 5 minutes.
- Schedule daily performance summary reports to be sent to the infrastructure team via email or Slack.

**Incident Response**
- Instantly notify the facility management team when a site returns a 5xx error code during peak traffic hours.
- Automatically verify if a site is back online after a reported outage before closing the incident ticket.

**Performance Benchmarking**
- Compare site performance metrics across different geographic regions to optimize content delivery.
- Track historical uptime data to identify recurring patterns in site instability during high-traffic periods.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the workflow to your Uplizd workspace.
3. Connect your required API credentials within the Composio Toolset node.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives performance check requests or manual status queries.
- **Agent**: Analyzes the request and determines which monitoring tools to execute.
- **Composio Toolset**: Executes the specific API calls to fetch site health data.
- **Chat Output**: Delivers the formatted performance report or alert to the user.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Check the current uptime status for the main storage facility portal.`
- `What is the average latency for our site over the last 24 hours?`
- `Generate a performance report for all storage sites and highlight any downtime incidents.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for interpreting performance data and summarizing technical logs.
- Use a model capable of structured data analysis (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a performance monitoring assistant. Analyze raw site data, identify trends, and communicate status clearly."
- Instruction: "Always prioritize reporting critical downtime events immediately."

### 2) Composio Toolset Node
- Provide your API key for the relevant monitoring service (e.g., UptimeRobot, Pingdom, or custom web scraper).
- Ensure the connection scope includes read-only access to site performance logs and status endpoints.

### 3) Tool Availability
- **Site Status Checker**: Fetches current HTTP response codes and uptime status.
- **Latency Analyzer**: Retrieves historical response time data.
- **Alert Manager**: Triggers notifications based on predefined health thresholds.

---

## Related Solutions
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Audit and manage user permissions for storage facility portals.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automate the setup and provisioning of new facility administrators.
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Monitor and update maintenance work orders for facility infrastructure.
