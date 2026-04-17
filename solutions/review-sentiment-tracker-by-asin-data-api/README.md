# Review Sentiment Tracker (Uplizd) - Automated ASIN-based customer feedback analysis

## Summary
The Review Sentiment Tracker is an intelligent Uplizd workflow designed to automate the extraction and analysis of customer feedback for specific products. By leveraging the ASIN Data API, this solution aggregates product reviews, performs real-time sentiment analysis, and generates actionable insights. It serves as a single source of truth for product teams, enabling them to identify recurring pain points, track sentiment trends over time, and improve overall product hygiene and customer satisfaction.

---

## Demo
![Review Sentiment Tracker dashboard showing sentiment scores and trend analysis for product ASINs](image.png)
**Alt text (SEO-ready):** Uplizd Review Sentiment Tracker workflow dashboard showing automated ASIN data extraction, customer feedback sentiment analysis, and product performance trends.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/698c85c9-5451-5dca-b0d8-cc5584c6ebc1)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** sentiment analysis, asin data, customer feedback, product insights, e-commerce, ai workflow, composio, data analytics
- This solution bridges the gap between raw e-commerce product reviews and strategic product development by automating data ingestion and sentiment classification.

---

## Who is this for?
This solution is designed for teams managing product performance and customer experience at scale.

- **Product Managers**
    - Identify feature gaps and usability issues directly from customer-reported feedback.
- **Customer Success Leads**
    - Monitor shifts in product sentiment to proactively address emerging customer concerns.
- **E-commerce Analysts**
    - Automate the aggregation of competitive intelligence and review data across multiple ASINs.
- **Marketing Operations**
    - Track the impact of product updates on public perception and brand sentiment.

---

## Features
- **Automated ASIN Data Extraction**
    - Seamlessly pulls real-time review data for specific product ASINs using integrated API connectors.
- **AI-Driven Sentiment Analysis**
    - Utilizes advanced LLM capabilities to categorize feedback into positive, neutral, or negative sentiment.
- **Trend Identification**
    - Detects recurring keywords and topics within reviews to highlight common product strengths and weaknesses.
- **Composio-Powered Tooling**
    - Leverages the Composio Toolset to manage data flow between the ASIN Data API and the Uplizd agentic workflow.
- **Actionable Reporting**
    - Generates summarized insights and recommendations based on the analyzed review corpus for immediate stakeholder review.

---

## Use Cases
**Product Quality Monitoring**
- Automatically flag products with a sudden drop in sentiment scores for immediate engineering review.
- Generate weekly summaries of top-mentioned product issues to prioritize the development roadmap.

**Competitive Intelligence**
- Track sentiment trends for competitor ASINs to identify market opportunities and feature gaps.
- Benchmark your product's performance against similar items in the category based on verified customer reviews.

**Customer Experience Optimization**
- Extract specific feature requests from positive reviews to inform future product iterations.
- Identify common friction points in the user experience that lead to negative sentiment and churn.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Review Sentiment Tracker template from the solution library.
3. Connect your ASIN Data API credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the target ASINs and analysis parameters from the user.
- **Agent**: Processes review data, performs sentiment classification, and synthesizes findings.
- **Composio Toolset**: Executes API calls to fetch raw review data and metadata.
- **Chat Output**: Delivers the final sentiment report and actionable insights to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Analyze the sentiment for ASIN B08N5K3LWJ over the last 30 days.`
- `What are the top 3 recurring complaints for this product based on recent reviews?`
- `Compare the sentiment of my product ASIN against this competitor ASIN.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting raw review text and mapping it to sentiment categories.
- **Instruction Pattern:**
    - Act as a product analyst specializing in e-commerce sentiment and customer feedback.
    - Focus on identifying recurring themes and quantifying sentiment shifts.
    - Maintain a neutral, data-driven tone in all generated summaries and reports.

### 2) Composio Toolset Node
- Requires a valid API key for the ASIN Data API.
- Connection scope should include read-only access to product review endpoints to ensure data integrity.

### 3) Tool Availability
- **Review Fetcher**: Retrieves raw review text, star ratings, and timestamps.
- **Sentiment Classifier**: Categorizes text into sentiment buckets.
- **Trend Aggregator**: Groups feedback by common topics or keywords.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automate the gathering of account-level insights and reporting.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze audience sentiment and engagement on video content.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Manage customer inquiries and support tickets with AI-driven responses.
