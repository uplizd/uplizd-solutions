# Startup Opportunity Finder (Uplizd) - Automated lead and partnership discovery from Hacker News

## Summary
The Startup Opportunity Finder (Uplizd) is an intelligent AI workflow that monitors Hacker News discussions to identify emerging business opportunities, investment leads, and potential partnership signals. By leveraging real-time data extraction and natural language processing, this solution helps teams stay ahead of market trends, providing a single source of truth for high-value leads and reducing the manual effort required to scan community forums for actionable insights.

---

## Demo
![Startup Opportunity Finder workflow dashboard showing Hacker News data ingestion and lead extraction](image.png)
**Alt text (SEO-ready):** Startup Opportunity Finder workflow dashboard showing Hacker News data ingestion and lead extraction for business intelligence and lead generation on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e7d13aa2-b042-5f92-8652-1f0492f762cc)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** hackernews, lead generation, market intelligence, startup scouting, data extraction, ai workflow, composio, business development
- This solution bridges the gap between community-driven insights and professional sales operations by automating the discovery of high-intent startup signals.

---

## Who is this for?
This solution is designed for professionals who need to identify market opportunities before they become mainstream.

- **Business Development Managers**
    - Identify early-stage startups and potential partners mentioned in trending community discussions.
- **Venture Capital Analysts**
    - Track emerging technology trends and discover promising startups through real-time Hacker News sentiment analysis.
- **Sales Operations Leads**
    - Automate the ingestion of qualified leads from community forums directly into your CRM pipeline.
- **Growth Marketers**
    - Monitor niche discussions to find product-market fit signals and engage with potential customers in their natural environment.

---

## Features
- **Real-time Trend Monitoring**
    - Automatically scans Hacker News for specific keywords, company mentions, or industry-specific topics as they gain traction.
- **Intelligent Lead Extraction**
    - Uses advanced AI agents to parse unstructured forum comments and extract actionable contact data or company information.
- **Composio Toolset Integration**
    - Seamlessly connects extracted insights to your existing CRM or communication tools via the Composio Toolset.
- **Sentiment & Intent Analysis**
    - Filters noise by evaluating the intent behind discussions, ensuring only high-quality opportunities are flagged for review.
- **Automated Pipeline Sync**
    - Updates your sales or research pipeline automatically, ensuring no potential lead is missed due to manual oversight.

---

## Use Cases
**Market Intelligence Gathering**
- Monitor discussions about specific technology stacks to identify companies currently seeking solutions.
- Track sentiment changes around competitors to find gaps in their service offerings.

**Lead Generation & Scouting**
- Identify founders or early employees posting about their new ventures for potential outreach.
- Aggregate "Who is hiring" or "Show HN" threads to build a database of active, growing startups.

**Partnership Development**
- Find community members requesting features that align with your product's roadmap for targeted engagement.
- Discover potential integration partners by monitoring threads discussing interoperability and API needs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Configure your API credentials for the integrated tools within the settings panel.
4. Ensure nodes are correctly connected from the **Chat Input** to the **Agent** and finally to the **Composio Toolset** and **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the search parameters or industry keywords to monitor.
- **Agent**: Processes the Hacker News data and evaluates the relevance of each discussion.
- **Composio Toolset**: Executes the connection to your CRM or database to log the identified opportunities.
- **Chat Output**: Returns a summary report of the discovered leads and their context.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Find all startups mentioned in the last 24 hours related to AI infrastructure.`
- `Identify potential partnership opportunities from discussions about CRM integration.`
- `Scan for companies expressing pain points with current data synchronization tools.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary filter and analyst for incoming forum data.
- **Role**: Act as a market research analyst specialized in identifying high-intent business signals.
- **Instruction Pattern**: 
    - Prioritize mentions of company names and specific product pain points.
    - Ignore generic discussions and focus on actionable inquiries or founder announcements.
    - Format output as a structured list containing company name, context, and relevance score.

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and authorized for the target CRM or database.
- **Connection Scope**: Grant the toolset access to create or update records in your CRM to ensure seamless lead logging.

### 3) Tool Availability
- **Search API**: For querying Hacker News archives and real-time threads.
- **CRM Connector**: For logging leads directly into platforms like Salesforce or HubSpot.
- **Data Parser**: For cleaning and normalizing the extracted text into actionable fields.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed reports on target accounts and lead signals.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into potential business accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms and tools.
