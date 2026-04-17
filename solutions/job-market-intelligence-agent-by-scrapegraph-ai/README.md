# Job Market Intelligence Agent (Uplizd) - Automate real-time job market tracking and salary analysis

## Summary
The Job Market Intelligence Agent leverages ScrapeGraph AI to autonomously monitor job postings, extract salary data, and identify hiring trends across global job boards. By centralizing fragmented labor market data into a single source of truth, this workflow enables recruiters, analysts, and HR professionals to maintain a competitive edge, improve pipeline velocity, and ensure data-driven hiring decisions.

---

## Demo
![Job Market Intelligence Agent dashboard showing real-time job posting trends and salary distribution analysis](image.png)
**Alt text (SEO-ready):** Job Market Intelligence Agent dashboard by Uplizd showing real-time job posting trends, salary distribution analysis, and automated market data scraping via ScrapeGraph AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/68e67f64-ca88-5d21-80c6-f861a584c803)

---

## Category
**Primary category:** Market Intelligence
**Secondary tags:** job market, recruitment, scrapegraph, data extraction, salary analysis, hiring trends, competitive intelligence, ai workflow

This solution bridges the gap between raw web-based job board data and actionable recruitment strategy through automated scraping and analysis.

---

## Who is this for?
This agent is designed for professionals who need to stay ahead of labor market shifts and optimize their talent acquisition strategies.

*   **Recruitment Manager**
    *   Gain visibility into competitor hiring volumes and salary benchmarks to adjust offer packages in real-time.
*   **HR Data Analyst**
    *   Automate the collection of market-wide compensation data to support annual budget planning and internal equity audits.
*   **Talent Acquisition Specialist**
    *   Identify emerging skill requirements and high-demand roles to better target passive candidates.
*   **Business Strategist**
    *   Monitor regional labor market health and expansion opportunities based on real-time job posting density.

---

## Features
- **Automated Web Scraping**
  Utilizes ScrapeGraph AI to extract structured job data from complex, dynamic job board interfaces without manual intervention.
- **Salary Trend Analysis**
  Processes extracted compensation figures to provide aggregated insights into market-rate fluctuations for specific roles.
- **Competitor Benchmarking**
  Tracks hiring frequency and job description keywords across multiple target organizations to map competitor growth.
- **Real-time Data Sync**
  Delivers processed market intelligence directly into your workflow, ensuring your team acts on the latest available information.
- **Customizable Extraction Logic**
  Allows for granular control over the data points captured, from location and seniority to specific tech stack requirements.

---

## Use Cases
**Competitive Hiring Intelligence**
*   Track the volume of new job postings from direct competitors over a rolling 30-day window.
*   Analyze shifts in competitor job descriptions to identify new product focuses or technology adoption.

**Compensation Benchmarking**
*   Aggregate salary ranges for specific job titles across different geographic regions to inform local hiring budgets.
*   Identify outliers in market salary data to refine your organization’s total rewards strategy.

**Talent Pipeline Optimization**
*   Monitor the emergence of new, high-demand roles to proactively adjust your sourcing and outreach criteria.
*   Automate the identification of "always-hiring" companies to prioritize engagement with high-growth organizations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Job Market Intelligence template from the library.
3. Connect your ScrapeGraph AI credentials to the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your search parameters (e.g., job title, location, or target company).
*   **Agent**: Processes the intent and orchestrates the scraping logic via the toolset.
*   **Composio Toolset**: Executes the ScrapeGraph AI functions to fetch and parse external job board data.
*   **Chat Output**: Returns the summarized market intelligence report to the user.

### 3) Run the Flow
Use the Playground to test the agent with prompts like:
* `Analyze the current salary trends for Senior Software Engineers in the New York area.`
* `List the top 5 companies currently hiring for Product Managers and summarize their key requirements.`
* `Compare the hiring volume of [Company A] vs [Company B] over the last month.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a market research analyst.
*   **Recommended instruction pattern:**
    *   "You are an expert labor market analyst; prioritize accuracy and data-backed insights."
    *   "Always format output as a clear summary with bulleted key findings and actionable recommendations."
    *   "If data is missing for a specific query, clearly state the limitation and suggest alternative search parameters."

### 2) Composio Toolset Node
*   **API Key**: Provide your ScrapeGraph AI API key in the node configuration.
*   **Connection Scope**: Ensure the toolset has permission to access web scraping endpoints and data parsing utilities.

### 3) Tool Availability
*   **ScrapeGraph Scraper**: Core engine for navigating and extracting data from job boards.
*   **Data Formatter**: Utility to convert raw HTML/JSON into readable market intelligence reports.
*   **Trend Aggregator**: Analytical tool for calculating averages and identifying patterns in the scraped data.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and identify key decision-makers.
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate comprehensive reports on account activity and intent signals.
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into target accounts and company profiles.
