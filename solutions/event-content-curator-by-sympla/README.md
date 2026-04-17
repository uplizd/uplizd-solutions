# Event Content Curator (Uplizd) - Automated event promotion and social media content generation

## Summary
The Event Content Curator is an intelligent Uplizd workflow designed to streamline event marketing by automatically generating promotional content, social media posts, and engagement materials from event details. By leveraging the Composio Toolset to interface with platforms like Sympla, this solution eliminates manual copywriting bottlenecks, ensuring consistent brand messaging and increased event visibility across digital channels.

---

## Demo
![Event Content Curator workflow dashboard showing automated content generation from event data](image.png)
**Alt text (SEO-ready):** Event Content Curator Uplizd workflow dashboard showing automated content generation, social media promotion, and Sympla integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f32c2c40-0bf3-5095-aaf7-15014deea34a)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** event marketing, content automation, sympla, social media, ai workflow, composio, lead generation, digital engagement.
This solution bridges the gap between event management platforms and social media distribution to maximize attendee acquisition.

---

## Who is this for?
This solution empowers marketing teams and event organizers to scale their promotional efforts without increasing headcount.

*   **Event Managers**
    *   Automate the creation of multi-channel promotional assets to save hours of manual drafting.
*   **Social Media Coordinators**
    *   Maintain a consistent posting cadence across platforms with AI-generated, event-specific content.
*   **Marketing Operations Leads**
    *   Ensure data-driven event details are accurately reflected in all external communications.
*   **Community Managers**
    *   Quickly generate engagement-focused updates to keep potential attendees informed and excited.

---

## Features
- **Automated Content Drafting**
  Generates high-converting social media captions, email blurbs, and blog post summaries directly from event metadata.
- **Sympla Integration**
  Uses the Composio Toolset to pull real-time event details, ticket availability, and schedules directly from your Sympla dashboard.
- **Multi-Platform Formatting**
  Optimizes content length and tone specifically for LinkedIn, Twitter, and Instagram requirements.
- **Real-Time Sync**
  Ensures that any updates made to the event details in the source platform are reflected in the generated promotional copy.
- **Engagement Optimization**
  Suggests relevant hashtags and call-to-action phrases to maximize reach and conversion for every event.

---

## Use Cases
**Event Launch Campaigns**
*   Automatically draft a series of "Save the Date" and "Registration Open" posts as soon as an event is published on Sympla.
*   Generate unique promotional variations for different audience segments based on event categories.

**Last-Minute Promotion**
*   Create urgent "Limited Tickets Remaining" social media updates triggered by low-inventory alerts.
*   Draft speaker-focused content to highlight key sessions and drive last-minute registrations.

**Post-Event Follow-up**
*   Generate "Thank You" posts and highlight reels based on event summary data.
*   Create recap content to share key takeaways and drive traffic to on-demand event recordings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Event Content Curator template from the solution gallery.
3. Connect your Sympla account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the event ID or event name from the user.
*   **Agent**: Processes event data and applies marketing persona instructions.
*   **Composio Toolset**: Fetches event details and attendee data from Sympla.
*   **Chat Output**: Delivers the finalized promotional content to the user.

### 3) Run the Flow
Use the Playground to test your content generation:
*   `"Generate a LinkedIn post for the upcoming 'Tech Summit 2024' event on Sympla."`
*   `"Create 3 variations of a Twitter thread promoting the keynote speaker for event ID 12345."`
*   `"Draft a short email announcement for the 'Workshop Series' event."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your expert marketing copywriter.
*   Set the system prompt to prioritize a professional yet engaging tone.
*   Instruct the agent to always include a clear call-to-action (CTA) pointing to the event registration link.
*   Ensure the agent maintains brand consistency by referencing provided style guidelines.

### 2) Composio Toolset Node
*   Provide your Sympla API key within the Composio configuration.
*   Set the connection scope to allow read access to event listings and attendee metrics.

### 3) Tool Availability
*   **Event Fetcher**: Retrieves full event metadata, including dates, descriptions, and ticket links.
*   **Attendee Analytics**: Provides insights into current registration counts for targeted copy.
*   **Platform Formatter**: Applies specific character limits and formatting rules for social media APIs.

---

## Related Solutions
*   [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) — Automate video promotion and metadata generation.
*   [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Engage potential attendees directly through automated messaging.
*   [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) — Streamline the creation of event-related visual assets and templates.
