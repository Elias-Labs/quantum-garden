#!/bin/bash

echo "🚀 Quantum Garden GitHub Setup Script"
echo "===================================="

# Check if gh is authenticated
if ! gh auth status &>/dev/null; then
    echo "📋 GitHub CLI needs authentication."
    echo ""
    echo "This will open your browser for secure authentication."
    echo "Press Enter to continue..."
    read
    
    # Start authentication
    gh auth login --hostname github.com --git-protocol https --web
    
    # Wait for user to complete auth
    echo ""
    echo "Complete the authentication in your browser, then press Enter..."
    read
fi

echo "✅ GitHub authenticated!"

# Create organization
echo ""
echo "📁 Creating Elias Labs organization..."
# Note: Organizations must be created via web interface
echo "Organizations can only be created through the GitHub website."
echo ""
echo "Would you like me to:"
echo "1) Create the repository under your personal account (can transfer to org later)"
echo "2) Open the organization creation page in your browser"
echo ""
read -p "Choose option (1 or 2): " choice

if [ "$choice" = "2" ]; then
    echo "Opening GitHub organization creation page..."
    open "https://github.com/organizations/new"
    echo ""
    echo "After creating the organization, run this script again and choose option 1"
    exit 0
fi

# Create repository
echo ""
echo "📦 Creating quantum-garden repository..."
repo_name="quantum-garden"
repo_desc="AI Agent Orchestration Platform - Build your own AI civilization with specialized insect agents"

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Not in the quantum-garden-oss directory"
    exit 1
fi

# Create and push repository
gh repo create "$repo_name" --public --description "$repo_desc" --source . --remote origin --push

echo ""
echo "✅ Repository created and code pushed!"
echo ""
echo "🔗 Your repository is now live at:"
echo "   https://github.com/$(gh api user -q .login)/$repo_name"
echo ""
echo "📋 Next steps:"
echo "   1. Transfer to elias-labs organization when ready"
echo "   2. Set up GitHub Actions CI/CD"
echo "   3. Create the first demo"