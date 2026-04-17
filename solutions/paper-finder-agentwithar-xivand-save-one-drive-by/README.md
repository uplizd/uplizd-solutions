# Paper Finder Agent (Uplizd) - Automate arXiv research discovery and cloud storage

## Summary
The Paper Finder Agent is an intelligent Uplizd workflow designed to streamline academic research by automating the discovery of scientific papers via arXiv and instantly archiving relevant findings to Microsoft OneDrive. By bridging real-time research databases with personal cloud storage, this solution eliminates manual download tasks, ensures a centralized repository for literature reviews, and accelerates the knowledge-gathering phase for students, researchers, and data-driven professionals.

---

## Demo
![Paper Finder Agent workflow showing arXiv search integration and OneDrive file saving](image.png)
**Alt text (SEO-ready):** Uplizd Paper Finder Agent workflow, arXiv research automation, Microsoft OneDrive integration, academic paper discovery, and automated file storage.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/08d51a03-da13-50b8-abc7-051afc911835)

---

## Category
- **Primary category:** Research automation
- **Secondary tags:** arxiv, academic research, onedrive, data sync, document management, ai workflow, composio, knowledge management
- This solution bridges the gap between open-access scientific databases and personal cloud storage to optimize research workflows.

---

## Who is this for?
This solution is designed for professionals and academics who need to maintain a structured library of scientific literature without manual intervention.

- **Academic Researchers**
    - Automate the collection of relevant papers to maintain an up-to-date literature review library.
- **Data Scientists**
    - Quickly source and store the latest pre-prints and methodologies from arXiv for model benchmarking.
- **University Students**
    - Organize research materials across specific topics directly into organized OneDrive folders.
- **Technical Writers**
    - Efficiently gather source material and documentation for white papers and technical reports.

---

## Features
- **arXiv Search Integration**
    - Leverages the Composio Toolset to query the vast arXiv database using natural language inputs.
- **Automated OneDrive Sync**
    - Automatically creates and saves PDF files or metadata summaries directly to your designated OneDrive directory.
- **Intelligent Filtering**
    - Uses the Agent node to parse search results and prioritize papers based on relevance to your specific query.
- **Real-time Workflow Execution**
    - Processes search and save requests instantly, reducing the time spent on manual file management.
- **Structured Data Handling**
    - Ensures that saved files are named and organized according to your preferences for easy retrieval later.

---

## Use Cases
**Literature Review Management**
- Automatically collect all papers related to "Large Language Model optimization" published in the last month.
- Organize research papers into specific project folders within OneDrive based on subject tags.

**Competitive Research**
- Monitor new submissions on arXiv for specific keywords to stay ahead of industry trends.
- Batch-save relevant technical papers to a shared OneDrive folder for team-wide access.

**Academic Knowledge Base**
- Build a personal repository of foundational research papers without leaving your chat interface.
- Quickly archive high-impact studies discovered during deep-dive research sessions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your arXiv and Microsoft OneDrive connections via the Composio Toolset.
4. Ensure nodes are connected in the sequence: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language research queries.
- **Agent**: Processes the query and determines the necessary search parameters.
- **Composio Toolset**: Executes the arXiv search and handles the OneDrive file upload.
- **Chat Output**: Confirms the successful storage of the paper to your cloud drive.

### 3) Run the Flow
Use the Playground to test your agent with prompts like:
- `Find the latest papers on 'transformer architectures' and save them to my 'Research' folder.`
- `Search for recent arXiv papers by author 'Yann LeCun' and upload them to OneDrive.`
- `Look for papers about 'reinforcement learning in robotics' and save the top 3 results.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your intent and the external tools.
- Set the system prompt to prioritize academic accuracy and relevance.
- Configure the agent to summarize the paper metadata before saving.
- Ensure the agent is instructed to confirm the file path in the final output.

### 2) Composio Toolset Node
- Provide your API keys for the arXiv and Microsoft OneDrive integrations.
- Set the connection scope to allow read access to arXiv and write access to your OneDrive root or specific folder.

### 3) Tool Availability
- **arXiv Search**: Capability to query by keyword, author, or category.
- **OneDrive File Management**: Capability to create files, manage folders, and upload content.

---

## Related Solutions
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) - Monitor the citation impact and reach of academic publications.
- [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) - Enhance the clarity and vocabulary of your research drafts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather and report on account-level data for professional research.
