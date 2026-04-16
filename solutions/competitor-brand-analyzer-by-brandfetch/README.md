# Competitor Brand Analyzer (Uplizd) - Automate visual identity and brand intelligence tracking

## Summary
The Competitor Brand Analyzer is an intelligent Uplizd workflow that leverages the Brandfetch API to monitor, extract, and analyze competitor branding assets in real-time. By automating the retrieval of logos, color palettes, and brand guidelines, this solution provides marketing and product teams with a single source of truth for competitive visual intelligence, ensuring your brand positioning remains distinct and data-driven.

---

## Demo
![Competitor Brand Analyzer workflow showing Brandfetch integration and automated asset extraction](image.png)
**Alt text (SEO-ready):** Competitor Brand Analyzer Uplizd workflow using Brandfetch for automated brand asset extraction, visual identity tracking, and competitive intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5c4613bc-74a2-5a02-9f94-831ba626e380)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** brand intelligence, competitor analysis, brandfetch, marketing automation, visual identity, market research, asset management, composio
- This solution streamlines the collection of external brand data, allowing teams to maintain a competitive edge through automated visual monitoring.

---

## Who is this for?
This workflow is designed for teams that need to maintain a pulse on the competitive landscape without manual research.

- **Brand Managers**
    - Automate the collection of competitor visual assets to ensure brand differentiation.
- **Product Marketers**
    - Quickly gather brand guidelines and color palettes to inform landing page and campaign design.
- **Market Researchers**
    - Maintain an up-to-date database of competitor branding changes for quarterly competitive audits.
- **Creative Directors**
    - Access high-quality brand assets instantly to streamline the creative briefing process.

---

## Features
- **Automated Asset Retrieval**
    - Instantly fetch logos, icons, and brand imagery directly from the Brandfetch database.
- **Color Palette Extraction**
    - Automatically identify and store competitor color hex codes to analyze market design trends.
- **Real-time Brand Updates**
    - Trigger workflows to refresh brand data whenever a competitor updates their public identity.
- **Composio-Powered Integration**
    - Seamlessly connect the Brandfetch toolset to your existing CRM or project management tools via the Composio workflow engine.
- **Centralized Intelligence Hub**
    - Aggregate disparate brand data into a structured format for easy reporting and team collaboration.

---

## Use Cases
**Competitive Benchmarking**
- Automatically pull competitor logos and brand styles to populate a competitive landscape dashboard.
- Compare your brand's color palette against industry leaders to identify opportunities for visual differentiation.

**Marketing Asset Management**
- Sync competitor brand assets into your internal asset library for quick reference during campaign planning.
- Monitor for changes in competitor branding to proactively adjust your own creative strategy.

**Market Research Automation**
- Generate automated reports detailing the visual evolution of key competitors over time.
- Streamline the onboarding of new competitors into your research database with one-click asset fetching.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Competitor Brand Analyzer.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Brandfetch API credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the competitor domain or brand name from the user.
- **Agent**: Processes the request and determines which brand assets to retrieve.
- **Composio Toolset**: Executes the Brandfetch API calls to fetch specific visual data.
- **Chat Output**: Displays the retrieved brand assets and analysis summary to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Fetch the brand assets and primary color palette for apple.com`
- `Get the latest logo and brand guidelines for slack.com`
- `Analyze the visual identity trends for microsoft.com`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for brand intelligence queries.
- Use a model capable of structured data extraction.
- Instruct the agent to prioritize high-resolution assets.
- Ensure the agent formats output clearly for marketing team review.

### 2) Composio Toolset Node
- Provide your Brandfetch API key to enable secure access to brand data.
- Configure the connection scope to allow read-only access to public brand profiles.

### 3) Tool Availability
- **Brandfetch Search**: Locate brand profiles by domain.
- **Asset Extractor**: Retrieve logos, icons, and typography files.
- **Palette Analyzer**: Extract primary and secondary brand colors.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with contact and firmographic insights.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into target accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate automated reports on account engagement and intent.
