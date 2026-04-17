# Email List Cleaner (Uplizd) - Automated email verification and list hygiene

## Summary
The Email List Cleaner (Uplizd) is an automated workflow designed to maintain high deliverability by verifying email addresses in real-time before marketing or sales campaigns. By integrating with NeverBounce, this solution identifies invalid, risky, or disposable email addresses, ensuring your CRM data remains clean and your sender reputation stays protected.

---

## Demo
![Email List Cleaner workflow diagram showing email input, verification via NeverBounce, and output of cleaned data](image.png)
**Alt text (SEO-ready):** Email List Cleaner (Uplizd) workflow for automated email verification, list hygiene, and deliverability optimization using NeverBounce.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/faaa9404-0726-5885-bb59-b9b372466d4a)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, data hygiene, lead management, neverbounce, deliverability, crm, automation, composio
- This solution streamlines the data cleaning process to ensure high-quality lead lists for all outbound communication channels.

---

## Who is this for?
This solution is designed for teams focused on maintaining high-quality databases and maximizing campaign ROI.

- **Email Marketer**
    - Ensures that campaign budgets are not wasted on invalid or bouncing email addresses.
- **Sales Operations Manager**
    - Maintains a clean, reliable CRM database by preventing the entry of low-quality lead data.
- **Growth Hacker**
    - Improves overall lead-to-customer conversion rates by focusing outreach on verified, reachable prospects.
- **Deliverability Specialist**
    - Protects the organization's domain reputation by minimizing bounce rates and spam complaints.

---

## Features
- **Real-time Verification**
    - Instantly validates email addresses against NeverBounce's extensive database to confirm deliverability.
- **Automated Hygiene**
    - Automatically flags or removes invalid, duplicate, or risky email entries from your source lists.
- **Composio Integration**
    - Leverages the Composio Toolset to bridge the gap between your data sources and the verification engine.
- **Customizable Thresholds**
    - Allows users to define specific criteria for what constitutes a "clean" vs. "risky" email address.
- **Scalable Processing**
    - Handles bulk list processing efficiently, allowing for large-scale data cleanup without manual intervention.

---

## Use Cases
**Campaign Preparation**
- Verify entire lead lists exported from your CRM before launching a new email marketing campaign.
- Filter out disposable email domains to ensure your messaging reaches genuine human recipients.

**CRM Maintenance**
- Periodically scan existing CRM contacts to identify and remove decayed or inactive email addresses.
- Sync verification results back to your CRM to update lead status fields automatically.

**Lead Ingestion**
- Validate new leads as they enter your system to ensure only high-quality data is processed by your sales team.
- Trigger automated alerts for leads that fail verification for immediate manual review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace and project destination.
3. Authenticate your NeverBounce and CRM credentials within the connection manager.
4. Ensure nodes are correctly mapped to your specific data input and output fields.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw email list or individual contact details for processing.
- **Agent**: Analyzes the input and orchestrates the verification logic using the provided instructions.
- **Composio Toolset**: Executes the API calls to NeverBounce to perform the actual email validation.
- **Chat Output**: Returns the cleaned list or a summary report of verified vs. invalid addresses.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Clean the following email list: [list of emails] and provide a summary of valid versus invalid addresses.`
- `Verify the email address john.doe@example.com and update the status in my CRM if it is invalid.`
- `Run a hygiene check on my recent lead import and flag all risky domains for manual review.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-maker for list processing.
- Always prioritize the "valid" status returned by the verification tool.
- Flag "unknown" or "risky" results for secondary review rather than deleting them immediately.
- Maintain a consistent output format for reporting the final count of cleaned records.

### 2) Composio Toolset Node
- Provide your NeverBounce API key within the Composio configuration settings.
- Ensure the connection scope includes read/write access to your email list sources (e.g., CSV, CRM, or Database).

### 3) Tool Availability
- **NeverBounce Verify**: Core tool for checking email deliverability.
- **Data Parser**: Utility for extracting email addresses from unstructured input text.
- **CRM Connector**: Interface for updating contact records based on verification results.

---

## Related Solutions
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive tools for maintaining overall CRM data quality and formatting.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms to ensure consistency.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact information and firmographic details.
