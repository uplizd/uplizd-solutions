# Website Lead Qualifier (Uplizd) - Automated website research and lead qualification

## Summary
The Website Lead Qualifier is an intelligent Uplizd workflow that automates the discovery and assessment of potential leads by scraping and analyzing company website data. By leveraging the Composio Toolset to interface with web browsing capabilities, the agent extracts key business insights, identifies value propositions, and qualifies prospects against your ideal customer profile (ICP), significantly reducing manual research time and increasing pipeline velocity.

---

## Demo
![Website Lead Qualifier workflow interface showing browser-based data extraction and AI analysis](image.png)
**Alt text (SEO-ready):** Website Lead Qualifier (Uplizd) workflow showing browser-based data extraction, AI-driven lead analysis, and CRM integration for sales automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/77702830-2fcd-5488-a288-9d10b7dac311)

---

## Category
*   **Primary category:** Sales automation
*   **Secondary tags:** `lead qualification`, `web scraping`, `sales intelligence`, `composio`, `ai workflow`, `crm`, `prospecting`
*   This solution bridges the gap between raw web data and actionable sales intelligence, streamlining the qualification process for high-growth revenue teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate the top-of-funnel research process.

*   **Sales Development Representatives (SDRs)**
    *   Instantly gather context on new leads to personalize outreach and improve conversion rates.
*   **Account Executives (AEs)**
    *   Focus on high-intent prospects by automating the initial discovery and qualification research.
*   **Revenue Operations (RevOps) Managers**
    *   Standardize the lead qualification process across the team to ensure consistent data hygiene.
*   **Growth Marketers**
    *   Identify and segment prospects based on specific website technologies or business models discovered during research.

---

## Features
- **Automated Web Discovery**
  Uses the Composio Toolset to navigate target URLs and extract core business information in real-time.
- **Intelligent ICP Matching**
  The Agent analyzes scraped content against your predefined criteria to score leads based on fit.
- **Structured Data Extraction**
  Converts unstructured website text into clean, organized summaries ready for CRM entry.
- **Contextual Sales Insights**
  Identifies key pain points and value propositions mentioned on the prospect's site to tailor your messaging.
- **Seamless Pipeline Integration**
  Connects directly with your existing sales stack to push qualified lead data without manual entry.

---

## Use Cases
**Lead Qualification & Scoring**
*   Automatically score inbound leads based on their company's industry and service offerings.
*   Filter out prospects that do not meet minimum revenue or technology stack requirements.

**Personalized Sales Outreach**
*   Generate custom ice-breakers based on recent company news or product launches found on their site.
*   Identify specific technical pain points to address in your initial discovery call.

**Competitive Intelligence**
*   Track the positioning of competitors by monitoring their website updates and messaging.
*   Compare prospect service offerings against your own to highlight unique value propositions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Review the workflow canvas to ensure all nodes are connected correctly.
3. Configure your API credentials for the browser-based tools within the Composio Toolset.
4. Ensure nodes are properly mapped, authenticated, and ready for execution.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target company URL or list of domains for qualification.
*   **Agent**: Processes the scraped content, performs ICP analysis, and generates a qualification report.
*   **Composio Toolset**: Executes web browsing and data extraction tasks to feed the Agent.
*   **Chat Output**: Delivers the final lead summary, qualification score, and recommended next steps.

### 3) Run the Flow
Open the Playground and test the workflow with the following prompts:
* `Qualify this lead: https://www.example-company.com and summarize their core service offering.`
* `Analyze https://tech-startup.io and tell me if they are a good fit for our enterprise CRM solution.`
* `Research https://agency-partner.com and list 3 potential pain points they might be facing based on their website.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a research analyst and qualification engine.
*   Focus on extracting specific business metrics and value propositions.
*   Maintain a neutral, objective tone when scoring leads against the ICP.
*   Prioritize data accuracy by cross-referencing extracted text with the provided URL.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Composio API key is active and authorized for web browsing tools.
*   **Connection Scope**: Grant the toolset read-only access to browse and extract public website content.

### 3) Tool Availability
*   **Web Browser**: For navigating and reading page content.
*   **Content Extractor**: For parsing HTML into clean, readable text.
*   **Search Engine**: For finding additional context on the company if the primary URL is insufficient.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich company profiles with deep firmographic data.
*   [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Track and score sales opportunities through the pipeline.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and account data across multiple platforms.
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) — Perform deep-dive research on target accounts to support high-touch sales.
