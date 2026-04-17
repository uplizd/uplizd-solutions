# Group Dining Splitter (Uplizd) - Automate bill splitting and expense tracking

## Summary
The Group Dining Splitter is an intelligent Uplizd workflow designed to streamline restaurant bill management by automating the calculation and distribution of costs among participants. By integrating with Splitwise, this solution eliminates manual math errors and ensures fair, transparent expense tracking, significantly increasing pipeline velocity for social and professional group dining coordination.

---

## Demo
![Uplizd Group Dining Splitter workflow interface showing bill parsing and Splitwise integration](image.png)
**Alt text (SEO-ready):** Uplizd Group Dining Splitter workflow, automated bill splitting, Splitwise integration, expense management, and restaurant cost calculation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/09c665b2-4954-5863-ab72-890575fd535d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** splitwise, expense management, group dining, bill splitting, finance automation, personal finance, composio, ai workflow
- This solution bridges the gap between social dining experiences and organized financial tracking through automated data integration.

---

## Who is this for?
This solution is designed for individuals and professional teams who frequently manage shared expenses and require a frictionless way to settle group costs.

- **Event Organizers**
  - Quickly distribute individual costs to attendees without manual calculation.
- **Team Leads**
  - Maintain transparency during team lunches and off-site dining events.
- **Frequent Travelers**
  - Ensure shared meal expenses are tracked accurately across group trips.
- **Financial Controllers**
  - Reduce administrative overhead by automating the entry of shared dining costs into tracking systems.

---

## Features
- **Automated Bill Parsing**
  - Extracts line items and total amounts from receipts to ensure accurate data entry.
- **Splitwise Integration**
  - Seamlessly pushes calculated shares to the Splitwise platform using the Composio Toolset.
- **Dynamic Participant Mapping**
  - Automatically identifies group members and assigns specific costs based on individual consumption.
- **Real-time Settlement Notifications**
  - Triggers instant updates to participants regarding their share of the bill.
- **Error-Free Calculation Engine**
  - Eliminates human error in tax and tip distribution across multiple parties.

---

## Use Cases
**Professional Team Dining**
- Automatically split the bill for team lunches and client dinners.
- Sync expenses directly to the team's shared Splitwise group for immediate visibility.

**Social Event Coordination**
- Manage costs for large group dinners or birthday celebrations.
- Ensure fair distribution of shared appetizers and drinks among all attendees.

**Travel and Off-site Expenses**
- Track daily meal costs during corporate off-sites or group travel.
- Reconcile shared dining expenses at the end of each day to prevent end-of-trip confusion.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Group Dining Splitter template from the solution library.
3. Connect your Splitwise account via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the bill details or receipt text from the user.
- **Agent**: Processes the input, calculates individual shares, and formats the data.
- **Composio Toolset**: Executes the API calls to update Splitwise records.
- **Chat Output**: Returns a confirmation message with the breakdown of costs per person.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Split a $200 bill among 4 people, including a 20% tip, and add it to the 'Team Lunch' group.`
- `Calculate the share for 3 people on a $150 bill and send the details to Splitwise.`
- `Parse this receipt text [insert text] and split the total equally among the 5 attendees.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the financial logic engine, ensuring accurate math and clear communication.
- Instruction: "Act as a precise financial assistant that parses receipt data and calculates individual shares."
- Instruction: "Always verify the total amount including tax and tip before splitting."
- Instruction: "Format the output clearly so users can easily see their specific contribution."

### 2) Composio Toolset Node
- Requires a valid Splitwise API key configured within the Composio dashboard.
- Ensure the connection scope includes permissions for creating expenses and retrieving group IDs.

### 3) Tool Availability
- **Splitwise Create Expense**: Adds the calculated amounts to the specified group.
- **Splitwise Get Groups**: Fetches available groups to ensure the expense is logged correctly.
- **Splitwise Add Comment**: Allows the agent to append notes or receipt summaries to the expense.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](Account Reconciliation Helper) - Automate financial record matching and ledger updates.
- [../workflow-automation-agent-by-jobnimbus/README.md](Workflow Automation Agent) - Streamline operational tasks and cross-platform data synchronization.
- [../account-health-usage-monitor-by-jotform/README.md](Account Health Usage Monitor) - Track and report on account usage metrics and compliance.
