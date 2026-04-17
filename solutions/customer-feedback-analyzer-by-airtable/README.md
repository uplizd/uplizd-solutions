# Customer Feedback Analyzer (Uplizd) - Automated sentiment analysis and product insight extraction

## Summary
The Customer Feedback Analyzer is an intelligent Uplizd workflow that ingests raw customer feedback from Airtable, categorizes sentiment, and prioritizes actionable product insights. By automating the classification of user input, this solution helps product teams maintain a single source of truth for feature requests and bug reports, significantly increasing pipeline velocity and data hygiene across the development lifecycle.

---

## Demo
![Customer Feedback Analyzer workflow diagram showing Airtable data ingestion, AI sentiment analysis, and categorized output](image.png)
**Alt text (SEO-ready):** Customer Feedback Analyzer (Uplizd) workflow for automated sentiment analysis, Airtable data integration, and product feedback prioritization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/dcd65728-9256-5247-bbb4-24d55bc3b708)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** airtable, feedback, sentiment analysis, product management, data hygiene, composio, ai workflow, customer insights
- This solution bridges the gap between raw customer communication and structured product development data.

---

## Who is this for?
This solution is designed for teams looking to turn qualitative user feedback into quantitative product strategy.

- **Product Managers**
    - Automatically surface high-priority feature requests and recurring pain points from raw feedback logs.
- **Customer Success Leads**
    - Identify at-risk accounts by flagging negative sentiment trends in real-time feedback submissions.
- **Support Operations**
    - Reduce manual triage time by auto-tagging incoming tickets and feedback entries for faster routing.
- **Data Analysts**
    - Maintain clean, categorized datasets in Airtable for reporting on product health and user satisfaction.

---

## Features
- **Automated Sentiment Scoring**
    - Uses advanced LLM processing to assign polarity scores to every feedback entry, enabling quick identification of frustrated users.
- **Intelligent Categorization**
    - Automatically maps feedback to specific product areas or functional modules using the Composio Toolset.
- **Airtable Sync Integration**
    - Seamlessly reads from and writes back to Airtable, ensuring your feedback database remains current and actionable.
- **Priority Ranking**
    - Dynamically assigns urgency levels based on keyword analysis and sentiment intensity to highlight critical issues.
- **Real-time Alerting**
    - Triggers notifications for urgent negative feedback, allowing teams to respond to critical issues before they escalate.

---

## Use Cases
**Product Development Prioritization**
- Automatically group feedback by feature area to inform the next sprint cycle.
- Identify the top three most requested improvements based on recurring user feedback patterns.

**Customer Experience Monitoring**
- Track sentiment trends over time to measure the impact of recent product updates.
- Flag negative feedback from high-value accounts for immediate follow-up by the success team.

**Support Triage Efficiency**
- Sort incoming feedback into "Bug," "Feature Request," or "General Inquiry" buckets automatically.
- Filter out noise and duplicate reports to focus support efforts on unique, actionable user issues.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Connect your Airtable account within the integration settings.
3. Map your specific feedback table and fields to the workflow input nodes.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw feedback string from your Airtable trigger.
- **Agent**: Analyzes the feedback, determines sentiment, and classifies the intent.
- **Composio Toolset**: Executes the update to your Airtable records with the new tags.
- **Chat Output**: Returns the summary and classification status to the user or dashboard.

### 3) Run the Flow
Use the Playground to test the flow with these prompts:
- `Analyze the latest feedback entry in the 'General' view and update the sentiment field.`
- `Categorize all feedback from the last 24 hours and flag any entries marked as 'Urgent'.`
- `Summarize the top 5 feature requests found in the 'Product Feedback' table.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary intelligence layer, responsible for parsing natural language and structuring data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment classification.
- Instruction: "You are a product feedback analyst. Extract the core intent, assign a sentiment score (-1 to 1), and categorize the feedback."
- Instruction: "Always prioritize identifying bug reports versus feature requests."

### 2) Composio Toolset Node
- Ensure your Airtable API key is active and has read/write permissions for the target workspace.
- Set the connection scope to include the specific base and tables containing your feedback data.

### 3) Tool Availability
- **Airtable Search**: Locate specific records by ID or timestamp.
- **Airtable Update**: Modify record fields (e.g., 'Sentiment', 'Category', 'Priority').
- **Text Analysis**: Perform semantic clustering on incoming strings.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Comprehensive support automation for high-volume ticket environments.
- [whats-app-feedback-collection-agent-by-wati](../whats-app-feedback-collection-agent-by-wati/README.md) - Collects user feedback directly through WhatsApp channels.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Tracks account health metrics to complement qualitative feedback data.
