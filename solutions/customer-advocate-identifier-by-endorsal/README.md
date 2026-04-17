# Customer Advocate Identifier (Uplizd) - Automate the discovery and engagement of your top brand advocates

## Summary
The Customer Advocate Identifier workflow leverages AI to scan customer interactions and feedback data to pinpoint high-value users who frequently provide positive testimonials or product endorsements. By automating the identification process, this Uplizd solution enables teams to proactively nurture brand advocates, streamline referral programs, and convert satisfied customers into long-term growth partners.

---

## Demo
![Workflow diagram showing the Customer Advocate Identifier agent analyzing CRM feedback data to flag potential brand advocates](image.png)
**Alt text (SEO-ready):** Uplizd Customer Advocate Identifier workflow diagram showing AI-driven CRM feedback analysis and brand advocate segmentation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/99b0a324-8471-5873-a5df-b54f2b8ff0cd)

---

## Category
- **Primary category:** Customer Success
- **Secondary tags:** advocacy, crm, feedback, customer retention, loyalty, engagement, ai workflow, composio
- This solution bridges the gap between raw customer sentiment and actionable advocacy programs by automating the identification of your most vocal supporters.

---

## Who is this for?
This solution is designed for teams looking to transform passive customer satisfaction into active brand growth through data-driven identification.

- **Customer Success Manager**
    - Proactively identify high-sentiment accounts ready for upsell or testimonial requests.
- **Marketing Operations Lead**
    - Build a reliable pipeline of verified brand advocates for case studies and social proof.
- **Community Manager**
    - Spot influential users within support tickets to invite them into exclusive beta programs.
- **Revenue Operations Analyst**
    - Correlate customer advocacy signals with lifetime value to optimize retention strategies.

---

## Features
- **Sentiment-Driven Scoring**
    - Automatically analyzes support tickets and feedback logs to assign an advocacy score based on tone and content.
- **Composio-Powered CRM Integration**
    - Seamlessly connects with your CRM to tag accounts and update contact fields with advocate status in real-time.
- **Automated Outreach Triggers**
    - Flags high-scoring advocates for immediate follow-up by the account management team via Slack or email.
- **Feedback Trend Analysis**
    - Extracts recurring themes from positive feedback to help product teams understand what drives user loyalty.
- **Dynamic Segment Sync**
    - Keeps your "Advocate" mailing lists updated by syncing identified users across your marketing automation platforms.

---

## Use Cases
**Advocacy Pipeline Management**
- Automatically move customers with high sentiment scores into a "Brand Ambassador" CRM list.
- Notify the marketing team when a user submits a glowing review that qualifies for a featured case study.

**Customer Retention & Loyalty**
- Identify "at-risk" advocates early by monitoring for drops in positive sentiment in their recent support interactions.
- Trigger personalized "Thank You" campaigns for users who have provided consistent positive feedback over a 90-day period.

**Product Feedback Loop**
- Aggregate specific feature praises from support tickets to create a "Voice of the Customer" report for product managers.
- Identify power users who are consistently suggesting improvements, marking them as candidates for early-access beta testing.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in the builder.
2. Connect your preferred CRM (e.g., Salesforce, HubSpot) via the Composio Toolset.
3. Configure your API keys for the LLM and the CRM integration.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger or manual request to scan for new advocates.
- **Agent**: Processes feedback data and evaluates sentiment against your custom advocacy criteria.
- **Composio Toolset**: Executes the CRM updates, tagging, and list management actions.
- **Chat Output**: Returns a summary of identified advocates and actions taken.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Scan the last 30 days of support tickets and identify customers with high sentiment scores.`
- `Tag all customers who mentioned "love" or "excellent" in their feedback as "Potential Advocate" in the CRM.`
- `Generate a list of top 10 brand advocates from the last quarter and notify the marketing team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, filtering qualitative data into structured insights.
- **Instruction Pattern:**
    - "Act as a Customer Success Analyst identifying high-sentiment interactions."
    - "Evaluate feedback based on tone, frequency of positive keywords, and user history."
    - "Output results in a structured format compatible with CRM field updates."

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable secure CRM connectivity.
- **Connection Scope:** Ensure the agent has read/write permissions for your CRM's "Contacts" and "Accounts" objects.

### 3) Tool Availability
- **CRM Search:** Fetch recent support tickets and customer notes.
- **Sentiment Analysis:** Process text to determine advocacy potential.
- **CRM Update:** Apply tags, update custom fields, or create tasks for account managers.

---

## Related Solutions
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather account-level intelligence to inform outreach.
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Strengthen customer relationships through automated CRM data management.
- [../whats-app-feedback-collection-agent-by-wati/README.md](../whats-app-feedback-collection-agent-by-wati/README.md) - Collect direct customer feedback via WhatsApp for analysis.
