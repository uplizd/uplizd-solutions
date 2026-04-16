# Client Consultation Manager (Uplizd) - Streamline booking and availability synchronization

## Summary
The Client Consultation Manager is an intelligent Uplizd workflow designed to automate the scheduling lifecycle by syncing client availability directly with your calendar. By leveraging the Composio Toolset to interface with Calendly and CRM platforms, this solution eliminates manual coordination, reduces scheduling friction, and ensures that every consultation is captured, confirmed, and logged without administrative overhead.

---

## Demo
![Client Consultation Manager workflow interface showing automated booking and calendar synchronization](image.png)
**Alt text (SEO-ready):** Client Consultation Manager Uplizd workflow, automated calendar booking, Calendly CRM integration, and scheduling automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/64eae9e7-661e-5fd5-9fa2-d08f85138f74)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** scheduling, calendly, crm, automation, client management, workflow, composio, booking
- This solution optimizes operational efficiency by bridging the gap between client communication channels and internal scheduling systems.

---

## Who is this for?
This solution is designed for professionals who manage high-volume client interactions and require a seamless, automated approach to calendar management.

- **Account Managers**
    - Automate follow-up meetings and ensure consistent touchpoints without manual calendar checking.
- **Sales Representatives**
    - Reduce lead-to-meeting time by allowing prospects to book directly into optimized time slots.
- **Customer Success Leads**
    - Coordinate onboarding sessions and health check calls across multiple time zones effortlessly.
- **Operations Managers**
    - Standardize the booking process across the team to maintain data hygiene and pipeline velocity.

---

## Features
- **Real-time Availability Sync**
    - Automatically updates your calendar availability across platforms to prevent double-booking and scheduling conflicts.
- **Smart CRM Integration**
    - Automatically logs new consultation bookings as activities or events within your CRM, ensuring a single source of truth.
- **Automated Confirmation Logic**
    - Triggers instant confirmation messages and calendar invites immediately upon successful booking via the Composio Toolset.
- **Intelligent Buffer Management**
    - Dynamically applies buffer times between meetings to ensure preparation time and travel flexibility.
- **Customizable Booking Rules**
    - Configures specific constraints such as minimum notice periods and daily meeting caps to protect your productivity.

---

## Use Cases
**Client Onboarding**
- Automatically schedule kickoff calls immediately after a deal is marked as "Closed Won" in your CRM.
- Send personalized welcome packets and meeting links to new clients without manual intervention.

**Sales Pipeline Acceleration**
- Enable prospects to book discovery calls directly from email signatures or landing pages.
- Sync meeting details back to the lead record to keep sales history updated in real-time.

**Customer Support & Success**
- Coordinate recurring quarterly business reviews (QBRs) by automating the scheduling outreach process.
- Manage urgent support triage sessions by prioritizing high-value accounts in your booking flow.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the `client-consultation-manager-by-cal` solution template.
3. Connect your required CRM and Calendly accounts via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives client booking requests or scheduling intent from your communication channel.
- **Agent**: Processes natural language requests and maps them to specific calendar actions.
- **Composio Toolset**: Executes the API calls to verify availability and create calendar events.
- **Chat Output**: Confirms the booking details or requests additional information from the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check my availability for next Tuesday and suggest three slots for a client meeting.`
- `Book a 30-minute discovery call with John Doe from Acme Corp for tomorrow afternoon.`
- `Reschedule my current 2 PM meeting to the next available slot on Wednesday.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your scheduling assistant, interpreting intent and managing tool execution.
- Instruction: "You are a professional scheduling assistant. Always verify availability before proposing times."
- Instruction: "If a conflict is detected, offer the next two available time slots."
- Instruction: "Ensure all booked meetings are logged in the CRM with the correct client ID."

### 2) Composio Toolset Node
- Provide your API key to enable secure communication with your calendar and CRM providers.
- Ensure the connection scope includes `calendar.read`, `calendar.write`, and `crm.write` permissions.

### 3) Tool Availability
- **Calendar API**: For checking availability and creating/updating events.
- **CRM Connector**: For logging meeting details and updating client interaction history.
- **Notification Service**: For sending automated confirmation emails or messages.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects before meetings.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline the creation of new client records in your CRM.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up tasks for your sales team.
