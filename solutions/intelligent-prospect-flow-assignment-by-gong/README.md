# Intelligent Prospect Flow Assignment (Uplizd) - Automated lead routing based on Gong call intelligence

## Summary
The Intelligent Prospect Flow Assignment workflow leverages Uplizd and Gong call intelligence to automatically categorize and route prospects into the most effective engagement pipelines. By analyzing conversation transcripts in real-time, this solution ensures that high-intent leads are prioritized and assigned to the correct sales motion, drastically reducing manual data entry and increasing pipeline velocity.

---

## Demo
![Intelligent Prospect Flow Assignment dashboard showing automated routing logic based on Gong call sentiment and keyword analysis](image.png)
**Alt text (SEO-ready):** Intelligent Prospect Flow Assignment dashboard showing automated routing logic based on Gong call sentiment and keyword analysis for Uplizd sales automation workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/4db22cd3-3797-57a9-8e8c-f975a60fdd3b)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, gong, lead routing, sales intelligence, pipeline management, composio, ai workflow, data sync
- This solution bridges the gap between conversation intelligence and CRM execution to streamline lead lifecycle management.

---

## Who is this for?
This solution is designed for revenue teams looking to eliminate manual lead triage and ensure every prospect receives a tailored follow-up experience.

- **Sales Operations Manager**
    - Automates complex routing rules to ensure leads are assigned to the right AE without manual intervention.
- **Account Executive**
    - Receives qualified leads with pre-populated context from Gong calls, allowing for faster deal progression.
- **Revenue Operations (RevOps) Lead**
    - Maintains data hygiene and pipeline consistency by syncing call-derived insights directly into the CRM.
- **Sales Development Representative (SDR)**
    - Focuses on high-priority outreach based on real-time sentiment and intent signals captured during discovery.

---

## Features
- **Gong Transcript Analysis**
    - Uses AI to parse call recordings for intent signals, pain points, and budget authority mentions.
- **Automated CRM Routing**
    - Dynamically updates lead status and owner fields in your CRM based on the specific outcome of the call.
- **Real-time Intent Scoring**
    - Assigns a lead score based on conversation depth and engagement markers identified by the agent.
- **Composio Toolset Integration**
    - Seamlessly connects Gong and your CRM (e.g., Salesforce or HubSpot) to execute field updates instantly.
- **Customizable Routing Logic**
    - Easily adjust thresholds for what constitutes a "hot" lead versus a "nurture" lead within the agent node.

---

## Use Cases
**Lead Prioritization**
- Automatically flag prospects as "High Priority" if they mention specific competitor names or budget approval timelines.
- Move leads to a "Closed-Lost" or "Nurture" queue if the call sentiment indicates a lack of product-market fit.

**Sales Pipeline Hygiene**
- Update the "Next Step" field in your CRM based on the action items discussed during the Gong discovery call.
- Sync meeting summaries directly into the lead activity log to ensure the entire team has a single source of truth.

**Automated Follow-up Assignment**
- Route technical discovery calls to Solutions Engineers while routing commercial-focused calls to Account Executives.
- Trigger automated email sequences in your marketing platform based on the specific product features requested during the call.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Gong and CRM accounts via the Composio Toolset.
3. Configure your routing logic parameters in the Agent node.
4. Ensure nodes are correctly linked from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the Gong call transcript or meeting summary data.
- **Agent**: Analyzes the text to extract intent, sentiment, and key action items.
- **Composio Toolset**: Executes the API calls to update lead fields and assign owners in the CRM.
- **Chat Output**: Confirms the routing action taken and provides a summary of the update.

### 3) Run the Flow
Use the Playground to test your routing logic with these example prompts:
- `Analyze the latest Gong transcript for "Acme Corp" and route to the Enterprise AE team.`
- `Extract action items from the discovery call and update the Salesforce lead record for John Doe.`
- `Identify if the prospect mentioned a budget of over $50k and tag as "High Value" in HubSpot.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a sales intelligence analyst that maps conversation data to CRM actions.
- **Role:** Act as a Sales Operations Assistant that interprets call transcripts.
- **Instruction Pattern:**
    - Identify key buying signals and pain points from the provided transcript.
    - Map these signals to predefined CRM lead stages and owner categories.
    - Output a structured JSON object that the Composio Toolset can use for API execution.

### 2) Composio Toolset Node
- **API Key:** Provide your Gong and CRM API keys within the Composio dashboard.
- **Connection Scope:** Ensure the agent has read access to Gong transcripts and write access to your CRM's Lead/Opportunity objects.

### 3) Tool Availability
- **Gong API:** For fetching call transcripts and metadata.
- **CRM Connector (Salesforce/HubSpot):** For updating lead fields, status, and owner assignments.
- **Data Transformer:** For formatting extracted insights into CRM-compatible field values.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates deep-dive research on prospects to improve discovery call quality.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages pipeline stages and follow-up cadences for active opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes multi-platform data to ensure consistent lead information across your stack.
