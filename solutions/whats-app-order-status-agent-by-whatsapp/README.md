# WhatsApp Order Status Agent (Uplizd) - Proactive delivery updates and automated order tracking

## Summary
The WhatsApp Order Status Agent is an intelligent automation workflow designed to streamline post-purchase communication by providing real-time order tracking and delivery updates directly within WhatsApp. By leveraging the Composio Toolset to interface with e-commerce platforms and messaging APIs, this solution eliminates manual status inquiries, reduces customer support ticket volume, and enhances the post-purchase experience through automated, personalized notifications.

---

## Demo
![WhatsApp Order Status Agent workflow interface showing automated order tracking and customer notification flow](image.png)
**Alt text (SEO-ready):** WhatsApp Order Status Agent workflow interface showing automated order tracking and customer notification flow, powered by Uplizd and Composio for real-time e-commerce updates.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bdf0bf45-20d1-550e-9966-5fdb5231c485)

---

## Category
- **Primary category:** Customer Support Automation
- **Secondary tags:** whatsapp, e-commerce, order tracking, customer experience, ai workflow, composio, logistics, support automation
- This solution bridges the gap between e-commerce backend data and customer messaging platforms to provide instant, self-service order visibility.

---

## Who is this for?
This solution is designed for teams looking to automate routine customer inquiries and improve transparency in the delivery lifecycle.

- **Customer Support Lead**
    - Reduces the volume of repetitive "Where is my order?" (WISMO) tickets, allowing agents to focus on complex resolutions.
- **E-commerce Manager**
    - Increases customer satisfaction scores (CSAT) by providing proactive, accurate delivery status updates without manual intervention.
- **Operations Specialist**
    - Ensures data consistency between order management systems and customer communication channels.
- **Growth Marketer**
    - Leverages the WhatsApp channel to maintain high engagement rates during the post-purchase phase, fostering brand loyalty.

---

## Features
- **Real-time Order Sync**
    - Automatically fetches the latest order status and tracking information from your e-commerce platform via the Composio Toolset.
- **Automated WhatsApp Notifications**
    - Triggers personalized status updates directly to customers when delivery milestones are reached.
- **Natural Language Query Handling**
    - Uses an AI agent to interpret customer inquiries in natural language, identifying order numbers and status requests accurately.
- **Proactive Exception Alerts**
    - Notifies customers immediately if there is a shipping delay or delivery exception, maintaining transparency.
- **Secure Data Mapping**
    - Safely maps customer phone numbers and order IDs to ensure private communication and secure data handling.

---

## Use Cases
**Post-Purchase Engagement**
- Send automated "Order Shipped" notifications with tracking links immediately upon fulfillment.
- Provide "Out for Delivery" updates to keep customers informed on the day of arrival.

**Customer Support Efficiency**
- Enable customers to check their order status by simply messaging their order ID to your WhatsApp business line.
- Automatically route complex delivery issues to a human agent if the AI cannot resolve the inquiry.

**Logistics & Operations**
- Sync tracking status from third-party logistics (3PL) providers to ensure the WhatsApp agent always has the latest data.
- Batch update order statuses to prevent redundant API calls while maintaining high data accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the WhatsApp Order Status Agent template from the marketplace.
3. Connect your preferred WhatsApp Business API provider and e-commerce platform via the Composio integration menu.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the customer's message or order inquiry.
- **Agent**: Analyzes the intent and extracts the order ID to determine the necessary action.
- **Composio Toolset**: Executes the API calls to retrieve order details or update status records.
- **Chat Output**: Delivers the formatted order status or tracking information back to the customer.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Check the status of order #12345.`
- `Where is my package? My order number is 98765.`
- `Can you tell me when my order 55443 is expected to arrive?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for interpreting customer intent and managing the conversation flow.
- Set the system prompt to prioritize accuracy and helpfulness regarding order data.
- Configure the agent to handle missing order IDs by politely asking the user for the missing information.
- Ensure the agent is restricted to only accessing order-related tools to maintain security.

### 2) Composio Toolset Node
- Provide your API keys for the e-commerce platform (e.g., Shopify, WooCommerce) and the WhatsApp provider.
- Set the connection scope to allow read-only access to order data to ensure maximum security.

### 3) Tool Availability
- **Order Lookup Tool**: Retrieves order status, tracking numbers, and delivery dates.
- **Messaging Tool**: Sends template-based messages to WhatsApp users.
- **Data Formatting Tool**: Cleans and structures raw API data into human-readable responses.

---

## Related Solutions
- [WhatsApp Lead Qualifier (by WATI)](../whats-app-lead-qualifier-by-wati/README.md) — Automate lead qualification and initial engagement on WhatsApp.
- [WhatsApp Support Triage Agent (by 2Chat)](../whats-app-support-triage-agent-by2chat/README.md) — Route incoming support tickets to the right team members.
- [Abandoned Cart Recovery Agent (by Klaviyo)](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Recover lost sales through automated recovery sequences.
