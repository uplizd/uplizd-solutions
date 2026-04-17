# Resume Screening Agent (Uplizd) - Automated candidate evaluation and data extraction

## Summary
The Resume Screening Agent is an intelligent Uplizd workflow designed to automate the initial stages of talent acquisition by extracting, parsing, and evaluating candidate data from resumes. By leveraging the Composio Toolset to interface with document storage and ATS platforms, this solution eliminates manual data entry, reduces time-to-hire, and ensures consistent candidate scoring based on your specific job requirements.

---

## Demo
![Resume Screening Agent dashboard showing automated candidate data extraction and scoring workflow](image.png)
**Alt text (SEO-ready):** Resume Screening Agent dashboard showing automated candidate data extraction, parsing, and scoring workflow on the Uplizd platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1ea9eb3a-c399-52eb-98bd-9579f0fc3573)

---

## Category
**Primary category:** Recruiting operations
**Secondary tags:** hr, talent acquisition, resume parsing, candidate screening, automation, composio, ai workflow, data extraction.
This solution streamlines the recruitment pipeline by transforming unstructured resume documents into actionable candidate profiles.

---

## Who is this for?
This solution is built for HR professionals and hiring teams looking to scale their recruitment efforts without sacrificing quality.

*   **Recruitment Manager**
    *   Standardize candidate evaluation criteria across high-volume job postings.
*   **Talent Acquisition Specialist**
    *   Drastically reduce manual screening time by automating the extraction of key skills and experience.
*   **HR Operations Lead**
    *   Maintain clean, structured candidate data within your ATS for better reporting and pipeline visibility.
*   **Hiring Manager**
    *   Receive prioritized candidate lists to focus interviews on the most qualified applicants.

---

## Features
- **Automated Data Extraction**
  Parsing unstructured PDF and Word documents into structured JSON formats for immediate processing.
- **Intelligent Skill Matching**
  Comparing candidate experience against specific job descriptions to generate relevance scores.
- **Composio-Powered Integrations**
  Seamlessly connecting with document repositories and CRM/ATS platforms to fetch and update candidate records.
- **Real-time Scoring Logic**
  Applying custom business rules to rank candidates based on years of experience, certifications, and technical proficiencies.
- **Pipeline Velocity Tracking**
  Reducing the time from application receipt to initial screening through automated trigger-based workflows.

---

## Use Cases
**High-Volume Hiring**
*   Processing hundreds of incoming applications for entry-level roles to identify top 10% candidates.
*   Filtering candidates based on mandatory certifications or specific technical stack requirements.

**Candidate Data Hygiene**
*   Standardizing resume data formats before syncing them into your primary CRM or ATS.
*   Flagging incomplete applications or missing contact information for follow-up by the recruiting team.

**Strategic Talent Mapping**
*   Building a searchable talent database by extracting historical data from legacy resume archives.
*   Identifying "silver medalist" candidates from past roles who match current open positions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the solution template.
2. Select your workspace and import the Resume Screening Agent workflow.
3. Connect your required document storage or ATS integrations via the Composio dashboard.
4. Ensure nodes are correctly mapped and all API credentials are authenticated in the configuration panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives the resume file or link and the target job description.
*   **Agent**: Analyzes the document, extracts key data points, and performs the matching logic.
*   **Composio Toolset**: Executes file retrieval and pushes structured data to your ATS.
*   **Chat Output**: Returns the candidate score, summary, and recommendation to the recruiter.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
* `Analyze the attached resume for the Senior Software Engineer role and provide a summary of relevant experience.`
* `Extract contact info and top 5 skills from this resume and format them for our ATS.`
* `Score this candidate on a scale of 1-10 based on their experience with Python and cloud infrastructure.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for document interpretation.
*   Instruct the model to prioritize specific keywords found in the job description.
*   Define the output schema to ensure consistent JSON formatting for ATS integration.
*   Set a "strict" mode for data extraction to avoid hallucinations on missing fields.

### 2) Composio Toolset Node
The Composio Toolset manages the connection between the agent and your external tools. Ensure your API keys for your document storage (e.g., Google Drive, Dropbox) or ATS (e.g., Greenhouse, Lever) are active and scoped with read/write permissions.

### 3) Tool Availability
*   **Document Parsers**: Capabilities for reading PDF, DOCX, and TXT files.
*   **ATS Connectors**: Functions for updating candidate profiles and status fields.
*   **Data Validation Tools**: Logic for checking email, phone, and LinkedIn URL formats.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospective accounts and leads.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline the creation and configuration of new accounts in your CRM.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Optimize end-to-end business processes with intelligent task routing.
