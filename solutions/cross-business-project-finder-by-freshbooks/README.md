# Cross-Business Project Finder (Uplizd) - Centralized project discovery across FreshBooks accounts

## Summary
The Cross-Business Project Finder is an intelligent Uplizd workflow designed to aggregate and search project data across multiple FreshBooks business entities. By leveraging the Composio Toolset, this agent eliminates the need for manual cross-account navigation, providing a single source of truth for project status, timelines, and resource allocation to improve operational visibility and pipeline velocity.

---

## Demo
![Cross-Business Project Finder workflow interface showing multi-account data aggregation](image.png)
**Alt text (SEO-ready):** Uplizd Cross-Business Project Finder workflow for FreshBooks, demonstrating multi-account data synchronization, project discovery, and AI-driven project management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQ64205QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxHT+eAAAAF0lEQVR42mP8z8AARsBAMGIQjBq4GAAM+QEB557/wwAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/a862e24f-3000-52e7-be5b-8b262bed75de)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** freshbooks, project management, cross-account, data sync, business intelligence, composio, ai workflow
- This solution streamlines multi-entity project tracking by unifying fragmented data into a single, searchable interface.

---

## Who is this for?
This solution is designed for professionals managing multiple business entities or complex portfolios who require real-time project oversight.

- **Operations Manager**
    - Gain immediate visibility into project status across all business units without manual login switching.
- **Account Executive**
    - Quickly identify project availability and resource constraints when pitching to new clients.
- **Finance Lead**
    - Track project billing status and timelines across diverse accounts to ensure consistent revenue recognition.
- **Project Coordinator**
    - Sync project milestones and deadlines into a centralized view to prevent scheduling conflicts.

---

## Features
- **Multi-Account Aggregation**
    - Automatically pulls project metadata from multiple FreshBooks accounts into a unified queryable interface.
- **Intelligent Project Search**
    - Uses natural language processing to filter projects by name, status, or client across your entire business ecosystem.
- **Real-Time Status Sync**
    - Ensures project updates, including budget and timeline changes, are reflected instantly via the Composio Toolset.
- **Cross-Entity Reporting**
    - Generates consolidated summaries of project health, helping identify stalled initiatives across different business units.
- **Automated Data Hygiene**
    - Standardizes project naming conventions and status labels during the ingestion process for cleaner reporting.

---

## Use Cases
**Portfolio Management**
- Identify all active projects across three different business entities to balance team workloads.
- Flag projects that have exceeded their estimated hours across multiple client accounts.

**Operational Efficiency**
- Retrieve specific project details for a client without navigating through individual FreshBooks dashboards.
- Generate a weekly summary of project completions across the entire organization.

**Client Communication**
- Quickly confirm project delivery dates for clients who have services spread across multiple business units.
- Provide accurate status updates to stakeholders by aggregating data from disparate project folders.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your FreshBooks account via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts natural language queries regarding project names or status.
- **Agent**: Processes intent and maps requests to specific FreshBooks API calls.
- **Composio Toolset**: Executes secure, authenticated queries across your FreshBooks entities.
- **Chat Output**: Delivers a human-readable summary of the requested project data.

### 3) Run the Flow
Use the Playground to test your setup with these prompts:
- `Find all active projects for 'Acme Corp' across all my connected businesses.`
- `List all projects that are currently marked as 'In Progress' and have a deadline this week.`
- `Show me the total budget utilization for the 'Website Redesign' project across all accounts.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized project research assistant.
- Use a model capable of high-precision tool calling (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize data accuracy and cross-reference account IDs.
- Configure the system prompt to output data in clear, bulleted lists for readability.

### 2) Composio Toolset Node
- Provide your FreshBooks API credentials within the Composio dashboard.
- Ensure the connection scope includes read access for `projects`, `clients`, and `invoices`.

### 3) Tool Availability
- `freshbooks_list_projects`: Fetches project lists across authorized entities.
- `freshbooks_get_project_details`: Retrieves granular data for specific project IDs.
- `freshbooks_search_clients`: Maps project data to specific client profiles for context.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial data matching across accounts.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline project-based tasks and status updates.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track client engagement and project usage metrics.
