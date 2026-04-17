# Event Promotion Link Generator (Uplizd) - Automate branded event tracking links

## Summary
The Event Promotion Link Generator is an intelligent Uplizd workflow that automates the creation of shortened, trackable URLs for event marketing campaigns. By integrating directly with TinyURL, this solution eliminates manual link management, ensures consistent UTM parameter application, and provides marketing teams with a single source of truth for campaign performance data.

---

## Demo
![Event Promotion Link Generator workflow interface showing Chat Input, Agent, TinyURL Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Event Promotion Link Generator workflow in Uplizd using TinyURL for automated marketing link shortening and campaign tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d4353b7f-c3c8-5f6f-b4b9-f6813f7f1cca)

---

## Category
*   **Primary category:** Marketing operations
*   **Secondary tags:** marketing, event promotion, tinyurl, link shortening, campaign tracking, automation, composio, ai workflow
*   This solution streamlines event promotion by automating the generation of branded tracking links, ensuring high-quality data hygiene for marketing analytics.

---

## Who is this for?
This solution is designed for marketing and operations professionals who need to manage high volumes of event-related traffic links efficiently.

*   **Event Marketing Manager**
    *   Reduces time spent manually creating and organizing unique tracking links for multi-channel event promotions.
*   **Digital Growth Specialist**
    *   Ensures every promotional asset is tagged correctly for accurate attribution in analytics platforms.
*   **Social Media Coordinator**
    *   Generates clean, professional-looking short links instantly for use across various social platforms.
*   **Operations Lead**
    *   Maintains a standardized link generation process that prevents human error and broken redirects in campaign assets.

---

## Features
- **Automated Link Shortening**
  Instantly converts long, complex event URLs into clean, shareable links using the TinyURL API via the Composio Toolset.
- **Dynamic UTM Injection**
  Automatically appends necessary UTM parameters to your destination URLs based on the specific event and channel provided in the prompt.
- **Real-time Validation**
  The agent verifies the structure of the input URL before processing to ensure the generated link is functional and ready for distribution.
- **Custom Alias Support**
  Allows users to request specific custom aliases for links, making them more memorable and brand-aligned for high-visibility campaigns.
- **Seamless Integration**
  Leverages the Composio Toolset to bridge the gap between your chat-based instructions and the TinyURL infrastructure without manual API coding.

---

## Use Cases
**Campaign Launch Management**
*   Generate unique tracking links for every speaker and partner involved in a virtual summit.
*   Create distinct short links for email, LinkedIn, and Twitter to isolate performance metrics per channel.

**Event Content Distribution**
*   Quickly shorten registration page links for inclusion in press releases and influencer outreach emails.
*   Generate trackable links for downloadable event assets like whitepapers or slide decks.

**Performance Analytics Hygiene**
*   Standardize link naming conventions across the marketing team to prevent fragmented data in Google Analytics.
*   Automate the creation of "link-in-bio" URLs for social media profiles during active event registration windows.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your TinyURL account within the Composio Toolset node.
3. Configure the Agent node with your preferred LLM (e.g., GPT-4o).
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the destination URL, campaign name, and channel details from the user.
*   **Agent**: Processes the request, formats the UTM parameters, and calls the TinyURL tool.
*   **Composio Toolset**: Executes the link shortening and alias creation via the TinyURL API.
*   **Chat Output**: Returns the final, shortened, and trackable URL to the user.

### 3) Run the Flow
Use the Playground to test your link generation:
*   `Generate a TinyURL for https://events.example.com/summit-2024 with UTM source=linkedin and campaign=summer_summit`
*   `Create a short link for the registration page at https://example.com/register and use the alias 'summit-reg-2024'`
*   `Shorten this URL for our email newsletter campaign: https://example.com/webinar-landing-page`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for link formatting and tool selection.
*   Use a model capable of strict instruction following.
*   Ensure the system prompt defines the required UTM structure.
*   Instruct the agent to always confirm the shortened link back to the user.

### 2) Composio Toolset Node
*   **API Key**: Provide your TinyURL API key in the Composio configuration.
*   **Connection Scope**: Ensure the toolset has permission to create and manage links within your TinyURL account.

### 3) Tool Availability
*   `tinyurl_create_link`: Used for generating the short URL.
*   `tinyurl_get_link_details`: Optional, for verifying existing links.

---

## Related Solutions
*   [Affiliate Link Performance Tracker](../affiliate-link-performance-tracker-by-cutt-ly/README.md) - Monitor and analyze the performance of your affiliate marketing links.
*   [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automate lead follow-ups and engagement via WhatsApp.
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data to better target your event marketing campaigns.
