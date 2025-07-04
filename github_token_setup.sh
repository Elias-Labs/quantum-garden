#!/bin/bash

echo "🔐 GitHub Token Setup for Quantum Garden"
echo "======================================"
echo ""
echo "To automate everything, we need a GitHub Personal Access Token."
echo ""
echo "I'll open the GitHub token creation page with the right settings."
echo "You'll need to:"
echo "1. Click 'Generate new token (classic)'"
echo "2. Name it: 'Quantum Garden Setup'"
echo "3. Select these scopes:"
echo "   ✓ repo (all)"
echo "   ✓ admin:org (for creating organizations)"
echo "4. Click 'Generate token' at the bottom"
echo "5. Copy the token (it looks like: ghp_...)"
echo ""
echo "Opening GitHub token page in 3 seconds..."
sleep 3

# Open the token creation page with pre-selected scopes
open "https://github.com/settings/tokens/new?scopes=repo,admin:org&description=Quantum%20Garden%20Setup"

echo ""
echo "After creating the token, paste it here (it will be hidden):"
read -s GITHUB_TOKEN

# Save token to environment
export GH_TOKEN="$GITHUB_TOKEN"

echo ""
echo "✅ Token saved! Now creating repository..."
echo ""

# Create the repository
gh repo create quantum-garden \
  --public \
  --description "AI Agent Orchestration Platform - Build your own AI civilization with specialized insect agents" \
  --source . \
  --remote origin \
  --push

echo ""
echo "🎉 Success! Your repository is live at:"
echo "   https://github.com/$(gh api user -q .login)/quantum-garden"
echo ""
echo "📋 To transfer to elias-labs organization later:"
echo "   gh repo transfer quantum-garden elias-labs"