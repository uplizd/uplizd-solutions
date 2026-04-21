# UK Lead Qualification Agent (Uplizd) - Automated lead scoring and validation for UK markets

## Summary
The UK Lead Qualification Agent is an intelligent workflow designed to streamline sales operations by automatically validating and scoring incoming leads based on UK-specific phone number insights. By leveraging real-time data verification, this Uplizd solution ensures that sales teams focus their efforts on high-intent, legitimate prospects, significantly reducing manual data hygiene tasks and increasing pipeline velocity.

---

## Demo
![UK Lead Qualification Agent workflow interface showing phone validation and lead scoring nodes](image.png)
**Alt text (SEO-ready):** UK Lead Qualification Agent workflow interface showing phone validation and lead scoring nodes for Uplizd sales automation and CRM data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/317fdbf3-0960-5e0b-97aa-e3b4830a81ff)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead qualification, uk market, data hygiene, sales operations, composio, ai workflow, lead scoring
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the verification of UK-based contact data.

---

## Who is this for?
This agent is built for revenue-focused teams looking to optimize their lead management process.

- **Sales Development Representatives (SDRs)**
    - Eliminate time wasted on invalid or disconnected phone numbers.
- **RevOps Managers**
    - Maintain high-quality CRM data hygiene through automated validation triggers.
- **Sales Managers**
    - Improve lead-to-opportunity conversion rates by prioritizing verified prospects.
- **Marketing Operations Specialists**
    - Ensure lead attribution and routing are based on accurate, qualified contact information.

---

## Features
- **Real-time Phone Validation**
    - Instantly verify the status and carrier information of UK phone numbers using integrated lookup tools.
- **Automated Lead Scoring**
    - Assign dynamic scores to leads based on verification results and predefined business rules.
- **CRM Integration**
    - Seamlessly push qualified lead data directly into your CRM via the Composio Toolset.
- **Intelligent Routing**
    - Automatically flag invalid or suspicious leads for manual review by the operations team.
- **Workflow Customization**
    - Easily adjust qualification thresholds and scoring logic to match your specific sales cycle.

---

## Use Cases
**Lead Intake Optimization**
- Automatically filter out non-UK or invalid phone numbers at the point of entry.
- Update lead status in the CRM based on successful verification checks.

**Sales Pipeline Hygiene**
- Identify and remove "dead" leads from active sequences to improve email deliverability.
- Enrich lead profiles with carrier and location data for better regional segmentation.

**Outbound Campaign Efficiency**
- Prioritize high-scoring leads for immediate follow-up by the sales team.
- Reduce bounce rates by ensuring all contact data is validated before outreach begins.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the UK Lead Qualification Agent template from the solution library.
3. Connect your preferred CRM and the required phone validation tool via the Composio dashboard.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data including phone numbers and contact details.
- **Agent**: Analyzes the input and triggers the validation logic.
- **Composio Toolset**: Executes the phone lookup and CRM update commands.
- **Chat Output**: Returns the qualification status and lead score to the user.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Validate the phone number +44 7700 900077 and update the lead status.`
- `Check if the lead with phone +44 20 7946 0123 is a valid UK mobile number.`
- `Score this lead based on the provided contact info and verify the phone number.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for lead qualification.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruct the agent to prioritize accuracy in phone number formatting.
- Ensure the agent follows strict logic for flagging "Invalid" vs "Qualified" leads.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication with external validation services.
- Set the connection scope to allow read/write access to your CRM's lead objects.

### 3) Tool Availability
- **Phone Validation API**: Capability to perform real-time lookups on UK numbers.
- **CRM Connector**: Capability to update lead fields and status labels.
- **Data Parser**: Capability to extract and normalize phone numbers from unstructured text.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with verified contact details.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain clean and accurate records across your CRM.
- [WhatsApp Lead Qualification Agent](../whats-app-lead-qualification-agent-by-whatsapp/README.md) — Qualify leads directly through WhatsApp messaging.
