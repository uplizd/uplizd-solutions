# Emergency Response Dispatcher (Uplizd) - Automate critical work order creation from emergency alerts

## Summary
The Emergency Response Dispatcher is an intelligent Uplizd workflow designed to bridge the gap between real-time emergency alerts and field operations. By monitoring incoming sensor data and incident notifications, the agent automatically categorizes, prioritizes, and dispatches work orders within MaintainX. This solution ensures immediate response times, reduces manual data entry for dispatchers, and maintains a single source of truth for critical maintenance operations.

---

## Demo
![Emergency Response Dispatcher workflow diagram showing sensor data triggering a MaintainX work order creation process](image.png)
**Alt text (SEO-ready):** Emergency Response Dispatcher workflow in Uplizd, automating MaintainX work order creation from sensor alerts and incident data.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/emergency-response-dispatcher-by-maintainx)

---

## Category
**Primary category:** Operations automation  
**Secondary tags:** maintainx, emergency response, work order, field service, iot, incident management, composio, ai workflow  
This solution bridges the gap between IoT sensor alerts and field maintenance execution to minimize downtime.

---

## Who is this for?
This workflow is designed for operations teams managing high-stakes maintenance environments.

* **Maintenance Manager**
    * Ensures critical equipment failures are addressed immediately without manual oversight.
* **Dispatch Coordinator**
    * Reduces the time spent manually creating work orders during high-pressure incident events.
* **Field Technician**
    * Receives clear, prioritized work orders directly on their mobile device via MaintainX.
* **Safety Officer**
    * Maintains a precise audit trail of emergency responses for compliance and safety reporting.

---

## Features
- **Real-time Alert Ingestion**
  Connects directly to sensor streams to capture incident data the moment a threshold is breached.
- **Automated Work Order Generation**
  Uses the Composio Toolset to push structured incident data directly into MaintainX as actionable tasks.
- **Intelligent Priority Scoring**
  Analyzes the severity of the incoming alert to automatically assign appropriate urgency levels to the work order.
- **Contextual Data Enrichment**
  Attaches relevant sensor logs and incident metadata to the work order, providing technicians with immediate diagnostic context.
- **Seamless Dispatch Routing**
  Automatically assigns the generated work order to the correct maintenance team based on location and equipment type.

---

## Use Cases
**Emergency Maintenance**
* Automatically create a "High Priority" work order when a temperature sensor exceeds safety limits.
* Trigger an immediate notification to the on-call technician when a critical machine power-down is detected.

**Preventative Response**
* Generate a work order for routine inspection if a sensor detects abnormal vibration patterns.
* Log incident data in MaintainX for long-term trend analysis of equipment health.

**Operational Compliance**
* Create a standardized incident report for every emergency alert to satisfy safety audit requirements.
* Update asset status in MaintainX to "Under Maintenance" automatically upon dispatch.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the builder.
2. Connect your MaintainX account via the Composio Toolset.
3. Configure your sensor data source (webhook or API) as the trigger.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the raw alert payload from your monitoring system.
* **Agent**: Analyzes the alert, determines the severity, and formats the work order details.
* **Composio Toolset**: Executes the API calls to create the work order in MaintainX.
* **Chat Output**: Confirms the successful creation of the work order and notifies the dispatch team.

### 3) Run the Flow
Use the Playground to test your configuration with these example prompts:
* `Create a high-priority work order for the HVAC unit based on the latest temperature spike alert.`
* `Dispatch a technician to the main plant floor because the vibration sensor reported a critical anomaly.`
* `Generate a work order for the fire suppression system check following the triggered smoke alarm.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, interpreting raw sensor data into structured maintenance tasks.
* Use a model capable of high-precision instruction following (e.g., GPT-4o).
* Instruction: "Extract the equipment ID, severity level, and incident description from the input."
* Instruction: "If the alert is critical, set the MaintainX work order priority to 'Urgent'."

### 2) Composio Toolset Node
* Provide your MaintainX API key within the Composio configuration.
* Ensure the connection scope includes `work_order:write` and `asset:read` permissions.

### 3) Tool Availability
* `maintainx_create_work_order`: Used to generate the task.
* `maintainx_get_asset_details`: Used to fetch location and technician assignment data.
* `maintainx_update_work_order_status`: Used to finalize the dispatch process.

---

## Related Solutions
* [../work-order-status-tracker-by-maintainx/README.md](Work Order Status Tracker) - Monitor and update the progress of maintenance tasks in real-time.
* [../workflow-automation-agent-by-jobnimbus/README.md](Workflow Automation Agent) - Streamline general business processes and task routing.
* [../account-health-usage-monitor-by-jotform/README.md](Account Health Usage Monitor) - Track usage metrics and trigger proactive maintenance alerts.
