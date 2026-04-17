# Feedback Triage Agent (Uplizd) - Automated Customer Feedback Categorization and Prioritization

## Summary
The Feedback Triage Agent is an intelligent workflow designed to streamline product feedback loops by automatically ingesting, categorizing, and prioritizing user submissions from Canny. By leveraging AI to analyze sentiment and urgency, this solution ensures that product teams focus on high-impact feature requests and critical bug reports, significantly reducing manual triage time and improving pipeline velocity.

---

## Demo
![Feedback Triage Agent workflow dashboard showing automated categorization of Canny feedback items into priority buckets](image.png)
**Alt text (SEO-ready):** Uplizd Feedback Triage Agent workflow for Canny, showing automated feedback categorization, sentiment analysis, and priority scoring for product teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/78b13d33-c64e-52e2-8b2e-6c2c29a9f19d)

---

## Category
- **Primary category:** Support automation
- **Secondary tags:** canny, feedback, product management, customer support, ai workflow, triage, prioritization, composio
- This solution bridges the gap between raw customer feedback and actionable product development by automating the organization of incoming data.

---

## Who is this for?
This workflow is designed for product-led organizations looking to maintain a clean and actionable feedback loop.

- **Product Managers**
    - Quickly identify high-demand feature requests to inform the product roadmap.
- **Customer Success Leads**
    - Ensure critical user pain points are escalated to engineering without manual intervention.
- **Support Operations**
    - Reduce the overhead of manual ticket tagging and feedback sorting.
- **Engineering Managers**
    - Receive pre-prioritized bug reports that are ready for immediate sprint planning.

---

## Features
- **Automated Sentiment Analysis**
    - Uses AI to detect user frustration or urgency in feedback text to trigger immediate alerts.
- **Intelligent Categorization**
    - Automatically maps incoming Canny posts to specific product areas or functional modules.
- **Dynamic Prioritization**
    - Assigns priority scores based on predefined business logic and feedback volume.
- **Composio-Powered Integration**
    - Seamlessly connects with Canny and other project management tools to sync data in real-time.
- **Customizable Thresholds**
    - Allows teams to set specific triggers for when feedback requires human review versus automated logging.

---

## Use Cases
**Feedback Pipeline Management**
- Automatically tagging new posts as "Feature Request," "Bug," or "UI/UX Improvement."
- Routing high-priority bugs directly to a Jira or Linear board for immediate visibility.

**Customer Sentiment Tracking**
- Aggregating feedback to identify recurring themes that impact user retention.
- Alerting the success team when a "Churn Risk" sentiment is detected in a user post.

**Product Roadmap Alignment**
- Summarizing top-voted requests for weekly product planning meetings.
- Filtering out duplicate feedback to keep the product backlog clean and manageable.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Feedback Triage Agent.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Canny API credentials via the Composio Toolset node.
4. Ensure nodes are correctly linked from Chat Input through the Agent to the final Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw feedback data or manual triggers for triage.
- **Agent**: Analyzes the feedback content against your product taxonomy.
- **Composio Toolset**: Executes API calls to update Canny statuses or push to external trackers.
- **Chat Output**: Returns the triage summary and confirmation of actions taken.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Triage the latest feedback posts from the last 24 hours and categorize by urgency.`
- `Find all feature requests related to 'mobile app' and summarize the top 3 pain points.`
- `Identify any high-priority bug reports in Canny and create a summary report for the engineering team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized product analyst.
- **Instruction Pattern:**
    - Analyze the intent and sentiment of the provided feedback text.
    - Categorize feedback based on the provided product taxonomy.
    - Assign a priority score (1-5) based on urgency and user sentiment.

### 2) Composio Toolset Node
- Requires a valid Canny API key with read/write permissions.
- Ensure the connection scope includes `posts:read` and `posts:write` to enable automated status updates.

### 3) Tool Availability
- **Canny API**: For fetching posts, updating statuses, and adding internal comments.
- **Sentiment Analyzer**: For detecting user emotion and urgency.
- **Categorization Engine**: For mapping feedback to product modules.

---

## Related Solutions
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Automated customer support responses.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Triage support tickets via WhatsApp.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Monitor account health and usage metrics.
