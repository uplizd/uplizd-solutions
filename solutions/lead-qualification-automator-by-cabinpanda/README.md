# Lead Qualification Automator (Uplizd) - Streamline lead scoring and routing for faster sales cycles

## Summary
The Lead Qualification Automator is an intelligent Uplizd workflow designed to ingest raw lead data, evaluate prospect fit against predefined criteria, and automatically route qualified leads to the appropriate sales pipeline. By leveraging AI-driven analysis, this solution eliminates manual data entry and ensures that high-intent prospects are prioritized, significantly increasing pipeline velocity and improving lead-to-opportunity conversion rates for revenue teams.

---

## Demo
![Lead Qualification Automator workflow diagram showing data ingestion, AI scoring, and CRM routing](image.png)
**Alt text (SEO-ready):** Lead Qualification Automator workflow diagram showing data ingestion, AI scoring, and CRM routing within the Uplizd platform and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/26699a79-b13f-5556-a42b-c1dc850e4df2)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, lead qualification, sales pipeline, lead scoring, data sync, ai workflow, composio, revenue operations
This solution optimizes the sales funnel by automating the transition from raw lead capture to actionable sales opportunity.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to reduce manual administrative overhead and improve lead response times.

* **Sales Development Rep (SDR):**
    * Spend less time on manual lead research and more time engaging with high-intent prospects.
* **Revenue Operations Manager:**
    * Standardize lead qualification criteria across the organization to ensure consistent data hygiene.
* **Sales Manager:**
    * Gain real-time visibility into lead quality and ensure that the best opportunities are routed to the right account executives.
* **Marketing Operations Specialist:**
    * Close the loop between lead generation campaigns and sales follow-up by automating the hand-off process.

---

## Features
- **Automated Lead Scoring**
    AI-driven evaluation of incoming leads based on firmographic data, intent signals, and historical conversion patterns.
- **Intelligent Routing Logic**
    Dynamic assignment of leads to specific sales queues or account owners based on territory, industry, or company size.
- **CRM Data Synchronization**
    Seamless integration with major CRM platforms via the Composio Toolset to ensure lead records are updated in real-time.
- **Custom Qualification Criteria**
    Flexible configuration settings that allow teams to define their own "Ideal Customer Profile" (ICP) thresholds.
- **Real-time Alerting**
    Instant notifications to sales reps when a high-priority lead is qualified and ready for immediate outreach.

---

## Use Cases
**Lead Prioritization**
* Automatically flag leads that match the ICP for immediate follow-up by the BDR team.
* Filter out low-intent or non-target leads to keep the sales pipeline clean and focused.

**CRM Enrichment & Hygiene**
* Automatically populate missing company details (e.g., employee count, revenue) using external data providers.
* Standardize lead formatting and contact information before syncing to the CRM to prevent duplicate records.

**Pipeline Velocity Optimization**
* Reduce the time-to-first-contact by automating the hand-off from marketing automation tools to sales CRM.
* Trigger automated follow-up tasks in the CRM for leads that meet specific engagement thresholds.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the builder.
3. Authenticate your CRM and data provider connections within the Composio dashboard.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives raw lead data from webhooks or manual uploads.
* **Agent:** Analyzes lead data against your defined ICP and qualification rules.
* **Composio Toolset:** Executes CRM updates, lead creation, and data enrichment tasks.
* **Chat Output:** Confirms the qualification status and routing destination to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
* `Qualify this lead: {name: "John Doe", company: "TechCorp", role: "CTO"}`
* `Check if this lead matches our enterprise ICP and update Salesforce.`
* `Route this high-intent lead to the North American sales queue.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for lead qualification.
* **Recommended instruction pattern:**
    * Define the specific ICP attributes (e.g., industry, company size, budget).
    * Instruct the agent to output a qualification score (1-10) for every lead.
    * Provide clear logic for routing (e.g., "If score > 8, assign to Enterprise Team").

### 2) Composio Toolset Node
* Requires an active API key for your CRM (e.g., Salesforce, HubSpot).
* Ensure the connection scope includes read/write permissions for Lead and Opportunity objects.

### 3) Tool Availability
* **CRM Search/Update:** Capability to query existing accounts and update lead fields.
* **Data Enrichment:** Ability to fetch additional firmographic data for better scoring.
* **Notification Service:** Capability to trigger Slack or Email alerts for high-value leads.

---

## Related Solutions
* [../account-intelligence-reporter-by-leadfeeder/README.md](Account Intelligence Reporter) - Identify and report on high-value account signals.
* [../crm-data-sync-agent/README.md](CRM Data Sync Agent) - Synchronize lead and account data across multiple platforms.
* [../deal-pipeline-manager/README.md](Deal Pipeline Manager) - Manage and track deal stages within your sales pipeline.
* [../whats-app-lead-qualifier-by-wati/README.md](WhatsApp Lead Qualifier) - Qualify leads directly through WhatsApp interactions.
