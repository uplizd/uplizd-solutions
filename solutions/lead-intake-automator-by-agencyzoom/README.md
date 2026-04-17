# Lead Intake Automator (Uplizd) - Streamline insurance lead capture and processing

## Summary
The Lead Intake Automator by AgencyZoom is an intelligent AI workflow designed to capture, qualify, and route incoming insurance leads from multiple digital channels into your CRM. By automating the ingestion of lead data, this solution eliminates manual entry errors, accelerates response times, and ensures that high-priority prospects are immediately assigned to the right agents, driving higher conversion rates and improved pipeline velocity.

---

## Demo
![Lead Intake Automator workflow diagram showing AgencyZoom lead capture, AI qualification, and CRM routing](image.png)
**Alt text (SEO-ready):** Uplizd Lead Intake Automator workflow for AgencyZoom, automating insurance lead qualification, data synchronization, and CRM routing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/dcabf775-c459-5a7d-9c6d-28fe90d1fe15)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** insurance, lead management, agencyzoom, crm, data sync, ai workflow, lead qualification, sales operations
- This solution bridges the gap between raw lead intake and actionable CRM data, providing a unified pipeline for insurance agencies.

---

## Who is this for?
This workflow is built for insurance professionals and sales teams looking to scale their operations without increasing manual administrative overhead.

- **Sales Managers**
    - Gain real-time visibility into lead volume and quality across all intake channels.
- **Insurance Agents**
    - Receive pre-qualified leads directly in the CRM, allowing for faster outreach and follow-up.
- **RevOps Specialists**
    - Standardize lead entry formats and ensure data hygiene across the entire sales funnel.
- **Agency Owners**
    - Reduce lead response time and maximize ROI on marketing spend through automated routing.

---

## Features
- **Automated Lead Ingestion**
    - Seamlessly captures incoming lead data from web forms, emails, and AgencyZoom triggers.
- **AI-Powered Qualification**
    - Uses intelligent agents to score leads based on predefined criteria before they reach your team.
- **Real-Time CRM Sync**
    - Leverages the Composio Toolset to push clean, formatted lead data directly into your CRM environment.
- **Intelligent Routing**
    - Automatically assigns leads to specific agents based on territory, product line, or lead score.
- **Data Hygiene Enforcement**
    - Cleans and validates contact information during the intake process to prevent duplicate or incomplete records.

---

## Use Cases
**Lead Lifecycle Management**
- Automatically parse incoming lead emails into structured CRM contact fields.
- Trigger immediate follow-up tasks for high-intent leads identified during the intake process.

**Sales Pipeline Optimization**
- Route high-value insurance prospects to senior agents based on real-time scoring.
- Update deal stages automatically as new information is captured from the lead source.

**Operational Efficiency**
- Eliminate manual data entry by syncing AgencyZoom lead data with secondary marketing platforms.
- Standardize lead formatting to ensure consistent reporting across all agency branches.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the workflow.
3. Authenticate your AgencyZoom and CRM connections via the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data strings or webhooks.
- **Agent**: Processes the data, performs qualification, and maps fields.
- **Composio Toolset**: Executes the API calls to update your CRM and AgencyZoom.
- **Chat Output**: Confirms successful lead processing and routing to the user.

### 3) Run the Flow
Use the Playground to test your intake logic with these prompts:
- `Process the latest lead from the web form and assign it to the commercial insurance queue.`
- `Qualify this lead based on the provided coverage requirements and update the CRM status.`
- `Sync the new lead data from AgencyZoom and notify the assigned agent via email.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for parsing and decision-making.
- Configure the system prompt to recognize insurance-specific terminology.
- Set the temperature to 0.2 for consistent, accurate data extraction.
- Define clear mapping rules for CRM field population.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication with your CRM and AgencyZoom.
- Define the connection scope to allow read/write access to lead and contact objects.

### 3) Tool Availability
- **AgencyZoom Connector**: For retrieving and updating lead records.
- **CRM API**: For creating new contacts and updating pipeline stages.
- **Data Validation Utility**: For ensuring phone and email formats are correct.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on incoming leads.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistency across multiple CRM platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages after lead intake.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich lead data with external intelligence.
