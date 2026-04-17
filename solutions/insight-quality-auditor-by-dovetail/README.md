# Insight Quality Auditor (Uplizd) - Automate research insight validation and data completeness

## Summary
The Insight Quality Auditor is an intelligent Uplizd workflow designed to evaluate research insights against predefined quality standards and completeness criteria. By leveraging AI-driven analysis, this solution ensures that qualitative data captured in platforms like Dovetail remains consistent, actionable, and free of ambiguity, significantly reducing the manual effort required for research operations and data hygiene.

---

## Demo
![Insight Quality Auditor workflow interface showing automated validation of research notes and metadata](image.png)
**Alt text (SEO-ready):** Insight Quality Auditor (Uplizd) workflow for automated research data validation, insight completeness, and qualitative data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bb222487-9b72-501f-a959-59dec3407968)

---

## Category
**Primary category:** Data Operations
**Secondary tags:** research, data hygiene, insight management, quality assurance, ai workflow, composio, automation, qualitative analysis.
This solution streamlines research operations by automating the audit process for qualitative insights, ensuring high-quality data standards across the organization.

---

## Who is this for?
This solution is designed for research and operations teams looking to maintain high-integrity data repositories.

- **UX Researchers**
    - Ensure that all captured insights contain sufficient context and evidence before being added to the research repository.
- **Research Operations Managers**
    - Standardize the quality of incoming data across distributed teams to maintain a single source of truth.
- **Product Managers**
    - Rely on verified, high-quality insights to make data-backed product decisions without manual vetting.
- **Data Analysts**
    - Reduce time spent cleaning and normalizing qualitative datasets by automating the initial quality audit.

---

## Features
- **Automated Quality Scoring**
    - Evaluates insights based on clarity, evidence support, and relevance to research goals using advanced LLM analysis.
- **Completeness Verification**
    - Automatically checks for missing metadata, tags, or required fields to ensure no insight is left incomplete.
- **Real-time Feedback Loop**
    - Provides immediate suggestions to researchers on how to improve insight quality directly within the workflow.
- **Composio Toolset Integration**
    - Seamlessly connects with research platforms and CRM tools to pull and push audit results in real-time.
- **Customizable Audit Rules**
    - Allows teams to define specific quality benchmarks and threshold scores tailored to their unique research methodology.

---

## Use Cases
**Research Repository Governance**
- Automatically flagging insights that lack supporting documentation or source links.
- Standardizing tag taxonomy by identifying and suggesting corrections for non-compliant labels.

**Team Productivity & Training**
- Providing automated coaching to junior researchers by highlighting common gaps in insight documentation.
- Reducing the time spent by senior leads on manual peer reviews of research notes.

**Data Integrity & Compliance**
- Ensuring all qualitative data meets organizational privacy and formatting standards before storage.
- Maintaining a clean, searchable research database by filtering out low-value or duplicate entries.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Insight Quality Auditor template from the library.
3. Connect your preferred research platform via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw insight text and associated metadata.
- **Agent**: Analyzes the input against quality rubrics and generates feedback.
- **Composio Toolset**: Executes API calls to update the research platform with audit status.
- **Chat Output**: Delivers the final audit report and improvement recommendations to the user.

### 3) Run the Flow
Use the Playground to test the auditor with the following prompts:
- `Audit the latest research note from the 'User Interviews' project for completeness.`
- `Check if the insight titled 'Mobile Navigation Issues' meets our quality threshold.`
- `Review all pending insights and provide a summary of missing metadata fields.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary auditor, applying research standards to incoming data.
- **Instruction Pattern**:
    - Act as a senior research operations specialist focused on data quality.
    - Evaluate the input based on the provided rubric (clarity, evidence, context).
    - Provide constructive, actionable feedback for any insight that fails the audit.

### 2) Composio Toolset Node
- **API Key**: Ensure your research platform API key is securely stored in the Composio configuration.
- **Connection Scope**: Grant read/write permissions for the specific projects or workspaces you intend to audit.

### 3) Tool Availability
- **Read Operations**: Fetching raw notes, tags, and existing metadata.
- **Write Operations**: Updating insight status, adding audit tags, or posting comments.
- **Search Operations**: Querying the repository for related insights to check for duplicates.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automates the auditing of account configurations and compliance.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational health and efficiency of your automated workflows.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregates and reports on account-level data for better research insights.
