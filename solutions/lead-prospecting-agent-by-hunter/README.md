# Lead Prospecting Agent (Uplizd) - Automated lead discovery and email verification for outbound sales

## Summary
The Lead Prospecting Agent by Hunter is an AI-powered workflow designed to accelerate outbound sales by automating the discovery of high-intent leads and verifying contact information in real-time. By integrating directly with Hunter.io via the Composio Toolset, this solution eliminates manual research bottlenecks, ensuring sales teams maintain a clean, actionable pipeline of verified prospects to drive higher conversion rates and pipeline velocity.

---

## Demo
![Lead Prospecting Agent workflow showing Hunter.io integration for automated lead discovery and email verification](image.png)
**Alt text (SEO-ready):** Lead Prospecting Agent workflow showing Hunter.io integration for automated lead discovery and email verification on Uplizd, streamlining sales outreach and data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/afd32829-3a62-5342-b721-d7d34ced521b)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead generation, hunter.io, sales outreach, email verification, prospecting, sales operations, composio, ai workflow
- This solution bridges the gap between raw company data and verified contact lists, serving as a critical component of modern RevOps and outbound sales stacks.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outbound efforts without sacrificing data quality.

- **Sales Development Representative (SDR):**
    - Automates the time-consuming process of finding and verifying prospect contact details.
- **Account Executive (AE):**
    - Ensures that outreach efforts are directed at validated, high-intent leads to maximize meeting bookings.
- **Sales Operations Manager:**
    - Maintains high data hygiene standards by ensuring only verified emails enter the CRM.
- **Growth Marketer:**
    - Rapidly builds targeted lead lists for personalized cold-outreach campaigns.

---

## Features
- **Automated Lead Discovery**
  Leverages Hunter.io to find professional email addresses associated with specific domains or company profiles.
- **Real-time Email Verification**
  Automatically validates email deliverability before adding leads to your pipeline, reducing bounce rates.
- **Composio-Powered Integration**
  Seamlessly connects the Uplizd agent to Hunter.io, enabling secure, authenticated data retrieval.
- **Intelligent Data Mapping**
  Automatically parses and structures lead data, ensuring consistent formatting across your sales tools.
- **Pipeline Hygiene Enforcement**
  Prevents duplicate or invalid entries from polluting your CRM by filtering data at the point of ingestion.

---

## Use Cases
**Outbound Sales Prospecting**
- Automatically generate a list of verified leads for a target company domain.
- Enrich existing lead records with missing professional email addresses.

**Sales Pipeline Hygiene**
- Cleanse existing lead databases by verifying the status of legacy email addresses.
- Filter out low-quality or invalid leads before they reach the sales outreach stage.

**Account Intelligence**
- Identify key decision-makers within a target account by searching for specific job titles.
- Aggregate contact information for multiple stakeholders during the account mapping process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your Hunter.io account within the Composio connection manager.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input:** Receives the target company domain or prospect search criteria.
- **Agent:** Processes the intent and triggers the appropriate Hunter.io search functions.
- **Composio Toolset:** Executes the API calls to Hunter.io for lead discovery and verification.
- **Chat Output:** Displays the verified lead contact information and status.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Find and verify professional email addresses for employees at google.com`
- `Search for marketing managers at hubspot.com and provide their verified emails`
- `Verify the email address for john.doe@example.com and return the deliverability status`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your prospecting logic.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize high-confidence email matches.
- Ensure the agent is configured to handle "no result" scenarios gracefully.

### 2) Composio Toolset Node
- Provide your Hunter.io API key via the Composio dashboard.
- Set the connection scope to allow `email-finder` and `email-verifier` permissions.

### 3) Tool Availability
- `hunter_email_finder`: Search for emails by domain and name.
- `hunter_email_verifier`: Check the deliverability of a specific email address.
- `hunter_domain_search`: Discover company-wide contact patterns.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Identify and report on high-intent account signals.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep dive into account firmographics and contact data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize verified lead data across multiple CRM platforms.
