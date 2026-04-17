# Lead Qualification Engine (Uplizd) - Automated lead scoring and prioritization for chatbot interactions

## Summary
The Lead Qualification Engine is an intelligent Uplizd workflow that processes incoming chatbot interactions to instantly score, categorize, and prioritize leads. By leveraging AI to analyze user intent and data in real-time, this solution eliminates manual triage, ensures high-value prospects are routed to sales teams immediately, and maintains a clean, actionable pipeline.

---

## Demo
![Lead Qualification Engine workflow diagram showing chatbot input, AI analysis, and CRM update](image.png)
**Alt text (SEO-ready):** Lead Qualification Engine workflow diagram showing chatbot input, AI analysis, and CRM update for Uplizd sales automation and lead scoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/db3612cf-c8e5-5570-b988-4f462b9dec25)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, lead qualification, landbot, sales pipeline, ai workflow, lead scoring, composio, data hygiene.
This solution bridges the gap between conversational marketing tools and CRM systems to ensure no qualified lead goes unnoticed.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their conversion funnels through automated intelligence.

*   **Sales Development Representative (SDR)**
    *   Focuses energy on high-intent leads that have been pre-qualified by the AI.
*   **Revenue Operations Manager**
    *   Maintains pipeline hygiene by ensuring consistent data entry and lead categorization.
*   **Marketing Manager**
    *   Measures the effectiveness of chatbot campaigns by tracking lead quality metrics.
*   **Sales Manager**
    *   Reduces lead response time by automating the initial qualification and routing process.

---

## Features
- **Real-time Lead Scoring**
    Automatically assigns a lead score based on user responses, intent, and company fit.
- **Automated CRM Sync**
    Seamlessly pushes qualified lead data directly into your CRM using the Composio Toolset.
- **Intelligent Intent Analysis**
    Uses advanced LLMs to interpret natural language inputs from Landbot conversations.
- **Dynamic Routing Logic**
    Routes leads to specific sales queues or account owners based on qualification criteria.
- **Pipeline Hygiene**
    Standardizes lead formatting and removes incomplete or low-quality entries before they hit your CRM.

---

## Use Cases
**Lead Prioritization**
*   Automatically flagging "Hot" leads for immediate follow-up by the sales team.
*   Filtering out non-business inquiries to keep the CRM free of noise.

**Sales Pipeline Management**
*   Updating lead status in the CRM based on the conversation stage reached in the chatbot.
*   Appending conversation summaries to lead records for context-rich sales outreach.

**Data Enrichment**
*   Extracting key contact details from chat transcripts to populate CRM fields.
*   Validating lead information against existing records to prevent duplicate entries.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Landbot account and your target CRM (e.g., Salesforce or HubSpot) via the Composio Toolset.
3. Configure the environment variables for your specific API keys and CRM field mappings.
4. Ensure nodes are correctly linked from Chat Input through the Agent to the final CRM output.

### 2) Setup the Nodes
*   **Chat Input**: Captures the raw conversation data and user responses from Landbot.
*   **Agent**: Analyzes the input, performs sentiment analysis, and calculates the lead score.
*   **Composio Toolset**: Executes the API calls to create or update records in your CRM.
*   **Chat Output**: Sends a confirmation message back to the user or notifies the internal team.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Qualify this lead: "I am looking for an enterprise solution for 500+ users and need a demo this week."`
* `Analyze this chat: "Just browsing, not interested in a demo yet."`
* `Score this interaction: "I'm the CTO at a fintech startup, we need to integrate this with our current stack."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the qualification process, transforming unstructured chat into structured data.
*   **Role**: Act as a professional Sales Qualification Assistant.
*   **Instruction**: Extract company size, intent, and contact info from the chat.
*   **Instruction**: Assign a score from 1-10 based on the lead's expressed urgency and authority.

### 2) Composio Toolset Node
*   **API Key**: Provide your Composio API key to enable secure integration with your CRM.
*   **Connection Scope**: Ensure the toolset has write access to your CRM's "Leads" or "Opportunities" objects.

### 3) Tool Availability
*   **CRM Create/Update**: Capability to push qualified data into Salesforce, HubSpot, or Pipedrive.
*   **Data Parser**: Ability to extract specific entities like email, phone, and company name.
*   **Notification Service**: Ability to trigger Slack or email alerts for high-priority leads.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates deep-dive research on prospects.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes lead data across multiple platforms.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages and tracks sales pipeline stages.
