# Team Performance Analyzer (Uplizd) - Optimize safety operations through inspection data insights

## Summary
The Team Performance Analyzer (Uplizd) is an intelligent workflow designed to ingest, process, and evaluate inspection data from SafetyCulture. By automating the analysis of team performance metrics and safety compliance patterns, this solution provides operational leaders with a single source of truth, enabling faster identification of safety gaps, improved pipeline velocity for corrective actions, and enhanced organizational hygiene.

---

## Demo
![Team Performance Analyzer dashboard showing inspection trends and safety compliance scores](image.png)
**Alt text (SEO-ready):** Team Performance Analyzer dashboard showing inspection trends, safety compliance scores, and Uplizd workflow automation for SafetyCulture data.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ec30ed9c-4c87-58d4-a99e-d896cabf9b5c)

---

## Category
- **Primary category:** Operations management
- **Secondary tags:** safetyculture, team performance, data analytics, compliance, operational efficiency, workflow automation, composio, ai insights
- This solution bridges the gap between raw inspection data and actionable team performance insights to drive continuous improvement.

---

## Who is this for?
This solution is designed for operational leaders and safety managers who need to translate field data into strategic team improvements.

- **Safety Manager**
    - Identifies recurring safety hazards across multiple sites to prioritize training interventions.
- **Operations Director**
    - Monitors team-wide inspection completion rates to ensure adherence to corporate safety standards.
- **Team Lead**
    - Receives automated performance summaries to provide targeted feedback to field staff.
- **Compliance Officer**
    - Tracks audit-ready documentation and flags deviations from safety protocols in real-time.

---

## Features
- **Automated Data Ingestion**
    - Seamlessly pulls inspection logs from SafetyCulture via the Composio Toolset to ensure real-time data availability.
- **Performance Trend Analysis**
    - Uses AI to detect patterns in inspection scores, highlighting teams that consistently exceed or fall below safety benchmarks.
- **Corrective Action Tracking**
    - Automatically maps identified safety gaps to follow-up tasks, ensuring no compliance issue remains unaddressed.
- **Customizable Reporting**
    - Generates summarized performance reports tailored to specific management roles, focusing on actionable metrics rather than raw data.
- **Proactive Alerting**
    - Triggers notifications when team performance drops below defined thresholds, allowing for immediate intervention.

---

## Use Cases
**Safety Compliance Monitoring**
- Automatically flag inspections that fail to meet minimum safety score requirements.
- Generate monthly compliance reports for executive review based on historical inspection data.

**Operational Efficiency**
- Identify bottlenecks in the inspection process where teams are spending excessive time on specific checklist items.
- Optimize resource allocation by identifying high-performing teams that can mentor others.

**Team Development**
- Create personalized performance feedback loops for field staff based on their specific inspection history.
- Track the impact of new safety training programs on team inspection quality over time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Team Performance Analyzer template from the marketplace.
3. Connect your SafetyCulture account via the Composio Toolset integration.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding team performance or specific inspection data.
- **Agent**: Processes the request, interprets safety metrics, and formulates analytical responses.
- **Composio Toolset**: Executes API calls to fetch and filter real-time data from SafetyCulture.
- **Chat Output**: Delivers clear, actionable insights and performance summaries to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Analyze the performance of the North Region team for the last 30 days.`
- `Which inspection categories are showing the highest failure rates this week?`
- `Generate a summary of safety compliance issues for the maintenance department.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as an analytical engine that synthesizes technical data into human-readable insights.
- Focus on identifying anomalies and trends in inspection data.
- Maintain a professional, objective tone suitable for operational reporting.
- Prioritize actionable recommendations over raw data dumps.

### 2) Composio Toolset Node
- Provide your API key for the SafetyCulture integration.
- Ensure the connection scope includes read access to inspections, templates, and user performance data.

### 3) Tool Availability
- `get_inspections`: Retrieve historical and recent inspection logs.
- `get_team_metrics`: Access aggregated performance data for specific groups.
- `list_compliance_alerts`: Query active safety violations or flagged items.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Streamline employee integration and compliance training.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize team productivity and process bottlenecks.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor account performance and usage metrics for operational success.
