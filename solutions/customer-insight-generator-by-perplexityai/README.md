# Customer Insight Generator (Uplizd) - Transform customer inquiries into actionable business intelligence

## Summary
The Customer Insight Generator (Uplizd) is an automated AI workflow that ingests raw customer questions and feedback, processes them through Perplexity AI, and synthesizes them into high-level business insights. By bridging the gap between front-line support interactions and strategic decision-making, this solution provides product and marketing teams with a single source of truth regarding customer sentiment, feature requests, and market trends, significantly increasing pipeline velocity and data-driven product development.

---

## Demo
![Customer Insight Generator workflow interface showing input processing and insight synthesis](image.png)
**Alt text (SEO-ready):** Customer Insight Generator Uplizd workflow, Perplexity AI integration for business intelligence, automated customer feedback analysis, and actionable insight synthesis.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhL7c6xCQAgEETRj785u4sF/EALwU0I2oU3M5O5SgghhBBCCCGEEEIIIYQQQvjP8wJCCCGEEEIIIYQQQvj/D299A20wB25yAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/50065383-cd4e-57d9-a467-1cfba5c69415)

---

## Category
**Primary category:** Customer Intelligence
**Secondary tags:** perplexity, ai workflow, customer insights, business intelligence, feedback analysis, data synthesis, composio, product strategy.
This solution leverages advanced AI search capabilities to convert unstructured customer communication into structured strategic intelligence.

---

## Who is this for?
This solution is designed for teams that need to turn high-volume customer interactions into clear, strategic roadmaps.

*   **Product Managers**
    *   Identify recurring feature requests and pain points directly from user inquiries to prioritize the product roadmap.
*   **Customer Success Leads**
    *   Synthesize common support themes to improve self-service documentation and reduce ticket volume.
*   **Marketing Strategists**
    *   Extract market sentiment and competitive intelligence from customer feedback to refine messaging and positioning.
*   **Data Analysts**
    *   Automate the categorization and reporting of qualitative customer data to provide stakeholders with consistent, actionable metrics.

---

## Features
- **Real-time Insight Synthesis**
  Automatically processes incoming customer questions using Perplexity AI to extract key themes and actionable takeaways.
- **Automated Data Categorization**
  Uses the Composio Toolset to organize insights by topic, urgency, and product area for streamlined reporting.
- **Seamless CRM Integration**
  Connects with your existing CRM to log insights directly against relevant accounts or support tickets.
- **Trend Identification**
  Detects emerging patterns in customer feedback over time, helping teams stay ahead of market shifts.
- **Actionable Output Generation**
  Delivers concise summaries and recommended next steps, ensuring insights are ready for immediate team review.

---

## Use Cases
**Product Roadmap Prioritization**
*   Aggregating feature requests from support tickets to determine the most requested functionality.
*   Identifying specific user friction points that correlate with churn risk.

**Competitive Intelligence**
*   Extracting mentions of competitor products from customer feedback to benchmark market perception.
*   Monitoring shifts in industry terminology and user expectations via real-time web search.

**Customer Experience Optimization**
*   Analyzing sentiment trends following new product releases or feature updates.
*   Generating automated weekly reports on top customer pain points for executive review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Insight Generator template from the solution library.
3. Authenticate your Perplexity AI and CRM credentials within the connection manager.
4. Ensure nodes are properly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw customer inquiries or feedback logs.
*   **Agent**: Executes the reasoning logic to interpret and summarize the input.
*   **Composio Toolset**: Connects to external search and CRM tools to validate and store insights.
*   **Chat Output**: Displays the final synthesized insight report.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
*   `Analyze the last 10 customer support tickets for recurring feature requests.`
*   `What are the top 3 pain points mentioned in recent feedback regarding our onboarding process?`
*   `Compare current customer sentiment on our mobile app versus our desktop platform.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the primary reasoning engine.
*   **Role**: Senior Product Analyst.
*   **Instruction Pattern**: 
    *   Maintain an objective, data-driven tone.
    *   Prioritize insights that have a direct impact on product usability.
    *   Cite specific customer feedback examples when summarizing trends.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Perplexity AI and relevant CRM API keys are active.
*   **Connection Scope**: Grant read access to support ticket databases and write access to your project management or CRM tools.

### 3) Tool Availability
*   **Search Tools**: Perplexity AI for real-time market research and trend verification.
*   **Data Tools**: CRM connectors for logging insights and retrieving customer context.
*   **Utility Tools**: Text summarization and categorization modules for structured output.

---

## Related Solutions
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate comprehensive reports on account health and intelligence.
*   [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Automate 24/7 support responses using AI-driven knowledge retrieval.
*   [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new sales opportunities based on customer signals.
