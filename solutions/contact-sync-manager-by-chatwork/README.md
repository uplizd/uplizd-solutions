# Contact Sync Manager (Uplizd) - Automated cross-platform contact synchronization

## Summary
The Contact Sync Manager is an intelligent Uplizd workflow designed to bridge the gap between Chatwork and your primary CRM, ensuring contact information remains consistent and up-to-date across your entire tech stack. By automating the extraction and synchronization of contact data, this solution eliminates manual entry errors, reduces data fragmentation, and provides a single source of truth for your team's communication and relationship management pipelines.

---

## Demo
![Contact Sync Manager workflow interface showing Chatwork input nodes connected to CRM synchronization tools](image.png)
**Alt text (SEO-ready):** Contact Sync Manager workflow in Uplizd, automating Chatwork contact data synchronization with CRM platforms using Composio integrations.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADtJREFUeNpi/P//PwM1AQsAE8P///8Z/v//z8AARgYgA0YGBgYgA0YGBgYgA0YGBgYgA0YGBgYgA0YGAAMA5/0D/84318sAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/03067dfd-a083-5da3-8491-380f23418758)

---

## Category
- **Primary category:** CRM data
- **Secondary tags:** chatwork, contact sync, data hygiene, crm, automation, composio, ai workflow, lead management
- This solution bridges communication platforms and CRM databases to ensure contact data integrity and operational efficiency.

---

## Who is this for?
This workflow is designed for teams looking to unify their contact management processes across disparate messaging and sales platforms.

- **Sales Operations Manager**
    - Ensures that contact details captured in chat are immediately reflected in the CRM without manual intervention.
- **Account Executive**
    - Maintains accurate, real-time access to client contact information while working directly within Chatwork.
- **Customer Success Lead**
    - Reduces data decay by automating the sync of new contact touchpoints into the centralized database.
- **RevOps Analyst**
    - Standardizes contact formatting and reduces duplicate entries across the sales pipeline.

---

## Features
- **Real-time Synchronization**
    - Automatically pushes contact updates from Chatwork to your CRM as soon as new information is detected.
- **Intelligent Data Mapping**
    - Uses the Composio Toolset to intelligently map Chatwork user fields to the corresponding CRM contact schema.
- **Conflict Resolution**
    - Identifies and resolves data discrepancies between messaging platforms and CRM records to maintain high data hygiene.
- **Automated Enrichment**
    - Triggers enrichment workflows to append missing contact details during the synchronization process.
- **Error Handling & Logging**
    - Provides automated alerts and logs for any sync failures, ensuring no contact information is lost during the transfer.

---

## Use Cases
**CRM Data Integrity**
- Automatically update existing CRM contact records when a user changes their display name or status in Chatwork.
- Deduplicate contact entries by matching Chatwork identifiers against existing CRM email or phone number fields.

**Sales Pipeline Velocity**
- Instantly create new CRM leads from Chatwork conversations to ensure immediate follow-up by the sales team.
- Sync meeting notes and contact context from Chatwork threads directly into the CRM opportunity activity log.

**Operational Automation**
- Bulk-sync contact lists from Chatwork groups into CRM segments for targeted marketing campaigns.
- Archive inactive contacts from the CRM based on inactivity signals detected within Chatwork communication patterns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Contact Sync Manager template file provided in this repository.
3. Connect your Chatwork and CRM accounts via the integration settings.
4. Ensure nodes are correctly linked from the Chat Input to the final Chat Output to verify the data pipeline.

### 2) Setup the Nodes
- **Chat Input**: Receives raw contact data or trigger events from Chatwork.
- **Agent**: Processes, cleans, and formats the contact information for CRM compatibility.
- **Composio Toolset**: Executes the API calls to push or update records in your CRM.
- **Chat Output**: Confirms the successful sync or reports any errors back to the user.

### 3) Run the Flow
Use the Playground to test your sync logic with these example prompts:
- `Sync all new contacts from the 'Sales-Team' Chatwork group to Salesforce.`
- `Find and update the contact record for 'John Doe' in HubSpot using the latest Chatwork profile data.`
- `Check for duplicate contacts between Chatwork and my CRM and merge them based on email address.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic layer for mapping and cleaning data.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Extract contact name, email, and company from the input and map them to the CRM schema."
- Instruction: "If a field is missing, flag the record for manual review rather than creating an incomplete CRM entry."

### 2) Composio Toolset Node
- Authenticate with your CRM API key and ensure the connection scope includes `read` and `write` permissions for Contacts and Leads.

### 3) Tool Availability
- **CRM Connector**: Capabilities for `get_contact`, `create_contact`, `update_contact`, and `search_contacts`.
- **Chatwork Connector**: Capabilities for `list_contacts`, `get_user_info`, and `monitor_chat_events`.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) — Comprehensive multi-platform CRM data synchronization.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) — Automated cleanup and maintenance for CRM databases.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) — Manage sales stages and pipeline velocity effectively.
