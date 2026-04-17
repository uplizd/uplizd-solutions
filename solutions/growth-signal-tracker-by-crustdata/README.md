# Growth Signal Tracker (Uplizd) - Automate high-intent prospect monitoring and pipeline alerts

## Summary
The Growth Signal Tracker (Uplizd) is an intelligent automation workflow designed to monitor, identify, and alert revenue teams on high-intent prospect signals in real-time. By leveraging the Crustdata integration, this solution transforms raw market data into actionable pipeline opportunities, ensuring sales teams never miss a critical buying signal or account expansion trigger.

---

## Demo
![Growth Signal Tracker workflow dashboard showing real-time prospect signal identification and CRM alert automation](image.png)
**Alt text (SEO-ready):** Growth Signal Tracker workflow dashboard showing real-time prospect signal identification and CRM alert automation via Uplizd and Crustdata.

---

## 🚀 Run on Uplizd
[Launch 'Growth Signal Tracker'](https://uplizd.ai/solutions/0e84e109-2cd7-5db8-b570-ce16ce51258d)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, crustdata, sales intelligence, lead scoring, pipeline, growth, composio, ai workflow
- This solution bridges the gap between raw market signals and CRM execution, enabling data-driven outreach for modern sales teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to prioritize their outreach based on verified market intent.

- **Sales Development Rep (SDR)**
    - Receives instant notifications when target accounts show high-intent growth signals.
- **Account Executive (AE)**
    - Gains context-rich insights to tailor discovery calls and improve conversion rates.
- **Revenue Operations (RevOps)**
    - Automates the hygiene and enrichment of lead data to maintain a clean, actionable pipeline.
- **Growth Marketer**
    - Identifies emerging market trends and account behaviors to refine targeting strategies.

---

## Features
- **Real-time Signal Monitoring**
    - Automatically polls Crustdata for specific growth indicators, such as headcount changes or funding rounds.
- **Intelligent Lead Scoring**
    - Uses AI to evaluate signal strength, ensuring sales teams focus only on the highest-probability opportunities.
- **CRM Integration**
    - Seamlessly pushes qualified signals into your CRM via the Composio Toolset to update lead records instantly.
- **Automated Alerting**
    - Triggers Slack or email notifications to the relevant account owner the moment a signal is validated.
- **Customizable Thresholds**
    - Allows users to define specific growth metrics that trigger an automated workflow response.

---

## Use Cases
**Pipeline Acceleration**
- Automatically flag accounts that have recently increased their engineering headcount for targeted outreach.
- Update CRM opportunity stages based on external growth signals detected by the agent.

**Account Expansion**
- Identify existing customers showing "high growth" signals to trigger an upsell conversation.
- Monitor competitor-related signals to proactively defend at-risk accounts.

**Lead Qualification**
- Filter out low-intent noise by setting strict criteria for what constitutes a "Growth Signal."
- Enrich lead profiles with real-time market data to provide context for initial outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Launch" link above to open the template in the Uplizd builder.
2. Connect your Crustdata API key and CRM credentials within the Composio integration settings.
3. Configure your target account lists or search parameters in the initial node.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Defines the search parameters and target account lists for the agent.
- **Agent**: Processes market data and determines if signals meet the defined growth threshold.
- **Composio Toolset**: Executes data retrieval from Crustdata and writes updates to your CRM.
- **Chat Output**: Delivers a summary of identified signals and actions taken to the user.

### 3) Run the Flow
Use the Playground to test your signal tracking:
- `Find all accounts in my CRM that have increased headcount by 20% in the last quarter.`
- `Monitor for new funding rounds among my top 50 target accounts and alert me via Slack.`
- `Identify high-growth companies in the SaaS sector and add them to the 'Prospecting' list in Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the analytical engine that interprets raw data signals.
- Use a model capable of logical reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize signals based on the user's specific ICP (Ideal Customer Profile).
- Ensure the agent is configured to output structured data for CRM mapping.

### 2) Composio Toolset Node
- Provide your Crustdata API key to enable market intelligence gathering.
- Configure the connection scope to allow read access to market data and write access to your CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- **Crustdata API**: For fetching real-time company growth and funding data.
- **CRM Connector**: For updating lead status, adding notes, or creating new opportunities.
- **Notification Service**: For sending alerts to Slack, Microsoft Teams, or email.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with contact-level insights.
- [Account Expansion Identifier](../account-expansion-identifier-by-crustdata/README.md) — Detect expansion opportunities within existing customer bases.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Score and track deal progression through the sales pipeline.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep multi-platform CRM data consistent and conflict-free.
