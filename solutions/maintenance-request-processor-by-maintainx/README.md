# Maintenance Request Processor (Uplizd) - Automate work order creation and categorization

## Summary
The Maintenance Request Processor is an intelligent Uplizd workflow that transforms unstructured employee maintenance requests into structured, actionable work orders within MaintainX. By leveraging AI to categorize issues, assign priority levels, and route tasks to the appropriate maintenance teams, this solution eliminates manual data entry, reduces response times, and ensures facility hygiene through a single source of truth.

---

## Demo
![Maintenance Request Processor workflow diagram showing input, AI categorization, and MaintainX integration](image.png)
**Alt text (SEO-ready):** Maintenance Request Processor Uplizd workflow, automated work order generation, MaintainX integration, AI-driven facility management, and maintenance request automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7f411be5-856c-59f7-90ec-41df03c8d529)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** maintainx, facility management, work orders, automation, ai workflow, maintenance, composio, operations
- This solution streamlines facility operations by bridging the gap between incoming maintenance requests and structured work order management.

---

## Who is this for?
This solution is designed for operations teams looking to standardize their maintenance intake process and improve technician efficiency.

- **Facility Manager**
    - Gains real-time visibility into facility issues and automated prioritization of critical repairs.
- **Maintenance Technician**
    - Receives clearly defined, categorized work orders directly in their dashboard, reducing ambiguity.
- **Operations Coordinator**
    - Eliminates manual ticket logging and ensures all requests are routed to the correct department.
- **HR/Office Manager**
    - Provides a seamless, automated channel for employees to report office issues without administrative overhead.

---

## Features
- **Intelligent Categorization**
    - Automatically classifies incoming requests (e.g., HVAC, Plumbing, Electrical) using AI to ensure correct routing.
- **Automated Priority Scoring**
    - Analyzes request urgency to assign priority levels, ensuring critical safety issues are addressed immediately.
- **MaintainX Integration**
    - Seamlessly creates and updates work orders in MaintainX via the Composio Toolset without manual intervention.
- **Real-time Status Updates**
    - Keeps stakeholders informed by automatically logging request receipt and assignment status.
- **Standardized Data Formatting**
    - Normalizes unstructured text input into consistent fields for better reporting and historical analysis.

---

## Use Cases
**Emergency Facility Repairs**
- Automatically flagging "water leak" or "power outage" requests as high-priority.
- Instantly alerting the on-call technician via MaintainX when a critical issue is submitted.

**Routine Maintenance Scheduling**
- Batching non-urgent requests like "replace lightbulb" or "furniture repair" for weekly maintenance rounds.
- Updating work order descriptions with photos or location details extracted from the original request.

**Operational Reporting**
- Tracking the volume of maintenance requests by category to identify recurring facility issues.
- Generating monthly summaries of response times for different types of maintenance tasks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the workflow template.
2. Connect your MaintainX account via the Composio Toolset node.
3. Configure your Chat Input to accept email or form-based maintenance submissions.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw text description of the maintenance issue from the employee.
- **Agent**: Analyzes the request, extracts key entities (location, urgency, category), and formats the data.
- **Composio Toolset**: Executes the API calls to create the work order within MaintainX.
- **Chat Output**: Confirms to the requester that the work order has been successfully created and provides a tracking ID.

### 3) Run the Flow
Test the workflow using the following prompts in the Uplizd Playground:
- `The kitchen sink on the 3rd floor is leaking water, please fix it.`
- `The light in the main conference room is flickering and needs a replacement.`
- `Urgent: The HVAC unit in the server room is making a loud grinding noise.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, ensuring data integrity before it hits your CRM or maintenance platform.
- **Instruction Pattern**:
    - "Extract the location, issue type, and urgency level from the user's message."
    - "If the urgency is not specified, default to 'Medium' unless the issue involves safety or infrastructure failure."
    - "Format the output into a structured JSON object compatible with the MaintainX API."

### 2) Composio Toolset Node
- **API Key**: Ensure your MaintainX API key is securely stored in the Composio configuration.
- **Connection Scope**: Grant the toolset permissions to create and update work orders within your organization's MaintainX account.

### 3) Tool Availability
- **MaintainX Create Work Order**: Capability to generate new tickets.
- **MaintainX Get Asset List**: Capability to verify equipment IDs for precise routing.
- **MaintainX Update Work Order**: Capability to append notes or change status based on agent analysis.

---

## Related Solutions
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Monitor and update the progress of active maintenance tasks.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate general operational workflows and task routing.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Standardize data entry and account creation processes.
