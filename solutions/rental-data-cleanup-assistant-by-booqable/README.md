# Rental Data Cleanup Assistant (Uplizd) - Automated database hygiene for rental operations

## Summary
The Rental Data Cleanup Assistant is an intelligent Uplizd workflow designed to automate the maintenance of customer and order records within Booqable. By leveraging the Composio Toolset, the agent identifies duplicate entries, corrects formatting inconsistencies, and validates contact information, ensuring a single source of truth for your rental business. This solution eliminates manual data entry errors and improves pipeline velocity by maintaining high-quality, actionable data for your operations team.

---

## Demo
![Rental Data Cleanup Assistant dashboard showing automated record deduplication and formatting logs in the Uplizd workflow builder](image.png)

**Alt text (SEO-ready):** Rental Data Cleanup Assistant dashboard showing automated record deduplication and formatting logs in the Uplizd workflow builder for Booqable data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ca433672-f81e-5815-91ec-b21cf8aef953)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** rental, booqable, data hygiene, crm, data sync, automation, composio, ai workflow
This solution streamlines rental operations by providing automated data cleansing and record synchronization for Booqable users.

---

## Who is this for?
This solution is designed for operations teams and rental business owners who need to maintain pristine data without manual intervention.

- **Operations Manager**
    - Automates routine database maintenance to focus on high-level rental strategy.
- **Rental Business Owner**
    - Ensures accurate customer records to prevent shipping errors and billing discrepancies.
- **Customer Success Lead**
    - Maintains clean contact history for personalized communication and support.
- **Data Analyst**
    - Relies on consistent, deduplicated datasets for accurate reporting and inventory forecasting.

---

## Features
- **Automated Deduplication**
    - Identifies and merges duplicate customer profiles based on email or phone number matches.
- **Real-time Data Formatting**
    - Standardizes address, phone, and name fields across all incoming rental orders.
- **Composio-Powered Integration**
    - Seamlessly connects with Booqable via the Composio Toolset to perform secure read/write operations.
- **Validation Logic**
    - Automatically flags incomplete or invalid order entries for human review.
- **Bulk Cleanup Cycles**
    - Executes scheduled cleanup tasks to keep the database healthy without manual triggers.

---

## Use Cases
**Customer Record Hygiene**
- Merging duplicate customer profiles created during peak rental seasons.
- Standardizing contact naming conventions to ensure consistent communication.

**Order Data Integrity**
- Validating delivery addresses against regional formats before dispatch.
- Cleaning up orphaned order records that lack valid customer associations.

**Operational Efficiency**
- Automating the cleanup of test or draft orders that clutter the active dashboard.
- Syncing updated customer details across multiple rental platforms to ensure data consistency.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and project to initialize the workflow.
3. Authenticate your Booqable connection within the Composio Toolset node.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or manual cleanup request.
- **Agent**: Processes the data cleanup logic and identifies records for modification.
- **Composio Toolset**: Executes the specific API calls to Booqable to update or delete records.
- **Chat Output**: Returns a summary report of all cleaned, merged, or flagged records.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Clean up all duplicate customer records created in the last 30 days.`
- `Standardize the address formatting for all active rental orders.`
- `Identify and flag any orders missing valid contact information.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine for identifying data anomalies.
- Use a high-reasoning model (e.g., GPT-4o) for accurate record matching.
- Instruct the agent to prioritize data integrity over speed during merge operations.
- Define strict rules for what constitutes a "duplicate" (e.g., matching email + last name).

### 2) Composio Toolset Node
- Provide your Booqable API key to enable secure access to your rental data.
- Ensure the connection scope includes read/write permissions for Customers and Orders.

### 3) Tool Availability
- `booqable_get_customers`: Retrieve existing profiles for comparison.
- `booqable_update_customer`: Merge or correct customer record fields.
- `booqable_list_orders`: Scan for order inconsistencies.
- `booqable_delete_record`: Remove redundant or test data entries.

---

## Related Solutions
- [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate new account provisioning and record creation.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - General-purpose data cleanup for complex CRM environments.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline field service and rental management workflows.
