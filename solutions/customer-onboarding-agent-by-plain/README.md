# Customer Onboarding Agent (Uplizd) - Streamline new client setup and support workflows

## Summary
The Customer Onboarding Agent automates the end-to-end process of initializing new client accounts and generating support threads within Plain. By orchestrating data synchronization and task creation, this workflow eliminates manual entry, reduces time-to-value for new users, and ensures a consistent, high-quality onboarding experience for every customer.

---

## Demo
![Customer Onboarding Agent workflow diagram showing Chat Input, Agent, Plain Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Customer Onboarding Agent workflow in Uplizd, automating client setup and support ticket creation using the Plain integration and Composio toolset.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b6a2de5a-c88c-5b23-bde9-73bad008a659)

---

## Category
**Primary category:** Customer Support
**Secondary tags:** onboarding, plain, crm, support automation, client success, workflow, composio, ai agent

This solution bridges the gap between initial customer sign-up and active support engagement by automating account provisioning and communication tracking.

---

## Who is this for?
This solution is designed for teams looking to scale their client operations without increasing manual administrative overhead.

*   **Customer Success Managers**
    *   Automate the creation of welcome threads and initial account documentation to ensure no client is left waiting.
*   **Support Operations Leads**
    *   Standardize the onboarding process across all new sign-ups to maintain high service level agreements (SLAs).
*   **Onboarding Specialists**
    *   Offload repetitive data entry and ticket creation tasks to the AI, allowing focus on high-touch client interactions.
*   **Revenue Operations Managers**
    *   Ensure that customer data captured during sign-up is accurately reflected in support systems for better account intelligence.

---

## Features
- **Automated Account Provisioning**
  Instantly create and configure new customer profiles in Plain based on incoming sign-up data.
- **Dynamic Support Thread Generation**
  Automatically initialize welcome support threads, ensuring the first point of contact is personalized and immediate.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely bridge the gap between your data sources and the Plain support platform.
- **Real-Time Data Sync**
  Maintain data hygiene by ensuring that customer attributes are consistently updated across platforms in real-time.
- **Intelligent Context Injection**
  The Agent node analyzes incoming user intent to tailor the onboarding message and initial support priority.

---

## Use Cases
**New Client Activation**
*   Automatically trigger a welcome thread in Plain the moment a new user registers in your CRM.
*   Populate account metadata fields to ensure support agents have full context before the first interaction.

**Support Workflow Optimization**
*   Route onboarding-related queries to specific support queues based on the customer's subscription tier.
*   Automate the creation of follow-up tasks for the success team if the onboarding thread remains inactive for 48 hours.

**Data Consistency & Hygiene**
*   Standardize naming conventions for new customer accounts to prevent duplicate entries in the support dashboard.
*   Sync custom attributes from your sign-up form directly into Plain’s customer profile fields.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Plain account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the new customer registration payload.
*   **Agent**: Processes the data and determines the necessary onboarding actions.
*   **Composio Toolset**: Executes the API calls to create or update records in Plain.
*   **Chat Output**: Confirms the successful creation of the account and support thread.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Create a new support thread for customer ID 98765 and tag it as 'onboarding'.`
* `Initialize a welcome thread for a new enterprise client and assign it to the 'Priority' queue.`
* `Sync the latest account details from the registration form to the Plain customer profile for user 'jdoe@example.com'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for your onboarding process.
*   **Recommended instruction pattern:**
    *   "You are an expert onboarding assistant; extract customer details from the input and map them to the Plain API schema."
    *   "Prioritize accuracy in account mapping and ensure all mandatory fields are populated."
    *   "If the customer is an enterprise tier, flag the support thread for immediate human review."

### 2) Composio Toolset Node
*   **API Key:** Provide your Plain API key via the Composio dashboard.
*   **Connection Scope:** Ensure the agent has 'Read/Write' access to customer and thread resources.

### 3) Tool Availability
*   `plain_create_thread`: Initializes new communication channels.
*   `plain_update_customer`: Updates profile metadata and attributes.
*   `plain_get_customer`: Retrieves existing account context to prevent duplicates.

---

## Related Solutions
* [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - General-purpose support automation.
* [crm-data-sync-agent](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms.
* [account-setup-agent-by-salesforce](../account-setup-agent-by-salesforce/README.md) - Automate account creation within Salesforce.
