# Content Intelligence Analyst (Uplizd) - Transform raw content into actionable business insights

## Summary
The Content Intelligence Analyst is an automated Uplizd workflow that leverages the TextRazor engine to parse, categorize, and extract deep semantic insights from unstructured text. By automating the extraction of entities, topics, and sentiment, this solution enables marketing and research teams to turn raw content into a single source of truth for data-driven decision-making, significantly increasing pipeline velocity and content hygiene.

---

## Demo
![Content Intelligence Analyst workflow showing TextRazor integration for semantic data extraction](image.png)
**Alt text (SEO-ready):** Content Intelligence Analyst workflow for semantic text parsing, Uplizd AI automation, and TextRazor data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/d841ef67-be30-5053-ad8e-b4f11aa49d3f)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content intelligence, textrazor, semantic analysis, nlp, data extraction, ai workflow, content strategy, composio
- This solution bridges the gap between unstructured content and structured marketing data, providing automated intelligence for content optimization.

---

## Who is this for?
This solution is designed for professionals who need to derive structured value from high volumes of text-based information.

- **Content Strategist**
    - Automates the tagging and categorization of large content libraries to improve searchability and audience targeting.
- **Market Researcher**
    - Extracts key entities and sentiment trends from competitor articles and industry reports to identify market shifts.
- **SEO Specialist**
    - Identifies high-value keywords and semantic topics to optimize content performance and organic search rankings.
- **Marketing Operations Manager**
    - Ensures consistent metadata application across marketing assets, reducing manual data entry and improving content hygiene.

---

## Features
- **Semantic Entity Extraction**
    - Automatically identifies people, organizations, and locations within text using advanced NLP to build structured databases.
- **Automated Topic Categorization**
    - Classifies content into predefined industry taxonomies, ensuring every asset is correctly indexed for internal search.
- **Sentiment & Tone Analysis**
    - Evaluates the emotional resonance of content pieces to ensure brand consistency and audience alignment.
- **Real-time Data Integration**
    - Uses the Composio Toolset to push extracted insights directly into your CRM or marketing automation platform.
- **Bulk Processing Capability**
    - Handles high-volume document ingestion, allowing for the rapid analysis of entire content archives in minutes.

---

## Use Cases
**Content Library Optimization**
- Automatically tag legacy blog posts with relevant entities to improve internal content discovery.
- Generate metadata summaries for large batches of whitepapers to streamline content management workflows.

**Competitive Intelligence**
- Extract key strategic themes from competitor press releases to inform your own content roadmap.
- Monitor industry news feeds for specific entity mentions to track market sentiment in real-time.

**Marketing Performance Analysis**
- Correlate extracted topic clusters with engagement metrics to identify which content themes drive the most conversions.
- Standardize content classification across global teams to maintain a clean and actionable marketing database.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the provided Content Intelligence Analyst JSON template.
3. Connect your TextRazor API credentials to the environment variables.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw text or URL to be analyzed.
- **Agent**: Processes the text and applies semantic logic via the TextRazor engine.
- **Composio Toolset**: Executes the data mapping and pushes results to external platforms.
- **Chat Output**: Returns the structured insights and categorization report to the user.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Analyze this article for key entities and provide a sentiment score: [Paste URL/Text]`
- `Categorize the following text into our marketing taxonomy and identify the primary topic: [Paste Text]`
- `Extract all organization names and their associated relevance scores from this report: [Paste Text]`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for semantic parsing and data formatting.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5) for accurate entity extraction.
- Instruct the agent to output data in a consistent JSON schema for downstream integration.
- Define specific taxonomy rules in the system prompt to ensure categorization alignment.

### 2) Composio Toolset Node
- Authenticate with your chosen CRM or database via the Composio Toolset.
- Ensure the connection scope includes write access to the relevant content metadata fields.

### 3) Tool Availability
- **TextRazor API**: For deep semantic parsing and entity recognition.
- **CRM Connectors**: For syncing extracted metadata to Salesforce, HubSpot, or similar platforms.
- **Data Transformation Tools**: For formatting output into CSV or JSON structures.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with external signals.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate automated reports on account activity.
- [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) - Automate the distribution of video content assets.
