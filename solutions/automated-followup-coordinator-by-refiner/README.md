# Automated Follow-up Coordinator (Uplizd) - Intelligent CRM response orchestration

## Summary
The Automated Follow-up Coordinator is an Uplizd AI workflow designed to streamline post-interaction engagement by automatically triggering personalized follow-up actions based on survey responses and customer feedback. By integrating directly with your CRM and communication platforms, this solution ensures no lead goes cold, maintaining high pipeline velocity and improving customer satisfaction through timely, data-driven outreach.

---

## Demo
![Automated Follow-up Coordinator workflow diagram showing survey input, agent processing, and CRM action execution](image.png)
**Alt text (SEO-ready):** Automated Follow-up Coordinator Uplizd workflow for CRM data synchronization, lead nurturing, and automated customer follow-up actions.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cf56f7c2-3938-5e45-90d6-d193438757d6)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, follow-up, lead nurturing, survey automation, pipeline, data sync, composio, ai workflow
- This solution bridges the gap between customer feedback and actionable sales tasks to ensure consistent engagement.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual follow-up bottlenecks.

- **Sales Development Representative (SDR)**
    - Automates the scheduling of follow-up tasks based on survey sentiment, allowing focus on high-intent conversations.
- **Customer Success Manager (CSM)**
    - Ensures immediate outreach to dissatisfied customers by triggering alerts when negative survey feedback is detected.
- **RevOps Manager**
    - Maintains clean, actionable pipeline data by ensuring every customer interaction is logged and followed up with consistently.
- **Marketing Operations Specialist**
    - Orchestrates multi-channel follow-up sequences that react to real-time customer feedback data.

---

## Features
- **Intelligent Sentiment Analysis**
    - Uses advanced LLM processing to categorize survey responses and determine the appropriate urgency for follow-up.
- **CRM Integration**
    - Automatically updates lead statuses and creates follow-up tasks in your CRM platform via the Composio Toolset.
- **Dynamic Task Routing**
    - Routes follow-up actions to the correct team member based on account ownership and response priority.
- **Real-time Notification Triggers**
    - Sends instant alerts to Slack or email when high-priority feedback requires immediate human intervention.
- **Automated Personalization**
    - Drafts context-aware follow-up messages that reference specific survey feedback, increasing response rates.

---

## Use Cases
**Lead Qualification & Nurturing**
- Automatically create a "Hot Lead" task in the CRM when a survey indicates high purchase intent.
- Trigger a personalized nurturing email sequence for leads who express interest but require more information.

**Customer Retention & Support**
- Create an urgent support ticket when a customer provides a low satisfaction score in a post-purchase survey.
- Schedule a check-in call for accounts that report neutral sentiment to proactively address potential churn.

**Pipeline Hygiene**
- Update lead stages automatically based on survey-driven engagement signals to keep the sales pipeline accurate.
- Archive or re-assign leads who indicate they are not currently in the market, keeping the active list focused.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow configuration.
3. Connect your required CRM and communication tool accounts via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific API credentials and environment variables.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw survey response data and customer metadata.
*   **Agent**: Analyzes the input, determines sentiment, and selects the appropriate follow-up action.
*   **Composio Toolset**: Executes CRM updates, task creation, or email dispatch based on Agent instructions.
*   **Chat Output**: Confirms the action taken and logs the result for the user.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Process survey response from ID 9821: "The product is great, but I need help with integration."`
- `Analyze feedback: "Not interested right now, maybe next quarter." - Update CRM status to Nurture.`
- `Urgent follow-up needed for account 445: "I am experiencing critical downtime."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision engine for your follow-up strategy.
- **Instruction Pattern**:
    - "Analyze the provided survey response for sentiment and intent."
    - "Map the intent to the predefined CRM action categories."
    - "Draft a professional follow-up response if required by the workflow logic."

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and authorized for your CRM (e.g., Salesforce, HubSpot).
- **Connection Scope**: Grant read/write permissions for Tasks, Leads, and Contacts to allow the agent to perform updates.

### 3) Tool Availability
- **CRM Connector**: For creating tasks and updating lead fields.
- **Communication Connector**: For sending automated emails or Slack notifications.
- **Data Parser**: For extracting structured information from unstructured survey text.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into prospect accounts.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and optimize your sales pipeline stages.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms seamlessly.
