# Lead Email Qualifier Agent (Uplizd) - Automated lead verification and email hygiene for sales outreach

## Summary
The Lead Email Qualifier Agent is an intelligent Uplizd workflow designed to automate the verification and scoring of lead email addresses. By integrating real-time validation via the EmailListVerify API, this agent ensures your sales pipeline remains clean, reduces bounce rates, and improves deliverability for outbound campaigns. It serves as a single source of truth for lead data hygiene, allowing RevOps and sales teams to focus their efforts on high-quality, reachable prospects.

---

## Demo
![Lead Email Qualifier Agent workflow showing email input, EmailListVerify tool integration, and validation output](image.png)
**Alt text (SEO-ready):** Lead Email Qualifier Agent workflow in Uplizd, featuring EmailListVerify integration for automated CRM data hygiene and sales lead validation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c708b152-f0d0-58a1-93c9-122f4ccc0776)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, email marketing, lead qualification, data hygiene, sales outreach, composio, ai workflow, lead management
- This solution bridges the gap between raw lead generation and actionable sales data by automating the verification process within your existing CRM ecosystem.

---

## Who is this for?
This solution is designed for teams looking to optimize their outreach efficiency and maintain high-quality prospect databases.

- **Sales Development Representative (SDR)**
  - Spend less time on manual list scrubbing and more time engaging with verified, high-intent prospects.
- **Revenue Operations Manager**
  - Maintain pristine CRM data hygiene by automatically filtering out invalid or risky email addresses before they enter the pipeline.
- **Marketing Operations Specialist**
  - Improve email campaign deliverability and sender reputation by ensuring only validated leads receive marketing communications.
- **Growth Lead**
  - Scale outbound efforts confidently by automating the lead qualification process, reducing bounce-related costs and account blocks.

---

## Features
- **Real-time Email Verification**
  - Instantly check the validity of email addresses using the EmailListVerify API to prevent bounce-backs.
- **Automated Lead Scoring**
  - Assign quality scores to leads based on email deliverability status, allowing for prioritized outreach.
- **Composio Toolset Integration**
  - Seamlessly connect the Uplizd agent to your email verification tools and CRM platforms for end-to-end automation.
- **Bulk Data Processing**
  - Efficiently handle large lists of leads, ensuring consistent data quality across your entire prospect database.
- **Intelligent Error Handling**
  - Automatically flag catch-all, disposable, or invalid email formats for manual review or exclusion from sequences.

---

## Use Cases
**Lead List Hygiene**
- Automatically scrub imported CSV leads to remove invalid or syntax-error email addresses before they reach the sales team.
- Regularly audit existing CRM contacts to identify and remove decayed email addresses that could harm sender reputation.

**Outbound Campaign Preparation**
- Validate new leads captured via web forms in real-time to ensure immediate follow-up is directed to reachable accounts.
- Pre-qualify leads before adding them to automated email sequences to maximize open rates and minimize bounce-related account suspensions.

**Sales Pipeline Optimization**
- Flag high-risk leads for manual verification, ensuring that only verified prospects move to the 'Qualified' stage in your CRM.
- Sync verified lead status back to your CRM to trigger automated follow-up workflows for high-quality prospects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Email Qualifier Agent template from the solution library.
3. Connect your preferred CRM and the EmailListVerify API key within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead email address or list of contacts for processing.
- **Agent**: Analyzes the input and determines the necessary verification steps.
- **Composio Toolset**: Executes the API calls to verify email validity and deliverability.
- **Chat Output**: Returns the validation status, quality score, and recommended next steps.

### 3) Run the Flow
Use the Uplizd Playground to test your agent with the following prompts:
- `Verify the email address: contact@example.com and provide a quality score.`
- `Check if the following list of leads is valid for our upcoming outreach campaign: [list of emails].`
- `Identify any disposable or risky email addresses in this batch and flag them for removal.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data validation specialist that interprets API responses to provide actionable insights.
- Instruct the agent to prioritize deliverability status over syntax.
- Configure the agent to output results in a structured format (JSON or table) for easy CRM integration.
- Set clear thresholds for what constitutes a "Qualified" lead versus a "Risky" lead.

### 2) Composio Toolset Node
- Provide your **EmailListVerify API Key** to enable real-time validation capabilities.
- Define the scope to allow the agent to read lead data from your CRM and write back the verification status.

### 3) Tool Availability
- **Email Verification API**: Performs syntax, domain, and mailbox existence checks.
- **CRM Connector**: Updates lead fields (e.g., `Email_Status`, `Lead_Quality_Score`) based on verification results.
- **Data Logger**: Records verification history for compliance and audit purposes.

---

## Related Solutions
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate bulk data cleanup and formatting to maintain a healthy CRM.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensure seamless synchronization of lead data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score high-value opportunities within your sales pipeline.
