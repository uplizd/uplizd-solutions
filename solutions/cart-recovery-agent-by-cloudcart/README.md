# Cart Recovery Agent (Uplizd) - Automate abandoned cart recovery and boost conversion rates

## Summary
The Cart Recovery Agent is an intelligent Uplizd workflow designed to identify, engage, and convert users who have left items in their shopping carts. By leveraging real-time data from your e-commerce platform, the agent automates personalized outreach, offering incentives or assistance to recover lost revenue and improve overall pipeline velocity.

---

## Demo
![Cart Recovery Agent workflow showing data ingestion, AI analysis, and automated outreach](../image.png)
**Alt text (SEO-ready):** Cart Recovery Agent workflow for Uplizd, automating e-commerce abandoned cart recovery, customer outreach, and conversion optimization via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7bb48dc1-9d6e-51c4-b223-cf0ec9e7bd90)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** ecommerce, cart recovery, conversion, sales, customer retention, composio, ai workflow, revenue growth
- This solution bridges the gap between abandoned shopping sessions and completed transactions through automated, data-driven engagement.

---

## Who is this for?
This solution is built for teams focused on maximizing e-commerce revenue and improving customer retention.

- **E-commerce Manager**
    - Automates the recovery process to ensure no potential sale is left behind without manual intervention.
- **Growth Marketer**
    - Increases conversion rates by triggering personalized, timely follow-ups based on user cart behavior.
- **Sales Operations Lead**
    - Maintains clean, actionable data on lost opportunities and recovery success metrics.
- **Customer Success Specialist**
    - Provides proactive support to users who may be experiencing technical issues during the checkout process.

---

## Features
- **Real-time Abandonment Detection**
    - Instantly identifies when a user leaves a cart, allowing for immediate, high-intent follow-up.
- **Personalized Outreach Engine**
    - Uses AI to craft tailored messages that address specific items left in the cart, increasing the likelihood of conversion.
- **Dynamic Incentive Management**
    - Automatically applies discounts or limited-time offers to nudge hesitant buyers toward checkout.
- **Seamless CRM Integration**
    - Syncs recovery status and customer interactions directly into your CRM using the Composio Toolset.
- **Performance Analytics Dashboard**
    - Tracks recovery rates and revenue generated, providing clear visibility into the ROI of your automated campaigns.

---

## Use Cases
**Proactive Revenue Recovery**
- Automatically send a personalized email or SMS 30 minutes after a cart is abandoned.
- Offer a time-sensitive discount code to users who have high-value items in their cart.

**Customer Support & Friction Removal**
- Identify if a user abandoned their cart due to shipping costs and offer a one-time shipping waiver.
- Flag technical errors during checkout for immediate review by the support team.

**Lead Nurturing & Re-engagement**
- Add users who abandoned their carts to a dedicated re-engagement campaign in your marketing automation platform.
- Segment recovered users based on their purchase history to suggest complementary products.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your e-commerce platform and CRM via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are authenticated.

### 2) Setup the Nodes
- **Chat Input**: Receives trigger events from your e-commerce platform regarding abandoned sessions.
- **Agent**: Processes cart data and determines the optimal recovery strategy.
- **Composio Toolset**: Executes actions like sending emails, updating CRM fields, or generating discount codes.
- **Chat Output**: Logs the recovery action taken and provides a summary of the interaction.

### 3) Run the Flow
Use the Playground to test your recovery logic:
- `Identify all carts abandoned in the last 2 hours and draft recovery emails.`
- `Check if the user with ID 12345 has completed their purchase after the last follow-up.`
- `Apply a 10% discount code to the cart for user email: customer@example.com.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your automated sales assistant, prioritizing high-value carts and maintaining a helpful tone.
- Instruction: Analyze cart contents and user history to determine the best recovery incentive.
- Instruction: Maintain a professional, helpful, and non-intrusive communication style.
- Instruction: Always verify the current status of the cart before triggering an outreach action.

### 2) Composio Toolset Node
- Requires an active API key for your e-commerce platform (e.g., Shopify, WooCommerce) and your CRM.
- Connection scope should include read access to cart data and write access to customer communication channels.

### 3) Tool Availability
- **E-commerce Connector**: Fetch cart details, apply discounts, and check order status.
- **CRM Connector**: Update lead records, log interactions, and trigger follow-up tasks.
- **Communication Connector**: Send automated emails or SMS notifications.

---

## Related Solutions
- [Abandoned Cart Recovery Agent (Klaviyo)](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Specialized recovery workflows using Klaviyo's marketing automation.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize customer data across platforms to ensure accurate recovery targeting.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score high-value opportunities for your sales team.
