# Email List Hygiene Agent (Uplizd) - Automated email deliverability and list optimization

## Summary
The Email List Hygiene Agent is an intelligent Uplizd workflow designed to maintain high sender reputation and email deliverability by automating the identification and removal of invalid, inactive, or risky contacts. By integrating directly with your email marketing platform via the Composio Toolset, this agent ensures your mailing lists remain clean, compliant, and optimized for engagement, ultimately protecting your domain from blacklisting and improving campaign ROI.

---

## Demo
![Email List Hygiene Agent workflow showing automated contact validation and list cleanup in the Uplizd builder](image.png)
**Alt text (SEO-ready):** Email List Hygiene Agent workflow for automated contact validation, list scrubbing, and email deliverability optimization using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKAAABAAAB)](https://uplizd.ai/solutions/9233f6a3-885c-5074-94bb-fb225f9f3db5)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, list hygiene, deliverability, data cleaning, sendfox, automation, composio, ai workflow
- This solution streamlines marketing operations by automating the data hygiene processes required to maintain healthy and responsive email subscriber lists.

---

## Who is this for?
This solution is built for marketing and operations teams focused on maintaining high-quality communication channels.

- **Email Marketing Managers**
    - Ensure high open rates and domain health by removing inactive or invalid contacts automatically.
- **Growth Marketers**
    - Improve campaign performance by focusing resources on verified, high-intent leads.
- **RevOps Specialists**
    - Maintain data hygiene across the marketing stack to ensure accurate reporting and segmentation.
- **Compliance Officers**
    - Reduce the risk of spam complaints and ensure adherence to email marketing best practices.

---

## Features
- **Automated List Scrubbing**
    - Automatically identifies and flags invalid email addresses, syntax errors, and disposable domains.
- **Real-time Engagement Analysis**
    - Filters out subscribers who have not engaged with content over a defined period to prevent bounce-backs.
- **Composio-Powered Integration**
    - Seamlessly connects with SendFox and other email platforms to execute list updates without manual exports.
- **Customizable Hygiene Rules**
    - Define specific criteria for what constitutes a "stale" contact based on your unique business logic.
- **Audit Logging**
    - Maintains a record of all list modifications, providing transparency into your data maintenance processes.

---

## Use Cases
**List Maintenance**
- Automatically purge contacts that have hard-bounced across three consecutive campaigns.
- Identify and remove duplicate entries that cause inflated subscriber counts and wasted budget.

**Engagement Optimization**
- Segment inactive users into a "re-engagement" campaign before final removal from the primary list.
- Sync list cleanup results back to your CRM to ensure sales and marketing teams share a single source of truth.

**Compliance & Deliverability**
- Scan for role-based email addresses (e.g., info@, support@) that typically result in lower engagement.
- Ensure compliance with anti-spam regulations by maintaining an up-to-date and verified subscriber database.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your SendFox account within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or list ID to begin the cleaning process.
- **Agent**: Processes instructions to evaluate contact status based on predefined hygiene rules.
- **Composio Toolset**: Executes API calls to fetch, verify, and update contact records in your email platform.
- **Chat Output**: Returns a summary report of the cleaned contacts and the actions taken.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Clean my main newsletter list by removing all contacts who haven't opened an email in 6 months.`
- `Identify and flag all invalid email addresses in the 'Q3 Leads' list.`
- `Provide a summary report of all contacts removed from the 'General' list today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for your hygiene strategy.
- Set the system prompt to prioritize data accuracy and strict adherence to your defined "inactive" thresholds.
- Ensure the agent is instructed to request confirmation before performing bulk deletions.
- Configure the agent to output clean, structured summaries of all actions performed.

### 2) Composio Toolset Node
- Provide your SendFox API key within the Composio configuration.
- Set the connection scope to allow read/write access to your contact lists.

### 3) Tool Availability
- **List Fetcher**: Retrieves subscriber data from specified campaigns.
- **Contact Validator**: Checks email syntax and domain validity.
- **List Updater**: Performs bulk updates, deletions, or tag modifications.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automates follow-ups for unpurchased items.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Manages lead engagement via messaging channels.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Broad-spectrum data cleanup for enterprise CRM platforms.
