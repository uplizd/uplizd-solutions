# Job Market Analyzer (Uplizd) - Real-time talent intelligence and salary benchmarking

## Summary
The Job Market Analyzer is an intelligent Uplizd workflow that leverages AgentQL to scrape, aggregate, and synthesize real-time labor market data. By automating the extraction of job postings and compensation trends, this solution provides recruiters, HR professionals, and business leaders with a single source of truth for competitive hiring, helping to optimize pipeline velocity and ensure data-driven decision-making in talent acquisition.

---

## Demo
![Job Market Analyzer workflow showing AgentQL extraction from job boards to salary benchmarking dashboard](image.png)
**Alt text (SEO-ready):** Job Market Analyzer Uplizd workflow using AgentQL for real-time talent intelligence, salary benchmarking, and automated job market data extraction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9cdf0163-6245-53e1-9fb3-881bd62ff9f3)

---

## Category
**Primary category:** Operations
**Secondary tags:** job market, talent intelligence, salary benchmarking, agentql, recruitment, data extraction, market analysis, hr tech
This solution bridges the gap between raw web data and actionable recruitment strategy by automating the collection of competitive market signals.

---

## Who is this for?
This solution is designed for professionals who need to maintain a competitive edge in the rapidly evolving talent landscape.

- **Recruitment Manager**
    - Gain instant visibility into competitor hiring trends and salary ranges for specific roles.
- **HR Business Partner**
    - Use data-backed insights to justify compensation adjustments and retention strategies.
- **Talent Acquisition Specialist**
    - Automate the manual research process to focus on high-value candidate engagement.
- **Business Strategist**
    - Monitor regional labor market shifts to inform workforce planning and expansion efforts.

---

## Features
- **Real-time Data Extraction**
    - Uses AgentQL to navigate complex job boards and extract structured data without brittle selectors.
- **Automated Salary Benchmarking**
    - Normalizes compensation data across different regions and seniority levels for accurate comparisons.
- **Competitive Intelligence Mapping**
    - Identifies which companies are hiring for similar roles and the specific skills they prioritize.
- **Pipeline Velocity Optimization**
    - Reduces the time spent on manual market research, allowing teams to react faster to talent shifts.
- **Customizable Reporting**
    - Generates summarized insights that can be exported or pushed directly to your internal CRM or Slack.

---

## Use Cases
**Competitive Hiring Analysis**
- Track the frequency and volume of job postings for specific technical roles across top-tier competitors.
- Identify emerging skill requirements in job descriptions to adjust your own recruitment criteria.

**Compensation Strategy**
- Aggregate salary ranges from public listings to ensure your offers remain within the 75th percentile of the market.
- Monitor compensation trends for remote-first roles to maintain global hiring competitiveness.

**Workforce Planning**
- Analyze regional job availability to determine the best locations for new office expansions or remote hubs.
- Detect shifts in hiring demand to pivot your recruitment focus toward high-growth sectors.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your AgentQL and relevant output integrations.
4. Ensure nodes are correctly connected and API keys are validated in the settings panel.

### 2) Setup the Nodes
- **Chat Input**: Defines the target job titles, locations, and industries to analyze.
- **Agent**: Processes the search parameters and orchestrates the extraction logic.
- **Composio Toolset**: Executes the AgentQL queries to fetch live data from target job platforms.
- **Chat Output**: Displays the synthesized market report and salary benchmarks.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Analyze the current market demand and average salary for Senior Software Engineers in the San Francisco Bay Area.`
- `Compare hiring activity for Product Managers between Amazon, Google, and Microsoft over the last 30 days.`
- `What are the top 5 most requested skills for Data Scientist roles in the current job market?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the analytical engine, interpreting raw data into human-readable insights.
- Instruct the agent to prioritize accuracy in salary ranges.
- Set the tone to professional and data-driven for executive reporting.
- Enable "Search Mode" to allow the agent to refine queries based on initial findings.

### 2) Composio Toolset Node
- Provide your **AgentQL API Key** to enable web-based data extraction.
- Ensure the connection scope includes access to public job board domains.

### 3) Tool Availability
- **Query Engine**: For parsing job board HTML structures.
- **Data Aggregator**: For normalizing currency and job metadata.
- **Report Generator**: For formatting the final output into tables or summaries.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data for better sales targeting.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Leverage ZoomInfo data for comprehensive account profiling.
