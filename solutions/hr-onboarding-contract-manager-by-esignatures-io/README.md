# HR Onboarding Contract Manager (Uplizd) - Automated new hire document generation and signing

## Summary
The HR Onboarding Contract Manager automates the lifecycle of new hire documentation by integrating AI-driven workflows with eSignatures.io. This solution streamlines the transition from offer acceptance to contract execution, ensuring HR teams maintain a single source of truth, reduce manual data entry errors, and accelerate pipeline velocity for onboarding new talent.

---

## Demo
![HR Onboarding Contract Manager workflow showing Chat Input, Agent, Composio Toolset, and eSignatures.io integration](image.png)
**Alt text (SEO-ready):** Uplizd HR Onboarding Contract Manager workflow automating document generation and e-signature requests via eSignatures.io.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2d9f57cb-89d1-5261-8968-fddb352cce45)

---

## Category
- **Primary category:** HR Operations
- **Secondary tags:** hr, onboarding, contract management, esignatures.io, document automation, workflow, composio, ai agent
- This solution bridges the gap between candidate data and legal compliance by automating contract generation and signature tracking within your HR tech stack.

---

## Who is this for?
This solution is designed for HR professionals and operations teams looking to eliminate manual paperwork bottlenecks during the hiring process.

- **HR Operations Manager**
    - Automates repetitive document drafting to focus on strategic talent management.
- **Recruitment Coordinator**
    - Ensures new hire contracts are generated and sent for signature immediately upon offer approval.
- **Legal Compliance Officer**
    - Maintains consistent document standards and audit trails for all employment agreements.
- **People Operations Lead**
    - Reduces time-to-hire by removing manual administrative friction from the onboarding pipeline.

---

## Features
- **Automated Contract Drafting**
    - Dynamically generates employment contracts using candidate data, reducing manual template editing.
- **eSignature Integration**
    - Seamlessly triggers signature requests via eSignatures.io directly from the workflow.
- **Real-time Status Tracking**
    - Monitors document progress and updates the status automatically within your HR system.
- **Error-Free Data Mapping**
    - Uses the Composio Toolset to ensure candidate information is accurately mapped to contract fields.
- **Centralized Document Repository**
    - Keeps all generated contracts organized and accessible for quick retrieval and audit purposes.

---

## Use Cases
**Contract Lifecycle Management**
- Automatically generate a personalized offer letter and employment contract for a new hire.
- Trigger an immediate e-signature request to the candidate's email address upon document finalization.

**HR Process Optimization**
- Sync candidate details from your ATS directly into the contract generation workflow.
- Send automated follow-up reminders to candidates who have not yet signed their onboarding documents.

**Compliance and Reporting**
- Ensure all employment contracts adhere to standardized legal templates and formatting requirements.
- Maintain a digital audit trail of when documents were sent, viewed, and signed by the new hire.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the HR Onboarding Contract Manager template from the solution library.
3. Connect your eSignatures.io account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives candidate details (Name, Role, Salary, Start Date).
- **Agent**: Processes the request and instructs the toolset to draft the contract.
- **Composio Toolset**: Executes the API calls to eSignatures.io to generate and send the document.
- **Chat Output**: Confirms the contract has been successfully generated and sent for signature.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Generate a standard employment contract for John Doe, hired as a Software Engineer starting on October 1st.`
- `Create a contract for Jane Smith, Senior Product Manager, with a salary of $120,000 and send for signature.`
- `Draft an onboarding agreement for the new Marketing Intern, Alex Johnson, and notify the HR team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between HR data and the e-signature platform.
- Use a clear, professional instruction set for document generation.
- Ensure the agent is configured to extract specific variables like start date and compensation.
- Set the agent to verify all required fields are present before triggering the eSignatures.io tool.

### 2) Composio Toolset Node
- Provide your eSignatures.io API key within the Composio configuration.
- Set the connection scope to allow document creation and signature request management.

### 3) Tool Availability
- `esignatures_create_contract`: Generates the document from templates.
- `esignatures_send_signature_request`: Dispatches the document to the candidate.
- `esignatures_get_document_status`: Retrieves real-time updates on signature progress.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamlines general employee onboarding tasks and communications.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates the creation and configuration of new user accounts in CRM.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Helps manage and prioritize follow-up tasks generated from HR or project workflows.
