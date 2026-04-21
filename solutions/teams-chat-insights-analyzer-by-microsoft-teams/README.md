# Teams Chat Insights Analyzer (Uplizd) - Extract actionable intelligence and follow-ups from Microsoft Teams

## Summary
The Teams Chat Insights Analyzer is an automated Uplizd workflow designed to process, summarize, and extract actionable follow-ups from Microsoft Teams conversations. By leveraging the Composio Toolset to interface directly with communication threads, this solution enables teams to maintain pipeline velocity, ensure no task is overlooked, and transform unstructured chat data into a single source of truth for project management and sales operations.

---

## Demo
![Teams Chat Insights Analyzer workflow interface showing chat extraction and analysis nodes](image.png)
**Alt text (SEO-ready):** Uplizd Teams Chat Insights Analyzer workflow showing automated conversation analysis, Microsoft Teams integration, and Composio toolset processing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/56974f15-3aa8-5ff5-b2fb-74dfff9941d3)

---

## Category
- **Primary category:** Communication Operations
- **Secondary tags:** microsoft teams, chat analysis, workflow automation, composio, ai agent, data extraction, productivity, collaboration
- This solution bridges the gap between fragmented team discussions and structured project management by automating the extraction of key insights from Microsoft Teams.

---

## Who is this for?
This workflow is designed for teams looking to eliminate manual note-taking and improve accountability in digital workspaces.

- **Project Managers**
    - Automatically capture action items and deadlines from daily stand-up chats.
- **Sales Representatives**
    - Sync client sentiment and key requirements from Teams discussions directly into CRM records.
- **Operations Leads**
    - Monitor team communication for bottlenecks and recurring process friction points.
- **Customer Success Managers**
    - Identify urgent support requests or escalation signals buried in long conversation threads.

---

## Features
- **Automated Thread Summarization**
    - Uses advanced LLMs to condense long-form Teams discussions into concise, executive-level summaries.
- **Action Item Extraction**
    - Automatically identifies tasks, owners, and due dates mentioned within chat messages.
- **Composio-Powered Integration**
    - Seamlessly connects with Microsoft Teams APIs to pull real-time conversation data without manual export.
- **Context-Aware Analysis**
    - Maintains conversation history to ensure that follow-up tasks are attributed to the correct project or client.
- **Structured Output Generation**
    - Formats extracted insights into standardized reports ready for ingestion by project management tools.

---

## Use Cases
**Meeting Follow-up Management**
- Automatically generate a list of action items after a project sync meeting in Teams.
- Email or post a summary of decisions made to the relevant project channel.

**Sales Intelligence Gathering**
- Extract prospect pain points and feature requests from pre-sales chat discussions.
- Update CRM opportunity notes with key intelligence gathered during team brainstorming sessions.

**Operational Efficiency Tracking**
- Identify recurring support issues or technical blockers mentioned in engineering chat channels.
- Aggregate team feedback on new process rollouts to identify areas for improvement.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Solution."
2. Upload the `teams-chat-insights-analyzer` configuration file.
3. Authenticate your Microsoft Teams account via the Composio connection prompt.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Define the target Teams channel or thread ID for analysis.
- **Agent**: Configure the prompt instructions to focus on task extraction and sentiment analysis.
- **Composio Toolset**: Enable the Microsoft Teams connector to allow the agent to read and parse messages.
- **Chat Output**: Direct the summarized insights to a Slack channel, email, or project management board.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Analyze the last 50 messages in the 'Project Alpha' channel and list all pending action items.`
- `Summarize the conversation regarding the Q3 roadmap and highlight any disagreements or blockers.`
- `Extract all customer feedback mentioned in the 'Support-Escalations' channel from the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, parsing raw text into structured data.
- **Instruction Pattern**: Focus on identifying specific task-related keywords (e.g., "due," "assign," "fix").
- **Instruction Pattern**: Maintain a neutral, professional tone for all summaries.
- **Instruction Pattern**: Prioritize urgency when flagging action items for the user.

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and authorized for Microsoft Teams read-access.
- **Connection Scope**: Grant permissions for `Channel.ReadBasic.All` and `Chat.Read` to ensure the agent can access relevant conversation history.

### 3) Tool Availability
- **Teams Message Fetcher**: Retrieves raw text from specified channels.
- **Thread Context Parser**: Maintains the relationship between messages in a thread.
- **Action Item Formatter**: Converts natural language tasks into JSON or Markdown tables.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support response and ticket management.
- [action-item-cleanup-agent-by-rootly](../action-item-cleanup-agent-by-rootly/README.md) - Streamline and resolve incident-related action items.
- [workflow-health-monitor-by-dailybot](../workflow-health-monitor-by-dailybot/README.md) - Monitor team productivity and workflow bottlenecks.
