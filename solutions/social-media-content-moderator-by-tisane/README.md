# Social Media Content Moderator (Uplizd) - Automated multi-language content safety and compliance

## Summary
The Social Media Content Moderator (Uplizd) is an intelligent AI workflow designed to automatically detect, analyze, and flag toxic or policy-violating content across diverse social platforms. By leveraging the Tisane API via the Composio Toolset, this solution provides community managers and brand safety teams with a single source of truth for content hygiene, significantly reducing manual moderation overhead and ensuring brand integrity in real-time.

---

## Demo
![Social Media Content Moderator workflow interface showing automated text analysis and flagging nodes](image.png)
**Alt text (SEO-ready):** Social media content moderator workflow in Uplizd, featuring automated text analysis, Tisane API integration, and real-time content flagging for brand safety.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6o3987QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lPUElepV1JAAAAEklEQVQ4y2NgGAWjYBSMglEAAAGAAAH0Qz7MAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/1cbf025f-421d-5039-bffb-7f8cd72c4464)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** social media, content moderation, tisane, brand safety, ai workflow, compliance, community management, composio
- This solution streamlines digital community management by automating the detection of harmful content and ensuring adherence to platform-specific safety guidelines.

---

## Who is this for?
This solution is designed for teams responsible for maintaining digital brand reputation and user safety.

*   **Community Manager**
    *   Automates the triage of user comments to focus on high-priority engagement rather than manual moderation.
*   **Brand Safety Officer**
    *   Ensures consistent enforcement of corporate communication policies across global social channels.
*   **Social Media Strategist**
    *   Protects brand equity by preventing toxic interactions from remaining visible on public-facing posts.
*   **Customer Support Lead**
    *   Reduces the volume of abusive tickets by filtering out non-constructive or harmful content before it reaches the support queue.

---

## Features
- **Multi-Language Detection**
    - Identifies toxic content, hate speech, and harassment across dozens of languages using advanced linguistic analysis.
- **Real-Time Content Filtering**
    - Processes incoming social media comments instantly to flag or hide content that violates community standards.
- **Composio Toolset Integration**
    - Seamlessly connects the Uplizd agent with the Tisane API to perform deep semantic analysis on text inputs.
- **Automated Policy Enforcement**
    - Triggers predefined actions, such as flagging for human review or automatic deletion, based on severity scores.
- **Context-Aware Moderation**
    - Distinguishes between constructive criticism and malicious intent to minimize false positives in your moderation pipeline.

---

## Use Cases
**Brand Reputation Management**
*   Automatically flag comments containing profanity or hate speech on high-traffic corporate posts.
*   Monitor brand mentions for negative sentiment that requires immediate PR intervention.

**Community Health Monitoring**
*   Filter out spam and bot-generated comments to keep discussion threads focused and relevant.
*   Identify and escalate recurring harassment patterns targeting specific community members.

**Compliance and Safety**
*   Ensure all user-generated content complies with platform-specific terms of service and legal requirements.
*   Maintain a safe environment for younger audiences by blocking age-inappropriate language in real-time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import Flow" option.
2. Upload the provided solution JSON file to initialize the nodes.
3. Connect your preferred social media accounts and the Tisane API credentials.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw text from social media comments or posts.
*   **Agent**: Evaluates the text against safety criteria and determines the appropriate moderation action.
*   **Composio Toolset**: Executes the Tisane API calls to analyze the content's linguistic and semantic properties.
*   **Chat Output**: Returns the moderation decision, including flags, severity scores, and recommended actions.

### 3) Run the Flow
Use the Playground to test the moderation logic with the following prompts:
* `Analyze this comment for hate speech: "I hate this product and everyone who works there!"`
* `Review this user post for potential policy violations: "Check out my site for cheap deals at [link]."`
* `Flag any profanity in the following text: "This is a [expletive] amazing update!"`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine that interprets the analysis results.
*   Prioritize safety and brand guidelines in every decision.
*   Maintain a neutral, objective tone when reporting moderation status.
*   Always include the severity score provided by the toolset in the final output.

### 2) Composio Toolset Node
*   Requires a valid Tisane API key to function.
*   The connection scope should be set to allow read access to text analysis endpoints.

### 3) Tool Availability
*   **Text Analysis**: Deep linguistic scanning for toxicity, harassment, and hate speech.
*   **Language Identification**: Automatic detection of the input language for accurate processing.
*   **Policy Mapping**: Matching detected content against predefined safety categories.

---

## Related Solutions
* [Abuse Report Manager](../abuse-report-manager-by-abuselpdb/README.md) - Streamline the processing and tracking of abuse reports.
* [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Automate support ticket categorization and routing.
* [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Analyze and improve video content engagement metrics.
