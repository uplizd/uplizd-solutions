# Connection CRM Sync Agent (Uplizd) - Automated Prospect Enrichment and CRM Synchronization

## Summary
The Connection CRM Sync Agent streamlines your sales operations by automatically capturing new professional connections and syncing them directly into your CRM with enriched prospect data. This AI-driven workflow eliminates manual data entry, ensures your pipeline remains up-to-date with verified contact information, and provides a single source of truth for your sales team to accelerate lead conversion.

---

## Demo
![Connection CRM Sync Agent workflow diagram showing data flow from connection source to CRM](image.png)
**Alt text (SEO-ready):** Connection CRM Sync Agent workflow diagram showing automated data flow from connection source to CRM with Uplizd and Composio integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKYGBgYPhPBf9vYGBg+E8F/29gYGD4TwX/b2BgYPhPBf9vYGD4TwX/b2BgYPhPBf9vYAAAM0kH/V5v5yQAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/913d9af5-046a-5e65-9674-ea52be5e9015)

---

## Category
**Primary category:** CRM data sync  
**Secondary tags:** sales automation, lead enrichment, crm, data hygiene, pipeline, composio, ai workflow  
This solution bridges the gap between networking platforms and your CRM to ensure high-quality, actionable prospect data is always available.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate manual administrative tasks and improve data accuracy.

*   **Sales Development Reps (SDRs)**
    *   Automate the tedious process of manual lead entry to focus on high-value outreach.
*   **Revenue Operations (RevOps) Managers**
    *   Maintain pristine CRM data hygiene by standardizing incoming prospect information.
*   **Account Executives (AEs)**
    *   Receive real-time notifications and enriched context for every new connection added to the pipeline.
*   **Sales Managers**
    *   Gain visibility into team networking efforts with automated tracking and reporting.

---

## Features
- **Automated Prospect Enrichment**
    Automatically fetch and append professional details to new connections using integrated data providers.
- **Real-time CRM Synchronization**
    Instantly push validated contact records into your CRM, ensuring your database reflects the latest networking activity.
- **Intelligent Deduplication**
    Identify and merge duplicate entries automatically to prevent data fragmentation within your CRM.
- **Customizable Field Mapping**
    Configure how specific data points—such as job titles, company names, and LinkedIn profiles—map to your CRM fields.
- **Composio-Powered Connectivity**
    Leverage the Composio Toolset to securely connect with major CRM platforms like Salesforce, HubSpot, and Dynamics 365.

---

## Use Cases
**Lead Pipeline Management**
*   Automatically sync new LinkedIn connections to your CRM as "New Lead" status.
*   Update existing lead records with the latest professional contact information.

**Data Hygiene & Enrichment**
*   Standardize job titles and company formatting during the sync process.
*   Append missing email addresses or phone numbers to newly created CRM records.

**Sales Outreach Efficiency**
*   Trigger an automated "Welcome" task in your CRM immediately after a connection is synced.
*   Segment new connections based on industry or company size for targeted follow-up campaigns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your CRM and data enrichment tool connections via the Composio dashboard.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual command to initiate the sync.
*   **Agent**: Processes the raw connection data and determines the necessary enrichment steps.
*   **Composio Toolset**: Executes the API calls to enrich data and update your CRM records.
*   **Chat Output**: Confirms the successful sync or reports any data conflicts to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
*   `Sync my latest connections to Salesforce and enrich with company data.`
*   `Check for new connections and update HubSpot records with current job titles.`
*   `Run a full sync of all pending connections and notify me of any duplicates found.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for data parsing and CRM interaction.
*   Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Ensure the system prompt explicitly defines the mapping between incoming connection fields and CRM schema.
*   Enable tool-calling mode to allow the agent to invoke Composio functions dynamically.

### 2) Composio Toolset Node
*   Provide your **Composio API Key** in the node settings to enable secure integration.
*   Set the connection scope to include read/write access for your specific CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
*   **CRM Connector**: Create, Update, and Search records.
*   **Enrichment API**: Fetch professional profile data and company metadata.
*   **Data Validator**: Format and sanitize inputs before CRM ingestion.

---

## Related Solutions
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and formatting for CRM records.
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive intelligence gathering for target accounts.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up cadences effectively.
