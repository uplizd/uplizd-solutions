# Asset Maintenance Tracker (Uplizd) - Proactive equipment monitoring and predictive service scheduling

## Summary
The Asset Maintenance Tracker is an intelligent Uplizd workflow designed to bridge the gap between field service data and proactive maintenance scheduling. By leveraging the Composio Toolset to interface with RepairShopr, this solution automates the monitoring of customer asset health, triggers timely service alerts, and ensures that maintenance records remain a single source of truth. It empowers operations teams to move from reactive repairs to predictive maintenance, significantly increasing equipment uptime and pipeline velocity.

---

## Demo
![Asset Maintenance Tracker workflow dashboard showing automated service ticket generation and asset health status updates](image.png)
**Alt text (SEO-ready):** Asset Maintenance Tracker workflow dashboard showing automated service ticket generation and asset health status updates within the Uplizd platform and RepairShopr integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/09874de8-2be7-554a-841a-68631dafd6d8)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** repairshopr, asset management, maintenance, field service, automation, predictive maintenance, composio, ai workflow
- This solution streamlines technical operations by automating the synchronization and monitoring of customer assets across service platforms.

---

## Who is this for?
This solution is designed for operations and service teams looking to optimize asset lifecycle management and reduce manual administrative overhead.

- **Service Managers**
    - Gain real-time visibility into asset health and upcoming maintenance requirements across all customer accounts.
- **Field Technicians**
    - Receive automated, prioritized work orders that include accurate asset history and specific maintenance instructions.
- **Operations Leads**
    - Standardize maintenance protocols and ensure data hygiene across RepairShopr and internal tracking systems.
- **Customer Success Managers**
    - Proactively communicate maintenance needs to clients, strengthening relationships through reliable, high-uptime service delivery.

---

## Features
- **Automated Asset Monitoring**
    - Continuously tracks asset status and usage metrics to identify when equipment requires inspection or servicing.
- **Smart Ticket Generation**
    - Automatically creates service tickets in RepairShopr when maintenance thresholds are met, reducing manual entry.
- **Predictive Maintenance Logic**
    - Uses AI-driven analysis to forecast potential failures before they occur, allowing for scheduled interventions.
- **Seamless Composio Integration**
    - Connects directly to the RepairShopr API to ensure real-time data synchronization and secure credential management.
- **Centralized Health Dashboard**
    - Provides a unified view of all active assets, their maintenance history, and current service status in one interface.

---

## Use Cases
**Preventive Maintenance Scheduling**
- Automatically trigger service requests based on predefined usage hours or elapsed time intervals.
- Notify technicians of upcoming maintenance windows to ensure parts and labor are available.

**Asset Lifecycle Management**
- Track the age and condition of customer assets to provide data-backed recommendations for upgrades or replacements.
- Maintain a clean, updated log of all service interventions directly within the customer's asset profile.

**Service Efficiency Optimization**
- Prioritize maintenance tasks based on asset criticality and historical failure rates.
- Reduce administrative downtime by automating the creation and assignment of routine service tickets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd library and search for "Asset Maintenance Tracker."
2. Click "Import" to add the workflow template to your workspace.
3. Configure your environment variables and API credentials for RepairShopr.
4. Ensure nodes are correctly connected from Chat Input to Chat Output to validate the data pipeline.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or automated status updates from the monitoring system.
- **Agent**: Processes asset data and determines if maintenance or service scheduling is required.
- **Composio Toolset**: Executes API calls to RepairShopr to fetch asset details or create new service tickets.
- **Chat Output**: Confirms the action taken and provides a summary of the updated asset status.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Check the maintenance status for all assets associated with Customer ID 98765.`
- `Create a new service ticket for Asset A-101 due to upcoming routine maintenance.`
- `List all assets that have exceeded their 500-hour service interval this month.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that interprets asset data and maps it to service actions.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instructions should prioritize accuracy in identifying asset IDs and maintenance triggers.
- Ensure the agent is configured to handle missing data gracefully by requesting clarification.

### 2) Composio Toolset Node
- Provide your RepairShopr API key within the Composio configuration.
- Set the connection scope to allow read/write access to Assets and Service Tickets.

### 3) Tool Availability
- `repairshopr_get_asset_details`: Retrieve current status and history for specific assets.
- `repairshopr_create_ticket`: Generate new service requests based on agent analysis.
- `repairshopr_list_assets`: Query assets based on filter criteria like last service date.

---

## Related Solutions
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Monitor and update field service work orders in real-time.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track customer usage patterns to identify account health trends.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate end-to-end service and project workflows for field operations.
