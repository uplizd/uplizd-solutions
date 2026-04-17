# Learning Analytics Dashboard Generator (Uplizd) - Automate training insights and performance metrics

## Summary
The Learning Analytics Dashboard Generator by Coassemble is an intelligent Uplizd workflow that transforms raw training data into actionable performance metrics and visual insights. By automating the aggregation and analysis of learner progress, this solution enables L&D teams to identify knowledge gaps, track course completion velocity, and optimize curriculum effectiveness without manual reporting overhead.

---

## Demo
![Learning Analytics Dashboard Generator workflow showing data ingestion, analysis, and visualization nodes](image.png)
**Alt text (SEO-ready):** Learning Analytics Dashboard Generator workflow in Uplizd, automating training data analysis, course performance tracking, and L&D reporting with Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKAAABAAAB)](https://uplizd.ai/solutions/49543ccf-8714-5f2f-8e1c-015015748230)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** learning analytics, coassemble, l&d, training data, dashboard, reporting, composio, ai workflow
- This solution bridges the gap between raw LMS data and executive-level reporting by automating the transformation of training metrics into visual dashboards.

---

## Who is this for?
This solution is designed for Learning & Development professionals and data-driven managers who need to quantify the impact of their training programs.

- **L&D Manager**
    - Automates the generation of monthly training impact reports for stakeholders.
- **Training Coordinator**
    - Identifies stalled learners and course bottlenecks in real-time.
- **HR Operations Specialist**
    - Ensures training compliance data is accurate and ready for audit.
- **Curriculum Designer**
    - Uses performance metrics to iterate on course content and improve engagement.

---

## Features
- **Automated Data Ingestion**
    - Seamlessly pulls learner progress and assessment scores from Coassemble into your analysis pipeline.
- **Real-time Performance Metrics**
    - Calculates completion rates, average quiz scores, and time-to-complete metrics automatically.
- **Intelligent Insight Generation**
    - Uses the Agent node to summarize trends and highlight underperforming training modules.
- **Composio Toolset Integration**
    - Leverages pre-built connectors to push analyzed data directly into your preferred visualization or BI tools.
- **Customizable Reporting**
    - Tailors output summaries based on specific organizational KPIs and training objectives.

---

## Use Cases
**Training Effectiveness Analysis**
- Correlate assessment scores with module engagement time to identify difficult content.
- Generate weekly summaries of knowledge retention rates across different departments.

**Operational Compliance Tracking**
- Monitor mandatory training completion windows to ensure 100% organizational compliance.
- Flag overdue certifications and trigger automated reminders to relevant team leads.

**Curriculum Optimization**
- Analyze learner feedback patterns to prioritize updates for high-drop-off course sections.
- Benchmark course performance against historical data to measure the ROI of new training initiatives.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Connect your Coassemble API credentials within the integration settings.
3. Configure your target output destination (e.g., Google Sheets, Slack, or BI tool).
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Accepts user queries regarding specific course performance or date ranges.
- **Agent**: Processes training data using LLM logic to identify trends and summarize performance.
- **Composio Toolset**: Executes API calls to fetch data from Coassemble and push reports to external platforms.
- **Chat Output**: Delivers the final analytical summary or dashboard link to the user.

### 3) Run the Flow
- `Generate a summary of all training completion rates for the Q3 marketing cohort.`
- `Which training modules have the highest drop-off rate this month?`
- `Create a performance report for the new hire onboarding curriculum and send it to the L&D Slack channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting training data and formatting it for stakeholders.
- Maintain a professional, data-focused tone in all generated reports.
- Prioritize identifying outliers, such as modules with unusually low completion rates.
- Structure output with clear headings, bulleted insights, and actionable recommendations.

### 2) Composio Toolset Node
- Requires a valid Coassemble API key to authenticate and fetch learner records.
- Scope should be set to read-only access for training data to maintain security best practices.

### 3) Tool Availability
- **Data Fetcher**: Retrieves course, user, and assessment data from Coassemble.
- **Report Formatter**: Converts raw JSON data into human-readable summaries or CSV formats.
- **Notification Dispatcher**: Sends finalized reports to Slack, Email, or internal project management tools.

---

## Related Solutions
- [Account Intelligence Reporter (../account-intelligence-reporter-by-leadfeeder/README.md)](../account-intelligence-reporter-by-leadfeeder/README.md) - Automate account data gathering and reporting.
- [Workflow Health Monitor (../workflow-health-monitor-by-dailybot/README.md)](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize organizational workflow performance.
- [Account Health Usage Monitor (../account-health-usage-monitor-by-jotform/README.md)](../account-health-usage-monitor-by-jotform/README.md) - Monitor usage metrics to maintain account health.
