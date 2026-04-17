# Opportunity Replication Agent (Uplizd) - Automate deal cloning and product synchronization

## Summary
The Opportunity Replication Agent streamlines sales operations by automating the cloning of successful opportunities and their associated product line items. By leveraging the Composio Toolset to interface with Salesforce, this workflow ensures that high-performing deal structures are instantly replicated for new prospects, reducing manual data entry, minimizing configuration errors, and accelerating pipeline velocity for sales teams.

---

## Demo
![Opportunity Replication Agent workflow diagram showing Salesforce opportunity cloning](image.png)
**Alt text (SEO-ready):** Uplizd Opportunity Replication Agent workflow for Salesforce, automating deal cloning, product line item synchronization, and sales pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cfe76175-6b34-5f35-8454-a292e5bad646)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** salesforce, crm, opportunity management, pipeline, data sync, automation, sales ops, composio
- This solution bridges the gap between historical deal success and future pipeline growth by automating complex object replication in CRM environments.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to standardize their sales process and reduce administrative overhead.

- **Sales Operations Manager**
    - Standardizes deal structures across the team to ensure consistent pricing and product bundling.
- **Account Executive**
    - Eliminates manual effort when creating new opportunities based on successful historical templates.
- **Sales Enablement Lead**
    - Ensures that best-practice product configurations are applied to every new deal opportunity.
- **Revenue Operations Analyst**
    - Maintains high data hygiene by automating the creation of related records and preventing manual entry discrepancies.

---

## Features
- **Intelligent Opportunity Cloning**
    - Automatically duplicates existing Salesforce opportunities while preserving critical metadata and stage history.
- **Product Line Item Sync**
    - Maps and copies all associated product line items from the source deal to the new opportunity in real-time.
- **Composio-Powered CRM Integration**
    - Utilizes secure, authenticated connections to Salesforce to perform complex object creation and data mapping.
- **Customizable Logic Gates**
    - Allows for conditional filtering to ensure only qualified or "won" deals are used as templates for replication.
- **Error-Resilient Execution**
    - Built-in validation ensures that all required fields and dependencies are met before the new opportunity is finalized.

---

## Use Cases
**Standardizing Sales Playbooks**
- Automatically clone a "Gold Standard" opportunity template when a new prospect enters the negotiation phase.
- Ensure all new deals include the correct product bundles and service tiers based on historical success.

**Accelerating Deal Velocity**
- Reduce the time spent on manual opportunity creation by triggering a clone workflow directly from a chat prompt.
- Instantly populate new opportunities with pre-configured product line items to speed up the quoting process.

**Data Hygiene and Consistency**
- Prevent manual data entry errors by programmatically copying opportunity fields and product associations.
- Maintain a clean CRM environment by ensuring all replicated deals follow the same naming and structure conventions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the builder.
2. Connect your Salesforce account via the Composio integration settings.
3. Configure your target environment and default opportunity owner settings.
4. Ensure nodes are correctly linked from the Chat Input through the Agent and Composio Toolset to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the source opportunity ID and the new deal name.
- **Agent**: Processes the request and orchestrates the cloning logic.
- **Composio Toolset**: Executes the Salesforce API calls to fetch and replicate records.
- **Chat Output**: Confirms the successful creation of the new opportunity with a link to the record.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Clone opportunity 0068c00000abc123 as 'New Enterprise Deal Q4'`
- `Replicate the product structure from the last closed-won deal for this new lead`
- `Create a new opportunity based on the 'Standard SaaS Package' template for Acme Corp`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for CRM interactions.
- Use a model capable of structured JSON output for reliable API parameter mapping.
- **Recommended instruction pattern:**
    - "You are a Salesforce automation assistant; extract the source opportunity ID and target name from the user input."
    - "Verify the existence of the source opportunity before initiating the cloning process."
    - "Always confirm the new opportunity ID and provide a direct link to the record upon completion."

### 2) Composio Toolset Node
- Provide your Salesforce API credentials within the Composio dashboard.
- Ensure the connection scope includes `Read` and `Write` permissions for `Opportunities` and `OpportunityLineItems`.

### 3) Tool Availability
- `salesforce_get_opportunity`: Fetches details and line items from the source deal.
- `salesforce_create_opportunity`: Initializes the new record with cloned data.
- `salesforce_add_opportunity_line_items`: Maps products from the source to the new destination.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistency across multiple CRM platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages and follow-ups.
