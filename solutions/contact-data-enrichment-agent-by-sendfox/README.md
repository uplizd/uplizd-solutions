# Contact Data Enrichment Agent (Uplizd) - Automate CRM profile enrichment and data hygiene

## Summary
The Contact Data Enrichment Agent is an intelligent Uplizd workflow designed to automatically enhance contact profiles by sourcing missing information and populating custom fields. By leveraging the Composio Toolset to bridge your CRM with external data providers, this solution eliminates manual research, improves lead accuracy, and ensures your sales team always has a complete, actionable source of truth for every prospect.

---

## Demo
![Contact Data Enrichment Agent workflow showing CRM integration and data mapping](image.png)
**Alt text (SEO-ready):** Contact Data Enrichment Agent workflow in Uplizd, featuring automated CRM data synchronization, lead profile enhancement, and Composio toolset integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/f218e160-ba84-559b-8a74-ec427419eee5)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, data enrichment, lead qualification, data hygiene, sales operations, composio, ai workflow, prospect intelligence.  
This solution streamlines RevOps by automating the enrichment of contact records, ensuring high-quality data across your sales pipeline.

---

## Who is this for?
This agent is built for revenue-focused teams looking to reduce manual administrative overhead and improve lead conversion rates.

* **Sales Operations Manager**
    * Ensures CRM data hygiene and reduces the time spent on manual record updates.
* **Account Executive**
    * Gains immediate access to complete prospect profiles, allowing for more personalized outreach.
* **Growth Marketer**
    * Leverages enriched contact data to segment audiences more effectively for targeted campaigns.
* **Business Development Representative**
    * Increases pipeline velocity by having verified contact details ready for high-volume prospecting.

---

## Features
- **Automated Profile Enrichment**
  Automatically fetches missing contact details from external databases and updates CRM fields in real-time.
- **Custom Field Mapping**
  Seamlessly maps enriched data points to your specific CRM custom fields, ensuring compatibility with existing workflows.
- **Intelligent Data Validation**
  Uses AI to verify the accuracy of incoming data, preventing the entry of stale or incorrect contact information.
- **Composio Toolset Integration**
  Connects directly to your CRM and data providers via the Composio Toolset for secure, authenticated API interactions.
- **Event-Driven Updates**
  Triggers enrichment workflows automatically when a new contact is created or a specific field is updated in your CRM.

---

## Use Cases
**Lead Qualification**
* Automatically append job titles and company size to new leads to prioritize high-value prospects.
* Flag incomplete records for immediate enrichment before they reach the sales outreach stage.

**Data Hygiene & Maintenance**
* Periodically scan existing contact lists to fill in missing email addresses or phone numbers.
* Standardize formatting for location and industry fields across your entire CRM database.

**Sales Outreach Optimization**
* Populate custom fields with company revenue data to tailor messaging for account-based marketing (ABM).
* Ensure contact records are fully enriched before triggering automated email sequences in your CRM.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your CRM and data provider connections within the Composio Toolset node.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives the contact ID or email address to initiate the enrichment process.
* **Agent:** Orchestrates the logic, determining which data points are missing and requesting updates.
* **Composio Toolset:** Executes the API calls to your CRM and enrichment services to fetch and write data.
* **Chat Output:** Confirms the enrichment status and provides a summary of the updated fields.

### 3) Run the Flow
Use the Playground to test your enrichment logic with these prompts:
* `Enrich contact record for email: sales@example.com`
* `Check for missing industry and revenue data for contact ID: 98765`
* `Update all incomplete contact profiles created in the last 24 hours`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst, interpreting CRM records and deciding which enrichment tools to trigger.
* Use a model with strong reasoning capabilities (e.g., GPT-4o).
* Instruction: "Analyze the provided contact record, identify missing fields, and use the available tools to fetch and update the CRM."
* Ensure the agent is configured to handle null values gracefully.

### 2) Composio Toolset Node
* Provide your API key to enable secure communication between Uplizd and your CRM/Data providers.
* Set the connection scope to include read/write access for contact and lead objects.

### 3) Tool Availability
* **CRM Connector:** Read/Write access to Contact, Lead, and Account objects.
* **Enrichment API:** Capability to query external databases for professional contact information.
* **Validation Utility:** Tool to verify email syntax and phone number formatting.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Deep-dive research for B2B account profiles.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Multi-platform synchronization and conflict resolution.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automated cleanup and maintenance for CRM databases.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Automated prospecting and account intelligence.
