# WhatsApp Order Status Agent (Uplizd) - Automated real-time order tracking and customer updates

## Summary
The WhatsApp Order Status Agent by 2Chat is an intelligent automation workflow designed to provide customers with instant, accurate order updates directly within their preferred messaging platform. By integrating real-time order data with WhatsApp, this solution eliminates manual status inquiries, reduces support ticket volume, and significantly improves the post-purchase customer experience.

---

## Demo
![WhatsApp Order Status Agent workflow interface showing automated customer inquiry resolution](image.png)
**Alt text (SEO-ready):** WhatsApp Order Status Agent (Uplizd) workflow interface showing automated customer inquiry resolution via 2Chat and real-time order tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dc403700-81ed-563e-8543-76172ac86ecb)

---

## Category
**Primary category:** Customer Support Automation  
**Secondary tags:** whatsapp, 2chat, order tracking, ecommerce, customer experience, ai workflow, composio, support automation  
This solution streamlines post-purchase communications by bridging the gap between your order management system and WhatsApp messaging.

---

## Who is this for?
This solution is designed for businesses looking to automate routine customer inquiries and scale their support operations without adding headcount.

- **E-commerce Store Owners**
  - Reduce "Where is my order?" (WISMO) tickets by providing proactive, automated status updates.
- **Customer Support Managers**
  - Free up human agents to handle complex issues by automating repetitive status lookup tasks.
- **Operations Leads**
  - Ensure consistent, accurate data delivery across all customer touchpoints using integrated toolsets.
- **Growth Marketers**
  - Enhance customer retention and brand loyalty through seamless, high-velocity communication channels.

---

## Features
- **Real-time Order Retrieval**
  - Instantly fetch current order status, shipping details, and tracking numbers from your backend systems.
- **Automated WhatsApp Messaging**
  - Trigger personalized, conversational responses directly to the customer's WhatsApp interface via 2Chat.
- **Intelligent Intent Recognition**
  - Utilize AI to accurately identify order-related queries and map them to the correct data lookup functions.
- **Seamless Composio Integration**
  - Leverage the Composio Toolset to securely connect your messaging platform with your order management database.
- **Proactive Status Notifications**
  - Configure the agent to push updates automatically when order milestones are reached, such as "Shipped" or "Out for Delivery."

---

## Use Cases
**Customer Self-Service**
- Provide 24/7 instant access to order status without requiring human agent intervention.
- Enable customers to request tracking links or delivery estimates via simple WhatsApp commands.

**Support Efficiency**
- Automatically triage and resolve high-volume WISMO inquiries during peak shopping seasons.
- Reduce average response time by providing immediate, data-backed answers to common order questions.

**Post-Purchase Engagement**
- Send automated, branded shipping confirmations that keep customers informed and excited.
- Proactively notify customers of delivery delays or status changes to build trust and transparency.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your 2Chat and CRM/Order Management accounts within the integration settings.
4. Ensure nodes are correctly connected and all required API keys are active.

### 2) Setup the Nodes
- **Chat Input:** Receives the customer's order inquiry from WhatsApp.
- **Agent:** Processes the intent and determines the necessary data to retrieve.
- **Composio Toolset:** Executes the secure lookup against your order management system.
- **Chat Output:** Delivers the formatted order status update back to the customer via 2Chat.

### 3) Run the Flow
Test your agent in the Uplizd Playground:
- `What is the status of order #12345?`
- `Can you tell me where my package is?`
- `Check the delivery date for order #98765.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a conversational interface between your customer and your database.
- Maintain a helpful, professional, and concise tone.
- Prioritize accuracy by strictly referencing the data returned by the Composio Toolset.
- If an order number is missing, politely prompt the user to provide it.

### 2) Composio Toolset Node
- Provide your API key to authenticate the connection between Uplizd and your order management platform.
- Ensure the connection scope includes read-only access to order history and tracking information.

### 3) Tool Availability
- **Order Lookup:** Queries database by order ID or customer email.
- **Tracking Link Generator:** Retrieves live carrier tracking URLs.
- **WhatsApp Messaging:** Formats and sends replies via 2Chat API.

---

## Related Solutions
- [WhatsApp Support Triage Agent (2Chat)](../whats-app-support-triage-agent-by2chat/README.md) - Automate ticket categorization and routing for WhatsApp support.
- [WhatsApp Feedback Collection Agent (2Chat)](../whats-app-feedback-collection-agent-by2chat/README.md) - Gather customer sentiment and reviews directly via WhatsApp.
- [WhatsApp Lead Qualifier (2Chat)](../whats-app-lead-qualifier-by2chat/README.md) - Qualify incoming sales leads automatically through conversational WhatsApp flows.
