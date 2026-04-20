# Technical Debt Tracker (Uplizd) - Automate codebase maintenance and prioritization

## Summary
The Technical Debt Tracker (Uplizd) is an automated workflow designed to systematically identify, catalog, and prioritize technical debt within your software projects. By leveraging the Composio Toolset to interface with Shortcut, this solution helps engineering teams maintain high code quality, reduce long-term maintenance burdens, and ensure that refactoring tasks are visible and actionable within the existing development lifecycle.

---

## Demo
![Technical Debt Tracker workflow interface showing Shortcut integration and automated ticket creation](image.png)
**Alt text (SEO-ready):** Technical Debt Tracker workflow in Uplizd, showing automated Shortcut ticket creation, code quality analysis, and technical debt prioritization for engineering teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1b14a82a-fee6-53ef-86d0-1cdaae6c5685)

---

## Category
**Primary category:** Operations  
**Secondary tags:** technical debt, shortcut, engineering management, code quality, software development, automation, devops, workflow optimization.  
This solution bridges the gap between code-level technical debt and project management, ensuring that maintenance tasks are tracked with the same rigor as new feature development.

---

## Who is this for?
This solution is designed for engineering organizations looking to balance rapid feature delivery with long-term system health.

* **Engineering Managers**
    * Gain visibility into the accumulation of technical debt and allocate sprint capacity for refactoring.
* **Software Architects**
    * Systematically document architectural bottlenecks and ensure they are prioritized in the product roadmap.
* **DevOps Engineers**
    * Automate the creation of cleanup tasks based on infrastructure alerts or code quality metrics.
* **Product Owners**
    * Understand the trade-offs between new feature development and the necessity of addressing underlying technical debt.

---

## Features
- **Automated Debt Identification**
  Automatically scan and log technical debt items directly from developer feedback or automated linting reports.
- **Shortcut Integration**
  Seamlessly sync debt items into Shortcut stories, ensuring they live within the existing project management ecosystem.
- **Priority Scoring**
  Apply custom logic to score debt based on severity, impact on velocity, and potential security risks.
- **Real-time Sync**
  Maintain a single source of truth by updating ticket status in real-time as refactoring progress is made.
- **Customizable Thresholds**
  Define specific criteria for what constitutes "debt" versus "maintenance" to keep the backlog clean and relevant.

---

## Use Cases
**Backlog Grooming**
* Automatically convert high-priority code comments into actionable Shortcut tickets during sprint planning.
* Filter and group technical debt by module or service to identify systemic issues across the codebase.

**Maintenance Sprints**
* Generate a list of "quick win" refactoring tasks to fill gaps in sprint capacity.
* Track the lifecycle of a debt item from identification to verification and final closure.

**Quality Assurance**
* Link automated test failures to specific technical debt items to highlight the cost of deferred maintenance.
* Monitor the rate of debt accumulation versus resolution to ensure long-term project sustainability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Shortcut account via the Composio connection prompt.
4. Ensure nodes are correctly mapped to your specific Shortcut project IDs and team workflows.

### 2) Setup the Nodes
* **Chat Input**: Receives the description of the technical debt or the automated report data.
* **Agent**: Analyzes the input, determines the severity, and formats the ticket details.
* **Composio Toolset**: Executes the API calls to create or update stories within Shortcut.
* **Chat Output**: Confirms the successful creation of the ticket and provides a link to the new item.

### 3) Run the Flow
Use the Playground to test the agent's ability to categorize and log debt:
* `Create a new technical debt ticket for the legacy authentication module due to outdated dependency.`
* `Prioritize the existing debt ticket #123 as 'High' and add a comment about performance degradation.`
* `List all open technical debt items in the 'Core Services' project that have been stagnant for over 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical project coordinator that translates unstructured input into structured project management data.
* Focus on extracting actionable titles and clear descriptions.
* Assign severity levels based on the context provided in the prompt.
* Maintain consistency with existing Shortcut label and workflow naming conventions.

### 2) Composio Toolset Node
Requires a valid Shortcut API token. Ensure the connection scope includes permissions to create stories, update fields, and search for existing tickets within your target workspace.

### 3) Tool Availability
* **Story Creation**: Ability to generate new tickets with custom descriptions and priority labels.
* **Search & Query**: Ability to look up existing tickets to prevent duplicate logging.
* **Update & Comment**: Ability to modify ticket status or add context to existing debt items.

---

## Related Solutions
* [Action Item Prioritizer (Rootly)](../action-item-prioritizer-by-rootly/README.md) — Streamline the prioritization of operational action items.
* [Action Item Cleanup Agent (Rootly)](../action-item-cleanup-agent-by-rootly/README.md) — Automate the resolution and archiving of stale action items.
* [Workflow Health Monitor (DailyBot)](../workflow-health-monitor-by-dailybot/README.md) — Track the overall health and velocity of your development workflows.
