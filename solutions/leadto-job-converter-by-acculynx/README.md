# Lead to Job Converter (Uplizd) - Automate lead-to-job conversion and appointment scheduling

## Summary
The Lead to Job Converter by Acculynx is an intelligent Uplizd AI workflow designed to streamline the transition from qualified lead to active job. By automating the data transfer and appointment scheduling process, this solution eliminates manual entry errors, accelerates pipeline velocity, and ensures a single source of truth for your sales and operations teams.

---

## Demo
![Lead to Job Converter workflow diagram showing lead qualification, data mapping to Acculynx, and automated appointment scheduling](image.png)
**Alt text (SEO-ready):** Lead to Job Converter Uplizd workflow, automated lead qualification, Acculynx CRM integration, sales pipeline automation, and appointment scheduling.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2950c401-c08f-5852-b452-1565cef212d5)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, acculynx, lead management, pipeline, appointment scheduling, data sync, ai workflow, composio
- This solution bridges the gap between lead generation and job execution, providing a seamless operational flow for field service businesses.

---

## Who is this for?
This workflow is designed for teams looking to reduce administrative overhead and improve conversion speed.

- **Sales Managers**
    - Ensure every qualified lead is immediately converted into a job without manual oversight.
- **Operations Coordinators**
    - Automatically sync appointment details to field teams to prevent scheduling conflicts.
- **Business Owners**
    - Increase pipeline velocity and reduce the time-to-job metric across the organization.
- **Customer Success Leads**
    - Maintain consistent communication by triggering automated follow-ups once a job is created.

---

## Features
- **Automated Lead Mapping**
    - Seamlessly maps lead data fields from your CRM directly into Acculynx job objects.
- **Real-time Appointment Sync**
    - Automatically schedules site visits or consultations based on lead availability and technician capacity.
- **Intelligent Validation**
    - Uses the Composio Toolset to verify lead readiness before initiating the job creation process.
- **Error-Free Data Transfer**
    - Eliminates manual data entry, reducing the risk of typos or missing information in job files.
- **Workflow Orchestration**
    - Triggers downstream notifications and status updates as soon as the lead-to-job transition is confirmed.

---

## Use Cases
**Lead Qualification & Conversion**
- Automatically convert leads marked as "Qualified" in your CRM into active jobs in Acculynx.
- Trigger a job creation sequence only after specific lead criteria (e.g., budget, location) are met.

**Scheduling & Resource Allocation**
- Sync appointment windows directly from the lead's preference to the Acculynx calendar.
- Reassign or update job appointments in real-time if lead availability changes.

**Operational Hygiene**
- Archive stale leads automatically once they have been successfully converted to a job.
- Generate a summary report of all converted leads for weekly sales performance reviews.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Lead to Job Converter" template.
2. Click "Import Flow" to initialize the workflow in your workspace.
3. Connect your Acculynx and CRM accounts via the Composio integration settings.
4. Ensure nodes are correctly mapped to your specific CRM field names and Acculynx project templates.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead details or trigger signal from your CRM.
- **Agent**: Analyzes lead data and determines if the conversion criteria are met.
- **Composio Toolset**: Executes the API calls to create the job and schedule the appointment in Acculynx.
- **Chat Output**: Confirms successful job creation and provides a summary of the scheduled appointment.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Convert lead ID 98765 to a new job in Acculynx and schedule a site visit for Tuesday at 10 AM.`
- `Check if lead 'John Doe' is ready for job conversion and create the record if all fields are populated.`
- `List all recent lead-to-job conversions and confirm their scheduled appointment times.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for data validation and tool selection.
- Prioritize accuracy when mapping lead fields to job parameters.
- Use the provided context to identify missing information before attempting job creation.
- Maintain a professional tone when confirming conversion details in the output.

### 2) Composio Toolset Node
- Provide your Acculynx API key and ensure the connection scope includes read/write access to jobs and calendars.

### 3) Tool Availability
- **CRM Connector**: For fetching and updating lead status.
- **Acculynx API**: For creating jobs, updating project details, and managing calendars.
- **Data Validator**: For ensuring all mandatory fields are present before API execution.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate general business processes and task management.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline the initialization of new accounts in your CRM.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage and strengthen B2B account connections.
