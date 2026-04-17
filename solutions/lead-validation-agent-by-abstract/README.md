# Lead Validation Agent (Uplizd) - Automated lead scoring and data verification for sales teams

## Summary
The Lead Validation Agent is an intelligent Uplizd workflow designed to automate the verification and scoring of incoming leads, ensuring sales teams focus only on high-intent prospects. By integrating real-time data enrichment and validation logic, this agent eliminates manual data entry, reduces pipeline friction, and maintains high-quality CRM hygiene, ultimately increasing conversion rates and sales pipeline velocity.

---

## Demo
![Lead Validation Agent workflow showing input, enrichment, and CRM update nodes](image.png)
**Alt text (SEO-ready):** Lead Validation Agent workflow in Uplizd, showing automated lead scoring, data enrichment, and CRM integration for sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwCuA/AA0G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8A)https://uplizd.ai/solutions/37253c51-22aa-5ea9-96e1-23b82bd0cce4](https://uplizd.ai/solutions/37253c51-22aa-5ea9-96e1-23b82bd0cce4)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, lead scoring, data enrichment, sales pipeline, lead qualification, composio, ai workflow, data hygiene.
This solution bridges the gap between raw lead ingestion and actionable sales intelligence through automated validation.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to scale their outreach without sacrificing lead quality.

- **Sales Development Reps (SDRs)**
    - Spend less time manually researching prospects and more time engaging with qualified leads.
- **Revenue Operations (RevOps)**
    - Maintain a clean, standardized CRM database by automating field validation and enrichment.
- **Sales Managers**
    - Ensure pipeline visibility is accurate by filtering out low-intent or invalid contact entries.
- **Marketing Operations**
    - Improve lead-to-opportunity conversion rates by ensuring only high-quality data reaches the sales team.

---

## Features
- **Real-time Data Enrichment**
    - Automatically pulls firmographic and contact data to fill missing fields in your CRM.
- **Intelligent Lead Scoring**
    - Assigns dynamic scores based on predefined criteria like company size, industry, and job title.
- **Automated Validation Logic**
    - Checks email deliverability and phone number validity before pushing data to your sales stack.
- **Seamless CRM Integration**
    - Uses the Composio Toolset to push validated data directly to Salesforce, HubSpot, or Pipedrive.
- **Customizable Thresholds**
    - Allows teams to set specific "pass/fail" criteria for leads to enter the active sales pipeline.

---

## Use Cases
**Lead Qualification**
- Automatically flag leads that match your Ideal Customer Profile (ICP) for immediate follow-up.
- Filter out generic or personal email addresses to protect your domain reputation.

**CRM Data Hygiene**
- Standardize company names and job titles across your entire database during the ingestion phase.
- Remove duplicate entries by checking existing records before creating new opportunities.

**Pipeline Velocity**
- Route high-scoring leads directly to the appropriate AE's queue in real-time.
- Trigger automated Slack or email notifications to the sales team when a "Hot Lead" is validated.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Validation Agent JSON configuration file.
3. Connect your preferred CRM and data enrichment tool via the Composio Toolset.
4. Ensure nodes are correctly mapped from input to output and verify all API credentials are active.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data (name, email, company) from your web form or CRM webhook.
- **Agent**: Processes the data using validation logic and scoring instructions.
- **Composio Toolset**: Executes external lookups and writes validated data back to your CRM.
- **Chat Output**: Confirms the validation status and provides a summary of the lead score.

### 3) Run the Flow
Use the Playground to test the agent with these example prompts:
- `Validate this lead: John Doe, john.doe@company.com, Company Inc.`
- `Score the following lead based on our enterprise ICP: [Insert Lead Data]`
- `Check if this lead exists in Salesforce and enrich their profile if missing.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for lead assessment.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize accuracy over speed when validating contact information.
- Ensure the agent follows strict JSON output schemas for CRM compatibility.

### 2) Composio Toolset Node
- Provide a valid API key for your Composio account.
- Set the connection scope to include read/write access for your specific CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- **CRM Connector**: For searching, updating, and creating lead records.
- **Email Validator**: For checking the existence and deliverability of lead email addresses.
- **Enrichment API**: For fetching missing firmographic data based on company domains.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Deep research and firmographic enrichment for target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score deal progression throughout the sales lifecycle.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automated research to prepare sales teams for discovery calls.
