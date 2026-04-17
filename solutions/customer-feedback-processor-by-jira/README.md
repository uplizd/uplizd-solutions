# Customer Feedback Processor (Uplizd) - Automate Jira task creation from customer feedback

## Summary
The Customer Feedback Processor is an intelligent Uplizd AI workflow that bridges the gap between raw customer insights and engineering execution. By automatically analyzing incoming feedback, categorizing sentiment, and generating structured Jira issues, this solution eliminates manual ticket entry, ensures engineering teams receive high-fidelity requirements, and accelerates the product development lifecycle.

---

## Demo
![Customer Feedback Processor workflow showing feedback ingestion, AI analysis, and Jira ticket creation](image.png)
**Alt text (SEO-ready):** Customer Feedback Processor workflow in Uplizd, automating Jira ticket creation from customer feedback using AI and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2063bbfd-97b6-528e-b88e-2c5965fc8815)

---

## Category
- **Primary category:** Support operations
- **Secondary tags:** jira, feedback, product management, automation, ai workflow, customer insights, ticketing, composio
- This solution streamlines the feedback-to-development loop by automating the triage and documentation of customer requests directly into your project management system.

---

## Who is this for?
This solution is designed for product and support teams looking to reduce manual administrative overhead and improve the feedback loop between customers and engineering.

- **Product Managers**
    - Automatically convert high-impact customer requests into prioritized Jira backlog items.
- **Customer Support Leads**
    - Reduce time spent manually logging bug reports and feature requests from support tickets.
- **Engineering Managers**
    - Ensure developers receive structured, actionable tasks with clear context and user impact.
- **Operations Specialists**
    - Maintain a clean, organized feedback pipeline that maps directly to development progress.

---

## Features
- **Automated Sentiment Analysis**
    - Uses AI to evaluate the urgency and tone of customer feedback to prioritize incoming requests.
- **Jira Integration**
    - Leverages the Composio Toolset to create, update, and link Jira issues automatically based on feedback content.
- **Intelligent Summarization**
    - Condenses long-form customer emails or chat logs into concise, technical requirement descriptions.
- **Real-time Sync**
    - Ensures that feedback captured in support channels is reflected in your development roadmap without manual intervention.
- **Customizable Mapping**
    - Configures how feedback fields map to Jira issue types, labels, and priority levels for consistent data hygiene.

---

## Use Cases
**Support Ticket Triage**
- Automatically escalate bug reports from support tickets to the engineering backlog.
- Tag and route feature requests to the relevant product team based on the feedback category.

**Product Development Lifecycle**
- Sync customer pain points directly into Jira epics to inform the next sprint planning.
- Generate "Voice of Customer" reports by aggregating feedback-driven Jira issues.

**Data-Driven Prioritization**
- Score feature requests based on the frequency of similar feedback received.
- Maintain a clean backlog by linking duplicate feedback to existing Jira tickets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Customer Feedback Processor solution.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Jira account via the Composio integration settings.
4. Ensure nodes are correctly mapped and all API credentials are authenticated.

### 2) Setup the Nodes
- **Chat Input**: Receives raw customer feedback text or support ticket data.
- **Agent**: Analyzes the input, determines intent, and formats the data for Jira.
- **Composio Toolset**: Executes the creation of Jira issues using the structured data.
- **Chat Output**: Confirms successful ticket creation and provides a summary link to the Jira issue.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Process this feedback: "The export button on the dashboard is unresponsive when I try to download CSV files."`
- `Analyze this request: "It would be great if we could integrate with Slack for real-time notifications."`
- `Summarize this ticket: "Users are reporting that the login page takes over 10 seconds to load on mobile devices."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets customer intent.
- **Role:** Act as a technical product analyst.
- **Instruction:** Extract key requirements, identify the urgency, and map the content to standard Jira fields.
- **Constraint:** Maintain a neutral, professional tone in all generated issue descriptions.

### 2) Composio Toolset Node
- **API Key:** Provide your Jira API credentials within the Composio dashboard.
- **Connection Scope:** Ensure the agent has 'Write' permissions for the specific Jira project where tickets should be created.

### 3) Tool Availability
- **Jira Create Issue:** Allows the agent to generate new tasks.
- **Jira Search Issue:** Enables the agent to check for existing duplicates before creating new tickets.
- **Jira Add Comment:** Allows the agent to append feedback details to existing issues.

---

## Related Solutions
- [../action-item-prioritizer-by-rootly/README.md](../action-item-prioritizer-by-rootly/README.md) - Prioritize and manage action items across your technical stack.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate account insights to inform product strategy.
- [../247-customer-support-assistant-by-ai-ml-api/README.md](../247-customer-support-assistant-by-ai-ml-api/README.md) - Provide 24/7 automated support responses.
