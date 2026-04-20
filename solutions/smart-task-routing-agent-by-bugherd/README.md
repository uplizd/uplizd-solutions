# Smart Task Routing Agent (Uplizd) - Automate bug assignment and team workload balancing

## Summary
The Smart Task Routing Agent leverages AI to analyze incoming bug reports from BugHerd and automatically route them to the most qualified team member based on technical expertise and current capacity. This workflow eliminates manual triage bottlenecks, ensures accountability, and significantly reduces the time-to-resolution for critical product issues.

---

## Demo
![Smart Task Routing Agent workflow diagram showing BugHerd integration and AI-driven assignment](image.png)
**Alt text (SEO-ready):** Smart Task Routing Agent workflow for BugHerd, featuring AI-powered task assignment, team capacity management, and automated issue triage on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/168d44cc-bc6f-579c-b5ac-83ceb6554b1b)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** bugherd, task routing, workflow automation, bug tracking, team management, ai agent, composio, incident management
- This solution streamlines technical operations by connecting issue tracking platforms with intelligent routing logic to optimize team productivity.

---

## Who is this for?
This agent is designed for engineering and product teams looking to scale their issue management processes without increasing administrative overhead.

- **Engineering Managers**
    - Gain visibility into team bandwidth and ensure critical bugs are assigned to the right specialists immediately.
- **Product Managers**
    - Accelerate the feedback loop by ensuring bug reports are categorized and routed to developers without manual intervention.
- **QA Leads**
    - Maintain high product quality by automating the distribution of incoming bug reports to the appropriate feature owners.
- **Support Operations**
    - Reduce ticket backlog by automating the triage process and minimizing the time bugs spend in an unassigned state.

---

## Features
- **Intelligent Routing Logic**
    - Maps incoming bug reports to specific developers based on historical performance and technical domain expertise.
- **Real-time BugHerd Integration**
    - Connects directly to BugHerd to pull new tasks and push assignment updates instantly via the Composio Toolset.
- **Capacity-Aware Assignment**
    - Evaluates current developer workloads before routing new tasks to prevent burnout and ensure balanced distribution.
- **Automated Priority Scoring**
    - Analyzes bug descriptions to automatically set priority levels, ensuring urgent issues are flagged for immediate attention.
- **Workflow Transparency**
    - Provides detailed logs of why a task was routed to a specific individual, maintaining auditability across the development lifecycle.

---

## Use Cases
**Automated Bug Triage**
- Automatically route frontend-specific bugs to the UI/UX development team.
- Flag critical security vulnerabilities for immediate review by the lead security engineer.

**Workload Balancing**
- Distribute incoming tasks evenly across the engineering team based on current ticket counts.
- Re-assign tasks automatically if a developer marks themselves as out-of-office or at capacity.

**Incident Escalation**
- Escalate unresolved bugs to senior engineering staff if they remain unassigned for more than 24 hours.
- Notify the project manager via Slack or email when high-priority bugs are successfully routed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your BugHerd account within the Composio connection settings.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the new bug report data from the BugHerd webhook.
- **Agent**: Processes the bug details and determines the best assignee based on the provided instructions.
- **Composio Toolset**: Executes the API call to update the assignee field in BugHerd.
- **Chat Output**: Confirms the successful routing and assignment back to the user.

### 3) Run the Flow
Use the Playground to test your routing logic with these example prompts:
- `Route the latest unassigned bug in the 'Mobile App' project to the most available developer.`
- `Analyze the bug description 'Login button unresponsive' and assign it to the frontend team lead.`
- `Check current workload for all developers and assign the critical bug #402 to the least busy member.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent decision-maker for task distribution.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide a clear list of team members and their specific technical domains.
- Define the threshold for "overloaded" capacity to ensure the agent routes tasks effectively.

### 2) Composio Toolset Node
- Provide your BugHerd API key to enable read/write access to your projects.
- Set the connection scope to allow the agent to read tasks and update assignment fields.

### 3) Tool Availability
- `bugherd_get_tasks`: Fetches the list of new or unassigned bugs.
- `bugherd_update_task`: Updates the assignee and priority fields on the platform.
- `bugherd_list_team`: Retrieves current team member availability and project roles.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automatically rank and prioritize incoming tasks and action items.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose automation for streamlining complex business workflows.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gather and synthesize account intelligence to inform task routing decisions.
