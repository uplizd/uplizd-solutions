# Customer Feedback Aggregator (Uplizd) - Centralized sentiment analysis and actionable insights

## Summary
The Customer Feedback Aggregator by Exa is an intelligent Uplizd workflow designed to unify fragmented customer sentiment data into a single source of truth. By automating the collection and analysis of feedback across multiple channels, this solution enables teams to identify trends, prioritize product improvements, and increase pipeline velocity through data-driven decision-making.

---

## Demo
![Customer Feedback Aggregator workflow dashboard showing sentiment analysis and data aggregation nodes](image.png)
**Alt text (SEO-ready):** Uplizd Customer Feedback Aggregator workflow dashboard showing sentiment analysis, data aggregation, and Exa integration for actionable customer insights.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/5b71e562-505f-515a-977e-32cac8b8f69c)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** customer feedback, sentiment analysis, exa, data aggregation, support automation, voice of customer, composio, ai workflow
- This solution streamlines the feedback lifecycle, turning raw customer input into structured data for improved operational hygiene.

---

## Who is this for?
This solution is designed for teams looking to bridge the gap between customer input and product strategy.

- **Product Manager**
    - Identifies high-priority feature requests and pain points directly from user feedback.
- **Customer Success Manager**
    - Monitors account health by tracking sentiment trends and flagging at-risk customers early.
- **Support Lead**
    - Automates the triage of incoming feedback to ensure critical issues are addressed immediately.
- **Data Analyst**
    - Aggregates disparate feedback sources into a clean, actionable dataset for executive reporting.

---

## Features
- **Unified Data Ingestion**
    - Automatically pulls feedback from multiple sources using the Composio Toolset to ensure no customer voice is missed.
- **AI-Powered Sentiment Analysis**
    - Leverages advanced LLMs to categorize feedback by tone, urgency, and topic, providing instant clarity on customer satisfaction.
- **Real-Time Trend Detection**
    - Identifies recurring themes and emerging issues as they happen, allowing for proactive rather than reactive responses.
- **Actionable Insight Mapping**
    - Connects feedback directly to internal project management or CRM tools to trigger follow-up workflows.
- **Automated Reporting**
    - Generates summary reports that highlight key metrics, helping stakeholders understand the pulse of the user base.

---

## Use Cases
**Product Roadmap Prioritization**
- Automatically tag feature requests to identify the most requested capabilities for the next sprint.
- Correlate negative sentiment spikes with specific product updates to quickly identify and fix regressions.

**Customer Retention Strategy**
- Flag feedback containing "churn" or "cancellation" keywords for immediate intervention by the Success team.
- Track sentiment improvements over time following the implementation of requested features or support fixes.

**Support Operations Efficiency**
- Categorize incoming tickets by topic to route them to the appropriate technical or billing specialists.
- Summarize long feedback threads into concise bullet points for faster review by support management.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Customer Feedback Aggregator template from the solution library.
3. Connect your required API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly mapped from the Chat Input to the Agent and finally to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw customer feedback strings or data batches.
- **Agent**: Analyzes sentiment, extracts key topics, and determines urgency.
- **Composio Toolset**: Executes data lookups and pushes structured insights to your CRM or project management tools.
- **Chat Output**: Delivers the summarized report and recommended actions to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Summarize the top 3 complaints from the last 24 hours of feedback.`
- `Identify all feedback mentioning 'billing' and tag them as 'High Priority'.`
- `Create a sentiment report for the product team based on the latest feedback batch.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, processing natural language to extract structured insights.
- **Recommended instruction pattern:**
    - Analyze the provided text for sentiment polarity (Positive, Neutral, Negative).
    - Extract specific product features or pain points mentioned in the feedback.
    - Categorize the feedback into predefined buckets (e.g., Bug, Feature Request, Praise).

### 2) Composio Toolset Node
- **API Key**: Ensure your Exa and CRM/Support platform keys are active in the Composio dashboard.
- **Connection Scope**: Grant read/write access to the feedback sources and target destination tools.

### 3) Tool Availability
- **Search & Retrieval**: Ability to query feedback databases and external documentation.
- **Data Formatting**: Capability to convert unstructured text into JSON or CSV formats.
- **Integration Hooks**: Ability to push data to Slack, Jira, Salesforce, or Zendesk.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support assistant for handling high-volume inquiries.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Conversational chatbot for real-time customer engagement.
- [whats-app-feedback-collection-agent-by-whatsapp](../whats-app-feedback-collection-agent-by-whatsapp/README.md) - Targeted feedback collection via WhatsApp channels.
