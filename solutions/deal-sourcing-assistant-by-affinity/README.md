# Deal Sourcing Assistant (Uplizd) - Automated deal flow analysis and investment opportunity scoring

## Summary
The Deal Sourcing Assistant is an intelligent Uplizd workflow designed to streamline the identification and evaluation of investment opportunities. By integrating directly with Affinity, the agent automates the ingestion of deal data, scores potential opportunities based on predefined investment criteria, and maintains a single source of truth for your pipeline, significantly increasing deal flow velocity and reducing manual research time.

---

## Demo
![Deal Sourcing Assistant workflow diagram showing data ingestion from Affinity, automated scoring, and output to the CRM](image.png)
**Alt text (SEO-ready):** Uplizd Deal Sourcing Assistant workflow for automated investment opportunity scoring and CRM data integration with Affinity.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a906dc39-f4f5-5e1b-a36e-961b7c07e6cb)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** affinity, crm, deal sourcing, investment, pipeline, lead scoring, composio, ai workflow
This solution bridges the gap between raw market data and actionable investment intelligence by automating the qualification process.

---

## Who is this for?
This solution is designed for investment professionals and sales teams looking to optimize their outreach and evaluation processes.

* **Investment Associates**
    * Automate the initial screening of inbound deal flow to prioritize high-potential opportunities.
* **Venture Capital Analysts**
    * Maintain real-time visibility into market trends and company health metrics without manual data entry.
* **Sales Operations Managers**
    * Ensure consistent scoring criteria are applied across all incoming leads to improve pipeline hygiene.
* **Growth Managers**
    * Quickly identify and engage with prospects that match specific investment or partnership mandates.

---

## Features
- **Automated Data Ingestion**
  Directly pulls company and contact data from Affinity to ensure the agent is working with the most current information.
- **Intelligent Opportunity Scoring**
  Uses AI to evaluate companies against your specific investment thesis, assigning scores based on growth signals and sector alignment.
- **Real-time CRM Sync**
  Automatically updates deal stages and notes in your CRM via the Composio Toolset, eliminating manual data entry tasks.
- **Customizable Evaluation Logic**
  Configure the agent's instructions to prioritize specific metrics like funding stage, employee growth, or industry vertical.
- **Proactive Alerting**
  Generates summaries and alerts for high-scoring opportunities, ensuring your team never misses a critical lead.

---

## Use Cases
**Pipeline Management**
* Automatically move qualified leads to the 'Due Diligence' stage in Affinity based on AI scoring.
* Flag stalled deals that have not had activity in over 30 days for immediate follow-up.

**Market Intelligence**
* Aggregate data on emerging competitors within a specific sector to inform investment strategy.
* Monitor portfolio company news and updates to provide proactive support or follow-on investment analysis.

**Lead Qualification**
* Filter incoming deal submissions by revenue thresholds and geographic location before they reach a human analyst.
* Enrich lead profiles with external market signals to provide a 360-degree view of the opportunity.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deal Sourcing Assistant template file.
3. Connect your Affinity API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger or manual request to scan for new deals.
* **Agent**: Processes the data using your custom investment thesis instructions.
* **Composio Toolset**: Executes API calls to Affinity to fetch and update deal records.
* **Chat Output**: Returns the summary of scored deals and actions taken to the user.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Scan the latest deals in Affinity and score them based on our SaaS growth criteria.`
* `Identify all companies in the 'Seed' stage and update their profile with recent funding news.`
* `Generate a summary report of all high-scoring opportunities added to the pipeline this week.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your primary investment analyst.
* Define your investment thesis clearly in the system prompt.
* Instruct the agent to prioritize specific data fields (e.g., ARR, headcount growth).
* Set the tone for output summaries to match your internal reporting standards.

### 2) Composio Toolset Node
* Provide your Affinity API key to enable secure read/write access.
* Define the connection scope to include only the necessary CRM modules (e.g., Organizations, People, Opportunities).

### 3) Tool Availability
* **Affinity Search**: Find organizations and contacts by name or domain.
* **Affinity Update**: Modify deal stages, custom fields, and contact notes.
* **Affinity Fetch**: Retrieve detailed company profiles and interaction history.

---

## Related Solutions
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive intelligence gathering for target accounts.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - End-to-end management of sales stages and follow-up workflows.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automated enrichment of CRM contact data.
