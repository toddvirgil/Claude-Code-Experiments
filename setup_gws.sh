#!/usr/bin/env bash
# setup_gws.sh — Install and configure the Google Workspace CLI (gws)
# Source: https://github.com/googleworkspace/cli

set -euo pipefail

echo "=== Google Workspace CLI (gws) Setup ==="
echo

# Install gws via npm
echo "[1/3] Installing gws..."
if command -v npm &>/dev/null; then
  npm install -g @googleworkspace/cli
else
  echo "npm not found. Install Node.js first: https://nodejs.org"
  exit 1
fi

echo
echo "[2/3] Verify installation..."
gws --version

echo
echo "[3/3] Authenticate..."
echo "You'll need a Google Cloud project with the desired Workspace APIs enabled."
echo "  1. Go to https://console.cloud.google.com/"
echo "  2. Enable APIs (Gmail, Drive, Calendar, Sheets, etc.)"
echo "  3. Create OAuth 2.0 Desktop credentials and note the Client ID/Secret"
echo
gws auth setup   # interactive — prompts for client ID & secret
gws auth login   # opens browser for OAuth consent

echo
echo "=== Setup complete! ==="
echo
echo "Quick-start examples:"
echo "  gws drive files list --params '{\"pageSize\": 10}'"
echo "  gws gmail users messages list --params '{\"userId\": \"me\", \"maxResults\": 5}'"
echo "  gws calendar events list --params '{\"calendarId\": \"primary\"}'"
echo "  gws sheets spreadsheets create --json '{\"properties\": {\"title\": \"My Sheet\"}}'"
echo
echo "Explore available commands:"
echo "  gws --help"
echo "  gws schema drive.files.list"
