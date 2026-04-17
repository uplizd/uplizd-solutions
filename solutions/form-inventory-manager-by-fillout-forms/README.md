# Form Inventory Manager (Uplizd) - Centralized form library and lifecycle automation

## Summary
The Form Inventory Manager is an intelligent Uplizd workflow designed to streamline your digital form ecosystem by automating the tracking, auditing, and lifecycle management of your form assets. By integrating directly with Fillout Forms, this solution provides a single source of truth for your organization, ensuring that redundant, outdated, or non-compliant forms are identified and archived to maintain operational hygiene and pipeline velocity.

---

## Demo
![Form Inventory Manager dashboard showing active vs archived forms and automated audit logs](image.png)
**Alt text (SEO-ready):** Uplizd Form Inventory Manager workflow dashboard displaying automated form lifecycle tracking, Fillout Forms integration, and data hygiene analytics.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bd3faf25-0b69-53d8-83e6-66dda6b4d869)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** form management, fillout, data hygiene, workflow automation, asset tracking, operational efficiency, composio, ai workflow
- This solution bridges the gap between scattered form creation and centralized operational oversight, ensuring your data collection tools remain optimized and secure.

---

## Who is this for?
This solution is designed for teams managing high volumes of data collection assets who need to maintain strict control over their digital footprint.

- **Operations Manager**
    - Automates the audit of active forms to reduce clutter and ensure team members use only approved templates.
- **Data Compliance Officer**
    - Ensures all data collection points meet internal security standards by flagging outdated or unauthorized forms.
- **Marketing Coordinator**
    - Tracks form performance and lifecycle status to ensure lead generation assets are always current and functional.
- **IT Administrator**
    - Maintains a clean inventory of third-party integrations, preventing shadow IT and redundant form subscriptions.

---

## Features
- **Automated Inventory Discovery**
    - Automatically scans and indexes all forms connected via Fillout, providing a real-time view of your entire library.
- **Lifecycle Status Tracking**
    - Categorizes forms by status (Active, Deprecated, Archived) to simplify maintenance and cleanup efforts.
- **Redundancy Detection**
    - Uses AI to identify duplicate form logic or overlapping data collection fields across your organization.
- **Compliance Auditing**
    - Flags forms that have not been updated or reviewed within a specific timeframe to ensure ongoing policy adherence.
- **Unified Reporting**
    - Generates summary reports of form usage and health, enabling data-driven decisions on which assets to retire.

---

## Use Cases
**Form Lifecycle Management**
- Automatically archive forms that have not received submissions in the last 90 days.
- Flag forms with missing mandatory fields or outdated branding for immediate review.

**Operational Data Hygiene**
- Identify duplicate form structures that cause data fragmentation across your CRM.
- Maintain a clean, searchable registry of all active data collection touchpoints.

**Compliance and Security**
- Audit forms for PII collection to ensure they align with current data privacy regulations.
- Restrict form access by automatically disabling links for deprecated or legacy campaigns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Fillout Forms account via the integration settings.
3. Configure your notification channels (e.g., Slack or Email) for audit alerts.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding form status or inventory requests.
- **Agent**: Processes inventory data and applies logic to categorize or flag forms.
- **Composio Toolset**: Executes API calls to Fillout to fetch, update, or archive form records.
- **Chat Output**: Returns the status report or confirmation of inventory actions to the user.

### 3) Run the Flow
Use the Playground to test your inventory management:
- `List all active forms created in the last 30 days.`
- `Find and flag any duplicate forms in the marketing workspace.`
- `Archive all forms that have zero submissions and were created before 2023.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for form governance.
- **Role**: Act as a meticulous Operations Auditor.
- **Instruction Pattern**:
    - Prioritize accuracy when identifying form metadata.
    - Only perform destructive actions (like archiving) after explicit confirmation or based on clear inactivity thresholds.
    - Provide concise, actionable summaries for all audit reports.

### 2) Composio Toolset Node
- **API Key**: Ensure your Fillout API key is securely stored in the Composio environment.
- **Connection Scope**: Grant read/write access to form metadata and submission logs to enable full lifecycle management.

### 3) Tool Availability
- `fillout_list_forms`: Retrieve the comprehensive inventory of existing forms.
- `fillout_get_form_details`: Fetch specific metadata for deep-dive audits.
- `fillout_update_form_status`: Toggle forms between active, paused, or archived states.

---

## Related Solutions
- [../account-health-usage-monitor-by-jotform/README.md](../account-health-usage-monitor-by-jotform/README.md) - Monitor usage metrics and health for your Jotform assets.
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Track the operational health and performance of your automated workflows.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate data across your CRM platforms.
