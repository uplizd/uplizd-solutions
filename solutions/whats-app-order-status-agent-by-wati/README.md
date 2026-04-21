# WhatsApp Order Status Agent (Uplizd) - Automated real-time order tracking and customer updates

## Summary
The WhatsApp Order Status Agent by WATI is an intelligent automation workflow designed to provide customers with instant, accurate order updates directly within their preferred messaging platform. By integrating real-time order data with WhatsApp, this solution eliminates manual support inquiries, reduces ticket volume for customer service teams, and enhances the post-purchase experience through proactive, automated communication.

---

## Demo
![WhatsApp Order Status Agent workflow showing Chat Input, Agent, WATI Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** WhatsApp Order Status Agent by Uplizd, automated order tracking workflow, WATI integration, real-time customer support automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/90d1a414-21a7-576e-99be-933986766cde)

---

## Category
**Primary category:** Customer Support Automation
**Secondary tags:** whatsapp, wati, order tracking, ecommerce, customer experience, ai workflow, composio, support automation.
This solution streamlines post-purchase communication by bridging the gap between your order management system and WhatsApp messaging.

---

## Who is this for?
This solution is designed for teams managing high-volume ecommerce operations and customer support.

- **Customer Support Manager**
    - Reduces the volume of repetitive "Where is my order?" tickets by providing instant, automated status updates.
- **Ecommerce Operations Lead**
    - Ensures consistent, high-quality communication across the post-purchase lifecycle without increasing headcount.
- **Customer Success Specialist**
    - Empowers agents to focus on complex account issues while the AI handles routine order status inquiries.
- **Technical Product Manager**
    - Leverages pre-built Composio integrations to deploy scalable messaging workflows without custom API development.

---

## Features
- **Real-time Order Retrieval**
    - Automatically fetches the latest order status and tracking details from your connected ecommerce platform.
- **Automated WhatsApp Delivery**
    - Sends structured, timely updates to customers via the WATI API, ensuring high open rates and immediate engagement.
- **Intelligent Intent Recognition**
    - Uses the Agent node to accurately parse customer queries and distinguish between order status requests and general support needs.
- **Seamless Composio Integration**
    - Connects directly to WATI via the Composio Toolset, managing authentication and API communication securely.
- **Proactive Notification Logic**
    - Configurable triggers that allow the agent to initiate updates based on status changes like "Shipped" or "Out for Delivery."

---

## Use Cases
**Post-Purchase Support**
- Providing instant order tracking links when a customer sends their order number via WhatsApp.
- Automatically notifying customers of delivery delays or status changes to maintain transparency.

**Customer Experience Optimization**
- Reducing average handle time (AHT) by automating the retrieval of shipping information.
- Offering 24/7 self-service options for customers to check their order status without waiting for human support.

**Operational Efficiency**
- Deflecting routine inquiries away from live support agents to improve overall team productivity.
- Standardizing the format of order status updates to ensure brand consistency across all customer interactions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in the builder.
2. Connect your WATI API credentials within the Composio Toolset node.
3. Configure your ecommerce platform connection to allow the agent to query order databases.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the customer's order inquiry or tracking request.
*   **Agent**: Processes the request, identifies the order ID, and determines the necessary tool call.
*   **Composio Toolset**: Executes the API call to WATI and your order management system to fetch status.
*   **Chat Output**: Delivers the formatted order status update back to the customer on WhatsApp.

### 3) Run the Flow
Use the Playground to test your agent with the following prompts:
- `Check the status of order #12345.`
- `Where is my package? My order number is 98765.`
- `Can you give me an update on my recent order?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between the user's natural language and the WATI API.
*   Maintain a helpful, professional tone suitable for customer support.
*   Strictly extract order numbers from user input to prevent lookup errors.
*   If an order is not found, provide a clear, polite fallback message directing the user to human support.

### 2) Composio Toolset Node
*   **API Key**: Provide your WATI API key to authorize the agent to send messages and retrieve data.
*   **Connection Scope**: Ensure the toolset has read access to your order management database and write access to the WATI messaging channel.

### 3) Tool Availability
*   **WATI Send Message**: Enables the agent to push updates to the customer.
*   **Order Lookup Tool**: Allows the agent to query the status of specific order IDs.
*   **Customer Verification**: Optional tool to verify the customer's phone number against the order record.

---

## Related Solutions
- [WhatsApp Lead Qualifier by WATI](../whats-app-lead-qualifier-by-wati/README.md) - Automate lead qualification and scoring directly in WhatsApp.
- [WhatsApp Support Triage Agent by WATI](../whats-app-support-triage-agent-by-wati/README.md) - Efficiently categorize and route support tickets from WhatsApp.
- [WhatsApp Feedback Collector by WATI](../whats-app-feedback-collector-by-wati/README.md) - Gather post-purchase customer sentiment and feedback automatically.
