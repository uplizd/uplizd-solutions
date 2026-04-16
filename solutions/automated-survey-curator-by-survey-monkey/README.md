# Automated Survey Curator (Uplizd) - Streamline survey management and data organization

## Summary
The Automated Survey Curator (Uplizd) is an intelligent AI-driven workflow designed to organize, clean, and manage your SurveyMonkey data. By automating the curation of survey responses and metadata, this solution eliminates manual data entry, ensures your feedback repository remains actionable, and provides a single source of truth for your customer insights pipeline.

---

## Demo
![Automated Survey Curator workflow dashboard showing SurveyMonkey integration and data processing nodes](../image.png)
**Alt text (SEO-ready):** Automated Survey Curator workflow for SurveyMonkey data management, Uplizd AI integration, and automated survey response organization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6ea009a9-f48f-57d1-80fc-41e01a131dac)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** surveymonkey, data hygiene, survey automation, feedback management, composio, ai workflow, data sync, customer insights
- This solution bridges the gap between raw survey collection and structured data analysis, ensuring your feedback loops are always optimized.

---

## Who is this for?
This solution is designed for teams looking to transform raw survey data into structured business intelligence.

- **Marketing Manager**
    - Automates the aggregation of customer feedback to identify sentiment trends without manual spreadsheet work.
- **Customer Success Lead**
    - Ensures that critical survey responses are categorized and routed to the appropriate account owners immediately.
- **Product Researcher**
    - Maintains a clean, searchable database of survey results, allowing for faster iteration on product features.
- **Operations Specialist**
    - Reduces data decay by enforcing consistent formatting and archival standards across all active survey campaigns.

---

## Features
- **Automated Survey Sync**
    - Real-time ingestion of new survey responses from SurveyMonkey into your centralized data environment.
- **Intelligent Response Categorization**
    - Uses AI to tag and sort incoming feedback based on sentiment, topic, and urgency.
- **Data Hygiene Enforcement**
    - Automatically cleans and standardizes respondent metadata to ensure high-quality reporting.
- **Composio Toolset Integration**
    - Leverages the Composio Toolset to securely connect and interact with your SurveyMonkey API endpoints.
- **Actionable Insight Extraction**
    - Summarizes long-form survey comments into concise bullet points for rapid stakeholder review.

---

## Use Cases
**Feedback Loop Optimization**
- Automatically trigger follow-up tasks in your CRM when a survey response indicates low customer satisfaction.
- Aggregate weekly feedback summaries to present at team syncs, highlighting top-performing product areas.

**Data Repository Maintenance**
- Archive stale survey data to cold storage while keeping active campaign results readily accessible.
- Standardize naming conventions for survey titles and respondent fields across multiple departments.

**Operational Reporting**
- Generate automated performance reports for ongoing surveys, tracking completion rates and response quality.
- Sync survey respondent details with your existing customer database to enrich user profiles with recent feedback.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Automated Survey Curator.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your SurveyMonkey account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers or manual requests to curate specific survey data.
- **Agent**: Analyzes the survey data and determines the appropriate categorization or cleanup action.
- **Composio Toolset**: Executes API calls to fetch, update, or organize SurveyMonkey data.
- **Chat Output**: Delivers a confirmation report or summary of the curated survey data.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Curate all new responses from the 'Q3 Customer Satisfaction' survey.`
- `Identify and tag all negative feedback from the latest product survey.`
- `Generate a summary report of the top 3 themes from last week's survey data.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your survey data.
- Instruction: "Act as a data curator, identifying key themes and sentiment in survey responses."
- Instruction: "Ensure all data is formatted according to the organization's standard schema."
- Instruction: "Prioritize urgent feedback for immediate escalation to the support team."

### 2) Composio Toolset Node
- Requires a valid SurveyMonkey API key provided through the Composio connection manager.
- Scope should include read/write access to survey responses and collector metadata.

### 3) Tool Availability
- **Survey Fetcher**: Retrieves raw response data from active collectors.
- **Response Categorizer**: Applies AI-driven tags based on content analysis.
- **Data Formatter**: Standardizes field values and removes duplicates.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with external intelligence.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate CRM records.
- [Customer Support Ticket Manager](../whats-app-support-ticket-manager-by-spoki/README.md) — Manage support tickets across communication channels.
