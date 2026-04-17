# Connection Insights Reporter (Uplizd) - Transform network data into actionable sales intelligence

## Summary
The Connection Insights Reporter is an automated Uplizd AI workflow that synthesizes raw connection data into high-value sales intelligence. By leveraging the Composio Toolset to interface with Leadoku and CRM platforms, this solution identifies key relationship signals, provides account-level context, and accelerates pipeline velocity for revenue teams.

---

## Demo
![Connection Insights Reporter workflow dashboard showing data synthesis from Leadoku into CRM insights](image.png)
**Alt text (SEO-ready):** Connection Insights Reporter Uplizd workflow showing automated Leadoku data synthesis, sales intelligence, and CRM integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/39f8d3f5-0c8a-538c-aebd-3c3601e64006)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, leadoku, sales intelligence, pipeline, data sync, account research, composio, ai workflow
This solution bridges the gap between raw professional network data and actionable CRM insights to drive smarter sales outreach.

---

## Who is this for?
This solution is designed for revenue-focused professionals who need to turn fragmented connection data into a strategic advantage.

- **Account Executives**
    - Quickly identify warm entry points into target accounts based on existing network connections.
- **Sales Development Reps**
    - Prioritize daily outreach by focusing on prospects with the highest relationship relevance.
- **Revenue Operations Managers**
    - Ensure CRM data remains enriched with real-time intelligence for better pipeline forecasting.
- **Growth Marketers**
    - Leverage connection insights to tailor account-based marketing campaigns for higher conversion.

---

## Features
- **Automated Data Synthesis**
  Aggregates raw connection signals from Leadoku into a structured format ready for CRM ingestion.
- **Real-time Relationship Scoring**
  Applies AI logic to rank connections based on engagement potential and account relevance.
- **Seamless CRM Integration**
  Uses the Composio Toolset to push enriched insights directly into your existing sales stack.
- **Actionable Intelligence Extraction**
  Identifies key decision-makers and provides context-aware summaries for personalized outreach.
- **Pipeline Velocity Optimization**
  Reduces research time by automating the discovery of relationship-based opportunities.

---

## Use Cases
**Relationship Mapping**
- Automatically map connections to open opportunities to identify internal champions.
- Flag stale accounts that require a fresh touchpoint based on new network activity.

**Lead Prioritization**
- Score incoming leads based on existing mutual connections within your professional network.
- Filter high-intent prospects who have recently engaged with your company's digital presence.

**Account Research**
- Generate comprehensive briefing notes for upcoming meetings using aggregated connection data.
- Sync contact-level intelligence to ensure sales teams have the latest context before every call.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Connection Insights Reporter solution.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Leadoku and CRM accounts via the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target account name or prospect list for analysis.
- **Agent**: Processes connection data and generates actionable sales summaries.
- **Composio Toolset**: Executes secure API calls to fetch network data and update CRM fields.
- **Chat Output**: Delivers the final intelligence report directly to your dashboard or Slack channel.

### 3) Run the Flow
Use the Playground to test your connection insights:
- `Analyze all connections for the 'Acme Corp' account and summarize key relationship signals.`
- `Find high-potential leads in my network for the 'Tech Solutions' sector.`
- `Update my CRM with the latest relationship intelligence for all active opportunities.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting connection signals and formatting them for sales teams.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data synthesis.
- Instruct the agent to prioritize "warm" signals over generic network data.
- Ensure the output format is strictly mapped to your CRM's custom field requirements.

### 2) Composio Toolset Node
- Authenticate with your Leadoku API key to enable data retrieval.
- Set the connection scope to allow read access to network data and write access to your CRM's contact/opportunity objects.

### 3) Tool Availability
- **Leadoku Search**: Fetches professional network connections and metadata.
- **CRM Update**: Performs bulk or individual updates to contact records.
- **Data Formatter**: Cleans and normalizes connection data before CRM ingestion.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account records with deep firmographic data.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into target prospects.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across multiple platforms to maintain a single source of truth.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Strengthen account ties using automated relationship mapping.
