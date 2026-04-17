# Job Market Intelligence Agent (Uplizd) - Real-time hiring trends and salary benchmarking

## Summary
The Job Market Intelligence Agent leverages the Composio Toolset and SerpApi to aggregate real-time hiring data, salary benchmarks, and industry-specific job market shifts. By automating the collection and analysis of global job postings, this workflow provides recruiters, analysts, and HR leaders with a single source of truth for competitive talent intelligence, significantly reducing the time spent on manual market research.

---

## Demo
![Job Market Intelligence Agent dashboard showing real-time hiring trends and salary analysis](image.png)
**Alt text (SEO-ready):** Job Market Intelligence Agent dashboard displaying real-time hiring trends, salary benchmarks, and industry job market analysis powered by Uplizd and SerpApi.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8b7c4f8b-bd19-5d1d-8645-0c0356ebbeda)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** job market, salary benchmarking, hiring trends, recruitment, serpapi, composio, data analysis, talent acquisition
- This solution transforms raw job board data into actionable market insights for data-driven hiring strategies.

---

## Who is this for?
This solution is designed for professionals who need to stay ahead of the competitive talent landscape through data-backed decision-making.

- **Recruitment Manager**
    - Identifies competitive salary ranges to improve offer acceptance rates.
- **HR Data Analyst**
    - Automates the collection of industry-wide hiring volume metrics for quarterly reporting.
- **Talent Acquisition Lead**
    - Tracks emerging skill requirements to adjust sourcing strategies in real-time.
- **Business Strategist**
    - Monitors competitor expansion plans by analyzing their active job posting volume.

---

## Features
- **Real-time Data Aggregation**
    - Fetches live job posting data across multiple regions and platforms using the SerpApi integration.
- **Automated Salary Benchmarking**
    - Normalizes and analyzes compensation data to provide clear market-rate insights for specific roles.
- **Competitor Trend Analysis**
    - Identifies shifts in hiring focus by tracking the frequency of specific job titles and required skills.
- **Intelligent Data Synthesis**
    - Uses the Agent node to summarize complex search results into concise, executive-level market reports.
- **Seamless Composio Integration**
    - Connects external search tools directly into your workflow for automated, repeatable market intelligence gathering.

---

## Use Cases
**Competitive Salary Benchmarking**
- Compare current internal compensation packages against live market data for specific engineering roles.
- Generate regional salary reports to optimize budget allocation for new office locations.

**Talent Pipeline Optimization**
- Identify high-growth industries and roles to pivot recruitment efforts toward emerging talent pools.
- Analyze job description keywords to refine candidate sourcing and outreach messaging.

**Market Expansion Research**
- Track the hiring velocity of competitors entering new geographic markets.
- Evaluate the availability of niche skill sets in target regions before launching expansion projects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your SerpApi and LLM credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your search parameters (e.g., job title, location, industry).
- **Agent**: Processes the request and determines the necessary search queries.
- **Composio Toolset**: Executes the SerpApi calls to retrieve live job market data.
- **Chat Output**: Delivers a formatted summary of findings and actionable insights.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `What is the average salary range for a Senior Product Manager in London based on current job postings?`
- `Compare the hiring volume for AI Engineers between Q1 and Q2 in the US tech sector.`
- `List the top 5 most requested skills for Data Scientists in the current market.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a market research analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a market intelligence expert. Use the provided tools to fetch live data, synthesize trends, and present findings clearly."
- Instruction: "Always cite the source of salary data and specify the geographic region analyzed."

### 2) Composio Toolset Node
- Requires a valid SerpApi API key configured within the Composio dashboard.
- Ensure the connection scope includes `serpapi_google_jobs` to access real-time job board data.

### 3) Tool Availability
- `google_jobs_search`: Retrieves live listings based on keywords and location.
- `data_summarizer`: Aggregates and formats raw search results into structured reports.
- `trend_analyzer`: Compares historical and current data points to identify market shifts.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with firmographic and contact insights.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research on target accounts and prospect companies.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting on account engagement and intent signals.
