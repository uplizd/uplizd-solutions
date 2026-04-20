# UK Sales Compliance Agent (Uplizd) - Automate GDPR-compliant cold calling workflows

## Summary
The UK Sales Compliance Agent (Uplizd) streamlines outbound sales operations by automating Telephone Preference Service (TPS) and Corporate Telephone Preference Service (CTPS) checks. By integrating real-time compliance validation directly into your CRM pipeline, this workflow ensures that sales teams maintain strict adherence to UK data protection regulations, reducing legal risk while increasing pipeline velocity.

---

## Demo
![UK Sales Compliance Agent workflow interface showing CRM data validation and TPS check nodes](image.png)
**Alt text (SEO-ready):** UK Sales Compliance Agent (Uplizd) workflow interface showing CRM data validation, TPS check integration, and automated compliance reporting for sales teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b6bba47c-b0f5-5f6e-9713-48d040f6413a)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, gdpr, tps, compliance, sales, outbound, data hygiene, composio, ai workflow
- This solution bridges the gap between high-volume outbound sales and rigorous UK regulatory compliance standards.

---

## Who is this for?
This solution is designed for sales and operations teams managing outbound lead generation within the United Kingdom.

- **Sales Operations Manager**
    - Automates compliance checks to ensure all lead lists are scrubbed before reaching the sales floor.
- **Compliance Officer**
    - Maintains a digital audit trail of all TPS/CTPS verification attempts for regulatory reporting.
- **Outbound SDR**
    - Prevents wasted effort by automatically filtering out non-compliant numbers from daily calling queues.
- **RevOps Lead**
    - Standardizes data hygiene across CRM platforms to protect brand reputation and avoid regulatory fines.

---

## Features
- **Automated TPS/CTPS Scrubbing**
    - Real-time validation of phone numbers against official UK preference databases to ensure legal outreach.
- **CRM Integration**
    - Seamlessly syncs with your CRM to flag, update, or remove records based on compliance status.
- **Intelligent Routing**
    - Automatically routes compliant leads to active calling queues while quarantining restricted entries.
- **Audit Logging**
    - Generates detailed logs of compliance checks, providing a single source of truth for internal reviews.
- **Composio Toolset Connectivity**
    - Leverages the Composio Toolset to execute complex API calls across CRM and compliance verification services.

---

## Use Cases
**Lead List Hygiene**
- Automatically scrub imported CSV lead lists against the latest TPS/CTPS registry before CRM ingestion.
- Flag existing CRM contacts that have recently registered with the TPS to prevent accidental outreach.

**Outbound Campaign Protection**
- Validate individual phone numbers in real-time during the lead qualification process.
- Prevent sales agents from initiating calls to numbers identified as "Do Not Call" by UK regulations.

**Regulatory Reporting**
- Generate weekly compliance summaries showing the volume of scrubbed leads and total risk exposure.
- Maintain a persistent record of compliance verification for GDPR and PECR audit requirements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your CRM and compliance verification API credentials within the integration settings.
3. Map your CRM lead fields to the agent's input parameters.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives lead data or manual phone number queries for validation.
- **Agent**: Analyzes the request and triggers the appropriate compliance check logic.
- **Composio Toolset**: Executes the API calls to the TPS/CTPS database and updates the CRM.
- **Chat Output**: Returns the validation status and compliance action taken to the user.

### 3) Run the Flow
Use the Playground to test your compliance logic with these prompts:
- `Check if the phone number +44 7700 900000 is registered on the TPS.`
- `Scrub the current list of leads in the 'New Prospect' CRM view for compliance.`
- `Provide a summary of all leads flagged as non-compliant in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the compliance orchestrator, interpreting data and triggering API actions.
- Use a model capable of high-precision instruction following.
- System prompt should prioritize regulatory accuracy over conversational flair.
- Ensure the agent is restricted to read/write access only for the specific CRM fields required for compliance.

### 2) Composio Toolset Node
- Provide your API keys for both the CRM and the TPS/CTPS verification service.
- Set the connection scope to include read access for lead lists and write access for compliance status fields.

### 3) Tool Availability
- **CRM Connector**: For fetching lead data and updating compliance status fields.
- **TPS/CTPS Validator**: For performing the actual database lookup.
- **Data Logger**: For recording verification timestamps and results.

---

## Related Solutions
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automates data cleanup and formatting for cleaner CRM records.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes lead data across multiple platforms with conflict resolution.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Optimizes sales stages and tracks stalled opportunities.
