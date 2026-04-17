# Research Project Manager (Uplizd) - Streamline research workflows and centralize project insights

## Summary
The Research Project Manager (Uplizd) is an intelligent automation workflow designed to streamline the lifecycle of research projects by integrating Dovetail with your existing data stack. By automating the ingestion, categorization, and synthesis of research findings, this solution provides a single source of truth for product teams, significantly increasing pipeline velocity and ensuring research hygiene across complex project datasets.

---

## Demo
![Research Project Manager workflow interface showing Dovetail integration nodes and automated insight synthesis](image.png)
**Alt text (SEO-ready):** Uplizd Research Project Manager workflow showing automated Dovetail data ingestion, research categorization, and insight synthesis for product teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e7d8be52-3bbb-5af4-ba1f-7ebe76277399)

---

## Category
- **Primary category:** Product operations
- **Secondary tags:** research, dovetail, knowledge management, insights, product management, data synthesis, composio, ai workflow
- This solution bridges the gap between raw user feedback and actionable product strategy by automating the research documentation process.

---

## Who is this for?
This solution is built for teams looking to eliminate manual data entry and accelerate the time-to-insight for user research.

- **Product Managers**
    - Automate the synthesis of user interviews to prioritize product roadmaps based on real-time feedback.
- **UX Researchers**
    - Reduce time spent on administrative tagging and organization, allowing more focus on high-level analysis.
- **Product Designers**
    - Quickly retrieve specific user pain points and feature requests directly from the research repository.
- **Customer Success Leads**
    - Align customer feedback loops with research initiatives to ensure high-priority issues are addressed in product cycles.

---

## Features
- **Automated Data Ingestion**
    - Seamlessly pull raw research notes and interview transcripts into your project workspace using the Composio Toolset.
- **Intelligent Categorization**
    - Automatically tag and sort research findings by theme, sentiment, and product area to maintain high data hygiene.
- **Real-time Insight Synthesis**
    - Leverage LLMs to generate executive summaries and actionable takeaways from unstructured research data.
- **Cross-Platform Sync**
    - Maintain consistency between your research repository and project management tools to ensure visibility across the organization.
- **Customizable Workflow Logic**
    - Adapt the agent's processing rules to fit specific research methodologies, from discovery interviews to usability testing.

---

## Use Cases
**Project Setup & Organization**
- Automatically create and structure new research projects in Dovetail based on incoming interview data.
- Organize disparate research notes into standardized project folders based on product feature tags.

**Research Synthesis**
- Generate concise summaries of long-form user interviews to highlight recurring user pain points.
- Extract and categorize specific feature requests from raw transcriptions for immediate product team review.

**Knowledge Retrieval**
- Query historical research data to find past insights related to specific user segments or product areas.
- Maintain a searchable index of research findings that updates automatically as new data is processed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Research Project Manager template from the solution library.
3. Connect your Dovetail account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your research project parameters or specific query.
- **Agent**: Processes the input, determines the research scope, and orchestrates the tool calls.
- **Composio Toolset**: Executes the API calls to fetch, organize, or update research data in Dovetail.
- **Chat Output**: Delivers the synthesized research insights or project status updates back to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Summarize the key user pain points from the latest 'Q3 Onboarding' research project.`
- `Create a new research project in Dovetail titled 'Mobile App Navigation' and import the latest transcript.`
- `Find all insights related to 'search functionality' across all active research projects.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research coordinator, ensuring data is parsed and synthesized accurately.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for complex synthesis.
- Set the system prompt to prioritize objective data extraction over subjective interpretation.
- Configure the temperature to 0.2 to ensure consistent and reproducible research summaries.

### 2) Composio Toolset Node
- Provide your Dovetail API key within the Composio configuration.
- Ensure the connection scope includes read/write access to your research projects and notes.

### 3) Tool Availability
- **Dovetail Fetcher**: Retrieve project lists, notes, and transcriptions.
- **Dovetail Writer**: Create new projects and update existing research entries.
- **Data Processor**: Perform text analysis, categorization, and summarization tasks.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate account intelligence gathering and research.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed reports on account activity and insights.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform project and workflow management.
