# AI Testimonial Curator (Uplizd) - Automate social proof collection and marketing categorization

## Summary
The AI Testimonial Curator by Endorsal is an intelligent workflow designed to streamline the collection, organization, and categorization of customer feedback. By leveraging the Composio Toolset to interface with Endorsal, this solution transforms raw testimonials into structured marketing assets, ensuring your team maintains a high-velocity pipeline of social proof to drive conversions and build brand trust.

---

## Demo
![AI Testimonial Curator workflow showing Endorsal integration and automated categorization](image.png)
**Alt text (SEO-ready):** AI Testimonial Curator workflow by Uplizd, automating social proof collection, Endorsal data integration, and marketing content categorization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f2fc5ff6-460d-5d44-98cf-cfc9052baf18)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** testimonials, social proof, endorsal, content automation, marketing, reputation management, composio, ai workflow.
This solution bridges the gap between raw customer feedback and high-impact marketing collateral through automated data processing.

---

## Who is this for?
This solution is designed for marketing and growth teams looking to scale their social proof efforts without manual overhead.

*   **Content Marketers**
    *   Automate the curation of high-performing testimonials for website and social media campaigns.
*   **Customer Success Managers**
    *   Identify and flag high-value customer feedback for immediate marketing outreach.
*   **Growth Leads**
    *   Maintain a consistent stream of social proof to improve landing page conversion rates.
*   **Brand Managers**
    *   Ensure all collected testimonials are tagged and categorized by product feature or sentiment.

---

## Features
- **Automated Collection**
    Automatically fetch new testimonials from Endorsal as they arrive, eliminating manual data entry.
- **Sentiment Categorization**
    Use AI to analyze the tone and intent of feedback, automatically sorting testimonials into positive, neutral, or constructive buckets.
- **Feature-Based Tagging**
    Extract specific product mentions from feedback to map testimonials to relevant product features or use cases.
- **Composio Integration**
    Seamlessly connect with the Endorsal API to retrieve, filter, and manage testimonial data in real-time.
- **Marketing-Ready Output**
    Format raw customer quotes into polished, ready-to-publish snippets for your marketing channels.

---

## Use Cases
**Social Proof Scaling**
*   Automatically push 5-star testimonials to your website's "Customer Love" section.
*   Filter for specific keywords like "ease of use" to create targeted landing page copy.

**Reputation Management**
*   Flag negative or constructive feedback for immediate review by the Customer Success team.
*   Generate weekly reports summarizing sentiment trends across your customer base.

**Content Distribution**
*   Sync categorized testimonials directly into your content management system or social media scheduler.
*   Identify "Super Fans" based on recurring positive feedback for potential case study outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Endorsal account via the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger or manual command to fetch new testimonials.
*   **Agent**: Processes the raw text, performs sentiment analysis, and assigns relevant tags.
*   **Composio Toolset**: Executes API calls to Endorsal to retrieve and organize the data.
*   **Chat Output**: Delivers the curated and categorized testimonial report to your dashboard.

### 3) Run the Flow
Use the Playground to test your curator with these prompts:
*   `Fetch all new testimonials from the last 24 hours and categorize them by sentiment.`
*   `Find testimonials that mention 'onboarding' and format them for a LinkedIn post.`
*   `Identify the top 3 most positive testimonials from this week and summarize why they were successful.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your testimonial data.
*   Analyze text for sentiment, key themes, and product-specific mentions.
*   Maintain a professional, brand-aligned tone when summarizing customer feedback.
*   Strictly follow the output schema provided in the system instructions.

### 2) Composio Toolset Node
*   **API Key**: Provide your Endorsal API key within the Composio configuration.
*   **Connection Scope**: Ensure the toolset has read access to your testimonial library and write access for tagging/categorization.

### 3) Tool Availability
*   `endorsal_get_testimonials`: Fetches raw data from your Endorsal account.
*   `endorsal_update_tags`: Applies labels to testimonials based on AI analysis.
*   `sentiment_analyzer_tool`: Evaluates the emotional tone of the feedback.

---

## Related Solutions
*   [../whats-app-feedback-collection-agent-by-wati/README.md](../whats-app-feedback-collection-agent-by-wati/README.md) - Automate feedback collection via WhatsApp.
*   [../whats-app-feedback-collection-agent-by2chat/README.md](../whats-app-feedback-collection-agent-by2chat/README.md) - Streamline customer feedback loops using 2Chat.
*   [../whats-app-feedback-collector-by-wati/README.md](../whats-app-feedback-collector-by-wati/README.md) - Efficiently gather and manage customer insights.
