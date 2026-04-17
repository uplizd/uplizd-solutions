# Customer Call Analyzer (Uplizd) - Automated transcription and insight extraction for sales and support calls

## Summary
The Customer Call Analyzer by CastingWords is an intelligent Uplizd workflow that processes audio recordings to generate accurate transcripts, identify key customer pain points, and extract actionable follow-up tasks. By automating the analysis of voice interactions, teams can ensure consistent service quality, reduce manual documentation time, and maintain a single source of truth for customer feedback across the organization.

---

## Demo
![Customer Call Analyzer workflow interface showing audio processing and insight extraction nodes](image.png)
**Alt text (SEO-ready):** Uplizd Customer Call Analyzer workflow interface showing audio transcription, sentiment analysis, and action item extraction using CastingWords and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/49142ab3-e42f-500c-96fa-d9f61cde7b60)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** voice analytics, transcription, sales enablement, customer insights, ai workflow, composio, call recording
- This solution bridges the gap between raw audio data and structured business intelligence, enabling teams to optimize their communication strategy.

---

## Who is this for?
This solution is designed for teams that rely on voice-based communication to drive revenue and customer satisfaction.

- **Sales Managers**
    - Gain visibility into call performance and identify coaching opportunities for the team.
- **Customer Success Leads**
    - Monitor sentiment trends to proactively address churn risks before they escalate.
- **Support Operations**
    - Automate the logging of support tickets and action items directly from customer conversations.
- **Product Managers**
    - Extract direct feature requests and user feedback from real-world customer calls.

---

## Features
- **Automated Transcription**
    - Leverages high-accuracy speech-to-text engines to convert call audio into searchable, structured text.
- **Sentiment Analysis**
    - Detects emotional shifts and tone throughout the conversation to gauge customer satisfaction levels.
- **Action Item Extraction**
    - Automatically identifies commitments made during calls and maps them to follow-up tasks.
- **CRM Integration**
    - Uses the Composio Toolset to push summarized insights and tasks directly into your connected CRM.
- **Real-time Insight Dashboard**
    - Provides a centralized view of key topics and recurring customer concerns across multiple calls.

---

## Use Cases
**Sales Performance Optimization**
- Analyze discovery calls to identify common objections and refine the sales pitch.
- Automatically log meeting summaries into the CRM to keep the pipeline updated without manual entry.

**Customer Support Quality Assurance**
- Review support interactions to ensure compliance with company communication standards.
- Flag calls with negative sentiment for immediate management review and follow-up.

**Product Feedback Loop**
- Aggregate mentions of specific product features or bugs across all customer support calls.
- Generate monthly reports on top customer pain points to inform the product roadmap.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Call Analyzer template from the marketplace.
3. Connect your CastingWords API credentials and CRM integration via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts audio file URLs or raw audio data from your call recording platform.
- **Agent**: Processes the transcription and performs intent recognition to extract key insights.
- **Composio Toolset**: Executes API calls to push data into external systems like Salesforce or HubSpot.
- **Chat Output**: Returns the structured summary, sentiment score, and list of action items.

### 3) Run the Flow
Use the Playground to test the flow with these example prompts:
- `Analyze this call recording URL for primary customer pain points and list three action items.`
- `Summarize the sentiment of the last support call and update the CRM record with the findings.`
- `Extract all feature requests mentioned in the provided audio file and format them as a bulleted list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent is configured to act as a specialized business analyst.
- Use a high-context window model to ensure long-form transcripts are analyzed accurately.
- Instruct the agent to prioritize "Actionable Items" over general conversation filler.
- Maintain a neutral, professional tone for all extracted summaries.

### 2) Composio Toolset Node
- Provide your API key within the Composio node settings.
- Ensure the connection scope includes write access to your CRM (e.g., Salesforce, HubSpot) to allow for automatic task creation.

### 3) Tool Availability
- **Transcription Service**: Handles audio-to-text conversion.
- **CRM Connector**: Syncs extracted action items to specific deal or contact records.
- **Sentiment Engine**: Analyzes text for positive/negative polarity.
- **Task Manager**: Creates follow-up reminders in your project management tool.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automated voice-based support interactions.
- [247-customer-support-voice-assistant-by-synthflow-ai](../247-customer-support-voice-assistant-by-synthflow-ai/README.md) - AI-driven voice assistant for customer service.
- [account-intelligence-reporter-by-leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Reporting tool for account-level insights.
