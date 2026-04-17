# Agile Retrospective Analyzer (Uplizd) - Automated sprint insights and team sentiment tracking

## Summary
The Agile Retrospective Analyzer (Uplizd) streamlines the post-sprint review process by automatically extracting, categorizing, and analyzing feedback from Miro boards. By leveraging AI to synthesize team sentiment and identify recurring blockers, this workflow provides engineering leads and Scrum Masters with actionable data to improve velocity and team morale, ensuring every retrospective leads to measurable process improvements.

---

## Demo
![Agile Retrospective Analyzer workflow diagram showing Miro board integration, AI analysis, and summary report generation](../image.png)
**Alt text (SEO-ready):** Agile Retrospective Analyzer workflow for Miro, featuring automated sprint feedback synthesis, team sentiment analysis, and Uplizd AI-driven retrospective reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/eb638387-bebf-5790-aab2-dddb968bedec)

---

## Category
**Primary category:** Operations
**Secondary tags:** agile, miro, sprint, retrospective, sentiment analysis, engineering management, team velocity, composio

This solution bridges the gap between raw team feedback in Miro and structured operational insights for continuous improvement.

---

## Who is this for?
This solution is designed for agile teams looking to transform qualitative retrospective discussions into quantitative process improvements.

* **Scrum Master**
    * Automates the aggregation of sticky notes and feedback themes to save hours of manual synthesis.
* **Engineering Manager**
    * Gains visibility into systemic blockers and team sentiment trends across multiple sprints.
* **Product Owner**
    * Identifies recurring friction points in the development lifecycle that impact feature delivery.
* **Agile Coach**
    * Uses data-driven insights to facilitate more productive team discussions and targeted process adjustments.

---

## Features
- **Automated Board Extraction**
  Seamlessly pulls feedback data from Miro boards using the Composio Toolset to ensure no insight is left behind.
- **Sentiment & Theme Analysis**
  Uses advanced LLM reasoning to categorize feedback into "Keep," "Stop," and "Start" buckets while gauging team morale.
- **Trend Reporting**
  Generates longitudinal reports that track recurring issues across consecutive sprints to measure the impact of process changes.
- **Action Item Prioritization**
  Automatically suggests high-impact action items based on the frequency and severity of reported blockers.
- **Real-time Integration**
  Connects directly with your existing Miro workspace to ensure the analysis is always based on the most current retrospective data.

---

## Use Cases
**Sprint Performance Review**
* Consolidating feedback from distributed teams to identify the top three bottlenecks impacting velocity.
* Generating a summary report of "Start/Stop/Continue" items to share with stakeholders after every sprint.

**Team Health Monitoring**
* Tracking sentiment trends over time to detect early signs of burnout or team friction.
* Correlating specific technical debt mentions with team feedback to prioritize infrastructure improvements.

**Process Optimization**
* Comparing retrospective outcomes against historical data to validate if recent process changes have improved efficiency.
* Identifying recurring communication gaps between cross-functional teams during the sprint cycle.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Agile Retrospective Analyzer template from the marketplace.
3. Connect your Miro account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the Miro board URL or sprint identifier.
* **Agent**: Analyzes the raw board data and synthesizes feedback themes.
* **Composio Toolset**: Executes API calls to fetch board items and export summary reports.
* **Chat Output**: Displays the final retrospective analysis and recommended action items.

### 3) Run the Flow
Use the Playground to test the workflow with prompts like:
* `Analyze the retrospective board at [Miro URL] and summarize the top 3 blockers.`
* `Compare the sentiment of this sprint's retrospective with the previous one.`
* `Generate a list of actionable process improvements based on the latest Miro board feedback.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an Agile Coach, focusing on objective synthesis and constructive feedback.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Act as an expert Agile Coach. Categorize feedback objectively and prioritize action items based on team impact."
* Instruction: "Maintain a neutral, supportive tone when summarizing team sentiment."

### 2) Composio Toolset Node
* Requires a valid Miro API key with read/write access to your team's boards.
* Ensure the connection scope includes `boards:read` and `items:read`.

### 3) Tool Availability
* `miro_get_board_items`: Fetches all sticky notes and text elements from the specified board.
* `miro_export_summary`: Creates a new summary document or comment on the board.
* `sentiment_analysis_tool`: Processes text strings to determine team mood.

---

## Related Solutions
* [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automate workshop agendas and participant engagement.
* [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manage and deploy standardized workshop templates.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track team productivity and workflow bottlenecks.
