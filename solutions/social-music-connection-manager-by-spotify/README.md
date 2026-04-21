# Social Music Connection Manager (Uplizd) - Automate playlist discovery and social music synchronization

## Summary
The Social Music Connection Manager is an intelligent Uplizd workflow designed to bridge the gap between your social network and your music library. By leveraging the Spotify API via the Composio Toolset, this solution automatically monitors, follows, and syncs curated playlists from your connections, ensuring your discovery pipeline remains fresh and relevant without manual intervention.

---

## Demo
![Social Music Connection Manager dashboard showing automated playlist synchronization and friend activity tracking](image.png)
**Alt text (SEO-ready):** Social Music Connection Manager Uplizd workflow for automated Spotify playlist discovery, social music synchronization, and network music tracking using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ef098e7a-574d-564e-9a7f-f127d0203a81)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** spotify, music, social discovery, playlist management, automation, composio, ai workflow, data sync.
This solution streamlines music discovery by automating the synchronization of social playlist data into your personal library.

---

## Who is this for?
This workflow is built for music enthusiasts, curators, and social media power users who want to optimize their listening experience.

* **Music Curators**
    * Automatically aggregate new tracks from influential playlists to maintain high-quality discovery feeds.
* **Social Media Managers**
    * Sync brand-aligned music content across multiple accounts to ensure consistent audio branding.
* **Digital Creators**
    * Effortlessly track trending music within your niche to stay ahead of audio-based content trends.
* **Casual Listeners**
    * Eliminate manual searching by having your friends' latest musical discoveries delivered directly to your library.

---

## Features
- **Automated Playlist Sync**
  Real-time synchronization of tracks from monitored social playlists directly into your personal Spotify collection.
- **Intelligent Discovery Engine**
  Uses AI to identify and prioritize high-engagement tracks from your network's activity.
- **Composio Toolset Integration**
  Seamlessly connects to the Spotify API to handle authentication, playlist retrieval, and track management securely.
- **Network Activity Monitoring**
  Tracks updates from your connections, ensuring you never miss a new release or playlist update.
- **Customizable Filtering**
  Define specific criteria for which tracks get added, ensuring your library remains curated to your personal taste.

---

## Use Cases
**Playlist Curation**
* Automatically add tracks from a friend's "Weekly Discovery" playlist to your own library.
* Sync collaborative playlists to ensure all contributors' additions are captured in real-time.

**Trend Tracking**
* Monitor industry-leading playlists to identify emerging artists and trending genres.
* Aggregate music signals from your social network to build a "Trending Now" master list.

**Library Maintenance**
* Periodically clean up your library by cross-referencing your saved tracks against active social playlists.
* Sync your "Liked Songs" across multiple Spotify accounts for a unified listening experience.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your Spotify account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your commands or trigger signals for playlist synchronization.
* **Agent**: Processes your intent, analyzes playlist data, and decides which tracks to sync.
* **Composio Toolset**: Executes secure API calls to Spotify for fetching and updating playlist data.
* **Chat Output**: Provides a summary of the tracks synced and the status of your playlist updates.

### 3) Run the Flow
Open the Playground and try these prompts:
* `Sync all new tracks from my 'Friends Favorites' playlist to my 'Discovery' folder.`
* `Check if any of my followed curators have updated their playlists today.`
* `Find the latest tracks added to my network's playlists and add them to my 'New Music' queue.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your music discovery logic.
* Use a model capable of logical reasoning to filter tracks based on your preferences.
* Set the system prompt to prioritize discovery of new artists over existing library content.
* Ensure the agent is configured to handle API error responses gracefully.

### 2) Composio Toolset Node
* Provide your Spotify API credentials within the Composio dashboard.
* Ensure the connection scope includes `playlist-read-private`, `playlist-modify-public`, and `user-library-modify`.

### 3) Tool Availability
* `spotify_get_playlist_tracks`: Fetches current tracks from a specified playlist.
* `spotify_add_tracks_to_playlist`: Adds identified tracks to your target library.
* `spotify_get_followed_playlists`: Retrieves a list of playlists you are currently following.

---

## Related Solutions
* [Workout Music Optimizer (Spotify)](../workout-music-optimizer-by-spotify/README.md) - Tailor your workout playlists for maximum intensity.
* [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) - Gain deep insights into your video content performance.
* [Abandoned Cart Recovery Agent (Klaviyo)](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate marketing outreach for recovered sales.
