# Recurring Meeting Optimizer (Uplizd) - Streamline calendar efficiency and meeting ROI

## Summary
The Recurring Meeting Optimizer is an intelligent Uplizd AI workflow designed to audit, evaluate, and refine your calendar habits. By connecting directly to your Google Calendar via the Composio Toolset, this solution identifies low-value recurring events, suggests consolidation opportunities, and automates the pruning of redundant syncs, helping teams reclaim focus time and improve overall operational velocity.

---

## Demo
![Recurring Meeting Optimizer dashboard showing calendar audit results and optimization suggestions](image.png)
**Alt text (SEO-ready):** Recurring Meeting Optimizer dashboard showing calendar audit results and optimization suggestions for Uplizd AI workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1e0bf605-62dc-599e-ae4f-a59a35000490)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** google calendar, meeting management, productivity, time optimization, workflow automation, calendar hygiene, composio, ai assistant
- This solution transforms calendar management from a passive administrative task into a proactive strategy for maximizing team productivity.

---

## Who is this for?
This solution is designed for professionals and team leaders looking to eliminate meeting fatigue and regain control over their daily schedules.

- **Operations Manager**
    - Identifies and eliminates redundant recurring meetings to boost team output.
- **Executive Assistant**
    - Automates the audit of executive calendars to ensure high-value time allocation.
- **Engineering Lead**
    - Protects "deep work" blocks by consolidating fragmented syncs into efficient sessions.
- **Project Manager**
    - Monitors meeting attendance and relevance to optimize stakeholder time investment.

---

## Features
- **Intelligent Audit**
    - Scans recurring calendar events to detect patterns of low attendance or lack of clear agendas.
- **Consolidation Engine**
    - Suggests merging overlapping or similar-topic meetings to reduce context switching.
- **Composio Integration**
    - Leverages secure Google Calendar API connectivity to read and modify event metadata in real-time.
- **Automated Cleanup**
    - Provides one-click actions to cancel or reschedule meetings based on AI-driven value scoring.
- **Focus Time Protection**
    - Automatically identifies and preserves deep work blocks by flagging conflicting recurring syncs.

---

## Use Cases
**Meeting Hygiene**
- Automatically flagging recurring meetings that have had low attendance over the last 30 days.
- Identifying "zombie" meetings that lack a recurring agenda or description.

**Calendar Optimization**
- Consolidating three separate 30-minute status updates into a single, high-impact 45-minute session.
- Rescheduling recurring meetings that consistently conflict with high-priority project deadlines.

**Operational Efficiency**
- Analyzing meeting frequency across departments to ensure alignment with current project goals.
- Generating weekly reports on time spent in recurring meetings to identify potential cost savings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Connect your Google Calendar account via the Composio Toolset integration.
3. Review the pre-configured Agent instructions to tailor the optimization logic to your team's culture.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's request to audit or optimize specific calendar segments.
- **Agent**: Processes calendar data, evaluates meeting value, and generates optimization recommendations.
- **Composio Toolset**: Executes read/write operations on Google Calendar to fetch events and apply changes.
- **Chat Output**: Displays the audit summary and actionable buttons to confirm meeting adjustments.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Audit my calendar for the next two weeks and identify recurring meetings with low attendance.`
- `Find all recurring meetings that overlap with my focus time and suggest new slots.`
- `Consolidate my team's daily standups into a single bi-weekly sync.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a calendar strategist, balancing meeting necessity against team availability.
- Instruct the agent to prioritize "Deep Work" blocks.
- Define a threshold for "low value" (e.g., meetings with fewer than 3 participants).
- Maintain a neutral, helpful tone when suggesting cancellations to stakeholders.

### 2) Composio Toolset Node
- Provide your Google Calendar API credentials within the Composio dashboard.
- Ensure the connection scope includes `calendar.events.readonly` and `calendar.events` for modification capabilities.

### 3) Tool Availability
- `list_events`: Fetches recurring event series for analysis.
- `get_event_details`: Retrieves participant lists and meeting descriptions.
- `update_event`: Modifies time slots or cancels meetings based on user approval.
- `create_event`: Schedules consolidated meetings.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the efficiency of your automated processes.
- [Workspace Setup Optimizer](../workspace-setup-optimizer-by-clockify/README.md) — Align your time-tracking and workspace habits.
- [Work Hours Compliance Monitor](../work-hours-compliance-monitor-by-timely/README.md) — Ensure meeting schedules align with healthy work-life balance.
