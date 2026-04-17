# Investor Deal Sourcer (Uplizd) - Automated investment opportunity identification and qualification

## Summary
The Investor Deal Sourcer is an intelligent Uplizd workflow designed to streamline the venture capital and private equity pipeline by automating the discovery and initial vetting of potential investment targets. By leveraging real-time data from Crustdata, the agent identifies high-potential companies based on custom investment theses, reducing manual research time and ensuring that investment teams focus only on the most promising opportunities.

---

## Demo
![Investor Deal Sourcer workflow dashboard showing automated company qualification and data enrichment via Crustdata integration](image.png)
**Alt text (SEO-ready):** Investor Deal Sourcer workflow dashboard showing automated company qualification and data enrichment via Crustdata integration on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/investor-deal-sourcer-by-crustdata)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, crustdata, investment, deal sourcing, lead qualification, pipeline, data enrichment, composio, ai workflow

This solution bridges the gap between raw market data and actionable investment intelligence, enabling firms to automate their deal flow management.

---

## Who is this for?
This workflow is designed for investment professionals who need to scale their outreach and vetting processes without sacrificing data quality.

*   **Venture Capital Associate**
    *   Automates the manual burden of screening early-stage companies against specific investment criteria.
*   **Private Equity Analyst**
    *   Accelerates the identification of potential acquisition targets by filtering through market-wide data.
*   **Investment Manager**
    *   Ensures a consistent, data-backed approach to building a robust pipeline of high-potential opportunities.
*   **Growth Equity Researcher**
    *   Leverages real-time signals to track company momentum and growth milestones automatically.

---

## Features
- **Automated Market Scanning**
    Connects to Crustdata to ingest real-time company performance metrics and growth signals.
- **Thesis-Driven Filtering**
    Applies custom logic to qualify companies based on industry, funding stage, and headcount growth.
- **Intelligent Data Enrichment**
    Automatically populates CRM records with deep company insights, reducing the need for manual data entry.
- **Pipeline Velocity Optimization**
    Reduces the time from discovery to initial outreach by automating the qualification workflow.
- **Composio-Powered Integration**
    Seamlessly bridges the gap between data providers and your existing CRM or communication tools.

---

## Use Cases
**Pipeline Prospecting**
*   Automatically identify startups that have recently reached a Series A funding milestone.
*   Flag companies showing significant headcount growth in specific technical departments.

**Investment Vetting**
*   Cross-reference company growth data against your firm's specific investment thesis.
*   Generate summary reports for potential targets to share with the investment committee.

**CRM Maintenance**
*   Update existing prospect profiles with the latest funding and market valuation data.
*   Archive companies that no longer meet your firm's evolving investment criteria.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Crustdata API credentials to the Composio Toolset node.
3. Configure your target CRM (e.g., Salesforce or HubSpot) to receive the qualified leads.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your specific investment thesis or search parameters.
*   **Agent**: Processes the search query and determines which data points to fetch.
*   **Composio Toolset**: Executes the Crustdata API calls to retrieve and parse company data.
*   **Chat Output**: Delivers a curated list of qualified investment opportunities to your dashboard.

### 3) Run the Flow
Use the Playground to test your sourcing logic:
*   `Find 10 SaaS companies in the fintech sector with over 20% headcount growth in the last 6 months.`
*   `Identify Series B startups in the healthcare space that have recently expanded their engineering team.`
*   `List potential investment targets that match our current thesis for B2B infrastructure software.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your digital investment analyst.
*   Instruction: "You are an expert deal sourcer. Analyze the provided company data against the user's investment thesis."
*   Instruction: "Prioritize companies that show strong growth signals and match the specified industry focus."
*   Instruction: "Format the output as a clean, actionable list of companies with a brief justification for each."

### 2) Composio Toolset Node
*   **API Key**: Provide your Crustdata API key in the configuration settings.
*   **Connection Scope**: Ensure the toolset has read access to company data and search endpoints.

### 3) Tool Availability
*   `crustdata_search`: For querying company databases based on specific filters.
*   `crustdata_enrichment`: For pulling detailed performance and growth metrics.
*   `crm_update`: For pushing qualified leads directly into your pipeline management system.

---

## Related Solutions
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automates the reporting of account-level insights and engagement data.
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) — Simplifies deep-dive research into target accounts.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Tracks and manages the lifecycle of sales and investment deals.
*   [Account Expansion Identifier](../account-expansion-identifier-by-crustdata/README.md) — Uses Crustdata to find upsell and expansion opportunities within existing accounts.
