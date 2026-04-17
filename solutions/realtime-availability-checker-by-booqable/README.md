# Real-time Availability Checker (Uplizd) - Automated equipment scheduling and inventory management

## Summary
The Real-time Availability Checker (Uplizd) is an intelligent automation workflow that bridges the gap between customer inquiries and live inventory data. By leveraging the Booqable integration, this solution eliminates manual scheduling conflicts, provides instant booking confirmation, and ensures your team maintains a single source of truth for equipment availability, significantly increasing operational velocity and customer satisfaction.

---

## Demo
![Real-time Availability Checker workflow showing Chat Input, Agent, Booqable Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Real-time Availability Checker workflow in Uplizd showing Booqable inventory integration for automated booking and scheduling.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/31ca5f2f-a743-5fe5-b994-cc8b507cf798)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** booqable, inventory management, scheduling, automation, real-time, booking, composio, ai workflow
- This solution streamlines equipment rental operations by connecting customer-facing chat interfaces directly to your Booqable inventory system.

---

## Who is this for?
This solution is designed for operations teams and rental businesses looking to automate their booking pipeline and reduce manual administrative overhead.

- **Operations Manager**
    - Automate inventory checks to prevent double-bookings and scheduling errors.
- **Customer Support Lead**
    - Provide instant, accurate responses to rental availability inquiries without manual lookups.
- **Rental Business Owner**
    - Scale booking capacity by removing the bottleneck of manual availability verification.
- **Sales Representative**
    - Quickly confirm equipment availability during client calls to close deals faster.

---

## Features
- **Real-time Inventory Sync**
    - Connects directly to Booqable to fetch live stock levels and equipment status.
- **Automated Availability Logic**
    - Uses AI to interpret natural language booking requests and map them to specific inventory items.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely authenticate and execute API calls to your Booqable account.
- **Instant Response Generation**
    - Delivers human-like, accurate availability updates directly to the customer in the chat interface.
- **Conflict Resolution**
    - Automatically identifies overlapping booking requests and suggests alternative equipment or time slots.

---

## Use Cases
**Rental Operations**
- Automatically verify if high-demand equipment is available for specific date ranges requested by customers.
- Sync rental status updates across multiple channels to ensure consistent availability data.

**Customer Experience**
- Provide 24/7 instant availability checks for website visitors inquiring about equipment rentals.
- Reduce response times for booking inquiries by eliminating the need for manual database verification.

**Business Intelligence**
- Track frequently requested items that are often unavailable to optimize future inventory purchasing.
- Monitor booking conversion rates by analyzing the interaction between availability checks and final reservations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Booqable account via the Composio connection prompt.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the customer's natural language request regarding equipment and dates.
- **Agent**: Processes the request, extracts dates and items, and decides which tool to invoke.
- **Composio Toolset**: Executes the specific API call to Booqable to retrieve real-time data.
- **Chat Output**: Formats the retrieved availability data into a helpful, conversational response.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Is the professional camera kit available for rent from October 12th to October 15th?`
- `Check availability for the lighting rig next weekend.`
- `Do you have any audio mixers available on the 20th of this month?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between the user and the inventory database.
- **Recommended instruction pattern:**
    - Act as a professional rental assistant with access to real-time Booqable inventory.
    - Always verify the exact dates and item names before confirming availability.
    - If an item is unavailable, suggest the nearest alternative or contact the support team.

### 2) Composio Toolset Node
- **API Key**: Ensure your Booqable API key is stored securely in your Composio account.
- **Connection Scope**: Grant read-only access to inventory and booking endpoints to maintain data security.

### 3) Tool Availability
- `booqable_get_products`: Retrieve a list of available rental items.
- `booqable_check_availability`: Query specific item availability for defined date ranges.
- `booqable_get_bookings`: Fetch current booking status for conflict verification.

---

## Related Solutions
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) - Manage and track maintenance work orders efficiently.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data for better sales targeting.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate end-to-end business workflows and task management.
