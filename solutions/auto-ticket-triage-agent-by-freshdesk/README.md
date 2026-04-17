# Auto Ticket Triage Agent (Uplizd) - Intelligent support ticket categorization and priority routing

## Summary
The Auto Ticket Triage Agent is an automated Uplizd workflow that leverages AI to ingest, categorize, and prioritize incoming support tickets from Freshdesk. By instantly analyzing ticket sentiment, urgency, and topic, this solution ensures that high-priority issues reach the right support engineers immediately, reducing response times and maintaining consistent service hygiene across your support operations.

---

## Demo
![Auto Ticket Triage Agent workflow diagram showing Freshdesk ticket ingestion, AI-driven classification, and automated priority routing](image.png)
**Alt text (SEO-ready):** Auto Ticket Triage Agent workflow for Freshdesk, featuring AI-powered ticket categorization, priority routing, and automated support ticket management on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/auto-ticket-triage-agent-by-freshdesk)

---

## Category
**Primary category:** Customer Support Automation  
**Secondary tags:** freshdesk, ticketing, ai workflow, support operations, ticket triage, automation, composio, customer experience  
This solution streamlines helpdesk management by automating the classification of incoming requests, ensuring support teams focus on high-impact issues.

---

## Who is this for?
This workflow is designed for support organizations looking to eliminate manual ticket sorting and improve response SLAs.

* **Support Manager**
    * Ensures consistent ticket routing and prevents high-priority issues from stalling in the queue.
* **Customer Success Lead**
    * Monitors sentiment and urgency trends to proactively address potential churn risks.
* **Support Engineer**
    * Receives pre-categorized tickets with clear context, allowing for faster resolution times.
* **Operations Analyst**
    * Gains visibility into ticket volume patterns and category distribution for better resource planning.

---

## Features
- **Intelligent Ticket Classification**
  Uses AI to analyze ticket content and automatically assign relevant tags or categories based on your business logic.
- **Automated Priority Routing**
  Instantly identifies urgent requests and updates ticket priority levels in Freshdesk to ensure immediate visibility.
- **Sentiment-Aware Triage**
  Detects frustrated or high-emotion language to escalate sensitive tickets to senior support staff automatically.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely interface with Freshdesk APIs for real-time ticket updates and data retrieval.
- **Customizable Workflow Logic**
  Easily adjust the Agent's instructions to handle specific product lines, technical tiers, or regional support requirements.

---

## Use Cases
**Support Queue Optimization**
* Automatically move "Billing" or "Security" tagged tickets to the top of the queue.
* Route technical bugs directly to the engineering support team based on keyword analysis.

**Customer Experience Enhancement**
* Flag tickets with negative sentiment for immediate review by a Customer Success Manager.
* Send automated, personalized acknowledgement responses based on the ticket's identified topic.

**Operational Reporting**
* Aggregate ticket data by category to identify recurring product issues or documentation gaps.
* Maintain clean ticket metadata by enforcing consistent categorization across all incoming requests.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Connect your Freshdesk account via the Composio Toolset node.
3. Configure your desired LLM model in the Agent node.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives raw ticket data (subject, description, requester info) from Freshdesk webhooks.
* **Agent**: Analyzes the input, determines the category, and decides the appropriate priority level.
* **Composio Toolset**: Executes the API calls to update the ticket fields within Freshdesk.
* **Chat Output**: Confirms the triage action taken and logs the result for audit purposes.

### 3) Run the Flow
Test your agent in the Playground using these prompts:
* `Triage this ticket: "I cannot access my account after the latest update, it says 403 error."`
* `Analyze this ticket for urgency: "This is the third time this week my report failed to export, I am very frustrated."`
* `Categorize and prioritize this request: "How do I change my billing cycle to annual?"`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent engine for ticket analysis.
* Set the system prompt to define your specific support categories.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Ensure the instruction includes a clear output format for the Composio Toolset to parse.

### 2) Composio Toolset Node
* Provide your Freshdesk API key and domain URL within the Composio connection settings.
* Scope the connection to allow `read` and `update` permissions for tickets.

### 3) Tool Availability
* `freshdesk_get_ticket`: Retrieve full ticket details for deep analysis.
* `freshdesk_update_ticket`: Apply priority, tags, and status changes.
* `freshdesk_add_note`: Append internal triage notes to the ticket history.

---

## Related Solutions
* [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - General purpose AI support automation.
* [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Similar triage logic applied to WhatsApp channels.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Workflow for managing and prioritizing operational tasks.
