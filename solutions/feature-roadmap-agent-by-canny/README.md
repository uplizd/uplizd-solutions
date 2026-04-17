# Feature Roadmap Agent (Uplizd) - Align product development with user feedback trends

## Summary
The Feature Roadmap Agent is an intelligent workflow designed to bridge the gap between user feedback and product development. By automatically analyzing trends from Canny, this Uplizd solution helps product teams prioritize features based on real-time customer demand, ensuring your roadmap remains data-driven, agile, and focused on the highest-impact initiatives.

---

## Demo
![Feature Roadmap Agent workflow showing feedback analysis and roadmap updates](image.png)
**Alt text (SEO-ready):** Feature Roadmap Agent by Uplizd for automated product roadmap updates using Canny feedback trends and AI-driven prioritization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/57bd2632-242a-5e1f-8cfe-7d70687c57fd)

---

## Category
- **Primary category:** Product Operations
- **Secondary tags:** product management, canny, roadmap, feedback loop, data-driven, ai workflow, prioritization, composio
- This solution streamlines the product lifecycle by converting fragmented customer feedback into actionable roadmap items.

---

## Who is this for?
This agent is designed for product teams looking to eliminate manual feedback sorting and focus on high-value feature delivery.

- **Product Managers**
    - Automate the synthesis of user requests to identify top-requested features without manual spreadsheet work.
- **Product Operations Leads**
    - Maintain a clean, up-to-date roadmap that reflects current customer sentiment and business priorities.
- **Customer Success Managers**
    - Close the feedback loop by ensuring customer-reported pain points are directly linked to roadmap progress.
- **Engineering Leads**
    - Receive prioritized feature requirements that are already validated by user demand and feedback volume.

---

## Features
- **Automated Feedback Aggregation**
    - Automatically pulls new posts and comments from Canny to ensure your analysis is always based on the latest user data.
- **AI-Driven Trend Analysis**
    - Uses advanced LLMs to cluster similar feedback requests, identifying recurring themes and high-priority feature needs.
- **Dynamic Roadmap Updates**
    - Seamlessly pushes prioritized insights into your roadmap tools, keeping stakeholders informed of development focus.
- **Real-time Prioritization Scoring**
    - Calculates feature importance based on feedback frequency and user sentiment, removing bias from the planning process.
- **Composio Toolset Integration**
    - Leverages the Composio Toolset to securely connect and interact with Canny and your project management stack.

---

## Use Cases
**Feedback Prioritization**
- Automatically tag and group incoming feature requests by category (e.g., UI/UX, Performance, New Functionality).
- Rank feature requests based on the number of unique upvotes and recent user activity windows.

**Roadmap Synchronization**
- Sync top-voted feedback items directly into your development backlog or roadmap tool.
- Update existing roadmap items with new context or user quotes gathered from recent Canny discussions.

**Stakeholder Reporting**
- Generate weekly summaries of the most requested features to present during product planning meetings.
- Create automated alerts for product teams when a specific feature request reaches a critical mass of user interest.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Canny API credentials within the Composio Toolset node.
3. Configure your target roadmap or project management integration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers or manual requests to analyze feedback.
- **Agent**: Processes feedback data and determines the priority of roadmap items.
- **Composio Toolset**: Executes API calls to Canny to fetch data and update roadmap status.
- **Chat Output**: Delivers a summary report of the updated roadmap and key feedback trends.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze the latest feedback from Canny and suggest the top 3 features to add to the roadmap.`
- `Which feature requests have gained the most momentum in the last 30 days?`
- `Update the roadmap with the latest high-priority feedback clusters identified this week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a product analyst, interpreting qualitative feedback into quantitative roadmap priorities.
- **Instruction Pattern**:
    - Focus on identifying recurring user pain points and feature requests.
    - Maintain objectivity by weighing user upvotes and sentiment equally.
    - Format output to clearly distinguish between "New Feature" and "Improvement" categories.

### 2) Composio Toolset Node
- **API Key**: Ensure your Canny API key is securely stored in your Uplizd environment variables.
- **Connection Scope**: Grant the agent read access to feedback boards and write access to your roadmap management tools.

### 3) Tool Availability
- **Feedback Fetcher**: Retrieves raw posts, comments, and upvote counts.
- **Trend Analyzer**: Clusters feedback into thematic categories.
- **Roadmap Updater**: Pushes prioritized items to your project management system.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gain deeper insights into account behavior and engagement.
- [Widget Experience Optimizer](../widget-experience-optimizer-by-productlane/README.md) — Enhance user feedback collection through optimized widget interactions.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline cross-platform operations and task management.
