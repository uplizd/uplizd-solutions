# Customer Call Analyzer (Uplizd) - Transform sales and support calls into actionable customer insights

## Summary
The Customer Call Analyzer (Uplizd) is an AI-driven workflow that automates the transcription, sentiment analysis, and insight extraction from customer interactions. By leveraging the Rev AI integration, this solution provides teams with a single source of truth for voice data, enabling faster pipeline velocity, improved support quality, and proactive churn management through automated data hygiene and CRM logging.

---

## Demo
![Customer Call Analyzer workflow showing Rev AI transcription and CRM insight logging](image.png)
**Alt text (SEO-ready):** Customer Call Analyzer (Uplizd) workflow for automated transcription, sentiment analysis, and CRM data synchronization using Rev AI and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/50218b0b-82bc-5da3-81a8-77a5940f5e00)

---

## Category
**Primary category:** Support operations
**Secondary tags:** crm, rev-ai, voice-analytics, sentiment-analysis, customer-support, data-sync, composio, ai-workflow

This solution bridges the gap between raw audio recordings and structured CRM data, ensuring that every customer conversation is analyzed and indexed for business intelligence.

---

## Who is this for?
This workflow is designed for revenue and support teams looking to turn unstructured voice data into strategic assets.

* **Sales Managers**
    * Gain visibility into objection handling and closing techniques across the entire team.
* **Customer Success Leads**
    * Identify at-risk accounts early by monitoring sentiment shifts in recurring support calls.
* **RevOps Specialists**
    * Automate the logging of call summaries directly into CRM fields to maintain data hygiene.
* **Product Managers**
    * Extract recurring feature requests and pain points directly from the voice of the customer.

---

## Features
- **Automated Transcription**
  Leverage Rev AI to convert high-fidelity audio files into accurate, timestamped text transcripts.
- **Sentiment Analysis**
  Automatically detect emotional tone and urgency levels to prioritize follow-up actions.
- **CRM Integration**
  Use the Composio Toolset to push summarized insights and action items directly into your CRM.
- **Action Item Extraction**
  Identify and categorize tasks mentioned during calls to ensure no customer commitment is missed.
- **Real-time Data Sync**
  Maintain a synchronized record of customer interactions across your support and sales platforms.

---

## Use Cases
**Sales Performance Optimization**
* Analyze discovery calls to identify the most effective pitch patterns for high-conversion deals.
* Automatically update CRM opportunity fields based on the sentiment detected in the final negotiation call.

**Customer Support Excellence**
* Triage support tickets by analyzing the urgency and frustration levels in incoming voice messages.
* Generate automated summaries for support managers to review complex escalations without listening to full recordings.

**Product Feedback Loop**
* Aggregate mentions of specific product features across multiple calls to inform the product roadmap.
* Flag recurring technical issues or bugs reported by customers for immediate engineering review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Call Analyzer template from the marketplace.
3. Connect your Rev AI and CRM credentials via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the audio file URL or raw recording data.
* **Agent**: Processes the transcript, performs sentiment analysis, and structures the summary.
* **Composio Toolset**: Executes the API calls to update your CRM with the extracted data.
* **Chat Output**: Returns the final summary and confirmation of the CRM update.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Analyze the sentiment of the latest call recording and update the CRM opportunity notes.`
* `Extract all action items from this transcript and create tasks for the account owner.`
* `Summarize the customer's primary pain points and flag this call for manager review.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized analyst that interprets voice data and formats it for business systems.
* Use a model with strong summarization capabilities (e.g., GPT-4o or Claude 3.5).
* Instruct the agent to prioritize objective facts over subjective interpretation.
* Ensure the agent is configured to output JSON for seamless CRM field mapping.

### 2) Composio Toolset Node
* Provide your API key to authenticate with the Composio platform.
* Scope the connection to allow read/write access to your specific CRM objects (e.g., Opportunities, Tickets).

### 3) Tool Availability
* **Rev AI Connector**: For high-accuracy audio-to-text conversion.
* **CRM Connector**: For updating contact records, opportunity notes, and task lists.
* **Sentiment Analysis Engine**: For quantifying customer satisfaction and urgency.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms with automated conflict resolution.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-ups to keep your pipeline moving.
* [Account Intelligence Reporter](../account-intelligence-reporter/README.md) - Aggregate account-level insights to drive personalized outreach.
