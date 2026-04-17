# Lead Processing Automation Agent (Uplizd) - Streamline lead intake and CRM organization

## Summary
The Lead Processing Automation Agent by Uplizd transforms raw incoming lead data into structured, actionable CRM entries within Salesmate. By automating the qualification and data entry pipeline, this workflow eliminates manual administrative overhead, reduces lead response time, and ensures a single source of truth for your sales team’s pipeline velocity.

---

## Demo
![Lead Processing Automation Agent workflow diagram showing Chat Input, Agent, Composio Toolset, and Salesmate CRM integration](image.png)
**Alt text (SEO-ready):** Lead Processing Automation Agent for Salesmate CRM, featuring Uplizd AI workflow, automated lead qualification, and Composio toolset integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjZKAxYKSx+QyjOgMDw38UjFgwGoaGgWjADhjFwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMAAAJ4sB4042s5AAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/796cd3e6-f9b5-533f-aca7-989bcef5dc7f)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, salesmate, lead management, pipeline, data hygiene, composio, ai workflow, lead qualification
- This solution bridges the gap between raw lead ingestion and CRM data hygiene, ensuring every lead is processed with consistent logic.

---

## Who is this for?
This automation is designed for teams looking to scale their lead management without increasing manual data entry.

- **Sales Operations Manager**
    - Ensures data integrity across the pipeline by enforcing standardized lead entry protocols.
- **Account Executive**
    - Receives pre-qualified, enriched lead data directly in Salesmate, allowing for faster outreach.
- **BDR/SDR Lead**
    - Eliminates time spent on manual lead input, focusing instead on high-value prospect engagement.
- **Revenue Operations Lead**
    - Gains visibility into lead source performance and conversion metrics through automated tracking.

---

## Features
- **Automated Lead Parsing**
    - Extracts key contact and company information from unstructured inputs using intelligent AI extraction.
- **Salesmate CRM Integration**
    - Seamlessly pushes processed lead data into Salesmate using the Composio Toolset for real-time synchronization.
- **Intelligent Lead Qualification**
    - Evaluates lead quality based on predefined business rules before creating records in the CRM.
- **Data Hygiene Enforcement**
    - Standardizes formatting for phone numbers, email addresses, and company names to prevent duplicate entries.
- **Real-time Pipeline Updates**
    - Triggers immediate CRM updates, ensuring the sales team acts on new opportunities the moment they arrive.

---

## Use Cases
**Lead Intake Management**
- Automatically routing web-form submissions into Salesmate as new contacts.
- Cleaning and formatting lead contact fields to ensure consistent CRM data.

**Sales Pipeline Acceleration**
- Assigning new leads to the correct sales representative based on territory or industry.
- Updating existing lead records with fresh interaction data to maintain an accurate history.

**Operational Efficiency**
- Reducing manual data entry errors by automating the transfer of lead information.
- Triggering follow-up tasks in Salesmate immediately upon lead creation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your Salesmate account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data (email, name, company, source).
- **Agent**: Processes the input, performs qualification, and maps data to CRM fields.
- **Composio Toolset**: Executes the API calls to create or update records in Salesmate.
- **Chat Output**: Confirms successful lead ingestion and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Process this new lead: John Doe from Acme Corp, email john@acme.com, source: LinkedIn.`
- `Create a new lead in Salesmate for Sarah Jenkins, VP of Sales at TechFlow, phone 555-0199.`
- `Update the existing lead for Michael Scott at Dunder Mifflin with the new lead source: Referral.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent bridge between raw text and structured CRM data.
- Instruct the agent to prioritize data accuracy and field mapping.
- Use a system prompt that enforces strict JSON formatting for CRM inputs.
- Configure the agent to identify and flag incomplete lead information for manual review.

### 2) Composio Toolset Node
- Provide your Salesmate API key within the Composio configuration.
- Set the connection scope to allow read/write access to Leads and Contacts.

### 3) Tool Availability
- `salesmate_create_lead`: Creates a new lead record with parsed contact details.
- `salesmate_update_lead`: Updates existing records based on email or unique identifier.
- `salesmate_search_contact`: Checks for existing records to prevent duplicates.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) - Synchronize multi-platform CRM data with conflict resolution.
- [../crm-data-hygiene-manager/README.md](CRM Data Hygiene Manager) - Automate data decay cleanup and formatting for Salesmate.
- [../deal-pipeline-manager/README.md](Deal Pipeline Manager) - Manage pipeline stages and stalled deal follow-ups.
