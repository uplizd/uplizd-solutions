# BTCPay Merchant Onboarding Agent (Uplizd) - Automate Bitcoin payment gateway setup for new merchants

## Summary
The BTCPay Merchant Onboarding Agent streamlines the complex process of setting up cryptocurrency payment infrastructure for new vendors. By leveraging the Composio Toolset to interface with BTCPay Server, this Uplizd AI workflow automates store creation, wallet configuration, and API key provisioning, ensuring merchants can accept Bitcoin payments with minimal manual intervention and maximum operational velocity.

---

## Demo
![BTCPay Merchant Onboarding Agent workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** BTCPay Merchant Onboarding Agent workflow in Uplizd, automating Bitcoin payment gateway configuration and merchant store setup via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/btc-pay-merchant-onboarding-agent-by-btcpay-server)

---

## Category
**Primary category:** Payment Operations
**Secondary tags:** btcpay server, bitcoin, merchant onboarding, crypto payments, automation, fintech, composio, ai workflow

This solution bridges the gap between manual merchant registration and automated payment gateway provisioning for crypto-native businesses.

---

## Who is this for?
This workflow is designed for teams managing high-volume merchant acquisition and payment infrastructure.

* **Payment Operations Manager**
    * Reduces the time spent on manual store configuration and wallet setup for new clients.
* **Fintech Developer**
    * Automates the provisioning of API keys and store settings through standardized AI-driven workflows.
* **Merchant Success Lead**
    * Ensures new merchants are ready to accept payments immediately, improving onboarding satisfaction.
* **Crypto Infrastructure Architect**
    * Maintains consistent security and configuration standards across all merchant payment gateways.

---

## Features
- **Automated Store Provisioning**
    Creates new store entities within BTCPay Server automatically based on merchant input data.
- **Wallet Configuration Sync**
    Configures derivation paths and wallet settings to ensure seamless Bitcoin payment processing.
- **API Key Management**
    Securely generates and provisions access credentials for new merchant accounts.
- **Real-time Validation**
    Validates merchant details and store settings before finalizing the onboarding process.
- **Composio Integration**
    Utilizes the Composio Toolset to execute complex BTCPay Server commands with natural language instructions.

---

## Use Cases
**Merchant Onboarding**
* Automating the setup of a new store profile for a vendor joining the platform.
* Configuring default payment settings and invoice templates for new merchant accounts.

**Payment Infrastructure Scaling**
* Provisioning multiple store instances simultaneously for large-scale merchant rollouts.
* Synchronizing wallet configurations across different merchant accounts to ensure uniform payment processing.

**Operational Efficiency**
* Reducing manual data entry errors by mapping merchant information directly to BTCPay Server fields.
* Streamlining the hand-off between sales teams and technical operations during the merchant activation phase.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Connect your BTCPay Server instance via the Composio Toolset.
3. Configure your LLM provider in the Agent node settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives merchant details and configuration requirements.
* **Agent**: Processes natural language requests and determines the necessary BTCPay actions.
* **Composio Toolset**: Executes authenticated calls to the BTCPay Server API.
* **Chat Output**: Confirms successful store creation and provides status updates to the user.

### 3) Run the Flow
Use the Playground to test the onboarding process with these prompts:
* `Create a new store named 'TechGear' for merchant 'support@techgear.com' with default Bitcoin settings.`
* `Configure the wallet for store ID 'ABC123XYZ' using the provided xpub key.`
* `Generate an API key for the new merchant 'GlobalRetail' and confirm the store is active.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent requires a model capable of structured tool calling to interact with the BTCPay API.
* Set the system prompt to prioritize accurate extraction of store parameters.
* Enable function calling to allow the agent to invoke Composio tools.
* Use a temperature setting of 0.2 to ensure consistent and reliable configuration outputs.

### 2) Composio Toolset Node
* Provide your BTCPay Server API credentials within the Composio dashboard.
* Ensure the connection scope includes `stores:create`, `wallets:setup`, and `api_keys:generate`.

### 3) Tool Availability
* `create_store`: Initializes a new merchant store entity.
* `setup_wallet`: Configures the Bitcoin wallet derivation path.
* `generate_api_key`: Creates secure access credentials for the merchant.
* `get_store_status`: Verifies the operational state of the newly created store.

---

## Related Solutions
* [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) - Automate CRM account creation and field population.
* [Affiliate Payment Automation Agent](../affiliate-payment-automation-agent-by-tapfiliate/README.md) - Streamline merchant and affiliate payout workflows.
* [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for business process management.
