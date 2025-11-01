# ASCII Art Generator 🎨

A simple and fun ASCII art generator that converts text into various ASCII art styles. Available as a **standalone executable** (no Python required!) or as a Python script.

## Features

- **3 Different Styles**: Block, Slant, and Mini fonts
- **Standalone Executable**: Works on Mac/Linux without Python installation
- **Interactive CLI**: Easy-to-use command-line interface
- **Command-line Arguments**: Quick generation by passing text as arguments
- **Full Alphabet & Numbers**: Supports A-Z, 0-9, and basic punctuation

## Quick Start (Standalone Executable)

### Build the Executable

```bash
# Using Make
make build

# Or using the build script
./build.sh
```

### Run It

```bash
# Interactive mode
./dist/ascii-art

# Quick mode - pass text as arguments
./dist/ascii-art HELLO
```

### Install System-Wide (Optional)

```bash
# Install to /usr/local/bin
make install

# Now you can run from anywhere!
ascii-art HELLO
```

## Alternative: Run with Python

If you prefer to run the Python script directly:

```bash
chmod +x ascii_art.py
python3 ascii_art.py HELLO
```

## Usage

### Interactive Mode

Run without arguments for interactive mode:

```bash
./dist/ascii-art
```

You'll be prompted to:
1. Enter your text
2. Choose a style (block, slant, mini, or all)

### Command-line Mode

Pass your text as arguments for instant results:

```bash
./dist/ascii-art HELLO
./dist/ascii-art CODE
./dist/ascii-art "HI!"
```

## Examples

### Block Style (Bold and Classic)

```
  ###     ###     ##      ##      #####
 ## ##   ## ##   ##      ##     ##   ##
#######  #######  ##      ##     ##   ##
##   ##  ##   ##  ##      ##     ##   ##
##   ##  ##   ##  ####### ####### #####
```

### Slant Style (Dynamic and Diagonal)

```
    ___     ____    ______   ____    ____
   /   |   / __ )  / ____/  / __ \  / __/
  / /| |  / __  | / /      / / / / / _/
 / ___ | / /_/ / / /___   / /_/ / / /___
/_/  |_|/_____/  \____/  /_____/  \____/
```

### Mini Style (Compact and Cute)

```
 _   ___   _
/_\ | __| /_\
    | _|
    |_|
```

## Supported Characters

- **Letters**: A-Z (automatically converted to uppercase)
- **Numbers**: 0-9
- **Punctuation**: Space, !, ?
- Unsupported characters are replaced with '?'

## Style Descriptions

| Style  | Description | Best For |
|--------|-------------|----------|
| Block  | Bold, blocky letters with # symbols | Headlines, banners |
| Slant  | Diagonal, dynamic style with / and \ | Modern, stylish text |
| Mini   | Compact, 3-line height | Space-constrained displays |

## Tips

- Use the "all" option to preview your text in all styles at once
- Keep text short (1-10 characters) for best results
- Great for creating banners, headers, or fun messages!

## Examples to Try

```bash
# With executable
./dist/ascii-art HELLO
./dist/ascii-art CODE
./dist/ascii-art 2024
./dist/ascii-art "HI!"

# With Python
python3 ascii_art.py HELLO
python3 ascii_art.py CODE
```

## Building from Source

### Requirements
- Python 3.6+
- PyInstaller (automatically installed by build scripts)

### Build Commands

```bash
# Build the executable
make build

# Clean build artifacts
make clean

# Build and install system-wide
make install

# Show help
make help
```

### Build Files
- `Makefile` - Build automation
- `build.sh` - Shell script for building
- `ascii_art.spec` - PyInstaller configuration

## Contributing

Feel free to add more fonts or features! The code is structured to make adding new fonts easy - just add a new dictionary following the existing pattern.

## File Structure

```
.
├── ascii_art.py       # Main Python script
├── ascii_art.spec     # PyInstaller spec file
├── build.sh           # Build script
├── Makefile           # Build automation
├── dist/
│   └── ascii-art      # Standalone executable (after build)
└── README.md          # This file
```

## License

Open source experiment - use freely!
