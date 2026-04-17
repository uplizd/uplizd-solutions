# Hot Lead Qualifier (Uplizd) - Automate lead scoring and prioritization using real-time visitor intelligence

## Summary
The Hot Lead Qualifier by Uplizd streamlines your sales pipeline by automatically analyzing website visitor data from Leadfeeder to score and prioritize prospects in real-time. By integrating visitor intent signals with your CRM, this AI workflow ensures your sales team focuses their energy on high-value accounts, significantly reducing manual research time and increasing conversion velocity.

---

## Demo
![Hot Lead Qualifier workflow showing Leadfeeder data ingestion, AI scoring, and CRM update](image.png)
**Alt text (SEO-ready):** Uplizd Hot Lead Qualifier workflow dashboard showing Leadfeeder integration, AI-driven lead scoring, and automated CRM pipeline updates.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/06b950bc-f9e7-5305-8577-a65175d31a3e)

---

## Category
* **Primary category:** Sales automation
* **Secondary tags:** leadfeeder, crm, lead scoring, pipeline, sales intelligence, b2b sales, composio, ai workflow
* This solution bridges the gap between raw web traffic data and actionable sales opportunities by automating the qualification process.

---

## Who is this for?
This workflow is designed for revenue teams looking to eliminate manual lead triage and accelerate their sales cycle.

* **Sales Development Representative (SDR)**
    * Spend less time on manual research and focus exclusively on high-intent leads ready for outreach.
* **RevOps Manager**
    * Maintain clean, prioritized pipeline data by automating the flow of intent signals from website traffic to the CRM.
* **Account Executive (AE)**
    * Receive pre-qualified opportunities with attached company intelligence, allowing for more personalized and effective discovery calls.
* **Marketing Operations Specialist**
    * Close the feedback loop between web traffic behavior and sales outcomes to optimize lead generation campaigns.

---

## Features
- **Real-time Intent Scoring**
  Automatically assigns a qualification score to visitors based on Leadfeeder data and custom business logic.
- **Automated CRM Enrichment**
  Instantly pushes qualified lead data and intent signals into your CRM, ensuring your sales team has the latest context.
- **Intelligent Filtering**
  Filters out low-intent traffic and noise, ensuring only high-value prospects reach your sales queue.
- **Composio-Powered Integrations**
  Leverages the Composio Toolset to securely connect with CRM platforms and lead intelligence APIs without custom middleware.
- **Customizable Qualification Logic**
  Easily adjust scoring thresholds and criteria within the Agent node to match your specific Ideal Customer Profile (ICP).

---

## Use Cases
**Lead Prioritization**
* Automatically flag visitors from target accounts for immediate follow-up by the assigned account owner.
* Assign "Hot," "Warm," or "Cold" status to leads based on the number of page views and specific high-value content visited.

**Sales Intelligence**
* Append company size, industry, and revenue data from Leadfeeder directly to the lead record in your CRM.
* Trigger personalized email sequences based on the specific services or products a lead was researching on your site.

**Pipeline Hygiene**
* Automatically archive or tag leads that do not meet your minimum qualification threshold to keep the CRM clean.
* Sync visitor activity logs to the CRM so the sales team can see the full history of a prospect's engagement before reaching out.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Hot Lead Qualifier template from the solution library.
3. Authenticate your Leadfeeder and CRM connections within the Composio Toolset.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Accepts trigger signals or manual requests to qualify a specific lead or batch of visitors.
* **Agent**: Processes visitor data, applies scoring logic, and determines the qualification status.
* **Composio Toolset**: Executes API calls to fetch Leadfeeder data and update CRM records.
* **Chat Output**: Returns the qualification summary and confirmation of the CRM update.

### 3) Run the Flow
Use the Playground to test your qualification logic with these prompts:
* `Qualify the latest batch of visitors from Leadfeeder and update the CRM.`
* `Check if any visitors from Fortune 500 companies have visited our pricing page today.`
* `Score the most recent 10 website visitors and assign them to the sales queue if they meet our ICP.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets visitor behavior and maps it to your business rules.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Analyze the provided Leadfeeder visitor data against our ICP criteria."
* Instruction: "Assign a score from 1-10 and determine if the lead should be pushed to the CRM."

### 2) Composio Toolset Node
* Provide your API key to enable secure communication between Uplizd and your integrated platforms.
* Ensure the connection scope includes read access for Leadfeeder and write access for your CRM (e.g., Salesforce or HubSpot).

### 3) Tool Availability
* **Leadfeeder API**: For fetching visitor company data and page view history.
* **CRM API**: For creating or updating lead/opportunity records.
* **Data Transformation Utility**: For normalizing company data and formatting strings for CRM fields.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate comprehensive reports on account research and intent signals.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and optimize your sales pipeline stages and follow-up cadences.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple platforms with conflict resolution.
