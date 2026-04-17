# Report Visualizer (Uplizd) - Automate executive slide deck creation from data reports

## Summary
The Report Visualizer (Uplizd) workflow streamlines the transition from raw data analysis to executive-ready presentations. By leveraging AI to interpret complex datasets and automatically mapping them into Google Slides, this solution eliminates manual formatting, ensures consistent branding, and accelerates the delivery of business insights to stakeholders.

---

## Demo
![Report Visualizer workflow showing data ingestion from a report and output to Google Slides](image.png)
**Alt text (SEO-ready):** Report Visualizer workflow by Uplizd, automating data-to-slide conversion for executive reporting and business intelligence presentations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/241a2544-ec14-573f-b34e-61f9f42a27d0)

---

## Category
*   **Primary category:** Data integration
*   **Secondary tags:** google slides, reporting, automation, data visualization, executive briefing, composio, ai workflow
*   This solution bridges the gap between analytical data sources and visual communication tools to improve reporting velocity.

---

## Who is this for?
This solution is designed for professionals who need to turn data into actionable narratives without spending hours in presentation software.

*   **Data Analysts**
    *   Automate the creation of recurring slide decks to focus on deep-dive analysis rather than manual formatting.
*   **Sales Operations Managers**
    *   Standardize quarterly business review (QBR) presentations with real-time data pulled directly from CRM reports.
*   **Marketing Leads**
    *   Convert campaign performance metrics into visual summaries for stakeholder updates instantly.
*   **Executive Assistants**
    *   Prepare high-fidelity briefing materials for leadership meetings by syncing the latest data snapshots to slide templates.

---

## Features
- **Automated Slide Generation**
  Translates structured data points into professional slide layouts using the Composio Google Slides integration.
- **Data-to-Visual Mapping**
  Intelligently maps key performance indicators (KPIs) and metrics to appropriate chart types within the presentation.
- **Template Consistency**
  Applies corporate branding and slide themes automatically to ensure every generated report meets organizational standards.
- **Real-Time Data Sync**
  Pulls the latest figures from your connected data sources to ensure executive reports are always based on current information.
- **Workflow Orchestration**
  Seamlessly connects your data input, the AI analysis engine, and the final slide output into a single, repeatable pipeline.

---

## Use Cases
**Quarterly Business Reviews**
*   Syncing regional sales performance data into standardized QBR slide templates.
*   Updating competitive analysis charts automatically before executive leadership meetings.

**Marketing Campaign Reporting**
*   Generating visual summaries of ad spend and conversion rates from analytics platforms.
*   Creating monthly performance decks for client-facing presentations without manual data entry.

**Operational Health Briefings**
*   Transforming system uptime and support ticket volume data into executive dashboard slides.
*   Automating the creation of project status updates for cross-departmental stakeholders.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Report Visualizer template from the solution library.
3. Connect your Google Slides and relevant Data Source accounts via the Composio integration menu.
4. Ensure nodes are correctly mapped: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw data or report summary to be visualized.
*   **Agent**: Processes the data, identifies key insights, and formats the content for presentation.
*   **Composio Toolset**: Executes the API calls to create and populate Google Slides.
*   **Chat Output**: Confirms the successful generation of the slide deck and provides a link to the presentation.

### 3) Run the Flow
Access the Playground to test your visualization pipeline:
*   `Create a QBR slide deck based on the Q3 sales data report.`
*   `Generate a marketing performance summary slide for the last 30 days.`
*   `Build an executive briefing deck using the latest project status metrics.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical bridge, transforming text-based data into structured slide content.
*   Instruct the agent to prioritize high-impact metrics for executive visibility.
*   Define the tone as professional, concise, and data-driven.
*   Ensure the agent follows specific slide layout instructions provided in the system prompt.

### 2) Composio Toolset Node
*   Requires a valid Google Slides API key and appropriate OAuth scopes for document creation and editing.
*   Ensure the "Google Slides" toolset is enabled and authenticated within the Composio dashboard.

### 3) Tool Availability
*   **Google Slides API**: For creating slides, inserting text, and adding chart placeholders.
*   **Data Connector**: For fetching raw data from your CRM or analytics platform.
*   **Formatting Engine**: For applying styles and layout templates to the output.

---

## Related Solutions
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automate the gathering and reporting of account-level intelligence.
*   [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Analyze and report on video content metrics for better strategy.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your data sources aligned across platforms to ensure reporting accuracy.
