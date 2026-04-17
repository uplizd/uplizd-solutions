# Global Proposal Manager (Uplizd) - Streamline multi-currency international sales proposals

## Summary
The Global Proposal Manager is an intelligent Uplizd workflow designed to automate the creation, calculation, and delivery of international sales proposals. By leveraging the Composio Toolset to integrate with Better Proposals, this solution ensures accurate currency conversion, localized pricing, and rapid document generation, enabling sales teams to scale their global outreach while maintaining consistent brand standards and pipeline velocity.

---

## Demo
![Global Proposal Manager workflow interface showing automated document generation and currency conversion steps](image.png)
**Alt text (SEO-ready):** Global Proposal Manager Uplizd workflow for automated multi-currency sales proposals and Better Proposals integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fb4e58b0-b0f5-55a4-99bb-ac7274aea184)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** `better-proposals`, `sales`, `international-business`, `currency-conversion`, `document-automation`, `composio`, `ai-workflow`
This solution bridges the gap between international client requirements and standardized sales operations through automated document management.

---

## Who is this for?
This solution is designed for revenue-focused teams managing complex international sales cycles.

*   **Sales Operations Manager**
    *   Standardizes proposal templates across different regions to ensure brand compliance and pricing accuracy.
*   **Account Executive**
    *   Reduces manual document preparation time, allowing for faster turnaround on international deal opportunities.
*   **Global Sales Director**
    *   Gains visibility into proposal performance and pipeline health across multiple currencies and territories.
*   **Finance Lead**
    *   Ensures that multi-currency proposals align with current exchange rates and corporate pricing policies.

---

## Features
- **Automated Multi-Currency Logic**
  Real-time currency conversion ensures that proposals are presented in the client's local currency without manual calculation errors.
- **Better Proposals Integration**
  Seamlessly pushes data from the Uplizd agent into Better Proposals to trigger document creation and delivery.
- **Dynamic Template Population**
  Automatically maps CRM data into predefined proposal templates, ensuring personalized content for every international lead.
- **Real-Time Status Tracking**
  Monitors proposal engagement and status updates, feeding information back into the workflow for proactive follow-ups.
- **Compliance-Aware Formatting**
  Applies regional formatting and legal clauses automatically based on the client's geographic location.

---

## Use Cases
**International Deal Closing**
*   Generating localized proposals for clients in different time zones and currency markets.
*   Automating the inclusion of region-specific terms and conditions in sales contracts.

**Sales Pipeline Velocity**
*   Reducing the time between initial client interest and proposal delivery by automating document drafting.
*   Triggering instant follow-up notifications when a proposal is viewed or signed by an international prospect.

**Data Hygiene & Accuracy**
*   Syncing finalized proposal values back to the CRM to maintain a single source of truth for global revenue.
*   Standardizing product descriptions and pricing tiers across all international sales documentation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `global-proposal-manager` JSON configuration file.
3. Connect your Better Proposals and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives client details, deal value, and target currency.
*   **Agent**: Processes the request, calculates conversions, and selects the appropriate proposal template.
*   **Composio Toolset**: Executes the API calls to Better Proposals to generate and send the document.
*   **Chat Output**: Confirms successful proposal generation and provides a link to the document.

### 3) Run the Flow
Access the Playground to test the workflow with these prompts:
*   `Create a proposal for Acme Corp in EUR using the standard enterprise template.`
*   `Generate a quote for a $50,000 deal for our Japanese client, converting to JPY.`
*   `Draft a proposal for the UK market including the Q3 discount terms.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for document logic and currency handling.
*   Prioritize accuracy in currency conversion and template selection.
*   Maintain a professional, localized tone based on the client's region.
*   Verify all input data against the CRM before triggering the proposal generation.

### 2) Composio Toolset Node
Requires a valid API key for Better Proposals and appropriate read/write permissions for your CRM to ensure data consistency.

### 3) Tool Availability
*   **Better Proposals API**: For document creation, template management, and status tracking.
*   **Currency Exchange API**: For real-time conversion rates.
*   **CRM Connector**: For fetching client contact details and updating deal stages.

---

## Related Solutions
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on international accounts.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up cadences globally.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensure multi-platform data consistency across international CRM instances.
