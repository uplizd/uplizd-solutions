# HR Onboarding Document Agent (Uplizd) - Automated paperwork and signature workflows

## Summary
The HR Onboarding Document Agent streamlines the new hire experience by automating document generation, distribution, and signature collection. By integrating HR systems with e-signature platforms, this Uplizd workflow eliminates manual data entry, reduces administrative bottlenecks, and ensures all onboarding paperwork is completed with full compliance and audit trails.

---

## Demo
![HR Onboarding Document Agent workflow showing automated document generation and SignWell integration](image.png)
**Alt text (SEO-ready):** HR Onboarding Document Agent workflow for automated paperwork, SignWell signature collection, and Uplizd AI-driven onboarding.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/993e4b9a-301b-57f5-9e4b-10ed05a3d08e)

---

## Category
**Primary category:** Operations  
**Secondary tags:** hr, onboarding, document automation, signwell, e-signature, workflow automation, employee lifecycle, composio  
This solution bridges the gap between HR management systems and document execution to create a seamless, touchless onboarding pipeline.

---

## Who is this for?
This solution is designed for HR and Operations teams looking to scale their hiring processes without increasing administrative overhead.

*   **HR Manager**
    *   Reduces time-to-hire by automating the delivery of offer letters and employment contracts.
*   **Operations Coordinator**
    *   Ensures consistent document formatting and compliance across all new hire documentation.
*   **Recruitment Lead**
    *   Provides a professional, frictionless experience for candidates during the final offer stage.
*   **Compliance Officer**
    *   Maintains a secure, digital audit trail of all signed documents and onboarding acknowledgments.

---

## Features
- **Automated Document Generation**
  Instantly populate employment contracts and onboarding forms with candidate data using the Composio Toolset.
- **Seamless Signature Integration**
  Trigger signature requests directly via SignWell, keeping the entire process within the Uplizd workflow.
- **Real-time Status Tracking**
  Monitor document progress and receive automated alerts when candidates view or sign their paperwork.
- **Centralized Data Sync**
  Automatically update HR systems or databases once a document is signed, ensuring a single source of truth.
- **Error-Free Data Mapping**
  Eliminate manual entry errors by mapping candidate profile fields directly into standardized document templates.

---

## Use Cases
**New Hire Paperwork Automation**
*   Automatically generate and send offer letters, NDAs, and benefits enrollment forms upon candidate selection.
*   Trigger follow-up reminders to candidates who have not yet completed their signature tasks.

**Compliance and Audit Readiness**
*   Store signed documents in designated cloud folders with standardized naming conventions for easy retrieval.
*   Maintain a comprehensive log of document delivery and signature timestamps for internal audits.

**Cross-Departmental Onboarding**
*   Notify IT and Facilities teams automatically once the final employment contract is signed by the new hire.
*   Sync onboarding completion status to project management tools to trigger equipment provisioning workflows.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your SignWell and HR system connections within the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are saved in the environment settings.

### 2) Setup the Nodes
*   **Chat Input**: Receives candidate details and document type requests.
*   **Agent**: Processes the request, selects the correct template, and prepares the data.
*   **Composio Toolset**: Executes the document generation and signature request via SignWell.
*   **Chat Output**: Confirms the document has been sent and provides a tracking link.

### 3) Run the Flow
Use the Playground to test the agent with prompts like:
* `Generate an offer letter for John Doe for the Software Engineer role with a start date of October 1st.`
* `Send the standard NDA and employment contract to the new hire at candidate@example.com.`
* `Check the status of the onboarding documents for the latest batch of new hires.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for document logic and tool selection.
*   Use a model with high instruction-following capability (e.g., GPT-4o).
*   Provide clear context regarding document templates and required fields.
*   Ensure the system prompt emphasizes data privacy and accuracy.

### 2) Composio Toolset Node
*   **API Key**: Provide your SignWell API key to enable document signing capabilities.
*   **Connection Scope**: Ensure the toolset has read/write access to your document storage and e-signature platform.

### 3) Tool Availability
*   **Document Generation**: Capability to fill templates with dynamic variables.
*   **E-Signature Dispatch**: Capability to initiate and track signature workflows.
*   **Notification Service**: Capability to send status updates to Slack or Email.

---

## Related Solutions
* [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) — Manage employee onboarding tasks and team communication.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate account creation and configuration for new users.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline cross-platform business process automation.
