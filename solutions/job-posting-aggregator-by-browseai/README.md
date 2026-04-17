# Job Posting Aggregator (Uplizd) - Automated job board monitoring and opportunity extraction

## Summary
The Job Posting Aggregator (Uplizd) is an intelligent workflow designed to automate the discovery and extraction of career opportunities from multiple job boards. By leveraging the Composio Toolset and BrowseAI, this solution eliminates manual searching, providing recruiters and job seekers with a centralized, real-time feed of relevant listings to accelerate pipeline velocity and ensure no high-value opportunity is missed.

---

## Demo
![Job Posting Aggregator workflow showing BrowseAI extraction and data synchronization](image.png)
**Alt text (SEO-ready):** Job Posting Aggregator workflow using Uplizd, BrowseAI, and Composio for automated job board data extraction and pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/job-posting-aggregator-by-browseai)

---

## Category
**Primary category:** Recruitment automation
**Secondary tags:** job boards, browseai, data extraction, talent acquisition, pipeline, composio, ai workflow, lead generation.
This solution streamlines the recruitment lifecycle by transforming fragmented job board data into a structured, actionable intelligence stream.

---

## Who is this for?
This solution is designed for professionals who need to monitor competitive job markets and talent acquisition channels with high precision.

*   **Technical Recruiters**
    *   Automate the identification of new roles to source candidates faster than competitors.
*   **Sales Development Reps (SDRs)**
    *   Identify companies currently hiring for specific roles to time outreach campaigns effectively.
*   **Market Researchers**
    *   Aggregate job posting trends to analyze industry growth and hiring velocity.
*   **Job Seekers**
    *   Centralize listings from multiple platforms into a single, filtered view based on specific criteria.

---

## Features
- **Automated Data Extraction**
  Leverages BrowseAI to scrape job boards in real-time, ensuring your database is always populated with the latest listings.
- **Intelligent Filtering**
  Uses the Agent node to parse raw text and filter opportunities based on seniority, location, and tech stack requirements.
- **Unified Pipeline Sync**
  Seamlessly pushes extracted job data into your CRM or spreadsheet, maintaining a single source of truth for all leads.
- **Customizable Alerting**
  Configures the Chat Output to notify your team via Slack or email the moment a high-priority role is detected.
- **Composio Toolset Integration**
  Connects directly to external platforms, allowing the agent to perform multi-step actions like saving leads or updating status fields.

---

## Use Cases
**Competitive Intelligence**
*   Monitor competitor hiring patterns to predict their expansion into new markets or product lines.
*   Track the frequency of specific skill requirements to identify emerging industry trends.

**Lead Generation**
*   Flag companies that have recently posted for "Head of Sales" or "VP" roles to trigger high-touch outreach.
*   Automate the population of a "Target Accounts" list based on active job board activity.

**Recruitment Operations**
*   Sync new job postings directly to a master tracking sheet for internal team review.
*   Filter out irrelevant listings by keyword, ensuring recruiters only spend time on high-match opportunities.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the builder.
3. Authenticate your BrowseAI and CRM credentials within the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Define the job boards, keywords, and filters (e.g., "Senior Engineer in New York").
*   **Agent**: Processes the input and instructs the tools on which specific data points to extract.
*   **Composio Toolset**: Executes the scraping and data synchronization tasks across connected platforms.
*   **Chat Output**: Returns a formatted summary of the discovered opportunities to your dashboard.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Find all remote Senior Product Manager roles posted in the last 24 hours on LinkedIn.`
* `Extract job titles and company names from the provided list of startup career pages.`
* `Monitor for new 'Sales Director' openings and sync them to my 'Target Accounts' CRM list.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence layer for interpreting job requirements and filtering noise.
*   Use a model capable of high-precision extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: "Act as a recruitment analyst. Parse job board data, filter by the user's criteria, and format the output for CRM entry."
*   Ensure the system prompt emphasizes data accuracy and deduplication.

### 2) Composio Toolset Node
*   **API Key**: Provide your unique Composio API key in the node settings.
*   **Connection Scope**: Ensure the toolset has read/write permissions for your target CRM and BrowseAI account.

### 3) Tool Availability
*   **BrowseAI**: For scraping and structured data extraction.
*   **CRM Connectors**: For pushing data into Salesforce, HubSpot, or Google Sheets.
*   **Notification Tools**: For sending alerts via Slack, Email, or Webhooks.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich company data and verify contact information for identified leads.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive into target company profiles to support personalized outreach.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Score and track new opportunities discovered through your aggregation workflows.
