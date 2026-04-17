# Account Intelligence Reporter (Uplizd) - Automate website visitor insights and account reporting

## Summary
The Account Intelligence Reporter (Uplizd) workflow automates the extraction and synthesis of visitor data from Leadfeeder, transforming raw web traffic into actionable account intelligence reports. By bridging the gap between anonymous website activity and CRM-ready insights, this solution empowers sales and marketing teams to prioritize high-intent accounts, accelerate pipeline velocity, and ensure a single source of truth for account-based marketing (ABM) strategies.

---

## Demo
![Account Intelligence Reporter workflow dashboard showing Leadfeeder data integration and automated report generation](../image.png)
**Alt text (SEO-ready):** Uplizd Account Intelligence Reporter workflow, automating Leadfeeder data synthesis for sales intelligence and account-based marketing pipeline growth.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ca85555b-5b18-5b50-9677-58bcaf9fa178)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** leadfeeder, account intelligence, abm, sales pipeline, lead qualification, crm, data enrichment, ai workflow
- This solution streamlines the conversion of raw web visitor data into structured account reports to drive smarter sales outreach.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to turn website traffic into qualified sales opportunities.

- **Sales Development Representative (SDR)**
    - Quickly identify and prioritize high-intent accounts based on real-time website engagement signals.
- **Account Executive (AE)**
    - Access pre-synthesized account dossiers to personalize outreach and improve conversion rates during discovery calls.
- **Marketing Operations Manager**
    - Automate the flow of visitor intelligence into the CRM to maintain data hygiene and improve lead scoring accuracy.
- **Growth Strategist**
    - Analyze visitor trends and account behavior to refine targeting parameters for ongoing ABM campaigns.

---

## Features
- **Automated Data Extraction**
    - Seamlessly pulls visitor firmographics and behavioral data from Leadfeeder via the Composio Toolset.
- **Intelligent Report Synthesis**
    - Uses advanced LLM logic to summarize complex visitor activity into concise, actionable account intelligence reports.
- **CRM Integration Ready**
    - Formats extracted insights for direct ingestion into your CRM, ensuring sales teams have the latest context.
- **Real-time Signal Prioritization**
    - Automatically flags accounts showing high-intent activity, such as repeat visits or engagement with pricing pages.
- **Customizable Output Templates**
    - Generates reports tailored to specific sales needs, whether for cold outreach, follow-ups, or executive briefings.

---

## Use Cases
**Account-Based Marketing (ABM) Prioritization**
- Automatically generate daily summaries of top-tier accounts visiting your website.
- Flag high-value prospects that have engaged with specific product pages for immediate SDR outreach.

**Sales Outreach Personalization**
- Create "cheat sheets" for AEs containing recent visitor activity and company firmographics before a scheduled meeting.
- Tailor cold email sequences based on the specific content and pages an account has interacted with.

**Lead Qualification & Hygiene**
- Filter out low-intent traffic and focus resources only on accounts that meet your ideal customer profile (ICP).
- Maintain a clean, updated log of account interest levels within your CRM to improve lead scoring models.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your Leadfeeder and CRM credentials within the Composio Toolset node.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and save the flow.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger or manual request for an account report.
- **Agent**: Processes visitor data and synthesizes insights based on your specific sales criteria.
- **Composio Toolset**: Executes API calls to fetch real-time data from Leadfeeder and external sources.
- **Chat Output**: Delivers the final, formatted account intelligence report to your dashboard or notification channel.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Generate an account intelligence report for all companies that visited our pricing page in the last 24 hours.`
- `Create a summary of high-intent accounts from the technology sector that visited our site this week.`
- `List the top 5 accounts by engagement score and provide a brief summary of their recent website activity.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence layer, interpreting raw data into human-readable reports.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data synthesis.
- Instruct the agent to prioritize firmographic data like company size, industry, and revenue.
- Configure the agent to format outputs in clear, bulleted sections for quick reading by sales reps.

### 2) Composio Toolset Node
- Authenticate with your Leadfeeder API key within the Composio dashboard.
- Set the connection scope to allow read-only access to visitor data and account firmographics.

### 3) Tool Availability
- **Leadfeeder API**: For fetching visitor logs, company details, and engagement metrics.
- **CRM Connector**: For pushing synthesized reports to specific account records.
- **Data Enrichment Tools**: Optional secondary tools to append contact information to the generated reports.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on target accounts.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with contact-level details.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages within your CRM.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize account data across multiple platforms.
