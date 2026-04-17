# Knowledge Sharing Curator (Uplizd) - Automate team knowledge discovery and organization in Slack

## Summary
The Knowledge Sharing Curator is an intelligent Uplizd workflow designed to capture, categorize, and surface critical team insights directly within Slack. By leveraging AI to monitor communication channels and index shared documentation, this solution eliminates information silos, reduces repetitive questions, and ensures that institutional knowledge remains accessible, organized, and actionable for the entire organization.

---

## Demo
![Knowledge Sharing Curator workflow diagram showing Slack integration, AI processing, and automated knowledge indexing](image.png)
**Alt text (SEO-ready):** Uplizd Knowledge Sharing Curator workflow diagram showing Slack integration, AI processing, and automated knowledge indexing for team collaboration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAy5l4k7gAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAK+A8DA8N/ID4DxP8H4j8Q/4H4D8R/IP4H4j8Q/4H4D8R/IP4H4j8Q/4H4D8R/IP4HAA==)](https://uplizd.ai/solutions/691df3a8-0184-525b-8628-a20d82c478dc)

---

## Category
- **Primary category:** Knowledge Management
- **Secondary tags:** slack, ai workflow, knowledge base, team collaboration, automation, internal comms, composio, productivity
- This solution streamlines internal information flow by transforming unstructured Slack conversations into a structured, searchable knowledge repository.

---

## Who is this for?
This solution is designed for fast-moving teams looking to preserve institutional memory and improve operational efficiency.

- **Operations Managers**
    - Automate the documentation of recurring processes and team decisions.
- **Engineering Leads**
    - Ensure technical documentation and architectural discussions are easily discoverable.
- **HR & People Ops**
    - Simplify onboarding by surfacing historical context and team policies automatically.
- **Customer Success Managers**
    - Quickly retrieve internal product knowledge to resolve client inquiries faster.

---

## Features
- **Automated Knowledge Capture**
    - Monitors designated Slack channels to identify and extract key insights and decisions.
- **Intelligent Categorization**
    - Uses AI to tag and organize extracted content by topic, project, or department.
- **Composio-Powered Slack Integration**
    - Seamlessly connects with Slack APIs to read threads and post summaries or alerts.
- **Searchable Knowledge Index**
    - Maintains a structured database of team insights that can be queried in real-time.
- **Proactive Knowledge Surfacing**
    - Automatically notifies relevant team members when new, related information is added to the repository.

---

## Use Cases
**Onboarding & Training**
- Automatically generate "getting started" summaries for new hires based on historical project discussions.
- Surface relevant documentation links when common onboarding questions are asked in Slack.

**Project Post-Mortems**
- Extract key takeaways and action items from project-specific Slack channels after a milestone.
- Compile historical decision logs to provide context for future project planning.

**Internal Support Triage**
- Identify recurring technical questions in support channels to flag them for documentation updates.
- Provide instant answers to team members by querying the curated knowledge base directly via Slack.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Knowledge Sharing Curator template from the solution library.
3. Connect your Slack workspace via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers from Slack messages or manual queries.
- **Agent**: Analyzes the input, extracts key knowledge, and determines the appropriate categorization.
- **Composio Toolset**: Executes Slack API calls to fetch thread history or post updates.
- **Chat Output**: Delivers the curated summary or confirmation back to the Slack channel.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Summarize the key decisions made in the #engineering-updates channel this week.`
- `Find all discussions related to the Q4 roadmap and organize them by project.`
- `What is the current team policy on remote work as discussed in the #general channel?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a knowledge curator and summarization engine.
- **Recommended instruction pattern:**
    - "You are an expert knowledge manager. Analyze Slack threads to extract actionable insights and ignore noise."
    - "Categorize all extracted information into predefined topics: Technical, Process, or General."
    - "Maintain a professional, concise tone when summarizing discussions for the team."

### 2) Composio Toolset Node
- **API Key**: Ensure your Slack App token is configured within the Composio dashboard.
- **Connection Scope**: Grant `channels:history`, `channels:read`, and `chat:write` permissions to allow the agent to read threads and post summaries.

### 3) Tool Availability
- **Slack Read**: Access to channel history and thread metadata.
- **Slack Write**: Capability to post summaries and alerts to specific channels.
- **Knowledge Base Sync**: Integration to push structured data to your internal documentation platform.

---

## Related Solutions
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor and optimize your team's workflow efficiency.
- [../247-customer-support-assistant-by-ai-ml-api/README.md](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automate support responses using AI-driven knowledge retrieval.
- [../workshop-template-curator-by-miro/README.md](../workshop-template-curator-by-miro/README.md) - Organize and surface collaborative workshop assets.
