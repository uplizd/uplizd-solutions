# Lead Qualification Agent (Uplizd) - Automate lead scoring and CRM routing

## Summary
The Lead Qualification Agent by Fireberry is an intelligent workflow designed to streamline your sales pipeline by automatically evaluating incoming leads against your specific business criteria. By leveraging the Composio Toolset to interface directly with your CRM, this agent ensures that only high-intent prospects reach your sales team, reducing manual data entry, eliminating lead leakage, and significantly accelerating pipeline velocity.

---

## Demo
![Lead Qualification Agent workflow showing CRM integration and automated scoring logic](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow by Uplizd for automated CRM lead scoring, pipeline routing, and sales automation using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a80d8711-c196-58b5-b30a-72124dace5ff)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, fireberry, lead scoring, pipeline, sales operations, data sync, composio, ai workflow
This solution bridges the gap between raw lead intake and actionable sales intelligence, ensuring your CRM remains a clean, high-performing source of truth.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to eliminate manual qualification bottlenecks and improve lead-to-opportunity conversion rates.

* **Sales Operations Manager**
    * Automates lead routing rules to ensure equitable distribution and faster response times.
* **Account Executive**
    * Receives only pre-qualified leads with enriched context, allowing for more personalized outreach.
* **BDR/SDR Lead**
    * Spends less time on manual data hygiene and more time engaging with high-intent prospects.
* **Revenue Operations Lead**
    * Maintains a standardized qualification framework across the entire organization for better forecasting.

---

## Features
- **Automated Lead Scoring**
    Real-time evaluation of incoming leads based on custom parameters like company size, industry, and engagement signals.
- **CRM Integration**
    Seamless connectivity with Fireberry and other major CRMs to read lead data and update status fields automatically.
- **Intelligent Routing**
    Dynamic assignment of leads to the appropriate account owner based on predefined territory or expertise rules.
- **Data Hygiene Enforcement**
    Standardizes lead information formats upon entry, preventing duplicate records and incomplete contact profiles.
- **Real-time Notification**
    Triggers instant alerts to sales representatives when a high-value lead meets the qualification threshold.

---

## Use Cases
**Pipeline Acceleration**
* Automatically move leads that meet "Hot" criteria to the "Discovery" stage in your CRM.
* Flag stalled leads for immediate follow-up if they haven't been contacted within 24 hours.

**Lead Enrichment & Scoring**
* Cross-reference incoming lead data with existing account intelligence to assign a priority score.
* Automatically append missing firmographic data to new leads to assist in better segmentation.

**Sales Operations Efficiency**
* Route inbound leads based on current lead volume to ensure balanced workloads across the team.
* Archive or nurture low-intent leads automatically to keep the active pipeline focused on high-probability deals.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Lead Qualification Agent.
2. Click "Import" to add the workflow template to your workspace.
3. Authenticate your CRM and Composio Toolset credentials in the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the raw lead data payload or manual trigger request.
* **Agent**: Processes the lead data against your qualification logic and instructions.
* **Composio Toolset**: Executes CRM API calls to update lead status, scores, and owner fields.
* **Chat Output**: Returns a summary of the action taken (e.g., "Lead qualified and assigned to John Doe").

### 3) Run the Flow
Use the Playground to test your qualification logic with these example prompts:
* `Qualify the latest leads from the webform and assign them to the appropriate sales rep.`
* `Score all new leads created in the last 24 hours and update their status to 'Qualified' if they meet the enterprise criteria.`
* `Check for missing industry data on new leads and update the CRM records accordingly.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine that interprets lead data and applies business rules.
* Prioritize accuracy and adherence to the provided qualification rubric.
* Use the Composio Toolset to perform CRUD operations on CRM objects.
* Maintain a professional, objective tone when summarizing actions taken in the output.

### 2) Composio Toolset Node
* **API Key**: Ensure your Composio API key is active and has the necessary permissions for your CRM.
* **Connection Scope**: Grant read/write access to lead, contact, and account objects within your CRM.

### 3) Tool Availability
* **CRM Read/Write**: Capability to fetch lead details and update custom fields.
* **Data Validation**: Logic to verify email formats and company domain existence.
* **Routing Logic**: Ability to map leads to specific user IDs based on territory rules.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich lead profiles with deep firmographic data.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and track the progress of qualified opportunities.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple platforms.
