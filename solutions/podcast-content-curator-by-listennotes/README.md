# Podcast Content Curator (Uplizd) - Automated discovery and curation of podcast episodes

## Summary
The Podcast Content Curator is an intelligent Uplizd workflow that automates the discovery, filtering, and organization of podcast episodes based on specific topics, guests, or industry trends. By leveraging the ListenNotes API via the Composio Toolset, this solution enables content marketers and researchers to maintain a consistent stream of high-quality audio insights, reducing manual search time and ensuring your audience stays informed with the latest relevant content.

---

## Demo
![Podcast Content Curator workflow dashboard showing automated episode discovery and filtering](image.png)
**Alt text (SEO-ready):** Podcast Content Curator dashboard showing automated episode discovery, filtering, and curation workflow on Uplizd using ListenNotes and AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6223e9QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVHjaY2BgYPjPABgGgHggGgAAGMYBwD8GgHggGgAAGMYBAA0uAAGb640aAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/c8b15324-ed54-5da8-9642-b5e94b114b87)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content curation, podcasting, listennotes, ai workflow, research automation, media intelligence, composio, content strategy
- This solution streamlines the media monitoring process by connecting AI-driven curation logic directly to your content distribution pipeline.

---

## Who is this for?
This solution is designed for professionals who need to scale their content research and curation efforts without manual overhead.

- **Content Marketers**
    - Automate the discovery of trending industry topics to fuel blog posts and social media calendars.
- **Podcast Producers**
    - Identify competitor episode themes and guest opportunities to refine your own content strategy.
- **Industry Researchers**
    - Aggregate expert insights from niche podcasts into a centralized database for deeper analysis.
- **Newsletter Curators**
    - Automatically source high-value audio content to include in weekly subscriber digests.

---

## Features
- **Automated Episode Discovery**
    - Uses the ListenNotes API to search for episodes based on complex keyword queries and industry-specific tags.
- **Intelligent Relevance Filtering**
    - Employs AI to evaluate episode descriptions and transcripts, ensuring only high-quality, relevant content is curated.
- **Composio-Powered Integration**
    - Seamlessly connects the Uplizd agent to the ListenNotes ecosystem for real-time data retrieval.
- **Customizable Curation Logic**
    - Easily adjust parameters like episode length, publication date, and language to match your specific audience needs.
- **Structured Output Generation**
    - Automatically formats curated episode metadata into ready-to-use lists for your CMS or project management tools.

---

## Use Cases
**Content Strategy Development**
- Automatically pull the latest episodes from top-tier industry podcasts to identify emerging trends.
- Generate a weekly summary of "must-listen" episodes to inform your editorial calendar.

**Competitive Intelligence**
- Monitor competitor podcast appearances and discussion topics to identify gaps in your own content coverage.
- Track mentions of specific industry keywords across thousands of podcast episodes in real-time.

**Audience Engagement**
- Curate personalized podcast recommendations for your newsletter subscribers based on their interests.
- Simplify the process of finding guest experts by identifying frequent speakers in your niche.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Podcast Content Curator template from the solution library.
3. Connect your ListenNotes API credentials within the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your search criteria, such as "Find recent episodes about AI in healthcare."
- **Agent**: Processes the request and determines the necessary search parameters for the toolset.
- **Composio Toolset**: Executes the API calls to ListenNotes to fetch and filter episode data.
- **Chat Output**: Returns the curated list of episodes with links and summaries to the user.

### 3) Run the Flow
Use the Playground to test your curation logic with prompts like:
- `Find the top 5 most popular episodes about 'Generative AI' published in the last week.`
- `Search for podcasts featuring interviews with experts in 'Sustainable Energy' under 30 minutes.`
- `Curate a list of recent episodes discussing 'Remote Work Trends' from tech-focused podcasts.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your curation strategy.
- Focus on extracting intent from natural language queries.
- Map user-defined constraints (date, length, topic) to API parameters.
- Summarize and format the final list of curated episodes for readability.

### 2) Composio Toolset Node
- Requires a valid ListenNotes API key configured within the Composio platform.
- Ensure the connection scope allows for search and metadata retrieval permissions.

### 3) Tool Availability
- **Search Episodes**: Capability to query the ListenNotes database by keyword.
- **Get Episode Metadata**: Capability to retrieve detailed info like duration, audio link, and show description.
- **Filter/Sort**: Capability to organize results by relevance, date, or popularity.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Automate the collection of firmographic data for lead enrichment.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze video content trends to optimize your multimedia strategy.
- [Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) — Streamline the multi-channel publishing of your curated media assets.
