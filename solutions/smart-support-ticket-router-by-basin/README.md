# Smart Support Ticket Router (Uplizd) - Intelligent automated ticket classification and routing

## Summary
The Smart Support Ticket Router by Basin is an automated Uplizd AI workflow that streamlines customer service operations by instantly categorizing and routing incoming support requests. By leveraging the Composio Toolset to interface with your helpdesk, this solution ensures that high-priority issues reach the correct department immediately, reducing response times and eliminating manual triage bottlenecks for support teams.

---

## Demo
![Uplizd AI workflow diagram showing a support ticket being routed from a Basin form submission through an intelligent agent to a helpdesk system](image.png)
**Alt text (SEO-ready):** Uplizd AI workflow for automated support ticket routing, Basin form integration, and intelligent helpdesk triage.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2ZmZiI+PHBhdGggZD0iTTEyIDJMMCAxMmgyNHoiLz48L3N2Zz4=)](https://uplizd.ai/solutions/7ecf3702-a6da-5355-afb9-afe494b9a04a)

---

## Category
**Primary category:** Support automation
**Secondary tags:** basin, ticket routing, helpdesk, customer support, ai workflow, triage, composio, automation

This solution optimizes support operations by bridging the gap between customer input forms and ticketing platforms through intelligent intent analysis.

---

## Who is this for?
This workflow is designed for teams looking to scale their support operations without increasing manual overhead.

*   **Support Managers**
    *   Reduce ticket resolution time by automating the initial triage and assignment process.
*   **Customer Success Leads**
    *   Ensure high-priority accounts receive immediate attention through automated sentiment-based routing.
*   **Operations Engineers**
    *   Maintain a clean, organized ticketing pipeline by enforcing standardized routing rules.
*   **Support Agents**
    *   Focus on complex problem-solving rather than manual ticket categorization and manual tagging.

---

## Features
- **Intelligent Intent Classification**
  Uses AI to analyze the content of incoming Basin form submissions to determine the urgency and topic of the request.
- **Automated Ticket Routing**
  Dynamically assigns tickets to the appropriate team or queue based on the classification results.
- **Priority Scoring**
  Automatically flags tickets as "High Priority" if the agent detects urgent keywords or negative sentiment.
- **Seamless Composio Integration**
  Connects directly to your helpdesk infrastructure via the Composio Toolset for real-time ticket creation and updates.
- **Standardized Data Hygiene**
  Ensures all incoming tickets are formatted consistently, improving searchability and reporting within your helpdesk.

---

## Use Cases
**Urgent Issue Escalation**
*   Automatically route tickets containing keywords like "outage," "critical," or "billing error" to the senior support queue.
*   Trigger an immediate notification to the on-call engineer when a high-severity ticket is detected.

**Departmental Triage**
*   Route technical inquiries to the engineering support team while directing general account questions to the customer success team.
*   Filter out spam or non-support inquiries before they reach the agent dashboard.

**Customer Sentiment Analysis**
*   Tag tickets with sentiment scores (Positive, Neutral, Negative) to help agents prioritize their daily workflow.
*   Escalate tickets with high frustration levels to a dedicated retention specialist.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your Basin and Helpdesk accounts within the connection settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input:** Receives the raw form submission data from Basin.
*   **Agent:** Processes the text to classify intent, urgency, and sentiment.
*   **Composio Toolset:** Executes the API calls to create or update the ticket in your helpdesk.
*   **Chat Output:** Confirms the successful routing and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your routing logic with these sample prompts:
* `Route this ticket: "My account is locked and I cannot access my dashboard, this is urgent!"`
* `Classify this request: "How do I update my billing address for next month?"`
* `Analyze this feedback: "The new UI update is confusing and I'm having trouble finding the export button."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, interpreting user intent and determining the correct routing path.
*   Instruct the agent to prioritize keywords related to system outages or security.
*   Define clear mapping rules between intent categories and helpdesk team IDs.
*   Maintain a neutral, professional tone for any automated responses generated.

### 2) Composio Toolset Node
*   Provide your API key to authorize the connection between Uplizd and your helpdesk provider.
*   Set the connection scope to allow read/write access to ticket creation and tagging endpoints.

### 3) Tool Availability
*   **Ticket Creation:** Ability to generate new tickets in the helpdesk system.
*   **Tagging/Labeling:** Ability to apply labels based on AI classification.
*   **Assignment:** Ability to update the 'Assignee' field based on routing logic.
*   **Search/Lookup:** Ability to check existing customer records to prevent duplicate tickets.

---

## Related Solutions
* [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - A general-purpose AI assistant for 24/7 customer support.
* [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Specialized triage for WhatsApp-based support channels.
* [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Intelligent prioritization for technical action items and incident management.
