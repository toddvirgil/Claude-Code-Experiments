#!/bin/bash
#
# Build script for ASCII Art Generator
# Creates a standalone executable for Mac/Linux
#

set -e  # Exit on error

echo "======================================"
echo "ASCII Art Generator - Build Script"
echo "======================================"
echo ""

# Check if pyinstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
    echo ""
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist __pycache__
echo "✓ Clean complete"
echo ""

# Build the executable
echo "Building executable..."
pyinstaller --clean ascii_art.spec

if [ -f "dist/ascii-art" ]; then
    echo ""
    echo "======================================"
    echo "✓ Build successful!"
    echo "======================================"
    echo ""
    echo "Executable created at: dist/ascii-art"
    echo ""
    echo "Test it:"
    echo "  ./dist/ascii-art HELLO"
    echo ""
    echo "Install system-wide (optional):"
    echo "  sudo cp dist/ascii-art /usr/local/bin/"
    echo "  sudo chmod +x /usr/local/bin/ascii-art"
    echo ""
else
    echo ""
    echo "✗ Build failed!"
    echo "Check the output above for errors."
    exit 1
fi
