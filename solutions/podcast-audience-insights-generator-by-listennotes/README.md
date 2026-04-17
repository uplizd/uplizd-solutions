# Podcast Audience Insights Generator (Uplizd) - AI-driven listener demographics and content analytics

## Summary
The Podcast Audience Insights Generator leverages the ListenNotes API to extract deep listener demographics, content trends, and engagement metrics for any podcast. By automating the research process, this Uplizd workflow enables marketers and creators to make data-backed advertising decisions, identify high-value sponsorship opportunities, and optimize content strategy with a single source of truth.

---

## Demo
![Podcast Audience Insights Generator workflow dashboard showing demographic data and listener trends](image.png)
**Alt text (SEO-ready):** Podcast Audience Insights Generator workflow dashboard showing demographic data, listener trends, Uplizd AI automation, and ListenNotes API integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIGFz0k5K525QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK0cAAAAkSURBVHja7cEBAQAAAIIQDj+7uQkAAAAAAAAAAAAAAADw1wAF+AABjV0J5QAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/c6696669-8d8e-53a0-bd45-5baf96852abe)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** podcast, audience insights, listennotes, advertising, content strategy, data analytics, ai workflow, sponsorship

This solution streamlines the acquisition of podcast intelligence, bridging the gap between raw audio data and actionable marketing insights.

---

## Who is this for?
This workflow is designed for professionals who need to decode podcast performance and audience behavior at scale.

- **Podcast Marketer**
    - Quickly identify podcasts that align with specific brand demographics to maximize ad spend ROI.
- **Sponsorship Manager**
    - Access verified listener data to negotiate better rates and validate partnership opportunities.
- **Content Strategist**
    - Analyze competitor podcast themes and listener feedback to refine production and growth strategies.
- **Media Buyer**
    - Automate the research phase of media planning by pulling real-time insights across thousands of shows.

---

## Features
- **Automated Audience Profiling**
    - Instantly generate listener demographic summaries using integrated ListenNotes data.
- **Trend Analysis**
    - Identify rising content themes and popular topics within specific podcast niches.
- **Sponsorship Intelligence**
    - Evaluate show reach and engagement metrics to prioritize high-performing advertising channels.
- **Real-time Data Sync**
    - Connects directly to the Composio Toolset to fetch the latest podcast metadata without manual scraping.
- **Actionable Reporting**
    - Outputs structured insights ready for integration into CRM or media planning spreadsheets.

---

## Use Cases
**Media Planning & Buying**
- Automate the vetting process for potential podcast ad placements by comparing listener reach across multiple shows.
- Generate comparative reports for client pitches to justify advertising budget allocation based on data-driven audience segments.

**Content & Growth Strategy**
- Research competitor podcast performance to identify content gaps and emerging listener interests.
- Track the impact of specific guest appearances or episode topics on overall show engagement metrics.

**Sponsorship Outreach**
- Build targeted outreach lists for brands by filtering podcasts based on specific audience interests and show categories.
- Create professional "one-pagers" for sponsorship decks using automatically generated audience insights.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Podcast Audience Insights template file.
3. Connect your ListenNotes API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the podcast name or RSS feed URL from the user.
- **Agent**: Processes the request and determines which data points to extract.
- **Composio Toolset**: Executes API calls to ListenNotes to retrieve show metadata and audience signals.
- **Chat Output**: Formats the retrieved data into a concise, readable insights report.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Analyze the audience demographics for the 'Huberman Lab' podcast.`
- `Find top-rated podcasts in the 'Technology' category and summarize their listener profiles.`
- `Compare the content themes of these two podcasts: [Podcast A] and [Podcast B].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized research analyst capable of interpreting API responses into human-readable marketing insights.
- Instruct the agent to prioritize demographic data and engagement trends.
- Set the tone to be professional, analytical, and objective.
- Ensure the agent provides actionable recommendations based on the retrieved metrics.

### 2) Composio Toolset Node
- Requires a valid ListenNotes API key configured within your Composio account.
- Scope should be set to allow read-only access to podcast metadata and search endpoints.

### 3) Tool Availability
- `listennotes_search`: For locating specific podcasts by name or category.
- `listennotes_get_metadata`: For fetching detailed show statistics and audience signals.
- `listennotes_get_episodes`: For analyzing recent content and listener feedback trends.

---

## Related Solutions
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) - Analyze video content performance and viewer demographics.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather company-level insights for B2B sales outreach.
- [Affiliate Program Analytics Agent](../affiliate-program-analytics-agent-by-tapfiliate/README.md) - Track and optimize affiliate marketing performance data.
