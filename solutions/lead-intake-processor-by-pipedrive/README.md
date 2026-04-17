# Lead Intake Processor (Uplizd) - Automate inbound lead qualification and CRM synchronization

## Summary
The Lead Intake Processor is an automated Uplizd AI workflow designed to ingest, qualify, and route inbound leads from Pipedrive directly into your sales pipeline. By leveraging the Composio Toolset to interface with CRM data, this solution eliminates manual data entry, ensures immediate lead response times, and maintains high data hygiene, allowing sales teams to focus on high-intent prospects rather than administrative triage.

---

## Demo
![Lead Intake Processor workflow showing automated lead qualification and Pipedrive CRM synchronization](image.png)
**Alt text (SEO-ready):** Lead Intake Processor Uplizd workflow for automated CRM lead qualification, Pipedrive integration, and sales pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/295d8ddb-50c0-50f0-8571-2806b7480c27)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, pipedrive, lead qualification, sales pipeline, data sync, automation, composio, ai workflow
- This solution streamlines the transition from raw lead capture to actionable CRM opportunity, ensuring no prospect is left behind.

---

## Who is this for?
This solution is built for revenue-focused teams looking to reduce lead response latency and improve conversion rates.

- **Sales Development Representative (SDR)**
    - Reduces time spent manually entering lead details, allowing for faster outreach.
- **Revenue Operations Manager**
    - Ensures consistent lead data formatting and pipeline hygiene across the CRM.
- **Sales Manager**
    - Provides real-time visibility into incoming lead quality and team performance.
- **Marketing Operations Lead**
    - Bridges the gap between lead generation campaigns and sales execution.

---

## Features
- **Automated Lead Ingestion**
    - Seamlessly captures inbound lead data and triggers the qualification workflow in real-time.
- **Intelligent Qualification**
    - Uses AI to score and categorize leads based on predefined criteria before pushing to Pipedrive.
- **Pipedrive CRM Integration**
    - Automatically creates or updates contacts and deals within Pipedrive using the Composio Toolset.
- **Data Hygiene Enforcement**
    - Standardizes lead information and removes duplicates to maintain a clean CRM database.
- **Instant Notification Routing**
    - Alerts the appropriate sales owner immediately upon successful lead qualification and CRM entry.

---

## Use Cases
**Lead Qualification & Triage**
- Automatically filter incoming leads based on company size, industry, or specific intent signals.
- Route high-priority leads to senior account executives while tagging others for automated nurturing.

**CRM Data Synchronization**
- Map incoming web-form fields directly to Pipedrive custom fields for comprehensive record-keeping.
- Resolve data conflicts between existing CRM contacts and new inbound lead submissions.

**Pipeline Velocity Optimization**
- Trigger immediate follow-up tasks in Pipedrive to ensure sales reps engage prospects within minutes.
- Update deal stages automatically based on qualification status to keep the sales pipeline moving.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the builder.
3. Authenticate your Pipedrive account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data strings or JSON payloads from your intake source.
- **Agent**: Processes the input, performs qualification logic, and determines the CRM action.
- **Composio Toolset**: Executes the Pipedrive API calls to create or update records.
- **Chat Output**: Confirms the successful creation of the lead or reports any processing errors.

### 3) Run the Flow
Use the Uplizd Playground to test your workflow with these prompts:
- `Process this new lead: John Doe from Acme Corp, interested in Enterprise plan, phone 555-0199.`
- `Qualify the following lead and add to Pipedrive: Sarah Smith, CTO at TechFlow, budget $50k.`
- `Check for existing contact for 'Jane Miller' and update her deal stage to 'Qualified'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic layer for lead assessment.
- **Recommended instruction pattern:**
    - "Act as a Sales Operations assistant; extract lead details from the input and map them to Pipedrive fields."
    - "Evaluate the lead's intent; if they meet the 'Enterprise' criteria, tag as 'High Priority'."
    - "Always check for existing records before creating a new entry to prevent duplicates."

### 2) Composio Toolset Node
- Requires a valid Pipedrive API key configured in your Composio dashboard.
- Ensure the connection scope includes `deals.create`, `deals.update`, and `persons.search`.

### 3) Tool Availability
- **Pipedrive Search**: Locate existing contacts or organizations.
- **Pipedrive Create**: Generate new deals and person records.
- **Pipedrive Update**: Modify deal stages and custom field data.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on incoming leads.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and track deal progression through sales stages.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate CRM records automatically.
