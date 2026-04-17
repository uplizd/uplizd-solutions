# Lead Email Discovery Agent (Uplizd) - Automate prospect contact acquisition and verification

## Summary
The Lead Email Discovery Agent is an intelligent Uplizd workflow designed to streamline sales prospecting by automatically identifying and verifying professional email addresses from company domains. By integrating real-time data lookups with AI-driven validation, this solution eliminates manual research, ensures high-quality lead data, and significantly accelerates pipeline velocity for sales and marketing teams.

---

## Demo
![Lead Email Discovery Agent workflow interface showing automated email lookup and verification nodes](image.png)
**Alt text (SEO-ready):** Lead Email Discovery Agent workflow by Uplizd, featuring automated email lookup, ZeroBounce integration, and prospect contact verification for sales teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d53a57ba-df5f-5080-8b6e-6fac275a97af)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead generation, email verification, zerobounce, sales prospecting, crm, data enrichment, pipeline, composio
- This solution bridges the gap between raw company data and actionable contact information, serving as a critical component in modern RevOps stacks.

---

## Who is this for?
This agent is designed for professionals who need to scale their outreach efforts without sacrificing data quality.

- **Sales Development Representative (SDR)**
    - Quickly build high-intent lead lists by converting company domains into verified contact points.
- **Growth Marketer**
    - Automate the enrichment of inbound leads to ensure marketing campaigns reach the correct decision-makers.
- **Revenue Operations (RevOps) Manager**
    - Maintain data hygiene by ensuring only valid, deliverable email addresses enter the CRM.
- **Account Executive (AE)**
    - Reduce time spent on manual administrative research, allowing more focus on high-value prospect engagement.

---

## Features
- **Automated Domain Lookup**
    - Leverages advanced search tools to identify potential email patterns associated with specific company domains.
- **Real-time Email Verification**
    - Integrates with ZeroBounce to validate email deliverability, reducing bounce rates and protecting sender reputation.
- **CRM Integration**
    - Seamlessly pushes verified contact data directly into your existing CRM workflows via the Composio Toolset.
- **Intelligent Deduplication**
    - Automatically checks existing records to prevent duplicate entries and maintain a clean, single source of truth.
- **Customizable Confidence Scoring**
    - Filters results based on verification confidence levels, ensuring only high-quality leads reach your sales pipeline.

---

## Use Cases
**Outbound Prospecting**
- Automatically generate a list of verified decision-maker emails from a target company domain list.
- Enrich cold lead data with direct contact information to improve multi-channel outreach effectiveness.

**Lead Qualification**
- Validate incoming lead data in real-time to ensure sales teams are only working with reachable prospects.
- Filter out invalid or risky email addresses before they are assigned to a sales representative.

**Data Hygiene**
- Periodically scan existing CRM records to identify and update decayed contact information.
- Cleanse bulk lead imports to maintain high deliverability rates for automated email sequences.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Email Discovery Agent template from the marketplace.
3. Connect your ZeroBounce and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company domain or lead name.
- **Agent**: Analyzes the input and determines the necessary search and verification steps.
- **Composio Toolset**: Executes the API calls to search for emails and verify their status.
- **Chat Output**: Returns the verified email address and confidence score to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Find and verify the email address for the CEO of example-company.com`
- `Search for marketing manager contacts at tech-startup.io and validate their emails`
- `Check the deliverability of john.doe@target-corp.com and add to CRM if valid`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your input and the email discovery tools.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruct the agent to prioritize high-confidence verification results.
- Ensure the agent is configured to handle "no result found" scenarios gracefully.

### 2) Composio Toolset Node
- Provide your ZeroBounce API key within the Composio connection settings.
- Ensure the connection scope includes read/write access to your CRM (e.g., Salesforce or HubSpot) for automated data entry.

### 3) Tool Availability
- **Email Discovery API**: For pattern-based email identification.
- **ZeroBounce API**: For real-time deliverability and status verification.
- **CRM Connector**: For updating contact records with verified data.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with deep firmographic and contact insights.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new sales opportunities from enriched lead data.
