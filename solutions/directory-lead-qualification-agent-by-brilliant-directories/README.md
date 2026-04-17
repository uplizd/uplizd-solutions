# Directory Lead Qualification Agent (Uplizd) - Automate lead scoring and categorization for directory platforms

## Summary
The Directory Lead Qualification Agent streamlines the intake and assessment of new leads from Brilliant Directories, ensuring high-intent prospects are prioritized for sales outreach. By leveraging AI-driven analysis, this workflow automatically categorizes incoming leads based on profile data, significantly reducing manual administrative overhead and improving pipeline velocity for directory managers and sales teams.

---

## Demo
![Directory Lead Qualification Agent workflow interface showing lead intake, AI scoring, and CRM routing](image.png)
**Alt text (SEO-ready):** Directory Lead Qualification Agent workflow on Uplizd for automated lead scoring, CRM integration, and sales pipeline management using Brilliant Directories.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/2b3e7e13-ae6a-5d56-bf67-4b185a18a968)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** directory, lead qualification, crm, sales pipeline, data hygiene, composio, ai workflow, lead scoring
- This solution bridges the gap between raw directory sign-ups and actionable sales intelligence, ensuring every lead is qualified and routed efficiently.

---

## Who is this for?
This solution is designed for revenue-focused teams managing high-volume directory platforms who need to separate qualified prospects from noise.

- **Sales Operations Manager**
    - Automates lead routing rules to ensure the right sales rep receives high-intent leads instantly.
- **Directory Administrator**
    - Eliminates manual data entry and categorization tasks, allowing for focus on platform growth.
- **Business Development Representative**
    - Receives pre-qualified leads with actionable context, increasing conversion rates on initial outreach.
- **Growth Marketer**
    - Gains insights into lead quality trends to optimize acquisition channels and directory visibility.

---

## Features
- **Automated Lead Scoring**
    - Instantly assigns a quality score to new directory sign-ups based on profile completeness and user intent.
- **Intelligent Categorization**
    - Automatically tags leads into segments (e.g., "Ready for Outreach," "Nurture," "Spam") using AI-driven classification.
- **Real-time CRM Sync**
    - Seamlessly pushes qualified lead data into your CRM via the Composio Toolset for immediate sales action.
- **Customizable Qualification Logic**
    - Adapts to your specific business criteria, allowing you to define what constitutes a "qualified" lead for your directory.
- **Pipeline Velocity Tracking**
    - Reduces the time-to-contact by eliminating manual review cycles for incoming directory registrations.

---

## Use Cases
**Lead Prioritization**
- Automatically flag high-value business profiles that meet specific revenue or industry criteria.
- Route low-intent or incomplete profiles to a automated nurture sequence instead of a sales queue.

**Data Hygiene & Enrichment**
- Standardize lead information formats across the directory database to ensure consistent CRM records.
- Detect and flag duplicate or fraudulent directory submissions before they reach the sales team.

**Sales Outreach Optimization**
- Trigger personalized follow-up tasks in the CRM based on the specific category assigned to the lead.
- Provide sales reps with a summary of the lead's directory activity to facilitate more relevant discovery calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Directory Lead Qualification Agent template from the marketplace.
3. Connect your Brilliant Directories API credentials and your target CRM.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data payloads from your directory platform.
- **Agent**: Analyzes lead attributes against your qualification criteria using LLM logic.
- **Composio Toolset**: Executes the API calls to update lead status and sync data to your CRM.
- **Chat Output**: Confirms the qualification status and logs the action for audit purposes.

### 3) Run the Flow
Use the Playground to test your qualification logic with these prompts:
- `Qualify the latest lead from the directory and assign a priority score.`
- `Categorize the new sign-up based on their industry and profile completeness.`
- `Sync the qualified lead to the CRM and notify the sales team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your lead data.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on your specific "Ideal Customer Profile" (ICP).
- Define strict output formats for the qualification tags to ensure CRM compatibility.

### 2) Composio Toolset Node
- Authenticate with your CRM (e.g., Salesforce, HubSpot) via the Composio dashboard.
- Ensure the connection scope includes read/write access to lead and contact objects.

### 3) Tool Availability
- **CRM Connector**: For pushing qualified lead objects.
- **Directory API**: For fetching and validating user profile data.
- **Notification Service**: For alerting sales teams via Slack or Email.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data for better lead qualification.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep dive into prospect background for personalized outreach.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent lead data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score opportunities identified from qualified leads.
