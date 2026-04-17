# Sprint Retrospective Analyzer (Uplizd) - Transform team feedback into actionable insights

## Summary
The Sprint Retrospective Analyzer is an intelligent Uplizd workflow that processes raw team feedback and sticky notes from Mural to identify recurring themes, sentiment trends, and actionable process improvements. By automating the synthesis of qualitative retrospective data, this solution helps engineering and product teams move from brainstorming to execution with greater velocity and objective clarity.

---

## Demo
![Sprint Retrospective Analyzer workflow interface showing feedback synthesis and trend analysis](image.png)
**Alt text (SEO-ready):** Sprint Retrospective Analyzer Uplizd workflow, Mural feedback synthesis, team sentiment analysis, and automated action item generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/da162881-830b-5aa0-9ac7-e3146c4c4b65)

---

## Category
*   **Primary Category:** Operations
*   **Secondary Tags:** mural, retrospective, agile, sprint, feedback analysis, team velocity, process improvement, composio, ai workflow
*   This solution bridges the gap between raw team feedback and structured operational improvements by leveraging AI to analyze collaborative board data.

---

## Who is this for?
This solution is designed for agile teams looking to optimize their development lifecycle through data-driven retrospectives.

*   **Engineering Manager**
    *   Identify systemic bottlenecks and recurring technical debt patterns across multiple sprints.
*   **Scrum Master**
    *   Synthesize large volumes of sticky notes into concise, objective summaries for team discussion.
*   **Product Owner**
    *   Align team sentiment with product roadmap adjustments and feature prioritization.
*   **Agile Coach**
    *   Track the effectiveness of process changes over time using sentiment trend data.

---

## Features
- **Automated Mural Extraction**
  Seamlessly pulls sticky note content and board data using the Composio Toolset to ensure no feedback is missed.
- **Sentiment & Theme Analysis**
  Categorizes feedback into positive, negative, and neutral buckets while identifying core recurring themes.
- **Action Item Generation**
  Translates team pain points into concrete, assignable tasks to ensure retrospectives lead to actual change.
- **Trend Tracking**
  Maintains a historical record of team sentiment to visualize improvements or regressions over successive sprints.
- **Real-time Reporting**
  Generates concise summary reports ready for sharing with stakeholders or inclusion in project management tools.

---

## Use Cases
**Sprint Process Optimization**
*   Automatically group feedback by sprint phase to identify specific stages causing team friction.
*   Generate a "Top 3 Improvements" list based on the frequency and intensity of team feedback.

**Team Health Monitoring**
*   Analyze sentiment trends across consecutive sprints to detect early signs of team burnout.
*   Correlate retrospective feedback with velocity changes to understand the impact of process adjustments.

**Actionable Insight Documentation**
*   Convert raw sticky note clusters into structured documentation for internal knowledge bases.
*   Sync identified action items directly to project management boards to ensure accountability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Sprint Retrospective Analyzer template from the marketplace.
3. Connect your Mural account via the Composio Toolset integration.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the Mural board URL or specific retrospective session ID.
*   **Agent**: Processes the raw data, performs sentiment analysis, and drafts improvement suggestions.
*   **Composio Toolset**: Executes API calls to fetch board content and update project management tasks.
*   **Chat Output**: Delivers the final summary report and recommended action items to the user.

### 3) Run the Flow
Use the Playground to test your analysis with these prompts:
* `Analyze the feedback from the last sprint board at [URL] and identify the top 3 recurring pain points.`
* `Generate a summary of team sentiment for the latest retrospective and suggest actionable process improvements.`
* `Create a list of action items based on the 'What went wrong' section of the Mural board and assign them to the team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an Agile Facilitator, focusing on objective synthesis and constructive feedback.
*   Instruction: Analyze input data for sentiment, recurring themes, and actionable insights.
*   Instruction: Maintain a neutral, supportive tone suitable for team retrospective environments.
*   Instruction: Prioritize high-impact process changes over minor administrative suggestions.

### 2) Composio Toolset Node
*   **API Key**: Provide your Mural API credentials within the Composio configuration.
*   **Connection Scope**: Ensure the agent has read access to the specific team workspace and write access to the project management tool for action item creation.

### 3) Tool Availability
*   **Mural API**: Fetch board content, sticky note text, and grouping metadata.
*   **Project Management Connectors**: Create tasks or tickets based on identified action items.
*   **Data Summarization Engine**: Advanced NLP for clustering feedback and sentiment scoring.

---

## Related Solutions
*   [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automate the management and coordination of collaborative workshop sessions.
*   [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manage and deploy standardized workshop templates across distributed teams.
*   [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and report on the operational efficiency of team workflows and daily standups.
