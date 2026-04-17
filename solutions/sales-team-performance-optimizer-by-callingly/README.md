# Sales Team Performance Optimizer (Uplizd) - Automate agent scheduling and drive sales velocity

## Summary
The Sales Team Performance Optimizer is an intelligent Uplizd workflow designed to streamline sales operations by automating agent scheduling, performance tracking, and activity management. By integrating real-time data from Callingly and your CRM, this solution provides a single source of truth for team capacity, reduces administrative overhead, and ensures high-priority leads are always handled by the most available and qualified representative.

---

## Demo
![Sales Team Performance Optimizer workflow interface showing automated scheduling nodes and CRM integration](image.png)
**Alt text (SEO-ready):** Uplizd Sales Team Performance Optimizer workflow, automated agent scheduling, CRM sales pipeline management, and performance tracking integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/284bb48c-1f81-50b6-ab72-f97d60123db6)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales, crm, scheduling, performance, pipeline, callingly, composio, ai workflow
- This solution bridges the gap between raw lead data and actionable team performance metrics to optimize daily sales output.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate scheduling bottlenecks and maximize agent productivity.

- **Sales Managers**
    - Gain real-time visibility into agent availability and individual performance metrics.
- **RevOps Specialists**
    - Automate the distribution of leads based on current team capacity and historical success rates.
- **Account Executives**
    - Reduce time spent on manual scheduling and focus on high-value prospect interactions.
- **Sales Development Reps (SDRs)**
    - Receive optimized lead assignments that align with active work hours and skill sets.

---

## Features
- **Automated Scheduling**
    - Syncs agent availability with incoming lead volume to ensure instant response times via Callingly.
- **Performance Analytics**
    - Tracks key performance indicators (KPIs) and agent activity logs to identify coaching opportunities.
- **CRM Integration**
    - Seamlessly updates lead status and activity history in your CRM using the Composio Toolset.
- **Dynamic Lead Routing**
    - Routes prospects to the most qualified agent based on real-time workload and historical conversion data.
- **Proactive Alerts**
    - Triggers notifications for stalled deals or missed follow-ups to maintain pipeline hygiene.

---

## Use Cases
**Lead Response Optimization**
- Automatically trigger a call through Callingly the moment a high-intent lead is captured in your CRM.
- Route leads to available agents based on current time-zone and active status.

**Team Capacity Management**
- Monitor agent workload in real-time to prevent burnout and ensure balanced lead distribution.
- Adjust scheduling parameters dynamically based on daily team performance reports.

**Pipeline Hygiene**
- Automatically log all call outcomes and follow-up tasks back into the CRM to keep records accurate.
- Identify and re-assign leads that have not been contacted within a specified SLA window.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your dashboard.
3. Connect your CRM and Callingly accounts via the Composio Toolset configuration.
4. Ensure nodes are correctly mapped and all API credentials are saved in the environment settings.

### 2) Setup the Nodes
- **Chat Input**: Receives lead triggers or manual performance report requests.
- **Agent**: Processes scheduling logic, analyzes performance data, and determines the next best action.
- **Composio Toolset**: Executes API calls to Callingly for dialing and your CRM for data updates.
- **Chat Output**: Delivers confirmation of scheduled calls or summary reports of team performance.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Schedule a follow-up call for the latest high-priority lead in the CRM.`
- `Generate a performance summary for the sales team for the last 7 days.`
- `Check current agent availability and assign the next 5 incoming leads.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, interpreting CRM data and scheduling constraints.
- Use a model capable of structured reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a Sales Operations Assistant. Analyze CRM lead data and agent availability to optimize scheduling."
- Instruction: "Prioritize leads based on conversion probability and ensure all actions are logged in the CRM."

### 2) Composio Toolset Node
- Provide your **Composio API Key** in the node settings.
- Ensure the connection scope includes read/write access to your CRM (e.g., Salesforce, HubSpot) and Callingly.

### 3) Tool Availability
- **CRM Connector**: For fetching lead details and updating activity logs.
- **Callingly API**: For initiating automated outbound calls and managing agent queues.
- **Calendar/Scheduling Tools**: For cross-referencing agent availability windows.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate prospect intelligence gathering.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and stalled opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain multi-platform data consistency.
