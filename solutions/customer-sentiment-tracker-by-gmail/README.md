# Customer Sentiment Tracker (Uplizd) - Automated email sentiment analysis for customer satisfaction

## Summary
The Customer Sentiment Tracker is an intelligent Uplizd AI workflow that automatically scans incoming emails to detect, categorize, and report on customer sentiment. By leveraging the Composio Toolset to interface with Gmail, this solution enables support teams to prioritize urgent issues, identify dissatisfied customers in real-time, and maintain a high standard of service quality without manual triage.

---

## Demo
![Customer Sentiment Tracker dashboard showing email sentiment analysis and priority flagging](image.png)
**Alt text (SEO-ready):** Customer Sentiment Tracker dashboard showing email sentiment analysis, Uplizd AI workflow, Gmail integration, and priority flagging.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7fee3794-d84e-52dc-ac48-25628b9d6915)

---

## Category
- **Primary category:** Support automation
- **Secondary tags:** crm, gmail, sentiment analysis, customer satisfaction, support, ai workflow, composio, data hygiene
- This solution bridges the gap between raw communication and actionable support intelligence by automating the sentiment classification of every incoming customer inquiry.

---

## Who is this for?
This workflow is designed for teams looking to transform unstructured email data into actionable customer insights.

- **Support Manager**
    - Gain immediate visibility into team performance and customer frustration levels across all support queues.
- **Customer Success Lead**
    - Proactively identify at-risk accounts by monitoring negative sentiment trends before they lead to churn.
- **Operations Analyst**
    - Streamline support workflows by automating the tagging and categorization of incoming tickets based on emotional tone.
- **Support Agent**
    - Focus on high-priority, dissatisfied customers first by utilizing automated sentiment-based task prioritization.

---

## Features
- **Real-time Sentiment Detection**
  Automatically analyzes the tone of incoming emails using advanced LLM processing to categorize sentiment as positive, neutral, or negative.
- **Gmail Integration**
  Seamlessly connects to your inbox via the Composio Toolset to fetch, read, and label emails without manual intervention.
- **Priority Flagging**
  Automatically tags and prioritizes negative sentiment emails, ensuring urgent customer issues are escalated to the right team members.
- **Automated Reporting**
  Aggregates sentiment data over time to provide a clear view of customer satisfaction trends and service quality metrics.
- **Customizable Thresholds**
  Allows teams to define specific keywords or sentiment scores that trigger automated alerts or specific routing rules.

---

## Use Cases
**Proactive Churn Prevention**
- Automatically flag emails from key accounts that contain negative sentiment for immediate account manager review.
- Generate weekly sentiment summaries to identify recurring pain points that lead to customer dissatisfaction.

**Support Efficiency Optimization**
- Route negative sentiment emails to a dedicated "High Priority" folder to reduce response times for frustrated users.
- Automatically draft empathetic responses for agents based on the detected sentiment of the customer's email.

**Service Quality Monitoring**
- Track the impact of new product releases on customer sentiment by comparing pre- and post-launch email tone metrics.
- Identify training opportunities for support staff by analyzing interactions where customer sentiment improved or declined during the thread.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Gmail account via the Composio Toolset integration.
3. Configure your notification channels (e.g., Slack or Email) to receive sentiment alerts.
4. Ensure nodes are correctly mapped from Chat Input to Chat Output to enable end-to-end processing.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to scan the inbox.
- **Agent**: Processes email content and evaluates sentiment using the configured LLM instructions.
- **Composio Toolset**: Executes Gmail API calls to fetch emails and apply labels or tags.
- **Chat Output**: Delivers the final sentiment report or notification to the designated dashboard or user.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Analyze the sentiment of the last 10 emails in my inbox and summarize the findings.`
- `Flag all emails from the last 24 hours that show negative sentiment and move them to the 'Urgent' folder.`
- `Generate a report on customer sentiment trends for the current week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting the emotional content of text.
- **Instruction Pattern:**
    - "Analyze the provided email text and assign a sentiment score between -1 and 1."
    - "Identify key topics or complaints mentioned in emails flagged as negative."
    - "Maintain a neutral, objective tone when summarizing customer feedback for the support team."

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to authorize the connection.
- **Connection Scope:** Ensure the Gmail integration has read/write access to labels and messages to perform accurate analysis and tagging.

### 3) Tool Availability
- **Gmail.list_messages**: To fetch recent incoming inquiries.
- **Gmail.get_message**: To retrieve the full body content for analysis.
- **Gmail.update_message**: To apply labels or move emails based on sentiment results.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Comprehensive AI-driven support automation.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Multi-channel support triage and prioritization.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Monitoring account health through usage data.
