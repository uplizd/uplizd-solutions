# Email to Task Converter (Uplizd) - Automate email-to-task workflows with smart categorization

## Summary
The Email to Task Converter (Uplizd) is an intelligent automation workflow that bridges the gap between your inbox and project management tools. By leveraging AI to parse incoming emails, this solution extracts key details, determines priority, and creates structured tasks in TickTick, ensuring that critical action items are never lost in the noise of daily communication.

---

## Demo
![Email to Task Converter workflow diagram showing email parsing and task creation in TickTick](image.png)
**Alt text (SEO-ready):** Email to Task Converter workflow using Uplizd, AI-powered email parsing, TickTick task management, and automated task synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8d7a0d60-1551-502e-9374-000957b93cce)

---

## Category
- **Primary category:** Productivity automation
- **Secondary tags:** email, ticktick, task management, ai workflow, productivity, automation, composio, data sync
- This solution streamlines personal and professional task management by converting unstructured email communication into organized, actionable project items.

---

## Who is this for?
This solution is designed for professionals and teams looking to reduce manual data entry and improve task visibility.

- **Project Managers**
    - Automatically convert client requests and project updates into tracked tasks without manual copy-pasting.
- **Executive Assistants**
    - Efficiently triage high-volume inboxes and ensure leadership priorities are captured in the team's task manager.
- **Freelancers**
    - Maintain a single source of truth for client deliverables and deadlines by syncing email communications directly to TickTick.
- **Operations Leads**
    - Standardize the intake process for internal support requests by transforming email tickets into structured, assignable tasks.

---

## Features
- **Intelligent Parsing**
    - Uses advanced LLMs to extract task titles, descriptions, and deadlines from unstructured email bodies.
- **TickTick Integration**
    - Seamlessly connects with the Composio Toolset to create, update, and organize tasks within your specific TickTick lists.
- **Smart Prioritization**
    - Automatically assigns priority levels based on keywords, sender importance, or urgency detected within the email content.
- **Context Preservation**
    - Attaches original email metadata or links to the generated task, ensuring full context is available during execution.
- **Real-time Sync**
    - Operates as a continuous workflow, processing incoming emails the moment they arrive to keep your task list current.

---

## Use Cases
**Project Intake Management**
- Automatically create tasks from project requirement emails sent by stakeholders.
- Map email subject lines to task titles and body content to task descriptions in TickTick.

**Client Communication Tracking**
- Convert client feedback emails into follow-up tasks to ensure no request is overlooked.
- Set due dates for tasks based on time-sensitive language found within client correspondence.

**Personal Productivity**
- Transform "to-do" style emails into organized tasks to clear your inbox faster.
- Categorize tasks into specific TickTick lists (e.g., "Work," "Personal," "Urgent") based on email context.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Email to Task Converter template from the marketplace.
3. Authenticate your TickTick account via the Composio connection prompt.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw email content or trigger payload.
- **Agent**: Analyzes the text to extract actionable task data and intent.
- **Composio Toolset**: Executes the API call to create the task in TickTick.
- **Chat Output**: Confirms successful task creation or flags errors for review.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Create a task in TickTick from this email: "Please finish the Q3 report by Friday."`
- `Extract the task from this message and set priority to High: "Urgent: Review the new design mockups."`
- `Convert this email into a task titled 'Client Meeting Prep' and add it to my Work list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligence layer, transforming unstructured text into structured JSON for the TickTick API.
- **Instruction Pattern:**
    - Extract the task title, description, and due date from the provided email text.
    - If no due date is found, default to the next business day.
    - Map the extracted data to the required fields for the TickTick task creation tool.

### 2) Composio Toolset Node
- **API Key:** Ensure your TickTick API key is configured within the Composio dashboard.
- **Connection Scope:** Grant the agent permission to "Create Tasks" and "Read Lists" to ensure proper routing.

### 3) Tool Availability
- `ticktick_create_task`: Primary function for generating new items.
- `ticktick_list_folders`: Used to identify the correct list for task placement.
- `ticktick_update_task`: Optional capability for modifying existing tasks based on follow-up emails.

---

## Related Solutions
- [../action-item-prioritizer-by-rootly/README.md](../action-item-prioritizer-by-rootly/README.md) - Prioritize and manage action items across your infrastructure.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Automate complex business workflows and task handoffs.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize data across platforms to maintain a single source of truth.
