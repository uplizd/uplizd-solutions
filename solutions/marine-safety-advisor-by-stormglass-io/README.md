# Marine Safety Advisor (Uplizd) - Automated marine weather and vessel safety risk assessment

## Summary
The Marine Safety Advisor is an intelligent Uplizd workflow that integrates real-time maritime weather data from Stormglass.io to provide automated safety assessments for vessel operations. By analyzing wave heights, wind speeds, and visibility metrics, this solution helps maritime operators and fleet managers mitigate risks, ensure regulatory compliance, and optimize voyage planning through proactive, data-driven decision-making.

---

## Demo
![Marine Safety Advisor dashboard showing real-time weather risk assessment and vessel safety alerts](image.png)
**Alt text (SEO-ready):** Marine Safety Advisor Uplizd workflow dashboard displaying real-time maritime weather risk analysis, vessel safety alerts, and Stormglass.io integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/146ec980-c7e0-5ca6-baf0-ccc250a7ba8e)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** marine safety, weather monitoring, stormglass, vessel operations, risk management, maritime logistics, ai workflow, composio
- This solution bridges the gap between raw meteorological data and actionable maritime safety protocols for fleet operators.

---

## Who is this for?
This solution is designed for maritime professionals who require real-time situational awareness to ensure crew safety and vessel integrity.

- **Fleet Managers**
    - Monitor global vessel positions against incoming weather patterns to prevent operational delays.
- **Marine Safety Officers**
    - Automate the generation of safety reports based on threshold breaches for wind and wave conditions.
- **Logistics Coordinators**
    - Optimize route planning by identifying high-risk weather zones before departure.
- **Vessel Captains**
    - Receive instant, AI-synthesized briefings on local sea state conditions to inform navigation decisions.

---

## Features
- **Real-time Weather Integration**
    - Seamlessly pulls live meteorological data from Stormglass.io to provide up-to-the-minute environmental insights.
- **Automated Risk Thresholds**
    - Configurable safety parameters that trigger alerts when wave height or wind speed exceeds vessel-specific limits.
- **Composio-Powered Connectivity**
    - Leverages the Composio Toolset to bridge weather data with internal communication and logging systems.
- **Proactive Alerting System**
    - Delivers automated notifications to relevant stakeholders when hazardous conditions are detected on planned routes.
- **Historical Data Analysis**
    - Maintains a log of weather-related safety assessments for post-voyage review and compliance auditing.

---

## Use Cases
**Voyage Risk Mitigation**
- Automatically check weather conditions for a specific coordinate set 24 hours prior to vessel arrival.
- Flag high-risk zones that require route adjustments to avoid severe storm cells.

**Operational Compliance**
- Generate automated safety logs whenever a vessel enters a region with restricted weather conditions.
- Maintain a digital audit trail of weather-related decision-making for insurance and regulatory reporting.

**Fleet Performance Optimization**
- Compare planned transit times against weather-adjusted estimates to improve arrival accuracy.
- Identify recurring weather-related delays on specific shipping lanes to refine future scheduling.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Solution."
2. Import the Marine Safety Advisor template file provided in this repository.
3. Configure your Stormglass.io API credentials within the environment variables.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives vessel coordinates, timestamps, and specific safety queries.
- **Agent**: Processes environmental data and evaluates safety risks against defined thresholds.
- **Composio Toolset**: Executes API calls to Stormglass.io to fetch precise weather metrics.
- **Chat Output**: Returns a concise safety assessment and recommended actions to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Check the safety risk for vessel at 34.05, -118.24 for the next 6 hours.`
- `Are there any gale warnings for the current route of vessel V-992?`
- `Summarize the wave height trends for the upcoming 12 hours at these coordinates.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized maritime safety analyst.
- Use a model with strong reasoning capabilities to interpret complex weather data.
- Instruct the agent to prioritize safety-critical information in all summaries.
- Ensure the agent maintains a professional, objective tone suitable for maritime operations.

### 2) Composio Toolset Node
- Provide a valid Stormglass.io API key to enable weather data retrieval.
- Set the connection scope to include read access for marine weather endpoints.

### 3) Tool Availability
- **Weather Fetcher**: Retrieves wave, wind, and visibility data.
- **Coordinate Parser**: Converts user input into valid API request parameters.
- **Alert Generator**: Formats risk notifications for external communication channels.

---

## Related Solutions
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) - Proactive monitoring for organizational safety and risk mitigation.
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Automated tracking of compliance and health status for business operations.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Real-time oversight for maintaining operational efficiency and system integrity.
