# Issue Auto-Classifier (Uplizd) - AI-powered automated ticket tagging and triage

## Summary
The Issue Auto-Classifier by Linear is an intelligent workflow designed to streamline project management by automatically analyzing, tagging, and categorizing incoming issues. By leveraging AI to interpret issue content, this Uplizd solution eliminates manual triage bottlenecks, ensures consistent data hygiene across your Linear workspace, and accelerates pipeline velocity for engineering and product teams.

---

## Demo
![Issue Auto-Classifier workflow diagram showing automated tagging of Linear tickets](image.png)
**Alt text (SEO-ready):** Issue Auto-Classifier workflow diagram showing automated tagging of Linear tickets using Uplizd and Composio for intelligent project management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8a5137ca-6957-5a62-9256-43642d49f63a)

---

## Category
**Primary category:** Operations
**Secondary tags:** linear, issue tracking, automation, ai workflow, data hygiene, project management, composio, ticketing.
This solution bridges the gap between raw issue intake and organized project backlogs through intelligent, automated classification.

---

## Who is this for?
This solution is designed for teams looking to reduce manual administrative overhead in their issue tracking systems.

* **Engineering Managers**
    * Maintain a clean, searchable backlog without spending hours manually labeling incoming tickets.
* **Product Managers**
    * Gain immediate visibility into feature requests versus bug reports through automated priority tagging.
* **Support Leads**
    * Ensure that critical customer-reported issues are routed to the correct engineering squads instantly.
* **Operations Specialists**
    * Standardize project data hygiene across the organization by enforcing consistent classification schemas.

---

## Features
- **Intelligent Content Analysis**
  Uses advanced LLMs to parse issue titles and descriptions, identifying intent and context automatically.
- **Automated Linear Labeling**
  Directly updates Linear issue labels based on the AI's classification, ensuring real-time organization.
- **Customizable Classification Logic**
  Easily adapt the agent's instructions to match your specific team's taxonomy and project structure.
- **Seamless Composio Integration**
  Leverages the Composio Toolset to securely interact with the Linear API for high-fidelity data updates.
- **Real-time Triage Pipeline**
  Processes new issues as they arrive, reducing the time-to-action for critical engineering tasks.

---

## Use Cases
**Backlog Grooming**
* Automatically categorize incoming feature requests into "Frontend," "Backend," or "Infrastructure" buckets.
* Flag issues as "High Priority" based on sentiment analysis of the issue description.

**Bug Triage Automation**
* Identify and label duplicate bug reports by comparing new submissions against existing open issues.
* Assign specific engineering team labels to bugs based on the technical keywords detected in the report.

**Project Data Hygiene**
* Ensure every ticket has a valid status and category tag before it reaches the sprint planning board.
* Archive or move stale issues to a "Backlog" project based on inactivity patterns detected during classification.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your dashboard.
2. Connect your Linear account via the Composio integration settings.
3. Configure your target project ID within the workflow settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the new issue data payload from your webhook or manual trigger.
* **Agent:** Processes the text, determines the appropriate tags, and generates the update command.
* **Composio Toolset:** Executes the `linear_update_issue` function to apply the classification.
* **Chat Output:** Confirms the successful tagging or logs any errors for manual review.

### 3) Run the Flow
Test your classifier in the Uplizd Playground with these prompts:
* `Analyze the latest issue in the 'Engineering' project and apply the 'Bug' label if it mentions a crash.`
* `Categorize all untagged issues in the 'Product' project based on their description content.`
* `Scan the 'Support' project and prioritize issues containing keywords like 'urgent' or 'blocked'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, mapping unstructured text to your team's specific tag taxonomy.
* Define your tag schema clearly in the system prompt.
* Instruct the agent to ignore non-actionable chatter.
* Set the output format to match the required API parameters for Linear.

### 2) Composio Toolset Node
Requires a valid Linear API key configured within the Composio platform. Ensure the connection scope includes `issues:write` and `issues:read` permissions to allow the agent to perform its triage duties.

### 3) Tool Availability
* `linear_get_issue`: Fetch details for analysis.
* `linear_update_issue`: Apply labels and status changes.
* `linear_list_projects`: Retrieve project IDs for routing.
* `linear_search_issues`: Identify potential duplicates or related tickets.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automatically rank and prioritize tasks based on urgency.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline cross-platform task management and status updates.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track and categorize account health data for better operational insights.
