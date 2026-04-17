# Local Business Scout (Uplizd) - Automated discovery and analysis for local market expansion

## Summary
The Local Business Scout workflow leverages the Foursquare API to identify, filter, and analyze local businesses, enabling teams to pinpoint expansion opportunities with precision. By automating the discovery process, this Uplizd AI workflow provides a single source of truth for market intelligence, significantly increasing pipeline velocity and data hygiene for regional growth strategies.

---

## Demo
![Local Business Scout workflow interface showing Foursquare API integration and business data analysis](image.png)
**Alt text (SEO-ready):** Local Business Scout Uplizd workflow showing Foursquare API business discovery and automated market analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/4bd70d02-4214-5d3e-9450-7ca3f12d9dc6)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** local business, foursquare, market intelligence, lead generation, expansion, data sync, composio, ai workflow
- This solution bridges the gap between raw location data and actionable sales intelligence for rapid market entry.

---

## Who is this for?
This solution is designed for teams focused on hyper-local growth and competitive intelligence.

- **Sales Development Rep (SDR)**
    - Quickly identify high-potential prospects in new territories to fill the top of the funnel.
- **Market Expansion Manager**
    - Analyze regional business density and category saturation to inform site selection and strategy.
- **Business Analyst**
    - Aggregate real-world location data into structured reports for data-driven decision-making.
- **RevOps Lead**
    - Maintain high-quality, verified business data within the CRM to ensure accurate territory planning.

---

## Features
- **Automated Discovery**
    - Query the Foursquare database in real-time to surface businesses based on location, category, and popularity.
- **Intelligent Filtering**
    - Apply custom logic to narrow down results by rating, price point, or operational status.
- **Composio-Powered Integration**
    - Seamlessly bridge Foursquare data with your CRM or spreadsheet tools for immediate actionability.
- **Data Enrichment**
    - Automatically append metadata such as contact info and venue categories to your prospect lists.
- **Real-time Synchronization**
    - Ensure your expansion pipeline is always updated with the latest venue changes and market shifts.

---

## Use Cases
**Market Expansion Planning**
- Identify high-traffic business clusters in a new city to prioritize sales outreach.
- Compare venue density across multiple zip codes to determine optimal territory coverage.

**Lead Generation & Prospecting**
- Generate a targeted list of local businesses that match specific industry and service criteria.
- Automatically qualify leads based on venue ratings and customer review signals.

**Competitive Intelligence**
- Monitor new business openings in specific sectors to stay ahead of market trends.
- Track competitor presence in key locations to adjust your regional sales strategy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Local Business Scout template from the marketplace.
3. Connect your Foursquare API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your search criteria (e.g., "Find coffee shops in downtown Austin").
*   **Agent**: Processes the intent and formulates queries for the Foursquare API.
*   **Composio Toolset**: Executes the API calls to fetch and parse business data.
*   **Chat Output**: Delivers the structured list of businesses and insights back to the user.

### 3) Run the Flow
Open the Playground and test with these prompts:
`Find all high-rated fitness centers in the 90210 area.`
`List the top 10 restaurants in Chicago that have been opened in the last 6 months.`
`Identify potential retail partners in Seattle that specialize in sustainable goods.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary orchestrator for location-based reasoning.
- Use a model with strong reasoning capabilities to interpret geographic constraints.
- Instruction: "Always prioritize businesses with verified location data and high user ratings."
- Instruction: "Format output as a structured list including name, address, and category."

### 2) Composio Toolset Node
- Provide your Foursquare API key to enable secure access to the venue database.
- Set the connection scope to read-only for venue discovery and metadata retrieval.

### 3) Tool Availability
- **Venue Search**: Capabilities to query by geographic coordinates or city names.
- **Venue Details**: Ability to pull specific metadata like contact info and operating hours.
- **Category Filtering**: Tools to narrow results by specific business types.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact signals.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research for enterprise-level prospecting.
- [Account Expansion Identifier](../account-expansion-identifier-by-crustdata/README.md) - Identify growth opportunities within existing market segments.
