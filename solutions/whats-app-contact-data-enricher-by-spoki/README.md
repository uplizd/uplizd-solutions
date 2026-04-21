# WhatsApp Contact Data Enricher (Uplizd) - Automated CRM Synchronization and Profile Enrichment

## Summary
The WhatsApp Contact Data Enricher (Uplizd) is an intelligent automation workflow designed to bridge the gap between WhatsApp messaging and your CRM. By leveraging the Composio Toolset, this solution automatically extracts contact details from incoming WhatsApp conversations, cross-references them with existing records, and enriches your database with updated fields. This workflow ensures your customer data remains accurate and actionable, significantly reducing manual entry time and improving pipeline velocity for sales and support teams.

---

## Demo
![WhatsApp Contact Data Enricher workflow diagram showing data flow from WhatsApp to CRM](image.png)
**Alt text (SEO-ready):** WhatsApp Contact Data Enricher workflow diagram for automated CRM synchronization, contact profile enrichment, and data hygiene using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7c7f3f5c-97a3-5306-8c56-067af9688cf0)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** whatsapp, spoki, crm, data enrichment, contact management, sales automation, composio, ai workflow
- This solution streamlines the synchronization of messaging data into centralized CRM systems to maintain a single source of truth for customer profiles.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual data entry and maintain high-quality contact records across their communication channels.

- **Sales Representatives**
    - Automatically update prospect information during active conversations to keep CRM records current.
- **Customer Success Managers**
    - Ensure support interactions are logged against the correct contact profile with enriched metadata.
- **RevOps Specialists**
    - Maintain data hygiene by automating the ingestion of contact signals from messaging platforms.
- **Marketing Managers**
    - Capture lead intelligence from WhatsApp interactions to improve segmentation and targeting accuracy.

---

## Features
- **Real-time Data Extraction**
    - Automatically parses incoming WhatsApp messages to identify and extract key contact attributes.
- **Intelligent CRM Mapping**
    - Uses the Composio Toolset to map extracted data points directly to custom fields in your CRM.
- **Automated Profile Enrichment**
    - Cross-references existing CRM records to update missing information without manual intervention.
- **Conflict Resolution Logic**
    - Ensures that the most recent information from WhatsApp takes precedence during the synchronization process.
- **Seamless Integration Workflow**
    - Connects WhatsApp (via Spoki) and your CRM through a unified, low-latency AI pipeline.

---

## Use Cases
**Lead Qualification**
- Automatically tag leads based on intent signals detected during WhatsApp conversations.
- Populate lead source fields in the CRM based on the specific WhatsApp campaign or thread.

**Customer Data Hygiene**
- Standardize contact formatting (e.g., phone numbers, job titles) as they are ingested from WhatsApp.
- Flag incomplete contact profiles for follow-up by the sales team.

**Relationship Management**
- Log interaction history directly into the CRM to provide a 360-degree view of the customer.
- Sync custom notes from WhatsApp chats into the CRM activity feed for historical tracking.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the WhatsApp Contact Data Enricher template from the marketplace.
3. Authenticate your Spoki and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped and the agent is connected to the Composio Toolset.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming WhatsApp messages and contact metadata.
- **Agent**: Analyzes the message content and determines which fields require enrichment.
- **Composio Toolset**: Executes the API calls to update the CRM with the parsed data.
- **Chat Output**: Confirms the successful enrichment or logs an error if data validation fails.

### 3) Run the Flow
Open the Playground and test the workflow with the following prompts:
- `Enrich the contact record for the incoming WhatsApp message from +1234567890.`
- `Extract job title and company from the latest chat and update the CRM profile.`
- `Sync all pending contact updates from the last 24 hours of WhatsApp activity.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the intelligent bridge between unstructured chat data and structured CRM fields.
- Use a model capable of high-precision entity extraction (e.g., GPT-4o).
- Instruct the agent to prioritize existing record IDs to prevent duplicate creation.
- Configure the agent to normalize data formats (e.g., ISO date formats) before pushing to the CRM.

### 2) Composio Toolset Node
- Provide your API key for the CRM and Spoki integrations.
- Set the connection scope to allow read/write access for contact and activity objects.

### 3) Tool Availability
- **CRM Search Tool**: Locates existing contact records by phone number or email.
- **CRM Update Tool**: Modifies specific fields (e.g., "Last Contacted," "Job Title") in the CRM.
- **WhatsApp Parser**: Extracts structured entities from raw message strings.

---

## Related Solutions
- [WhatsApp Lead Nurturing Agent (Spoki)](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automate follow-ups and lead engagement sequences.
- [WhatsApp Support Ticket Manager (Spoki)](../whats-app-support-ticket-manager-by-spoki/README.md) - Convert WhatsApp queries into organized support tickets.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms to ensure consistency.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and standardize your CRM database automatically.
