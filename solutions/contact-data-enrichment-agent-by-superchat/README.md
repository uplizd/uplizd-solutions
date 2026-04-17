# Contact Data Enrichment Agent (Uplizd) - Automated customer profile enhancement

## Summary
The Contact Data Enrichment Agent is an intelligent Uplizd workflow designed to automatically aggregate conversation insights and behavioral data into your CRM. By leveraging the Composio Toolset to bridge communication platforms with your database, this solution eliminates manual data entry, ensures a single source of truth for customer profiles, and significantly improves pipeline velocity through real-time data hygiene.

---

## Demo
![Contact Data Enrichment Agent workflow diagram showing data flow from chat inputs to CRM enrichment](image.png)

**Alt text (SEO-ready):** Contact Data Enrichment Agent workflow diagram showing data flow from chat inputs to CRM enrichment via Uplizd and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3c939917-930d-511e-ba8e-d24d14bb7186)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** crm, data enrichment, customer insights, sales automation, data hygiene, composio, ai workflow
- This solution streamlines the synchronization of unstructured conversation data into structured CRM fields to maintain high-quality customer records.

---

## Who is this for?
This solution is built for revenue-focused teams looking to turn every customer interaction into actionable data.

- **Sales Operations Manager**
    - Automates the population of custom CRM fields to ensure reporting accuracy without manual intervention.
- **Account Executive**
    - Gains immediate visibility into lead sentiment and behavioral signals directly within the contact record.
- **Customer Success Lead**
    - Maintains an up-to-date profile of client needs and pain points based on recent support or chat history.
- **Growth Marketer**
    - Leverages enriched demographic and interaction data to segment audiences for more personalized outreach campaigns.

---

## Features
- **Automated Insight Extraction**
    - Uses advanced LLMs to parse unstructured chat logs and identify key customer attributes or intent signals.
- **Real-time CRM Sync**
    - Instantly pushes enriched data points to your CRM using the Composio Toolset for seamless integration.
- **Intelligent Data Mapping**
    - Dynamically maps extracted conversation entities to the correct CRM fields, ensuring consistent data formatting.
- **Conflict Resolution Logic**
    - Prevents data overwrites by validating incoming information against existing CRM records before updating.
- **Workflow Observability**
    - Provides transparent logging of every enrichment step, allowing for easy audit and performance tuning of the agent.

---

## Use Cases
**Lead Qualification & Scoring**
- Automatically update lead scores based on specific keywords or intent detected during initial chat interactions.
- Flag high-intent contacts for immediate follow-up by updating the "Lead Status" field in your CRM.

**Customer Profile Maintenance**
- Sync updated contact details, such as job titles or company changes, discovered during routine support conversations.
- Populate "Last Interaction Summary" fields to provide a historical context for future sales or support calls.

**Sales Pipeline Hygiene**
- Identify stalled opportunities by monitoring engagement signals and updating "Last Activity" timestamps automatically.
- Ensure all required fields for deal progression are populated by prompting the agent to extract missing info from chat logs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the workflow to your Uplizd workspace.
3. Connect your preferred CRM and communication platform via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are saved in the environment configuration.

### 2) Setup the Nodes
- **Chat Input**: Receives raw conversation data or trigger events from your communication platform.
- **Agent**: Processes the input, extracts key data points, and determines the appropriate CRM update action.
- **Composio Toolset**: Executes the API calls to read from or write to your CRM database securely.
- **Chat Output**: Confirms the successful enrichment of the contact record or flags the entry for manual review.

### 3) Run the Flow
Test the agent in the Uplizd Playground with these example prompts:
- `Extract the company size and industry from the last 5 messages and update the CRM profile.`
- `Analyze the sentiment of this conversation and add a summary note to the contact record.`
- `Identify any missing contact information in the current chat and update the corresponding CRM fields.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node requires a model capable of structured data extraction.
- **Recommended instruction pattern:**
    - Act as a data enrichment specialist that extracts key entities from unstructured text.
    - Prioritize accuracy by cross-referencing extracted data with existing CRM field constraints.
    - Maintain a professional, concise tone when summarizing interactions for CRM notes.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key in the node settings.
- **Connection Scope:** Ensure the connection has read/write permissions for the specific CRM objects (e.g., Contacts, Leads, Accounts) you intend to enrich.

### 3) Tool Availability
- **CRM Connector:** Enables reading and writing to standard and custom objects.
- **Text Parser:** Specialized tool for identifying entities like email, phone, company, and intent.
- **Data Validator:** Ensures that the formatted output matches the schema requirements of the target CRM.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automates the collection of firmographic data for enriched lead profiles.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Manages multi-platform data synchronization and conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Cleans and standardizes CRM records to prevent data decay.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Provides deep-dive research on accounts to support sales outreach.
