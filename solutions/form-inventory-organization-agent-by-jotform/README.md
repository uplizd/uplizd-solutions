# Form Inventory & Organization Agent (Uplizd) - Automated form library management and data hygiene

## Summary
The Form Inventory & Organization Agent streamlines your digital workspace by automatically auditing, categorizing, and maintaining your form library. By leveraging the Composio Toolset to interface with platforms like Jotform, this workflow ensures your data collection assets remain organized, reducing administrative overhead and preventing form clutter. It provides a single source of truth for your active forms, enabling teams to maintain high pipeline velocity and data hygiene standards.

---

## Demo
![Form Inventory & Organization Agent dashboard showing automated form categorization and library cleanup status](image.png)
**Alt text (SEO-ready):** Uplizd Form Inventory & Organization Agent workflow, automated Jotform library management, data hygiene, and form organization automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4a5a8056-013a-599d-a649-b8a02d52cfa4)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** form management, jotform, data hygiene, automation, workflow, library organization, composio, ai agent
- This solution optimizes operational efficiency by automating the lifecycle management of your digital forms and data collection assets.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual administrative tasks and maintain a clean, searchable form repository.

- **Operations Manager**
    - Automates the audit of active vs. deprecated forms to ensure organizational compliance.
- **Data Analyst**
    - Maintains consistent naming conventions across all form assets for easier reporting and data extraction.
- **IT Administrator**
    - Reduces clutter in the organization's Jotform account by identifying and archiving unused forms.
- **Marketing Coordinator**
    - Ensures that lead generation forms are correctly categorized and accessible for campaign tracking.

---

## Features
- **Automated Form Auditing**
    - Scans your entire Jotform library to identify active, draft, and archived forms in real-time.
- **Intelligent Categorization**
    - Uses AI to group forms by department, purpose, or campaign type based on metadata and naming patterns.
- **Data Hygiene Enforcement**
    - Automatically flags forms with missing descriptions or non-standard naming conventions for quick cleanup.
- **Composio-Powered Integration**
    - Seamlessly connects to your Jotform account to perform bulk updates and organizational tasks without manual input.
- **Status Reporting**
    - Generates a summary report of your form inventory, highlighting areas that require immediate attention or archival.

---

## Use Cases
**Library Cleanup & Archival**
- Automatically identify and archive forms that have received zero submissions in the last 90 days.
- Bulk-rename legacy forms to match current organizational naming standards for improved searchability.

**Operational Compliance**
- Audit all public-facing forms to ensure they contain mandatory data privacy disclaimers and legal fields.
- Flag forms that lack assigned owners or department tags to ensure accountability for data collection.

**Workflow Optimization**
- Sync form metadata into your project management tools to keep team members informed of new form creation.
- Categorize new incoming forms into specific folders based on the intent detected in the form title.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your Jotform account via the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your audit commands or organizational requests.
- **Agent**: Processes the request and determines which form management actions to execute.
- **Composio Toolset**: Executes the specific API calls to Jotform to fetch, rename, or archive forms.
- **Chat Output**: Returns a summary of the actions taken and a list of updated form assets.

### 3) Run the Flow
Use the Playground to test your automation with these prompts:
- `Audit my Jotform library and list all forms that haven't been updated in the last 6 months.`
- `Rename all forms containing 'Draft' in the title to 'Archive - [Original Name]'.`
- `Categorize all forms related to 'Lead Generation' and move them to the 'Sales' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your form library logic.
- **Instruction Pattern:**
    - Analyze the user's intent to determine if the request is an audit, a rename, or a categorization task.
    - Map the request to the appropriate Composio tool functions for Jotform.
    - Summarize the outcome clearly, listing the specific forms affected by the operation.

### 2) Composio Toolset Node
- **API Key:** Provide your Jotform API key within the Composio configuration.
- **Connection Scope:** Ensure the connection has read/write permissions for forms and submissions to allow for full library management.

### 3) Tool Availability
- `jotform_get_forms`: Retrieves the list of all forms in the account.
- `jotform_update_form_properties`: Allows for renaming and updating form metadata.
- `jotform_delete_form`: Used for archiving or removing deprecated assets.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Monitor and track account usage metrics across Jotform assets.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate records across your CRM ecosystem.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline cross-platform operational workflows and task management.
