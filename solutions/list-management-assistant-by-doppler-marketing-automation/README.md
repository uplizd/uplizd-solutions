# List Management Assistant (Uplizd) - Intelligent subscriber list hygiene and automation

## Summary
The List Management Assistant is an Uplizd AI workflow designed to automate subscriber list maintenance, segmentation, and data hygiene. By leveraging the Composio Toolset, this solution enables marketing teams to maintain high-quality contact lists, reduce bounce rates, and ensure pipeline velocity through real-time synchronization and automated list cleanup.

---

## Demo
![List Management Assistant workflow interface showing automated subscriber list cleanup and segmentation](image.png)
**Alt text (SEO-ready):** List Management Assistant Uplizd workflow for automated subscriber list hygiene, marketing segmentation, and CRM data sync.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/477faf1e-c1fb-5bd1-835b-c8dc3891baa0)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** crm, marketing automation, list management, data hygiene, subscriber segmentation, composio, ai workflow, lead nurturing
- This solution streamlines the lifecycle of marketing lists by automating the ingestion, validation, and categorization of subscriber data.

---

## Who is this for?
This assistant is designed for marketing and operations professionals who need to maintain pristine contact data without manual intervention.

- **Marketing Manager**
    - Automates list segmentation to ensure high-relevance campaign targeting.
- **CRM Administrator**
    - Maintains data hygiene by identifying and removing inactive or duplicate subscriber records.
- **Growth Specialist**
    - Accelerates lead nurturing by ensuring the right contacts are synced to the correct automation workflows.
- **Email Operations Lead**
    - Improves deliverability rates by proactively cleaning lists of invalid or bounced email addresses.

---

## Features
- **Automated List Cleaning**
    - Identifies and removes invalid, duplicate, or inactive subscribers to maintain high list health.
- **Intelligent Segmentation**
    - Dynamically categorizes subscribers based on engagement signals and behavioral data.
- **Real-time CRM Sync**
    - Ensures that list updates are immediately reflected across your connected CRM and marketing platforms.
- **Engagement Monitoring**
    - Tracks subscriber interaction patterns to trigger automated re-engagement or pruning workflows.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interact with marketing APIs and CRM databases.

---

## Use Cases
**Subscriber Data Hygiene**
- Automatically flagging and purging contacts that have not engaged with emails in over 90 days.
- Merging duplicate contact records across multiple marketing platforms to create a single source of truth.

**Targeted List Segmentation**
- Creating dynamic segments based on recent purchase history or specific lead source attributes.
- Routing high-intent leads into specialized nurturing sequences based on real-time engagement scores.

**Marketing Pipeline Optimization**
- Syncing updated subscriber status changes directly into your CRM to keep sales and marketing teams aligned.
- Automating the export of cleaned, segmented lists for upcoming seasonal campaign launches.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import" option.
2. Upload the List Management Assistant JSON configuration file.
3. Connect your required CRM and marketing platform credentials via the Composio Toolset.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives user commands or trigger events for list maintenance.
- **Agent**: Processes instructions and determines the necessary cleanup or segmentation actions.
- **Composio Toolset**: Executes API calls to fetch, update, or delete subscriber records.
- **Chat Output**: Returns a summary report of the actions performed on the subscriber list.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Clean up my 'Newsletter' list by removing all subscribers who haven't opened an email in 6 months.`
- `Segment all contacts from the 'Q3 Campaign' into a new list based on their industry field.`
- `Find and merge duplicate entries in the 'Master Subscriber' list and notify me of the changes.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for list operations, ensuring data integrity and logical execution.
- Instruction: Focus on accuracy when identifying duplicate or invalid records.
- Instruction: Prioritize data privacy and compliance when handling subscriber information.
- Instruction: Provide clear, concise summaries of all list modifications performed.

### 2) Composio Toolset Node
- Requires an active API key for your specific CRM or marketing platform (e.g., HubSpot, Salesforce, Klaviyo).
- Ensure the connection scope includes read/write access to contact lists and subscriber metadata.

### 3) Tool Availability
- **List Fetcher**: Retrieves current subscriber data for analysis.
- **Record Validator**: Checks email syntax and status against external validation services.
- **Segmentation Engine**: Applies tags or moves contacts between lists based on defined criteria.
- **Sync Manager**: Pushes updates back to the source CRM to ensure consistency.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automates follow-ups for users who leave items in their cart.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enriches account data to improve lead qualification and targeting.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Engages subscribers through automated messaging workflows.
