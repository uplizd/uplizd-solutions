# Conversation Analytics Reporter (Uplizd) - Automated insights from chatbot interactions

## Summary
The Conversation Analytics Reporter (Uplizd) is an automated workflow that ingests, processes, and summarizes chatbot conversation logs to extract actionable business intelligence. By leveraging AI-driven analysis, this solution transforms raw chat transcripts into structured reports, helping teams identify customer pain points, track sentiment trends, and improve overall support efficiency without manual data entry.

---

## Demo
![Conversation Analytics Reporter workflow showing Chat Input, Botpress analysis agent, and report generation](image.png)

**Alt text (SEO-ready):** Conversation Analytics Reporter (Uplizd) workflow for automated chatbot data analysis, sentiment tracking, and customer insight reporting using Botpress and AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/253ff92f-ccac-5b95-91a3-5ba0dc2aa92f)

---

## Category
**Primary category:** Data analytics
**Secondary tags:** conversation analytics, botpress, customer insights, sentiment analysis, data reporting, ai workflow, support automation, business intelligence.

This solution bridges the gap between raw chatbot interactions and strategic decision-making by automating the extraction of key performance indicators from your conversational data.

---

## Who is this for?
This solution is designed for teams looking to turn high-volume chat traffic into a strategic asset.

*   **Customer Support Manager**
    *   Identify recurring ticket themes to reduce support volume and improve self-service documentation.
*   **Product Manager**
    *   Gather direct user feedback and feature requests extracted from real-time customer conversations.
*   **Data Analyst**
    *   Automate the hygiene and categorization of unstructured chat logs for downstream reporting in BI tools.
*   **Operations Lead**
    *   Monitor bot performance and sentiment trends to ensure high-quality automated interactions.

---

## Features
- **Automated Transcript Ingestion**
    Seamlessly pulls conversation logs from Botpress to ensure your analytics are always based on the latest customer interactions.
- **Sentiment Trend Analysis**
    Uses advanced LLM reasoning to categorize conversations by sentiment, highlighting shifts in customer satisfaction over time.
- **Actionable Insight Extraction**
    Automatically identifies and summarizes key user intent, common questions, and unresolved issues within chat threads.
- **Structured Data Formatting**
    Converts unstructured text into clean, JSON-ready formats for easy integration with external dashboards and databases.
- **Real-time Reporting Triggers**
    Configurable alerts that notify stakeholders when specific keywords or negative sentiment thresholds are detected.

---

## Use Cases
**Support Quality Assurance**
*   Automatically flag conversations with negative sentiment for manual review by team leads.
*   Generate weekly summaries of the top 5 most frequent customer inquiries to guide training.

**Product Feedback Loop**
*   Extract specific feature requests or bug reports mentioned by users during support sessions.
*   Categorize feedback by product area to prioritize the engineering roadmap based on actual user demand.

**Operational Efficiency**
*   Identify "dead-end" bot conversations where users were forced to escalate to a human agent.
*   Track the resolution rate of automated flows to optimize bot responses and reduce support overhead.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your target workspace and project environment.
3. Authenticate your Botpress connection within the integration settings.
4. Ensure nodes are correctly mapped to your local environment and verify the connection status of the Composio Toolset.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw conversation logs or transcript IDs from your Botpress environment.
*   **Agent**: Processes the text using an LLM to perform sentiment analysis and intent classification.
*   **Composio Toolset**: Connects to your data storage or reporting API to push the generated insights.
*   **Chat Output**: Delivers the final summary report or confirmation status back to the user or dashboard.

### 3) Run the Flow
Use the Playground to test your analytics pipeline with these prompts:
* `Analyze the last 50 conversations and generate a summary of top customer complaints.`
* `Identify all conversations from yesterday that ended with negative sentiment.`
* `Extract feature requests from the latest chat logs and format them as a CSV list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node requires a model capable of high-context reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
*   **Role:** Act as a data analyst specializing in conversational AI and customer sentiment.
*   **Instruction Pattern:** 
    *   Analyze the provided transcript for intent, sentiment, and key entities.
    *   Summarize findings into a structured format suitable for business reporting.
    *   Flag any urgent issues that require immediate human intervention.

### 2) Composio Toolset Node
*   **API Key:** Provide your valid Composio API key in the node settings.
*   **Connection Scope:** Ensure the Botpress and relevant database/reporting tool connectors are authorized for read/write access.

### 3) Tool Availability
*   **Botpress Connector**: For fetching conversation logs and transcript history.
*   **Data Formatting Tools**: For parsing and structuring extracted insights.
*   **Notification/Reporting APIs**: For delivering the final analytics report to your team.

---

## Related Solutions
*   [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Deploy a 24/7 automated support assistant.
*   [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Manage support tickets directly through WhatsApp.
*   [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational health of your automated workflows.
