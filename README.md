# ICEINMYVEIN Giveaway Tool

A lightweight, open-source, client-side giveaway tool for Kick.com chat.

## Features
- **Random.org API Integration**: Uses real, verifiable numbers from Random.org's API to draw winners.
- **Secure Fallback**: If Random.org is offline or rate-limited, it automatically falls back to secure browser-native cryptographic random generation (`window.crypto.getRandomValues`).
- **Customizable Rules**: Filter by subscription status, follow age, custom keyword, and more.
- **Multiple Visualizations**: Wheel spin, Slot machine (Classic), and Scramble animations.

---

## How to Get It Running

Since this is a client-side static application, it doesn't require any installation or server-side setup.

### Method 1: Just Double-Click (Easiest)
1. Extract the ZIP file contents to a folder.
2. Double-click the `index.html` file.
3. It will open directly in your default web browser (Chrome, Firefox, Edge, Safari, etc.).

### Method 2: Run a Simple Local Server
If you want to run it via a local URL:
1. Open your terminal/command prompt inside the extracted folder.
2. Start a simple static server (e.g., using Python):
   ```bash
   python -m http.server 8000
   ```
3. Open your browser and navigate to `http://localhost:8000`.
