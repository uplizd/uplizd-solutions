# Customer Feedback Analyzer (Uplizd) - Automate product insights from form submissions

## Summary
The Customer Feedback Analyzer by Formcarry is an intelligent Uplizd workflow that ingests raw user feedback, categorizes sentiment, and triggers automated follow-up actions. By connecting Formcarry submissions directly to your AI agent, this solution eliminates manual data entry, ensures no customer voice goes unheard, and accelerates your product development cycle through real-time insight extraction.

---

## Demo
![Customer Feedback Analyzer workflow showing Formcarry input, AI sentiment analysis, and automated CRM output](image.png)
**Alt text (SEO-ready):** Uplizd Customer Feedback Analyzer workflow for Formcarry, featuring automated sentiment analysis, AI-driven feedback categorization, and CRM integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9f6d674a-5d0b-527d-b7e6-bbf0b6ab3717)

---

## Category
*   **Primary category:** Customer Support
*   **Secondary tags:** formcarry, feedback, sentiment analysis, customer insights, automation, composio, ai workflow, product management
*   This solution bridges the gap between raw customer input and actionable product strategy by leveraging AI to process feedback at scale.

---

## Who is this for?
This workflow is designed for teams that need to turn high volumes of qualitative user feedback into structured data and immediate action.

*   **Product Managers**
    *   Identify recurring feature requests and pain points across thousands of form submissions without manual tagging.
*   **Customer Success Leads**
    *   Automatically flag urgent or negative feedback for immediate human intervention and personalized follow-up.
*   **Support Operations Managers**
    *   Standardize the triage process by routing feedback to the correct internal teams based on sentiment and topic.
*   **Growth Marketers**
    *   Extract positive testimonials and user success stories directly from feedback forms for use in marketing collateral.

---

## Features
- **Automated Sentiment Analysis**
  Real-time evaluation of incoming feedback to categorize tone and urgency using advanced LLM reasoning.
- **Formcarry Integration**
  Seamless ingestion of form data via the Composio Toolset to ensure secure and reliable data transmission.
- **Intelligent Categorization**
  Automatic tagging of submissions into predefined buckets like "Bug Report," "Feature Request," or "General Praise."
- **Actionable Routing**
  Dynamic triggering of downstream workflows, such as creating Jira tickets or Slack notifications based on feedback content.
- **Real-time Response Generation**
  Drafting of personalized, empathetic replies that can be reviewed or sent automatically to close the feedback loop.

---

## Use Cases
**Product Development**
*   Aggregating feature requests from feedback forms to prioritize the product roadmap.
*   Identifying "quick win" bug reports that are causing high friction for users.

**Customer Experience**
*   Escalating negative feedback to the support team within minutes of form submission.
*   Sending automated "Thank You" emails to users who provide detailed, constructive feedback.

**Data Hygiene**
*   Cleaning and normalizing feedback data before pushing it into a centralized CRM or data warehouse.
*   Removing duplicate or spam submissions to maintain a high-quality feedback repository.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Formcarry and target integration accounts (e.g., Slack, Jira, or CRM).
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw payload from your Formcarry webhook.
*   **Agent**: Processes the feedback text, performs sentiment analysis, and determines the appropriate action.
*   **Composio Toolset**: Executes the necessary API calls to update your external tools.
*   **Chat Output**: Returns a summary of the action taken and the status of the feedback processing.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Analyze the sentiment of this feedback: "I love the new dashboard, but the export button is hard to find."`
* `Categorize this submission: "The integration with my CRM keeps failing every time I try to sync data."`
* `Draft a polite response to a user who reported a bug in the mobile app.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your feedback pipeline.
*   **Instruction Pattern:**
    *   "Act as a Customer Insights Analyst; prioritize identifying actionable product feedback."
    *   "Maintain a professional and empathetic tone when drafting responses to users."
    *   "Always categorize feedback into 'Bug', 'Feature', or 'General' before taking action."

### 2) Composio Toolset Node
*   **API Key:** Ensure your Composio API key is active and authorized for the Formcarry and target CRM/Support platforms.
*   **Connection Scope:** Grant the agent read access to your form submissions and write access to your ticketing or communication tools.

### 3) Tool Availability
*   **Formcarry API:** For retrieving and managing form submission data.
*   **CRM/Ticketing APIs:** For creating records or updating existing customer profiles.
*   **Communication APIs:** For sending automated notifications or email drafts.

---

## Related Solutions
* [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) — Automate real-time customer support interactions.
* [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) — Triage support tickets via WhatsApp.
* [account-intelligence-reporter-by-leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate account-level insights and reporting.
