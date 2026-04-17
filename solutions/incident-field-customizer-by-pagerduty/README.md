# Incident Field Customizer (Uplizd) - Dynamic PagerDuty incident field orchestration

## Summary
The Incident Field Customizer (Uplizd) is an intelligent automation workflow designed to dynamically manage and update incident metadata within PagerDuty. By leveraging AI to analyze incident patterns, this solution ensures that critical field data—such as severity levels, custom tags, and diagnostic notes—is populated in real-time, reducing manual overhead for SREs and improving incident response velocity.

---

## Demo
![Incident Field Customizer workflow showing Chat Input, Agent, Composio PagerDuty Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Incident Field Customizer workflow in Uplizd, showing PagerDuty integration, automated field updates, and AI-driven incident management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cdc3e3d0-162c-5729-ab54-88406589f04a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** pagerduty, incident management, automation, devops, field customization, data hygiene, composio, ai workflow
- This solution streamlines incident response by automating the population and maintenance of custom fields in PagerDuty based on real-time incident context.

---

## Who is this for?
This solution is designed for technical teams looking to reduce manual data entry during high-pressure incident response scenarios.

- **Site Reliability Engineer (SRE)**
    - Automates the tagging of incident fields to ensure consistent reporting and post-mortem data quality.
- **Incident Commander**
    - Gains immediate visibility into incident context by ensuring all relevant metadata fields are populated upon creation.
- **DevOps Manager**
    - Standardizes incident documentation across the organization to improve MTTR (Mean Time To Resolution) metrics.
- **Support Operations Lead**
    - Ensures that support tickets linked to PagerDuty incidents contain the necessary diagnostic fields for faster triage.

---

## Features
- **Dynamic Field Mapping**
    - Automatically maps incident attributes to custom PagerDuty fields based on predefined logic or AI-detected patterns.
- **Real-time Enrichment**
    - Uses the Composio Toolset to fetch and inject external context directly into incident fields as events occur.
- **Intelligent Pattern Recognition**
    - Analyzes incoming alerts to suggest or apply specific field values, reducing the need for manual categorization.
- **Seamless PagerDuty Integration**
    - Leverages secure API connections to perform bulk or individual updates to incident fields without leaving the Uplizd environment.
- **Audit-Ready Documentation**
    - Maintains a consistent data structure across all incidents, facilitating easier compliance reporting and trend analysis.

---

## Use Cases
**Incident Triage & Categorization**
- Automatically populate 'Environment' and 'Service Impact' fields based on alert source metadata.
- Tag incidents with specific team identifiers to ensure correct routing and visibility.

**Automated Post-Mortem Preparation**
- Inject diagnostic links or log snippets into custom fields immediately after an incident is acknowledged.
- Update 'Root Cause' fields once an initial AI analysis of the incident logs is completed.

**Operational Compliance**
- Ensure all high-severity incidents have mandatory 'Compliance Check' fields filled before they can be closed.
- Sync incident status updates with external project management tools via custom field triggers.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the Incident Field Customizer workflow to your workspace.
3. Connect your PagerDuty account within the Composio Toolset node settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives incident ID and desired field updates from the user or automated trigger.
- **Agent**: Processes the input, determines the required field mapping, and generates the API call instructions.
- **Composio Toolset**: Executes the authenticated PagerDuty API requests to update the specified incident fields.
- **Chat Output**: Confirms the update status and provides a summary of the modified fields.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Update incident #12345: set 'Severity' to 'Critical' and 'Environment' to 'Production'.`
- `Find all open incidents for 'Database-Service' and add a tag 'Q4-Review' to their custom fields.`
- `Check incident #98765 and populate the 'Diagnostic-Link' field with the latest log URL.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for field logic.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a PagerDuty field manager. Extract incident IDs and field-value pairs from user input to update PagerDuty records."
- Ensure the agent is restricted to only modifying fields defined in your PagerDuty schema.

### 2) Composio Toolset Node
- Provide your PagerDuty API Key and ensure the connection scope includes `incidents.write` permissions.
- Verify that the toolset is authorized to interact with your specific PagerDuty service account.

### 3) Tool Availability
- `pagerduty_update_incident`: Updates specific fields for a given incident ID.
- `pagerduty_get_incident_details`: Retrieves current field values to prevent overwriting existing data.
- `pagerduty_list_incidents`: Allows the agent to search for incidents based on status or service.

---

## Related Solutions
- [../action-item-cleanup-agent-by-rootly/README.md](../action-item-cleanup-agent-by-rootly/README.md) - Automate the cleanup and organization of incident action items.
- [../action-item-prioritizer-by-rootly/README.md](../action-item-prioritizer-by-rootly/README.md) - Prioritize incident tasks based on urgency and impact.
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor the health and efficiency of your automated incident workflows.
