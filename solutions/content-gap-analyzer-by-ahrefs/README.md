# Content Gap Analyzer (Uplizd) - Identify competitor keyword gaps and scale organic traffic

## Summary
The Content Gap Analyzer is an intelligent Uplizd workflow that automates competitive research by cross-referencing your domain against top-performing competitors. By leveraging the Ahrefs API via the Composio Toolset, this solution identifies high-value keyword opportunities where your competitors rank but you do not, enabling content teams to prioritize high-impact topics, improve search engine visibility, and capture untapped organic traffic.

---

## Demo
![Content Gap Analyzer workflow showing Ahrefs data integration and keyword opportunity extraction](image.png)
**Alt text (SEO-ready):** Content Gap Analyzer workflow in Uplizd, showing Ahrefs integration for keyword research, competitor analysis, and SEO content opportunity identification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/52780e0a-4901-5d06-ada8-b15e275d1019)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** content strategy, seo, ahrefs, keyword research, competitive intelligence, organic growth, content marketing, composio  
This solution bridges the gap between raw competitive data and actionable content strategy for modern marketing teams.

---

## Who is this for?
This solution is designed for marketing and SEO professionals who need to turn competitive data into a prioritized content roadmap.

*   **SEO Manager**
    *   Automates the discovery of high-volume, low-competition keywords to improve domain authority.
*   **Content Strategist**
    *   Provides a data-driven foundation for editorial calendars by identifying specific topics missing from the current site.
*   **Growth Marketer**
    *   Accelerates pipeline velocity by targeting the same high-intent search terms that drive competitor conversions.
*   **Digital Agency Lead**
    *   Scales client reporting and strategy development by instantly generating competitive gap reports across multiple domains.

---

## Features
- **Automated Competitor Benchmarking**
    Connect your domain and competitor URLs to instantly pull ranking data and identify overlapping search terms.
- **High-Intent Keyword Discovery**
    Filter results by search volume and keyword difficulty to focus on topics that provide the highest ROI for your brand.
- **Composio-Powered Ahrefs Integration**
    Seamlessly execute complex API queries to Ahrefs without manual data exports or spreadsheet manipulation.
- **Real-Time Opportunity Scoring**
    The agent evaluates keyword relevance and search intent, surfacing only the most actionable content ideas for your team.
- **Streamlined Content Briefing**
    Automatically format identified gaps into actionable insights that can be passed directly to writers or content creators.

---

## Use Cases
**Competitive Content Strategy**
*   Identify "low-hanging fruit" keywords where competitors rank on page 2 but have weak content.
*   Map competitor content pillars to your own site to ensure comprehensive topical coverage.

**SEO Performance Optimization**
*   Analyze keyword gaps for specific product categories to outrank competitors in high-value search segments.
*   Monitor new competitor content releases to quickly identify and respond to emerging keyword gaps.

**Growth & Pipeline Development**
*   Target long-tail keywords that competitors are ignoring to capture high-intent, bottom-of-funnel traffic.
*   Prioritize content production based on the potential traffic lift identified by the gap analysis.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Configure the required API credentials for your Ahrefs account within the Composio integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target domain and competitor URLs from the user.
*   **Agent**: Processes the request, instructs the toolset, and synthesizes the gap data.
*   **Composio Toolset**: Executes the Ahrefs API calls to fetch ranking and keyword data.
*   **Chat Output**: Delivers a structured report of actionable content opportunities.

### 3) Run the Flow
Use the Playground to test the workflow with prompts like:
* `Compare my domain 'example.com' with 'competitor.com' and list the top 10 keyword gaps with high search volume.`
* `Find keywords where 'competitor.com' ranks in the top 3 but my site 'example.com' is not in the top 20.`
* `Generate a content strategy plan based on the keyword gaps identified for the 'SaaS marketing' topic.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an SEO strategist, interpreting raw API data into human-readable recommendations.
*   Role: Senior SEO Strategist.
*   Instruction: Focus on search intent, prioritize keywords with high volume/low difficulty, and maintain a professional, actionable tone.
*   Constraint: Always cite the source competitor and the specific keyword metrics when providing recommendations.

### 2) Composio Toolset Node
*   API Key: Ensure your Ahrefs API key is active in the Composio dashboard.
*   Connection Scope: Grant read-only access to site explorer and keyword explorer endpoints.

### 3) Tool Availability
*   `ahrefs_get_organic_keywords`: Fetches ranking data for specified domains.
*   `ahrefs_get_keyword_metrics`: Retrieves search volume and difficulty scores.
*   `ahrefs_compare_domains`: Performs the core gap analysis between two or more properties.

---

## Related Solutions
*   [AB Test Optimizer by Mixpanel](../ab-test-optimizer-by-mixpanel/README.md) - Optimize conversion rates through data-driven testing.
*   [YouTube Audience Research Agent by YouTube](../you-tube-audience-research-agent-by-youtube/README.md) - Analyze video content gaps and audience interests.
*   [Account Intelligence Reporter by Leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather competitive account insights for sales teams.
