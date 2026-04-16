# Automated Product Demo Creator (Uplizd) - AI-powered personalized video generation for sales demos

## Summary
The Automated Product Demo Creator (Uplizd) streamlines the sales cycle by leveraging AI to generate personalized product walkthroughs and demo videos. By integrating HeyGen’s avatar technology with your CRM data, this workflow enables revenue teams to deliver high-conversion, tailored content at scale, significantly reducing manual video production time and increasing prospect engagement.

---

## Demo
![Automated Product Demo Creator workflow showing HeyGen avatar integration and CRM data mapping](image.png)
**Alt text (SEO-ready):** Automated Product Demo Creator workflow using Uplizd, HeyGen AI avatars, and CRM data integration for personalized sales video generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/a25bbed3-17f5-5ce1-9b15-e1e8f2f4e177)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales, ai video, heygen, personalization, pipeline, content automation, composio, sales enablement
- This solution bridges the gap between static CRM data and dynamic video content to accelerate the sales pipeline through automated outreach.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach efforts with high-quality, personalized video content.

- **Sales Development Representative (SDR)**
  - Automate the creation of personalized video intros for cold outreach to increase response rates.
- **Account Executive (AE)**
  - Generate custom product walkthroughs tailored to specific prospect pain points identified in the CRM.
- **Marketing Operations Manager**
  - Standardize brand messaging across all automated video assets while maintaining a personalized touch.
- **Customer Success Manager**
  - Create personalized onboarding walkthroughs for new accounts to reduce time-to-value.

---

## Features
- **AI Avatar Integration**
  - Utilize HeyGen’s lifelike avatars to deliver professional-grade video presentations without the need for manual recording.
- **CRM Data Mapping**
  - Automatically pull prospect names, company details, and specific use cases from your CRM to customize video scripts.
- **Dynamic Script Generation**
  - Leverage the Agent node to synthesize prospect data into compelling, personalized video scripts in real-time.
- **Workflow Automation**
  - Seamlessly trigger video generation tasks directly from your existing sales workflow via the Composio Toolset.
- **Scalable Content Production**
  - Produce hundreds of unique, personalized demo videos in the time it previously took to create one, maximizing pipeline velocity.

---

## Use Cases
**Personalized Cold Outreach**
- Generate custom video intros that mention the prospect's company name and recent industry news.
- Automatically send personalized video links to prospects who have engaged with previous email campaigns.

**Tailored Product Walkthroughs**
- Create specific demo segments that highlight features relevant to the prospect's industry or job role.
- Update demo scripts dynamically based on the specific product tier or plan the prospect is evaluating.

**Customer Onboarding & Education**
- Send personalized welcome videos that address the specific goals identified during the sales process.
- Automate the creation of feature-specific tutorials based on the modules the customer has purchased.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Automated Product Demo Creator template from the library.
3. Connect your HeyGen API credentials and CRM account within the integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives prospect data and specific demo requirements.
- **Agent**: Processes the input, retrieves CRM context, and drafts the personalized video script.
- **Composio Toolset**: Executes the API calls to HeyGen to generate the video asset.
- **Chat Output**: Delivers the final video link or notification to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Generate a personalized demo video for John Doe at Acme Corp focusing on our reporting features.`
- `Create a 30-second product walkthrough for a prospect in the healthcare industry.`
- `Draft and generate a personalized welcome video for a new lead from the Salesforce 'New Opportunity' trigger.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative engine, transforming raw data into engaging video scripts.
- Use a high-reasoning model to ensure scripts sound natural and professional.
- Instruct the agent to maintain a consistent brand voice across all generated videos.
- Configure the agent to prioritize key value propositions based on the prospect's industry.

### 2) Composio Toolset Node
- Provide your HeyGen API key to enable video generation capabilities.
- Set the connection scope to allow the agent to read CRM data and write video assets to your storage.

### 3) Tool Availability
- **HeyGen API**: For avatar-based video rendering.
- **CRM Connector**: For fetching prospect profile details and account history.
- **Notification Service**: For alerting the sales team once the video is ready for distribution.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich prospect data for more effective personalization.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather deep insights to fuel your video script generation.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage the lifecycle of the deals you are creating demos for.
