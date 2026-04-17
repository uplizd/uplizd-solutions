# Knowledge Base Curator (Uplizd) - Automate and structure team knowledge into searchable wikis

## Summary
The Knowledge Base Curator is an intelligent Uplizd workflow designed to streamline documentation management by automatically organizing, tagging, and structuring unstructured team data into a centralized, searchable wiki. By leveraging AI to synthesize information from disparate sources, this solution reduces knowledge silos, improves team onboarding velocity, and ensures that your internal documentation remains a reliable single source of truth.

---

## Demo
![Knowledge Base Curator workflow diagram showing data ingestion, AI processing, and Notion wiki organization](image.png)
**Alt text (SEO-ready):** Knowledge Base Curator workflow diagram showing data ingestion, AI processing, and Notion wiki organization using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/24ed42f8-91f5-5999-8eac-8b3c712ac0c6)

---

## Category
**Primary category:** Operations
**Secondary tags:** knowledge management, notion, documentation, ai workflow, data organization, team collaboration, composio, wiki

This solution bridges the gap between scattered team communications and structured documentation, enabling automated knowledge lifecycle management.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual documentation overhead and improve information accessibility.

*   **Operations Managers**
    *   Standardize documentation workflows to ensure consistent team processes.
*   **Knowledge Managers**
    *   Automate the categorization and tagging of new content to maintain wiki hygiene.
*   **Technical Leads**
    *   Quickly convert technical notes and Slack threads into structured, searchable wiki pages.
*   **HR & Onboarding Specialists**
    *   Ensure new hires have immediate access to up-to-date company policies and project history.

---

## Features
- **Automated Content Synthesis**
  AI-driven summarization that converts raw meeting notes and chat transcripts into structured wiki articles.
- **Intelligent Tagging System**
  Automatically applies relevant metadata and labels to documentation for improved searchability and retrieval.
- **Notion Integration**
  Seamlessly pushes structured content directly into your Notion workspace using the Composio Toolset.
- **Real-time Syncing**
  Ensures that documentation remains current by triggering updates whenever new project data is ingested.
- **Knowledge Gap Detection**
  Identifies missing information or outdated sections within your existing wiki to prompt timely updates.

---

## Use Cases
**Documentation Maintenance**
*   Automatically convert weekly sprint retrospective notes into updated project wiki pages.
*   Archive outdated documentation versions to keep the primary knowledge base clean and relevant.

**Onboarding & Training**
*   Aggregate scattered technical documentation into a centralized "New Hire" handbook.
*   Generate searchable FAQ modules based on common support queries and internal communications.

**Cross-Functional Alignment**
*   Sync product requirement documents (PRDs) across engineering and marketing workspaces.
*   Centralize feedback loops from customer success teams into actionable product insights.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Knowledge Base Curator template from the solution library.
3. Connect your Notion account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw text, meeting transcripts, or document links.
*   **Agent**: Processes the input, extracts key information, and formats it for the wiki.
*   **Composio Toolset**: Executes the API calls to create or update pages in Notion.
*   **Chat Output**: Confirms successful documentation creation or notifies the user of errors.

### 3) Run the Flow
Use the Playground to test your curator with the following prompts:
* `Summarize the attached meeting transcript and create a new 'Project Alpha' page in Notion.`
* `Update the 'Onboarding' wiki page with these new security policy guidelines.`
* `Find all documents tagged 'Engineering' and generate a summary report of recent updates.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the content architect, ensuring all data is structured and formatted correctly.
*   Adopt a professional, clear, and concise tone for all documentation.
*   Prioritize extracting actionable items and key decisions from raw input.
*   Maintain consistent formatting (headers, bullet points, and tables) for all Notion outputs.

### 2) Composio Toolset Node
Requires a valid Notion API key and appropriate workspace permissions to create and edit pages. Ensure the connection scope includes "Read and Write" access to the target databases.

### 3) Tool Availability
*   **Notion API**: Page creation, block appending, and database querying.
*   **Text Processing**: Markdown conversion and entity extraction.
*   **Search/Retrieval**: Cross-referencing existing wiki entries to prevent duplicates.

---

## Related Solutions
* [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Automate the organization of collaborative workshop templates.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather and structure account intelligence for sales teams.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and report on the status of your internal team workflows.
