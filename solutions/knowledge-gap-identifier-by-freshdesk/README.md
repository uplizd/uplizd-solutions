# Knowledge Gap Identifier (Uplizd) - Automate support article creation by detecting recurring knowledge gaps

## Summary
The Knowledge Gap Identifier is an intelligent Uplizd workflow that analyzes incoming Freshdesk support tickets to pinpoint recurring user questions that lack corresponding documentation. By leveraging AI to cross-reference ticket content with existing knowledge base articles, this solution helps support teams proactively identify content gaps, reduce ticket volume, and improve self-service resolution rates.

---

## Demo
![Knowledge Gap Identifier workflow dashboard showing ticket analysis and missing article alerts](image.png)
**Alt text (SEO-ready):** Knowledge Gap Identifier Uplizd workflow dashboard showing Freshdesk ticket analysis, AI-driven content gap detection, and automated reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6e0a9526-8dce-599c-92be-6a1d00008a72)

---

## Category
- **Primary category:** Customer Support Operations
- **Secondary tags:** freshdesk, knowledge management, ai workflow, support automation, ticket analysis, content strategy, composio, self-service
- This solution bridges the gap between reactive support ticketing and proactive knowledge base maintenance to ensure your documentation evolves with your customers' needs.

---

## Who is this for?
This solution is designed for support and documentation teams looking to streamline their content creation process based on real-world user data.

- **Support Manager**
    - Reduces ticket volume by identifying and filling documentation gaps that lead to repetitive inquiries.
- **Technical Writer**
    - Gains data-driven insights into which topics require new articles or updates based on actual customer pain points.
- **Customer Success Lead**
    - Improves the overall customer experience by ensuring users have access to accurate, timely self-service resources.
- **Operations Analyst**
    - Tracks the correlation between support ticket trends and knowledge base health to optimize support efficiency.

---

## Features
- **Automated Ticket Analysis**
    - Uses AI to scan incoming Freshdesk tickets in real-time to categorize topics and identify recurring themes.
- **Knowledge Base Cross-Referencing**
    - Automatically checks existing documentation via the Composio Toolset to determine if a relevant article already exists.
- **Gap Detection Alerts**
    - Flags specific topics or user queries that lack sufficient coverage, notifying the content team immediately.
- **Trend Reporting**
    - Aggregates data over time to highlight which product areas are generating the most "unknown" support requests.
- **Seamless Integration**
    - Connects directly to Freshdesk and your knowledge management platform to create a closed-loop feedback system.

---

## Use Cases
**Proactive Content Creation**
- Automatically generate draft outlines for new knowledge base articles when a specific topic spikes in support tickets.
- Identify outdated articles that no longer address current customer questions or product features.

**Support Efficiency Optimization**
- Reduce the time agents spend answering repetitive "how-to" questions by flagging them for immediate documentation.
- Prioritize the content roadmap by focusing on the most frequent user queries that currently have no self-service path.

**Customer Experience Enhancement**
- Ensure that new product features are supported by documentation from day one by monitoring early-stage ticket trends.
- Improve searchability of the knowledge base by aligning article titles and tags with the language customers use in tickets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Freshdesk account and preferred LLM provider within the Uplizd dashboard.
3. Configure the trigger to monitor your primary support ticket queue.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming ticket data and metadata from Freshdesk.
- **Agent**: Processes the ticket content to determine intent and check for documentation gaps.
- **Composio Toolset**: Executes queries against the knowledge base and Freshdesk API to verify article existence.
- **Chat Output**: Delivers the final gap analysis report to your team via email or Slack.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Analyze the last 24 hours of tickets and list any topics that lack a corresponding KB article.`
- `Identify recurring questions about the new billing dashboard that aren't covered in our current documentation.`
- `Generate a summary report of the top 3 knowledge gaps detected this week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting ticket sentiment and intent.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on how to distinguish between a "known issue" and a "knowledge gap."
- Set the temperature to 0.2 to ensure consistent, factual analysis of support data.

### 2) Composio Toolset Node
- Provide your Freshdesk API key and Knowledge Base integration credentials.
- Ensure the connection scope includes read-only access to tickets and read/write access to knowledge base articles.

### 3) Tool Availability
- **Freshdesk API**: For fetching ticket content and metadata.
- **Knowledge Base Connector**: For searching existing articles and verifying content coverage.
- **Notification Service**: For alerting the documentation team when a gap is identified.

---

## Related Solutions
- [247 Customer Support Assistant by AI ML API](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automate routine customer inquiries with AI-driven responses.
- [247 Customer Support Chatbot by Botstar](../247-customer-support-chatbot-by-botstar/README.md) - Deploy a conversational chatbot for instant ticket resolution.
- [WhatsApp Support Triage Agent by Wati](../whats-app-support-triage-agent-by-wati/README.md) - Streamline support triage across WhatsApp channels.
