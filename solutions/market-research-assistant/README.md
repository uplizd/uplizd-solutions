
# Market Research Assistant (Uplizd) - Automate Company Intelligence & Reporting

## Summary
The Market Research Assistant is a specialized Uplizd AI workflow designed to automate the collection and analysis of comprehensive company data. By leveraging high-fidelity firmographic APIs (BigPicture.io), it transforms a simple list of company names into detailed market intelligence reports—saving research analysts 8-10 hours per report while maintaining 95% data completeness.

---

## Demo

![Market Research Assistant flow performing domain search and company profiling](image.png)

**Alt text:** Uplizd Market Research Assistant workflow showing an AI agent utilizing BigPicture.io tools to discover official domains and extract detailed company metrics for automated reporting.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5612058a-c8fb-483d-951f-5d23770e99f2)

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

- **Target List Enrichment**
  - Turn a list of 50 "Target Accounts" into a full database with verified URLs, funding status, and size.

- **Competitor Landscape Analysis**
  - Map out the key players in a specific sub-sector (e.g., "Fintech in SE Asia") with standardized data points.

- **Due Diligence Pre-screening**
  - Rapidly collect initial metrics on prospective companies to filter for high-value targets.

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all **5 nodes** are connected:
   - **Chat Input**
   - **Agent**
   - **BigpictureIo - NAME_TO_DOMAIN_SEARCH**
   - **BigpictureIo - COMPANY_FIND**
   - **Chat Output**

### 2) Setup the Nodes
Verify the core logic:

- **BigPicture.io Nodes** → perform the heavy lifting of data lookup and firmographic extraction.
- **Agent** → orchestrated with the "Market Research Assistant" prompt to handle data synthesis.
- **Chat Output** → outputs the final Markdown report.

### 3) Run the Flow
1. Click **Playground**.
2. Trigger the research by providing target names:
   - *"Research these companies: [Company A], [Company B], [Company C]"*
   - *"Give me a market report on the top 5 emerging AI startups in San Francisco."*
   - *"Find detailed metrics for [Company Name] and compare it to its main competitors."*

---

## Configuration

### 1) Language Model (Agent Node)
Optimized for data parsing and structured reporting.

Recommended settings:
- **Model**: GPT-4o or Claude-3.5-Sonnet (for precise formatting).
- **System Prompt**: Pre-configured to handle Domain Discovery → Data Collection → Analysis → Reporting.

### 2) BigPicture.io Connection
Requires a **Composio API Key** and a BigPicture.io account. Ensure your credits are sufficient for the number of companies you intend to research.

### 3) Tool Availability (BigPicture Actions)
The agent utilizes these specific actions via Composio:
- **BIGPICTURE_IO_NAME_TO_DOMAIN_SEARCH**: Reliable mapping of names to URLs.
- **BIGPICTURE_IO_COMPANY_FIND**: The primary engine for detailed firmographics and growth data.

---

## Related Solutions

* **[Content Research Assistant](../content-research-assistant/README.md)**  
  Analyze competitor content strategies and discover trending topics in your sector.

* **[Research Insight Synthesizer](../research-insight-synthesizer/README.md)**  
  Complement your quantitative data with qualitative synthesis of user interviews and research.

* **[Contact Sync Manager](../contact-sync-manager/README.md)**  
  Sync your enriched target company data automatically into your CRM or database.

* **[Professional Email Clarity Assistant](../professional-email-clarity-assistant/README.md)**  
  Reach out to your newly discovered research targets with professional, clear business communications.
