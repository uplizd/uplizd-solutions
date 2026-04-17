# Sales Call Analyzer (Uplizd) - Automate insights and conversion tracking from voice intelligence

## Summary
The Sales Call Analyzer (Uplizd) workflow leverages advanced voice intelligence to transcribe, analyze, and extract actionable insights from sales conversations. By integrating directly with your communication stack, this solution identifies key objection patterns, sentiment shifts, and buying signals, providing a single source of truth for sales teams to improve pipeline velocity and coaching efficacy.

---

## Demo
![Sales Call Analyzer workflow showing transcription, sentiment analysis, and CRM update nodes](image.png)
**Alt text (SEO-ready):** Sales Call Analyzer Uplizd workflow for automated voice intelligence, CRM data sync, and sales conversation analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8faa158c-597c-56de-9017-58cf77e4576f)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** sales, voice intelligence, crm, conversation intelligence, pipeline, ai workflow, composio, coaching
This solution bridges the gap between raw audio data and actionable CRM intelligence to streamline sales operations.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to turn every customer conversation into a data-driven opportunity.

- **Sales Managers**
    - Automate call reviews and identify coaching opportunities for underperforming reps.
- **Account Executives**
    - Instantly generate follow-up summaries and action items after every discovery call.
- **Revenue Operations (RevOps)**
    - Ensure consistent data hygiene by mapping call insights directly to CRM opportunity fields.
- **Sales Enablement Specialists**
    - Track objection trends across the team to refine messaging and sales collateral.

---

## Features
- **Automated Transcription**
    - Converts voice recordings into structured text using high-fidelity speech-to-text engines.
- **Sentiment & Intent Analysis**
    - Detects emotional shifts and buying intent throughout the call using advanced LLM analysis.
- **CRM Integration**
    - Automatically pushes call summaries and key takeaways into your CRM via the Composio Toolset.
- **Action Item Extraction**
    - Identifies and logs follow-up tasks, ensuring no prospect request is missed.
- **Objection Tracking**
    - Categorizes common sales objections to help teams proactively address customer concerns.

---

## Use Cases
**Pipeline Acceleration**
- Automatically update deal stages in the CRM based on positive buying signals detected during a call.
- Generate personalized follow-up emails for prospects based on specific pain points discussed.

**Sales Coaching**
- Flag calls where specific competitor mentions occurred for targeted manager review.
- Analyze talk-to-listen ratios and question quality to improve rep performance over time.

**Data Hygiene**
- Sync call notes directly to the relevant contact or account record to maintain a clean history.
- Standardize the format of meeting summaries across the entire sales organization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Sales Call Analyzer.
2. Click "Import Flow" to add the workflow to your workspace.
3. Connect your required API credentials for your voice provider and CRM.
4. Ensure nodes are correctly linked from the input trigger to the final output destination.

### 2) Setup the Nodes
- **Chat Input**: Receives raw audio file or transcription text from your sales platform.
- **Agent**: Analyzes the content for sentiment, objections, and key action items.
- **Composio Toolset**: Executes CRM updates and creates tasks based on agent findings.
- **Chat Output**: Delivers a structured summary report to your team’s communication channel.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Analyze the last call for 'Acme Corp' and update the CRM with the primary objection mentioned.`
- `Extract all action items from this transcript and create tasks for the account owner.`
- `Summarize the sentiment of the prospect and suggest a follow-up strategy for the next meeting.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized Sales Intelligence Analyst.
- Focus on extracting objective facts and sentiment indicators.
- Maintain a professional, concise tone for all generated summaries.
- Prioritize identifying actionable next steps over general conversation fluff.

### 2) Composio Toolset Node
Requires an active API key for your CRM (e.g., Salesforce, HubSpot) and appropriate read/write scopes to update deal records and tasks.

### 3) Tool Availability
- **CRM Connector**: For updating deal stages, notes, and contact fields.
- **Task Manager**: For creating follow-up reminders and action items.
- **Notification Service**: For alerting sales managers of high-priority deal signals.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-ups to keep deals moving.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across platforms with conflict resolution.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new sales opportunities automatically.
