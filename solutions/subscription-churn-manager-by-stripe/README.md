# Subscription Churn Manager (Uplizd) - Automated retention and cancellation workflows

## Summary
The Subscription Churn Manager is an intelligent Uplizd workflow designed to proactively identify at-risk subscribers and automate retention strategies. By integrating real-time Stripe data with AI-driven decision-making, it helps businesses reduce churn rates, recover revenue, and maintain a single source of truth for customer lifecycle management.

---

## Demo
![Subscription Churn Manager workflow diagram showing Stripe data integration and AI retention logic](image.png)
**Alt text (SEO-ready):** Subscription Churn Manager workflow diagram showing Stripe data integration, AI-driven retention logic, and automated customer communication via Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/35085df2-7fc5-5501-a006-ac4690846d2a)

---

## Category
- **Primary category:** Revenue Operations
- **Secondary tags:** stripe, churn, retention, subscription management, customer lifecycle, ai workflow, composio, revenue recovery
- This solution bridges the gap between payment processing and customer success by automating churn mitigation strategies.

---

## Who is this for?
This solution is designed for teams focused on maximizing customer lifetime value and reducing revenue leakage.

- **Customer Success Manager**
    - Proactively identifies at-risk accounts before they finalize a cancellation.
- **Revenue Operations Lead**
    - Automates the reconciliation of subscription data across payment gateways and CRM systems.
- **Growth Marketer**
    - Deploys personalized retention offers based on individual subscriber usage patterns.
- **Finance Analyst**
    - Tracks real-time churn metrics and recovery success rates for monthly reporting.

---

## Features
- **Real-time Churn Detection**
    - Monitors Stripe webhook events to trigger immediate retention workflows when a cancellation is initiated.
- **AI-Powered Retention Offers**
    - Generates personalized discount or service extension offers based on customer history and subscription tier.
- **Automated Outreach**
    - Executes multi-channel communication sequences to engage users who have flagged their intent to cancel.
- **Stripe Integration**
    - Leverages the Composio Toolset to safely query and update subscription statuses directly within the Stripe ecosystem.
- **Performance Analytics**
    - Logs every retention attempt and outcome to provide actionable insights into why customers are leaving.

---

## Use Cases
**Proactive Retention**
- Automatically send a personalized "save" offer when a high-value customer initiates a cancellation.
- Trigger a survey to collect qualitative feedback the moment a subscription is paused.

**Revenue Recovery**
- Identify failed payment events and initiate an automated dunning sequence to recover lost revenue.
- Re-engage lapsed subscribers with targeted win-back campaigns based on their previous usage data.

**Operational Hygiene**
- Sync cancellation reasons from Stripe to your internal CRM for better reporting.
- Update customer status labels in real-time to ensure support teams have the latest account context.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your dashboard.
3. Authenticate your Stripe account within the Composio Toolset node.
4. Ensure nodes are correctly mapped from **Chat Input** to **Agent**, **Composio Toolset**, and **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request to analyze a subscription.
- **Agent**: Processes the churn intent and determines the best retention strategy.
- **Composio Toolset**: Executes API calls to Stripe to fetch account details or apply discounts.
- **Chat Output**: Delivers the summary of the retention action taken to the dashboard or user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Analyze the recent cancellation request for customer_id: cus_12345 and suggest a retention offer.`
- `Check the status of subscription sub_67890 and apply a 20% discount if the customer is on the Pro plan.`
- `Generate a summary report of all churned customers from the last 7 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a retention specialist, balancing empathy with revenue protection.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruction: "You are a retention expert. Analyze the customer's subscription data and provide a tailored response to prevent churn."
- Instruction: "Always verify the subscription status in Stripe before proposing a discount."

### 2) Composio Toolset Node
- Connect your Stripe API key via the Composio dashboard.
- Ensure the connection scope includes `subscriptions:read` and `subscriptions:write` permissions.

### 3) Tool Availability
- `stripe_get_subscription`: Retrieve detailed subscription metadata.
- `stripe_update_subscription`: Apply discounts or modify subscription terms.
- `stripe_list_events`: Monitor for cancellation or payment failure webhooks.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Recover lost sales through automated email and SMS workflows.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track customer engagement metrics to predict potential churn.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automate financial data matching between payment gateways and accounting software.
