# Market Research Assistant (Uplizd) - Automate deep-dive industry and competitor intelligence

## Summary
The Market Research Assistant is an intelligent Uplizd workflow designed to aggregate, analyze, and synthesize complex market data into actionable intelligence reports. By leveraging the Composio Toolset to query real-time web and database sources, this solution enables RevOps and strategy teams to maintain a single source of truth for competitor positioning, industry trends, and account-level insights, significantly reducing manual research time.

---

## Demo
![Market Research Assistant workflow showing automated data retrieval and report generation](image.png)
**Alt text (SEO-ready):** Market Research Assistant (Uplizd) workflow for automated competitor intelligence, industry trend analysis, and data-driven market reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3f7ef63f-d03b-5b2b-9586-66d7bf938c2b)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** research, competitive analysis, data synthesis, business strategy, ai workflow, composio, market trends, intelligence reporting
- This solution streamlines the collection and analysis of external market signals to provide high-fidelity insights for strategic decision-making.

---

## Who is this for?
This assistant is designed for professionals who need to synthesize vast amounts of external information into clear, strategic narratives.

- **Market Researchers**
    - Automate the collection of competitor news and financial reports to focus on high-level synthesis.
- **Sales Strategy Managers**
    - Quickly generate account-specific intelligence packets to improve win rates during the discovery phase.
- **Product Marketing Leads**
    - Monitor industry shifts and competitor feature launches to refine positioning and messaging.
- **Business Development Executives**
    - Identify new market opportunities and potential partnership targets through automated trend scanning.

---

## Features
- **Automated Data Aggregation**
  Connects to diverse web sources and databases to pull the latest industry news and company updates in real-time.
- **Intelligent Synthesis**
  Uses advanced LLM reasoning to filter out noise and extract key takeaways relevant to your specific business context.
- **Composio Toolset Integration**
  Seamlessly bridges the gap between research tools and your workflow, ensuring data is retrieved securely and efficiently.
- **Customizable Report Formatting**
  Generates structured outputs tailored to your internal standards, whether for executive summaries or deep-dive dossiers.
- **Scalable Research Pipelines**
  Handles multiple research requests concurrently, allowing teams to scale intelligence gathering without increasing headcount.

---

## Use Cases
**Competitive Intelligence**
- Monitor competitor press releases and funding announcements to update internal battlecards.
- Analyze competitor product updates to identify gaps in your own feature set.

**Market Trend Analysis**
- Track emerging technologies and industry shifts to inform long-term product roadmaps.
- Aggregate sector-specific news to prepare quarterly market health reports for stakeholders.

**Account-Level Research**
- Compile comprehensive background reports on target accounts prior to high-stakes sales meetings.
- Identify recent leadership changes and strategic pivots within key prospect organizations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Market Research Assistant.
2. Click "Import" to add the workflow to your workspace.
3. Configure your API credentials within the environment settings.
4. Ensure nodes are correctly linked from **Chat Input** through the **Agent** and **Composio Toolset** to the **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company or industry keyword from the user.
- **Agent**: Processes the research request and determines the necessary search parameters.
- **Composio Toolset**: Executes precise queries against research databases and web search tools.
- **Chat Output**: Delivers the finalized, synthesized intelligence report to the user.

### 3) Run the Flow
Use the Playground to test your research capabilities:
- `Research the current market positioning of [Competitor Name] in the cloud infrastructure space.`
- `Provide a summary of recent industry trends affecting the SaaS sector for Q3.`
- `Generate a deep-dive intelligence report on [Target Account] including recent funding and leadership news.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine. Recommended instruction pattern:
- Define the persona as a Senior Market Analyst.
- Specify the required output structure (e.g., Executive Summary, Key Findings, Strategic Implications).
- Set constraints on data recency and source reliability to ensure high-quality output.

### 2) Composio Toolset Node
- Provide your API key for the relevant search and research integrations.
- Define the connection scope to allow the agent to access public web data and specific industry databases.

### 3) Tool Availability
- Web Search API for real-time news and public data.
- Financial Data Connectors for company-level performance metrics.
- Document Parser for synthesizing long-form reports into concise summaries.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Specialized agent for deep-dive account-level research and data gathering.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting tool for tracking lead signals and account activity.
- [Account Mapping Agent](../account-mapping-agent-by-bigpicture-io/README.md) - Visualizing and mapping complex account structures for enterprise sales.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) - Analyzing competitor video content for market positioning insights.
