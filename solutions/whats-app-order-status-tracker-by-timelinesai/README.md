# WhatsApp Order Status Tracker (Uplizd) - Automated real-time delivery updates and inquiry management

## Summary
The WhatsApp Order Status Tracker is an AI-powered workflow that streamlines post-purchase communication by providing customers with instant, accurate delivery updates directly within WhatsApp. By integrating TimelinesAI with the Uplizd agentic framework, this solution reduces support ticket volume, eliminates manual status lookups, and ensures a seamless, proactive customer experience that drives brand loyalty.

---

## Demo
![WhatsApp Order Status Tracker workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** WhatsApp Order Status Tracker workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes for automated customer support and order tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c4ae51a8-2a33-5c2b-9f50-0b86c2c5cd11)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** whatsapp, timelinesai, order tracking, ecommerce, customer experience, ai workflow, support automation, composio
- This solution bridges the gap between e-commerce backend data and messaging platforms to automate routine delivery status inquiries.

---

## Who is this for?
This solution is designed for teams looking to scale their support operations without increasing headcount.

- **Customer Support Lead**
    - Reduces the volume of repetitive "where is my order" tickets, allowing the team to focus on complex escalations.
- **E-commerce Operations Manager**
    - Ensures consistent, real-time communication across the customer journey, improving post-purchase satisfaction metrics.
- **Support Agent**
    - Offloads manual status lookups to the AI agent, freeing up time to provide personalized human assistance.
- **Growth Marketer**
    - Leverages the WhatsApp channel to maintain high engagement and trust after the initial sale is completed.

---

## Features
- **Automated Order Lookup**
    - Instantly queries order databases via the Composio Toolset to retrieve real-time shipment status and tracking numbers.
- **WhatsApp Integration**
    - Utilizes TimelinesAI to facilitate bi-directional communication, ensuring updates are delivered where customers are most active.
- **Context-Aware Responses**
    - The Agent node interprets natural language queries, distinguishing between status checks, delivery delays, and shipping address issues.
- **Proactive Notification Logic**
    - Enables the workflow to trigger status updates based on specific delivery milestones or changes in tracking status.
- **Seamless Handoff**
    - Automatically routes complex or unresolved inquiries to human support agents, maintaining a high standard of service.

---

## Use Cases
**Post-Purchase Support**
- Providing customers with instant tracking links and estimated delivery dates upon request.
- Notifying users automatically when an order status changes from "Processing" to "Out for Delivery."

**Operational Efficiency**
- Reducing average response times (ART) by automating the resolution of routine order inquiries.
- Centralizing order data visibility within the WhatsApp conversation thread for easier management.

**Customer Retention**
- Managing expectations during shipping delays by providing transparent, AI-generated status explanations.
- Offering a frictionless self-service experience that increases customer satisfaction and repeat purchase rates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your TimelinesAI and e-commerce platform credentials within the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the customer's WhatsApp message containing the order ID or inquiry.
- **Agent**: Processes the intent and determines the necessary data retrieval steps.
- **Composio Toolset**: Executes secure API calls to your order management system to fetch status details.
- **Chat Output**: Formats the retrieved data into a helpful, conversational WhatsApp response.

### 3) Run the Flow
Test the workflow in the Uplizd Playground using these prompts:
- `Check the status of order #12345 for me.`
- `My order was supposed to arrive yesterday, can you check where it is?`
- `Can you give me the tracking link for order #98765?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent interface between the customer and your backend data.
- **Instruction Pattern:**
    - Always maintain a helpful, professional, and brand-aligned tone.
    - If an order ID is missing, politely ask the user to provide it before proceeding.
    - Clearly state the current status and provide the tracking link if available.

### 2) Composio Toolset Node
- **API Key**: Configure your TimelinesAI and e-commerce platform API keys within the Composio dashboard.
- **Connection Scope**: Ensure the agent has read-only access to order history and shipment tracking endpoints.

### 3) Tool Availability
- **Order Lookup Tool**: Retrieves order status, tracking numbers, and delivery dates.
- **WhatsApp Messaging Tool**: Sends formatted text responses back to the customer thread.
- **Support Escalation Tool**: Flags the conversation for human intervention if the AI cannot resolve the query.

---

## Related Solutions
- [WhatsApp Support Automator](../whats-app-support-automator-by-timelinesai/README.md) — Streamline general support inquiries and ticket routing.
- [WhatsApp Lead Qualifier](../whats-app-lead-qualifier-by-timelinesai/README.md) — Automatically qualify incoming leads via WhatsApp conversation.
- [WhatsApp Webhook Integration Manager](../whats-app-webhook-integration-manager-by-timelinesai/README.md) — Manage complex event-driven workflows for WhatsApp.
