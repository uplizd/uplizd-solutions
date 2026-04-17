# Form Response Analyzer (Uplizd) - Automated categorization and insight extraction for form submissions

## Summary
The Form Response Analyzer is an intelligent Uplizd workflow that processes incoming form submissions in real-time, categorizing feedback and extracting actionable insights. By leveraging AI to parse unstructured data, it enables teams to maintain high pipeline velocity, improve data hygiene, and ensure that critical customer requests are routed to the right stakeholders without manual intervention.

---

## Demo
![Form Response Analyzer workflow showing automated categorization of incoming form submissions](image.png)
**Alt text (SEO-ready):** Form Response Analyzer workflow for automated data categorization, Uplizd AI workflow, Formsite integration, and real-time CRM data processing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8b4475a4-2ca1-58a8-bff6-c1c81ad6ec0e)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** form automation, data hygiene, crm, lead qualification, feedback analysis, composio, ai workflow, data integration.
This solution streamlines the intake process by transforming raw form submissions into structured, categorized data ready for immediate business action.

---

## Who is this for?
This solution is designed for teams managing high volumes of inbound data who need to prioritize responses based on content quality and intent.

* **Marketing Manager**
    * Automates the segmentation of leads based on form intent to improve conversion rates.
* **Customer Support Lead**
    * Instantly identifies urgent support tickets from general inquiries to reduce response times.
* **Sales Operations Specialist**
    * Ensures CRM data hygiene by cleaning and standardizing form input before it reaches the sales pipeline.
* **Product Manager**
    * Aggregates user feedback and feature requests from forms to drive data-informed product roadmaps.

---

## Features
- **Intelligent Categorization**
  Uses AI to automatically tag submissions based on sentiment, urgency, and topic, ensuring relevant teams are notified.
- **Real-time Data Enrichment**
  Connects via the Composio Toolset to cross-reference form data with existing CRM profiles for deeper context.
- **Automated Routing Logic**
  Directs high-priority submissions to specific Slack channels or email aliases based on predefined business rules.
- **Standardized Data Formatting**
  Cleans and formats contact information and free-text fields to maintain a consistent source of truth in your database.
- **Seamless CRM Integration**
  Syncs processed form data directly into your CRM, reducing manual entry and preventing data silos.

---

## Use Cases
**Lead Qualification & Routing**
* Automatically score leads based on budget or timeline fields provided in the form.
* Route high-intent demo requests directly to the assigned account executive’s calendar.

**Customer Feedback & Sentiment**
* Extract common pain points from support forms to identify recurring product issues.
* Flag negative sentiment submissions for immediate escalation to the customer success team.

**Operational Data Hygiene**
* Standardize company names and job titles from form submissions to keep CRM records clean.
* Automatically append lead source metadata to submissions for better attribution tracking.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Form Response Analyzer template from the solution library.
3. Connect your Formsite account and target CRM via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the raw JSON payload from the form submission.
* **Agent**: Processes the text using LLM instructions to categorize and extract key entities.
* **Composio Toolset**: Executes API calls to update the CRM or notify internal teams.
* **Chat Output**: Confirms the successful processing and routing of the submission.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Categorize this submission: "I am interested in your enterprise plan and need a demo by Friday."`
* `Extract the user's company name and job title from this form response: "Hi, I'm Jane from Acme Corp, looking for support."`
* `Analyze the sentiment of this feedback: "The new dashboard is confusing and I can't find the export button."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine to interpret form intent.
* Use a model with strong reasoning capabilities (e.g., GPT-4o).
* Instruction: "Analyze the provided form submission, categorize it as 'Sales', 'Support', or 'Feedback', and extract key contact details."
* Ensure the agent is instructed to output JSON for seamless downstream integration.

### 2) Composio Toolset Node
* Provide your API key within the Composio configuration panel.
* Set the connection scope to include read/write access for your CRM and notification platforms.

### 3) Tool Availability
* **CRM Connector**: For updating lead records and contact fields.
* **Notification Tool**: For sending alerts to Slack or Email.
* **Data Parser**: For cleaning and normalizing raw string inputs.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on incoming leads.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your CRM records synchronized across multiple platforms.
* [WhatsApp Lead Qualifier](../whats-app-lead-qualifier-by2chat/README.md) - Qualify inbound leads directly through messaging channels.
