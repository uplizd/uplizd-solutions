# Market Research Assistant (Uplizd) - Automate Company Intelligence & Reporting

## Summary
The Market Research Assistant is a specialized Uplizd AI workflow designed to automate the collection and analysis of comprehensive company data. By leveraging high-fidelity firmographic APIs (BigPicture.io), it transforms a simple list of company names into detailed market intelligence reports—saving research analysts 8-10 hours per report while maintaining 95% data completeness.

---

## Demo

![Market Research Assistant flow performing domain search and company profiling](image.png)

**Alt text (SEO-ready):** Uplizd Market Research Assistant workflow showing an AI agent utilizing BigPicture.io tools to discover official domains and extract detailed company metrics for automated reporting.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5612058a-c8fb-483d-951f-5d23770e99f2)

---

## Category

**Primary category:** Market Intelligence
**Secondary tags:** crm, bigpicture, research, firmographics, data enrichment, sales intelligence, ai workflow, composio

This solution bridges the gap between raw company lists and structured, actionable market data for strategic decision-making.

---

## Who is this for?

Built for strategic teams that need accurate, deep-dive firmographic data without the manual grind:

- **Market Research Analysts**
    - Generate standardized company profiles and industry overviews in minutes.
- **Sales Operations (SalesOps)**
    - Automatically enrich lead lists with funding data, employee counts, and market positioning.
- **Venture Capital & Private Equity**
    - Quickly vet target companies and monitor portfolio growth metrics.
- **Competitive Intelligence Teams**
    - Track competitor funding stages, leadership changes, and market shifts.

---

## Features

- **Automated Domain Discovery**
  Intelligently converts raw company names into verified official domains, ensuring zero confusion between similarly named entities.

- **Comprehensive Firmographic Capture**
  Extracts deep data points including funding history, employee growth metrics, business models, and industry classifications.

- **Standardized Data Categorization**
  Groups companies by industry sub-sectors and funding stages for easy comparative analysis and benchmarking.

- **Competitive Positioning Matrix**
  Analyzes unique value propositions and market sectors to identify leaders, challengers, and emerging threats.

- **Strategic Report Generation**
  Produces professional, structured reports featuring executive summaries, trend analysis, and actionable next steps.

---

## Use Cases

**Target List Enrichment**
- Turn a list of 50 "Target Accounts" into a full database with verified URLs, funding status, and size.
- Append missing firmographic data to existing CRM records for better segmentation.

**Competitor Landscape Analysis**
- Map out the key players in a specific sub-sector (e.g., "Fintech in SE Asia") with standardized data points.
- Identify emerging competitors by tracking funding rounds and employee growth trends.

**Due Diligence Pre-screening**
- Rapidly collect initial metrics on prospective companies to filter for high-value targets.
- Summarize leadership and business model changes to assess company health before deep-dive meetings.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts the list of company names or research queries.
- **Agent**: Orchestrates the research logic and synthesizes the final report.
- **Composio Toolset**: Connects to BigPicture.io to fetch real-time company data.
- **Chat Output**: Delivers the formatted market intelligence report.

### 3) Run the Flow
1. Click **Playground**.
2. Trigger the research by providing target names:
   - `Research these companies: [Company A], [Company B], [Company C]`
   - `Give me a market report on the top 5 emerging AI startups in San Francisco.`
   - `Find detailed metrics for [Company Name] and compare it to its main competitors.`

---

## Configuration

### 1) Language Model (Agent Node)
Optimized for data parsing and structured reporting.
- **Model**: GPT-4o or Claude-3.5-Sonnet (for precise formatting).
- **System Prompt**: Pre-configured to handle Domain Discovery → Data Collection → Analysis → Reporting.
- **Temperature**: Set to 0.2 for consistent, factual data synthesis.

### 2) Composio Toolset Node
Requires a **Composio API Key** and a linked BigPicture.io account. Ensure your connection scope includes read access to firmographic data endpoints.

### 3) Tool Availability
- **BIGPICTURE_IO_NAME_TO_DOMAIN_SEARCH**: Reliable mapping of names to URLs.
- **BIGPICTURE_IO_COMPANY_FIND**: The primary engine for detailed firmographics and growth data.

---

## Related Solutions

* **[Account Research Agent](../account-research-agent-by-onepage/README.md)**  
  Deep-dive into specific account details and relationship mapping.
* **[Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md)**  
  Generate automated reports on account activity and intent signals.
* **[CRM Data Sync Agent](../crm-data-sync-agent/README.md)**  
  Sync your enriched target company data automatically into your CRM or database.
* **[Content Research Assistant](../content-research-assistant/README.md)**  
  Analyze competitor content strategies and discover trending topics in your sector.
