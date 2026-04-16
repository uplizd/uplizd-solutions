# Changelog Publisher (Uplizd) - Automate feature release announcements

## Summary
The Changelog Publisher (Uplizd) is an automated AI workflow designed to transform completed feature tickets and development updates into polished, engaging changelog entries. By integrating directly with your product management tools via the Composio Toolset, this solution eliminates manual drafting, ensures consistent messaging across release notes, and accelerates your product marketing velocity.

---

## Demo
![Changelog Publisher workflow showing automated feature extraction and Canny publishing](image.png)
**Alt text (SEO-ready):** Changelog Publisher Uplizd workflow automating feature release notes and product updates via Canny integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/aad3bd10-6bf5-5964-8935-11ffb8993372)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** changelog, canny, product management, release notes, automation, ai workflow, composio, content generation.
This solution streamlines the transition from development completion to public-facing product announcements.

---

## Who is this for?
This workflow is designed for teams looking to maintain high-quality communication with their user base without the administrative burden of manual documentation.

*   **Product Managers**
    *   Reduce time spent manually summarizing technical tickets for public release.
*   **Product Marketers**
    *   Ensure every new feature launch is accompanied by professional, on-brand copy.
*   **Developer Advocates**
    *   Maintain a consistent cadence of updates that keep the community engaged.
*   **Customer Success Leads**
    *   Provide clear, accessible documentation of improvements to reduce support inquiries.

---

## Features
- **Automated Extraction**
  Pull completed feature details directly from your project management tools to identify key updates.
- **AI-Driven Copywriting**
  Generate professional, user-friendly changelog entries that highlight value rather than just technical specs.
- **Canny Integration**
  Seamlessly push finalized content to your Canny changelog board using the Composio Toolset.
- **Customizable Tone**
  Configure the agent to match your brand voice, whether it is technical, playful, or corporate.
- **Real-time Sync**
  Trigger updates immediately upon ticket closure to ensure your users are always informed of the latest improvements.

---

## Use Cases
**Release Note Automation**
*   Automatically draft a summary when a Jira or GitHub issue is moved to "Done."
*   Format technical release notes into benefit-driven bullet points for end-users.

**Product Marketing Alignment**
*   Sync feature highlights with your marketing calendar to ensure timely announcements.
*   Standardize the structure of all changelog posts across different product modules.

**Community Engagement**
*   Notify users of bug fixes and performance improvements to build trust and transparency.
*   Create "Coming Soon" or "Just Shipped" snippets for social media distribution.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow."
3. Configure your API credentials for Canny and your project management tool within the integration settings.
4. Ensure nodes are correctly mapped and the workflow is enabled in your Uplizd dashboard.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual request to publish a new update.
*   **Agent**: Processes the raw feature data and drafts the announcement based on your brand guidelines.
*   **Composio Toolset**: Connects to Canny to authenticate and push the generated content to your board.
*   **Chat Output**: Confirms the successful publication and provides a link to the live changelog entry.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Draft a changelog entry for the new dark mode feature based on ticket JIRA-102.`
* `Summarize the recent API performance improvements for our developer community.`
* `Create a 'Just Shipped' update for the new bulk-export functionality.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your technical copywriter.
*   **Instruction Pattern:**
    *   "Act as a professional product marketing manager."
    *   "Focus on user benefits rather than implementation details."
    *   "Maintain a concise, engaging, and professional tone."

### 2) Composio Toolset Node
Requires a valid Canny API key and appropriate scope permissions to create and manage posts on your changelog board.

### 3) Tool Availability
*   **Canny API:** For creating and updating changelog posts.
*   **Project Management Connectors:** For fetching ticket details (Jira, Linear, or GitHub).
*   **Formatting Utilities:** For ensuring Markdown compatibility in the final output.

---

## Related Solutions
* [Widget Experience Optimizer](../widget-experience-optimizer-by-productlane/README.md) — Enhance your product feedback and widget engagement.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather deep insights on your accounts to inform product strategy.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Keep your internal development and communication workflows running smoothly.
