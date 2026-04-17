# Portfolio Company Intelligence (Uplizd) - Automated data aggregation and actionable insights for investment portfolios

## Summary
The Portfolio Company Intelligence solution leverages the Uplizd AI workflow to automatically aggregate, monitor, and synthesize data from your portfolio companies. By integrating directly with platforms like Affinity, this solution provides investment teams with a single source of truth, enabling real-time visibility into company performance, pipeline velocity, and critical operational updates without manual data entry.

---

## Demo
![Portfolio Company Intelligence workflow dashboard showing automated data aggregation from Affinity and real-time insight generation](image.png)

**Alt text (SEO-ready):** Portfolio Company Intelligence dashboard showing Uplizd AI workflow, Affinity CRM integration, and automated portfolio data aggregation.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAK+A81A00xGgUjBwAAU4wGgUoGgUoGgUoGgUoGgUoGgUoGgUoGgUoGgUoGgUoGAAC+8wE0515C+gAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/fd5c6485-6310-5b6b-8d06-89fa930e725f)

---

## Category
- **Primary category:** RevOps
- **Secondary tags:** portfolio management, affinity, crm, data aggregation, investment intelligence, ai workflow, composio, pipeline tracking
- This solution streamlines investment operations by centralizing fragmented portfolio data into a unified, AI-driven intelligence layer.

---

## Who is this for?
This solution is designed for investment professionals and operations teams who need to maintain high-fidelity data across their portfolio.

- **Investment Associate**
    - Automates the manual collection of portfolio updates and KPI tracking.
- **Portfolio Manager**
    - Gains real-time visibility into company health and potential risk signals.
- **Operations Lead**
    - Ensures data hygiene across the CRM by standardizing incoming company reports.
- **Investor Relations**
    - Quickly generates accurate performance summaries for limited partner reporting.

---

## Features
- **Automated Data Aggregation**
    - Connects to Affinity and other data sources to pull company updates automatically.
- **Intelligent Insight Synthesis**
    - Uses AI to parse unstructured data from emails and reports into structured CRM fields.
- **Real-time Health Monitoring**
    - Detects anomalies or stalled metrics in portfolio company performance.
- **Composio-Powered Integrations**
    - Leverages the Composio Toolset to execute read/write actions across your CRM stack.
- **Pipeline Velocity Tracking**
    - Monitors the progression of portfolio company milestones and follow-up requirements.

---

## Use Cases
**Portfolio Performance Tracking**
- Automatically log quarterly KPI updates from portfolio companies into your CRM.
- Flag companies that have missed reporting deadlines or show declining engagement metrics.

**Investment Pipeline Management**
- Sync new lead signals from portfolio company board meetings directly into your deal flow.
- Map follow-up action items to specific team members based on meeting transcripts.

**Data Hygiene & Compliance**
- Standardize company profile data across multiple systems to ensure reporting accuracy.
- Audit portfolio contact lists to remove duplicates and verify current leadership roles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your required CRM and communication integrations via the Composio connection prompt.
4. Ensure nodes are correctly mapped from **Chat Input** to **Agent** to **Composio Toolset** to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers or manual requests for portfolio data updates.
- **Agent**: Processes natural language queries and determines the necessary data retrieval steps.
- **Composio Toolset**: Executes secure API calls to fetch or update records in your CRM.
- **Chat Output**: Delivers the synthesized intelligence report or confirms the data update.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize the latest KPI performance for all companies in the 'Growth' portfolio.`
- `Check for any missing Q3 financial reports in Affinity and draft a reminder email.`
- `Identify portfolio companies that have had no engagement in the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence hub for your portfolio data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data extraction.
- Provide clear instructions on the expected output format (e.g., JSON or Markdown tables).
- Define the scope of data access to ensure sensitive investment information remains secure.

### 2) Composio Toolset Node
- Provide your unique API key to enable secure connectivity.
- Configure the connection scope to allow read/write access to your specific CRM objects (e.g., Accounts, Opportunities, Contacts).

### 3) Tool Availability
- **CRM Connector**: For fetching and updating company records.
- **Email/Communication Tool**: For sending automated follow-ups and alerts.
- **Data Parser**: For extracting structured insights from unstructured text.

---

## Related Solutions
- [../account-intelligence-gatherer-by-dropcontact/README.md](Account Intelligence Gatherer) - Automate contact enrichment and data verification.
- [../account-relationship-builder-by-dynamics365/README.md](Account Relationship Builder) - Manage complex stakeholder mapping and relationship tracking.
- [../account-research-agent-by-onepage/README.md](Account Research Agent) - Deep-dive research and automated company profiling.
