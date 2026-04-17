# Real-Time Email Validator (Uplizd) - Instant email verification and bounce prevention

## Summary
The Real-Time Email Validator by Bouncer is an intelligent Uplizd workflow that verifies email addresses at the point of entry, ensuring high data hygiene and reducing bounce rates. By integrating directly into your lead capture or user registration pipelines, this solution acts as a gatekeeper, validating syntax, domain health, and mailbox existence to maintain a clean and reliable contact database.

---

## Demo
![Real-Time Email Validator workflow showing Chat Input, Agent, Bouncer integration, and Chat Output](image.png)
**Alt text (SEO-ready):** Real-Time Email Validator workflow by Uplizd, demonstrating automated email verification, Bouncer API integration, and CRM data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2d13cc6e-dd75-5e93-ad95-1ead6681e1dc)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** email validation, bouncer, data quality, lead management, crm, api integration, composio, bounce prevention
- This solution bridges the gap between raw user input and verified contact data, serving as a critical component for RevOps and marketing automation stacks.

---

## Who is this for?
This workflow is designed for teams prioritizing data integrity and efficient communication outreach.

- **Marketing Operations Manager**
    - Ensures that email marketing campaigns reach real, active inboxes to protect sender reputation.
- **Sales Development Representative (SDR)**
    - Validates lead contact information instantly to focus outreach efforts on high-quality, reachable prospects.
- **Data Engineer**
    - Automates the sanitization of incoming lead data before it reaches the CRM or marketing automation platform.
- **Customer Success Lead**
    - Maintains accurate user profiles to ensure critical account notifications and support updates are successfully delivered.

---

## Features
- **Instant Syntax Validation**
    - Checks email structure and format in real-time to catch typos before they enter your system.
- **Domain Health Analysis**
    - Verifies that the email domain is active and configured to receive messages, preventing delivery failures.
- **Mailbox Existence Verification**
    - Uses Bouncer's deep-check technology to confirm the specific mailbox exists without sending intrusive emails.
- **Composio-Powered Integration**
    - Seamlessly connects the Uplizd agent to the Bouncer API via the Composio Toolset for secure, authenticated requests.
- **Automated Data Routing**
    - Automatically flags or rejects invalid emails, keeping your CRM and marketing databases free of "dead" contacts.

---

## Use Cases
**Lead Capture Optimization**
- Validate email addresses immediately upon form submission on landing pages.
- Prevent low-quality leads from entering your CRM pipeline during the initial sign-up process.

**Marketing List Hygiene**
- Clean existing contact lists by running batch validations through the Bouncer integration.
- Reduce bounce rates for large-scale email campaigns by filtering out risky or invalid addresses.

**Sales Outreach Efficiency**
- Verify prospect contact details before adding them to automated sales sequences.
- Ensure that high-value account outreach is directed to verified, active professional email addresses.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Real-Time Email Validator.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Bouncer API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the email address string from your form or user input.
- **Agent**: Processes the request and determines the validation logic to apply.
- **Composio Toolset**: Executes the Bouncer API call to verify the email status.
- **Chat Output**: Returns the validation result (Valid, Invalid, or Risky) to the user or system.

### 3) Run the Flow
Use the Uplizd Playground to test the flow with these prompts:
- `Validate the email address: contact@example.com`
- `Check if the email support@startup.io is deliverable.`
- `Verify this lead's email: user123@gmail.com and return the status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between user input and the Bouncer API.
- Use a clear, concise system prompt to define the agent's role as a data validator.
- Instruct the agent to parse the email address accurately from the input.
- Configure the agent to output the validation status in a structured format (e.g., JSON or clear text).

### 2) Composio Toolset Node
- Provide your Bouncer API key within the Composio configuration panel.
- Ensure the connection scope includes `email_validation` permissions.

### 3) Tool Availability
- `bouncer_validate_email`: Performs the primary verification check.
- `bouncer_get_credits`: Monitors remaining validation credits in your Bouncer account.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with verified contact details.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain overall database health and remove duplicate records.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts and leads.
