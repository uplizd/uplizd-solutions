# Automated Contact List Hygiene Manager (Uplizd) - Maintain clean, compliant, and high-performing email lists

## Summary
The Automated Contact List Hygiene Manager is an intelligent Uplizd workflow that streamlines email list maintenance by identifying inactive, invalid, or unengaged contacts. By automating the scrubbing process, marketing and operations teams ensure higher deliverability rates, maintain sender reputation, and reduce costs associated with bloated, low-quality subscriber databases.

---

## Demo
![Automated Contact List Hygiene Manager workflow showing data scrubbing and validation steps](image.png)
**Alt text (SEO-ready):** Automated Contact List Hygiene Manager workflow for email list scrubbing, data validation, and CRM hygiene using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0bae26b2-0d57-576c-a61c-a462d52af3f3)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, list hygiene, data cleansing, crm, benchmark email, automation, composio, deliverability
- This solution optimizes marketing performance by ensuring your communication channels remain populated with high-intent, verified contacts.

---

## Who is this for?
This solution is designed for professionals responsible for maintaining database integrity and maximizing campaign ROI.

- **Email Marketing Manager**
    - Automates the removal of hard bounces and inactive subscribers to improve sender reputation.
- **CRM Administrator**
    - Maintains a single source of truth by synchronizing clean data across marketing platforms and sales databases.
- **Growth Marketer**
    - Ensures that high-value segments are not diluted by low-quality or outdated contact information.
- **Operations Analyst**
    - Reduces platform subscription costs by purging invalid records that inflate database size.

---

## Features
- **Automated List Scrubbing**
    - Triggers periodic scans to identify and remove invalid or non-responsive email addresses from your Benchmark Email lists.
- **Real-time Data Validation**
    - Uses the Composio Toolset to verify contact status against live CRM records before sending campaigns.
- **Engagement-Based Segmentation**
    - Automatically tags or moves contacts to suppression lists based on defined inactivity thresholds.
- **Compliance-Aware Cleanup**
    - Ensures adherence to data privacy regulations by managing opt-out requests and consent status automatically.
- **Performance Reporting**
    - Provides summary logs of cleaned records, helping teams track list health over time.

---

## Use Cases
**List Maintenance & Deliverability**
- Automatically purge contacts that have returned hard bounces across three consecutive campaigns.
- Identify and archive subscribers who have not opened an email in the last 180 days to boost open rates.

**CRM & Marketing Sync**
- Sync suppression lists between Benchmark Email and your primary CRM to prevent accidental re-engagement.
- Update contact status fields in real-time when a user unsubscribes via a landing page form.

**Compliance & Data Hygiene**
- Flag duplicate contact entries across multiple lists to ensure a unified customer view.
- Automate the removal of role-based email addresses (e.g., info@, support@) to maintain list quality.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Benchmark Email and CRM accounts via the Composio integration dashboard.
3. Configure your target list IDs and inactivity thresholds within the Agent node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to initiate the hygiene scan.
- **Agent**: Analyzes contact data, evaluates engagement metrics, and decides which records require action.
- **Composio Toolset**: Executes API calls to Benchmark Email and your CRM to update or remove contact records.
- **Chat Output**: Returns a summary report of the cleanup operation, including total records processed and deleted.

### 3) Run the Flow
Use the Playground to test your hygiene logic:
- `Run a full hygiene scan on my 'Newsletter' list and report back.`
- `Identify all inactive contacts from the last 6 months and move them to the suppression list.`
- `Clean my primary CRM list by removing all hard-bounced email addresses.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for your data hygiene strategy.
- Use a model capable of structured data processing (e.g., GPT-4o).
- Instruct the agent to prioritize accuracy when identifying invalid email formats.
- Define clear thresholds for "inactivity" to prevent accidental removal of active leads.

### 2) Composio Toolset Node
- Provide your Benchmark Email API key and CRM credentials within the Composio connection settings.
- Ensure the connection scope includes read/write access to contact lists and subscriber status fields.

### 3) Tool Availability
- **Benchmark Email API**: For list retrieval, contact status updates, and suppression management.
- **CRM Integration**: For cross-referencing contact data and updating lifecycle stages.
- **Logging/Reporting**: For generating post-run summaries of actions taken.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automates follow-ups for users who leave items in their cart.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - General purpose data cleansing and formatting for CRM databases.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Engages leads via WhatsApp to maintain high-quality communication channels.
