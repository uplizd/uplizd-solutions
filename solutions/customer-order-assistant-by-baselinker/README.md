# Customer Order Assistant (Uplizd) - Automated order tracking and history retrieval

## Summary
The Customer Order Assistant is an intelligent AI workflow designed to streamline e-commerce support by providing instant access to customer order history and status updates. By integrating with BaseLinker via the Composio Toolset, this solution eliminates manual search time for support teams, ensuring a single source of truth for order data and significantly improving response pipeline velocity.

---

## Demo
![Customer Order Assistant workflow interface showing BaseLinker order lookup and status retrieval](image.png)
**Alt text (SEO-ready):** Customer Order Assistant (Uplizd) workflow showing automated BaseLinker order status retrieval and e-commerce support integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/963fa52d-a680-5f14-925c-4512cbdd3ad8)

---

## Category
**Primary category:** Support automation  
**Secondary tags:** baselinker, e-commerce, order management, customer support, data retrieval, ai workflow, composio, order tracking  
This solution bridges the gap between customer inquiries and backend order management systems to provide real-time data visibility.

---

## Who is this for?
This solution is designed for support teams and operations managers who need to reduce ticket resolution time and improve customer satisfaction.

- **Support Agent**
  - Reduces time spent toggling between support tickets and BaseLinker to verify order details.
- **E-commerce Manager**
  - Ensures consistent order status communication across all customer touchpoints.
- **Operations Lead**
  - Automates routine data lookups, allowing the team to focus on complex issue resolution.
- **Customer Success Manager**
  - Provides instant, accurate updates to high-value clients regarding their current shipments.

---

## Features
- **Real-time Order Lookup**
  - Instantly query BaseLinker for specific order IDs or customer email addresses to retrieve current status.
- **Automated Status Reporting**
  - Translates raw system data into natural language responses for immediate customer communication.
- **Composio-Powered Integration**
  - Leverages secure, authenticated connections to BaseLinker to ensure data integrity and privacy.
- **Context-Aware Agent**
  - Uses the Agent node to interpret vague customer queries and map them to precise API calls.
- **Seamless Data Flow**
  - Connects Chat Input to Chat Output, creating a closed-loop system for rapid support ticket resolution.

---

## Use Cases
**Order Status Inquiries**
- Retrieve the current shipping status of an order using only the customer's order number.
- Provide estimated delivery dates based on the latest tracking information available in BaseLinker.

**Customer History Retrieval**
- Quickly pull a summary of a customer's recent purchase history to personalize support interactions.
- Verify order contents and SKU details to assist with return or exchange requests.

**Support Triage Optimization**
- Automatically append order status context to incoming support tickets before they reach a human agent.
- Reduce "Where is my order?" (WISMO) ticket volume by providing instant, automated self-service responses.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `customer-order-assistant-by-baselinker` template from the library.
3. Connect your BaseLinker API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the customer's order inquiry or request for status.
- **Agent**: Analyzes the intent and determines the necessary BaseLinker tool to invoke.
- **Composio Toolset**: Executes the API call to BaseLinker to fetch the requested order data.
- **Chat Output**: Formats the retrieved data into a helpful, professional response for the user.

### 3) Run the Flow
Use the Playground to test the assistant with the following prompts:
- `What is the status of order #12345?`
- `Can you check the shipping details for the latest order from john.doe@example.com?`
- `Has order #98765 been dispatched yet?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer between the user and the BaseLinker API.
- Maintain a professional and helpful tone for all customer-facing responses.
- Prioritize accuracy when extracting order IDs from user input.
- If an order is not found, instruct the agent to ask the user to verify the order number.

### 2) Composio Toolset Node
- Requires a valid BaseLinker API key.
- Connection scope should be limited to order read-only permissions for security.

### 3) Tool Availability
- `get_order_details`: Fetches comprehensive data for a specific order ID.
- `list_orders_by_customer`: Retrieves a list of orders associated with a specific email or customer profile.
- `get_shipping_status`: Queries the latest tracking information for a given order.

---

## Related Solutions
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) — Deploy a 24/7 AI chatbot for general customer support inquiries.
- [whats-app-order-status-agent-by-wati](../whats-app-order-status-agent-by-wati/README.md) — Automate order status updates directly through WhatsApp.
- [account-research-agent-by-onepage](../account-research-agent-by-onepage/README.md) — Gather deep intelligence on customer accounts for personalized support.
