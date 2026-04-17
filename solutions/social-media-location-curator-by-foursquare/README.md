# Social Media Location Curator (Uplizd) - Automate location-based content discovery and social curation

## Summary
The Social Media Location Curator is an intelligent Uplizd workflow that leverages Foursquare’s location intelligence to identify trending venues and curate visual content for social media campaigns. By automating the discovery of high-traffic locations and gathering relevant metadata, marketing teams can maintain a consistent pipeline of location-based assets, ensuring their social presence remains relevant, timely, and hyper-local.

---

## Demo
![Social Media Location Curator workflow interface showing Foursquare integration nodes and content curation logic](image.png)
**Alt text (SEO-ready):** Social Media Location Curator Uplizd workflow, Foursquare location discovery, automated social media content curation, and marketing campaign asset management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/91c7cf60-e242-561f-b113-7d9e6d431725)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** social media, location intelligence, foursquare, content curation, marketing automation, trend analysis, digital assets, composio
- This solution bridges the gap between physical location data and digital content strategy to streamline local marketing efforts.

---

## Who is this for?
This solution is designed for marketing professionals and social media managers who need to maintain a steady stream of location-relevant content.

- **Social Media Manager**
  - Automates the identification of trending hotspots to feature in brand stories.
- **Local Marketing Specialist**
  - Ensures regional campaigns are populated with verified, high-value location data.
- **Content Strategist**
  - Reduces manual research time by programmatically sourcing venue details and visual context.
- **Brand Partnership Lead**
  - Simplifies the process of scouting potential partner locations for collaborative social events.

---

## Features
- **Automated Venue Discovery**
  - Uses the Foursquare API to pull real-time data on trending and highly-rated locations in specified regions.
- **Intelligent Metadata Extraction**
  - Automatically parses venue categories, ratings, and user tips to provide context for social posts.
- **Composio-Powered Orchestration**
  - Seamlessly connects Foursquare data to your existing marketing stack via the Composio Toolset.
- **Campaign-Ready Formatting**
  - Transforms raw location data into structured, ready-to-publish social media captions and asset briefs.
- **Real-Time Trend Monitoring**
  - Filters location results based on current popularity metrics to ensure content remains ahead of the curve.

---

## Use Cases
**Regional Campaign Planning**
- Automatically generate a list of top-rated cafes or parks for local influencer outreach.
- Sync venue details directly into your content calendar to streamline regional campaign scheduling.

**Event & Pop-up Scouting**
- Identify high-traffic areas for potential brand pop-up events based on historical foot traffic data.
- Gather venue contact information and social handles to facilitate rapid partnership inquiries.

**Hyper-Local Content Creation**
- Curate "Best of the City" lists by pulling verified venue descriptions and geographic coordinates.
- Generate location-tagged social media captions that highlight trending spots in your target demographic's area.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Social Media Location Curator.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your Foursquare account within the Composio integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Define the target city, venue category, and campaign focus.
- **Agent**: Processes the request and determines the optimal search parameters for Foursquare.
- **Composio Toolset**: Executes the location queries and retrieves structured venue data.
- **Chat Output**: Displays the curated list of locations and suggested social media copy.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Find the top 5 trending coffee shops in downtown Austin for our weekend social campaign.`
- `List the most popular parks in Seattle and provide a brief description for an Instagram post.`
- `Identify trending fitness centers in Miami that have high user ratings for a local wellness partnership.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your location research assistant, interpreting user intent and mapping it to Foursquare search queries.
- Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5).
- Instruct the agent to prioritize "trending" and "high-rated" filters.
- Ensure the agent maintains a professional, brand-aligned tone for all generated social copy.

### 2) Composio Toolset Node
- Provide your Foursquare API credentials within the Composio dashboard.
- Set the connection scope to allow read-only access to venue search and details endpoints.

### 3) Tool Availability
- **Venue Search**: Discovery of locations based on geographic coordinates or city names.
- **Venue Details**: Retrieval of specific metadata including ratings, tips, and categories.
- **Trend Analysis**: Access to popularity metrics to filter for high-traffic locations.

---

## Related Solutions
- [../you-tube-content-performance-optimizer-by-youtube/README.md](../you-tube-content-performance-optimizer-by-youtube/README.md) - Optimize video content performance based on audience engagement metrics.
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and intelligence for targeted sales outreach.
- [../whats-app-lead-nurturing-agent-by-spoki/README.md](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automate lead nurturing sequences via WhatsApp for better conversion.
