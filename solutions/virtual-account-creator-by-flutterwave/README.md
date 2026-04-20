# Virtual Account Creator (Uplizd) - Automated financial provisioning for seamless customer onboarding

## Summary
The Virtual Account Creator (Uplizd) is an automated AI workflow designed to streamline the provisioning of virtual bank accounts for new customers and partners. By integrating directly with Flutterwave via the Composio Toolset, this solution eliminates manual data entry, reduces human error in financial record-keeping, and accelerates the time-to-revenue for businesses managing high-volume account creation.

---

## Demo
![Virtual Account Creator workflow showing Chat Input, Agent, Flutterwave Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Virtual Account Creator workflow in Uplizd, demonstrating automated Flutterwave account provisioning, AI-driven financial operations, and Composio tool integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c6ddc601-4e6a-5d69-ba37-66ef7a1f7b32)

---

## Category
**Primary category:** Financial Operations  
**Secondary tags:** flutterwave, fintech, virtual accounts, account provisioning, automation, api integration, composio, ai workflow  
This solution enables automated financial infrastructure management, bridging the gap between customer onboarding and banking service activation.

---

## Who is this for?
This solution is designed for operations teams and financial administrators who need to scale account provisioning without increasing manual overhead.

* **Fintech Operations Manager**
    * Automates the creation of virtual accounts at scale to support rapid user growth.
* **Customer Success Lead**
    * Reduces onboarding friction by providing new clients with immediate banking details.
* **Platform Engineer**
    * Integrates financial service APIs into internal workflows without writing custom middleware.
* **Business Development Manager**
    * Accelerates partner onboarding by automating the setup of dedicated financial sub-accounts.

---

## Features
- **Automated Provisioning**
  Instantly trigger virtual account creation via Flutterwave API calls as soon as a customer record is validated.
- **Real-time Synchronization**
  Ensures that account details generated in Flutterwave are immediately reflected in your internal CRM or database.
- **Error Handling & Validation**
  Built-in logic to verify customer data before submission, preventing failed account creation attempts.
- **Composio Toolset Integration**
  Leverages secure, authenticated connections to Flutterwave, ensuring all financial operations remain compliant and encrypted.
- **Scalable Workflow Architecture**
  Designed to handle high-frequency requests, allowing your team to provision hundreds of accounts without manual intervention.

---

## Use Cases
**Customer Onboarding**
* Automatically generate a unique virtual account for every new user during the sign-up flow.
* Send account details directly to the customer via email or in-app notification upon successful creation.

**Partner & Vendor Management**
* Provision dedicated virtual accounts for new vendors to facilitate seamless payouts and reconciliation.
* Update partner profiles with new account identifiers automatically to ensure timely payment processing.

**Financial Reconciliation**
* Map virtual account IDs to internal customer records to simplify end-of-month financial reporting.
* Audit account creation logs to ensure all provisioned accounts match approved customer profiles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Virtual Account Creator template from the marketplace.
3. Connect your Flutterwave API credentials within the Composio Toolset settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives customer details (name, email, currency) from your onboarding form.
* **Agent**: Processes the request and determines the necessary parameters for the Flutterwave API.
* **Composio Toolset**: Executes the secure API call to Flutterwave to provision the virtual account.
* **Chat Output**: Returns the generated account number and bank details to the user or system.

### 3) Run the Flow
Test the workflow in the Playground using these example prompts:
* `Create a new virtual account for customer John Doe with email john@example.com in USD.`
* `Provision a new sub-account for partner ID 98765 and return the bank details.`
* `Generate a virtual account for the new user registered under company 'TechCorp' using NGN currency.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your financial data requests.
* Use a model capable of structured JSON output for reliable API parameter mapping.
* Instruction: "Extract customer name, email, and currency from the input and call the Flutterwave tool to create a virtual account."
* Instruction: "Always confirm the success of the API call before notifying the user."

### 2) Composio Toolset Node
* Provide your Flutterwave API Key and Secret in the Composio configuration.
* Set the connection scope to include `virtual_account_write` permissions to allow the agent to provision accounts.

### 3) Tool Availability
* `flutterwave_create_virtual_account`: Primary tool for account generation.
* `flutterwave_get_account_details`: Used for verifying existing account status.
* `crm_update_record`: Optional tool to sync the new account number back to your database.

---

## Related Solutions
* [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial matching and ledger updates.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline CRM account creation and field population.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for complex business processes.
