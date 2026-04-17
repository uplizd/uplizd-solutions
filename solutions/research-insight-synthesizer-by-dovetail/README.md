# Research Insight Synthesizer (Uplizd) - Transform raw research data into actionable insights

## Summary
The Research Insight Synthesizer is an automated Uplizd AI workflow designed to ingest, analyze, and distill complex research data from platforms like Dovetail into clear, strategic takeaways. By automating the synthesis of qualitative feedback and research notes, this solution eliminates manual data processing, ensuring that product teams, researchers, and stakeholders can make evidence-based decisions with significantly reduced turnaround time.

---

## Demo
![Research Insight Synthesizer dashboard showing automated qualitative data analysis and insight extraction](image.png)
**Alt text (SEO-ready):** Research Insight Synthesizer dashboard showing automated qualitative data analysis and insight extraction within the Uplizd AI workflow and Composio integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQ6Y42OQAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAKYGBgYPhPBf9/YGBg+E8F/39gYGD4TwX/f2BgYPhPBf9/YGBg+E8F/39gYGD4TwUAAC44A4W622/gAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/02b7c201-c5a7-502f-9cf3-ed38e613ca1a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** research, dovetail, data synthesis, insights, qualitative analysis, ai workflow, composio, knowledge management
- This solution bridges the gap between raw user research and strategic product planning by automating the synthesis of qualitative datasets.

---

## Who is this for?
This solution is designed for teams that handle high volumes of qualitative research and need to accelerate the time-to-insight.

- **UX Researcher**
    - Automates the tedious tagging and clustering of interview transcripts to focus on high-level pattern recognition.
- **Product Manager**
    - Converts raw user feedback into prioritized feature requests and product requirements without manual synthesis.
- **Customer Insights Lead**
    - Ensures a single source of truth for customer sentiment by centralizing insights from disparate research projects.
- **Strategy Consultant**
    - Rapidly distills large-scale qualitative datasets into executive-ready summaries and strategic recommendations.

---

## Features
- **Automated Data Ingestion**
    - Seamlessly pulls raw research data and transcripts from Dovetail using the Composio Toolset for real-time processing.
- **Intelligent Pattern Recognition**
    - Leverages advanced LLM logic to identify recurring themes, sentiment shifts, and actionable pain points across multiple documents.
- **Structured Insight Generation**
    - Automatically formats synthesized findings into standardized reports, including executive summaries and evidence-backed recommendations.
- **Cross-Platform Integration**
    - Connects research repositories with project management tools to ensure insights are immediately actionable for development teams.
- **Customizable Synthesis Logic**
    - Allows users to define specific research goals or focus areas, ensuring the AI prioritizes the most relevant data points for the business.

---

## Use Cases
**Qualitative Data Analysis**
- Automatically cluster hundreds of user interview transcripts into distinct thematic categories.
- Extract sentiment trends from long-form customer feedback to identify emerging product issues.

**Strategic Product Planning**
- Transform raw research notes into a prioritized backlog of feature requests based on user impact.
- Generate evidence-based summaries for stakeholders that link specific user quotes to strategic business goals.

**Knowledge Management**
- Maintain a searchable, synthesized database of all historical research insights for future reference.
- Quickly generate "State of the User" reports by aggregating insights across multiple research cycles.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Research Insight Synthesizer template from the marketplace.
3. Authenticate your Dovetail and relevant project management tool connections via the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts the research project ID or raw text data for analysis.
- **Agent**: Orchestrates the synthesis logic, applying research frameworks to the input data.
- **Composio Toolset**: Executes API calls to retrieve research data and push synthesized insights to destination platforms.
- **Chat Output**: Delivers the final, structured insight report to the user.

### 3) Run the Flow
Use the Playground to test your synthesis logic with these prompts:
- `Synthesize the latest interview transcripts from project [ID] and highlight top 3 user pain points.`
- `Create a summary report of all user feedback regarding the new onboarding flow from the last 30 days.`
- `Extract actionable feature requests from the research data and format them for a Jira ticket.`

---

## Configuration

### 1) Language Model (Agent Node)
The Agent acts as a specialized research analyst, maintaining objectivity and clarity.
- **Instruction Pattern:**
    - "Act as a senior UX researcher; prioritize evidence-based findings over subjective interpretations."
    - "Maintain a consistent output format: Executive Summary, Key Themes, and Recommended Actions."
    - "Ensure all insights are directly linked to source data points or user quotes."

### 2) Composio Toolset Node
- **API Key:** Provide your authenticated API key for the research platform (e.g., Dovetail).
- **Connection Scope:** Ensure the agent has read access to research projects and write access to your chosen documentation or task management tool.

### 3) Tool Availability
- **Data Retrieval:** Fetch transcripts, notes, and tagged segments.
- **Insight Formatting:** Generate markdown-based reports and structured summaries.
- **Integration Sync:** Push findings to project management or collaborative workspace tools.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate account intelligence gathering for sales teams.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate comprehensive account reports based on web traffic and firmographic data.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize the efficiency of internal team processes.
