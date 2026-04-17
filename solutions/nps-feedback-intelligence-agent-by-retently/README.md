# NPS Feedback Intelligence Agent (Uplizd) - Automate customer sentiment analysis and feedback categorization

## Summary
The NPS Feedback Intelligence Agent by Retently leverages Uplizd AI workflows to automatically ingest, categorize, and synthesize customer feedback data. By connecting directly to your feedback streams, this agent identifies actionable improvement opportunities, reduces manual data processing time, and provides a single source of truth for customer sentiment, enabling teams to respond faster to critical product or service friction.

---

## Demo
![NPS Feedback Intelligence Agent workflow dashboard showing automated sentiment analysis and categorization nodes](image.png)
**Alt text (SEO-ready):** NPS Feedback Intelligence Agent workflow dashboard showing automated sentiment analysis and categorization nodes for Uplizd AI and Retently integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8488fdd1-54b0-5c51-ad5f-69700516112e)

---

## Category
- **Primary category:** Customer Experience (CX) Operations
- **Secondary tags:** nps, feedback, sentiment analysis, retently, customer insights, data automation, composio, ai workflow
- This solution bridges the gap between raw customer feedback and strategic product decisions by automating the classification and reporting of NPS data.

---

## Who is this for?
This agent is designed for teams focused on closing the feedback loop and improving customer retention through data-driven insights.

- **Customer Success Manager**
    - Proactively identify at-risk accounts based on negative sentiment trends in recent NPS surveys.
- **Product Manager**
    - Aggregate feature requests and pain points from qualitative feedback to prioritize the product roadmap.
- **Operations Lead**
    - Automate the hygiene and categorization of feedback data to ensure reporting accuracy across the organization.
- **Support Team Lead**
    - Trigger automated follow-up workflows for customers who provide low NPS scores to resolve issues immediately.

---

## Features
- **Automated Sentiment Scoring**
    - Uses advanced LLMs to analyze text-based feedback and assign sentiment polarity scores in real-time.
- **Intelligent Categorization**
    - Automatically tags feedback into predefined buckets like "Pricing," "Usability," or "Feature Request" using the Composio Toolset.
- **Seamless Retently Integration**
    - Connects directly to Retently to pull survey responses and push categorized insights back into your ecosystem.
- **Actionable Insight Extraction**
    - Distills long-form customer comments into concise summaries and key takeaways for executive review.
- **Real-time Alerting**
    - Triggers notifications for urgent negative feedback, ensuring high-priority issues are addressed by the right team members.

---

## Use Cases
**Feedback Loop Optimization**
- Automatically route negative NPS comments to the Customer Success team for immediate outreach.
- Sync categorized feedback into your internal project management tool to track recurring product issues.

**Sentiment Trend Analysis**
- Generate weekly reports on shifting customer sentiment across different user segments or subscription tiers.
- Identify correlations between specific product updates and changes in NPS scores over time.

**Operational Data Hygiene**
- Clean and standardize feedback entries by removing PII or irrelevant noise before analysis.
- Maintain a structured database of customer insights that is always up-to-date and ready for stakeholder reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the Uplizd builder.
2. Authenticate your Retently account via the Composio connection prompt.
3. Configure your target destination (e.g., Slack, CRM, or Spreadsheet) for the processed insights.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw NPS survey responses and metadata.
- **Agent**: Processes text, determines sentiment, and categorizes the feedback.
- **Composio Toolset**: Executes API calls to update Retently or push data to external platforms.
- **Chat Output**: Delivers the final summary and classification report to your dashboard or notification channel.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Analyze the latest NPS feedback from the last 24 hours and summarize the top 3 pain points.`
- `Categorize all feedback tagged as 'negative' and draft a follow-up response for the Customer Success team.`
- `Identify any recurring feature requests from this month's survey data and export them to our product board.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a CX analyst, focusing on empathy and objective data classification.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Act as a CX analyst. Categorize feedback accurately and flag urgent negative sentiment for immediate follow-up."
- Instruction: "Maintain a neutral, professional tone when summarizing qualitative feedback for stakeholders."

### 2) Composio Toolset Node
- Provide your Retently API key to enable read/write access to survey data.
- Ensure the connection scope includes `read:surveys` and `write:feedback_tags`.

### 3) Tool Availability
- **Retently API**: For fetching survey responses and updating feedback tags.
- **Notification Connectors**: For sending alerts to Slack, Microsoft Teams, or Email.
- **Data Formatting Tools**: For cleaning and structuring feedback text before analysis.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support ticket resolution and customer query handling.
- [whats-app-feedback-collection-agent-by-wati](../whats-app-feedback-collection-agent-by-wati/README.md) - Collect customer feedback directly through WhatsApp conversations.
- [crm-data-sync-agent](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms to ensure consistent insights.
