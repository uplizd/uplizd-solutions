# Survey Response Orchestrator (Uplizd) - Automated multi-channel customer feedback follow-up

## Summary
The Survey Response Orchestrator by Simplesat is an intelligent Uplizd AI workflow designed to automate post-survey actions, ensuring no customer feedback goes unaddressed. By integrating directly with your survey platforms and CRM, this solution triggers personalized follow-up sequences based on satisfaction scores, boosting response rates, improving customer sentiment, and streamlining the feedback-to-action pipeline for support and success teams.

---

## Demo
![Survey Response Orchestrator workflow showing automated feedback analysis and multi-channel follow-up routing](image.png)
**Alt text (SEO-ready):** Survey Response Orchestrator workflow for automated customer feedback analysis, sentiment-based routing, and multi-channel follow-up using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fadc4521-ebc4-5c4f-a73c-abc9ce5acf5b)

---

## Category
- **Primary category:** Customer Experience Operations
- **Secondary tags:** customer satisfaction, feedback loop, nps, csat, workflow automation, composio, support operations, sentiment analysis
- This solution bridges the gap between raw survey data and actionable customer success outcomes by automating the response lifecycle.

---

## Who is this for?
This solution is designed for teams looking to close the loop on customer feedback with speed and precision.

- **Customer Success Managers**
    - Proactively address negative feedback to prevent churn and improve account health.
- **Support Operations Leads**
    - Automate ticket creation and routing based on survey scores to ensure timely resolution.
- **Product Managers**
    - Aggregate qualitative feedback trends to prioritize feature requests and product improvements.
- **Marketing Specialists**
    - Identify satisfied customers to trigger automated requests for testimonials or case studies.

---

## Features
- **Sentiment-Based Routing**
    - Automatically categorizes survey responses by sentiment and score, routing critical issues to the appropriate team.
- **Multi-Channel Integration**
    - Leverages the Composio Toolset to push updates directly into CRMs, Slack, or email platforms.
- **Automated Follow-up Sequences**
    - Triggers personalized responses or internal alerts based on specific survey score thresholds.
- **Real-Time Data Sync**
    - Ensures survey data is instantly reflected in your source of truth, maintaining data hygiene across platforms.
- **Customizable Logic Nodes**
    - Easily adjust the workflow to handle different survey types, such as NPS, CSAT, or custom product feedback.

---

## Use Cases
**Churn Prevention**
- Automatically create a high-priority support ticket when a customer submits a low CSAT score.
- Notify the assigned Account Manager via Slack immediately when a "detractor" is identified in an NPS survey.

**Advocacy & Growth**
- Trigger an automated email sequence to "promoters" inviting them to leave a public review or join a beta program.
- Sync positive feedback snippets directly into a marketing repository for use in future case studies.

**Operational Efficiency**
- Batch process daily survey results to generate a summary report for the weekly product team meeting.
- Update customer profiles in your CRM with the latest feedback tags to keep account intelligence current.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your required survey and CRM integrations via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific API credentials and trigger events.

### 2) Setup the Nodes
* **Chat Input**: Receives raw survey payload from your feedback platform.
* **Agent**: Analyzes sentiment, evaluates score thresholds, and determines the appropriate follow-up action.
* **Composio Toolset**: Executes the necessary API calls to update CRM records or send notifications.
* **Chat Output**: Confirms the successful routing and logging of the survey response.

### 3) Run the Flow
* `Analyze the latest NPS survey results and flag all detractors for immediate follow-up.`
* `Send a personalized thank-you email to all customers who provided a 5-star CSAT score.`
* `Update the CRM record for account ID 12345 with the latest feedback summary and sentiment tag.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the brain of the operation, interpreting feedback and deciding the next best action.
* Use a model capable of nuanced sentiment analysis (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Analyze the input survey response, determine the sentiment, and map it to the predefined action category."
* Instruction: "If the score is below 3, escalate to the support queue; if above 4, tag for marketing advocacy."

### 2) Composio Toolset Node
* Provide your API keys for the survey platform (e.g., Simplesat) and your CRM (e.g., Salesforce or HubSpot).
* Ensure the connection scope includes read access for surveys and write access for CRM/Messaging platforms.

### 3) Tool Availability
* **Survey API**: Fetching response data and metadata.
* **CRM Connector**: Updating account fields and creating activity logs.
* **Communication Tools**: Sending Slack alerts or automated email responses.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - General purpose support automation.
- [crm-data-sync-agent](../crm-data-sync-agent/README.md) - Synchronizing customer data across platforms.
- [whats-app-feedback-collection-agent-by-whatsapp](../whats-app-feedback-collection-agent-by-whatsapp/README.md) - Alternative feedback collection via WhatsApp.
