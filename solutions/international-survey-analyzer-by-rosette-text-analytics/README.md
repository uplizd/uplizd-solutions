# International Survey Analyzer (Uplizd) - Multilingual feedback processing and data standardization

## Summary
The International Survey Analyzer is an automated Uplizd workflow that leverages Rosette Text Analytics to detect languages, extract sentiment, and standardize participant feedback across global datasets. By streamlining the ingestion of multilingual survey responses, this solution provides organizations with a single source of truth for customer insights, eliminating manual translation overhead and ensuring data hygiene across international markets.

---

## Demo
![International Survey Analyzer workflow showing language detection and data standardization nodes](image.png)
**Alt text (SEO-ready):** Uplizd International Survey Analyzer workflow using Rosette Text Analytics for multilingual feedback processing, sentiment analysis, and CRM data synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/babd4815-92cd-5fff-af87-df1b3d284bdd)

---

## Category
**Primary category:** Data integration
**Secondary tags:** survey, multilingual, rosette text analytics, data hygiene, nlp, customer insights, feedback, composio

This solution bridges the gap between raw international survey data and actionable business intelligence by automating language-aware data processing.

---

## Who is this for?
This solution is designed for teams managing global customer feedback loops who need to maintain data consistency across languages.

*   **Market Research Analyst**
    *   Automates the categorization of open-ended survey responses from diverse geographic regions.
*   **Customer Experience (CX) Manager**
    *   Ensures global sentiment trends are captured accurately without the need for manual translation services.
*   **Data Operations Lead**
    *   Maintains high data hygiene by standardizing participant inputs into a unified CRM format.
*   **Product Manager**
    *   Identifies feature requests and pain points from international users to prioritize the global product roadmap.

---

## Features
- **Automated Language Detection**
    - Uses Rosette Text Analytics to instantly identify the source language of incoming survey responses.
- **Sentiment Extraction**
    - Parses qualitative feedback to assign sentiment scores, enabling quantitative analysis of global customer satisfaction.
- **Data Standardization**
    - Normalizes participant information and survey metadata into a consistent schema for downstream reporting.
- **Composio-Powered Integration**
    - Seamlessly connects survey platforms with your CRM or data warehouse to trigger automated follow-up workflows.
- **Real-time Processing**
    - Processes survey submissions as they arrive, ensuring that global insights are always up-to-date.

---

## Use Cases
**Global Feedback Aggregation**
*   Consolidating survey results from different regional offices into a single, language-agnostic dashboard.
*   Automatically flagging negative sentiment in non-English responses for immediate escalation to support teams.

**Customer Data Hygiene**
*   Cleaning and standardizing participant contact fields across international survey datasets.
*   Removing duplicate entries and formatting inconsistencies before syncing data to your primary CRM.

**Market Intelligence**
*   Analyzing regional trends by comparing sentiment scores across different language demographics.
*   Extracting key themes and topics from multilingual feedback to inform localized marketing strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to navigate to the solution template.
2. Select "Import Flow" to add the International Survey Analyzer to your workspace.
3. Connect your preferred survey platform and Rosette Text Analytics API credentials.
4. Ensure nodes are correctly mapped and all API connections are authorized in the settings panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw survey response text and participant metadata.
*   **Agent**: Orchestrates the analysis, invoking Rosette tools to interpret the input.
*   **Composio Toolset**: Executes the language detection, sentiment analysis, and CRM update operations.
*   **Chat Output**: Delivers the standardized data and analysis summary to your dashboard or notification channel.

### 3) Run the Flow
Use the Playground to test the workflow with sample inputs:
*   `Analyze this survey response: "El servicio fue excelente, pero la entrega tardó demasiado."`
*   `Process feedback: "Die Benutzeroberfläche ist sehr intuitiv, aber ich vermisse eine Dark-Mode-Option."`
*   `Standardize and sync this response: "The product quality is good, but the pricing is a bit high for our market."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for routing and data interpretation.
*   Instruct the agent to prioritize accuracy in language identification.
*   Configure the agent to output standardized JSON objects for CRM compatibility.
*   Set the agent to trigger specific alerts when sentiment scores fall below a defined threshold.

### 2) Composio Toolset Node
*   Provide your Rosette Text Analytics API key to enable linguistic processing.
*   Define the connection scope to allow the agent to read survey data and write to your CRM.

### 3) Tool Availability
*   **Language Identification**: Detects the primary language of the input text.
*   **Sentiment Analysis**: Scores the emotional tone of the feedback.
*   **Entity Extraction**: Identifies key products or features mentioned in the survey.
*   **CRM Update**: Syncs the cleaned data to your integrated CRM platform.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriches account data to provide deeper context for survey participants.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Ensures that standardized survey data remains clean and deduplicated in your CRM.
*   [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - Provides automated support responses based on insights derived from survey feedback.
