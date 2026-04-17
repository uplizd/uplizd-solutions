# Product Review Intelligence (Uplizd) - Transform customer feedback into actionable product insights

## Summary
The Product Review Intelligence solution by Uplizd automates the analysis of customer feedback by leveraging the Diffbot API to extract, categorize, and synthesize sentiment from product reviews. This workflow empowers product teams to move beyond manual data entry, providing a single source of truth for user sentiment and feature requests to accelerate product development velocity and improve data hygiene.

---

## Demo
![Product Review Intelligence dashboard showing sentiment analysis and feature request extraction](image.png)
**Alt text (SEO-ready):** Product Review Intelligence dashboard showing sentiment analysis, customer feedback categorization, and feature request extraction using Uplizd and Diffbot.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/9581894a-de85-5a85-b54a-4f324862a6aa)

---

## Category
**Primary category:** Product operations
**Secondary tags:** product management, customer feedback, sentiment analysis, diffbot, data extraction, ai workflow, composio, product insights.
This solution bridges the gap between raw customer feedback and strategic product planning by automating the ingestion and analysis of review data.

---

## Who is this for?
This solution is designed for product-led teams looking to scale their feedback loops and prioritize development based on real user data.

- **Product Managers**
    - Identify recurring pain points and feature requests across multiple review platforms to inform the product roadmap.
- **Customer Success Leads**
    - Monitor sentiment trends to proactively address user dissatisfaction before it leads to churn.
- **Data Analysts**
    - Automate the extraction of structured data from unstructured review text for deeper quantitative analysis.
- **Growth Marketers**
    - Extract authentic user testimonials and common praise points to refine messaging and marketing collateral.

---

## Features
- **Automated Review Ingestion**
    - Seamlessly pull raw review data from various sources using the Diffbot integration for high-fidelity extraction.
- **Sentiment Scoring**
    - Automatically assign sentiment polarity to individual reviews to track user satisfaction over time.
- **Topic Categorization**
    - Cluster feedback into predefined product areas, such as UI/UX, performance, or pricing, for organized reporting.
- **Feature Request Extraction**
    - Identify and summarize specific feature requests mentioned by users to prioritize the engineering backlog.
- **Real-time Insight Sync**
    - Push synthesized insights directly into your project management tools via the Composio Toolset for immediate action.

---

## Use Cases
**Strategic Product Planning**
- Aggregate feedback from the last 30 days to identify the top three most requested features.
- Correlate sentiment drops with specific product updates or release versions.

**Customer Experience Optimization**
- Flag negative reviews containing specific keywords like "bug" or "crash" for immediate support triage.
- Identify "power users" based on positive sentiment and detailed feature feedback for beta testing programs.

**Competitive Benchmarking**
- Analyze competitor product reviews to identify gaps in their offering that your product can address.
- Track sentiment shifts following a competitor's pricing or feature change.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the template in the builder.
2. Connect your Diffbot API credentials within the Composio Toolset node.
3. Configure your target output destination (e.g., Slack, Jira, or a CRM).
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the URL or text block containing the product reviews to be analyzed.
- **Agent**: Processes the raw data, performs sentiment analysis, and extracts key product insights.
- **Composio Toolset**: Connects the agent to external APIs for data retrieval and insight distribution.
- **Chat Output**: Delivers the final summary report, categorized feedback, and actionable recommendations.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Analyze the reviews from this URL and summarize the top 3 user complaints.`
- `Extract all feature requests from the provided text and categorize them by product module.`
- `What is the overall sentiment trend for this product based on the last 50 reviews?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, transforming unstructured text into structured insights.
- Instruct the agent to maintain a neutral, objective tone when summarizing feedback.
- Use a structured JSON output format for easier integration with downstream tools.
- Prioritize identifying actionable requests over general praise or criticism.

### 2) Composio Toolset Node
- Provide your Diffbot API key to enable web scraping and data extraction capabilities.
- Define the connection scope to allow the agent to read from specific review platforms and write to your preferred project management tool.

### 3) Tool Availability
- **Web Extraction**: Capability to scrape and parse review content from public URLs.
- **Sentiment Analysis Engine**: Capability to process text and return sentiment scores.
- **Data Formatting**: Capability to structure extracted insights into actionable reports.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data to better understand your user base.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Track account engagement and intent signals.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the performance and health of your internal automated processes.
