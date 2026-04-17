# Multilingual Content Moderator (Uplizd) - Automated global content safety and language detection

## Summary
The Multilingual Content Moderator is an intelligent Uplizd workflow designed to automate the detection, classification, and moderation of user-generated content across 364 language combinations. By leveraging the Rosette Text Analytics engine, this solution provides global teams with a single source of truth for content safety, ensuring brand integrity and regulatory compliance while significantly reducing the manual overhead of multilingual moderation pipelines.

---

## Demo
![Multilingual Content Moderator workflow showing language detection and moderation nodes](image.png)
**Alt text (SEO-ready):** Multilingual Content Moderator workflow on Uplizd featuring Rosette Text Analytics for automated global content safety and language detection.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f41ba0be-fd5e-5abb-919f-37e9dab33bd1)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content moderation, multilingual, rosette text analytics, ai workflow, brand safety, compliance, global marketing, composio
- This solution bridges the gap between global user engagement and brand safety by automating language-specific content filtering.

---

## Who is this for?
This solution is designed for global organizations that need to maintain high standards of content quality across diverse linguistic markets.

- **Community Managers**
    - Automate the triage of flagged content to maintain safe and welcoming digital spaces.
- **Compliance Officers**
    - Ensure all user-generated content adheres to regional legal standards and internal brand guidelines.
- **Global Marketing Leads**
    - Protect brand reputation by preventing inappropriate content from appearing in multilingual campaigns.
- **Support Operations Managers**
    - Reduce ticket volume by filtering out spam and abusive content before it reaches human agents.

---

## Features
- **Multi-Language Support**
    - Seamlessly process and moderate content across 364 language combinations using advanced linguistic analysis.
- **Automated Sentiment Analysis**
    - Detect negative or harmful intent within user posts to trigger immediate moderation actions.
- **Real-Time Content Filtering**
    - Integrate directly with your existing platforms via the Composio Toolset to block or flag content in milliseconds.
- **Customizable Moderation Rules**
    - Define specific thresholds for toxicity, profanity, and off-topic content based on your unique brand policy.
- **Unified Reporting Dashboard**
    - Centralize moderation logs and language distribution data for better oversight of global content health.

---

## Use Cases
**Brand Safety & Reputation Management**
- Automatically flag and hide hate speech or offensive content in international comment sections.
- Ensure that marketing copy and user reviews align with local cultural norms and brand standards.

**Regulatory & Compliance Monitoring**
- Identify and redact PII (Personally Identifiable Information) in multilingual support tickets to meet GDPR/CCPA requirements.
- Maintain a clean audit trail of moderated content for compliance reporting in highly regulated markets.

**Operational Efficiency**
- Filter out high volumes of spam or bot-generated content across multiple languages to clear the queue for human moderators.
- Automatically categorize incoming multilingual feedback by language and sentiment for faster routing to the correct regional team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Connect your Rosette Text Analytics API credentials within the integration settings.
4. Ensure nodes are correctly mapped to your target communication channels and moderation databases.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw user-generated content from your website or social media feed.
*   **Agent**: Analyzes the input text, performs language detection, and applies moderation logic.
*   **Composio Toolset**: Executes the API calls to Rosette Text Analytics and updates your database.
*   **Chat Output**: Returns the moderation status and classification result to your dashboard or notification system.

### 3) Run the Flow
Use the Playground to test the moderation engine:
- `Analyze this comment for profanity: "This product is absolutely terrible and I hate it."`
- `Detect the language and check for compliance in this text: "¡Este servicio es increíblemente lento y decepcionante!"`
- `Moderate the following input for brand safety: "Check out my spam link at [URL] for free stuff!"`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for the moderation pipeline.
- **Role:** Act as a global content moderator with expertise in linguistic nuance and brand safety.
- **Instruction Pattern:**
    - Detect the primary language of the input text before applying moderation filters.
    - Classify content based on predefined toxicity, spam, and PII categories.
    - Provide a clear "Approve" or "Reject" status based on the Rosette analysis results.

### 2) Composio Toolset Node
- **API Key:** Provide your Rosette Text Analytics API key in the configuration panel.
- **Connection Scope:** Ensure the toolset has read/write permissions for your content management system or database.

### 3) Tool Availability
- **Language Identification:** Detects the source language for accurate processing.
- **Toxicity Scoring:** Evaluates the severity of harmful content.
- **Entity Extraction:** Identifies sensitive information for potential redaction.
- **Content Classification:** Categorizes input into spam, promotional, or user-feedback buckets.

---

## Related Solutions
- [../abuse-report-manager-by-abuselpdb/README.md](../abuse-report-manager-by-abuselpdb/README.md) - Manage and track abuse reports efficiently.
- [../247-customer-support-chatbot-by-botstar/README.md](../247-customer-support-chatbot-by-botstar/README.md) - Automate customer support interactions 24/7.
- [../accessibility-compliance-monitor-by-alttext-ai/README.md](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure your content meets global accessibility standards.
