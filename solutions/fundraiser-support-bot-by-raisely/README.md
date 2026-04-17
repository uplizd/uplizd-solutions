# Fundraiser Support Bot (Uplizd) - Automated donor and campaign management assistant

## Summary
The Fundraiser Support Bot by Raisely is an intelligent automation workflow designed to streamline donor inquiries, campaign updates, and team captain guidance. By integrating directly with your fundraising platform, this solution ensures that supporters receive real-time, accurate information, reducing administrative overhead and increasing campaign velocity through automated, context-aware communication.

---

## Demo
![Fundraiser Support Bot workflow interface showing automated donor inquiry handling and Raisely integration](image.png)
**Alt text (SEO-ready):** Fundraiser Support Bot (Uplizd) workflow for Raisely, automating donor inquiries, team captain support, and campaign data management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c0ce3c6a-e0ff-5cc1-8624-6eb2cb83d204)

---

## Category
**Primary category:** Support automation
**Secondary tags:** fundraising, raisely, donor management, non-profit, ai workflow, customer support, automation, composio
This solution bridges the gap between donor engagement platforms and automated support, ensuring non-profits maintain high-touch communication at scale.

---

## Who is this for?
This solution is designed for non-profit organizations and fundraising teams looking to optimize their supporter experience.

* **Fundraising Manager**
    * Automates routine donor FAQ responses to focus on high-value donor relationships.
* **Team Captain**
    * Receives instant guidance on campaign setup and progress tracking without waiting for manual support.
* **Non-profit Administrator**
    * Ensures consistent, brand-aligned messaging across all donor touchpoints and campaign updates.
* **Donor Relations Specialist**
    * Gains real-time visibility into supporter inquiries, allowing for proactive outreach and engagement.

---

## Features
- **Automated Donor FAQ**
    Real-time resolution of common donor questions regarding tax receipts, donation status, and campaign goals.
- **Team Captain Guidance**
    Intelligent onboarding support for new team captains, providing step-by-step instructions for campaign optimization.
- **Raisely Integration**
    Deep connectivity via the Composio Toolset to fetch live campaign data and update donor records instantly.
- **Context-Aware Responses**
    The Agent analyzes user intent to provide personalized support based on the specific campaign or donor history.
- **Multi-Channel Support**
    Standardized response logic that can be deployed across web widgets, email, or messaging platforms.

---

## Use Cases
**Donor Inquiry Management**
* Providing instant status updates on recurring donation schedules.
* Generating and sending tax-deductible receipt information upon request.

**Campaign Performance Support**
* Assisting team captains with real-time feedback on their fundraising page conversion rates.
* Automating milestone celebrations when a campaign reaches a new funding tier.

**Administrative Efficiency**
* Syncing donor contact information updates directly into the Raisely backend.
* Triaging complex support tickets to human staff only when the AI requires escalation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Fundraiser Support Bot template from the solution gallery.
3. Connect your Raisely API credentials within the integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives the donor or team captain's query.
* **Agent:** Processes the intent and determines the necessary action or information.
* **Composio Toolset:** Executes the specific Raisely API call to fetch or update data.
* **Chat Output:** Delivers the final, human-readable response to the user.

### 3) Run the Flow
Use the Playground to test your bot with these example prompts:
* `How do I update my team captain profile on my current fundraising page?`
* `Can you tell me the total amount raised by the 'Summer Gala' campaign so far?`
* `I need a copy of my donation receipt for the recent contribution to the local shelter project.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary interface for all fundraising inquiries.
* Use a system prompt that emphasizes empathy and clarity.
* Configure the temperature to 0.3 for factual, consistent responses.
* Enable tool-calling capabilities to allow the agent to query live Raisely data.

### 2) Composio Toolset Node
The Composio Toolset manages the authentication and execution of Raisely API requests. Ensure your API key is scoped to allow read/write access to campaign and donor objects.

### 3) Tool Availability
* **Campaign Fetcher:** Retrieve live stats, goal progress, and end dates.
* **Donor Record Manager:** Access and update contact details and donation history.
* **Support Triage:** Route specialized queries to internal ticketing systems.

---

## Related Solutions
* [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - General purpose support automation for broader customer inquiries.
* [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Managing support tickets via WhatsApp for mobile-first donor engagement.
* [account-relationship-builder-by-dynamics365](../account-relationship-builder-by-dynamics365/README.md) - Advanced CRM relationship management for high-value donor pipelines.
