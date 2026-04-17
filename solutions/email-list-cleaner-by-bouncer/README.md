# Email List Cleaner (Uplizd) - Automated email verification and list hygiene

## Summary
The Email List Cleaner by Bouncer is an intelligent Uplizd workflow designed to automate the verification of email addresses, ensuring high deliverability and protecting your sender reputation. By integrating directly with Bouncer’s verification engine, this solution identifies invalid, risky, or undeliverable addresses in real-time, allowing marketing and sales teams to maintain pristine contact databases and improve campaign performance.

---

## Demo
![Email List Cleaner workflow diagram showing Chat Input, Agent, Bouncer Toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Email List Cleaner workflow in Uplizd, showing automated email verification, Bouncer API integration, and contact list hygiene for improved deliverability.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/200be1dd-90aa-51c7-a8ae-4f0b23af7dac)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, data hygiene, bouncer, lead qualification, deliverability, crm, automation, composio
- This solution bridges the gap between raw contact collection and high-performance email outreach by automating the validation process.

---

## Who is this for?
This solution is designed for professionals who need to maintain high-quality contact lists and ensure their outreach efforts reach the inbox.

- **Email Marketers**
    - Reduce bounce rates and protect sender reputation by filtering out invalid addresses before launching campaigns.
- **Sales Operations Managers**
    - Maintain CRM data hygiene by ensuring that lead lists are verified and ready for high-touch outreach.
- **Growth Hackers**
    - Optimize lead nurturing funnels by focusing efforts only on verified, high-intent prospects.
- **Customer Success Leads**
    - Ensure critical communication reaches the intended recipient by verifying contact data during the onboarding process.

---

## Features
- **Real-Time Verification**
    - Instantly validate email addresses using the Bouncer API to catch typos and non-existent domains.
- **Risk Assessment**
    - Categorize emails as deliverable, undeliverable, or risky to allow for nuanced list management.
- **Composio-Powered Integration**
    - Seamlessly connect the Uplizd agent to Bouncer’s toolset for secure and efficient API communication.
- **Automated Hygiene**
    - Automatically flag or remove invalid entries from your database to keep your CRM clean and efficient.
- **Actionable Insights**
    - Receive clear, summarized reports on your list quality directly through the chat interface.

---

## Use Cases
**Campaign Preparation**
- Validate a new list of leads exported from a CRM before importing them into your email marketing platform.
- Identify and remove "catch-all" or risky email addresses to prevent account suspension.

**CRM Data Maintenance**
- Run a scheduled check on your existing database to identify and purge decayed or inactive email contacts.
- Automatically update contact status fields in your CRM based on the verification results provided by the agent.

**Lead Qualification**
- Verify email addresses at the point of entry during a web form submission or lead capture event.
- Prioritize outreach to verified high-value prospects while flagging unverified entries for manual review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Configure your environment variables, including your Bouncer API key.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the list of email addresses or the file path to be processed.
- **Agent**: Processes the input, interprets verification requirements, and triggers the Bouncer toolset.
- **Composio Toolset**: Executes the specific API calls to Bouncer to verify email validity.
- **Chat Output**: Returns the cleaned list or a summary report of the verification results.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Verify the following email list: [email1@example.com, email2@test.com]`
- `Check the deliverability status of this list and provide a summary of risky addresses.`
- `Clean my contact list and categorize the results into a CSV format.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between the user request and the Bouncer API.
- Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5).
- Ensure the system prompt instructs the agent to prioritize accuracy and data privacy.
- Configure the agent to format output clearly, highlighting invalid addresses for quick action.

### 2) Composio Toolset Node
- Provide your Bouncer API key within the Composio configuration settings.
- Ensure the connection scope allows for read/write access to email verification endpoints.

### 3) Tool Availability
- `bouncer_verify_email`: Single email address validation.
- `bouncer_bulk_verify`: Batch processing for large contact lists.
- `bouncer_get_credits`: Monitoring remaining verification balance.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich your contact data with professional insights.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain overall CRM health and data consistency.
- [WhatsApp Lead Qualifier](../whats-app-lead-qualifier-by-wati/README.md) - Qualify leads directly through messaging channels.
