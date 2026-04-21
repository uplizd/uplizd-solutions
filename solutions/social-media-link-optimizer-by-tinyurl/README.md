# Social Media Link Optimizer (Uplizd) - Streamline URL shortening and campaign tracking

## Summary
The Social Media Link Optimizer is an automated Uplizd AI workflow designed to transform long, messy URLs into clean, branded, and trackable links. By integrating with the TinyURL API, this solution eliminates manual link management, ensures consistent UTM parameter application, and provides marketing teams with a single source of truth for campaign performance metrics.

---

## Demo
![Social Media Link Optimizer workflow diagram showing input URL processing, TinyURL shortening, and output generation](image.png)
**Alt text (SEO-ready):** Social Media Link Optimizer workflow in Uplizd, featuring automated URL shortening, UTM parameter tagging, and campaign tracking via TinyURL integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d171a4a1-e09e-52b5-905d-30e7c0220b25)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** social media, url shortening, tinyurl, campaign tracking, marketing automation, link management, composio, ai workflow
This solution optimizes digital distribution by automating the link-shortening lifecycle for high-performance marketing campaigns.

---

## Who is this for?
This solution is designed for marketing professionals and growth teams who need to maintain clean, professional, and trackable links across multiple social channels.

*   **Social Media Manager**
    *   Reduces time spent manually shortening links for daily content calendars.
*   **Performance Marketer**
    *   Ensures every shared link includes accurate UTM parameters for precise ROI tracking.
*   **Content Strategist**
    *   Maintains brand consistency by using branded short domains across all digital touchpoints.
*   **Growth Lead**
    *   Centralizes link management to prevent broken redirects and lost traffic data.

---

## Features
- **Automated URL Shortening**
  Instantly converts long, complex URLs into concise, shareable links using the TinyURL API.
- **Dynamic UTM Injection**
  Automatically appends campaign, source, and medium parameters to ensure granular analytics tracking.
- **Branded Domain Support**
  Configures links to use your custom domain, reinforcing brand authority with every click.
- **Real-Time Link Validation**
  Checks destination URLs for validity before shortening to prevent 404 errors in live social posts.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely communicate with TinyURL and other marketing platforms.

---

## Use Cases
**Campaign Launch Management**
*   Batch-shortening URLs for multi-channel product launches across LinkedIn, Twitter, and Instagram.
*   Standardizing link naming conventions for cross-departmental marketing initiatives.

**Performance Analytics**
*   Generating unique tracking links for individual influencers to measure specific conversion rates.
*   Updating historical content with new, trackable links to revive underperforming evergreen posts.

**Content Workflow Automation**
*   Integrating link shortening directly into the content approval pipeline to save manual effort.
*   Creating QR codes and short links simultaneously for hybrid digital and physical marketing assets.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and import the workflow into your dashboard.
3. Authenticate your TinyURL account within the Composio Toolset configuration.
4. Ensure nodes are connected from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the long URL and desired campaign parameters from the user.
*   **Agent**: Processes the request, validates the URL, and structures the API call.
*   **Composio Toolset**: Executes the shortening command via the TinyURL API.
*   **Chat Output**: Returns the optimized, trackable short link to the user.

### 3) Run the Flow
Use the Playground to test your link optimization:
*   `Shorten this URL for my summer campaign: https://example.com/long-page-path?ref=internal`
*   `Create a TinyURL for this link with source=twitter and medium=social`
*   `Generate a branded short link for the new product landing page`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for URL processing and parameter mapping.
*   Always prioritize the inclusion of UTM parameters if provided in the prompt.
*   Validate that the input URL is a properly formatted web address.
*   Format the output to clearly distinguish between the original and the shortened link.

### 2) Composio Toolset Node
*   **API Key**: Provide your TinyURL API key in the connection settings.
*   **Connection Scope**: Ensure the toolset has read/write permissions for your TinyURL account.

### 3) Tool Availability
*   `tinyurl_create_link`: Generates the shortened URL.
*   `tinyurl_get_analytics`: Retrieves click-through data for existing links.
*   `tinyurl_update_link`: Modifies destination URLs for active campaigns.

---

## Related Solutions
*   [Affiliate Link Performance Tracker](../affiliate-link-performance-tracker-by-cutt-ly/README.md) - Monitor and optimize affiliate marketing link engagement.
*   [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) - Automate the sharing and tracking of video content across social platforms.
*   [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Use trackable links to drive users back to their shopping carts.
