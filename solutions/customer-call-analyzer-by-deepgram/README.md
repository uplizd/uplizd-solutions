# Customer Call Analyzer (Uplizd) - Automate insights from sales and support conversations

## Summary
The Customer Call Analyzer (Uplizd) workflow leverages advanced speech-to-text and natural language processing to transcribe, analyze, and extract actionable insights from customer interactions. By automating the evaluation of sales and support calls, teams can reduce manual review time, identify recurring customer pain points, and ensure consistent quality across all communication channels, creating a single source of truth for voice-based feedback.

---

## Demo
![Customer Call Analyzer workflow showing Deepgram transcription and AI-driven insight extraction](image.png)
**Alt text (SEO-ready):** Customer Call Analyzer workflow in Uplizd, featuring Deepgram speech-to-text integration, automated call transcription, and AI-driven sentiment analysis for sales and support teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f5770535-94f5-5773-8e9e-61de1cc7b5c7)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** deepgram, voice analytics, speech-to-text, crm, support automation, sentiment analysis, ai workflow, composio
- This solution bridges the gap between raw audio data and structured business intelligence, enabling teams to act on voice feedback instantly.

---

## Who is this for?
This solution is designed for organizations looking to scale their quality assurance and customer intelligence efforts through automated audio processing.

- **Support Manager**
    - Automate quality assurance scoring for support tickets to ensure consistent service delivery.
- **Sales Enablement Lead**
    - Identify winning talk tracks and common objections by analyzing high-performing sales calls.
- **Customer Success Manager**
    - Proactively detect churn signals and sentiment shifts in long-form customer conversations.
- **Product Manager**
    - Aggregate feature requests and usability complaints directly from customer voice feedback.

---

## Features
- **Automated Transcription**
    - High-accuracy speech-to-text processing using Deepgram to convert audio files into searchable text.
- **Sentiment Analysis**
    - Real-time detection of customer mood and tone throughout the conversation to flag high-priority interactions.
- **Action Item Extraction**
    - Automatically identifies follow-up tasks and commitments made during calls, syncing them directly to your CRM.
- **Topic Modeling**
    - Categorizes call segments by theme, such as pricing, technical issues, or feature requests, for easier reporting.
- **Composio Integration**
    - Seamlessly connects with your existing CRM and ticketing platforms to log insights without manual data entry.

---

## Use Cases
**Quality Assurance & Training**
- Automatically score support calls against predefined compliance and empathy rubrics.
- Identify training gaps by flagging calls where agents struggled to resolve specific technical queries.

**Sales Performance Optimization**
- Analyze successful sales calls to extract key phrases that lead to closed-won opportunities.
- Monitor objection handling performance to refine sales scripts and improve conversion rates.

**Customer Insight & Product Feedback**
- Aggregate recurring feature requests mentioned by customers during discovery calls.
- Detect early-stage churn risk by identifying negative sentiment trends in account management calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Call Analyzer template from the marketplace.
3. Connect your Deepgram and CRM credentials via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the audio file URL or raw recording data.
- **Agent**: Processes the transcription and performs sentiment and intent analysis.
- **Composio Toolset**: Executes actions to update CRM records or ticketing systems.
- **Chat Output**: Delivers the summary, sentiment report, and extracted action items.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Analyze this call recording for customer sentiment and list the top 3 pain points mentioned.`
- `Extract all action items from this transcript and create follow-up tasks in my CRM.`
- `Summarize this sales call and identify if the customer expressed interest in our premium tier.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the analytical engine for your audio data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment extraction.
- Provide a clear system prompt defining the desired output format (e.g., JSON or structured markdown).
- Configure the temperature to 0.2 to ensure consistent, objective analysis of call transcripts.

### 2) Composio Toolset Node
- Provide your API key to authenticate the connection between Uplizd and your CRM/Support platform.
- Define the scope to allow the agent to read/write to specific objects like "Tasks," "Opportunities," or "Tickets."

### 3) Tool Availability
- **CRM Connector**: For logging call summaries and creating follow-up tasks.
- **Transcription Service**: Deepgram API for high-fidelity audio conversion.
- **Notification Service**: To alert managers when a call with negative sentiment is detected.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automate voice-based customer support interactions.
- [247-customer-support-voice-assistant-by-synthflow-ai](../247-customer-support-voice-assistant-by-synthflow-ai/README.md) - Deploy intelligent voice assistants for 24/7 support.
- [account-intelligence-reporter-by-leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate comprehensive account intelligence reports.
