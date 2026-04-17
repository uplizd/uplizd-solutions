# Customer Win-Back Direct Mail Agent (Uplizd) - Automated personalized re-engagement campaigns

## Summary
The Customer Win-Back Direct Mail Agent is an intelligent workflow designed to automate the re-engagement of churned customers by triggering personalized physical mailers via Stannp. By identifying lapsed accounts and syncing data through the Composio Toolset, this solution helps businesses bridge the digital-to-physical gap, increasing win-back rates and improving customer retention through high-impact, tangible outreach.

---

## Demo
![Customer Win-Back Direct Mail Agent workflow diagram showing CRM data triggering Stannp postcard generation](image.png)
**Alt text (SEO-ready):** Uplizd Customer Win-Back Direct Mail Agent workflow, Stannp integration for automated physical marketing, churn reduction and customer re-engagement automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/eba20d4c-c276-5ae2-bc54-59aa11a8df24)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** stannp, direct mail, customer retention, churn reduction, marketing automation, composio, ai workflow, physical marketing
- This solution integrates digital CRM intelligence with physical mail delivery to create a seamless, automated re-engagement pipeline for lapsed customers.

---

## Who is this for?
This solution is designed for growth-focused teams looking to leverage physical touchpoints to reclaim lost revenue.

- **Retention Manager**
    - Automates the outreach process to churned segments without manual intervention.
- **Marketing Operations Specialist**
    - Syncs CRM churn data directly with physical mail providers for consistent brand messaging.
- **Customer Success Lead**
    - Identifies high-value lapsed accounts that warrant a personalized physical "win-back" gesture.
- **Growth Marketer**
    - Measures the ROI of offline marketing channels by tracking mailer conversion against digital win-back signals.

---

## Features
- **Automated Triggering**
    - Automatically initiates a mailer request the moment a customer status changes to 'Churned' or 'Inactive' in your CRM.
- **Personalized Content Generation**
    - Uses the Agent node to draft custom, empathetic messages for postcards based on the customer's historical purchase data.
- **Stannp Integration**
    - Leverages the Composio Toolset to securely transmit address and creative data to the Stannp API for printing and mailing.
- **Real-time Sync**
    - Ensures that address data is verified and synced in real-time, preventing wasted postage on invalid locations.
- **Campaign Analytics**
    - Tracks the status of sent mailers within the workflow to provide visibility into the win-back pipeline.

---

## Use Cases
**Churned Customer Re-engagement**
- Trigger a "We Miss You" postcard with a unique discount code when a subscription is cancelled.
- Send a physical product catalog to customers who haven't logged in for over 90 days.

**High-Value Account Recovery**
- Flag enterprise accounts that have gone dark and trigger a high-touch, personalized physical letter from an account executive.
- Send a physical gift or incentive to lapsed VIP customers to encourage a renewal conversation.

**Marketing Campaign Expansion**
- Integrate physical mailers into existing digital win-back email sequences for a multi-channel approach.
- Automate the mailing of physical event invitations to lapsed users in specific geographic regions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Connect your CRM and Stannp accounts within the integration settings.
3. Map your CRM 'Churned' status field to the workflow trigger.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the customer churn event data.
- **Agent**: Processes the customer profile and drafts the personalized mailer content.
- **Composio Toolset**: Executes the API call to Stannp to generate the physical mailer.
- **Chat Output**: Confirms the successful dispatch and logs the activity back to the CRM.

### 3) Run the Flow
Use the Playground to test your triggers with these example prompts:
- `Trigger a win-back postcard for customer ID 8842 with a 20% discount offer.`
- `Check for all customers who churned in the last 30 days and prepare a Stannp mailer for them.`
- `Draft a personalized re-engagement message for a lapsed enterprise client and send it via Stannp.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative copywriter and logic engine for your mailers.
- Use a model capable of high-context reasoning (e.g., GPT-4o).
- Instruction: "You are a retention expert. Draft empathetic, concise, and persuasive postcard copy based on the provided customer history."
- Instruction: "Ensure the tone matches our brand voice while highlighting the specific value proposition of our win-back offer."

### 2) Composio Toolset Node
- Provide your Stannp API key to authorize the connection.
- Set the connection scope to allow 'Write' access for mailer creation and 'Read' access for status tracking.

### 3) Tool Availability
- **Stannp API**: For postcard creation, address validation, and mailing status updates.
- **CRM Connector**: For fetching customer contact details and updating churn status logs.
- **Data Formatter**: For cleaning and normalizing address strings before sending to the printer.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automates follow-ups for incomplete purchases.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriches CRM data for better targeting.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Multi-channel engagement for active leads.
