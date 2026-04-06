

# CRM Data Quality Agent Flow (Uplizd) - Validate, Clean & Enrich CRM Data Automatically

## Summary
A Uplizd AI workflow that receives user input, routes decisions via a CRM Data Quality Agent, executes tools, and returns cleaned CRM-ready output.

---

## Demo

![Uplizd CRM Data Quality Agent Flow with Composio toolset, agent decision node, chat input, and chat output](image.png)

**Alt text (SEO-ready):** Uplizd CRM Data Quality Agent flow integrating Composio toolset to validate and clean CRM data from chat input to chat output.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/f11a0699-75d6-515a-8877-1e1d7a3625ba/)

---
## Who is this for?
This workflow is built for teams and individuals who want to maintain a "Single Source of Truth" without the manual grunt work:

- Sales Operations (SalesOps) & RevOps

    - Keep your pipeline clean and ensure sales reps are working with accurate, high-quality lead data.

- Marketing Managers

    - Reduce email bounce rates and improve campaign segmentation by validating contact info before hitting "Send."

- CRM Administrators

    - Automate the tedious tasks of deduplication, formatting, and standardizing records across Salesforce, HubSpot, or Pipedrive.

- Small Business Owners & Startups

    - Leverage enterprise-grade data cleaning tools without needing a dedicated data entry team.

- Data Engineers & Analysts

    - Quickly prototype or automate data validation pipelines using a flexible, AI-driven modular architecture.

---

## Features

- **AI Agent Decision Engine**  
  Uses an LLM-based agent to analyze user requests and decide which action/tool to execute.

- **Tool Execution via Composio**  
  Integrates with Composio Toolset to trigger external actions (API-based automations).

- **Structured Input → Process → Output Flow**  
  Chat Input is routed to the agent, processed through tool calls, and returned as Chat Output.

- **CRM Data Quality Focused**  
  Designed for cleaning, validating, enriching, and standardizing CRM datasets.

- **Modular Uplizd Architecture**  
  Components can be swapped (model, toolset, output format) without rebuilding the entire workflow.

---

## Use Cases

- **Validate CRM records**
  - Detect missing fields (email, phone, company name)
  - Flag invalid formats (wrong email pattern, phone length)

- **Standardize CRM data**
  - Normalize company names
  - Standardize country/state fields
  - Clean duplicated whitespace and casing issues

- **Deduplicate customer records**
  - Identify potential duplicates based on email/phone/name similarity

- **Enrich CRM lead profiles**
  - Add metadata such as company industry, size, or domain (depending on tool availability)

- **Automate CRM support operations**
  - Route requests like “update lead status” or “check customer info” through agent + tool execution


---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On the Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
5. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Composio Toolset**
   - **Agent**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow structure:

- **Chat Input** → sends user request into the system
- **Agent** → interprets the request and chooses actions
- **Composio Toolset** → provides callable tools/APIs
- **Chat Output** → displays final response to the user

### 3) Run the Flow
1. Click **Playground** to open Chat Interface
2. Enter a CRM-related request in Chat Input, for example:
   - `"Check if this email is valid: john@@gmail.com"`
   - `"Clean and standardize this customer record"`
   - `"Find duplicates for this lead list"`

3. Review output in Chat Output.

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node uses:

- **Model:** `gpt-4o-mini` (default in the current flow)
- **Instruction Prompt:** `You are a CRM Data Quality Agent...`

Recommended instruction pattern:

- Validate data accuracy
- Standardize formats
- Provide structured output
- Call tools only when needed
- Return clean CRM-ready results

Example agent instruction snippet:

```txt
You are a CRM Data Quality Agent.
Your job is to validate, clean, deduplicate, and enrich CRM data.
When needed, call available tools to verify data or perform updates.
Always return output in a structured and actionable format.
````

---

### 2) Composio Toolset Node

The Composio node requires:

* **Composio API Key** (required)

Steps:

1. Open **Composio Toolset** node
2. Paste your **Composio API Key**
3. Wait for tools/actions to load successfully

If you see `Error loading actions`, check:

* API key is valid
* Network access is allowed
* Composio workspace permissions are correct

---

### 3) Tool Availability

Once Composio actions are loaded, the agent can call tools such as:

* CRM record lookup
* Contact update
* Data enrichment APIs
* Validation services

> Actual tools depend on your Composio account and enabled connectors.

---

### 4) Input / Output Behavior

* **Input:** free text from user (chat-based)
* **Output:** cleaned/validated CRM response returned to Chat Output

---

## Related Solutions

* **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.

* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.

* **[Deal Pipeline Manager](../deal-pipeline-manager/README.md)**  
  Automatically update deal progress and create follow-up tasks for your sales team.

* **[CRM Address Data Cleanup Agent](../crm-address-data-cleanup-agent/README.md)**  
  Specialized verification and standardization of physical address and location data.