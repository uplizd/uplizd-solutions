# Preventive Maintenance Scheduler (Uplizd) - Automate asset upkeep and work order generation

## Summary
The Preventive Maintenance Scheduler (Uplizd) is an intelligent automation workflow designed to streamline facility and asset management by automatically generating work orders based on predefined maintenance schedules and real-time asset performance data. By integrating directly with MaintainX, this solution eliminates manual scheduling bottlenecks, ensures consistent equipment uptime, and provides a single source of truth for maintenance operations, ultimately increasing pipeline velocity and operational hygiene.

---

## Demo
![Preventive Maintenance Scheduler workflow showing asset data ingestion, automated scheduling logic, and MaintainX work order creation](image.png)
**Alt text (SEO-ready):** Preventive Maintenance Scheduler workflow in Uplizd, automating asset maintenance, work order generation, and MaintainX integration for operational efficiency.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4af5b83b-ac59-5985-97c6-89e0edf57bda)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** maintenance, asset management, maintainx, workflow automation, facility management, predictive maintenance, composio, ai workflow
- This solution optimizes facility operations by bridging the gap between asset monitoring and automated task execution.

---

## Who is this for?
This solution is designed for operations teams looking to transition from reactive repairs to proactive maintenance strategies.

- **Facility Manager**
    - Ensures consistent equipment uptime and reduces emergency repair costs through automated scheduling.
- **Maintenance Lead**
    - Eliminates manual data entry by automatically syncing asset health signals to actionable work orders.
- **Operations Analyst**
    - Gains visibility into maintenance cycles and asset performance trends via centralized data logs.
- **Reliability Engineer**
    - Standardizes maintenance protocols across multiple sites using automated trigger-based workflows.

---

## Features
- **Automated Work Order Generation**
    - Triggers the creation of new maintenance tasks in MaintainX based on time-based intervals or asset-specific usage triggers.
- **Real-time Asset Sync**
    - Maintains a continuous feedback loop between your asset database and the maintenance scheduler to ensure data accuracy.
- **Intelligent Scheduling Logic**
    - Uses AI to prioritize maintenance tasks based on asset criticality and historical failure patterns.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely authenticate and execute API calls directly within MaintainX.
- **Operational Hygiene Reporting**
    - Automatically logs all scheduled maintenance actions to provide a clean, auditable history of asset care.

---

## Use Cases
**Routine Facility Upkeep**
- Automatically schedule monthly HVAC inspections based on asset installation dates.
- Generate recurring work orders for fire safety equipment testing and compliance reporting.

**Asset Performance Optimization**
- Trigger an immediate maintenance work order when an asset reports a performance threshold breach.
- Sync usage-based metrics from IoT sensors to adjust maintenance intervals dynamically.

**Team Coordination**
- Assign generated work orders to specific technician groups based on the asset location or category.
- Notify maintenance staff via integrated channels as soon as a new work order is created by the agent.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the solution JSON file to initialize the canvas.
3. Connect your MaintainX account via the Composio Toolset node.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or system-generated maintenance requests.
- **Agent**: Processes the maintenance logic and determines the appropriate work order parameters.
- **Composio Toolset**: Executes the API calls to create and update work orders in MaintainX.
- **Chat Output**: Confirms successful scheduling and provides a summary of the generated work order.

### 3) Run the Flow
Use the Playground to test your automation with prompts like:
- `Create a preventive maintenance work order for the HVAC unit in Building A for next Monday.`
- `List all upcoming maintenance tasks for the production line assets.`
- `Schedule a recurring inspection for all fire extinguishers due this quarter.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for maintenance logic.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruction: "You are a maintenance scheduling assistant. Extract asset IDs, task descriptions, and dates from user input to trigger MaintainX work orders."
- Instruction: "Always verify if an asset exists before attempting to schedule a maintenance task."

### 2) Composio Toolset Node
- Provide your MaintainX API key within the Composio configuration.
- Set the connection scope to allow read/write access for work orders and asset management modules.

### 3) Tool Availability
- `maintainx_create_work_order`: Generates new maintenance tasks.
- `maintainx_get_asset_details`: Retrieves current status and history of specific assets.
- `maintainx_list_schedules`: Fetches existing maintenance intervals to prevent duplicates.

---

## Related Solutions
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Monitor and update the progress of active maintenance tasks.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Extend automation capabilities across different operational platforms.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track asset health and usage metrics for proactive maintenance planning.
