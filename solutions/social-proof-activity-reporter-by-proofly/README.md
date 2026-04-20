# Social Proof Activity Reporter (Uplizd) - Automate customer engagement and social proof analytics

## Summary
The Social Proof Activity Reporter is an intelligent Uplizd workflow designed to aggregate, analyze, and report on customer engagement signals and social proof data. By automating the collection of testimonials, reviews, and activity metrics, this solution provides marketing and sales teams with a single source of truth to validate brand authority, improve conversion rates, and streamline data-driven storytelling.

---

## Demo
![Social Proof Activity Reporter workflow dashboard showing automated data ingestion and report generation](image.png)
**Alt text (SEO-ready):** Social Proof Activity Reporter workflow dashboard showing automated data ingestion, customer engagement analysis, and report generation using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d4a2a22d-8afb-5ce8-a8c8-7458f4b0388c)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** social proof, customer engagement, data reporting, analytics, conversion optimization, composio, ai workflow, marketing automation  
This solution bridges the gap between raw customer interaction data and actionable marketing intelligence.

---

## Who is this for?
This workflow is designed for professionals focused on leveraging customer sentiment to drive growth and brand trust.

* **Marketing Managers**
    * Automate the aggregation of social proof to maintain a consistent library of customer success stories.
* **Growth Leads**
    * Identify high-impact engagement signals to optimize landing page copy and conversion strategies.
* **Customer Success Managers**
    * Track and report on positive user activities to highlight account health and advocacy.
* **Sales Operations Specialists**
    * Generate real-time reports on social proof effectiveness to support the sales pipeline with verified trust signals.

---

## Features
- **Automated Data Aggregation**
  Centralize customer feedback and activity logs from multiple platforms into a unified reporting structure.
- **Sentiment Analysis Engine**
  Utilize AI to categorize customer interactions, distinguishing between general feedback and high-value social proof.
- **Real-Time Reporting**
  Generate dynamic reports that summarize recent engagement trends, ready for stakeholder review.
- **Composio-Powered Integration**
  Seamlessly connect with CRM and social platforms to pull interaction data without manual export processes.
- **Customizable Insight Extraction**
  Configure the agent to focus on specific metrics, such as review frequency, testimonial quality, or engagement velocity.

---

## Use Cases
**Brand Authority Building**
* Automatically compile recent 5-star reviews into a weekly "Customer Success" digest.
* Identify top-performing testimonials to be featured in upcoming email marketing campaigns.

**Conversion Rate Optimization**
* Analyze which customer activities correlate most strongly with high-intent buying signals.
* Generate reports on social proof gaps to inform where more customer testimonials are needed.

**Sales Enablement**
* Provide sales teams with a list of recent positive customer mentions to use in outreach emails.
* Track the impact of social proof on deal velocity by mapping activity reports against opportunity stages.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Social Proof Activity Reporter template from the solution library.
3. Authenticate your required CRM and social platform connectors via the Composio dashboard.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the user request for specific social proof data or reporting timeframes.
* **Agent**: Processes the request, interprets the intent, and determines which data sources to query.
* **Composio Toolset**: Executes the API calls to fetch engagement data from integrated platforms.
* **Chat Output**: Formats the retrieved data into a clear, professional report for the user.

### 3) Run the Flow
Use the Playground to test your reporting capabilities:
* `Generate a summary report of all positive customer reviews from the last 7 days.`
* `Identify the top 3 most engaged customers based on recent social media interactions.`
* `Create a list of recent testimonials that mention our new product feature.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized data analyst.
* **Instruction Pattern:**
    * Focus on extracting actionable insights rather than just raw data.
    * Maintain a professional, objective tone suitable for marketing reporting.
    * Prioritize data accuracy by cross-referencing timestamps and engagement metrics.

### 2) Composio Toolset Node
Connect your specific platforms (e.g., HubSpot, Salesforce, or social media APIs) within the Composio Toolset node. Ensure the agent has "Read" access to the relevant modules (e.g., Contacts, Deals, or Social Activity logs).

### 3) Tool Availability
* **CRM Connector**: For pulling customer interaction history and feedback logs.
* **Social Media API**: For monitoring brand mentions and engagement metrics.
* **Data Formatting Tool**: For structuring raw API output into clean, readable reports.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Identify and report on key account signals for sales teams.
* [Affiliate Performance Monitor](../affiliate-performance-monitor-by-tapfiliate/README.md) — Track and optimize affiliate-driven engagement and conversion data.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Monitor and score opportunities based on engagement signals.
