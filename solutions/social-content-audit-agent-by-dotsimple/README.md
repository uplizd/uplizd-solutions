# Social Content Audit Agent (Uplizd) - Automated social media performance and compliance auditing

## Summary
The Social Content Audit Agent is an intelligent Uplizd workflow designed to streamline the review, categorization, and optimization of your social media content library. By leveraging AI to scan historical posts and engagement data, this solution ensures brand consistency, identifies high-performing content patterns, and automates the identification of outdated or non-compliant messaging, providing a single source of truth for your marketing operations.

---

## Demo

![Social Content Audit Agent workflow diagram showing content ingestion, AI analysis, and reporting](image.png)

**Alt text (SEO-ready):** Social Content Audit Agent workflow for automated social media content analysis, brand compliance, and performance optimization using Uplizd and Composio.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/10b2f171-9af8-53ce-9866-0c0ea7cbb151)

---

## Category

*   **Primary category:** Marketing operations
*   **Secondary tags:** social media, content audit, brand compliance, marketing automation, content strategy, composio, ai workflow
*   This solution bridges the gap between raw social media data and actionable marketing insights by automating the audit lifecycle.

---

## Who is this for?

This solution is designed for marketing teams looking to maintain brand integrity and content efficacy at scale.

*   **Social Media Manager**
    *   Automates the tedious process of reviewing historical posts for brand voice alignment and outdated campaign messaging.
*   **Content Strategist**
    *   Identifies high-performing content archetypes to inform future editorial calendars and creative direction.
*   **Compliance Officer**
    *   Ensures all public-facing social content adheres to current legal and regulatory guidelines through automated scanning.
*   **Marketing Operations Lead**
    *   Maintains a clean, optimized content library that integrates seamlessly with broader CRM and analytics platforms.

---

## Features

- **Automated Content Scanning**
  Deep-dives into your social media history to extract text, media types, and engagement metrics for comprehensive analysis.
- **Brand Voice Verification**
  Uses AI to score content against your defined brand guidelines, flagging posts that deviate from your established tone.
- **Performance Trend Analysis**
  Correlates content themes with engagement data to highlight what resonates most with your target audience.
- **Compliance & Risk Monitoring**
  Automatically detects outdated offers, broken links, or non-compliant terminology across all social channels.
- **Actionable Optimization Reports**
  Generates structured summaries and recommendations for archiving, updating, or repurposing specific pieces of content.

---

## Use Cases

**Content Library Maintenance**
*   Identify and flag posts containing expired promotional codes or outdated event information.
*   Archive low-engagement content that no longer aligns with current brand positioning.

**Brand Voice & Compliance**
*   Audit historical posts to ensure consistent usage of brand-approved terminology and hashtags.
*   Flag content that may violate updated platform policies or internal regulatory requirements.

**Strategy & Growth**
*   Analyze high-performing posts from the last quarter to identify successful creative patterns.
*   Generate summaries of content performance to present to stakeholders during marketing reviews.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your required social media and analytics accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are authenticated in the settings panel.

### 2) Setup the Nodes
*   **Chat Input:** Receives the audit scope (e.g., date range, specific platforms, or topic filters).
*   **Agent:** Processes the content, applies brand guidelines, and performs the audit logic.
*   **Composio Toolset:** Connects to social media APIs to fetch post data and engagement metrics.
*   **Chat Output:** Delivers the final audit report, including flagged items and optimization suggestions.

### 3) Run the Flow
Use the Playground to test your audit agent with prompts like:
* `Audit all posts from the last 30 days for broken links and outdated promotional offers.`
* `Analyze my top 10 performing posts and identify the common themes that drove engagement.`
* `Check my recent LinkedIn posts against our new brand voice guidelines and flag any deviations.`

---

## Configuration

### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your content library.
*   **Role:** Act as a Senior Social Media Auditor specialized in brand compliance and performance analytics.
*   **Instruction Pattern:**
    *   Prioritize accuracy in identifying specific post IDs and engagement metrics.
    *   Maintain a neutral, objective tone when flagging content for compliance issues.
    *   Provide clear, actionable recommendations for every flagged item.

### 2) Composio Toolset Node
*   **API Key:** Ensure your social media platform API keys are active within the Composio dashboard.
*   **Connection Scope:** Grant read-only access to your social media accounts to ensure secure data retrieval during the audit process.

### 3) Tool Availability
*   **Social Media Fetchers:** Capabilities to pull post content, timestamps, and engagement counts.
*   **Data Analysis Tools:** Functions for sentiment analysis, keyword matching, and trend identification.
*   **Reporting Tools:** Utilities for formatting audit results into CSV or structured text reports.

---

## Related Solutions

*   [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Analyze and improve your video content reach.
*   [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automate personalized follow-ups for your social leads.
*   [Affiliate Program Analytics Agent](../affiliate-program-analytics-agent-by-tapfiliate/README.md) - Track and optimize your affiliate marketing performance.
