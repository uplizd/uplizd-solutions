# Customer Success Playbook Executor (Uplizd) - Automate account health and success workflows

## Summary
The Customer Success Playbook Executor is an intelligent Uplizd AI workflow designed to automate high-touch account management tasks by triggering playbooks based on real-time account health signals. By integrating Process Street with your CRM, this solution ensures that customer success managers (CSMs) follow standardized, repeatable processes—such as onboarding sequences or churn prevention playbooks—without manual intervention, significantly increasing team velocity and ensuring consistent customer outcomes.

---

## Demo
![Customer Success Playbook Executor workflow showing account trigger to Process Street action](image.png)
**Alt text (SEO-ready):** Customer Success Playbook Executor workflow in Uplizd showing automated account health triggers and Process Street playbook execution.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6352P7wAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVHjaY2BgYPhPAwJgEqZpGEY1gA0Gg2gYhGEwGgYhGAAAM7oB/6J1+q8AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/b7c548d4-7f6c-5427-b7fa-6bc6eefe6b2e)

---

## Category
**Primary category:** Customer Success
**Secondary tags:** customer success, process street, automation, account health, onboarding, churn prevention, workflow, composio

This solution bridges the gap between account intelligence and actionable operational playbooks to drive consistent customer success outcomes.

---

## Who is this for?
This solution is designed for RevOps and Customer Success teams looking to scale their high-touch engagement models.

*   **Customer Success Manager (CSM)**
    *   Reduces manual administrative overhead by auto-launching playbooks when account health scores drop.
*   **Operations Manager**
    *   Standardizes team processes across the entire customer lifecycle to ensure compliance and quality.
*   **Account Executive**
    *   Ensures a seamless transition from sales to success by triggering onboarding workflows immediately upon deal closure.
*   **Head of Customer Success**
    *   Gains visibility into playbook execution rates and ensures that every customer receives timely, proactive attention.

---

## Features
- **Automated Playbook Triggering**
  Instantly launch specific Process Street workflows when account data in your CRM hits predefined thresholds.
- **Real-time Health Monitoring**
  Utilize the Composio Toolset to monitor account usage and engagement data, ensuring playbooks are relevant to current account status.
- **Dynamic Task Assignment**
  Automatically assign tasks within Process Street to the correct CSM based on account ownership or tier.
- **Cross-Platform Synchronization**
  Maintain a single source of truth by syncing account status updates between your CRM and your operational playbook platform.
- **Proactive Churn Prevention**
  Trigger "at-risk" playbooks automatically when usage metrics decline, allowing the team to intervene before churn happens.

---

## Use Cases
**Onboarding Automation**
*   Trigger a "New Customer Onboarding" checklist in Process Street the moment a deal is marked as "Closed Won" in your CRM.
*   Automatically populate onboarding tasks with customer contact details and account requirements gathered from the CRM.

**Account Health Management**
*   Launch a "Low Engagement" recovery playbook when usage drops below a specific threshold over a 30-day period.
*   Notify the assigned CSM via a task update in Process Street when an account health score changes from "Healthy" to "At Risk."

**Renewal & Expansion**
*   Initiate a "Renewal Planning" workflow 90 days before a contract expiration date to ensure timely outreach.
*   Trigger an "Upsell Opportunity" playbook when an account reaches a specific usage milestone or feature adoption level.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Success Playbook Executor template.
3. Connect your CRM and Process Street accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped from the trigger to the final output to verify the data flow.

### 2) Setup the Nodes
*   **Chat Input**: Receives the account trigger signal or manual command to initiate a playbook.
*   **Agent**: Evaluates the account data and determines which Process Street playbook is required.
*   **Composio Toolset**: Executes the API calls to create or update tasks in Process Street.
*   **Chat Output**: Confirms the successful launch of the playbook and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your configuration with these example prompts:
* `Launch the onboarding playbook for account ID 12345.`
* `Check current health for Acme Corp and trigger the churn prevention workflow if score is below 50.`
* `Create a renewal task for the account owner of Global Tech in Process Street.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision engine, parsing account signals and mapping them to specific operational playbooks.
*   Maintain a neutral, professional tone for all internal task descriptions.
*   Prioritize accuracy when mapping CRM account tiers to Process Street playbook templates.
*   Always confirm the account ID and owner before triggering a new process.

### 2) Composio Toolset Node
Provide your API keys for both your CRM and Process Street. Ensure the connection scope includes read access for account data and write access for task creation.

### 3) Tool Availability
*   **CRM Read/Write**: For fetching account health scores and updating status fields.
*   **Process Street API**: For creating, updating, and assigning checklists and tasks.
*   **Notification Service**: For alerting CSMs when a new playbook has been assigned.

---

## Related Solutions
* [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven support ticket resolution.
* [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Track and report on account usage metrics.
* [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose workflow automation for business operations.
