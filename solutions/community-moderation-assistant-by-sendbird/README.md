# Community Moderation Assistant (Uplizd) - Automated community safety and user management

## Summary
The Community Moderation Assistant (Uplizd) leverages AI-driven workflows to automate content moderation and user management within Sendbird-powered community channels. By integrating real-time monitoring with intelligent response logic, this solution helps community managers maintain high engagement standards, enforce community guidelines, and reduce manual oversight, ensuring a safe and healthy environment for all users.

---

## Demo
![Community Moderation Assistant workflow showing Sendbird integration and automated moderation logic](image.png)
**Alt text (SEO-ready):** Community Moderation Assistant workflow for Sendbird, featuring Uplizd AI-driven moderation, automated user management, and real-time content filtering.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhL7c5BDQAwDAOx/648sE8gQfBwT0qS1H2q1wIAAMB/BwAAwH8HAAAAvwMAAAD/HwAAAP8fAAAAvwMAAAD/HwAAAP8fAABgBwAA8g==)](https://uplizd.ai/solutions/cf859de5-7fb4-5b35-a2d4-c219f2969966)

---

## Category
**Primary category:** Community Operations
**Secondary tags:** community, moderation, sendbird, trust and safety, user management, ai workflow, composio, automated moderation.
This solution streamlines community health by automating the detection and mitigation of policy-violating content within Sendbird channels.

---

## Who is this for?
This solution is designed for teams managing high-traffic digital spaces who need to balance engagement with safety.

*   **Community Manager**
    *   Reduces time spent manually reviewing flagged messages and user reports.
*   **Trust & Safety Lead**
    *   Ensures consistent enforcement of community guidelines across all channels.
*   **Customer Support Agent**
    *   Automatically escalates complex moderation issues that require human intervention.
*   **Product Operations Manager**
    *   Maintains platform hygiene and improves user retention through proactive moderation.

---

## Features
- **Real-time Content Filtering**
    Automatically scans incoming messages for prohibited language or spam using AI-driven analysis.
- **Automated User Sanctions**
    Triggers immediate actions like muting or banning users based on configurable violation thresholds.
- **Sendbird Integration**
    Seamlessly connects with Sendbird APIs via the Composio Toolset to manage channel state and user permissions.
- **Intelligent Escalation Logic**
    Routes suspicious activity to human moderators when confidence scores fall below a defined threshold.
- **Audit Log Generation**
    Maintains a detailed record of all moderation actions taken, providing transparency for compliance reporting.

---

## Use Cases
**Proactive Safety Enforcement**
*   Automatically flag and hide messages containing hate speech or harassment in real-time.
*   Enforce "no-link" policies in specific channels to prevent phishing and spam distribution.

**User Lifecycle Management**
*   Automatically mute users who repeatedly violate community guidelines after a set number of warnings.
*   Grant temporary "trusted" status to long-term members to bypass strict automated filters.

**Operational Efficiency**
*   Summarize daily moderation activity for community leads to identify recurring behavioral trends.
*   Automate the onboarding welcome message and guideline acknowledgment check for new channel members.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Community Moderation Assistant template from the solution library.
3. Authenticate your Sendbird account within the Composio Toolset configuration.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw message data and metadata from Sendbird channels.
*   **Agent**: Processes content against safety guidelines and determines the appropriate moderation action.
*   **Composio Toolset**: Executes API calls to Sendbird to mute, ban, or delete messages.
*   **Chat Output**: Confirms the moderation action taken or logs the event for internal review.

### 3) Run the Flow
Use the Playground to test your moderation logic with these example prompts:
*   `"Check the latest message in channel #general for policy violations."`
*   `"Mute user ID 12345 for spamming promotional links."`
*   `"Provide a summary of all moderation actions taken in the last 24 hours."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central decision-maker for content safety.
*   Analyze message sentiment and intent against the provided community guidelines.
*   Maintain a neutral, objective tone when logging moderation decisions.
*   Prioritize safety by defaulting to "flag for review" if the content is ambiguous.

### 2) Composio Toolset Node
Connect your Sendbird API key to the Composio Toolset to enable direct channel management. Ensure the connection scope includes `channel:write` and `user:manage` permissions.

### 3) Tool Availability
*   **Sendbird Message API**: For retrieving and deleting message content.
*   **Sendbird User API**: For managing mute, ban, and member status.
*   **Moderation Log Service**: For recording actions taken by the agent.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) — Automated customer support triage and resolution.
- [abuse-report-manager-by-abuselpdb](../abuse-report-manager-by-abuselpdb/README.md) — Centralized management for abuse reports and incident tracking.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) — Intelligent triage for support tickets via WhatsApp.
