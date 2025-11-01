# ASCII Art Generator 🎨

A simple and fun Python-based ASCII art generator that converts text into various ASCII art styles.

## Features

- **3 Different Styles**: Block, Slant, and Mini fonts
- **Interactive CLI**: Easy-to-use command-line interface
- **Command-line Arguments**: Quick generation by passing text as arguments
- **Full Alphabet & Numbers**: Supports A-Z, 0-9, and basic punctuation

## Installation

No dependencies required! Just Python 3.6+

```bash
chmod +x ascii_art.py
```

## Usage

### Interactive Mode

Run the script without arguments for interactive mode:

```bash
python3 ascii_art.py
```

You'll be prompted to:
1. Enter your text
2. Choose a style (block, slant, mini, or all)

### Command-line Mode

Pass your text as arguments:

```bash
python3 ascii_art.py HELLO
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
python3 ascii_art.py HELLO
python3 ascii_art.py CODE
python3 ascii_art.py 2024
python3 ascii_art.py "HI!"
```

## Contributing

Feel free to add more fonts or features! The code is structured to make adding new fonts easy - just add a new dictionary following the existing pattern.

## License

Open source experiment - use freely!
