# Content Lifecycle Manager (Uplizd) - Automate documentation maintenance and content freshness

## Summary
The Content Lifecycle Manager is an intelligent Uplizd workflow designed to automate the maintenance, auditing, and archival processes of your documentation within Confluence. By leveraging AI-driven triggers, it ensures that your knowledge base remains accurate, relevant, and compliant, effectively reducing manual overhead for content managers and improving overall pipeline velocity for documentation teams.

---

## Demo
![Content Lifecycle Manager dashboard showing automated audit logs and status updates for Confluence pages](image.png)
**Alt text (SEO-ready):** Content Lifecycle Manager dashboard showing automated audit logs and status updates for Confluence pages, Uplizd workflow, Confluence integration, and automated content maintenance.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5f2959ac-212d-5f5b-82a9-1d3627fd334b)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** confluence, content management, documentation, lifecycle, automation, ai workflow, composio, knowledge base.
This solution bridges the gap between static documentation and dynamic content management by automating lifecycle triggers based on page age and relevance.

---

## Who is this for?
This solution is designed for teams managing large-scale documentation repositories who need to maintain high standards of content hygiene.

*   **Technical Writers**
    *   Automate the identification of stale documentation that requires review or updates.
*   **Knowledge Managers**
    *   Maintain a single source of truth by enforcing lifecycle policies across all Confluence spaces.
*   **Product Marketers**
    *   Ensure product-facing documentation stays synchronized with the latest feature releases.
*   **Compliance Officers**
    *   Track and audit document versioning to meet internal governance and regulatory requirements.

---

## Features
- **Automated Stale Content Detection**
    Identify pages that haven't been updated within a specific timeframe using real-time Confluence API monitoring.
- **Intelligent Review Workflows**
    Automatically assign review tasks to content owners based on document metadata and last-modified timestamps.
- **Bulk Archival Capabilities**
    Execute batch archival or deletion of deprecated content to keep the knowledge base clean and searchable.
- **Composio-Powered Integration**
    Utilize the Composio Toolset to securely interact with Confluence APIs for seamless page updates and status changes.
- **Customizable Lifecycle Policies**
    Define granular rules for content expiration, notification triggers, and automated cleanup actions.

---

## Use Cases
**Content Hygiene & Maintenance**
*   Automatically flag documentation older than 6 months for a mandatory content refresh.
*   Archive outdated release notes that are no longer relevant to current product versions.

**Compliance & Governance**
*   Generate audit reports for all pages modified in the last quarter to ensure policy adherence.
*   Verify that all public-facing documentation contains the latest legal disclaimers and version tags.

**Team Productivity**
*   Notify content owners via Slack or Email when a page is flagged for an upcoming lifecycle review.
*   Automate the transition of draft content to published status once review workflows are completed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Lifecycle Manager template from the solution library.
3. Connect your Confluence account via the Composio Toolset configuration.
4. Ensure nodes (Chat Input, Agent, Composio Toolset, Chat Output) are correctly linked in the canvas.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual audit command.
*   **Agent**: Processes the lifecycle rules and determines the required action for each page.
*   **Composio Toolset**: Executes the specific Confluence API calls to fetch, update, or archive pages.
*   **Chat Output**: Returns a summary report of all actions taken during the lifecycle audit.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
* `Audit all pages in the 'Product' space that haven't been updated in 90 days.`
* `Archive all pages tagged with 'deprecated' in the 'Engineering' space.`
* `List all pages currently pending review for the 'Marketing' team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for content governance.
*   Focus on identifying stale content patterns and mapping them to predefined lifecycle actions.
*   Maintain a neutral, professional tone for all audit logs and notification messages.
*   Prioritize data accuracy when interacting with Confluence page metadata.

### 2) Composio Toolset Node
*   **API Key**: Provide your Confluence API credentials within the secure Composio connection settings.
*   **Connection Scope**: Ensure the agent has 'Read' and 'Write' permissions for the target Confluence spaces.

### 3) Tool Availability
*   **Confluence Search**: Find pages based on labels, dates, or content keywords.
*   **Page Metadata Fetcher**: Retrieve last-modified dates and author information.
*   **Content Updater**: Modify page status, labels, or move content to the archive space.

---

## Related Solutions
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Streamline account intelligence gathering.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor and optimize team workflow performance.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and prioritize operational tasks.
