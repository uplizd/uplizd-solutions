# Customer Feedback Analyzer (Uplizd) - Automated sentiment and insight extraction for customer feedback

## Summary
The Customer Feedback Analyzer is an intelligent Uplizd workflow designed to ingest, process, and categorize customer feedback from multiple channels. By leveraging the Tisane AI engine, this solution transforms unstructured text into actionable sentiment data and thematic insights, helping support and product teams maintain a single source of truth for user satisfaction and pipeline velocity.

---

## Demo
![Customer Feedback Analyzer dashboard showing sentiment trends and thematic categorization](image.png)
**Alt text (SEO-ready):** Customer Feedback Analyzer Uplizd workflow dashboard showing sentiment trends, thematic categorization, and automated feedback processing using Tisane AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/eee8aec6-4384-556a-a562-a87bb72f79d8)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** `feedback`, `sentiment analysis`, `tisane`, `customer experience`, `cx`, `data hygiene`, `ai workflow`, `composio`
- This solution bridges the gap between raw customer communication and structured product intelligence through automated natural language processing.

---

## Who is this for?
This workflow is designed for teams that need to turn high volumes of qualitative feedback into quantitative business intelligence.

- **Customer Support Manager**
    - Identifies recurring pain points to reduce ticket volume and improve response quality.
- **Product Manager**
    - Aggregates user sentiment to prioritize feature requests and roadmap development.
- **Customer Success Lead**
    - Detects churn signals early by monitoring negative sentiment trends in client feedback.
- **Operations Analyst**
    - Maintains data hygiene by standardizing feedback inputs into a unified reporting format.

---

## Features
- **Automated Sentiment Scoring**
    - Utilizes Tisane AI to assign precise sentiment polarity to every incoming feedback entry.
- **Thematic Insight Extraction**
    - Automatically tags feedback with relevant topics, such as "UI/UX," "Performance," or "Pricing."
- **Multi-Channel Integration**
    - Connects via the Composio Toolset to ingest feedback from email, chat, and support ticketing platforms.
- **Real-Time Alerting**
    - Triggers notifications for high-priority negative feedback to ensure immediate service recovery.
- **Structured Data Export**
    - Normalizes unstructured text into a clean, queryable format for downstream CRM or BI tools.

---

## Use Cases
**Support Ticket Triage**
- Automatically categorize incoming tickets based on sentiment intensity to prioritize urgent issues.
- Route feedback to the appropriate department (e.g., Engineering for bugs, Sales for feature requests).

**Product Feedback Loop**
- Aggregate monthly sentiment trends to present to stakeholders during product review meetings.
- Identify specific feature friction points by filtering feedback by thematic tags.

**Churn Prevention**
- Flag feedback containing "cancellation" or "frustrated" keywords for immediate intervention by Success teams.
- Monitor sentiment shifts following new feature releases to gauge user adoption and satisfaction.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the template in your workspace.
2. Connect your required API credentials for the Tisane AI and your target CRM/Support platform.
3. Configure the trigger node to point to your primary feedback collection channel.
4. Ensure nodes are correctly mapped from the **Chat Input** to the **Agent** and finally to the **Composio Toolset** for execution.

### 2) Setup the Nodes
- **Chat Input**: Receives raw customer feedback strings or ticket bodies.
- **Agent**: Analyzes the input text using the Tisane AI model to extract sentiment and intent.
- **Composio Toolset**: Executes the categorization and data sync actions across your connected tools.
- **Chat Output**: Returns the processed summary and sentiment classification to the user or dashboard.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Analyze the sentiment of this feedback: "The new dashboard is confusing and slow to load."`
- `Categorize the following feedback and identify the core issue: "I love the new export feature, but it keeps crashing on large files."`
- `Summarize the top 3 pain points from the latest batch of support feedback.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary orchestrator for linguistic analysis.
- Set the system prompt to prioritize objective sentiment classification.
- Ensure the model is configured to output JSON for consistent downstream data handling.
- Use a high-context window to allow the agent to reference previous feedback for trend analysis.

### 2) Composio Toolset Node
- Provide your valid API key to enable secure communication with your support platforms.
- Set the connection scope to include read/write access to your ticketing or CRM system.

### 3) Tool Availability
- **Tisane API**: For deep linguistic analysis and sentiment detection.
- **CRM Connector**: For logging feedback directly to user profiles.
- **Notification Service**: For alerting teams to critical sentiment spikes.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - General support automation for high-volume ticket handling.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Conversational chatbot for real-time customer interaction.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Triage agent specifically for WhatsApp-based support channels.
