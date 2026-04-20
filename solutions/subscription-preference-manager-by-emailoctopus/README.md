# Subscription Preference Manager (Uplizd) - Intelligent email list hygiene and subscriber retention

## Summary
The Subscription Preference Manager is an automated Uplizd AI workflow designed to streamline email list hygiene and reduce churn by dynamically managing subscriber preferences. By integrating directly with EmailOctopus, this solution empowers marketing teams to automate opt-out processes, categorize subscriber interests, and maintain a healthy, compliant mailing list without manual intervention.

---

## Demo
![Subscription Preference Manager workflow showing EmailOctopus integration and automated preference updates](image.png)
**Alt text (SEO-ready):** Subscription Preference Manager (Uplizd) workflow for automated email list hygiene, subscriber preference updates, and EmailOctopus integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/09fd8731-2d8f-5e36-9ad7-d5ae9e9606f1)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, emailoctopus, subscriber management, churn reduction, data hygiene, automation, composio, ai workflow
- This solution bridges the gap between subscriber feedback and CRM data, ensuring your email marketing strategy remains personalized and compliant.

---

## Who is this for?
This solution is designed for marketing and operations teams looking to optimize their email communication strategy.

- **Email Marketing Manager**
    - Automate the management of subscriber preferences to reduce list churn and improve engagement metrics.
- **CRM Administrator**
    - Maintain high data hygiene standards by syncing subscriber status changes across platforms in real-time.
- **Customer Success Lead**
    - Ensure that customers receive only the content they have opted into, fostering trust and brand loyalty.
- **Growth Marketer**
    - Leverage granular preference data to segment audiences more effectively for targeted campaigns.

---

## Features
- **Automated Preference Sync**
    - Real-time synchronization of subscriber status and interest tags between your front-end forms and EmailOctopus.
- **Churn Reduction Logic**
    - Intelligent triggers that offer "pause" or "frequency reduction" options before a user completes a full unsubscribe.
- **Compliance-Aware Cleanup**
    - Automatically flag and archive inactive or bounced email addresses to maintain sender reputation and deliverability.
- **Composio-Powered Integration**
    - Seamlessly connects with the EmailOctopus API to execute complex list management tasks via natural language commands.
- **Dynamic Segment Routing**
    - Automatically moves subscribers into specific interest-based lists based on their interaction with preference center updates.

---

## Use Cases
**List Hygiene & Maintenance**
- Automatically remove or suppress email addresses that consistently trigger hard bounces.
- Clean up duplicate entries across multiple EmailOctopus lists to ensure a single source of truth.

**Subscriber Retention**
- Trigger a "re-engagement" sequence when a user attempts to unsubscribe, offering alternative content frequencies.
- Update subscriber interests dynamically based on their most recent clicks or survey responses.

**Compliance & Reporting**
- Generate automated reports on unsubscribe trends to identify which content types drive the most opt-outs.
- Ensure all preference changes are logged and updated in compliance with GDPR and CAN-SPAM regulations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Subscription Preference Manager template from the solution library.
3. Connect your EmailOctopus account within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the subscriber's email address and requested preference changes.
- **Agent**: Interprets the user's intent and decides which EmailOctopus action to trigger.
- **Composio Toolset**: Executes the API calls to update subscriber status or list membership.
- **Chat Output**: Confirms the update to the user and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Update subscriber john.doe@example.com to opt-out of weekly newsletters but keep monthly updates.`
- `Check the current status of user jane.smith@example.com and move them to the 'inactive' list.`
- `Process an unsubscribe request for user support@company.com and tag them as 'churned'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for interpreting subscriber intent.
- Use a model capable of high-precision instruction following (e.g., GPT-4o).
- Instruct the agent to prioritize data accuracy when mapping subscriber email addresses.
- Configure the system prompt to handle ambiguous requests by asking for clarification before executing list changes.

### 2) Composio Toolset Node
- Provide your EmailOctopus API key within the Composio configuration.
- Set the connection scope to include `lists:write`, `subscribers:write`, and `subscribers:read` permissions.

### 3) Tool Availability
- **List Management**: Create, update, and delete subscriber list memberships.
- **Subscriber Search**: Query subscriber status by email address.
- **Preference Tagging**: Add or remove interest-based tags for granular segmentation.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automate recovery sequences for lost sales.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean, accurate data across your marketing stack.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Extend your communication strategy to mobile messaging.
