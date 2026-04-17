# Personalized Video Sales Outreach Agent (Uplizd) - Scale high-converting video outreach with AI

## Summary
The Personalized Video Sales Outreach Agent automates the creation and distribution of tailored video messages, enabling sales teams to deliver high-touch engagement at scale. By integrating AI-driven personalization with video generation platforms, this workflow ensures every prospect receives a relevant, human-like video, significantly increasing response rates and pipeline velocity.

---

## Demo
![Personalized Video Sales Outreach Agent workflow showing HeyGen integration and lead data processing](image.png)
**Alt text (SEO-ready):** Personalized Video Sales Outreach Agent workflow using Uplizd, HeyGen, and Composio for automated sales outreach and lead engagement.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTA6s1H+GgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAK+A8DA8N/ID4DxP8H4j9A/A+I/wDxPyD+B8T/gPgfEP8D4n9A/A+I/wDxPyD+B8T/gPgfEAAAlw4D11/J0GAAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/d1abf9cf-8383-5f65-b562-d0ae4de3da5b)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** `video outreach`, `heygen`, `sales`, `lead engagement`, `composio`, `ai workflow`, `personalization`, `outbound`
This solution bridges the gap between CRM lead data and personalized video content to streamline high-touch outbound sales strategies.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to humanize their digital outreach and drive higher conversion rates.

*   **Sales Development Rep (SDR):**
    *   Automates the creation of personalized video intros to bypass cold email fatigue.
*   **Account Executive (AE):**
    *   Delivers high-value video summaries for key stakeholders during the middle of the sales cycle.
*   **Marketing Operations Manager:**
    *   Ensures consistent brand messaging across automated video assets at scale.
*   **Growth Lead:**
    *   Optimizes outbound conversion metrics by leveraging AI-generated video personalization.

---

## Features
- **AI-Driven Personalization**
  Uses LLMs to analyze prospect data and generate custom scripts that feel authentic and relevant.
- **Automated Video Generation**
  Seamlessly triggers HeyGen video production via the Composio Toolset to create professional-grade video messages.
- **CRM Integration**
  Syncs outreach status and video links directly back to your CRM to maintain a single source of truth.
- **Real-time Triggering**
  Initiates video creation based on specific CRM events, such as new lead assignment or deal stage changes.
- **Scalable Outreach**
  Handles high-volume video requests without manual intervention, ensuring consistent follow-up speed.

---

## Use Cases
**Cold Outreach Acceleration**
*   Generate personalized video intros for new inbound leads within minutes of form submission.
*   Automate video follow-ups for prospects who have opened an email but haven't booked a meeting.

**Account-Based Marketing (ABM)**
*   Create custom video summaries for key decision-makers at target accounts using specific pain points.
*   Produce personalized "thank you" videos after high-level discovery calls to maintain momentum.

**Pipeline Re-engagement**
*   Send personalized video check-ins to stalled opportunities to re-ignite interest.
*   Deliver video-based product updates tailored to the specific features a prospect previously inquired about.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the solution JSON file provided in this repository.
3. Connect your required API credentials (HeyGen, CRM, etc.) via the Composio dashboard.
4. Ensure nodes are correctly mapped and all API keys are validated in the builder.

### 2) Setup the Nodes
*   **Chat Input:** Receives prospect data and outreach intent from your CRM or manual trigger.
*   **Agent:** Processes the input, crafts the personalized script, and determines the video parameters.
*   **Composio Toolset:** Executes the HeyGen API calls to generate and render the video asset.
*   **Chat Output:** Delivers the final video URL and status report back to the user or CRM.

### 3) Run the Flow
Access the Playground to test your outreach logic with live data.
*   `Create a 30-second personalized video for John Doe at Acme Corp focusing on our new API integration.`
*   `Generate a follow-up video for a stalled lead in the 'Discovery' stage mentioning their interest in data hygiene.`
*   `Draft and trigger a personalized video outreach for all leads assigned to me today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative director, ensuring the script aligns with your brand voice.
*   Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for best script quality.
*   Provide clear instructions on tone, length, and mandatory prospect data points.
*   Ensure the agent is instructed to output JSON-formatted parameters for the video generation tool.

### 2) Composio Toolset Node
*   **API Key:** Ensure your HeyGen and CRM API keys are active in the Composio environment.
*   **Connection Scope:** Grant the toolset read/write access to your CRM (e.g., Salesforce, HubSpot) and HeyGen video generation endpoints.

### 3) Tool Availability
*   **CRM Connector:** For fetching prospect details and updating outreach status.
*   **HeyGen API:** For script-to-video generation and asset management.
*   **Notification Service:** For alerting the sales rep once the video is ready for review.

---

## Related Solutions
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and follow-up cadences.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain multi-platform data consistency for better outreach targeting.
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-crustdata/README.md) — Enrich prospect data to fuel better video personalization.
