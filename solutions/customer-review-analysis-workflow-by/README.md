# Customer Review Analysis Workflow (Uplizd) - Automated sentiment classification and feedback routing

## Summary
The Customer Review Analysis Workflow leverages Uplizd and the Composio Toolset to ingest, classify, and act upon customer feedback in real-time. By automating sentiment analysis and issue categorization, this workflow enables support and product teams to prioritize high-impact feedback, reduce manual triage time, and maintain a single source of truth for customer satisfaction metrics.

---

## Demo
![Workflow diagram showing customer review input flowing through an AI agent to sentiment classification and CRM routing](image.png)
**Alt text (SEO-ready):** Uplizd customer review analysis workflow, AI-driven sentiment classification, automated feedback routing, and CRM integration for support teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6529b463-53e3-59a9-b402-26c7e192b622)

---

## Category
- **Primary category:** Customer Experience Operations
- **Secondary tags:** customer feedback, sentiment analysis, crm, support automation, data hygiene, composio, ai workflow, review management
- This solution bridges the gap between raw customer feedback and actionable product insights by automating the classification and routing process.

---

## Who is this for?
This workflow is designed for teams managing high volumes of customer feedback who need to scale their response capabilities without sacrificing quality.

- **Customer Support Manager**
    - Reduces ticket triage time by automatically routing negative sentiment reviews to priority queues.
- **Product Manager**
    - Aggregates feature requests and bug reports from reviews to inform the product roadmap.
- **Customer Success Lead**
    - Identifies at-risk accounts early by monitoring trends in customer sentiment and satisfaction scores.
- **Operations Analyst**
    - Maintains clean, categorized data in the CRM for accurate reporting on customer health and churn risk.

---

## Features
- **Automated Sentiment Scoring**
    - Uses advanced LLMs to detect emotional tone, providing a granular sentiment score for every incoming review.
- **Intelligent Issue Categorization**
    - Automatically tags feedback as 'Bug', 'Feature Request', 'Pricing', or 'Usability' to ensure it reaches the correct department.
- **Real-time CRM Sync**
    - Pushes categorized feedback directly into your CRM via the Composio Toolset, ensuring data is always up-to-date.
- **Priority Routing Logic**
    - Triggers immediate alerts for 'Critical' or 'Negative' sentiment reviews, enabling rapid service recovery.
- **Unified Feedback Dashboard**
    - Consolidates reviews from multiple platforms into a single, searchable database for comprehensive trend analysis.

---

## Use Cases
**Support Triage and Response**
- Automatically flag negative reviews for immediate follow-up by the customer success team.
- Route technical bug reports directly to the engineering backlog via Jira or GitHub integration.

**Product Development Insights**
- Extract recurring feature requests from user reviews to prioritize upcoming sprint planning.
- Monitor sentiment shifts following a new product release to gauge user adoption and satisfaction.

**Customer Health Monitoring**
- Track sentiment trends over time to identify accounts that may be at risk of churn.
- Generate weekly reports summarizing key customer pain points and requested improvements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your preferred CRM and feedback source platforms via the Composio Toolset.
3. Configure the environment variables for your LLM and API authentication.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw review text and metadata from your feedback platform.
- **Agent**: Analyzes the text for sentiment and intent using your chosen LLM.
- **Composio Toolset**: Executes the categorization and CRM update actions.
- **Chat Output**: Confirms successful routing and provides a summary of the classification.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Analyze the sentiment of the latest review from ID 9928 and update the CRM record.`
- `Categorize all pending reviews from the last 24 hours and flag any with negative sentiment.`
- `Summarize the top three product complaints from this week's reviews and create a Jira ticket.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the operation, responsible for interpreting natural language and determining the appropriate action.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on your specific taxonomy for 'Issue Types'.
- Enable structured output (JSON mode) to ensure the Composio Toolset receives clean data.

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and has permissions for your CRM and ticketing tools.
- **Connection Scope**: Grant the agent access to read feedback sources and write to your CRM/Project Management tools.

### 3) Tool Availability
- **CRM Connector**: For updating account records and sentiment fields.
- **Ticketing Connector**: For creating bug reports or task items.
- **Notification Connector**: For sending alerts to Slack or Email when critical feedback is detected.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automate support responses using AI.
- [crm-data-sync-agent](../crm-data-sync-agent/README.md) - Keep your customer data synchronized across platforms.
- [whats-app-feedback-collection-agent-by-whatsapp](../whats-app-feedback-collection-agent-by-whatsapp/README.md) - Collect customer feedback directly via WhatsApp.
