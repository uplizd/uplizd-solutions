# Lead Intake Processor (Uplizd) - Automated CRM lead organization and qualification

## Summary
The Lead Intake Processor is an intelligent Uplizd workflow designed to streamline the transition of raw inquiries into structured CRM records. By automating the extraction, validation, and entry of lead data, this solution eliminates manual data entry bottlenecks, ensures immediate response times, and maintains a single source of truth for your sales pipeline.

---

## Demo
![Lead Intake Processor workflow diagram showing automated data extraction from chat inputs into CentralStationCRM via Composio](image.png)
**Alt text (SEO-ready):** Lead Intake Processor (Uplizd) workflow diagram showing automated data extraction from chat inputs into CentralStationCRM via Composio toolset integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a8339241-48cf-5f37-8abd-c22a9e010107)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead management, centralstationcrm, data entry, sales pipeline, lead qualification, composio, ai workflow
- This solution bridges the gap between initial prospect interest and CRM readiness by automating the ingestion and categorization of lead data.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce administrative overhead and accelerate lead velocity.

- **Sales Development Representative (SDR)**
    - Eliminates manual CRM entry, allowing for immediate focus on high-value outreach.
- **Revenue Operations Manager**
    - Ensures consistent data hygiene and standardized lead formatting across the sales pipeline.
- **Small Business Owner**
    - Provides enterprise-grade lead organization without the need for dedicated administrative staff.
- **Customer Success Lead**
    - Enables rapid hand-off of qualified leads to the appropriate account managers.

---

## Features
- **Automated Data Extraction**
    - Uses AI to parse unstructured lead inquiries and extract key contact details like name, email, and company.
- **CentralStationCRM Integration**
    - Seamlessly pushes validated lead data directly into your CRM using the Composio Toolset.
- **Real-time Lead Validation**
    - Verifies lead information against predefined criteria before creating new records to prevent duplicate entries.
- **Intelligent Routing**
    - Automatically assigns leads to appropriate pipeline stages based on the context of the initial inquiry.
- **Workflow Transparency**
    - Provides clear logging of every lead processed, ensuring full visibility into the intake pipeline.

---

## Use Cases
**Lead Capture Optimization**
- Automatically ingest leads from email or chat platforms directly into CentralStationCRM.
- Normalize contact fields and phone formats during the intake process to maintain database quality.

**Pipeline Velocity Acceleration**
- Trigger instant CRM record creation to ensure sales teams can follow up within minutes of an inquiry.
- Automatically flag high-intent leads for priority routing to senior account executives.

**Data Hygiene Maintenance**
- Filter out spam or incomplete inquiries before they reach your active sales pipeline.
- Standardize lead source attribution by automatically tagging incoming records based on the input channel.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Intake Processor template from the marketplace.
3. Connect your CentralStationCRM account via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead inquiries from your communication channels.
- **Agent**: Analyzes the input, extracts contact entities, and determines lead readiness.
- **Composio Toolset**: Executes the API calls required to create or update records in CentralStationCRM.
- **Chat Output**: Confirms successful lead processing or requests missing information from the sender.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Process this inquiry: John Doe from Acme Corp wants a demo, contact him at john@acme.com.`
- `Add a new lead: Sarah Smith, CTO at TechFlow, interested in our enterprise plan.`
- `Create a record for Mike Ross at LawFirm, phone 555-0199, inquiry regarding service pricing.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary intelligence layer for data extraction and intent classification.
- **Instruction Pattern:**
    - Extract name, company, email, and intent from the provided text.
    - Validate that all mandatory CRM fields are present before proceeding.
    - Maintain a professional and helpful tone for all output confirmations.

### 2) Composio Toolset Node
- **API Key:** Ensure your CentralStationCRM API key is active within the Composio dashboard.
- **Connection Scope:** Grant read/write permissions for contacts and lead objects to enable full automation.

### 3) Tool Availability
- **CRM Contact Management:** Create, update, and search for contact records.
- **Lead Pipeline Management:** Assign leads to specific stages and update status fields.
- **Data Validation Utilities:** Format phone numbers and verify email syntax before CRM submission.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) - Synchronize lead data across multiple platforms to maintain a single source of truth.
- [../crm-data-hygiene-manager/README.md](CRM Data Hygiene Manager) - Automate the cleanup of decayed or duplicate records in your CRM.
- [../deal-pipeline-manager/README.md](Deal Pipeline Manager) - Manage deal stages and follow-up cadences for qualified leads.
