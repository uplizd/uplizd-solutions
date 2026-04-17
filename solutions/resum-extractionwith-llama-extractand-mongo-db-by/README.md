# Resume Extraction Agent (Uplizd) - Automated resume parsing and database synchronization

## Summary
The Resume Extraction Agent leverages the LlamaExtract framework and MongoDB to transform unstructured resume documents into structured, queryable data. This Uplizd AI workflow automates the ingestion, parsing, and storage process, enabling HR teams and recruiters to maintain a clean, searchable talent database without manual data entry.

---

## Demo
![Resume Extraction Agent workflow showing document ingestion, LlamaExtract parsing, and MongoDB storage](image.png)
**Alt text (SEO-ready):** Resume Extraction Agent workflow using LlamaExtract and MongoDB for automated candidate data synchronization and talent pipeline management on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8dcef98b-8d50-59de-8bd7-51b8a1dafec0)

---

## Category
**Primary category:** Data integration
**Secondary tags:** resume parsing, mongodb, llamaextract, hr tech, talent acquisition, data pipeline, automation, recruitment

This solution bridges the gap between unstructured document storage and structured database management for high-volume recruitment operations.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual data entry in their hiring workflows.

* **Recruitment Operations Manager**
    * Ensures candidate data is consistently structured and ready for reporting.
* **HR Data Analyst**
    * Gains immediate access to parsed candidate skills and experience for talent mapping.
* **Technical Recruiter**
    * Reduces time-to-screen by automating the extraction of key qualifications from incoming resumes.
* **Talent Acquisition Lead**
    * Maintains a centralized, searchable database of applicants to improve pipeline velocity.

---

## Features
- **Intelligent Parsing**
    Leverages LlamaExtract to accurately identify and extract entities like name, education, and work history from varied resume formats.
- **MongoDB Integration**
    Seamlessly maps extracted JSON fields directly into your MongoDB collections for persistent storage and retrieval.
- **Automated Data Hygiene**
    Standardizes inconsistent resume formats into a uniform schema, reducing noise in your talent database.
- **Real-time Processing**
    Triggers extraction immediately upon file upload, ensuring your database reflects the latest candidate submissions.
- **Composio-Powered Workflow**
    Utilizes the Composio Toolset to orchestrate the connection between document storage services and your database.

---

## Use Cases
**Candidate Database Management**
* Automating the ingestion of resumes from email attachments or cloud storage into MongoDB.
* Updating existing candidate profiles with new certifications or work experience extracted from updated resumes.

**Talent Pipeline Optimization**
* Filtering candidates based on specific extracted skills or years of experience stored in MongoDB.
* Generating automated reports on candidate source quality by tracking data extracted from different channels.

**Compliance and Data Retention**
* Standardizing resume data to ensure all candidate information meets internal data privacy and retention policies.
* Cleaning up legacy resume databases by re-parsing old documents into a modern, structured format.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link to open the solution template.
2. Select your workspace and import the pre-configured workflow.
3. Authenticate your MongoDB and LlamaExtract connections within the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the file path or raw text of the resume to be processed.
* **Agent**: Analyzes the input and instructs the extraction tool to parse specific fields.
* **Composio Toolset**: Executes the LlamaExtract parsing and MongoDB write operations.
* **Chat Output**: Confirms successful extraction and provides a summary of the data saved.

### 3) Run the Flow
Use the Playground to test your extraction:
* `Extract the contact information and skills from the attached resume and save to the 'candidates' collection.`
* `Parse the provided PDF resume and update the MongoDB record for John Doe.`
* `Process the latest batch of resumes in the folder and log the extraction status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for document parsing logic.
* Use a model capable of high-fidelity JSON output (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Extract candidate details into a structured JSON format matching the MongoDB schema."
* Instruction: "Validate that all required fields like email and phone number are captured before writing to the database."

### 2) Composio Toolset Node
* Provide your API key to enable the LlamaExtract and MongoDB connectors.
* Ensure the connection scope includes read/write access to your target MongoDB database.

### 3) Tool Availability
* **LlamaExtract Parser**: Capability to convert unstructured text/PDFs into structured JSON.
* **MongoDB Connector**: Capability to perform `insert` or `update` operations on specified collections.
* **File System Access**: Capability to read source documents from integrated cloud storage.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriches candidate and account data for better outreach.
* [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automates the setup and data entry for new system users.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General-purpose automation for managing complex business processes.
