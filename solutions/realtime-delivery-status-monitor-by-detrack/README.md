# Real-time Delivery Status Monitor (Uplizd) - Automated logistics tracking and delay alerting

## Summary
The Real-time Delivery Status Monitor is an intelligent Uplizd workflow that automates the tracking of shipment lifecycles by integrating directly with Detrack. By providing a single source of truth for logistics data, this solution eliminates manual status checks, reduces customer support overhead, and ensures proactive communication regarding delivery delays or exceptions.

---

## Demo
![Real-time Delivery Status Monitor workflow dashboard showing automated shipment tracking and alert triggers](image.png)
**Alt text (SEO-ready):** Real-time Delivery Status Monitor workflow on Uplizd, featuring automated Detrack logistics tracking, shipment delay alerts, and supply chain data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/89eae0d3-8c0c-58fb-8502-a8f6729b8dab)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** logistics, detrack, delivery tracking, supply chain, automation, real-time, shipment monitoring, api integration
- This solution streamlines logistics operations by bridging the gap between real-time delivery data and automated status reporting.

---

## Who is this for?
This solution is designed for logistics professionals and operations teams who need to maintain visibility over complex delivery networks.

- **Logistics Manager**
    - Automate exception handling to reduce the time spent manually investigating delayed shipments.
- **Customer Support Lead**
    - Provide proactive delivery updates to customers before they reach out with "where is my order" inquiries.
- **Operations Analyst**
    - Gain insights into carrier performance and delivery bottlenecks through centralized status monitoring.
- **Supply Chain Coordinator**
    - Ensure seamless data flow between warehouse management systems and end-customer delivery notifications.

---

## Features
- **Automated Status Polling**
    - Continuously syncs shipment status updates from Detrack to ensure the latest delivery information is always available.
- **Proactive Delay Alerts**
    - Triggers instant notifications when a delivery status changes to "Delayed" or "Exception," allowing for immediate intervention.
- **Unified Logistics Dashboard**
    - Consolidates tracking data from multiple routes into a single, searchable interface for improved oversight.
- **Customizable Notification Logic**
    - Allows users to define specific thresholds for what constitutes an "urgent" delay requiring human attention.
- **Composio-Powered Connectivity**
    - Leverages the Composio Toolset to securely authenticate and interact with Detrack APIs without managing complex infrastructure.

---

## Use Cases
**Shipment Exception Management**
- Automatically flag deliveries that have missed their scheduled arrival window for immediate investigation.
- Route exception alerts to the relevant regional dispatch team via Slack or email based on the delivery zone.

**Customer Experience Enhancement**
- Trigger automated "out for delivery" or "delayed" status updates to customers via integrated communication channels.
- Reduce support ticket volume by providing real-time, accurate delivery ETAs directly from the source of truth.

**Logistics Performance Auditing**
- Aggregate historical delivery data to identify recurring patterns of delays or carrier-specific performance issues.
- Generate weekly reports on on-time delivery percentages to inform future logistics strategy and carrier selection.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the Real-time Delivery Status Monitor to your workspace.
3. Connect your Detrack API credentials within the integration settings.
4. Ensure nodes are correctly mapped and the workflow is toggled to "Active" to begin monitoring.

### 2) Setup the Nodes
- **Chat Input**: Receives tracking IDs or status queries from the user or automated triggers.
- **Agent**: Processes the request, interprets the delivery status, and determines if an alert is necessary.
- **Composio Toolset**: Executes API calls to Detrack to fetch real-time shipment details.
- **Chat Output**: Delivers the formatted status update or alert notification to the designated endpoint.

### 3) Run the Flow
Use the Playground to test your monitoring logic with these prompts:
- `Check the current status for tracking number TRK-992834.`
- `List all shipments currently marked as delayed in the North region.`
- `Provide a summary of today's delivery performance for the main distribution hub.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logistics intelligence layer, interpreting raw API data into actionable insights.
- Use a model with strong reasoning capabilities (e.g., GPT-4o) to handle complex status descriptions.
- Configure the system prompt to prioritize "Delayed" or "Exception" statuses in all summaries.
- Ensure the agent is instructed to provide clear, concise ETAs for all queried shipments.

### 2) Composio Toolset Node
- Provide your Detrack API key within the Composio configuration panel.
- Set the connection scope to allow read-only access to shipment and tracking endpoints for security.

### 3) Tool Availability
- `get_shipment_details`: Retrieves comprehensive data for a specific tracking ID.
- `list_delayed_shipments`: Filters and returns all shipments currently experiencing delays.
- `update_delivery_status`: Allows the agent to log notes or update internal status flags based on findings.

---

## Related Solutions
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Monitor and manage field service work orders.
- [WhatsApp Order Status Agent](../whats-app-order-status-agent-by-whatsapp/README.md) - Automate delivery updates directly via WhatsApp.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track customer usage metrics and account health.
