# Market Research Analyst (Uplizd) - Automated demographic and business intelligence reporting

## Summary
The Market Research Analyst workflow leverages the Uplizd AI engine to synthesize vast datasets from the Census Bureau and other public repositories into actionable business intelligence. By automating the extraction and analysis of demographic trends, this solution provides a single source of truth for market sizing, consumer profiling, and competitive landscape assessment, significantly increasing pipeline velocity for strategic planning teams.

---

## Demo
![Market Research Analyst workflow dashboard showing data extraction from Census Bureau APIs and AI-generated summary report](image.png)
**Alt text (SEO-ready):** Market Research Analyst dashboard by Uplizd showing automated demographic data extraction, business intelligence reporting, and AI-driven market analysis workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1a23b41e-6ef5-51f9-8520-6bed4412e742)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** market research, census bureau, business intelligence, data analysis, ai workflow, demographic data, composio, strategic planning
- This solution bridges the gap between raw public sector data and executive-level decision-making through automated AI synthesis.

---

## Who is this for?
This workflow is designed for professionals who need to turn complex demographic data into clear, strategic narratives.

- **Market Researcher**
    - Automates the collection of regional demographic data to identify new growth opportunities.
- **Strategic Planner**
    - Provides data-backed insights for long-term resource allocation and market entry strategies.
- **Business Analyst**
    - Reduces manual data cleanup time by normalizing Census Bureau outputs into structured reports.
- **Product Manager**
    - Validates target audience assumptions using real-world population and economic metrics.

---

## Features
- **Automated Data Extraction**
    - Seamlessly pulls real-time demographic and economic datasets from public APIs using the Composio Toolset.
- **AI-Driven Synthesis**
    - Uses advanced language models to summarize complex statistical tables into plain-English business insights.
- **Trend Forecasting**
    - Identifies year-over-year population and economic shifts to help predict future market behavior.
- **Structured Reporting**
    - Automatically formats research findings into professional, shareable summaries ready for stakeholder review.
- **Integration-Ready Pipeline**
    - Connects directly with your existing CRM and BI tools to push research findings into your active project workflows.

---

## Use Cases
**Market Expansion Analysis**
- Identify high-growth regions based on population density and median household income metrics.
- Compare demographic profiles across multiple zip codes to prioritize regional sales efforts.

**Consumer Profiling**
- Generate detailed personas based on local census data to refine marketing messaging.
- Analyze economic stability indicators to adjust pricing strategies for specific geographic segments.

**Competitive Landscape Mapping**
- Aggregate public data to assess the total addressable market (TAM) for new product launches.
- Monitor shifts in local labor force participation to inform talent acquisition and operational planning.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Market Research Analyst template from the solution library.
3. Authenticate your required API keys within the integration settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your research query (e.g., "Analyze demographic trends in Austin, TX").
- **Agent**: Processes the request and determines which data points to fetch.
- **Composio Toolset**: Executes the API calls to retrieve Census Bureau and market data.
- **Chat Output**: Delivers the final, synthesized research report to the user.

### 3) Run the Flow
Use the Playground to test your research agent with these prompts:
- `Analyze the population growth and median income trends in Seattle over the last 5 years.`
- `Create a demographic profile for the target audience in the 90210 zip code.`
- `Compare the economic stability of the top 3 metropolitan areas in Florida for a new retail launch.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized research analyst.
- **Instruction Pattern**:
    - Focus on extracting statistical significance from raw data.
    - Maintain an objective, professional tone suitable for executive summaries.
    - Prioritize data accuracy by cross-referencing multiple demographic indicators.

### 2) Composio Toolset Node
- Requires a valid API key for the Census Bureau or relevant data provider.
- Set the connection scope to allow read-only access to demographic and economic datasets.

### 3) Tool Availability
- **Data Fetching**: Capability to query census tracts, population counts, and economic indicators.
- **Data Normalization**: Ability to convert raw JSON/CSV responses into structured text.
- **Contextual Analysis**: Ability to correlate demographic shifts with business-specific variables.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research on specific business accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generates comprehensive intelligence reports for sales teams.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyzes viewer demographics and content performance metrics.
