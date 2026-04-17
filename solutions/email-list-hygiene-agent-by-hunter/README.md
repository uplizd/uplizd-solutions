# Email List Hygiene Agent (Uplizd) - Automated email verification and list cleaning for high deliverability

## Summary
The Email List Hygiene Agent is an intelligent Uplizd workflow designed to maintain pristine email marketing databases by automating the verification of contact lists. By leveraging the Hunter.io integration, this agent identifies invalid, disposable, or risky email addresses in real-time, significantly reducing bounce rates and protecting your sender reputation. It serves as a single source of truth for list health, ensuring your outreach reaches actual human recipients and maximizing your pipeline velocity.

---

## Demo
![Email List Hygiene Agent workflow interface showing Hunter.io verification nodes and list processing logic](image.png)
**Alt text (SEO-ready):** Email List Hygiene Agent by Uplizd, automated email verification workflow, Hunter.io integration, CRM data hygiene, and email deliverability optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b705539c-68de-58f1-b016-e1b7cbe551fb)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** email marketing, data hygiene, hunter.io, lead verification, crm, deliverability, composio, ai workflow  
This solution streamlines data hygiene by automating the validation of contact lists, ensuring high-quality data for all downstream sales and marketing activities.

---

## Who is this for?
This agent is designed for teams managing high-volume outreach who need to maintain sender reputation and data accuracy.

- **Marketing Manager**
    - Ensures campaign budgets are spent on valid leads rather than bounces.
- **Sales Operations Specialist**
    - Maintains clean CRM records by purging dead or risky email addresses.
- **Growth Marketer**
    - Improves open and click-through rates by targeting verified, active prospects.
- **Deliverability Lead**
    - Protects domain reputation by preventing blacklisting caused by high bounce rates.

---

## Features
- **Real-time Verification**
    - Instantly validates email addresses against global databases to confirm deliverability status.
- **Risk Scoring**
    - Assigns a risk level to each email, allowing you to filter out disposable or catch-all addresses.
- **Automated List Processing**
    - Handles bulk list uploads and processes them through the Hunter.io toolset without manual intervention.
- **Seamless CRM Integration**
    - Syncs verified status updates directly back to your CRM, ensuring your sales team works with clean data.
- **Customizable Thresholds**
    - Allows users to define specific rules for what constitutes a "clean" lead based on business requirements.

---

## Use Cases
**List Scrubbing**
- Automatically cleaning imported CSV lists before launching a new cold outreach campaign.
- Identifying and removing inactive or "dead" email addresses from legacy databases.

**Lead Qualification**
- Verifying prospect emails captured via web forms before they enter the sales pipeline.
- Flagging high-risk "catch-all" emails for manual review by the sales development team.

**Reputation Management**
- Monitoring domain health by preventing high bounce rates during large-scale email blasts.
- Ensuring compliance with email service provider (ESP) standards by maintaining low bounce thresholds.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your preferred workspace and project destination.
3. Authenticate your Hunter.io account within the Composio Toolset.
4. Ensure nodes are connected from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the list of email addresses or CRM contact IDs to be verified.
- **Agent**: Analyzes the input and orchestrates the verification logic using the provided instructions.
- **Composio Toolset**: Executes the Hunter.io API calls to validate the email status.
- **Chat Output**: Returns a clean, verified list or a report of identified invalid addresses.

### 3) Run the Flow
Use the Playground to test your list processing:
- `Verify the following email list: [email1@example.com, email2@test.com]`
- `Check the deliverability status for all leads in my current CRM list.`
- `Filter out all invalid and disposable emails from the provided contact batch.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data hygiene controller that interprets verification results and formats them for your team.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize "deliverable" status over "risky" or "undeliverable."
- Configure the agent to output a summary report of the cleanup process.

### 2) Composio Toolset Node
- **API Key**: Ensure your Hunter.io API key is active and has sufficient credits for your list size.
- **Connection Scope**: Grant the toolset access to email verification and domain search endpoints.

### 3) Tool Availability
- `hunter_email_verifier`: Validates individual or bulk email addresses.
- `hunter_domain_search`: Identifies patterns for email construction.
- `crm_update_tool`: Updates contact fields in your CRM with the verification status.

---

## Related Solutions
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact details.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Comprehensive CRM data maintenance and cleanup.
- [../account-research-assistant-by-zoominfo/README.md](../account-research-assistant-by-zoominfo/README.md) - Deep account research and lead intelligence.
