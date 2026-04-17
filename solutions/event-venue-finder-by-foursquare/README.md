# Event Venue Finder (Uplizd) - Intelligent location discovery and event planning

## Summary
The Event Venue Finder (Uplizd) is an AI-powered workflow that automates the discovery and selection of event spaces by integrating real-time location data from Foursquare. This solution enables event planners and operations teams to streamline site selection, ensuring venue requirements match specific event needs while reducing manual research time and improving pipeline velocity for event logistics.

---

## Demo
![Event Venue Finder workflow showing Foursquare integration and venue search logic](image.png)
**Alt text (SEO-ready):** Event Venue Finder by Foursquare on Uplizd, an AI-powered workflow for automated venue discovery, location-based search, and event planning integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3cc9ca53-d450-5ad6-aeca-75fb100f9428)

---

## Category
**Primary category:** Operations
**Secondary tags:** foursquare, event planning, venue search, location intelligence, logistics, ai workflow, composio, automation.
This solution bridges the gap between logistical requirements and real-world venue data to simplify the event planning lifecycle.

---

## Who is this for?
This solution is designed for professionals managing complex event logistics who need to source venues rapidly and accurately.

* **Event Planner**
    * Automates the tedious process of searching for venues that meet specific capacity and amenity criteria.
* **Operations Manager**
    * Ensures consistent data collection for site selection, maintaining a single source of truth for event logistics.
* **Corporate Marketing Lead**
    * Accelerates the venue scouting phase to ensure event timelines remain on track for high-priority launches.
* **Office Manager**
    * Simplifies the coordination of internal company gatherings by instantly surfacing top-rated local venues.

---

## Features
- **Real-time Venue Discovery**
  Leverages Foursquare’s extensive database to fetch up-to-date venue information based on specific geographic coordinates.
- **Requirement-Based Filtering**
  Uses AI to parse natural language requests and filter venues by category, rating, and proximity.
- **Composio-Powered Integration**
  Seamlessly connects the Uplizd agent to Foursquare APIs, ensuring secure and authenticated data retrieval.
- **Automated Data Formatting**
  Structures venue results into clear, actionable summaries for immediate review and decision-making.
- **Workflow Scalability**
  Easily adapts to different event types, from intimate team workshops to large-scale corporate conferences.

---

## Use Cases
**Corporate Event Planning**
* Sourcing off-site venues for quarterly team-building activities based on office proximity.
* Filtering for venues that offer specific amenities like high-speed Wi-Fi and presentation equipment.

**Logistics & Operations**
* Quickly generating a shortlist of potential event spaces for multi-city roadshows.
* Comparing venue ratings and popularity metrics to ensure high-quality attendee experiences.

**Administrative Support**
* Automating the search for local meeting spaces for visiting executives or clients.
* Compiling venue contact details and location data into a centralized report for management approval.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the **Event Venue Finder**.
2. Click "Import" to add the workflow to your workspace.
3. Configure your Foursquare API credentials within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Accepts the user's event requirements, location, and venue preferences.
* **Agent**: Processes the request and determines the necessary search parameters for the Foursquare API.
* **Composio Toolset**: Executes the search queries against the Foursquare platform to retrieve venue data.
* **Chat Output**: Delivers a curated list of venues with relevant details back to the user.

### 3) Run the Flow
Open the Playground and test the flow with prompts such as:
* `Find me top-rated conference venues in downtown Chicago with high-speed internet.`
* `Search for quiet cafes in San Francisco suitable for a team meeting of 10 people.`
* `List 5 popular event spaces in Austin that are open late and have good reviews.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent interface between user intent and the Foursquare API.
* Instruct the agent to prioritize high-rated venues.
* Maintain a professional and helpful tone for event planning.
* Ensure the agent asks for missing criteria (e.g., capacity, budget) if the initial prompt is vague.

### 2) Composio Toolset Node
* Provide your Foursquare API key to enable location data access.
* Ensure the connection scope is set to allow read access to venue search and details endpoints.

### 3) Tool Availability
* **Venue Search**: Capability to query venues by location, category, and keyword.
* **Venue Details**: Capability to fetch specific metadata like ratings, photos, and operating hours.
* **Geocoding**: Capability to resolve natural language locations into precise coordinates.

---

## Related Solutions
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Streamline account intelligence and lead gathering.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Manage and automate complex operational workflows.
* [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Coordinate team collaboration and workshop logistics.
