# ASCII Art Generator 🎨 - ULTIMATE EDITION

The most feature-rich ASCII art generator available! Convert text into stunning ASCII art with **10 font styles**, **21 color options** including gradients, **background colors**, **text effects**, and **PNG export**.

## 🆕 What's New in Ultimate Edition

- 🎨 **3 New Font Styles**: 3D, Script, and Graffiti
- 🌈 **8 New Color Options**: Fire, Ocean, Forest, Sunset gradients + 3 gradient directions
- 🎭 **12 Background Colors**: Full ANSI background color support
- ✨ **3 Text Effects**: Underline, Border, and Outline
- 💾 **PNG Export**: Save your creations as images
- 🚀 **Enhanced CLI**: Beautiful interactive interface with emojis

## ✨ Features

### 🎨 10 Unique Font Styles
- **Block** - Bold block letters (#)
- **Slant** - Slanted/diagonal style (/\)
- **Mini** - Compact mini style
- **Shadow** - Bold with shadow effect (█)
- **Bubble** - Rounded and bubbly (▄▀)
- **Double** - Double-lined box drawing (╔╗)
- **Banner** - Simple banner style
- **3D** - 3D depth effect 🆕
- **Script** - Elegant cursive style 🆕
- **Graffiti** - Street art style 🆕

### 🌈 21 Color Options
- **13 Solid Colors**: Red, Green, Yellow, Blue, Cyan, Magenta + Bright variants
- **Rainbow Mode**: Each character cycles through colors 🌈
- **4 Themed Gradients**: Fire 🔥, Ocean 🌊, Forest 🌲, Sunset 🌅
- **3 Gradient Directions**: Horizontal, Vertical, Diagonal

### 🎭 Background Colors
- **12 Background Options**: Full range of ANSI background colors including bright variants

### ✨ Text Effects
- **Underline**: Add underline under text
- **Border**: Wrap text in a box border
- **Outline**: Add outline frame around text

### 💾 Image Export
- **PNG Export**: Export your creations as PNG images
- **Customizable**: Choose filename and maintain visual fidelity

### 🚀 More Features
- **Standalone Executable**: Works on Mac/Linux without Python installation
- **Interactive CLI**: Beautiful, easy-to-use command-line interface
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

### Shadow Style (Bold with Shadow Effect)

```
██    ██   ████████
██    ██      ██
████████      ██
██    ██      ██
██    ██   ████████
```

### Bubble Style (Rounded and Bubbly)

```
 █ █   █
 █▀█   █
```

### Double Style (Box Drawing)

```
 ╦ ╦   ╦
 ╠═╣   ║
 ╩ ╩   ╩
```

### Rainbow Mode 🌈

All styles support rainbow colors where each character cycles through:
Red → Yellow → Green → Cyan → Blue → Magenta

## Supported Characters

- **Letters**: A-Z (automatically converted to uppercase)
- **Numbers**: 0-9
- **Punctuation**: Space, !, ?
- Unsupported characters are replaced with '?'

## Style Descriptions

| Style    | Characters | Height | Description | Best For |
|----------|-----------|--------|-------------|----------|
| Block    | `#` | 5 | Bold, blocky letters | Headlines, banners |
| Slant    | `/\` | 5 | Diagonal, dynamic style | Modern, stylish text |
| Mini     | `_/\|` | 3 | Compact, minimal | Space-constrained displays |
| Shadow   | `█` | 5 | Bold with shadow effect | Eye-catching headers |
| Bubble   | `▄▀█` | 2 | Rounded and bubbly | Fun, playful text |
| Double   | `╔╗╚╝` | 3 | Double-lined box drawing | Elegant, professional |
| Banner   | `#` | 4-5 | Simple banner style | Classic look |
| **3D** 🆕 | `_/\|` | 5 | 3D depth with shadows | Standout text |
| **Script** 🆕 | `//\` | 3 | Elegant cursive | Sophisticated, artsy |
| **Graffiti** 🆕 | `█▀▄` | 3 | Street art style | Urban, edgy vibes |

## Color & Gradient Options

The generator supports **21 color options**:

### Solid Colors
- **Standard**: Red, Green, Yellow, Blue, Cyan, Magenta
- **Bright**: Bright Red, Bright Green, Bright Yellow, Bright Blue, Bright Cyan, Bright Magenta

### Special Effects
- **Rainbow** 🌈: Each character cycles through 6 colors (Red → Yellow → Green → Cyan → Blue → Magenta)

### Themed Gradients
- **Fire** 🔥: Red → Bright Red → Yellow → Bright Yellow
- **Ocean** 🌊: Blue → Bright Blue → Cyan → Bright Cyan
- **Forest** 🌲: Green → Bright Green (alternating)
- **Sunset** 🌅: Magenta → Red → Yellow → Bright Yellow

### Gradient Directions
- **Horizontal**: Colors change left to right
- **Vertical**: Colors change top to bottom
- **Diagonal**: Colors change diagonally

## Background Colors & Effects

### Backgrounds
12 background color options including black, red, green, yellow, blue, magenta, cyan, white, and bright variants

### Text Effects
- **Underline**: Adds `====` under your text
- **Border**: Wraps text in `┌─┐│└┘` box characters
- **Outline**: Frames text with `█▄▀` characters

## 💡 Tips & Tricks

- **Preview All**: Use the "all" option to see your text in all 10 styles at once
- **Gradient Magic**: Try themed gradients (fire, ocean, sunset) for stunning effects
- **Background Pop**: Combine bright foreground colors with dark backgrounds for maximum contrast
- **3D Effect**: The 3D style looks amazing with fire or sunset gradients
- **Graffiti Style**: Works great with rainbow colors for authentic street art vibes
- **Export to Share**: Use PNG export to save and share your creations
- **Text Effects**: Border and outline effects work great for making text stand out
- **Keep it Short**: 1-10 characters work best for readability
- **Terminal Support**: Your terminal must support ANSI colors for colored output
- **Experiment**: Try combining different styles, colors, backgrounds, and effects!

## 💾 PNG Export

Export your ASCII art as PNG images:

```bash
# During interactive mode, choose 'y' when prompted
# Or programmatically in Python:
from ascii_art import generate_ascii_art, export_to_png

art = generate_ascii_art("HELLO", style='3d', color='fire', effect='border')
export_to_png(art, 'my_art.png')
```

Requirements: `pip install Pillow`

## 🎯 Awesome Combinations to Try

Here are some stunning combinations to get you started:

### 🔥 Fire Effect
- Style: **3D** or **Shadow**
- Color: **Fire gradient**
- Effect: **Border**
- Result: Eye-catching 3D text with fiery colors

### 🌊 Ocean Vibes
- Style: **Script** or **Bubble**
- Color: **Ocean gradient**
- Background: **Bright Blue**
- Result: Smooth, flowing oceanic text

### 🎨 Rainbow Graffiti
- Style: **Graffiti**
- Color: **Rainbow**
- Effect: **Outline**
- Result: Authentic street art with rainbow colors

### 🌅 Sunset Elegance
- Style: **Script** or **Double**
- Color: **Sunset gradient**
- Effect: **Border**
- Result: Elegant text with warm sunset hues

### ⚡ Maximum Impact
- Style: **Shadow**
- Color: **Bright Yellow**
- Background: **Black**
- Effect: **Outline**
- Result: Bold, high-contrast attention grabber

## Examples to Try

```bash
# With executable
./dist/ascii-art HELLO
./dist/ascii-art CODE
./dist/ascii-art 2024
./dist/ascii-art "WOW!"

# With Python
python3 ascii_art.py HELLO
python3 ascii_art.py CODE

# Try these specific combinations:
# 3D style with fire gradient and border
# Graffiti style with rainbow colors
# Script style with sunset gradient
# Shadow style with ocean gradient and blue background
```

## 📊 The Numbers

- **10** Font Styles
- **21** Color Options
- **12** Background Colors
- **4** Text Effects
- **10,080** Total Possible Combinations!

Create millions of unique ASCII art pieces!

## Building from Source

### Requirements
- Python 3.6+
- PyInstaller (automatically installed by build scripts)
- Pillow (optional, for PNG export): `pip install Pillow`

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
