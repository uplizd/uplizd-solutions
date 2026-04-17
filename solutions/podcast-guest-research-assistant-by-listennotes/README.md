# Podcast Guest Research Assistant (Uplizd) - Streamline guest vetting and background intelligence

## Summary
The Podcast Guest Research Assistant automates the discovery and vetting process for potential podcast guests by leveraging the ListenNotes API to aggregate professional histories and previous media appearances. This Uplizd AI workflow eliminates manual search fatigue, providing producers and content creators with a single source of truth for guest background data, ensuring higher quality interviews and improved pipeline velocity for content production.

---

## Demo
![Podcast Guest Research Assistant workflow showing ListenNotes API integration for guest vetting](image.png)
**Alt text (SEO-ready):** Podcast Guest Research Assistant workflow using Uplizd and ListenNotes API for automated guest vetting and background intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/674676e7-f972-5f55-bd0f-257320b9ad95)

---

## Category
**Primary category:** Content Operations  
**Secondary tags:** podcasting, guest research, listennotes, media intelligence, content production, ai workflow, research automation, composio  
This solution bridges the gap between raw data and editorial readiness by automating the retrieval of guest credentials and media history.

---

## Who is this for?
This solution is designed for media professionals and content teams looking to optimize their guest acquisition and preparation workflows.

- **Podcast Producers**
    - Dramatically reduce time spent manually verifying guest credentials and past media appearances.
- **Content Strategists**
    - Identify high-authority guests by analyzing their previous podcast presence and topical expertise.
- **Talent Managers**
    - Maintain a consistent vetting standard across all potential interviewees to ensure show quality.
- **Media Researchers**
    - Instantly generate comprehensive briefing documents based on real-time data from the ListenNotes index.

---

## Features
- **Automated Guest Discovery**
    - Quickly query the ListenNotes database to find relevant professional profiles and contact signals.
- **Cross-Platform Appearance History**
    - Retrieve a complete list of previous podcast appearances to assess a guest's speaking experience and style.
- **Intelligent Briefing Generation**
    - Synthesize raw API data into structured summaries that prepare hosts for high-impact interviews.
- **Composio-Powered Integration**
    - Utilize the Composio Toolset to securely connect the Uplizd agent to the ListenNotes API ecosystem.
- **Real-Time Data Sync**
    - Ensure your research is based on the most current episode data, preventing outdated guest information.

---

## Use Cases
**Guest Vetting & Selection**
- Verify a potential guest's industry authority by cross-referencing their appearance history across multiple shows.
- Filter prospective guests based on specific keywords or topics discussed in their previous podcast interviews.

**Show Preparation & Briefing**
- Generate a "cheat sheet" of talking points derived from a guest's most popular or recent podcast episodes.
- Compile a list of unique questions based on gaps in a guest's previous media coverage.

**Content Strategy & Outreach**
- Identify trending experts in a specific niche to reach out for upcoming interview slots.
- Track the podcast footprint of competitors' guests to uncover new talent acquisition opportunities.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Podcast Guest Research Assistant template from the solution library.
3. Connect your ListenNotes API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts the guest's name or professional profile URL.
- **Agent**: Processes the request and determines the necessary search parameters for the API.
- **Composio Toolset**: Executes the search queries against the ListenNotes API to fetch guest data.
- **Chat Output**: Returns a formatted report containing the guest's background and appearance history.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Research the podcast appearance history for [Guest Name] and summarize their main areas of expertise.`
- `Find 5 potential podcast guests who have discussed 'AI in Marketing' in the last 6 months.`
- `Create a briefing document for [Guest Name] based on their recent appearances on top-rated tech podcasts.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research analyst, parsing API responses into human-readable insights.
- Instruct the agent to prioritize recent appearances over legacy content.
- Configure the agent to highlight specific topics of interest defined by the user.
- Set the output format to a structured briefing template for consistency.

### 2) Composio Toolset Node
- Provide your ListenNotes API key within the Composio configuration.
- Set the connection scope to allow read-only access to podcast and guest metadata.

### 3) Tool Availability
- **Podcast Search**: Query episodes by keyword, guest, or host.
- **Guest Profile Retrieval**: Fetch detailed professional summaries and appearance lists.
- **Metadata Extraction**: Parse episode durations, release dates, and show ratings.

---

## Related Solutions
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze viewer trends and content performance on YouTube.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gather deep intelligence on business accounts and prospects.
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) — Monitor research influence and academic guest credentials.
