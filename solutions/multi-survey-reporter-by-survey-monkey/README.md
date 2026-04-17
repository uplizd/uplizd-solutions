# Multi-Survey Reporter (Uplizd) - Automate cross-platform survey data consolidation and reporting

## Summary
The Multi-Survey Reporter is an intelligent Uplizd workflow designed to aggregate, normalize, and synthesize feedback from multiple SurveyMonkey instances into a single source of truth. By automating the extraction and analysis of survey responses, this solution eliminates manual data entry, reduces reporting latency, and provides actionable insights for teams looking to improve customer satisfaction and product development velocity.

---

## Demo
![Multi-Survey Reporter workflow diagram showing data ingestion from SurveyMonkey into an AI analysis engine](image.png)
**Alt text (SEO-ready):** Multi-Survey Reporter Uplizd workflow diagram, survey data aggregation, SurveyMonkey integration, AI-powered feedback analysis, and automated reporting pipeline.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKwP///z8GAAkgA0YyGgUjYxQMAkYyGgUjYxQMAkYyGgUjYxQMAkYyGgUjYxQMAMA3BwA50/1+AAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/58363615-b681-5882-a19c-cfedeccc452f)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** survey, surveymonkey, data aggregation, reporting, analytics, ai workflow, feedback, composio
- This solution bridges the gap between disparate survey platforms and centralized business intelligence by automating the flow of qualitative and quantitative feedback.

---

## Who is this for?
This solution is designed for teams that need to synthesize customer sentiment at scale.

- **Product Manager**
    - Identifies recurring feature requests and pain points across multiple survey channels to prioritize the product roadmap.
- **Customer Success Lead**
    - Monitors sentiment trends to proactively address churn risks before they escalate into support tickets.
- **Data Analyst**
    - Automates the tedious process of cleaning and merging survey datasets, allowing for faster deep-dive analysis.
- **Marketing Director**
    - Tracks campaign effectiveness by correlating survey feedback with specific customer segments and touchpoints.

---

## Features
- **Automated Data Ingestion**
    - Seamlessly pulls raw response data from multiple SurveyMonkey surveys using the Composio Toolset.
- **Cross-Survey Normalization**
    - Standardizes disparate survey formats into a unified schema for consistent reporting and trend tracking.
- **AI-Powered Sentiment Synthesis**
    - Leverages LLMs to categorize open-ended text responses and extract key themes automatically.
- **Real-Time Reporting Pipeline**
    - Triggers automated report generation as soon as new survey data is detected, ensuring stakeholders have the latest insights.
- **Actionable Insight Extraction**
    - Translates raw feedback into prioritized action items, reducing the time from data collection to strategic implementation.

---

## Use Cases
**Customer Experience Optimization**
- Aggregate NPS scores across different product lines to identify specific areas for service improvement.
- Correlate customer satisfaction survey results with support ticket volume to identify process bottlenecks.

**Product Development Feedback**
- Consolidate beta testing feedback from multiple surveys to generate a master list of high-priority bug reports.
- Track feature request frequency across diverse user cohorts to validate product roadmap assumptions.

**Market Research Analysis**
- Synthesize competitive landscape surveys to identify market gaps and emerging industry trends.
- Automate the comparison of pre-launch and post-launch survey data to measure campaign impact.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Multi-Survey Reporter template from the solution library.
3. Connect your SurveyMonkey account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user request to trigger a specific survey report or analysis.
- **Agent**: Processes the natural language query and orchestrates the data retrieval logic.
- **Composio Toolset**: Executes the API calls to fetch and filter survey responses from SurveyMonkey.
- **Chat Output**: Delivers the synthesized report or summary back to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Generate a summary report of all feedback from the Q3 Product Satisfaction survey.`
- `What are the top 3 recurring complaints from the latest customer onboarding surveys?`
- `Compare the sentiment trends between the US and EU customer feedback surveys.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, responsible for interpreting survey data and formatting reports.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize quantitative trends before summarizing qualitative feedback.
- Maintain a neutral, professional tone for all generated business reports.

### 2) Composio Toolset Node
- Provide a valid SurveyMonkey API key within the Composio dashboard.
- Ensure the connection scope includes `survey_read` and `response_read` permissions.

### 3) Tool Availability
- **Survey Fetcher**: Retrieves metadata and list of available surveys.
- **Response Extractor**: Pulls individual survey responses based on ID or date range.
- **Data Formatter**: Converts JSON survey outputs into structured text for the agent.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) — Synchronizes customer data across platforms to ensure consistent records.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) — Aggregates account-level intelligence for sales and marketing teams.
- [../whats-app-feedback-collection-agent-by-wati/README.md](../whats-app-feedback-collection-agent-by-wati/README.md) — Automates the collection of customer feedback via WhatsApp channels.
