# Duplicate Ticket Merger (Uplizd) - Consolidate customer support tickets for streamlined resolution

## Summary
The Duplicate Ticket Merger by Uplizd is an intelligent AI workflow designed to automatically detect, analyze, and consolidate redundant customer support inquiries within Gorgias. By identifying overlapping issues from the same customer or across multiple channels, this solution ensures a single source of truth for support agents, significantly reducing ticket volume, improving response times, and maintaining high-quality customer service hygiene.

---

## Demo
![Duplicate Ticket Merger workflow showing Gorgias ticket analysis and consolidation](image.png)
**Alt text (SEO-ready):** Duplicate Ticket Merger workflow for Gorgias using Uplizd AI to automate support ticket consolidation and data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4d4e5d12-311f-5e47-ac3f-0968888d0324)

---

## Category
- **Primary category:** Support automation
- **Secondary tags:** gorgias, ticket management, customer support, data hygiene, ai workflow, composio, helpdesk, ticket consolidation
- This solution optimizes helpdesk operations by leveraging AI to clean up redundant ticket queues and improve agent focus.

---

## Who is this for?
This workflow is designed for support teams looking to eliminate manual ticket sorting and improve resolution efficiency.

- **Support Manager**
    - Reduces ticket backlog and improves team response time metrics by eliminating redundant work.
- **Customer Experience Lead**
    - Ensures a consistent, unified conversation history for customers by merging fragmented inquiries.
- **Support Operations Specialist**
    - Maintains high data hygiene within the Gorgias helpdesk by automating the identification of duplicate threads.
- **Helpdesk Agent**
    - Prevents context switching and confusion by providing a single, consolidated view of all customer issues.

---

## Features
- **Intelligent Deduplication**
    - Uses semantic analysis to identify tickets with similar subject lines or content across different channels.
- **Automated Merging Logic**
    - Automatically combines duplicate tickets into a primary thread while preserving all customer communication history.
- **Gorgias Integration**
    - Leverages the Composio Toolset to interact directly with Gorgias APIs for real-time ticket updates.
- **Customizable Thresholds**
    - Allows users to define sensitivity levels for what constitutes a "duplicate" to prevent accidental merging.
- **Audit Trail Logging**
    - Maintains a clear record of merged tickets, ensuring transparency and easy retrieval of historical data.

---

## Use Cases
**Support Queue Optimization**
- Automatically merging multiple emails from the same user regarding a single order status inquiry.
- Consolidating social media comments and direct messages that refer to the same support ticket ID.

**Agent Productivity Enhancement**
- Reducing the number of open tickets an agent needs to review by grouping related issues into a single workspace.
- Preventing multiple agents from accidentally responding to the same customer issue simultaneously.

**Data Hygiene & Reporting**
- Cleaning up Gorgias ticket exports to ensure accurate reporting on unique customer issues.
- Removing noise from the support dashboard to focus on high-priority, unique customer concerns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Gorgias account via the Composio Toolset node.
3. Configure your preferred trigger settings for ticket monitoring.
4. Ensure nodes are correctly linked from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming ticket data or manual trigger signals.
- **Agent**: Analyzes ticket content for semantic similarity and determines merge eligibility.
- **Composio Toolset**: Executes the API calls to Gorgias to merge identified duplicate tickets.
- **Chat Output**: Confirms the merge action and provides a summary of the consolidated ticket.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Check for duplicate tickets from the last 24 hours and merge them.`
- `Identify any redundant tickets related to order #12345 and consolidate them.`
- `Scan the support queue for tickets with similar subject lines and merge them into the oldest thread.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the decision-maker for ticket similarity.
- **Instruction Pattern:**
    - Analyze the subject and body of incoming tickets to detect overlapping intent.
    - Prioritize the oldest ticket as the "primary" thread for consolidation.
    - Flag any ambiguous cases for manual review rather than merging automatically.

### 2) Composio Toolset Node
- **API Key:** Provide your Gorgias API credentials within the Composio dashboard.
- **Connection Scope:** Ensure the agent has read/write access to `tickets`, `messages`, and `customers` endpoints.

### 3) Tool Availability
- `gorgias_list_tickets`: Fetches recent tickets for comparison.
- `gorgias_merge_tickets`: Performs the consolidation of identified duplicates.
- `gorgias_get_ticket_details`: Retrieves full context for accurate similarity matching.

---

## Related Solutions
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Automate initial customer inquiries with an AI-driven chatbot.
- [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Manage and organize support tickets originating from WhatsApp.
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Enhance overall support team efficiency with an AI assistant.
