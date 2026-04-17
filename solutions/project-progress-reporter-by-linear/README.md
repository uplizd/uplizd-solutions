# Project Progress Reporter (Uplizd) - Automated status reporting for Linear workflows

## Summary
The Project Progress Reporter is an intelligent Uplizd workflow that synthesizes real-time data from Linear into comprehensive, stakeholder-ready status reports. By automating the extraction and summarization of project milestones, blockers, and velocity metrics, this solution eliminates manual reporting overhead, ensuring project managers and engineering leads maintain a single source of truth with minimal effort.

---

## Demo
![Project Progress Reporter workflow dashboard showing Linear data integration and automated report generation](image.png)
**Alt text (SEO-ready):** Project Progress Reporter Uplizd workflow showing Linear data integration, automated status reporting, and project management analytics.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3d8698b3-b2a1-5c85-9b4a-82a90d65447b)

---

## Category
- **Primary category:** Project Management
- **Secondary tags:** linear, project reporting, status updates, engineering velocity, automation, workflow, composio, ai agent
- This solution streamlines project oversight by connecting Linear data directly to AI-driven reporting pipelines.

---

## Who is this for?
This solution is designed for teams looking to reduce administrative reporting friction and improve transparency across the software development lifecycle.

- **Engineering Managers**
    - Automate weekly status updates to stakeholders without manual data gathering.
- **Project Managers**
    - Identify project bottlenecks and stalled tasks in real-time across multiple Linear cycles.
- **Product Owners**
    - Maintain clear visibility into feature progress and sprint velocity for roadmap planning.
- **Team Leads**
    - Ensure consistent reporting standards across distributed squads using standardized report templates.

---

## Features
- **Automated Data Extraction**
    - Seamlessly pulls cycle, project, and issue data from Linear via the Composio Toolset.
- **Intelligent Summarization**
    - Uses LLM-based analysis to convert raw ticket data into clear, narrative-driven progress reports.
- **Blocker Identification**
    - Automatically flags high-priority blockers or overdue tasks that require immediate attention.
- **Customizable Report Templates**
    - Tailor the tone and structure of reports to suit executive, technical, or client-facing audiences.
- **Real-time Sync**
    - Ensures reports are generated based on the most current state of your Linear workspace.

---

## Use Cases
**Weekly Stakeholder Updates**
- Generate executive summaries of sprint progress every Friday afternoon.
- Aggregate completed tasks and upcoming milestones for cross-departmental visibility.

**Project Health Monitoring**
- Detect "at-risk" projects by analyzing issue status trends and cycle velocity.
- Provide automated alerts when project scope shifts significantly during a sprint.

**Sprint Retrospective Preparation**
- Compile a list of completed issues and velocity metrics to facilitate data-driven retrospectives.
- Highlight recurring themes or common blockers identified across multiple project cycles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project environment for the import.
3. Authenticate your Linear account via the Composio connection prompt.
4. Ensure nodes are correctly mapped and the API credentials for Linear are active.

### 2) Setup the Nodes
- **Chat Input:** Accepts the project name or cycle ID for the report.
- **Agent:** Processes the request and orchestrates the data retrieval logic.
- **Composio Toolset:** Executes secure API calls to fetch Linear project data.
- **Chat Output:** Delivers the formatted project status report to the user.

### 3) Run the Flow
Use the Playground to test your reports with prompts like:
- `Generate a status report for the Q3 Mobile App project.`
- `What are the current blockers for the API migration cycle?`
- `Summarize the progress and velocity for the last two weeks of the Design System project.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a project analyst that interprets Linear data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate summarization.
- Instruct the agent to prioritize "Blockers" and "Upcoming Milestones" in the output.
- Maintain a professional, concise tone suitable for project reporting.

### 2) Composio Toolset Node
- Provide your Linear API key within the Composio dashboard.
- Set the connection scope to allow read access to `issues`, `projects`, and `cycles`.

### 3) Tool Availability
- `linear_get_project`: Fetches high-level project metadata.
- `linear_list_issues`: Retrieves specific task status and assignee details.
- `linear_get_cycle`: Pulls time-bound sprint data for velocity analysis.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track overall team productivity and workflow efficiency.
- [Account Mapping Agent](../account-mapping-agent-by-bigpicture-io/README.md) - Visualize complex project dependencies and account structures.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks based on project urgency.
