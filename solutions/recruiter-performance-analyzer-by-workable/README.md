# Recruiter Performance Analyzer (Uplizd) - Optimize hiring velocity and recruiter effectiveness

## Summary
The Recruiter Performance Analyzer is an intelligent Uplizd workflow designed to track, evaluate, and optimize the effectiveness of your recruiting team using Workable data. By automating the extraction and analysis of candidate pipeline metrics, talent acquisition leaders gain a single source of truth for recruiter performance, helping to identify bottlenecks, improve time-to-hire, and ensure high-quality candidate engagement across the entire hiring lifecycle.

---

## Demo
![Recruiter Performance Analyzer dashboard showing recruiter metrics and hiring pipeline stages](image.png)
**Alt text (SEO-ready):** Uplizd Recruiter Performance Analyzer dashboard showing recruiter metrics, Workable integration, and hiring pipeline data visualization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/594b0b48-bc0b-586b-ae84-12a169feb1f4)

---

## Category
- **Primary category:** Recruiting Operations
- **Secondary tags:** `recruiting`, `workable`, `hiring`, `performance`, `analytics`, `pipeline`, `composio`, `ai workflow`
- This solution bridges the gap between raw Workable applicant data and actionable performance insights for recruiting teams.

---

## Who is this for?
This solution is built for talent acquisition teams looking to drive data-informed hiring decisions.

- **Head of Talent**
    - Gain high-level visibility into team productivity and resource allocation.
- **Recruiting Manager**
    - Identify stalled pipeline stages and coach recruiters based on objective performance data.
- **Operations Analyst**
    - Automate the reporting process to eliminate manual spreadsheet updates.
- **External Recruiter**
    - Track individual contribution metrics and conversion rates against hiring targets.

---

## Features
- **Automated Data Sync**
    - Seamlessly pulls candidate and recruiter activity logs from Workable using the Composio Toolset.
- **Performance Benchmarking**
    - Compares recruiter KPIs against historical team averages to highlight top performers and areas for improvement.
- **Pipeline Bottleneck Detection**
    - Real-time identification of stages where candidates are dropping off or lingering too long.
- **Custom Reporting**
    - Generates summarized performance reports tailored to specific hiring roles or timeframes.
- **Actionable Insights**
    - Provides AI-driven recommendations to accelerate the hiring process and improve candidate quality.

---

## Use Cases
**Recruiter Efficiency Audits**
- Analyze average time-to-move for candidates across different recruiter portfolios.
- Identify top-performing recruiters based on interview-to-offer conversion ratios.

**Pipeline Health Monitoring**
- Detect stalled applications in the "Technical Screen" or "Final Interview" stages.
- Monitor the volume of incoming candidates per recruiter to balance workload distribution.

**Hiring Strategy Optimization**
- Correlate recruiter activity patterns with successful hires to refine sourcing strategies.
- Generate weekly performance summaries for executive stakeholders without manual data entry.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Workable account via the Composio Toolset integration.
3. Configure your preferred LLM in the Agent node to process the data.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Triggers the analysis request (e.g., "Analyze recruiter performance for Q3").
- **Agent**: Processes the natural language query and orchestrates the data retrieval.
- **Composio Toolset**: Executes API calls to Workable to fetch candidate and recruiter metrics.
- **Chat Output**: Delivers the structured performance report to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Analyze the performance of all recruiters for the last 30 days.`
- `Which recruiter has the highest conversion rate from screening to offer?`
- `Identify any bottlenecks in the engineering hiring pipeline for this month.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your recruiting data analyst.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data interpretation.
- Set the system prompt to prioritize metrics like "time-to-hire" and "conversion rate."
- Ensure the agent is instructed to cite specific Workable data points in its analysis.

### 2) Composio Toolset Node
- Authenticate with your Workable API key via the Composio dashboard.
- Ensure the connection scope includes read access to candidate, job, and recruiter activity endpoints.

### 3) Tool Availability
- `workable_get_candidates`: Retrieve applicant status and history.
- `workable_list_recruiters`: Fetch recruiter profiles and assigned tasks.
- `workable_get_hiring_pipeline`: Extract stage-by-stage conversion data.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline new hire setup and documentation.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Gather deep intelligence on target hiring accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track team productivity and operational efficiency.
