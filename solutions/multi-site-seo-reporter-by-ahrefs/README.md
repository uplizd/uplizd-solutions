# Multi-Site SEO Reporter (Uplizd) - Automated cross-domain search performance monitoring

## Summary
The Multi-Site SEO Reporter is an automated Uplizd AI workflow designed to aggregate, analyze, and report on search performance metrics across multiple websites. By leveraging the Ahrefs integration via the Composio Toolset, this solution provides marketing teams and SEO specialists with a single source of truth for domain health, keyword rankings, and backlink velocity, significantly reducing manual data collection time and accelerating pipeline velocity for content optimization.

---

## Demo
![Multi-Site SEO Reporter dashboard showing keyword rankings and backlink health across multiple domains](image.png)
**Alt text (SEO-ready):** Multi-Site SEO Reporter dashboard showing keyword rankings and backlink health across multiple domains for Uplizd automated SEO workflows and Ahrefs data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/32a0c44b-b8cc-5b45-90e8-b8cb7aa883cc)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** seo, ahrefs, content strategy, data reporting, site audit, search performance, marketing automation, composio
- This solution streamlines technical SEO reporting by automating data retrieval from Ahrefs to provide actionable insights for multi-site portfolios.

---

## Who is this for?
This solution is built for professionals managing complex web portfolios who need to maintain search visibility and content performance.

- **SEO Specialist**
    - Automates recurring site audits and keyword ranking reports across dozens of client domains.
- **Content Marketing Manager**
    - Identifies high-performing content clusters and backlink opportunities to inform editorial calendars.
- **Digital Agency Owner**
    - Delivers consistent, data-backed performance reports to clients without manual spreadsheet work.
- **Growth Marketer**
    - Monitors search visibility trends to pivot strategies based on real-time search engine performance data.

---

## Features
- **Automated Domain Audits**
    - Triggers comprehensive site health checks across multiple domains to identify crawl errors and broken links.
- **Keyword Performance Tracking**
    - Aggregates ranking data for target keywords, highlighting position changes and search volume trends.
- **Backlink Velocity Analysis**
    - Monitors new and lost backlinks to maintain domain authority and identify potential link-building opportunities.
- **Cross-Platform Integration**
    - Uses the Composio Toolset to securely connect with Ahrefs and push data into your preferred reporting pipeline.
- **Customizable Reporting**
    - Generates summarized insights tailored to specific stakeholder needs, from technical health to high-level traffic growth.

---

## Use Cases
**Search Performance Monitoring**
- Automatically generate weekly ranking reports for top-tier keywords across all managed domains.
- Alert the team when a core landing page experiences a significant drop in organic search visibility.

**Technical SEO Hygiene**
- Run monthly site-wide audits to detect and resolve 404 errors and redirect chains.
- Monitor schema markup implementation status across different CMS environments.

**Competitor & Content Intelligence**
- Track backlink acquisition rates compared to top industry competitors.
- Identify content gaps by analyzing keyword opportunities that competitors currently rank for but you do not.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Ahrefs account within the Composio connection prompt.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target domain list and reporting frequency parameters.
- **Agent**: Processes SEO queries and interprets Ahrefs data into human-readable summaries.
- **Composio Toolset**: Executes API calls to Ahrefs to fetch real-time site metrics.
- **Chat Output**: Delivers the final SEO report directly to your dashboard or notification channel.

### 3) Run the Flow
Use the Playground to test your reporting capabilities:
- `Generate a site health summary for example-site.com and identify the top 5 crawl errors.`
- `Compare the keyword ranking performance of our blog against our top 3 competitors.`
- `Create a monthly backlink growth report for all domains in our portfolio.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your SEO analyst, synthesizing raw API data into strategic insights.
- Set the system prompt to prioritize "Actionable SEO Insights."
- Configure the temperature to 0.2 for precise, data-heavy reporting.
- Ensure the agent has access to the full context of the previous 30 days of site data.

### 2) Composio Toolset Node
- Provide your Ahrefs API key within the Composio configuration.
- Scope the connection to "Read-Only" for site audit and ranking data to ensure security.

### 3) Tool Availability
- **Site Explorer**: For domain-level health and backlink analysis.
- **Keywords Explorer**: For tracking ranking positions and search volume.
- **Rank Tracker**: For historical performance monitoring and trend analysis.

---

## Related Solutions
- [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Analyze video search performance and engagement metrics.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Track visitor intent and account-level search behavior.
- [Affiliate Performance Monitor](../affiliate-performance-monitor-by-tapfiliate/README.md) - Monitor traffic and conversion metrics for affiliate programs.
