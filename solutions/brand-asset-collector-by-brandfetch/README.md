# Brand Asset Collector (Uplizd) - Automate brand identity management and asset synchronization

## Summary
The Brand Asset Collector by Uplizd is an intelligent workflow designed to automate the discovery, retrieval, and organization of brand assets using the Brandfetch API. By streamlining the collection of logos, color palettes, and brand guidelines, this solution eliminates manual search time, ensures marketing teams maintain a single source of truth for visual identity, and accelerates the production of high-quality campaign materials.

---

## Demo
![Brand Asset Collector workflow diagram showing Brandfetch integration and automated asset organization](image.png)
**Alt text (SEO-ready):** Uplizd Brand Asset Collector workflow automating brand identity retrieval, logo collection, and asset synchronization via Brandfetch API.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8472c8d2-a7ec-580a-a705-baf459171ab2)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** brandfetch, asset management, marketing automation, brand identity, design ops, composio, ai workflow
- This solution bridges the gap between raw brand data and creative execution by automating the ingestion of corporate identity assets.

---

## Who is this for?
This solution is built for teams that need to maintain strict brand consistency across diverse digital channels.

- **Brand Managers**
    - Ensure all external partners and internal teams use the latest approved logo versions and color hex codes.
- **Graphic Designers**
    - Reduce time spent manually hunting for high-resolution assets by automating the retrieval process.
- **Marketing Operations Leads**
    - Standardize the asset collection pipeline to improve hygiene across campaign management platforms.
- **Content Strategists**
    - Quickly pull brand-compliant visual elements to populate social media templates and presentation decks.

---

## Features
- **Automated Asset Retrieval**
    - Instantly fetch logos, icons, and brand imagery directly from the Brandfetch database using company domains.
- **Centralized Metadata Sync**
    - Automatically extract and store color palettes, fonts, and social media links into your preferred project management tool.
- **Real-time Validation**
    - Verify asset availability and quality before syncing, ensuring only high-resolution files enter your creative repository.
- **Composio-Powered Integration**
    - Leverage the Composio Toolset to seamlessly connect Brandfetch data with CRM and project management workflows.
- **Scalable Batch Processing**
    - Process multiple brand profiles simultaneously to support large-scale agency operations or multi-brand portfolios.

---

## Use Cases
**Brand Identity Onboarding**
- Automatically populate a new client's workspace with their official logo and brand colors during the initial setup phase.
- Sync brand guidelines into a central knowledge base to ensure all stakeholders have immediate access to visual standards.

**Marketing Campaign Production**
- Pull the latest brand assets into a creative project folder as soon as a new campaign is initiated in your CRM.
- Update outdated brand elements across existing project files when a company undergoes a visual refresh.

**Agency Asset Audits**
- Periodically scan client portfolios to ensure the assets stored in your internal database match the current live brand identity.
- Generate summary reports of missing or low-resolution assets to prioritize cleanup tasks for the design team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Authenticate your Brandfetch API credentials within the integration settings.
4. Ensure nodes are correctly mapped to your target storage or CRM destination.

### 2) Setup the Nodes
- **Chat Input:** Define the company domain or brand name you wish to collect assets for.
- **Agent:** Processes the request and triggers the Brandfetch search logic.
- **Composio Toolset:** Executes the API calls to retrieve and format the brand data.
- **Chat Output:** Confirms the successful collection and storage of assets in your destination.

### 3) Run the Flow
Use the Playground to test your asset collection:
- `Collect all brand assets for apple.com and save them to the design folder.`
- `Fetch the primary logo and color palette for google.com.`
- `Get brand identity details for slack.com and update the project metadata.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for asset retrieval.
- Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Extract the company domain from the user input, query the Brandfetch API, and map the returned assets to the configured output fields."
- Ensure the agent is configured to handle null results gracefully if a brand is not found.

### 2) Composio Toolset Node
- Provide your Brandfetch API key in the integration settings.
- Set the connection scope to allow read-only access to brand metadata and asset URLs.

### 3) Tool Availability
- **Brandfetch Search:** Locate brand profiles by domain.
- **Asset Extraction:** Retrieve specific file types (SVG, PNG, JPG).
- **Metadata Parser:** Organize color codes, fonts, and social links into structured JSON.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with contact and firmographic details.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive into company profiles and market positioning.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline operational tasks across project management platforms.
