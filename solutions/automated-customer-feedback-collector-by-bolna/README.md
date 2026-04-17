# Automated Customer Feedback Collector (Uplizd) - Streamline voice-based customer insights

## Summary
The Automated Customer Feedback Collector is an intelligent Uplizd workflow that leverages Bolna voice AI to conduct conversational surveys, capturing real-time customer sentiment and actionable feedback. By automating the outreach and transcription process, this solution eliminates manual data entry, ensures consistent follow-up, and provides product and support teams with a unified source of truth for customer experience metrics.

---

## Demo
![Automated Customer Feedback Collector workflow diagram showing voice input processing and feedback logging](../image.png)
**Alt text (SEO-ready):** Automated Customer Feedback Collector workflow diagram showing voice input processing, Bolna voice AI integration, and feedback logging on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3c8c085b-3fc2-5186-b921-f086e9c5d402)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** voice ai, feedback collection, bolna, customer experience, sentiment analysis, automation, survey, nlp
- This solution bridges the gap between raw voice interactions and structured customer feedback data for improved operational intelligence.

---

## Who is this for?
This solution is designed for teams looking to scale their feedback loops without increasing manual overhead.

- **Customer Success Manager**
    - Automates post-interaction surveys to track Net Promoter Score (NPS) and customer satisfaction trends.
- **Product Manager**
    - Gathers qualitative voice data to identify feature requests and usability pain points directly from users.
- **Support Operations Lead**
    - Ensures consistent feedback collection across all support channels to maintain high service quality standards.
- **Growth Marketer**
    - Uses voice-captured testimonials and insights to refine messaging and identify high-value customer segments.

---

## Features
- **Conversational Voice Surveys**
    - Uses Bolna AI to conduct natural, human-like voice interviews that increase response rates compared to static forms.
- **Real-time Sentiment Analysis**
    - Automatically processes audio transcripts to detect emotional tone and urgency, flagging negative feedback for immediate attention.
- **Automated CRM Sync**
    - Seamlessly pushes feedback data into your CRM, ensuring that customer profiles are always updated with the latest interaction history.
- **Customizable Survey Logic**
    - Allows for dynamic branching based on user responses, ensuring the agent asks the most relevant follow-up questions.
- **Unified Feedback Dashboard**
    - Aggregates all voice-collected data into a single source of truth, making it easy to report on trends and performance metrics.

---

## Use Cases
**Post-Support Follow-up**
- Trigger a voice survey immediately after a support ticket is resolved to measure resolution quality.
- Automatically log satisfaction scores back into the ticketing system for performance tracking.

**Product Development Insights**
- Conduct targeted voice interviews with users after a new feature release to gather usability feedback.
- Categorize and prioritize feature requests based on frequency and sentiment detected during voice sessions.

**Customer Health Monitoring**
- Proactively reach out to at-risk accounts to gather feedback before churn occurs.
- Identify common themes in negative feedback to proactively adjust service or product strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Automated Customer Feedback Collector.
2. Click "Import" to add the workflow template to your workspace.
3. Configure your Bolna API credentials and CRM integration keys in the settings panel.
4. Ensure nodes are correctly mapped to your specific voice survey script and data destination fields.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event (e.g., ticket closure or scheduled outreach).
- **Agent**: Processes the conversation logic and manages the Bolna voice interaction.
- **Composio Toolset**: Connects the agent to your CRM and database to store feedback.
- **Chat Output**: Confirms the successful logging of feedback and triggers any necessary follow-up alerts.

### 3) Run the Flow
Use the Uplizd Playground to test your survey logic with these example prompts:
- `Initiate a feedback survey for customer ID 9872 after their recent support ticket closure.`
- `Run a sentiment analysis on the latest batch of voice feedback and summarize the top 3 product complaints.`
- `Trigger a follow-up survey for all users who provided a satisfaction score below 3 in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the conversational interface for the voice survey.
- Maintain a professional, empathetic tone throughout the survey.
- Use clear, concise questions to minimize user confusion.
- Ensure the agent adheres to the defined survey script while allowing for natural conversational flow.

### 2) Composio Toolset Node
- Provide your API key for the relevant CRM or database integration.
- Set the connection scope to allow the agent to read customer data and write feedback entries.

### 3) Tool Availability
- **CRM Connector**: For retrieving customer contact info and logging feedback.
- **Bolna Voice Engine**: For executing the conversational survey and transcribing audio.
- **Sentiment Analysis Tool**: For evaluating the emotional content of the transcribed feedback.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automate 24/7 support interactions using voice AI.
- [whats-app-feedback-collection-agent-by-wati](../whats-app-feedback-collection-agent-by-wati/README.md) - Collect customer feedback via automated WhatsApp messaging.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Track and monitor customer account health through form-based usage data.
