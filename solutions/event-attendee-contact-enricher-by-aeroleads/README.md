# Event Attendee Contact Enricher (Uplizd) - Automated lead enrichment for event networking

## Summary
The Event Attendee Contact Enricher is an automated Uplizd workflow designed to bridge the gap between event attendance and pipeline generation. By leveraging the AeroLeads integration via the Composio Toolset, this solution automatically processes attendee profiles, extracts verified contact information, and updates your CRM. It eliminates manual data entry, ensures high-quality lead hygiene, and accelerates sales outreach velocity for event-driven marketing teams.

---

## Demo
![Event Attendee Contact Enricher workflow showing LinkedIn profile processing and AeroLeads data extraction](image.png)
**Alt text (SEO-ready):** Uplizd workflow for event attendee contact enrichment using AeroLeads and CRM integration for automated sales prospecting.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDSo7S1j89gAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABkSURBVEjH7dOxCcAwDEXR1/3/0z06hA6FokMh+Jp00kUIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQv4XfAEL9wE1s6+2WwAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/1a909fd6-7cd7-5db1-9580-7ff734853dc0)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead enrichment, aeroleads, crm, sales prospecting, event marketing, data hygiene, composio, ai workflow
- This solution streamlines the conversion of raw event attendee lists into enriched, sales-ready contact records within your CRM.

---

## Who is this for?
This solution is built for revenue-focused teams looking to maximize the ROI of their event presence.

- **Sales Development Representative (SDR)**
    - Automates the tedious process of finding contact details for event leads, allowing for immediate outreach.
- **Event Marketing Manager**
    - Ensures that the leads generated at expensive industry events are captured and enriched for post-event nurturing.
- **Revenue Operations (RevOps) Lead**
    - Maintains data hygiene by ensuring all event-sourced contacts are verified and standardized before entering the CRM.
- **Growth Marketer**
    - Scales lead acquisition efforts by integrating third-party enrichment tools directly into the event follow-up pipeline.

---

## Features
- **Automated Profile Extraction**
    - Seamlessly pulls attendee data from LinkedIn profiles or event lists to initiate the enrichment process.
- **Real-time AeroLeads Integration**
    - Utilizes the Composio Toolset to query AeroLeads for verified email addresses, phone numbers, and professional titles.
- **CRM Data Synchronization**
    - Automatically pushes enriched contact records directly into your CRM, mapping fields to ensure consistent data structure.
- **Lead Qualification Scoring**
    - Applies logic to prioritize leads based on job title, company size, and enrichment success rate.
- **Error Handling & Validation**
    - Flags incomplete profiles or failed lookups for manual review, ensuring no potential opportunity is lost due to data gaps.

---

## Use Cases
**Post-Event Lead Nurturing**
- Automatically enrich attendee lists immediately following a trade show or webinar to enable same-day follow-up.
- Sync verified contacts to CRM "Event Lead" campaigns for automated email sequence enrollment.

**Sales Prospecting Efficiency**
- Convert LinkedIn profile URLs from event attendee lists into actionable contact records without leaving the Uplizd interface.
- Identify decision-makers within target accounts found at industry conferences to accelerate the sales cycle.

**Data Hygiene & Enrichment**
- Bulk-update existing CRM contacts with missing professional details using AeroLeads enrichment.
- Standardize job titles and company information for event attendees to ensure accurate segmentation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your CRM and AeroLeads accounts via the Composio Toolset.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw attendee profile URL or list.
- **Agent**: Analyzes the input and determines the necessary enrichment steps.
- **Composio Toolset**: Executes the AeroLeads API calls to fetch verified contact data.
- **Chat Output**: Returns the enriched contact summary and confirms CRM synchronization.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Enrich this LinkedIn profile for our upcoming sales outreach: [LinkedIn URL]`
- `Find contact details for all attendees in this list and add them to the 'Q3 Event' CRM campaign.`
- `Verify the current contact info for this lead and update their record if new data is found.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between input data and the enrichment tools.
- Set the system prompt to prioritize accuracy and data formatting.
- Ensure the agent is configured to handle multiple profile inputs in a single batch.
- Instruct the agent to report any failed lookups to the Chat Output for visibility.

### 2) Composio Toolset Node
- Authenticate with your AeroLeads API key within the Composio dashboard.
- Set the connection scope to allow read/write access for contact enrichment and CRM updates.

### 3) Tool Availability
- **AeroLeads Search**: Capability to find emails and phone numbers based on profile URLs.
- **CRM Connector**: Capability to create or update contact records in your specific CRM environment.
- **Data Formatter**: Capability to normalize job titles and company names before CRM insertion.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize and resolve data conflicts across multiple CRM platforms.
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Gather deep account intelligence and enrichment via Dropcontact.
- [../account-research-assistant-by-zoominfo/README.md](../account-research-assistant-by-zoominfo/README.md) - Leverage ZoomInfo for comprehensive account research and lead enrichment.
