# DFO Guild Scout (Uplizd) - Automated guild member scouting and recruitment analysis

## Summary
The DFO Guild Scout is an intelligent automation workflow designed to streamline the process of identifying, vetting, and recruiting potential members for Dungeon Fighter Online guilds. By leveraging real-time data analysis, this solution enables guild leaders to maintain optimal roster health, track player activity, and automate the outreach process, ensuring a competitive and active community without the manual overhead of traditional scouting.

---

## Demo
![DFO Guild Scout workflow interface showing automated player data extraction and recruitment filtering](image.png)

**Alt text (SEO-ready):** DFO Guild Scout workflow interface showing automated player data extraction and recruitment filtering for Uplizd AI guild management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0c563e49-b80a-52dc-9c09-7e8a5c4b0a4d)

---

## Category
**Primary category:** Operations  
**Secondary tags:** dfo, gaming, guild management, recruitment, player analysis, automation, community growth, composio  
This solution bridges the gap between raw player data and actionable recruitment insights for DFO guild leaders.

---

## Who is this for?
This solution is designed for gaming community leaders and guild administrators looking to professionalize their recruitment operations.

- **Guild Leaders**
    - Automate the identification of high-performing players to maintain roster dominance.
- **Recruitment Officers**
    - Reduce manual scouting time by filtering potential candidates based on specific activity metrics.
- **Community Managers**
    - Monitor guild health and member engagement levels through automated reporting.
- **Competitive Players**
    - Quickly identify guilds that align with their specific playstyle and activity requirements.

---

## Features
- **Automated Player Scouting**
  Real-time scanning of player profiles to identify candidates that meet your guild's specific criteria.
- **Customizable Recruitment Filters**
  Define thresholds for player level, activity frequency, and gear score to ensure high-quality recruitment.
- **Composio-Powered Data Integration**
  Seamlessly connects with gaming data APIs to pull accurate, up-to-date player statistics.
- **Outreach Pipeline Management**
  Tracks the status of recruitment invitations to prevent duplicate outreach and improve conversion rates.
- **Roster Health Analytics**
  Provides actionable insights into member retention and activity trends to keep your guild thriving.

---

## Use Cases
**Guild Recruitment Scaling**
- Automatically generate a daily list of potential recruits based on server activity.
- Filter candidates by class or specialization to fill specific roster gaps.

**Member Retention Monitoring**
- Track inactivity windows to identify members who may need follow-up or replacement.
- Generate reports on guild performance metrics to share with core leadership.

**Competitive Intelligence**
- Monitor top-tier player movements to identify potential talent before other guilds.
- Analyze recruitment trends across different servers to adjust your outreach strategy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the DFO Guild Scout template file.
3. Configure your API credentials within the Composio Toolset node.
4. Ensure nodes are connected as **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your scouting parameters (e.g., "Find active players level 100+").
- **Agent**: Processes the request and determines the necessary data points to fetch.
- **Composio Toolset**: Executes the API calls to retrieve player data and guild statistics.
- **Chat Output**: Delivers a formatted list of recommended recruits or guild insights.

### 3) Run the Flow
Use the Playground to test your scouting logic:
- `Find 5 active players on the Cain server with high activity levels.`
- `List potential recruits for my guild that specialize in support roles.`
- `Analyze the current recruitment trends for top-tier guilds this week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your primary scouting assistant, interpreting natural language queries into data-driven search parameters.
- Focus on identifying key performance indicators (KPIs) for guild members.
- Maintain a professional and objective tone when summarizing player data.
- Prioritize accuracy by cross-referencing multiple data points before recommending a recruit.

### 2) Composio Toolset Node
Requires a valid API key for the relevant gaming data provider. Ensure the connection scope includes read-only access to player profiles and guild activity logs to maintain security.

### 3) Tool Availability
- **Player Search**: Capability to query player profiles by level, class, and server.
- **Guild Analytics**: Capability to retrieve guild roster data and activity history.
- **Data Formatting**: Capability to structure raw API responses into readable recruitment reports.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Professional account intelligence and research automation.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Advanced automation for managing complex operational pipelines.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automated data enrichment and intelligence gathering.
