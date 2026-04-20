# Team Knowledge Curator (Uplizd) - Automate documentation and search across Google Drive

## Summary
The Team Knowledge Curator is an intelligent Uplizd workflow that bridges the gap between scattered Google Drive assets and actionable team insights. By leveraging AI to index, categorize, and retrieve information, this solution eliminates manual search time, ensures a single source of truth for internal documentation, and accelerates pipeline velocity by providing instant access to critical project data.

---

## Demo
![Team Knowledge Curator workflow interface showing Google Drive integration and AI-powered document retrieval](image.png)

**Alt text (SEO-ready):** Team Knowledge Curator Uplizd workflow, Google Drive AI document retrieval, automated knowledge management system, and enterprise search integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7843fc8a-5038-55ab-9840-f5fa132b8726)

---

## Category
- **Primary category:** Knowledge Management
- **Secondary tags:** google drive, document automation, ai search, knowledge base, productivity, workflow automation, composio, enterprise search
- This solution centralizes fragmented information into a unified, AI-driven knowledge hub to improve organizational data hygiene and retrieval speed.

---

## Who is this for?
This solution is designed for teams struggling with information silos and document sprawl.

- **Operations Manager**
    - Reduces time spent manually locating process documentation and internal policy updates.
- **Project Lead**
    - Ensures team members have immediate access to the latest project specs and status reports.
- **Sales Enablement Specialist**
    - Quickly surfaces collateral and case studies stored in shared drives for prospect outreach.
- **HR Coordinator**
    - Automates the retrieval of onboarding materials and employee handbooks for new hires.

---

## Features
- **Intelligent Document Indexing**
    - Automatically scans and categorizes files from Google Drive to maintain a searchable knowledge graph.
- **Natural Language Querying**
    - Uses the Agent node to interpret complex user questions and retrieve precise document excerpts.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interface with Google Drive APIs for real-time data access.
- **Context-Aware Summarization**
    - Provides concise, relevant summaries of long documents, saving time on deep-reading lengthy reports.
- **Automated Knowledge Sync**
    - Ensures that the most recent versions of documents are always prioritized during search queries.

---

## Use Cases
**Internal Process Documentation**
- Retrieve specific compliance or HR policy details from nested folders.
- Summarize updated SOPs to ensure team alignment on new workflows.

**Project & Sales Enablement**
- Locate the latest version of a client pitch deck or technical specification.
- Extract key project milestones from historical meeting notes stored in Drive.

**Onboarding & Training**
- Provide instant answers to common new-hire questions based on internal wikis.
- Aggregate training materials into a structured summary for new team members.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Team Knowledge Curator template from the solution library.
3. Connect your Google Drive account via the Composio integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's natural language question regarding internal knowledge.
- **Agent**: Processes the query and determines which documents to search within Google Drive.
- **Composio Toolset**: Executes the search and retrieval commands across your connected Drive folders.
- **Chat Output**: Delivers the synthesized answer or document link back to the user.

### 3) Run the Flow
Use the Playground to test your knowledge retrieval:
- `Find the latest project roadmap for the Q4 marketing campaign.`
- `What is our current internal policy regarding remote work expenses?`
- `Summarize the key takeaways from the Q3 product launch meeting notes.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for interpreting search intent and summarizing retrieved data.
- **Instruction Pattern:**
    - Always prioritize the most recently modified documents in Google Drive.
    - If a document is too large, provide a concise summary followed by a link to the source file.
    - Maintain a professional and helpful tone when responding to internal team queries.

### 2) Composio Toolset Node
- **API Key:** Ensure your Composio API key is active and authorized for Google Drive read-only scopes.
- **Connection Scope:** Limit access to specific shared drives or folders to maintain data security.

### 3) Tool Availability
- **Google Drive Search:** Capability to query filenames, folder structures, and document content.
- **Document Reader:** Capability to extract text from PDFs, Google Docs, and Sheets.
- **Metadata Filter:** Capability to sort results by date, author, or file type.

---

## Related Solutions
- [Workshop Template Curator (Miro)](../workshop-template-curator-by-miro/README.md) — Organize and retrieve collaborative workshop assets.
- [Account Research Assistant (ZoomInfo)](../account-research-assistant-by-zoominfo/README.md) — Gather external account intelligence to complement internal knowledge.
- [Workflow Health Monitor (DailyBot)](../workflow-health-monitor-by-dailybot/README.md) — Track the efficiency of internal team processes.
