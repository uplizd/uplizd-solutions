# Survey Insights Generator (Uplizd) - Automated analysis and reporting for customer feedback

## Summary
The Survey Insights Generator is an intelligent Uplizd workflow that ingests raw survey data from Formsite to produce actionable business intelligence. By automating the synthesis of qualitative and quantitative feedback, this solution enables teams to identify sentiment trends, prioritize product improvements, and generate executive-ready summaries without manual data processing.

---

## Demo
![Survey Insights Generator workflow dashboard showing data ingestion from Formsite and AI-generated sentiment reports](image.png)
**Alt text (SEO-ready):** Survey Insights Generator workflow for Uplizd, automating Formsite data analysis, sentiment tracking, and business reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/982f41e1-82c4-5b82-af24-98053ac4c86d)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** formsite, survey analysis, customer feedback, sentiment analysis, data insights, ai workflow, reporting, automation
- This solution bridges the gap between raw survey collection and strategic decision-making by automating the transformation of feedback into structured insights.

---

## Who is this for?
This solution is designed for teams looking to turn high-volume customer feedback into a competitive advantage.

- **Product Manager**
    - Identifies recurring feature requests and pain points to prioritize the product roadmap.
- **Customer Success Lead**
    - Monitors sentiment trends to proactively address churn risks before they escalate.
- **Marketing Analyst**
    - Aggregates survey data to measure brand perception and campaign effectiveness.
- **Operations Manager**
    - Streamlines the reporting process by eliminating manual data entry and spreadsheet consolidation.

---

## Features
- **Automated Data Ingestion**
    - Seamlessly pulls response data from Formsite to ensure your analysis is always based on the latest feedback.
- **Sentiment Analysis Engine**
    - Uses advanced LLMs to categorize responses by tone, urgency, and topic, providing a clear view of customer satisfaction.
- **Trend Identification**
    - Automatically detects patterns and recurring keywords across hundreds of survey submissions.
- **Executive Summary Generation**
    - Produces concise, professional reports that highlight key takeaways and recommended actions for stakeholders.
- **Actionable Recommendation Logic**
    - Suggests specific operational or product improvements based on the identified sentiment and feedback themes.

---

## Use Cases
**Customer Experience Optimization**
- Analyze Net Promoter Score (NPS) comments to identify specific friction points in the user journey.
- Categorize support feedback to determine if training or documentation updates are required.

**Product Development Strategy**
- Aggregate feature requests from beta testing surveys to rank development priorities.
- Correlate user sentiment with specific product versions to validate the impact of recent releases.

**Market Research & Brand Health**
- Synthesize open-ended survey responses to track changes in brand perception over time.
- Identify competitive advantages mentioned by customers to refine marketing messaging.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Survey Insights Generator template from the marketplace.
3. Connect your Formsite account via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger to initiate the analysis of recent survey submissions.
- **Agent**: Processes raw text data, performs sentiment analysis, and drafts the summary report.
- **Composio Toolset**: Connects to Formsite to fetch the latest survey responses and metadata.
- **Chat Output**: Delivers the final synthesized report and actionable recommendations to your dashboard.

### 3) Run the Flow
Use the Playground to test your analysis:
- `Analyze the latest 50 survey responses from the Q3 Product Feedback form.`
- `Generate a sentiment report highlighting the top three customer pain points.`
- `Create a summary of feature requests and suggest a priority list for the engineering team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst and strategic consultant.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment extraction.
- Instruct the agent to maintain an objective, professional tone in all reports.
- Configure the system prompt to prioritize specific metrics like "Urgency" and "Feature Request Frequency."

### 2) Composio Toolset Node
- Provide your Formsite API key to authorize read-only access to your survey forms.
- Set the connection scope to include specific form IDs to ensure data privacy and performance.

### 3) Tool Availability
- **Formsite Fetcher**: Retrieves raw survey responses.
- **Data Parser**: Cleans and structures unstructured text for analysis.
- **Report Generator**: Formats insights into structured markdown or PDF-ready text.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich customer profiles with external data.
- [Customer Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Automate ticket routing based on sentiment.
- [AB Test Performance Analyzer](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) - Evaluate user behavior and experiment outcomes.
