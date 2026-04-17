# Lead Qualification Processor (Uplizd) - Automated lead scoring and routing for contact forms

## Summary
The Lead Qualification Processor is an automated Uplizd AI workflow designed to streamline the intake of inbound leads from contact forms. By leveraging the Composio Toolset to integrate with your CRM, this solution instantly scores incoming inquiries, validates contact data, and routes high-intent leads to the appropriate sales representative, significantly reducing manual data entry and increasing pipeline velocity.

---

## Demo
![Lead Qualification Processor workflow diagram showing form input, AI scoring, and CRM routing](image.png)
**Alt text (SEO-ready):** Uplizd Lead Qualification Processor workflow showing automated lead scoring, CRM data integration, and sales pipeline routing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7c024607-26cd-524d-b7a1-a29144654055)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead scoring, lead routing, sales operations, data hygiene, composio, ai workflow, conversion optimization
- This solution bridges the gap between raw contact form submissions and actionable sales intelligence by automating the qualification lifecycle.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead triage and ensure no high-value opportunity is missed.

- **Sales Development Representative (SDR)**
    - Receives prioritized leads directly in the CRM, allowing for immediate outreach to high-intent prospects.
- **RevOps Manager**
    - Maintains a clean, automated pipeline with standardized scoring criteria across all inbound channels.
- **Marketing Operations Lead**
    - Ensures that lead quality feedback loops are closed by syncing form performance with actual conversion data.
- **Account Executive**
    - Focuses time on qualified opportunities rather than filtering through unqualified form submissions.

---

## Features
- **Automated Lead Scoring**
    - Assigns dynamic scores to incoming leads based on form data, company size, and intent signals.
- **Real-time CRM Sync**
    - Uses the Composio Toolset to push qualified leads directly into your CRM with pre-filled fields.
- **Intelligent Routing Logic**
    - Automatically assigns leads to the correct territory or account owner based on predefined business rules.
- **Data Validation & Enrichment**
    - Cleans and verifies contact information in real-time to ensure sales teams have accurate reach-out details.
- **Instant Notification Alerts**
    - Triggers internal alerts for high-priority leads, ensuring rapid response times for critical accounts.

---

## Use Cases
**Inbound Lead Triage**
- Automatically filter out spam or low-intent inquiries before they reach the sales dashboard.
- Route high-value enterprise leads to senior account executives based on company domain analysis.

**CRM Data Hygiene**
- Standardize lead formatting and field mapping across multiple contact form sources.
- Prevent duplicate records by checking existing CRM entries before creating new lead objects.

**Sales Velocity Optimization**
- Reduce the "lead-to-first-touch" time by automating the initial qualification and assignment process.
- Trigger automated follow-up tasks in the CRM for leads that meet specific engagement thresholds.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Processor template file.
3. Connect your CRM credentials via the Composio Toolset node.
4. Ensure nodes are correctly mapped from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw form submission data (Name, Email, Company, Message).
- **Agent**: Analyzes the input, performs scoring, and determines the qualification status.
- **Composio Toolset**: Executes CRM API calls to create or update lead records.
- **Chat Output**: Returns a confirmation summary of the lead's score and routing destination.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Process this new lead: John Doe from Acme Corp, interested in enterprise pricing.`
- `Score this inquiry: 'I need a demo for my team of 500' from a generic email address.`
- `Route this lead: Sarah Smith, CTO at TechFlow, requesting a technical integration consultation.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent gatekeeper for your sales pipeline.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Act as a Sales Operations Assistant. Score leads 1-10 based on company size and intent. Route to 'High Priority' if score > 8."
- Instruction: "Always validate email format and check for duplicate company domains before CRM entry."

### 2) Composio Toolset Node
- Provide your CRM API key (e.g., Salesforce, HubSpot) within the Composio configuration.
- Set the connection scope to allow 'Read' and 'Write' access to Lead and Account objects.

### 3) Tool Availability
- **CRM Search**: Query existing records to prevent duplicates.
- **Lead Creation**: Create new lead objects with enriched data.
- **Task Assignment**: Create follow-up tasks for assigned sales reps.
- **Data Validation**: Verify email and phone number formats.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on incoming leads.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep lead data consistent across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages once the lead is qualified.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed reports on account engagement signals.
