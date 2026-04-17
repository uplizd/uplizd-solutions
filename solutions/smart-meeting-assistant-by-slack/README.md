# Smart Meeting Assistant (Uplizd) - Streamline team coordination and action item tracking via Slack

## Summary
The Smart Meeting Assistant is an intelligent Uplizd workflow that integrates directly with Slack to automate meeting coordination, capture key takeaways, and sync action items across your workspace. By leveraging AI-driven context extraction, this solution eliminates manual documentation overhead, ensures team alignment, and accelerates pipeline velocity by turning meeting discussions into immediate, trackable tasks.

---

## Demo
![Smart Meeting Assistant workflow diagram showing Slack input, AI processing, and task synchronization](image.png)
**Alt text (SEO-ready):** Smart Meeting Assistant workflow for Slack, featuring Uplizd AI automation, Composio toolset integration, and automated meeting action item tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fb69d0d8-99ee-56b6-b88e-6d81b0c07dfb)

---

## Category
- **Primary category:** Team Productivity
- **Secondary tags:** slack, meeting management, ai workflow, automation, collaboration, task tracking, composio, productivity
- This solution bridges the gap between real-time team communication and project management by automating the extraction and assignment of meeting outcomes.

---

## Who is this for?
This solution is designed for fast-moving teams that need to maintain momentum without the burden of manual administrative tasks.

- **Project Managers**
    - Automate the logging of meeting minutes and ensure no action item falls through the cracks.
- **Sales Leads**
    - Quickly capture client requirements from Slack discussions and sync them directly to the CRM.
- **Operations Managers**
    - Standardize meeting follow-up processes across distributed teams to improve operational hygiene.
- **Engineering Managers**
    - Convert technical sync discussions into structured tickets or tasks without leaving the chat interface.

---

## Features
- **Slack Integration**
    - Seamlessly ingest meeting transcripts or summary notes directly from Slack channels for instant processing.
- **AI-Powered Extraction**
    - Utilizes advanced LLMs to identify action items, owners, and deadlines from unstructured conversation data.
- **Composio Toolset Connectivity**
    - Connects to your existing project management and CRM tools to push updates automatically via the Composio platform.
- **Real-Time Sync**
    - Ensures that all stakeholders are updated immediately, maintaining a single source of truth for meeting outcomes.
- **Automated Notifications**
    - Triggers follow-up messages or task assignments in Slack, keeping the team accountable and informed.

---

## Use Cases
**Meeting Documentation**
- Automatically summarize hour-long team syncs into concise bullet points.
- Generate and distribute meeting minutes to all channel participants instantly.

**Action Item Management**
- Extract tasks from Slack threads and assign them to the correct team member.
- Sync identified action items to external project management tools like Jira or Asana.

**Pipeline & CRM Updates**
- Update opportunity stages based on meeting outcomes discussed in Slack.
- Log meeting notes directly into client profiles to maintain comprehensive account history.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Slack and Composio connections when prompted.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives meeting transcripts or summary notes from Slack.
- **Agent**: Analyzes text to extract action items, owners, and deadlines.
- **Composio Toolset**: Executes API calls to sync data with your preferred project management tools.
- **Chat Output**: Posts a confirmation summary and task list back to the Slack channel.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize the meeting notes from the last 30 minutes and create Jira tickets for all action items.`
- `Extract all follow-up tasks from this thread and assign them to the mentioned team members.`
- `Log the key decisions made in this meeting to the CRM account associated with this channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that parses natural language into structured data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate extraction.
- Provide clear instructions on identifying action items versus general discussion.
- Define the output schema to ensure task titles, owners, and due dates are formatted correctly.

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure authentication with your third-party apps.
- Define the connection scope to allow the agent to read/write to your specific project management or CRM tools.

### 3) Tool Availability
- **Slack API**: For reading messages and posting summaries.
- **Project Management Connectors**: (e.g., Jira, Asana, Trello) for task creation.
- **CRM Connectors**: (e.g., Salesforce, HubSpot) for updating account records.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Focuses on ranking and managing high-priority tasks.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for complex business processes.
- [24/7 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - Handles inbound support queries using similar Slack/AI integration patterns.
