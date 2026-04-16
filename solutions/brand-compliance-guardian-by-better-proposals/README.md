# Brand Compliance Guardian (Uplizd) - Automated brand standard enforcement for proposals

## Summary
The Brand Compliance Guardian is an intelligent Uplizd workflow designed to automatically audit and enforce organizational brand standards across all outgoing proposals. By leveraging the Composio Toolset to integrate with Better Proposals, this solution ensures that every document adheres to predefined style guides, tone-of-voice requirements, and visual consistency, effectively eliminating manual review bottlenecks and protecting brand equity.

---

## Demo
![Brand Compliance Guardian workflow interface showing automated proposal analysis and style enforcement](image.png)
**Alt text (SEO-ready):** Brand Compliance Guardian Uplizd workflow for automated proposal auditing, brand standard enforcement, and Better Proposals integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDwc549419QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAKwP///z8DkYABxP8H8P8/A5GAAcT/B/D/PyMRgAHE/wfw/z8jkYABxP8H8P8/IxEAAK68D/G/2/4AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/01101e1a-574b-5583-a8dd-9018b26fd484)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** brand compliance, better proposals, content governance, document automation, sales enablement, quality assurance, composio, ai workflow
- This solution bridges the gap between creative proposal generation and corporate brand governance to ensure high-quality, consistent client communications.

---

## Who is this for?
This solution is designed for teams that need to maintain strict brand integrity while scaling their sales and proposal output.

- **Brand Manager**
    - Ensures all client-facing documents align with corporate identity and style guidelines.
- **Sales Operations Lead**
    - Reduces the time spent on manual document reviews and compliance check-ins.
- **Proposal Writer**
    - Receives real-time feedback on tone and formatting to minimize revision cycles.
- **Marketing Director**
    - Protects brand reputation by automating the detection of non-compliant content.

---

## Features
- **Automated Style Auditing**
    - Scans proposal text against established brand style guides to identify deviations in tone or vocabulary.
- **Better Proposals Integration**
    - Seamlessly connects with the Better Proposals platform via the Composio Toolset to fetch and update document drafts.
- **Real-time Compliance Scoring**
    - Provides instant feedback on document readiness, highlighting specific sections that require adjustment.
- **Customizable Brand Rules**
    - Allows for the configuration of specific keywords, prohibited phrases, and formatting standards unique to your brand.
- **Workflow Automation**
    - Automatically triggers compliance checks upon document creation or before final submission to the client.

---

## Use Cases
**Brand Integrity Management**
- Automatically flagging non-compliant terminology in new proposal drafts.
- Ensuring consistent use of company-approved value propositions and taglines.

**Sales Efficiency Optimization**
- Reducing the time spent by managers on manual document proofreading.
- Accelerating the approval process for high-value sales proposals.

**Quality Assurance & Compliance**
- Maintaining a unified voice across diverse sales teams and regions.
- Generating audit logs for compliance reviews of outgoing client communications.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Brand Compliance Guardian template from the solution library.
3. Connect your Better Proposals account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the proposal ID or text content for analysis.
- **Agent**: Processes the content against your brand guidelines and identifies compliance gaps.
- **Composio Toolset**: Executes API calls to fetch document data and push suggested corrections.
- **Chat Output**: Returns the compliance report and suggested edits to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Analyze proposal ID 12345 for brand compliance and suggest corrections.`
- `Check the tone of the latest proposal draft against our professional brand guidelines.`
- `Identify any prohibited terminology in the current proposal document.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a brand auditor, focusing on precision and adherence to style guides.
- Set the system prompt to define your brand's voice (e.g., "Professional, concise, and customer-centric").
- Provide the agent with a list of mandatory and prohibited keywords.
- Configure the agent to output structured feedback, including the specific section and the suggested correction.

### 2) Composio Toolset Node
- Provide your Better Proposals API key to authorize the agent to read and modify documents.
- Set the connection scope to allow read/write access to your proposal templates and active drafts.

### 3) Tool Availability
- `get_proposal_content`: Retrieves the text and metadata of a specific proposal.
- `update_proposal_draft`: Applies suggested edits back to the Better Proposals platform.
- `list_brand_assets`: Accesses stored style guides and approved terminology lists.

---

## Related Solutions
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Monitor and ensure account data compliance.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline business processes and task management.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the creation and configuration of new accounts.
