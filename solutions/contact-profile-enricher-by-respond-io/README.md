# Contact Profile Enricher (Uplizd) - Automated CRM data enrichment from messaging conversations

## Summary
The Contact Profile Enricher (Uplizd) is an intelligent automation workflow that extracts key customer data from messaging conversations and synchronizes it directly into your CRM. By leveraging the Composio Toolset, this solution eliminates manual data entry, ensures your contact profiles are always up-to-date, and provides a single source of truth for customer intelligence derived from real-time interactions.

---

## Demo
![Contact Profile Enricher workflow showing data extraction from chat to CRM](image.png)
**Alt text (SEO-ready):** Contact Profile Enricher workflow by Uplizd, automating CRM data synchronization and customer profile enrichment from messaging platforms via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-1dc49543--12a0--5150--b5a1--4b23a7cd2b92-blue)](https://uplizd.ai/solutions/1dc49543-12a0-5150-b5a1-4b23a7cd2b92)

---

## Category
**Primary category:** CRM data
**Secondary tags:** crm, contact enrichment, messaging, data sync, automation, customer intelligence, composio, ai workflow.
This solution bridges the gap between conversational messaging platforms and your CRM, ensuring every customer interaction contributes to a richer, more accurate database.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual data entry and maintain high-quality customer records.

- **Sales Representatives**
    - Automatically capture lead details and preferences without switching windows.
- **Customer Success Managers**
    - Maintain accurate account history by logging conversation insights directly to the CRM.
- **RevOps Specialists**
    - Ensure data hygiene and consistency across the sales pipeline through automated enrichment.
- **Support Leads**
    - Centralize customer feedback and profile updates to improve response personalization.

---

## Features
- **Automated Data Extraction**
  Intelligently parses unstructured chat text to identify names, emails, job titles, and company information.
- **Real-time CRM Sync**
  Utilizes the Composio Toolset to push enriched data directly into your CRM records instantly.
- **Intelligent Conflict Resolution**
  Automatically compares incoming data with existing CRM entries to prevent duplicates and overwrite errors.
- **Contextual Enrichment**
  Adds conversation summaries and sentiment tags to contact profiles for better sales and support visibility.
- **Customizable Mapping**
  Easily map extracted conversation variables to specific CRM fields, ensuring data lands exactly where it is needed.

---

## Use Cases
**Lead Qualification**
- Automatically populate CRM lead fields when a prospect shares their company or role during a chat.
- Flag high-intent contacts for immediate follow-up based on keywords detected in the conversation.

**Customer Data Maintenance**
- Update existing contact phone numbers or email addresses when a customer provides new details in a support thread.
- Append conversation transcripts to the contact's activity history for a complete audit trail.

**Sales Pipeline Hygiene**
- Sync meeting availability or interest levels mentioned in chats to the corresponding CRM opportunity fields.
- Standardize contact formatting across the database to improve reporting and outreach accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your preferred workspace and project folder.
3. Authenticate your CRM and messaging platform connections within the builder.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw conversation text from your messaging platform.
- **Agent**: Processes the text, identifies key entities, and structures the data for the CRM.
- **Composio Toolset**: Executes the API calls to update or create contact records in your CRM.
- **Chat Output**: Confirms to the user that the profile has been successfully enriched.

### 3) Run the Flow
Use the Playground to test the extraction logic with these prompts:
- `Extract contact details from this message: "Hi, I'm John Doe, I work as a Lead Developer at Acme Corp and my email is john@acme.com."`
- `Update the CRM profile for the current user with the following info: "Interested in the enterprise plan, budget is $50k."`
- `Find the contact record for Sarah Smith and add the note: "Requested a demo for next Tuesday."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, transforming raw chat data into structured CRM objects.
- Use a model with strong entity extraction capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions to prioritize existing record matching before creating new entries.
- Ensure the system prompt includes the specific CRM field schema required for your organization.

### 2) Composio Toolset Node
- Provide your unique API key to enable secure communication between Uplizd and your CRM.
- Configure the connection scope to allow read/write access to your Contacts and Leads modules.

### 3) Tool Availability
- **CRM Search**: Locates existing contacts by email or name to prevent duplicates.
- **CRM Update**: Modifies specific fields based on extracted conversation data.
- **CRM Create**: Initializes new contact profiles when no existing record is found.

---

## Related Solutions
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate bulk cleanup and formatting of your CRM database.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-up tasks for active opportunities.
