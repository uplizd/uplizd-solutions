# Content Review Coordinator (Uplizd) - Automate feedback loops and content approval workflows

## Summary
The Content Review Coordinator is an intelligent Uplizd AI workflow designed to streamline content production cycles by automating feedback collection, version tracking, and stakeholder approvals. By integrating directly with Google Drive, this solution eliminates manual status updates and email bottlenecks, providing a single source of truth for marketing teams to accelerate content velocity and ensure brand compliance.

---

## Demo
![Content Review Coordinator workflow diagram showing Google Drive integration and automated feedback loops](image.png)
**Alt text (SEO-ready):** Content Review Coordinator workflow diagram showing Uplizd AI integration with Google Drive for automated content feedback, version control, and marketing approval pipelines.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d7574774-af2b-5f3d-bdf6-56054054e76c)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content management, google drive, workflow automation, feedback loop, marketing, composio, ai workflow, collaboration
- This solution bridges the gap between creative production and stakeholder approval by automating file management and review notifications.

---

## Who is this for?
This solution is designed for teams looking to remove friction from their creative review processes and improve cross-departmental alignment.

- **Content Managers**
    - Centralize feedback from multiple stakeholders to reduce revision cycles and meet publishing deadlines.
- **Marketing Leads**
    - Maintain visibility into content status and approval stages across diverse campaigns without manual tracking.
- **Creative Designers**
    - Receive structured, actionable feedback directly within the project environment to minimize context switching.
- **Operations Specialists**
    - Standardize the review pipeline to ensure all content meets brand hygiene and compliance requirements before launch.

---

## Features
- **Automated Feedback Aggregation**
    - Centralizes comments and suggestions from Google Drive files into a unified dashboard for streamlined processing.
- **Real-time Status Tracking**
    - Monitors file changes and review status updates, triggering automated notifications to relevant stakeholders.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interact with Google Drive APIs for seamless file management and permission handling.
- **Version Control Management**
    - Automatically tags and organizes document versions to prevent confusion during the final approval phase.
- **Smart Approval Routing**
    - Routes content to the appropriate approver based on predefined rules, ensuring the right eyes are on the right assets.

---

## Use Cases
**Content Production Cycles**
- Automatically notify stakeholders when a new draft is uploaded to a shared Google Drive folder.
- Consolidate feedback comments into a summary report to guide the next iteration of the content.

**Brand Compliance Audits**
- Flag content that has not been reviewed by the legal or brand team within a specific timeframe.
- Archive approved assets into a "Finalized" folder to maintain a clean and organized content repository.

**Cross-Departmental Collaboration**
- Sync review status between the creative team and sales enablement to ensure collateral is always up-to-date.
- Trigger alerts for urgent revisions when a campaign launch date is approaching.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Review Coordinator template from the library.
3. Connect your Google Drive account via the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the file link or project name from the user.
- **Agent**: Analyzes the request and determines the necessary review or feedback action.
- **Composio Toolset**: Executes the specific Google Drive operations (read, comment, move).
- **Chat Output**: Delivers the confirmation or summary of the review action to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check the status of the 'Q3 Campaign' folder in Google Drive.`
- `Summarize the latest feedback on the 'Product Launch' document.`
- `Move all approved files in the 'Drafts' folder to the 'Finalized' directory.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your review process.
- Use a model capable of high-context reasoning for summarizing feedback.
- **Recommended instruction pattern:**
    - "You are a Content Review Assistant that manages file status and feedback."
    - "Always verify file permissions before attempting to read or move documents."
    - "Summarize feedback clearly, highlighting actionable items for the creative team."

### 2) Composio Toolset Node
- Provide your API key to enable the Google Drive integration.
- Set the connection scope to allow read/write access to the specific folders used for content reviews.

### 3) Tool Availability
- **File Retrieval**: Fetching document content and metadata.
- **Comment Extraction**: Parsing feedback from Google Docs/Drive.
- **Folder Management**: Moving and organizing files based on review status.
- **Notification Trigger**: Sending updates to the Chat Output node.

---

## Related Solutions
- [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) — Automate the publishing and distribution of video content.
- [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Ensure content meets accessibility standards during the review process.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose automation for managing complex business processes.
