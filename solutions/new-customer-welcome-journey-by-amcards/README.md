# New Customer Welcome Journey (Uplizd) - Automated personalized onboarding sequences

## Summary
The New Customer Welcome Journey (Uplizd) automates the delivery of personalized welcome cards and onboarding communications to new clients. By integrating CRM data with the Amcards platform, this AI workflow ensures every new customer receives a high-touch, memorable first impression, increasing brand loyalty and reducing churn through timely, automated engagement.

---

## Demo
![New Customer Welcome Journey workflow in the Uplizd builder showing CRM trigger, AI personalization agent, and Amcards delivery node](image.png)
**Alt text (SEO-ready):** New Customer Welcome Journey workflow in Uplizd showing automated CRM to Amcards integration for personalized customer onboarding.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9db1525e-872e-5d8f-a8e4-01744a088c51)

---

## Category
**Primary category:** Customer Success
**Secondary tags:** onboarding, crm, amcards, automation, customer experience, engagement, workflow, ai agent.
This solution bridges the gap between CRM lead status updates and physical or digital greeting card delivery to automate high-value customer touchpoints.

---

## Who is this for?
This solution is designed for teams looking to scale personalized customer appreciation without manual overhead.

* **Customer Success Manager**
    * Automates the "first touch" process to ensure no new client goes unacknowledged.
* **Marketing Operations Lead**
    * Streamlines multi-channel onboarding sequences by triggering physical mailers directly from CRM events.
* **Small Business Owner**
    * Provides enterprise-grade personalized customer experiences with minimal administrative effort.
* **Sales Operations Specialist**
    * Ensures consistent brand messaging and follow-up cadence across the entire customer lifecycle.

---

## Features
- **Automated Triggering**
  Seamlessly initiates the welcome sequence the moment a new customer is marked as 'Closed-Won' in your CRM.
- **Personalized Messaging**
  Uses the Agent node to draft warm, brand-aligned welcome notes based on customer profile data.
- **Amcards Integration**
  Leverages the Composio Toolset to trigger physical or digital card delivery through the Amcards platform.
- **Real-time Sync**
  Maintains data integrity between your CRM and the onboarding pipeline, ensuring accurate recipient details.
- **Customizable Cadence**
  Allows for flexible scheduling of welcome cards to align with your specific customer onboarding timeline.

---

## Use Cases
**Automated Onboarding**
* Sending a personalized "Welcome to the Family" card immediately after the first purchase.
* Triggering a follow-up card 7 days after onboarding to check on initial product satisfaction.

**Customer Appreciation**
* Automating birthday or anniversary cards for long-term clients to boost retention.
* Sending milestone achievement cards when a customer reaches a specific usage threshold.

**Brand Loyalty Programs**
* Dispatching exclusive "VIP" welcome kits to high-value accounts identified in the CRM.
* Automating referral thank-you cards to customers who provide high-quality feedback.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your CRM account and Amcards API credentials within the integration settings.
3. Map your CRM 'Customer' fields to the workflow input variables.
4. Ensure nodes are correctly linked from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives the new customer data trigger from your CRM.
* **Agent**: Processes the customer profile to generate a warm, personalized welcome message.
* **Composio Toolset**: Executes the Amcards API call to dispatch the physical or digital card.
* **Chat Output**: Confirms the successful dispatch of the welcome sequence to the user.

### 3) Run the Flow
Test the workflow in the Playground using these prompts:
* `Send a standard welcome card to the new customer identified in the latest CRM entry.`
* `Draft and send a personalized onboarding card for the client with ID 5501.`
* `Trigger a welcome sequence for all new customers added in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative copywriter for your welcome communications.
* Use a professional yet warm tone consistent with your brand voice.
* Instruct the agent to pull specific data points like 'Customer Name' and 'Company Name' for personalization.
* Ensure the agent confirms the card type and recipient address before finalizing the tool call.

### 2) Composio Toolset Node
* Provide your Amcards API key in the configuration panel.
* Set the connection scope to allow the agent to read customer data and write/trigger card delivery.

### 3) Tool Availability
* **CRM Connector**: For fetching customer contact details and status.
* **Amcards API**: For template selection, personalization, and dispatching cards.
* **Data Formatter**: For cleaning and preparing addresses for postal delivery.

---

## Related Solutions
* [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automates the technical and administrative setup of new accounts.
* [Admin User Onboarding Assistant by Storeganise](../admin-user-onboarding-assistant-by-storeganise/README.md) - Guides new administrative users through their initial platform configuration.
* [WhatsApp Lead Nurturing Agent by Spoki](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Engages new leads via messaging to accelerate the conversion process.
