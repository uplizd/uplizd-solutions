# Location-Based Lead Finder (Uplizd) - Automated geo-targeted prospect discovery and qualification

## Summary
The Location-Based Lead Finder by Uplizd automates the discovery, extraction, and qualification of local business prospects using real-time Google Maps data. By integrating search intelligence with automated lead processing, this workflow eliminates manual prospecting, ensuring sales teams maintain a high-velocity pipeline of verified local leads ready for outreach.

---

## Demo
![Location-Based Lead Finder workflow interface showing Google Maps integration and lead qualification nodes](image.png)
**Alt text (SEO-ready):** Location-Based Lead Finder workflow by Uplizd for automated Google Maps prospecting, lead qualification, and CRM data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/99f5d2b6-ad36-592d-bc6a-b7640b6942f9)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** google maps, lead generation, prospecting, sales intelligence, local business, data enrichment, composio, ai workflow
- This solution bridges the gap between raw geographic search data and actionable sales intelligence for local market expansion.

---

## Who is this for?
This workflow is designed for growth-focused teams looking to scale their local outreach efforts with precision.

- **Sales Development Representative (SDR)**
    - Automates the tedious process of finding and vetting local business leads, allowing for more time spent on direct outreach.
- **Growth Marketer**
    - Identifies high-potential geographic clusters to target for localized marketing campaigns and regional expansion.
- **Field Sales Manager**
    - Maintains a consistent stream of qualified local prospects to optimize territory planning and on-the-ground sales activities.
- **RevOps Specialist**
    - Ensures that lead data captured from external maps is standardized and synced directly into the CRM for better pipeline hygiene.

---

## Features
- **Automated Geo-Search**
    - Leverages the Composio Toolset to query Google Maps for specific business categories within defined geographic radiuses.
- **Intelligent Lead Qualification**
    - Uses an AI Agent to filter prospects based on business signals, such as review counts, ratings, and operational status.
- **Real-Time Data Extraction**
    - Automatically pulls contact details, addresses, and website links directly from map listings into a structured format.
- **CRM Integration Ready**
    - Seamlessly connects with your existing CRM to push qualified leads, preventing manual data entry errors.
- **Workflow Scalability**
    - Processes large volumes of location data in parallel, allowing for rapid scaling of lead lists across multiple cities or regions.

---

## Use Cases
**Local Market Expansion**
- Identify all competitors or potential partners within a 5-mile radius of a new office location.
- Aggregate contact information for local businesses to support a targeted regional direct-mail or email campaign.

**Sales Territory Optimization**
- Generate a list of high-rated businesses in under-penetrated zip codes to prioritize BDR outreach.
- Filter out low-intent leads by setting custom rating thresholds, ensuring the sales team focuses only on top-tier prospects.

**Competitive Intelligence**
- Monitor new business openings in specific sectors to gain a first-mover advantage in local markets.
- Analyze the density of specific service providers in a region to identify gaps in the local service landscape.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Google Maps and CRM integrations within the Composio Toolset.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the target location, business category, and qualification criteria.
- **Agent**: Analyzes the input and orchestrates the search and filtering logic.
- **Composio Toolset**: Executes the Google Maps API calls and data retrieval.
- **Chat Output**: Returns the final, qualified list of leads formatted for your CRM.

### 3) Run the Flow
Use the Playground to test your prospecting queries:
- `Find all coffee shops in downtown Seattle with a rating above 4.5.`
- `Search for plumbing services in Austin, TX and extract their website URLs.`
- `List all fitness centers in Miami within 10 miles of the city center that have more than 50 reviews.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, interpreting search intent and validating business data.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a lead generation expert. Use the provided tools to search for businesses, filter them based on the user's criteria, and output a clean JSON list."
- Ensure the agent is instructed to ignore businesses missing key contact information.

### 2) Composio Toolset Node
- Provide your API key to enable secure access to the Google Maps integration.
- Set the connection scope to allow read-only access to business listings and location data.

### 3) Tool Availability
- **Google Maps Search API**: For finding business entities based on keywords and location.
- **Place Details API**: For extracting specific contact information and review metrics.
- **Data Formatter**: For cleaning and standardizing the output for CRM compatibility.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact details.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Conduct deep-dive research on target accounts.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automate firmographic data collection for sales prospecting.
