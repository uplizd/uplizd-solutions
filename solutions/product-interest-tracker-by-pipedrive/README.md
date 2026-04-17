# Product Interest Tracker (Uplizd) - Automate cross-sell and upsell opportunity identification

## Summary
The Product Interest Tracker (Uplizd) is an intelligent workflow designed to monitor customer interactions and automatically identify high-intent cross-sell and upsell opportunities within Pipedrive. By analyzing communication patterns and product usage signals, this solution ensures your sales team never misses a revenue-generating conversation, providing a single source of truth for pipeline velocity and account expansion.

---

## Demo
![Product Interest Tracker workflow showing Pipedrive integration and AI analysis](image.png)
**Alt text (SEO-ready):** Product Interest Tracker (Uplizd) workflow for Pipedrive cross-sell and upsell automation using AI-driven lead signals.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/806e484f-6cfa-5ad9-8362-fa8f4272cca0)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, pipedrive, sales, upsell, cross-sell, pipeline, lead intelligence, composio, ai workflow
This solution bridges the gap between raw customer interaction data and actionable sales intelligence, enabling proactive revenue management.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to maximize customer lifetime value through data-driven outreach.

* **Account Executives**
    * Receive real-time alerts when a prospect expresses interest in additional product modules.
* **Sales Operations Managers**
    * Standardize the process of identifying and tagging expansion opportunities across the sales pipeline.
* **Customer Success Managers**
    * Proactively identify at-risk or growth-ready accounts based on recent communication sentiment.
* **Growth Marketers**
    * Leverage interaction data to refine messaging for targeted upsell campaigns.

---

## Features
- **Automated Signal Detection**
  Uses AI to scan Pipedrive notes and emails for specific keywords related to product interest and expansion intent.
- **Real-time CRM Sync**
  Automatically updates Pipedrive deal fields or creates new activities when a high-intent signal is detected.
- **Intelligent Scoring**
  Assigns a priority score to each identified opportunity, allowing sales reps to focus on the most promising leads first.
- **Context-Aware Summarization**
  Generates a concise summary of the interest signal, providing the sales rep with immediate context before they reach out.
- **Composio-Powered Integration**
  Seamlessly connects with Pipedrive via the Composio Toolset to ensure secure, authenticated data retrieval and updates.

---

## Use Cases
**Pipeline Expansion**
* Automatically flag existing deals where the prospect mentions a need for a higher-tier feature.
* Create follow-up tasks in Pipedrive for Account Executives when a trial user asks for pricing on additional seats.

**Account Health Monitoring**
* Identify "silent" interest by tracking inquiries about product documentation or help center articles.
* Trigger an internal notification to the account owner when a customer mentions a competitor's product in an email.

**Sales Velocity Optimization**
* Reduce manual data entry by automatically populating "Interest Area" fields in Pipedrive based on conversation analysis.
* Prioritize daily outreach lists based on the recency and strength of identified product interest signals.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your Pipedrive account within the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger event or manual query to initiate the analysis.
* **Agent**: Analyzes the input text and determines the appropriate Pipedrive action.
* **Composio Toolset**: Executes the API calls to read deal data and update CRM records.
* **Chat Output**: Returns the confirmation of the identified interest and the action taken in the CRM.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Analyze the latest emails for this deal and identify if the client is interested in our Enterprise plan.`
* `Check for any mentions of new product features in the recent Pipedrive notes for account ID 5501.`
* `Update the 'Upsell Potential' field for all deals where the client asked for a demo of the new API module.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a sales intelligence analyst that interprets unstructured communication data.
* Use a model with strong reasoning capabilities (e.g., GPT-4o).
* System instruction: "You are a sales intelligence assistant. Extract product interest signals from the provided text and map them to Pipedrive deal updates."
* Ensure the agent is instructed to be conservative with updates to maintain CRM data hygiene.

### 2) Composio Toolset Node
* Provide your Pipedrive API key within the Composio configuration.
* Set the connection scope to allow read/write access to Deals, Notes, and Activities.

### 3) Tool Availability
* `pipedrive_get_deal`: Retrieve current deal status and history.
* `pipedrive_update_deal`: Update custom fields related to interest signals.
* `pipedrive_create_activity`: Schedule follow-up tasks for the sales team.
* `pipedrive_list_notes`: Scan communication logs for intent signals.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate account data to identify high-value prospects.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-up cadences effectively.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensure multi-platform data consistency across your sales stack.
