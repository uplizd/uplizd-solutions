# Email Priority Sorter (Uplizd) - Intelligent Inbox Management and Triage

## Summary
The Email Priority Sorter is an AI-driven workflow that automatically scans, analyzes, and categorizes incoming emails based on urgency and context. By leveraging the Composio Toolset to interface with your email provider, the solution ensures that critical communications are surfaced immediately, reducing inbox clutter and significantly increasing response velocity for high-priority tasks.

---

## Demo
![Email Priority Sorter workflow dashboard showing automated email triage and categorization](image.png)
**Alt text (SEO-ready):** Email Priority Sorter workflow dashboard showing automated email triage, categorization, and AI-driven inbox management using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/18bfa656-0a0e-5c99-af6a-db7edc4bdecb)

---

## Category
**Primary category**: Operations  
**Secondary tags**: email, productivity, triage, automation, inbox management, composio, ai workflow, data organization  
This solution streamlines communication workflows by applying intelligent filtering to high-volume email traffic.

---

## Who is this for?
This solution is designed for professionals and teams looking to reclaim time spent on manual inbox management.

* **Executive Assistants**
    * Ensures VIP communications and urgent scheduling requests are never missed.
* **Customer Support Leads**
    * Automatically identifies and escalates critical support tickets requiring immediate human intervention.
* **Sales Representatives**
    * Prioritizes incoming lead inquiries and prospect follow-ups to maintain pipeline momentum.
* **Operations Managers**
    * Reduces noise by filtering out low-priority notifications and system alerts from daily workflows.

---

## Features
- **Contextual Urgency Scoring**
  Uses LLM analysis to assign priority levels based on sender intent, keywords, and historical interaction data.
- **Automated Labeling & Sorting**
  Directly interacts with your email client via Composio to move messages into designated priority folders or apply labels.
- **Real-time Triage Alerts**
  Triggers immediate notifications for emails flagged as "Urgent" to ensure rapid response times.
- **Customizable Logic Rules**
  Allows users to define specific criteria for what constitutes "High Priority" based on their unique business needs.
- **Seamless Integration**
  Connects natively with major email providers using the Composio Toolset for secure, authenticated access to your inbox.

---

## Use Cases
**Inbox Zero Optimization**
- Automatically archive or move newsletters and non-actionable updates to a "Read Later" folder.
- Consolidate fragmented threads into a single prioritized view for end-of-day review.

**Customer Response Management**
- Flag support emails containing negative sentiment or urgent keywords like "cancel" or "broken."
- Route high-value client inquiries directly to the account manager's primary inbox.

**Sales Lead Qualification**
- Identify and highlight emails from prospects expressing clear purchase intent or meeting requests.
- Filter out automated marketing blasts to keep the focus on active sales conversations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and import the Email Priority Sorter workflow.
3. Authenticate your email account within the Composio connection settings.
4. Ensure nodes are correctly mapped and the agent is linked to your email toolset.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger signal or manual request to scan the inbox.
* **Agent**: Analyzes email content against priority criteria and determines the appropriate action.
* **Composio Toolset**: Executes the read, label, or move operations within your email provider.
* **Chat Output**: Provides a summary report of the emails processed and actions taken.

### 3) Run the Flow
Use the Playground to test the flow with these prompts:
- `Scan my inbox for any emails from the last 2 hours that mention 'urgent' or 'immediate' and label them as High Priority.`
- `Move all newsletters and promotional emails received today to the 'Archive' folder.`
- `Summarize the most important emails from my primary inbox and list them by sender and urgency.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent filter, interpreting email intent and urgency.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Analyze the email body and subject line to determine if the message requires immediate action."
* Instruction: "Categorize messages into 'Urgent', 'Standard', or 'Low Priority' based on the sender's tone and request type."

### 2) Composio Toolset Node
* Provide your API key in the Composio configuration panel.
* Ensure the connection scope includes read, write, and label permissions for your email account.

### 3) Tool Availability
* `email_list_messages`: Retrieve recent emails for analysis.
* `email_update_label`: Apply priority tags to processed messages.
* `email_move_to_folder`: Organize emails into specific priority-based directories.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md): Focuses on extracting and organizing tasks from communications.
- [Customer Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md): Specializes in routing support tickets across messaging platforms.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md): Manages broader operational tasks beyond just email.
