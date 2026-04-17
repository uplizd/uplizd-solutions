# Instagram Lead Nurturing Bot (Uplizd) - Automated DM engagement for social sales

## Summary
The Instagram Lead Nurturing Bot is an intelligent AI workflow designed to automate direct message interactions, turning passive followers into qualified leads. By leveraging the Composio Toolset to interface with Instagram, this solution ensures timely follow-ups, personalized engagement, and efficient lead capture, significantly reducing manual response time and increasing conversion velocity for social-first marketing teams.

---

## Demo
![Instagram Lead Nurturing Bot workflow showing automated DM response logic and lead qualification steps](image.png)
**Alt text (SEO-ready):** Instagram Lead Nurturing Bot workflow automation on Uplizd, featuring automated DM responses, lead qualification, and social media integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMJFR0W+7/35QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK04AAAAiSURBVEjHY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwChgBAAAGAAH5314AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/fe7ed977-dd1c-56b1-bd40-00d81e87dcb7)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** instagram, social media, lead nurturing, automation, dm automation, lead qualification, sales, composio

This solution bridges the gap between social engagement and CRM pipeline management by automating the initial lead qualification process.

---

## Who is this for?
This workflow is designed for teams looking to scale their social media outreach without sacrificing the personal touch required for high-conversion sales.

* **Social Media Manager**
    * Automates routine DM responses to maintain high engagement rates 24/7.
* **Sales Development Representative (SDR)**
    * Receives pre-qualified leads directly from Instagram, reducing manual prospecting time.
* **Growth Marketer**
    * Improves conversion velocity by ensuring no lead inquiry goes unanswered.
* **Small Business Owner**
    * Manages customer inquiries and lead capture efficiently without needing a dedicated support team.

---

## Features
- **Automated DM Routing**
    Real-time detection and categorization of incoming Instagram messages based on intent.
- **Intelligent Lead Qualification**
    Uses AI to ask discovery questions and score leads before passing them to the sales team.
- **Seamless CRM Integration**
    Automatically syncs captured lead data and conversation summaries to your preferred CRM via Composio.
- **Personalized Response Engine**
    Generates human-like, context-aware replies that reflect your brand voice and tone.
- **Real-time Notification Alerts**
    Triggers instant alerts for high-intent leads, ensuring immediate follow-up by human agents.

---

## Use Cases
**Lead Qualification**
* Identifying high-intent prospects based on specific keywords in their initial DM.
* Filtering out general support queries from potential sales opportunities.

**Sales Pipeline Acceleration**
* Automatically scheduling discovery calls for leads that meet specific qualification criteria.
* Updating CRM deal stages based on the sentiment and progress of the Instagram conversation.

**Customer Engagement**
* Providing instant answers to frequently asked questions about pricing or product availability.
* Nurturing leads with personalized content recommendations based on their stated interests.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project to initialize the workflow.
3. Authenticate your Instagram and CRM accounts within the Composio connection manager.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the raw DM text and sender metadata from Instagram.
* **Agent**: Processes the message, determines intent, and formulates a response or qualification question.
* **Composio Toolset**: Executes actions like `send_dm`, `update_crm_lead`, or `log_interaction`.
* **Chat Output**: Delivers the final response back to the user via the Instagram API.

### 3) Run the Flow
Use the Playground to test your bot with these example prompts:
* `Check if the user is asking about pricing and provide the standard product brochure link.`
* `Analyze the message sentiment and flag it for human review if the user expresses frustration.`
* `Extract the user's email address from the conversation and update the lead record in Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, managing the conversation flow and decision-making.
* Instruct the agent to prioritize professional, brand-aligned communication.
* Define clear qualification criteria (e.g., "Ask for company size if the user mentions a demo").
* Set the agent to summarize the conversation before triggering any CRM update actions.

### 2) Composio Toolset Node
Connect your Instagram Business account and your CRM (e.g., HubSpot or Salesforce) to the Composio Toolset. Ensure the scope includes `instagram_messaging_write` and `crm_write_access` to allow the agent to perform its duties.

### 3) Tool Availability
* `instagram_send_message`: For delivering automated replies.
* `crm_create_lead`: For capturing new prospects in your database.
* `crm_update_deal`: For moving leads through your sales pipeline.
* `sentiment_analysis_tool`: For gauging lead temperature and urgency.

---

## Related Solutions
* [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automate lead qualification and nurturing via WhatsApp.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms for unified reporting.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages to optimize sales velocity.
