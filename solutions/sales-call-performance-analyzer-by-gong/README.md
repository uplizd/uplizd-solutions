# Sales Call Performance Analyzer (Uplizd) - Automate sales coaching and call insights

## Summary
The Sales Call Performance Analyzer is an intelligent Uplizd workflow that processes recorded sales conversations to extract actionable insights, identify buying signals, and provide objective performance feedback. By leveraging the Composio Toolset to integrate with call recording platforms like Gong, this solution eliminates manual review bottlenecks, ensuring sales teams maintain high-quality interactions and improve win rates through data-driven coaching.

---

## Demo
![Sales Call Performance Analyzer workflow dashboard showing call transcription analysis and coaching feedback](image.png)
**Alt text (SEO-ready):** Uplizd Sales Call Performance Analyzer workflow dashboard showing automated call transcription analysis, sales coaching insights, and Gong integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/75a81a95-30b9-56d6-8a05-f5af0d1faa78)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales, gong, coaching, conversation intelligence, pipeline, revenue operations, composio, ai workflow
- This solution streamlines revenue operations by turning raw call data into structured performance metrics and coaching opportunities.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their coaching efforts without increasing manual oversight.

- **Sales Managers**
    - Identify coaching gaps and track rep performance trends across the entire team.
- **Sales Enablement Leads**
    - Standardize messaging and ensure best practices are being followed on every discovery call.
- **Account Executives**
    - Receive immediate, objective feedback on talk-to-listen ratios and objection handling.
- **Revenue Operations (RevOps)**
    - Centralize call intelligence to correlate conversation topics with deal velocity and win rates.

---

## Features
- **Automated Transcription Analysis**
    - Uses AI to parse long-form call transcripts into structured summaries and key discussion points.
- **Objection Handling Intelligence**
    - Automatically flags common customer objections and provides suggested responses based on successful historical patterns.
- **Sentiment & Engagement Scoring**
    - Quantifies customer sentiment and engagement levels throughout the call to predict deal health.
- **Action Item Extraction**
    - Identifies follow-up tasks and commitments made during the call, pushing them directly to your CRM.
- **Coaching Feedback Loop**
    - Generates personalized coaching notes for reps, focusing on specific areas for improvement like discovery questions or value proposition delivery.

---

## Use Cases
**Sales Coaching & Training**
- Automatically generate a "scorecard" for every new hire's discovery call to accelerate onboarding.
- Identify top-performing talk tracks used by senior reps to share as templates for the rest of the team.

**Pipeline & Deal Management**
- Flag stalled deals where the customer has expressed specific concerns that haven't been addressed in follow-ups.
- Extract competitor mentions during calls to update the CRM and trigger competitive battlecard alerts.

**Revenue Operations Hygiene**
- Ensure all discovery calls have associated "Next Steps" logged in the CRM to prevent pipeline leakage.
- Sync call-derived data points to custom CRM fields to improve lead scoring accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow."
3. Connect your Gong or call-recording platform credentials via the Composio Toolset.
4. Ensure nodes are correctly mapped and the Agent is authorized to access your CRM.

### 2) Setup the Nodes
- **Chat Input**: Receives the call recording ID or transcript text.
- **Agent**: Analyzes the content against your team's sales playbook and coaching criteria.
- **Composio Toolset**: Executes API calls to fetch call data and update CRM records.
- **Chat Output**: Delivers the final coaching summary and action items to the user.

### 3) Run the Flow
Use the Playground to test your analysis with these example prompts:
- `Analyze the last call for [Prospect Name] and summarize the top 3 objections raised.`
- `Generate a coaching summary for [Rep Name] based on their recent demo call.`
- `Extract all action items from the latest call and update the corresponding deal in Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized Sales Coach, prioritizing objective analysis and constructive feedback.
- **Instruction Pattern:**
    - Focus on identifying "Value-Based" selling moments versus feature-dumping.
    - Maintain a professional, encouraging tone for rep-facing feedback.
    - Prioritize data extraction accuracy for CRM field updates.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key in the node settings.
- **Connection Scope:** Ensure the connection has read-access to call recordings and write-access to your CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- **Call Retrieval:** Fetch transcripts and metadata from Gong or similar platforms.
- **CRM Integration:** Create tasks, update deal stages, and append notes to accounts.
- **Data Formatting:** Standardize output for Slack notifications or email reports.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-ups to maintain pipeline velocity.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new opportunities based on lead signals.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
