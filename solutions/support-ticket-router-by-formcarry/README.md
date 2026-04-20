# Support Ticket Router (Uplizd) - Intelligent automated triage and routing for customer support

## Summary
The Support Ticket Router by Formcarry is an intelligent Uplizd AI workflow that automatically categorizes incoming customer inquiries and routes them to the appropriate department or team member. By leveraging real-time analysis of support requests, this solution eliminates manual triage bottlenecks, reduces response times, and ensures that critical issues are prioritized, ultimately improving team productivity and customer satisfaction.

---

## Demo
![Support Ticket Router workflow diagram showing Formcarry input, AI agent classification, and automated routing](image.png)
**Alt text (SEO-ready):** Support Ticket Router workflow in Uplizd, featuring automated ticket categorization, Formcarry integration, and intelligent AI routing for customer support teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4a74be5e-4d85-5785-9dda-68e2d391ac2b)

---

## Category
- **Primary category:** Customer support
- **Secondary tags:** support automation, ticket routing, formcarry, ai workflow, triage, customer experience, helpdesk, composio
- This solution streamlines helpdesk operations by automating the classification and assignment of incoming support tickets based on content and urgency.

---

## Who is this for?
This solution is designed for support teams and operations managers looking to scale their service capacity without increasing overhead.

- **Support Manager**
    - Automates ticket assignment to ensure balanced workloads across the team.
- **Customer Success Lead**
    - Ensures high-priority accounts receive immediate attention from dedicated representatives.
- **Operations Specialist**
    - Reduces the manual effort required to categorize and tag incoming support requests.
- **Technical Support Agent**
    - Eliminates time spent on ticket triage, allowing for faster resolution of complex issues.

---

## Features
- **Intelligent Categorization**
    - Uses advanced LLMs to analyze ticket sentiment and intent, automatically assigning relevant tags.
- **Automated Routing Logic**
    - Dynamically routes requests to specific team members or queues based on expertise and availability.
- **Formcarry Integration**
    - Seamlessly ingests form submissions from your website, ensuring no customer request is missed.
- **Priority Scoring**
    - Automatically flags urgent or high-impact tickets for immediate escalation to senior staff.
- **Real-time Workflow Execution**
    - Processes incoming tickets instantly, providing a consistent and rapid response experience for customers.

---

## Use Cases
**Support Triage Automation**
- Automatically route billing inquiries to the finance team while technical bugs are sent to engineering.
- Identify and escalate urgent customer complaints to the management queue within minutes of submission.

**Team Workload Balancing**
- Distribute incoming tickets evenly across available agents to prevent burnout and ensure consistent coverage.
- Assign tickets based on specific product expertise, ensuring the right agent handles the right technical issue.

**Customer Experience Optimization**
- Send automated "we are reviewing your request" notifications immediately after the AI routes the ticket.
- Reduce "time to first response" by eliminating the manual sorting process that often delays ticket assignment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Support Ticket Router solution.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Formcarry API credentials to the input node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw ticket data from Formcarry webhooks.
- **Agent**: Analyzes ticket content, determines intent, and selects the routing path.
- **Composio Toolset**: Executes the routing actions in your helpdesk or CRM platform.
- **Chat Output**: Confirms successful routing and logs the ticket status.

### 3) Run the Flow
Use the Playground to test your routing logic with these example prompts:
- `Analyze this ticket: "I am unable to access my dashboard after the latest update" and route to the Engineering queue.`
- `Classify the following request: "How do I upgrade my current subscription plan?" and assign to the Billing team.`
- `Evaluate this urgent message: "My service is completely down and I have a deadline in one hour" and escalate to the Priority Support team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, interpreting natural language requests to make routing decisions.
- **Recommended instruction pattern:**
    - Act as a professional support triage assistant.
    - Identify the core intent and urgency of every incoming ticket.
    - Map the ticket to the correct department based on the provided routing rules.

### 2) Composio Toolset Node
- Provide your API key for the target helpdesk or CRM platform.
- Ensure the connection scope includes permissions to update ticket status and assign owners.

### 3) Tool Availability
- **Ticket Assignment Tool**: Updates the "Assignee" field in your helpdesk.
- **Tagging Tool**: Adds relevant labels (e.g., "Billing", "Technical", "Urgent") to the ticket.
- **Notification Tool**: Triggers internal alerts for high-priority escalations.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-powered assistant for 24/7 customer support coverage.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Automated chatbot solutions for instant customer query resolution.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Specialized triage for support requests coming through WhatsApp.
