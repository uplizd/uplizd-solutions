# Team Capacity Planner (Uplizd) - Optimize resource allocation and hiring workflows

## Summary
The Team Capacity Planner (Uplizd) is an intelligent automation workflow designed to synchronize team workload data with hiring requirements. By leveraging the Composio Toolset to interface with Workable and project management platforms, this solution provides HR and Operations teams with a single source of truth for resource utilization, helping to eliminate bottlenecks and streamline pipeline velocity through real-time capacity analysis.

---

## Demo
![Team Capacity Planner dashboard showing real-time workload distribution and hiring gaps](image.png)
**Alt text (SEO-ready):** Team Capacity Planner dashboard showing real-time workload distribution, hiring gaps, and resource allocation metrics managed via Uplizd and Workable.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f98c0486-6ce3-5bb1-85e5-8d116179b567)

---

## Category
- **Primary category:** Operations automation
- **Secondary tags:** `workable`, `capacity planning`, `hiring`, `resource management`, `hr ops`, `composio`, `ai workflow`
- This solution bridges the gap between current team bandwidth and recruitment needs to ensure sustainable growth.

---

## Who is this for?
This workflow is built for organizations looking to scale efficiently without burning out existing teams.

- **HR Manager**
    - Automate the identification of hiring needs based on current team utilization data.
- **Operations Lead**
    - Maintain a balanced workload across departments to prevent project bottlenecks.
- **Recruitment Specialist**
    - Prioritize open roles based on real-time capacity constraints and project urgency.
- **Department Head**
    - Gain data-driven insights into team bandwidth to justify new headcount requests.

---

## Features
- **Real-time Capacity Sync**
    - Automatically pulls current project load and team availability metrics into the planning dashboard.
- **Workable Integration**
    - Seamlessly connects with Workable to align open job requisitions with identified capacity gaps.
- **Automated Resource Forecasting**
    - Uses AI to project future bandwidth requirements based on current project timelines and velocity.
- **Intelligent Bottleneck Detection**
    - Proactively flags teams approaching maximum capacity before performance or morale suffers.
- **Composio-Powered Tooling**
    - Utilizes the Composio Toolset to execute complex data queries across disparate HR and project management systems.

---

## Use Cases
**Resource Allocation**
- Syncing project management hours with team availability to identify under-utilized staff.
- Generating weekly capacity reports that highlight teams requiring additional headcount.

**Hiring Pipeline Alignment**
- Automatically triggering a review of open job requisitions when team capacity drops below a defined threshold.
- Mapping incoming project requests to existing team skills and current availability.

**Operational Efficiency**
- Reducing manual data entry by syncing Workable candidate status with internal capacity planning sheets.
- Providing leadership with automated, data-backed justifications for new hiring budgets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Solution."
2. Upload the `team-capacity-planner-by-workable` configuration file.
3. Connect your Workable and project management API credentials in the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language queries regarding team bandwidth or hiring needs.
- **Agent**: Processes requests and determines the necessary data points to retrieve.
- **Composio Toolset**: Executes secure API calls to fetch real-time capacity and hiring data.
- **Chat Output**: Delivers actionable insights and recommendations back to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `What is the current capacity of the engineering team for Q3?`
- `Identify which departments have the highest workload and need additional hiring.`
- `Create a summary of open roles in Workable that match our current capacity gaps.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as an Operations Analyst, interpreting capacity data to provide strategic hiring advice.
- Focus on identifying discrepancies between project load and team headcount.
- Maintain a professional, data-driven tone for all recommendations.
- Prioritize actionable insights that link directly to Workable job postings.

### 2) Composio Toolset Node
- Requires a valid Workable API key and read/write access to your project management platform.
- Ensure the connection scope includes `read:jobs`, `read:candidates`, and `read:projects`.

### 3) Tool Availability
- **Workable API**: For retrieving job requisition data and candidate status.
- **Project Management Connector**: For fetching task completion rates and team hours.
- **Data Aggregator**: For synthesizing cross-platform metrics into a unified view.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Streamline new hire setup and documentation.
- [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate CRM account creation and configuration.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Manage complex operational workflows across platforms.
