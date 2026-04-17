# Contact Research Agent (Uplizd) - Automate verified lead intelligence and account research

## Summary
The Contact Research Agent by Findymail is an automated Uplizd workflow designed to streamline lead generation by sourcing, verifying, and compiling accurate contact information for target accounts. By integrating real-time data retrieval with intelligent filtering, this solution eliminates manual prospecting bottlenecks, ensuring sales and marketing teams have a single source of truth for high-quality, actionable lead data.

---

## Demo
![Contact Research Agent workflow diagram showing data flow from Chat Input to Findymail and CRM output](image.png)
**Alt text (SEO-ready):** Contact Research Agent (Uplizd) workflow diagram for automated lead enrichment, email verification, and CRM data synchronization using Findymail and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d66c86a0-f0ec-5e5c-8887-ac7456e3940e)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead generation, contact enrichment, findymail, sales intelligence, prospect research, data hygiene, composio, ai workflow
- This solution bridges the gap between raw account lists and verified contact data, significantly increasing pipeline velocity for outbound sales teams.

---

## Who is this for?
This solution is built for revenue-focused teams looking to scale their outreach without sacrificing data quality.

- **Sales Development Representative (SDR)**
    - Reduces time spent on manual prospecting by automating the retrieval of verified professional contact details.
- **Growth Marketer**
    - Ensures high deliverability for outbound campaigns by utilizing pre-verified email addresses and contact signals.
- **RevOps Manager**
    - Maintains CRM data hygiene by automating the entry of enriched, standardized contact records directly into the pipeline.
- **Account Executive (AE)**
    - Accelerates account research by instantly surfacing key decision-maker information for targeted outreach strategies.

---

## Features
- **Automated Lead Enrichment**
    - Leverages the Findymail API to instantly fetch and validate professional contact information for specific domains or individuals.
- **Real-time Verification**
    - Filters out invalid or risky email addresses at the point of capture to protect sender reputation and improve campaign performance.
- **Composio Toolset Integration**
    - Seamlessly connects the agent to your existing CRM and communication platforms to push enriched data without manual export/import.
- **Intelligent Data Mapping**
    - Automatically parses unstructured research results into standardized fields for consistent CRM record creation.
- **Scalable Prospecting**
    - Allows for bulk processing of account lists, enabling teams to research hundreds of leads in the time it previously took to research one.

---

## Use Cases
**Outbound Sales Prospecting**
- Automatically research and verify contact information for all leads assigned to a new outbound campaign.
- Identify and append missing decision-maker contact details to existing accounts in your CRM.

**CRM Data Hygiene**
- Periodically scan existing CRM records to verify email deliverability and update outdated contact information.
- Standardize contact formatting across your database to ensure consistent reporting and segmentation.

**Account Intelligence Gathering**
- Quickly compile a list of key stakeholders at target accounts before an initial discovery call.
- Aggregate contact signals to prioritize outreach based on the most accurate and recent professional data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the **Contact Research Agent**.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Findymail API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company domain or prospect name from the user.
- **Agent**: Analyzes the input and triggers the appropriate search and verification logic.
- **Composio Toolset**: Executes the Findymail API calls to retrieve and validate contact data.
- **Chat Output**: Displays the verified contact details and confirms the data has been synced to your CRM.

### 3) Run the Flow
Open the Uplizd Playground and try these prompts:
- `Research and verify the contact information for the marketing team at [Company Domain].`
- `Find the email address for the VP of Sales at [Company Name] and add them to my CRM.`
- `Clean up the contact data for my current list of leads in the 'Prospecting' stage.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your research tasks.
- Use a model capable of structured output (e.g., GPT-4o or Claude 3.5 Sonnet).
- **Instruction pattern:**
    - "You are a professional research assistant; always prioritize verified email addresses over unverified ones."
    - "If a contact is not found, clearly state the limitation rather than hallucinating data."
    - "Format all output as a structured table for easy reading and CRM mapping."

### 2) Composio Toolset Node
- Provide your Findymail API key to enable secure access to the enrichment engine.
- Set the connection scope to allow the agent to read account data and write contact records to your CRM.

### 3) Tool Availability
- **Findymail Search**: Capability to query domains for associated professional contacts.
- **Email Verification**: Capability to ping mail servers to confirm address validity.
- **CRM Write/Update**: Capability to create or patch records in your connected CRM (e.g., Salesforce, HubSpot).

---

## Related Solutions
- [Account Intelligence Gatherer by Dropcontact](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data and identify key decision-makers.
- [Account Research Assistant by Zoominfo](../account-research-assistant-by-zoominfo/README.md) — Deep-dive account research and firmographic data retrieval.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize contact and account data across multiple platforms.
- [Account Research Agent by Onepage](../account-research-agent-by-onepage/README.md) — Streamline account-level research and prospect identification.
