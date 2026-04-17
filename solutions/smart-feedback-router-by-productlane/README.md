# Smart Feedback Router (Uplizd) - Intelligent customer feedback prioritization and routing

## Summary
The Smart Feedback Router is an automated Uplizd AI workflow that ingests, analyzes, and categorizes customer feedback from Productlane. By leveraging intelligent sentiment analysis and urgency scoring, the solution ensures that critical product insights are routed to the correct engineering or product teams in real-time, reducing manual triage time and accelerating product development cycles.

---

## Demo
![Smart Feedback Router workflow showing feedback ingestion, sentiment analysis, and routing to Productlane](image.png)
**Alt text (SEO-ready):** Smart Feedback Router workflow by Uplizd, demonstrating automated customer feedback sentiment analysis, urgency prioritization, and Productlane integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/40ad2a3c-7839-5f2d-aeaa-cb784ca17205)

---

## Category
- **Primary category:** Product operations
- **Secondary tags:** productlane, feedback, sentiment analysis, routing, automation, customer insights, ai workflow, product management
- This solution streamlines the feedback loop by connecting raw user input to actionable product development tasks.

---

## Who is this for?
This solution is designed for product teams looking to eliminate feedback bottlenecks and maintain a clear pulse on user needs.

- **Product Managers**
    - Automate the categorization of high-volume feedback to focus on high-impact roadmap items.
- **Customer Success Leads**
    - Ensure that urgent customer pain points are flagged and addressed by the product team immediately.
- **Engineering Managers**
    - Receive pre-triaged, actionable feedback tickets that are already mapped to specific product areas.
- **Product Operations Specialists**
    - Maintain a clean, organized feedback repository by removing noise and duplicates automatically.

---

## Features
- **Automated Sentiment Analysis**
    - Uses advanced LLMs to detect emotional tone and urgency in raw customer feedback.
- **Intelligent Routing Logic**
    - Dynamically assigns feedback to relevant product squads based on keyword mapping and topic extraction.
- **Productlane Integration**
    - Seamlessly syncs processed feedback directly into Productlane boards for immediate visibility.
- **Real-time Priority Scoring**
    - Assigns a numerical urgency score to every entry, ensuring critical bugs or feature requests rise to the top.
- **Noise Reduction Filters**
    - Automatically filters out generic praise or non-actionable comments to keep your backlog focused.

---

## Use Cases
**Feedback Triage**
- Automatically route feature requests to the product roadmap while flagging urgent bugs for engineering.
- Filter out duplicate feedback entries to maintain a single source of truth for user requirements.

**Customer Sentiment Tracking**
- Identify trending negative sentiment regarding specific features to trigger proactive support outreach.
- Aggregate positive feedback to highlight successful product launches and user satisfaction trends.

**Product Roadmap Alignment**
- Map incoming feedback to specific product modules to ensure development efforts align with user demand.
- Generate weekly summaries of top-requested features based on processed feedback volume and urgency.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Smart Feedback Router.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Productlane API credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw feedback text from your support channels or feedback forms.
- **Agent**: Analyzes the input for sentiment, urgency, and topic classification.
- **Composio Toolset**: Executes the API calls to push the structured data into Productlane.
- **Chat Output**: Confirms the successful routing and categorization of the feedback.

### 3) Run the Flow
Use the Playground to test your routing logic with these prompts:
- `Analyze this feedback: "The new dashboard export button is broken and I can't get my reports."`
- `Process this request: "It would be great if we could integrate with Slack for notifications."`
- `Route this feedback: "I love the new UI, but the font size is a bit small on mobile devices."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain of the workflow.
- Set the system prompt to prioritize "Urgency" and "Product Area" extraction.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5) for accurate sentiment classification.
- Define a strict output schema to ensure the Composio Toolset receives clean, structured data.

### 2) Composio Toolset Node
- Provide your Productlane API key to enable read/write access to your feedback boards.
- Ensure the connection scope includes `feedback:write` and `project:read` permissions.

### 3) Tool Availability
- **Productlane API**: For creating and updating feedback items.
- **Sentiment Analysis Tool**: For calculating urgency scores based on text patterns.
- **Categorization Engine**: For mapping feedback to specific product tags.

---

## Related Solutions
- [Widget Experience Optimizer](../widget-experience-optimizer-by-productlane/README.md) — Enhance user engagement through automated widget interaction analysis.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather deep account insights to inform product feedback prioritization.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the performance and efficiency of your automated product operations.
