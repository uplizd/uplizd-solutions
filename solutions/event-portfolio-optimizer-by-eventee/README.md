# Event Portfolio Optimizer (Uplizd) - Maximize speaker impact and resource allocation across your event portfolio

## Summary
The Event Portfolio Optimizer is an intelligent Uplizd workflow designed to streamline speaker management and resource distribution across multiple events. By leveraging AI to analyze speaker performance, availability, and audience engagement metrics, the solution provides a single source of truth for event planners, ensuring optimal scheduling and maximizing the ROI of your event portfolio.

---

## Demo
![Event Portfolio Optimizer dashboard showing speaker allocation metrics and event scheduling insights](image.png)
**Alt text (SEO-ready):** Event Portfolio Optimizer dashboard showing speaker allocation metrics, event scheduling insights, Uplizd AI workflow, and Eventee integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3f6c3824-2e24-5b36-9e49-acdfce46e340)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** event management, speaker coordination, resource optimization, eventee, ai workflow, portfolio management, scheduling, automation
- This solution bridges the gap between complex event logistics and data-driven decision-making to improve overall event portfolio performance.

---

## Who is this for?
This solution is designed for professionals managing multi-event calendars who need to balance speaker quality with logistical constraints.

- **Event Manager**
    - Streamlines the speaker booking process and reduces manual scheduling conflicts across multiple venues.
- **Operations Director**
    - Gains high-level visibility into speaker utilization rates and portfolio-wide resource efficiency.
- **Content Strategist**
    - Ensures the right speakers are aligned with specific event themes to maximize audience engagement.
- **Speaker Coordinator**
    - Automates communication and status tracking for speakers, ensuring all requirements are met before event day.

---

## Features
- **Automated Speaker Matching**
    - Uses AI to suggest the best speakers for specific event themes based on historical performance data.
- **Portfolio-Wide Scheduling**
    - Synchronizes speaker availability across your entire event calendar to prevent double-booking.
- **Performance Analytics Integration**
    - Pulls engagement metrics from Eventee to score speaker effectiveness and inform future booking decisions.
- **Real-time Conflict Resolution**
    - Automatically detects scheduling overlaps and suggests alternative slots or speakers using the Composio Toolset.
- **Resource Allocation Tracking**
    - Monitors travel and logistical costs associated with speakers to keep your event portfolio within budget.

---

## Use Cases
**Strategic Speaker Placement**
- Matching high-impact speakers with keynote slots based on historical audience sentiment scores.
- Identifying underutilized speakers for smaller breakout sessions to increase their portfolio exposure.

**Operational Efficiency**
- Automating the outreach and confirmation process for speakers across 10+ annual events.
- Syncing speaker bios and headshots directly from your CRM into the Eventee platform.

**Portfolio Performance Review**
- Generating quarterly reports on speaker engagement trends to optimize future event spend.
- Analyzing speaker "churn" and availability gaps to improve long-term recruitment strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your Eventee and relevant CRM accounts via the Composio Toolset.
3. Configure the **Chat Input** node to accept your event parameters.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives event details, speaker requirements, and portfolio constraints.
- **Agent**: Processes scheduling logic, evaluates speaker metrics, and makes optimization decisions.
- **Composio Toolset**: Executes API calls to Eventee and external databases to fetch/update speaker data.
- **Chat Output**: Delivers the optimized schedule and speaker recommendations to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Analyze the speaker distribution for our upcoming Q3 event portfolio and suggest improvements.`
- `Which speakers have the highest engagement scores from our last five events?`
- `Identify any scheduling conflicts for our keynote speakers across the October event calendar.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an expert event operations strategist.
- Instruct the agent to prioritize high-engagement speakers for flagship events.
- Require the agent to cross-reference availability before suggesting a speaker.
- Maintain a neutral, data-driven tone when providing scheduling recommendations.

### 2) Composio Toolset Node
- Provide your Eventee API key to enable read/write access to your event data.
- Set the connection scope to include speaker profiles, event schedules, and engagement analytics.

### 3) Tool Availability
- **Eventee API**: For retrieving event schedules and updating speaker assignments.
- **CRM Connector**: For fetching speaker contact details and historical performance data.
- **Calendar Integration**: For checking real-time availability and preventing scheduling conflicts.

---

## Related Solutions
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manage and deploy standardized workshop templates for your events.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather deep insights on account interactions to inform your event invite lists.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate complex operational tasks across your business platforms.
