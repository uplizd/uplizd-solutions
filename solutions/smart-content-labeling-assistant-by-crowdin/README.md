# Smart Content Labeling Assistant (Uplizd) - Automated localization and translation string management

## Summary
The Smart Content Labeling Assistant leverages the Uplizd AI workflow to automatically categorize, tag, and organize translation strings within Crowdin. By streamlining content metadata management, this solution ensures translation teams maintain high-quality localization pipelines, reduce manual sorting time, and achieve a single source of truth for global content assets.

---

## Demo
![Smart Content Labeling Assistant workflow showing automated Crowdin string categorization and tagging](image.png)
**Alt text (SEO-ready):** Smart Content Labeling Assistant by Uplizd for automated Crowdin translation string categorization, tagging, and localization workflow management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dd2d9bfa-da36-5df7-a38a-bb972657d435)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** crowdin, localization, content management, ai workflow, data hygiene, automation, composio, translation
This solution integrates AI-driven intelligence into your localization stack to ensure translation strings are accurately labeled and ready for global deployment.

---

## Who is this for?
This solution is designed for teams managing multilingual content at scale who need to reduce the overhead of manual string organization.

* **Localization Manager**
    * Automates the categorization of incoming translation requests to ensure faster project turnaround.
* **Content Strategist**
    * Maintains consistent taxonomy across global assets by enforcing automated labeling standards.
* **Translation Lead**
    * Reduces manual triage time by allowing the AI to pre-sort strings based on context and priority.
* **Operations Specialist**
    * Improves pipeline velocity by syncing Crowdin metadata directly with internal content management systems.

---

## Features
- **Automated String Classification**
    * Uses AI to analyze string context and assign relevant tags or categories automatically within Crowdin.
- **Real-time Metadata Sync**
    * Ensures that labels and categories are updated instantly across your localization projects via the Composio Toolset.
- **Context-Aware Labeling**
    * Leverages LLM reasoning to understand the intent behind strings, reducing miscategorization common in manual workflows.
- **Bulk Processing Capability**
    * Handles large volumes of translation strings efficiently, ensuring consistent hygiene across massive project files.
- **Customizable Taxonomy Support**
    * Allows users to define specific labeling rules that align with existing brand and product content structures.

---

## Use Cases
**Localization Pipeline Optimization**
* Automatically tagging new strings based on product feature modules for faster developer handoff.
* Sorting translation requests by priority level to ensure critical UI text is localized first.

**Content Hygiene & Maintenance**
* Identifying and flagging legacy strings that no longer match current product terminology.
* Cleaning up untagged or orphaned translation keys to maintain a structured Crowdin project.

**Global Marketing Coordination**
* Categorizing marketing copy by region or campaign to simplify the workflow for regional translation teams.
* Ensuring consistent brand voice by applying specific tags to strings destined for high-visibility landing pages.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Crowdin account through the authorized integration portal.
3. Configure your project-specific API keys within the workflow settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger or batch of translation strings to be processed.
* **Agent**: Analyzes the content and determines the appropriate labels based on your defined taxonomy.
* **Composio Toolset**: Executes the API calls to update string metadata directly in Crowdin.
* **Chat Output**: Returns a summary report of all labeled strings and any exceptions encountered.

### 3) Run the Flow
Use the Playground to test your labeling logic with these prompts:
* `Label all untagged strings in project 'Mobile-App-v2' as 'UI-Component' if they contain button text.`
* `Scan the latest batch of strings and categorize them by priority: High for checkout flows, Low for footer text.`
* `Identify any strings missing a category tag and apply the 'Needs-Review' label.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for interpreting string context.
* Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5).
* Provide a clear list of your internal taxonomy and tag definitions in the system prompt.
* Instruct the agent to prioritize accuracy over speed when dealing with ambiguous UI strings.

### 2) Composio Toolset Node
* Provide your Crowdin API key to enable secure read/write access to your projects.
* Ensure the connection scope includes `project.strings.update` and `project.strings.list` permissions.

### 3) Tool Availability
* **Crowdin String Manager**: For fetching, listing, and updating translation string metadata.
* **Project Metadata Inspector**: For retrieving current project tag structures and existing categories.
* **Bulk Update Handler**: For processing multiple string modifications in a single execution cycle.

---

## Related Solutions
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Ensures content meets global accessibility standards.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enriches customer data for better localization targeting.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose automation for complex business processes.
