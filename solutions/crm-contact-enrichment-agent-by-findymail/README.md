# CRM Contact Enrichment Agent (Uplizd) - Automated lead data verification and enrichment

## Summary
The CRM Contact Enrichment Agent by Findymail automates the process of validating and appending professional contact information to your CRM records. By leveraging real-time data lookups, this Uplizd AI workflow eliminates manual research, ensures your sales pipeline is populated with accurate, high-intent contact data, and significantly improves outbound outreach hygiene.

---

## Demo
![CRM Contact Enrichment Agent workflow showing Findymail integration](image.png)
**Alt text (SEO-ready):** Uplizd CRM contact enrichment workflow using Findymail for automated lead data verification, email lookup, and CRM synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/43ebf3cb-c1f2-51d2-aada-54cb74f5971f)

---

## Category
**Primary category:** CRM data enrichment
**Secondary tags:** crm, findymail, lead generation, data hygiene, sales automation, contact verification, composio, ai workflow
This solution bridges the gap between raw lead lists and actionable sales intelligence by automating the enrichment lifecycle.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach without sacrificing data quality.

* **Sales Development Representatives (SDRs)**
    * Spend less time on manual prospecting and more time engaging with verified, high-quality leads.
* **RevOps Managers**
    * Maintain a pristine CRM database by ensuring every contact record is complete and up-to-date.
* **Growth Marketers**
    * Increase campaign conversion rates by targeting prospects with accurate, verified professional email addresses.
* **Account Executives (AEs)**
    * Reduce bounce rates and improve deliverability for personalized outbound sales sequences.

---

## Features
- **Automated Data Lookup**
    Leverages the Findymail API to instantly verify and retrieve professional contact details for leads in your CRM.
- **Real-time CRM Sync**
    Seamlessly updates contact objects in your CRM with newly discovered email addresses and phone numbers via the Composio Toolset.
- **Intelligent Hygiene**
    Automatically flags or skips contacts with invalid or unreachable email formats to maintain high sender reputation.
- **Scalable Batch Processing**
    Handles large volumes of contact records, allowing for bulk enrichment cycles that keep your pipeline moving.
- **Customizable Logic**
    Easily adjust the Agent instructions to prioritize specific data points or integrate with secondary enrichment sources.

---

## Use Cases
**Lead Qualification**
* Automatically enrich inbound leads from web forms with verified professional email addresses.
* Filter out low-quality or generic email addresses before they reach your sales sequence.

**Outbound Sales Acceleration**
* Append missing contact data to cold lists exported from LinkedIn or other professional networks.
* Ensure every prospect in your CRM has a verified primary contact method before triggering automated outreach.

**CRM Data Maintenance**
* Periodically scan existing CRM contacts to update outdated information and fill in missing fields.
* Re-verify contact data for high-value accounts to ensure ongoing communication stability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred CRM integration (e.g., Salesforce, HubSpot) within the Uplizd builder.
3. Authenticate your Findymail and CRM accounts via the Composio connection manager.
4. Ensure nodes are correctly wired from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives the lead record or list of contacts to be processed.
* **Agent:** Analyzes the contact data and determines the necessary enrichment steps.
* **Composio Toolset:** Executes the Findymail lookup and pushes the verified data back to the CRM.
* **Chat Output:** Confirms the enrichment status and provides a summary of updated records.

### 3) Run the Flow
Use the Playground to test your enrichment logic:
* `Enrich the contact record for john.doe@example.com in my HubSpot CRM.`
* `Find and update the professional email for the lead with ID 98765 in Salesforce.`
* `Scan my 'New Leads' list and enrich all contacts missing a verified email address.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data validation and CRM updates.
* Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are a data enrichment specialist. Extract the lead's name and company, query Findymail for verified contact info, and update the CRM record."
* Ensure the agent is configured to handle null values gracefully if no contact info is found.

### 2) Composio Toolset Node
* Provide your Findymail API key and CRM credentials within the Composio connection portal.
* Ensure the scope includes read/write access to `Contacts` and `Leads` objects in your CRM.

### 3) Tool Availability
* **Findymail API:** Used for email discovery and verification.
* **CRM Connector:** Used for fetching existing records and performing bulk updates.
* **Data Parser:** Used to format incoming lead data into the required schema for the enrichment tool.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Automate deep account research and data enrichment.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your CRM data consistent across multiple platforms.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Leverage ZoomInfo for comprehensive account-level insights.
