#!/bin/bash

# SMSBtc Setup Script
# This script helps you set up the project quickly

set -e  # Exit on error

echo "========================================="
echo "  SMSBtc Setup Script"
echo "========================================="
echo ""

# Check Python version
echo "Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
    echo "✓ Found Python $PYTHON_VERSION"

    # Check if version is 3.10 or higher
    MAJOR=$(echo $PYTHON_VERSION | cut -d '.' -f 1)
    MINOR=$(echo $PYTHON_VERSION | cut -d '.' -f 2)

    if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 10 ]); then
        echo "⚠ Warning: Python 3.10+ recommended (you have $PYTHON_VERSION)"
    fi
else
    echo "✗ Python 3 not found. Please install Python 3.10 or higher."
    exit 1
fi

echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠ Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo "✓ pip upgraded"

echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet
echo "✓ Dependencies installed"

echo ""

# Create .env file if it doesn't exist
if [ -f ".env" ]; then
    echo "⚠ .env file already exists. Skipping..."
else
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
fi

echo ""
echo "========================================="
echo "  Setup Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Activate the virtual environment (if not already active):"
echo "   source venv/bin/activate"
echo ""
echo "2. (Optional) Edit .env file to customize settings:"
echo "   nano .env"
echo ""
echo "3. Run the application:"
echo "   python run.py"
echo ""
echo "4. For production deployment, see DEPLOYMENT.md"
echo ""
echo "5. To test locally with Twilio:"
echo "   - Install ngrok: https://ngrok.com/"
echo "   - Run: ngrok http 5000"
echo "   - Configure Twilio webhook with ngrok URL"
echo ""
echo "For more information, see README.md"
echo ""
echo "Happy coding! 🚀"
echo ""
