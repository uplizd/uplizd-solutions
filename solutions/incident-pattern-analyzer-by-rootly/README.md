# Incident Pattern Analyzer (Uplizd) - Automate root cause discovery and incident trend reporting

## Summary
The Incident Pattern Analyzer (Uplizd) is an intelligent workflow designed to ingest, categorize, and analyze incident data from Rootly to identify recurring technical bottlenecks. By automating the extraction of action items and mapping them against historical incident logs, this solution provides engineering teams with a single source of truth for system reliability, significantly reducing the time spent on manual post-mortem analysis and improving overall pipeline velocity.

---

## Demo
![Incident Pattern Analyzer workflow diagram showing Rootly data ingestion, AI-driven pattern recognition, and automated report generation](image.png)
**Alt text (SEO-ready):** Incident Pattern Analyzer (Uplizd) workflow diagram for automated root cause analysis, Rootly incident data processing, and technical trend reporting.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/49742071-c137-5831-8075-748abf3d2118)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** incident management, rootly, devops, root cause analysis, automation, ai workflow, composio, reliability engineering
- This solution streamlines the incident management lifecycle by transforming raw Rootly data into actionable reliability insights.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to move from reactive firefighting to proactive system optimization.

- **Site Reliability Engineer (SRE)**
    - Automates the identification of recurring failure modes to prioritize long-term system stability.
- **Engineering Manager**
    - Gains visibility into team bandwidth consumption caused by repetitive technical debt and incident remediation.
- **DevOps Lead**
    - Standardizes the post-mortem process by ensuring action items are consistently categorized and tracked.
- **Incident Commander**
    - Quickly surfaces historical context during active incidents to prevent repeat occurrences of known issues.

---

## Features
- **Automated Rootly Integration**
    - Seamlessly pulls incident logs and action items directly from Rootly using the Composio Toolset.
- **Pattern Recognition Engine**
    - Uses advanced LLM analysis to group similar incident descriptions and identify common root causes.
- **Action Item Prioritization**
    - Automatically flags high-frequency action items that contribute most to system downtime.
- **Real-time Trend Reporting**
    - Generates concise summaries of incident patterns, allowing for data-driven decision-making in sprint planning.
- **Contextual Knowledge Base**
    - Builds a searchable index of historical incidents, enabling faster resolution for future similar events.

---

## Use Cases
**Post-Mortem Analysis**
- Automatically summarize incident threads to extract key learning points for team reviews.
- Identify the most common "human error" vs. "system failure" patterns across the last 90 days.

**Technical Debt Reduction**
- Aggregate recurring action items to justify engineering time for infrastructure refactoring.
- Track the effectiveness of implemented fixes by monitoring the reduction of specific incident patterns over time.

**Operational Efficiency**
- Reduce the time spent by SREs on manual data entry and incident categorization.
- Provide stakeholders with automated, high-level reports on system health and incident frequency.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your dashboard.
3. Connect your Rootly account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the time range or specific incident IDs to analyze.
- **Agent**: Processes the incident data to identify recurring patterns and trends.
- **Composio Toolset**: Executes API calls to fetch incident logs and action items from Rootly.
- **Chat Output**: Displays the final analysis report and recommended action items.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Analyze all incidents from the last 30 days and list the top 3 recurring patterns.`
- `Identify any action items in Rootly that have been marked as 'pending' for more than 2 weeks.`
- `Generate a summary of the most frequent root causes for incidents involving our payment gateway.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a technical analyst, synthesizing raw logs into structured insights.
- **Instruction Pattern:**
    - Focus on identifying recurring themes in incident descriptions.
    - Prioritize action items that appear across multiple incident tickets.
    - Maintain a professional, objective tone suitable for engineering leadership.

### 2) Composio Toolset Node
- Requires a valid Rootly API key configured within the Composio dashboard.
- Ensure the connection scope includes read access to `incidents`, `action_items`, and `post_mortems`.

### 3) Tool Availability
- `rootly_get_incidents`: Fetches historical incident logs.
- `rootly_get_action_items`: Retrieves pending and completed remediation tasks.
- `rootly_search_post_mortems`: Searches through past incident documentation for keyword-based patterns.

---

## Related Solutions
- [../action-item-cleanup-agent-by-rootly/README.md](../action-item-cleanup-agent-by-rootly/README.md) — Automate the cleanup and status tracking of stale action items.
- [../action-item-prioritizer-by-rootly/README.md](../action-item-prioritizer-by-rootly/README.md) — Rank and prioritize incident action items based on business impact.
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) — Monitor the overall health and efficiency of your team's operational workflows.
