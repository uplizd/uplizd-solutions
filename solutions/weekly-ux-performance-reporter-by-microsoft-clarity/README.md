# Weekly UX Performance Reporter (Uplizd) - Automated insights for user experience optimization

## Summary
The Weekly UX Performance Reporter is an automated Uplizd AI workflow that synthesizes raw user experience metrics from Microsoft Clarity into actionable weekly insights. By leveraging the Composio Toolset to fetch session recordings, heatmaps, and engagement data, this solution eliminates manual reporting overhead, providing product teams with a single source of truth to improve pipeline velocity and site hygiene.

---

## Demo
![Weekly UX Performance Reporter dashboard showing automated insight generation and trend analysis](image.png)
**Alt text (SEO-ready):** Weekly UX Performance Reporter dashboard showing automated insight generation and trend analysis for Uplizd AI workflows and Microsoft Clarity data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/41920156-7910-548c-9ad9-faab30e94958)

---

## Category
**Primary category:** Product Analytics
**Secondary tags:** ux, microsoft clarity, data reporting, product management, automation, ai workflow, composio, user insights.
This solution bridges the gap between raw behavioral data and strategic decision-making by automating the synthesis of UX performance reports.

---

## Who is this for?
This workflow is designed for teams focused on data-driven product development and continuous site improvement.

* **Product Managers**
    * Identify friction points in user journeys to prioritize feature backlogs effectively.
* **UX Designers**
    * Receive automated summaries of heatmap data to validate design changes without manual analysis.
* **Growth Marketers**
    * Track how landing page UX changes correlate with conversion rate fluctuations.
* **Web Developers**
    * Gain visibility into performance bottlenecks and session-based technical errors.

---

## Features
- **Automated Data Aggregation**
  Connects directly to Microsoft Clarity to pull weekly session metrics and engagement trends without manual exports.
- **AI-Powered Insight Synthesis**
  Uses the Agent node to interpret complex behavioral data and generate human-readable executive summaries.
- **Composio-Driven Integration**
  Leverages the Composio Toolset to securely authenticate and query specific project data from your analytics environment.
- **Trend Analysis Reporting**
  Identifies week-over-week changes in bounce rates, scroll depth, and interaction patterns automatically.
- **Actionable Recommendation Engine**
  Provides concrete suggestions for UX improvements based on the identified behavioral patterns.

---

## Use Cases
**Conversion Rate Optimization**
* Analyze high-drop-off pages to identify specific UI elements causing user friction.
* Correlate weekly design updates with changes in user engagement metrics.

**Product Feature Validation**
* Monitor user interaction patterns immediately following the release of new features.
* Compare engagement metrics across different user segments to refine product-market fit.

**Technical Performance Monitoring**
* Detect spikes in rage clicks or dead clicks that indicate broken site functionality.
* Generate weekly reports on load time impact on user navigation behavior.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your preferred workspace to initialize the workflow.
3. Connect your Microsoft Clarity account via the Composio integration portal.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the request to generate the weekly UX report.
* **Agent**: Processes the raw data and drafts the performance summary.
* **Composio Toolset**: Executes API calls to fetch specific UX metrics from Microsoft Clarity.
* **Chat Output**: Delivers the final formatted report to your dashboard or notification channel.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Generate a summary of the top 3 pages with the highest bounce rate this week.`
* `Analyze user engagement trends for the new checkout flow compared to last week.`
* `Create a weekly UX performance report highlighting key friction points and suggested fixes.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized UX analyst.
* **Recommended instruction pattern:**
    * Act as a senior product analyst specializing in Microsoft Clarity data.
    * Focus on identifying actionable trends rather than just reporting raw numbers.
    * Maintain a professional, concise tone suitable for executive-level reporting.

### 2) Composio Toolset Node
* Requires a valid Microsoft Clarity API key configured within the Composio dashboard.
* Ensure the connection scope includes read access to session recordings and project analytics.

### 3) Tool Availability
* `get_project_metrics`: Fetches high-level engagement data.
* `list_session_recordings`: Retrieves specific user session data for deep-dive analysis.
* `get_heatmap_data`: Extracts visual interaction data for specific page URLs.

---

## Related Solutions
* [AB Test Performance Analyzer](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) - Analyze A/B test results using Clarity data.
* [Widget Experience Optimizer](../widget-experience-optimizer-by-productlane/README.md) - Optimize user-facing widgets based on feedback.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational health of automated business processes.
