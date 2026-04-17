# Sales Contract Automator (Uplizd) - Streamline document generation and contract delivery

## Summary
The Sales Contract Automator is an intelligent Uplizd workflow designed to eliminate manual bottlenecks in the closing process by automatically generating, populating, and dispatching contracts via eSignatures.io once a deal reaches a specific stage. By synchronizing CRM data with legal templates, this solution ensures pipeline velocity, reduces human error in document drafting, and provides a single source of truth for contract status, allowing sales teams to focus on revenue generation rather than administrative overhead.

---

## Demo
![Sales Contract Automator workflow showing CRM trigger, eSignatures.io integration, and automated document dispatch](image.png)
**Alt text (SEO-ready):** Sales Contract Automator workflow on Uplizd, featuring CRM integration with eSignatures.io for automated contract generation and document processing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/24db7b1e-6452-5ddd-8105-34ec3efcebef)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, esignatures.io, contract management, document automation, sales operations, pipeline velocity, composio, ai workflow
This solution bridges the gap between CRM opportunity management and legal execution, ensuring seamless document workflows for high-growth sales teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to accelerate the transition from verbal agreement to signed contract.

*   **Sales Operations Manager**
    *   Standardizes contract templates and ensures compliance across all outgoing sales documents.
*   **Account Executive**
    *   Reduces time spent on manual data entry and document drafting, allowing for faster deal closures.
*   **Legal Counsel**
    *   Maintains oversight of contract terms by ensuring only approved templates are used in the automated flow.
*   **Revenue Operations Lead**
    *   Gains visibility into the contract lifecycle and identifies bottlenecks in the final stages of the sales pipeline.

---

## Features
- **Automated Document Generation**
  Instantly populates legal templates with CRM data, ensuring accuracy and consistency in every contract.
- **Trigger-Based Dispatch**
  Automatically sends contracts for signature the moment a deal moves to a "Closed-Won" or "Contract Sent" stage.
- **eSignatures.io Integration**
  Leverages the Composio Toolset to securely interface with eSignatures.io for real-time document delivery and tracking.
- **Real-Time Status Sync**
  Updates the CRM with contract status changes, providing an immediate view of deal progress without manual updates.
- **Error-Free Data Mapping**
  Eliminates manual copy-paste errors by mapping CRM fields directly to contract placeholders via AI-driven logic.

---

## Use Cases
**Contract Lifecycle Management**
- Automatically generate a standard Service Agreement when an opportunity is marked as "Proposal Sent."
- Update the CRM deal record automatically once the client views or signs the document via eSignatures.io.

**Sales Pipeline Acceleration**
- Reduce the "Time to Close" by triggering contract delivery immediately upon verbal agreement.
- Standardize the outreach process by ensuring every client receives the correct contract version based on the product tier.

**Operational Compliance**
- Ensure all contracts are generated using the most recent, legally approved template stored in your document repository.
- Maintain a clear audit trail by logging all contract generation and dispatch events directly within the CRM activity feed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your CRM account and eSignatures.io API credentials within the integration settings.
3. Map your CRM deal fields to the corresponding placeholders in your contract template.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal from your CRM when a deal stage changes.
*   **Agent**: Interprets the deal data and selects the appropriate contract template.
*   **Composio Toolset**: Executes the API calls to eSignatures.io to generate and send the document.
*   **Chat Output**: Confirms the successful dispatch of the contract and logs the event back to the CRM.

### 3) Run the Flow
Use the Playground to test the automation with sample deal data:
- `Generate a contract for Deal ID 98765 using the Standard MSA template.`
- `Send the Enterprise Service Agreement to the primary contact for Opportunity 4432.`
- `Check the status of the contract associated with Deal 12345 and update the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that parses deal data and maps it to the contract template.
- Use a high-reasoning model to ensure accurate field mapping.
- Instruct the agent to validate that all required contact information is present before triggering the dispatch.
- Configure the agent to handle edge cases, such as missing fields, by notifying the user via the Chat Output.

### 2) Composio Toolset Node
- Provide your eSignatures.io API key within the Composio configuration.
- Ensure the connection scope includes permissions for document creation and status tracking.

### 3) Tool Availability
- **CRM Connector**: For fetching opportunity details and updating deal stages.
- **eSignatures.io API**: For template selection, document population, and signature request dispatch.
- **Notification Service**: For alerting the sales team upon successful contract delivery.

---

## Related Solutions
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Automates the creation of new accounts and onboarding workflows in Salesforce.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manages pipeline stages and automates follow-ups for stalled deals.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Gathers account insights to inform sales strategy and contract customization.
