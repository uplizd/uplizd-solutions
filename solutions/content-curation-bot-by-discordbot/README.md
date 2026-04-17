# Content Curation Bot (Uplizd) - Automated Discord message organization and content discovery

## Summary
The Content Curation Bot by Uplizd streamlines community management by automatically monitoring, filtering, and organizing high-value discussions within Discord. By leveraging AI to identify key insights and actionable content, this workflow eliminates manual moderation overhead, ensures critical information is never lost, and maintains a clean, searchable knowledge base for your community or team.

---

## Demo
![Content Curation Bot workflow diagram showing Discord input, AI processing, and content organization](image.png)
**Alt text (SEO-ready):** Content Curation Bot (Uplizd) workflow for automated Discord message filtering, AI-driven insight extraction, and community content management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/034fda83-f2d2-56a2-876f-f6f6e0416be4)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** discord, content curation, community management, ai workflow, automation, knowledge management, composio, social listening.  
This solution bridges the gap between raw community chatter and structured content assets, turning Discord into a high-signal knowledge repository.

---

## Who is this for?
This solution is designed for community leaders and content strategists who need to transform noisy chat environments into organized, actionable intelligence.

* **Community Manager**
    * Automates the identification of top-tier community contributions and recurring user questions.
* **Content Strategist**
    * Extracts high-quality user-generated content to repurpose for newsletters, blogs, or social media.
* **Developer Advocate**
    * Tracks technical feedback and feature requests directly from Discord channels to improve product roadmaps.
* **Support Lead**
    * Ensures that critical support issues or bugs reported in chat are captured and routed to the appropriate tracking systems.

---

## Features
- **Intelligent Message Filtering**
    * Uses AI to distinguish between casual chatter and high-value insights, ensuring only relevant content is curated.
- **Automated Content Tagging**
    * Automatically categorizes messages based on topic, sentiment, or urgency to keep your knowledge base organized.
- **Composio-Powered Integration**
    * Seamlessly connects Discord with external tools like Notion, Slack, or Trello to export curated content instantly.
- **Real-time Insight Extraction**
    * Processes incoming messages in real-time to provide immediate summaries of community trends and pain points.
- **Customizable Curation Logic**
    * Allows users to define specific keywords, user roles, or channel criteria to tailor the bot’s focus to their unique community needs.

---

## Use Cases
**Community Knowledge Base**
* Automatically archiving "Best of" discussions into a searchable Notion database.
* Flagging recurring user questions to build a dynamic FAQ document.

**Content Repurposing**
* Identifying high-engagement community discussions to serve as inspiration for weekly blog posts.
* Extracting user testimonials and positive feedback for marketing collateral.

**Feedback & Support Triage**
* Routing critical bug reports from Discord directly to Jira or GitHub Issues.
* Aggregating feature requests to provide product teams with a prioritized list of community demands.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Connect your Discord account via the Composio integration settings.
3. Configure your target destination (e.g., Notion, Slack, or Google Sheets) within the workflow builder.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives raw message data from your designated Discord channels.
* **Agent**: Analyzes the message intent, sentiment, and relevance using your custom instructions.
* **Composio Toolset**: Executes actions to store, tag, or route the curated content to your external platforms.
* **Chat Output**: Confirms successful processing and provides a summary log of the curated items.

### 3) Run the Flow
Use the Playground to test your curation logic with these prompts:
* `Scan the #general channel for any messages containing feedback about the new dashboard and save them to Notion.`
* `Identify the top 3 most helpful technical answers provided by users today and summarize them for the weekly newsletter.`
* `Monitor for any urgent bug reports in the #support channel and create a ticket in Jira.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent filter for your Discord community.
* **Recommended instruction pattern:**
    * Define the persona: "You are an expert community moderator and content curator."
    * Define the scope: "Only flag messages that provide constructive feedback, technical solutions, or actionable insights."
    * Define the output format: "Always return the curated content in a structured format including the user handle, timestamp, and summary."

### 2) Composio Toolset Node
* Requires a valid Discord API key and the appropriate OAuth scopes to read messages.
* Ensure the connection scope includes `channels.read` and `messages.read` permissions.

### 3) Tool Availability
* **Discord Connector**: For reading channel history and message metadata.
* **Notion/Slack/Jira Connectors**: For exporting curated insights to your preferred productivity stack.
* **Summarization Engine**: For condensing long threads into concise, readable summaries.

---

## Related Solutions
* [../you-tube-content-distribution-agent-by-youtube/README.md](../you-tube-content-distribution-agent-by-youtube/README.md) — Automate the distribution of video content across social channels.
* [../whats-app-feedback-collection-agent-by-wati/README.md](../whats-app-feedback-collection-agent-by-wati/README.md) — Collect and organize user feedback from WhatsApp conversations.
* [../247-customer-support-assistant-by-ai-ml-api/README.md](../247-customer-support-assistant-by-ai-ml-api/README.md) — Provide 24/7 automated support responses based on community knowledge.
