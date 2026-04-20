# Travel Itinerary Builder (Uplizd) - Automated personalized travel planning and local recommendations

## Summary
The Travel Itinerary Builder is an intelligent Uplizd workflow that automates the creation of custom travel schedules by integrating real-time location data and local insights. By leveraging the Foursquare API via the Composio Toolset, this solution transforms broad travel preferences into structured, actionable itineraries, significantly reducing planning time and ensuring high-quality, data-driven recommendations for travelers and travel agencies.

---

## Demo
![Travel Itinerary Builder workflow showing Foursquare integration and itinerary generation](image.png)
**Alt text (SEO-ready):** Travel Itinerary Builder (Uplizd) workflow for automated trip planning using Foursquare API and AI-driven itinerary generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c81df53c-68a7-56c5-a45e-9812ac28f7e0)

---

## Category
**Primary category:** Operations  
**Secondary tags:** travel, foursquare, itinerary, ai workflow, planning, automation, location intelligence, composio  
This solution streamlines the travel planning lifecycle by connecting AI agents directly to location-based discovery services.

---

## Who is this for?
This solution is designed for professionals and platforms looking to automate high-touch travel planning services.

* **Travel Agents**
    * Drastically reduce the time spent researching local venues and drafting daily schedules for clients.
* **Concierge Services**
    * Provide instant, hyper-personalized recommendations based on specific user interests and location constraints.
* **Travel Bloggers**
    * Quickly generate structured itinerary templates for readers based on trending locations and top-rated spots.
* **Event Planners**
    * Efficiently map out local experiences and dining options for corporate retreats or group excursions.

---

## Features
- **Intelligent Venue Discovery**
    Leverages Foursquare's extensive database to find top-rated attractions, restaurants, and hidden gems based on user preferences.
- **Dynamic Itinerary Generation**
    Automatically structures raw location data into a chronological, easy-to-read daily itinerary format.
- **Context-Aware Personalization**
    The Agent interprets specific user constraints—such as budget, interests, and trip duration—to filter and rank recommendations.
- **Real-time Data Integration**
    Uses the Composio Toolset to fetch live venue details, ensuring that the itinerary includes current and relevant information.
- **Seamless Workflow Automation**
    Connects the Chat Input directly to the Agent and Foursquare tools, enabling a hands-off, end-to-end planning experience.

---

## Use Cases
**Personalized Trip Planning**
* Generate a 3-day weekend itinerary for a family visiting a new city with a focus on kid-friendly parks and museums.
* Create a culinary-focused travel plan for a food enthusiast looking for the top-rated local eateries in a specific neighborhood.

**Corporate Travel Logistics**
* Build a structured schedule for business travelers that balances meeting times with recommended nearby coffee shops and quiet workspaces.
* Organize group outing itineraries that include team-building activities and group-friendly dining venues.

**Travel Agency Efficiency**
* Automate the initial draft of client itineraries, allowing agents to focus on final refinements and high-value customer interactions.
* Rapidly prototype multiple travel options for clients to choose from, increasing conversion rates through faster response times.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Travel Itinerary Builder template from the solution library.
3. Connect your Foursquare API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives the user's destination, duration, and specific interests.
* **Agent**: Processes the request and orchestrates the search for relevant venues.
* **Composio Toolset**: Executes the Foursquare API queries to fetch venue data.
* **Chat Output**: Delivers the final, formatted itinerary to the user.

### 3) Run the Flow
Open the Playground and test the flow with these prompts:
* `Create a 3-day itinerary for a trip to Tokyo focused on sushi restaurants and historical temples.`
* `I am visiting Paris for 2 days; suggest a budget-friendly itinerary with art galleries and parks.`
* `Build a business-friendly itinerary for a 24-hour stay in New York City near the financial district.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a travel consultant that translates natural language requests into structured location queries.
* Maintain a professional and helpful tone.
* Prioritize venues with high ratings and relevant tags.
* Ensure the output is formatted as a clear, day-by-day itinerary.

### 2) Composio Toolset Node
* Requires a valid Foursquare API key configured within the Composio platform.
* Scope: Access to venue search, details, and category filtering.

### 3) Tool Availability
* **Venue Search**: Find locations based on query and location coordinates.
* **Venue Details**: Retrieve specific information like ratings, address, and category.
* **Category Filtering**: Refine search results by specific interests (e.g., "museum," "restaurant").

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into business accounts.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex operational tasks across platforms.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Collect and verify data for professional account profiles.
