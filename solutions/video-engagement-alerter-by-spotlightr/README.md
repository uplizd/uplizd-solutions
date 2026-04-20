# Video Engagement Alerter (Uplizd) - Real-time prospect tracking and sales follow-up automation

## Summary
The Video Engagement Alerter by Spotlightr is an intelligent Uplizd workflow designed to bridge the gap between video content consumption and sales pipeline velocity. By monitoring viewer activity in real-time, this agent identifies high-intent prospects and triggers immediate notifications or CRM updates, ensuring your team never misses a window to engage with warm leads.

---

## Demo
![Video Engagement Alerter workflow showing real-time viewer tracking and automated CRM notification triggers](image.png)
**Alt text (SEO-ready):** Uplizd video engagement alerter workflow, Spotlightr viewer tracking, automated sales notifications, and CRM lead follow-up integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3fde1b34-db49-51ac-acfe-2d4c50c93646)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** spotlightr, video engagement, lead scoring, sales pipeline, real-time alerts, crm integration, composio, ai workflow
- This solution optimizes the sales funnel by converting passive video views into actionable engagement signals for revenue teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to prioritize outreach based on actual prospect interest.

- **Sales Development Reps (SDRs)**
    - Receive instant alerts when a prospect finishes a product demo video, allowing for perfectly timed follow-up calls.
- **Account Executives (AEs)**
    - Gain visibility into which stakeholders are reviewing proposal videos, helping to identify potential blockers or champions.
- **Marketing Operations Managers**
    - Automate the hand-off of "hot" leads from video content platforms directly into the CRM for faster pipeline movement.
- **Customer Success Managers**
    - Monitor usage of onboarding and training videos to proactively reach out to accounts that may be struggling with specific features.

---

## Features
- **Real-time Engagement Tracking**
    - Automatically detects when a prospect watches a video, providing immediate data on watch time and completion rates.
- **Intelligent Lead Scoring**
    - Assigns priority scores to leads based on their video interaction depth, surfacing the most engaged prospects first.
- **Automated CRM Integration**
    - Uses the Composio Toolset to log video engagement events directly into your CRM, keeping all prospect history in one source of truth.
- **Instant Notification Triggers**
    - Sends automated alerts via Slack, email, or CRM tasks the moment a high-value prospect hits a key engagement milestone.
- **Customizable Engagement Thresholds**
    - Allows users to define specific "trigger" actions, such as watching 80% of a video, to filter out noise and focus on high-intent signals.

---

## Use Cases
**Sales Pipeline Acceleration**
- Trigger an immediate follow-up task in Salesforce when a prospect completes a pricing video.
- Automatically move a lead to the "Engaged" stage in HubSpot after they watch a case study video.

**Account Intelligence Gathering**
- Identify which decision-makers are viewing shared proposal links to better understand account sentiment.
- Aggregate video watch data to build a profile of prospect interests for personalized discovery calls.

**Customer Onboarding Optimization**
- Alert the success team if a new client stops watching a critical "Getting Started" video series.
- Automate check-in emails for users who have completed the full onboarding video curriculum.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Video Engagement Alerter template using the provided solution link.
3. Connect your Spotlightr and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly linked from Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw webhook data from Spotlightr regarding viewer activity.
- **Agent**: Analyzes the viewer data against defined engagement thresholds to determine if an alert is required.
- **Composio Toolset**: Executes CRM updates or notification actions based on the Agent's decision.
- **Chat Output**: Confirms the successful logging of the engagement or the dispatch of the alert.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check if the latest viewer of the "Q4 Product Demo" has watched more than 75% and create a high-priority task for the owner.`
- `Summarize the engagement level of account "Acme Corp" based on their recent video activity.`
- `Notify the sales team if any lead from the "Enterprise" segment completes the "Security Overview" video.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine that interprets viewer behavior.
- Use a model capable of logical reasoning to distinguish between casual viewers and high-intent prospects.
- Instruct the agent to prioritize leads based on pre-defined account tiers.
- Ensure the agent is configured to handle missing CRM data gracefully by defaulting to a generic notification.

### 2) Composio Toolset Node
- Provide your API key to authenticate the connection between Uplizd and your CRM/Notification platforms.
- Set the scope to allow read/write access to lead and task objects to enable automated CRM updates.

### 3) Tool Availability
- **CRM Connector**: For logging engagement events and updating lead status.
- **Notification Service**: For sending real-time alerts to Slack or Email.
- **Data Parser**: For normalizing incoming webhook payloads from Spotlightr.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize prospect data across platforms to maintain a single source of truth.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage pipeline stages and automate follow-ups for stalled opportunities.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather account-level insights to complement video engagement data.
