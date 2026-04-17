# Knowledge Base Content Curator (Uplizd) - Automate help article creation from support insights

## Summary
The Knowledge Base Content Curator is an intelligent Uplizd workflow that transforms raw support conversations into structured, searchable help center articles. By leveraging AI to extract recurring themes and solutions from Intercom tickets, this solution ensures your knowledge base stays current, reduces repetitive support volume, and maintains a single source of truth for customer documentation.

---

## Demo
![Knowledge Base Content Curator workflow diagram showing Intercom ticket ingestion, AI summarization, and automated article publishing](image.png)
**Alt text (SEO-ready):** Knowledge Base Content Curator workflow diagram showing Intercom ticket ingestion, AI summarization, and automated article publishing via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ec07a52e-179f-50ff-9c48-f5634929168b)

---

## Category
- **Primary category:** Knowledge Management
- **Secondary tags:** intercom, content curation, help desk, documentation, ai workflow, knowledge base, customer support, automation
- This solution streamlines the lifecycle of support documentation by bridging the gap between customer inquiries and self-service resources.

---

## Who is this for?
This solution is designed for support teams and documentation managers looking to scale their self-service capabilities without manual overhead.

- **Support Operations Manager**
    - Automates the identification of knowledge gaps to reduce ticket volume.
- **Technical Writer**
    - Receives AI-drafted content based on real-world customer interactions.
- **Customer Success Lead**
    - Ensures customers have immediate access to accurate, up-to-date troubleshooting steps.
- **Product Manager**
    - Gains insights into recurring product friction points through aggregated support data.

---

## Features
- **Automated Ticket Analysis**
    - Uses AI to scan Intercom conversations for recurring questions and unresolved issues.
- **Intelligent Content Drafting**
    - Generates structured help articles including problem statements, steps, and resolutions.
- **Real-time Sync**
    - Connects directly to your knowledge base to push updates or create new drafts instantly.
- **Contextual Awareness**
    - Preserves tone and style guidelines while ensuring technical accuracy from support logs.
- **Feedback Loop Integration**
    - Flags articles for human review before publishing to ensure high-quality documentation.

---

## Use Cases
**Support Ticket Deflection**
- Automatically generate FAQ articles for common "how-to" questions found in recent tickets.
- Update existing help docs with new troubleshooting steps derived from successful support resolutions.

**Knowledge Base Maintenance**
- Identify outdated help articles by comparing them against current support conversation trends.
- Batch-process support logs to create comprehensive guides for new product feature releases.

**Content Quality Assurance**
- Draft summaries of complex technical issues for internal team training and knowledge sharing.
- Standardize formatting across all help center articles using AI-driven template enforcement.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided Knowledge Base Content Curator JSON configuration.
3. Connect your Intercom and Knowledge Base API credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input:** Receives the trigger signal or manual request to audit recent support tickets.
- **Agent:** Analyzes conversation transcripts and synthesizes them into structured documentation.
- **Composio Toolset:** Executes API calls to fetch Intercom data and push content to your help center.
- **Chat Output:** Confirms the creation of the draft or notifies the team of new content ready for review.

### 3) Run the Flow
Use the Playground to test your curation logic with these prompts:
- `Analyze the last 24 hours of Intercom tickets and draft a new help article for the login issue.`
- `Review the 'Billing' category and suggest updates based on the top 5 most common customer questions.`
- `Create a draft article for the new API integration based on the support logs from the last week.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical documentation specialist.
- **Role:** Expert Technical Writer and Support Analyst.
- **Instruction Pattern:**
    - Focus on clarity, conciseness, and actionable troubleshooting steps.
    - Extract only verified solutions from support conversation transcripts.
    - Maintain the brand voice and formatting standards of the existing knowledge base.

### 2) Composio Toolset Node
- **API Key:** Ensure your Intercom and Knowledge Base provider keys are active.
- **Connection Scope:** Grant read access to support tickets and write access to your help center documentation.

### 3) Tool Availability
- **Intercom API:** Fetch conversation threads, tags, and customer metadata.
- **Knowledge Base API:** Create, update, and retrieve existing help articles.
- **Semantic Search:** Identify existing articles that may overlap with new content to prevent duplicates.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automate responses to incoming customer support queries.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Deploy a conversational chatbot for instant customer assistance.
- [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Manage and track support tickets directly via WhatsApp.
