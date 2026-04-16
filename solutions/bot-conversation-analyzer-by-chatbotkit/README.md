# Bot Conversation Analyzer (Uplizd) - Optimize chatbot performance through automated conversation insights

## Summary
The Bot Conversation Analyzer is an intelligent Uplizd workflow designed to ingest, parse, and evaluate chatbot interaction logs to identify friction points, sentiment trends, and optimization opportunities. By automating the analysis of user-bot dialogues, this solution provides product teams and support managers with a single source of truth for improving conversational design, increasing resolution rates, and enhancing overall customer satisfaction.

---

## Demo
![Bot Conversation Analyzer workflow showing Chat Input, Agent analysis, and ChatbotKit integration](image.png)
**Alt text (SEO-ready):** Bot Conversation Analyzer Uplizd workflow for automated chatbot log analysis, sentiment tracking, and conversation optimization using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/882cdd9b-9ef4-56e0-b4ef-f3d2f45f3175)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** chatbot, conversation analysis, sentiment analysis, customer experience, cx, data insights, composio, ai workflow
- This solution bridges the gap between raw interaction data and actionable product improvements by leveraging AI to categorize and score user feedback.

---

## Who is this for?
This workflow is designed for teams looking to turn unstructured chat logs into structured product intelligence.

- **Product Manager**
    - Identify recurring user pain points to prioritize feature development and bot flow improvements.
- **Customer Support Lead**
    - Monitor agent or bot performance to ensure consistent quality and identify training gaps.
- **UX Researcher**
    - Analyze conversational patterns to refine user journeys and reduce friction in automated interactions.
- **Operations Analyst**
    - Track key performance metrics like sentiment trends and resolution efficiency across all support channels.

---

## Features
- **Automated Log Ingestion**
    - Seamlessly pulls conversation history from ChatbotKit and other connected platforms for real-time analysis.
- **Sentiment & Intent Scoring**
    - Automatically classifies user messages by sentiment and intent to highlight critical issues or positive feedback.
- **Friction Point Detection**
    - Pinpoints specific conversation turns where users express frustration or fail to reach a resolution.
- **Actionable Insight Reporting**
    - Generates concise summaries and recommended adjustments for bot scripts and response logic.
- **Composio Integration**
    - Leverages the Composio Toolset to securely interface with external CRM and analytics tools for data enrichment.

---

## Use Cases
**Conversation Quality Assurance**
- Flagging conversations where the bot failed to resolve the user's query for human review.
- Identifying high-frequency questions that require updated knowledge base documentation.

**Customer Sentiment Tracking**
- Aggregating daily sentiment scores to detect sudden drops in user satisfaction.
- Correlating negative sentiment spikes with specific bot deployment versions or script changes.

**Bot Workflow Optimization**
- Analyzing drop-off points in multi-turn conversations to streamline the user journey.
- Testing new response variations by comparing performance metrics before and after implementation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Bot Conversation Analyzer template from the marketplace.
3. Connect your ChatbotKit account via the Composio Toolset node.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw conversation logs or specific interaction IDs for processing.
- **Agent**: Analyzes the text for sentiment, intent, and potential improvement areas.
- **Composio Toolset**: Executes queries to fetch chat history and push insights to your dashboard.
- **Chat Output**: Delivers the final analysis report and actionable recommendations.

### 3) Run the Flow
Use the Playground to test the analysis capabilities:
- `Analyze the last 50 conversations and identify the top 3 reasons for user frustration.`
- `Generate a sentiment report for all interactions tagged with 'billing' from the last 24 hours.`
- `Summarize the most common user questions that the bot failed to answer correctly.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node requires a model capable of nuanced text analysis and structured output generation.
- Set the system prompt to prioritize objective analysis and clear, actionable feedback.
- Use a high-context window model to ensure the agent can process long conversation threads.
- Implement a JSON output schema to ensure the analysis results are easily readable by downstream tools.

### 2) Composio Toolset Node
- Provide your API key within the Composio node settings to authenticate with your chatbot platform.
- Define the scope to include read-only access to conversation logs to maintain data security.

### 3) Tool Availability
- **Log Retrieval**: Fetching historical chat transcripts.
- **Sentiment Analysis**: Scoring user inputs on a polarity scale.
- **Intent Classification**: Categorizing queries into predefined support topics.
- **Reporting**: Formatting insights into structured summaries.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support assistant for 24/7 customer query resolution.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Deployable chatbot solution for scalable customer engagement.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Intelligent triage agent for managing WhatsApp support tickets.
