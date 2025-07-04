#!/bin/bash

echo "🌟 Quantum Garden - AI Agent Orchestration Platform"
echo "=================================================="
echo ""
echo "Checking Python installation..."

# Check Python version
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ Python not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Found Python: $($PYTHON_CMD --version)"
echo ""

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    source venv/bin/activate
    
    echo "📦 Installing dependencies..."
    pip install rich typer click asyncio
else
    source venv/bin/activate
fi

echo ""
echo "🚀 Starting Firefly Email Demo..."
echo ""

# Run the demo
$PYTHON_CMD examples/firefly_demo.py