# Technology-Based Prospect Qualification Agent (Uplizd) - Automate lead scoring using real-time tech stack intelligence

## Summary
The Technology-Based Prospect Qualification Agent leverages Uplizd AI workflows to automatically analyze and score incoming leads based on their current technology infrastructure. By integrating real-time data from BuiltWith, this solution enables sales teams to prioritize high-value prospects, filter out unqualified leads, and increase pipeline velocity by focusing efforts on accounts that match specific technical requirements.

---

## Demo
![Technology-Based Prospect Qualification Agent workflow diagram showing lead input, BuiltWith tech stack analysis, and CRM qualification output](image.png)
**Alt text (SEO-ready):** Technology-Based Prospect Qualification Agent workflow using Uplizd, BuiltWith, and CRM integrations for automated lead scoring and sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8e67aa72-df02-59f1-a4b9-b23c1cbb5079)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead qualification, builtwith, tech stack, sales intelligence, pipeline, data enrichment, ai workflow
- This solution bridges the gap between raw lead data and actionable sales intelligence by automating the technical qualification process.

---

## Who is this for?
This agent is designed for revenue teams looking to optimize their lead management processes through data-driven technical insights.

- **Sales Development Representative (SDR)**
    - Instantly identifies if a prospect uses a competitor's technology or a complementary stack to tailor outreach.
- **Revenue Operations (RevOps) Manager**
    - Ensures only leads meeting specific technical criteria enter the high-priority sales pipeline.
- **Account Executive (AE)**
    - Receives pre-qualified leads with detailed tech stack reports, reducing time spent on manual research.
- **Growth Marketer**
    - Refines lead scoring models by incorporating firmographic and technology-based signals for better conversion.

---

## Features
- **Real-time Tech Stack Discovery**
    - Automatically queries BuiltWith to identify the software, frameworks, and infrastructure used by any prospect domain.
- **Automated Lead Scoring**
    - Assigns qualification scores based on the presence or absence of specific technologies defined in your ideal customer profile.
- **CRM Integration**
    - Seamlessly updates lead fields in your CRM with technical metadata, ensuring your sales team has the full picture.
- **Custom Qualification Logic**
    - Configures complex rules to flag leads based on specific technology triggers, such as the adoption of a new cloud service.
- **Pipeline Hygiene**
    - Automatically routes unqualified leads to a nurture sequence, keeping the active pipeline clean and focused on high-intent prospects.

---

## Use Cases
**Targeted Outbound Prospecting**
- Filter lead lists to prioritize companies currently using specific competitor technologies.
- Customize email templates dynamically based on the prospect's existing tech stack.

**CRM Data Enrichment**
- Automatically populate CRM fields with a company's primary tech stack upon lead creation.
- Maintain up-to-date technical profiles to support long-term account relationship management.

**Pipeline Prioritization**
- Flag "Ready to Buy" leads that have recently installed complementary technologies.
- Reduce manual research time by automating the technical discovery phase of the qualification process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the agent.
3. Connect your CRM and BuiltWith API credentials within the integration settings.
4. Ensure nodes are correctly linked from the input trigger to the final CRM update action.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead domain or email address to be qualified.
- **Agent**: Processes the input and executes the qualification logic against the tech stack data.
- **Composio Toolset**: Connects to BuiltWith and your CRM to fetch data and update records.
- **Chat Output**: Returns the qualification status and a summary of the prospect's technology stack.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Qualify the domain: example-tech-company.com based on their current tech stack.`
- `Check if the prospect at target-startup.io uses Salesforce and AWS.`
- `Analyze the tech stack for this lead and update their CRM status to 'Qualified' if they use HubSpot.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical researcher and lead analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize accuracy when interpreting tech stack data.
- Define clear thresholds for what constitutes a "Qualified" lead based on technology usage.

### 2) Composio Toolset Node
- Provide your BuiltWith API key to enable domain-level technology lookups.
- Configure CRM connection scopes to allow the agent to read lead data and update custom fields.

### 3) Tool Availability
- **BuiltWith API**: For deep-dive technology infrastructure reports.
- **CRM Connector**: For reading lead information and writing qualification results.
- **Data Formatter**: For cleaning and standardizing tech stack output before CRM ingestion.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with contact and firmographic details.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive into target accounts using ZoomInfo intelligence.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and account data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Monitor and score deal opportunities for sales teams.
