# Team Achievement Celebrator (Uplizd) - Automated real-time recognition for team milestones

## Summary
The Team Achievement Celebrator is an automated Uplizd AI workflow designed to boost team morale and engagement by instantly broadcasting project wins, closed deals, and milestones directly into Slack. By leveraging the Composio Toolset to monitor performance data and trigger personalized celebratory messages, this solution eliminates manual recognition delays, ensuring every accomplishment is acknowledged immediately to foster a culture of appreciation and high performance.

---

## Demo
![Team Achievement Celebrator workflow showing Slack integration for automated milestone recognition](image.png)
**Alt text (SEO-ready):** Team Achievement Celebrator workflow showing Slack integration for automated milestone recognition, Uplizd AI automation, and team engagement tools.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7f5f3e71-8ec8-54a1-b0aa-236d4f767a0d)

---

## Category
**Primary category:** Team Operations
**Secondary tags:** slack, team engagement, recognition, automation, workflow, ai agent, composio, culture

This solution streamlines internal communications by automating the recognition of key performance indicators and team successes.

---

## Who is this for?
This workflow is designed for managers and operations leaders who want to maintain high team morale without manual administrative overhead.

- **Sales Managers**
    - Automate the celebration of closed-won deals to keep the sales floor energized and motivated.
- **HR & People Ops**
    - Ensure company-wide milestones and work anniversaries are recognized consistently across all departments.
- **Engineering Leads**
    - Automatically announce successful product deployments or sprint completions to keep stakeholders informed and engaged.
- **Community Managers**
    - Recognize top contributors or community milestones in real-time to foster a sense of belonging and achievement.

---

## Features
- **Real-time Slack Integration**
    - Automatically posts celebratory messages to designated channels the moment a milestone is reached.
- **Customizable Recognition Templates**
    - Tailor the tone, emojis, and formatting of messages to align with your company culture.
- **Intelligent Trigger Logic**
    - Uses the Composio Toolset to monitor specific data points in your CRM or project management tools to trigger celebrations.
- **Multi-Platform Data Sync**
    - Aggregates data from various sources to ensure no achievement goes unnoticed, regardless of where the work is tracked.
- **Automated Performance Tracking**
    - Keeps a log of celebrated achievements, providing insights into team velocity and milestone frequency.

---

## Use Cases
**Sales Performance Recognition**
- Trigger a "Big Win" announcement in Slack whenever a deal stage changes to "Closed Won" in your CRM.
- Send personalized shout-outs to individual sales representatives upon hitting monthly quota targets.

**Project Milestone Celebration**
- Automatically notify the team when a Jira ticket or project task is marked as "Completed" in the production environment.
- Celebrate the successful launch of new features by posting summaries of resolved issues directly to the engineering channel.

**Culture & Engagement**
- Recognize team members for work anniversaries or birthdays by pulling data from your HRIS and posting in the general channel.
- Broadcast positive customer feedback or 5-star reviews to the support team to boost morale after high-volume periods.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Team Achievement Celebrator template from the marketplace.
3. Connect your Slack workspace and relevant data sources (e.g., CRM or Project Management tools) via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input:** Receives the trigger event data from your integrated tools.
- **Agent:** Processes the achievement data and drafts a celebratory message based on your pre-defined style guide.
- **Composio Toolset:** Executes the API call to post the formatted message into the specified Slack channel.
- **Chat Output:** Confirms the successful delivery of the recognition message to the team.

### 3) Run the Flow
Use the Playground to test your triggers with these example prompts:
- `Celebrate the latest closed-won deal from Salesforce in the #sales-wins channel.`
- `Post a congratulatory message for the engineering team regarding the completion of the Q3 feature sprint.`
- `Draft a shout-out for Sarah for her 2-year work anniversary and send it to the #general channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative engine, transforming raw data into engaging, human-like recognition messages.
- **Tone:** Professional yet enthusiastic and inclusive.
- **Context:** Always include the specific achievement and the individual or team responsible.
- **Formatting:** Utilize Slack-compatible markdown (bolding, emojis) for maximum visibility.

### 2) Composio Toolset Node
Requires an active Slack API key with `chat:write` and `channels:read` scopes to ensure the agent can post messages to the correct locations.

### 3) Tool Availability
- **Slack API:** For posting messages, creating threads, and managing channel interactions.
- **CRM/Project Connectors:** For real-time data retrieval from platforms like Salesforce, HubSpot, or Jira.
- **Notification Manager:** To handle scheduling and frequency capping for high-volume milestone events.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor/README.md) - Tracks the operational status and efficiency of your automated workflows.
- [Account Relationship Builder](../account-relationship-builder/README.md) - Manages and strengthens client interactions through automated CRM updates.
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Streamlines the new hire process with automated task assignments and team introductions.
