.PHONY: build clean install help

# Build the executable
build:
	@echo "Building ASCII Art executable..."
	pyinstaller --clean ascii_art.spec
	@echo ""
	@echo "✓ Build complete!"
	@echo "Executable location: dist/ascii-art"
	@echo ""
	@echo "To install system-wide, run: make install"

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build dist __pycache__ *.pyc
	@echo "✓ Clean complete!"

# Install to /usr/local/bin (requires sudo on Mac)
install: build
	@echo "Installing to /usr/local/bin..."
	@if [ ! -f dist/ascii-art ]; then \
		echo "Error: Executable not found. Run 'make build' first."; \
		exit 1; \
	fi
	@sudo cp dist/ascii-art /usr/local/bin/
	@sudo chmod +x /usr/local/bin/ascii-art
	@echo ""
	@echo "✓ Installation complete!"
	@echo "You can now run 'ascii-art' from anywhere!"

# Show help
help:
	@echo "ASCII Art Generator - Build Commands"
	@echo ""
	@echo "Available targets:"
	@echo "  make build    - Build the standalone executable"
	@echo "  make clean    - Remove build artifacts"
	@echo "  make install  - Install to /usr/local/bin (requires sudo)"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "Quick start:"
	@echo "  1. make build"
	@echo "  2. ./dist/ascii-art HELLO"
	@echo "  3. make install (optional, for system-wide access)"
