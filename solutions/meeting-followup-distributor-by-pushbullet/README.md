# Meeting Follow-up Distributor (Uplizd) - Automated cross-device synchronization for meeting action items

## Summary
The Meeting Follow-up Distributor is an intelligent Uplizd workflow designed to streamline post-meeting productivity by automatically capturing, summarizing, and broadcasting action items across all your connected devices via Pushbullet. By centralizing meeting intelligence, this solution ensures that critical tasks are never missed, reducing manual data entry and keeping stakeholders aligned regardless of their current platform or location.

---

## Demo
![Workflow diagram showing meeting notes flowing from Chat Input through an Agent to Pushbullet for cross-device distribution](image.png)
**Alt text (SEO-ready):** Uplizd workflow for meeting follow-up distribution, automating action item syncing across devices using Pushbullet and AI-driven task extraction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8bea55a9-bec3-5f4e-983b-35acd1f0141f)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meeting, productivity, pushbullet, automation, task management, sync, composio, ai workflow
- This solution bridges the gap between meeting documentation and task execution by leveraging AI to push actionable insights directly to your personal and professional devices.

---

## Who is this for?
This solution is built for professionals and teams who need to maintain high velocity after meetings without manual administrative overhead.

- **Project Managers**
    - Ensure that action items are instantly pushed to all team devices, preventing task slippage.
- **Sales Representatives**
    - Automatically sync follow-up tasks to mobile devices to stay responsive while on the move.
- **Executive Assistants**
    - Streamline the distribution of meeting summaries to leadership across multiple platforms.
- **Remote Team Leads**
    - Maintain operational transparency by broadcasting meeting outcomes to distributed team members.

---

## Features
- **Intelligent Summarization**
    - Uses advanced LLMs to parse raw meeting transcripts into concise, actionable task lists.
- **Cross-Device Sync**
    - Leverages the Pushbullet integration to broadcast notifications and notes to all linked devices simultaneously.
- **Composio Toolset Integration**
    - Seamlessly connects your meeting data sources with the Pushbullet API for automated task delivery.
- **Real-time Processing**
    - Executes the distribution logic immediately upon input, ensuring zero latency in task assignment.
- **Customizable Formatting**
    - Allows for tailored output templates to match your team's specific documentation style.

---

## Use Cases
**Meeting Documentation**
- Automatically extract action items from Zoom or Google Meet transcripts.
- Convert unstructured conversation logs into clean, bulleted task lists.

**Team Alignment**
- Push high-priority tasks to the devices of relevant stakeholders post-meeting.
- Sync meeting summaries to shared device environments for instant team visibility.

**Personal Productivity**
- Send meeting reminders directly to your mobile device to ensure timely follow-ups.
- Consolidate action items from multiple meetings into a single daily digest notification.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your Pushbullet API credentials within the Composio Toolset node.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Accepts raw meeting transcripts or notes.
- **Agent**: Processes the text to identify and prioritize action items.
- **Composio Toolset**: Executes the push notification command via Pushbullet.
- **Chat Output**: Confirms successful distribution to the target devices.

### 3) Run the Flow
Use the Playground to test the distribution logic:
- `Summarize this meeting transcript and push the action items to my devices.`
- `Extract tasks from the following notes and send them via Pushbullet: [Insert Notes]`
- `Create a high-priority alert for the action items identified in this meeting.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent is configured to act as a precision-focused administrative assistant.
- Focus on extracting clear, time-bound action items.
- Maintain a professional and concise tone for all notifications.
- Prioritize tasks based on urgency and stakeholder mentions.

### 2) Composio Toolset Node
- Requires a valid Pushbullet API key to authenticate and send notifications.
- Connection scope should be set to allow "Push" and "Device Management" permissions.

### 3) Tool Availability
- **Pushbullet API**: For sending notes, links, and task lists to connected devices.
- **Text Processing Utilities**: For cleaning and formatting meeting transcripts.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and rank tasks extracted from meeting notes.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate multi-step business processes following meeting conclusions.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - Manage support tickets and follow-ups derived from customer interactions.
