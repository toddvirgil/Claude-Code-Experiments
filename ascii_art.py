#!/usr/bin/env python3
"""
ASCII Art Generator
Converts text to various ASCII art styles with color support
"""

# ANSI Color Codes
class Colors:
    """ANSI color codes for terminal output"""
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright foreground colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Bright background colors
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'

COLOR_MAP = {
    'red': Colors.RED,
    'green': Colors.GREEN,
    'yellow': Colors.YELLOW,
    'blue': Colors.BLUE,
    'magenta': Colors.MAGENTA,
    'cyan': Colors.CYAN,
    'white': Colors.WHITE,
    'bright_red': Colors.BRIGHT_RED,
    'bright_green': Colors.BRIGHT_GREEN,
    'bright_yellow': Colors.BRIGHT_YELLOW,
    'bright_blue': Colors.BRIGHT_BLUE,
    'bright_magenta': Colors.BRIGHT_MAGENTA,
    'bright_cyan': Colors.BRIGHT_CYAN,
    'rainbow': 'rainbow',  # Special case
    'gradient_h': 'gradient_horizontal',  # Special case
    'gradient_v': 'gradient_vertical',  # Special case
    'gradient_d': 'gradient_diagonal',  # Special case
    'fire': 'fire',  # Red to yellow gradient
    'ocean': 'ocean',  # Blue to cyan gradient
    'forest': 'forest',  # Green gradient
    'sunset': 'sunset',  # Purple to orange gradient
    'none': ''
}

BG_COLOR_MAP = {
    'none': '',
    'black': Colors.BG_BLACK,
    'red': Colors.BG_RED,
    'green': Colors.BG_GREEN,
    'yellow': Colors.BG_YELLOW,
    'blue': Colors.BG_BLUE,
    'magenta': Colors.BG_MAGENTA,
    'cyan': Colors.BG_CYAN,
    'white': Colors.BG_WHITE,
    'bright_black': Colors.BG_BRIGHT_BLACK,
    'bright_red': Colors.BG_BRIGHT_RED,
    'bright_green': Colors.BG_BRIGHT_GREEN,
    'bright_yellow': Colors.BG_BRIGHT_YELLOW,
    'bright_blue': Colors.BG_BRIGHT_BLUE,
    'bright_magenta': Colors.BG_BRIGHT_MAGENTA,
    'bright_cyan': Colors.BG_BRIGHT_CYAN,
    'bright_white': Colors.BG_BRIGHT_WHITE
}

# Gradient color schemes
GRADIENTS = {
    'gradient_horizontal': [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA],
    'gradient_vertical': [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA],
    'gradient_diagonal': [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.MAGENTA],
    'fire': [Colors.RED, Colors.BRIGHT_RED, Colors.YELLOW, Colors.BRIGHT_YELLOW],
    'ocean': [Colors.BLUE, Colors.BRIGHT_BLUE, Colors.CYAN, Colors.BRIGHT_CYAN],
    'forest': [Colors.GREEN, Colors.BRIGHT_GREEN, Colors.GREEN, Colors.BRIGHT_GREEN],
    'sunset': [Colors.MAGENTA, Colors.RED, Colors.YELLOW, Colors.BRIGHT_YELLOW]
}

# Block Letters Style - Simple and bold
BLOCK_FONT = {
    'A': [
        "  ###  ",
        " ## ## ",
        "#######",
        "##   ##",
        "##   ##"
    ],
    'B': [
        "######",
        "##   ##",
        "######",
        "##   ##",
        "######"
    ],
    'C': [
        " ##### ",
        "##   ##",
        "##     ",
        "##   ##",
        " ##### "
    ],
    'D': [
        "######",
        "##   ##",
        "##   ##",
        "##   ##",
        "######"
    ],
    'E': [
        "#######",
        "##     ",
        "#####  ",
        "##     ",
        "#######"
    ],
    'F': [
        "#######",
        "##     ",
        "#####  ",
        "##     ",
        "##     "
    ],
    'G': [
        " ##### ",
        "##     ",
        "##  ###",
        "##   ##",
        " ##### "
    ],
    'H': [
        "##   ##",
        "##   ##",
        "#######",
        "##   ##",
        "##   ##"
    ],
    'I': [
        "#######",
        "  ##   ",
        "  ##   ",
        "  ##   ",
        "#######"
    ],
    'J': [
        "#######",
        "    ##",
        "    ##",
        "##  ##",
        " #### "
    ],
    'K': [
        "##   ##",
        "##  ## ",
        "#####  ",
        "##  ## ",
        "##   ##"
    ],
    'L': [
        "##     ",
        "##     ",
        "##     ",
        "##     ",
        "#######"
    ],
    'M': [
        "##   ##",
        "### ###",
        "## # ##",
        "##   ##",
        "##   ##"
    ],
    'N': [
        "##   ##",
        "###  ##",
        "## # ##",
        "##  ###",
        "##   ##"
    ],
    'O': [
        " ##### ",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    'P': [
        "######",
        "##   ##",
        "######",
        "##     ",
        "##     "
    ],
    'Q': [
        " ##### ",
        "##   ##",
        "##   ##",
        "##  ###",
        " ######"
    ],
    'R': [
        "######",
        "##   ##",
        "######",
        "##  ## ",
        "##   ##"
    ],
    'S': [
        " ##### ",
        "##     ",
        " ##### ",
        "     ##",
        " ##### "
    ],
    'T': [
        "#######",
        "  ##   ",
        "  ##   ",
        "  ##   ",
        "  ##   "
    ],
    'U': [
        "##   ##",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    'V': [
        "##   ##",
        "##   ##",
        "##   ##",
        " ## ## ",
        "  ###  "
    ],
    'W': [
        "##   ##",
        "##   ##",
        "## # ##",
        "### ###",
        "##   ##"
    ],
    'X': [
        "##   ##",
        " ## ## ",
        "  ###  ",
        " ## ## ",
        "##   ##"
    ],
    'Y': [
        "##   ##",
        " ## ## ",
        "  ###  ",
        "  ##   ",
        "  ##   "
    ],
    'Z': [
        "#######",
        "    ## ",
        "  ###  ",
        " ##    ",
        "#######"
    ],
    ' ': [
        "   ",
        "   ",
        "   ",
        "   ",
        "   "
    ],
    '!': [
        "  ##   ",
        "  ##   ",
        "  ##   ",
        "       ",
        "  ##   "
    ],
    '?': [
        " ##### ",
        "##   ##",
        "    ## ",
        "       ",
        "  ##   "
    ],
    '0': [
        " ##### ",
        "##   ##",
        "##   ##",
        "##   ##",
        " ##### "
    ],
    '1': [
        "  ##   ",
        " ###   ",
        "  ##   ",
        "  ##   ",
        "#######"
    ],
    '2': [
        " ##### ",
        "##   ##",
        "    ## ",
        "  ##   ",
        "#######"
    ],
    '3': [
        " ##### ",
        "     ##",
        "  #### ",
        "     ##",
        " ##### "
    ],
    '4': [
        "##   ##",
        "##   ##",
        "#######",
        "     ##",
        "     ##"
    ],
    '5': [
        "#######",
        "##     ",
        "###### ",
        "     ##",
        "###### "
    ],
    '6': [
        " ##### ",
        "##     ",
        "###### ",
        "##   ##",
        " ##### "
    ],
    '7': [
        "#######",
        "     ##",
        "    ## ",
        "   ##  ",
        "  ##   "
    ],
    '8': [
        " ##### ",
        "##   ##",
        " ##### ",
        "##   ##",
        " ##### "
    ],
    '9': [
        " ##### ",
        "##   ##",
        " ######",
        "     ##",
        " ##### "
    ]
}

# Slant Style - Diagonal and dynamic
SLANT_FONT = {
    'A': [
        "    ___ ",
        "   /   |",
        "  / /| |",
        " / ___ |",
        "/_/  |_|"
    ],
    'B': [
        "    ____ ",
        "   / __ )",
        "  / __  |",
        " / /_/ / ",
        "/_____/  "
    ],
    'C': [
        "  ______",
        " / ____/",
        "/ /     ",
        "/ /___  ",
        "\____/  "
    ],
    'D': [
        "    ____",
        "   / __ \\",
        "  / / / /",
        " / /_/ / ",
        "/_____/  "
    ],
    'E': [
        "   ____",
        "  / __/",
        " / _/  ",
        "/ /___ ",
        "\____/ "
    ],
    'F': [
        "   ____",
        "  / __/",
        " / _/  ",
        "/ /    ",
        "/_/    "
    ],
    'G': [
        "  _______",
        " / ______|",
        "/ / __  ",
        "/ /_/ /  ",
        "\____/   "
    ],
    'H': [
        "   __  __",
        "  / / / /",
        " / /_/ / ",
        "/ __  /  ",
        "/_/ /_/  "
    ],
    'I': [
        "   ____",
        "  /  _/",
        "  / /  ",
        "_/ /   ",
        "/___/  "
    ],
    'J': [
        "     __",
        "    / /",
        "   / / ",
        "  / /  ",
        "_/ /   ",
        "/___/  "
    ],
    'K': [
        "   __ __",
        "  / //_/",
        " / ,<   ",
        "/ /| |  ",
        "/_/ |_| "
    ],
    'L': [
        "   __ ",
        "  / / ",
        " / /  ",
        "/ /___",
        "/_____/"
    ],
    'M': [
        "   __  ___",
        "  /  |/  /",
        " / /|_/ / ",
        "/ /  / /  ",
        "/_/  /_/  "
    ],
    'N': [
        "   _   __",
        "  / | / /",
        " /  |/ / ",
        "/ /|  /  ",
        "/_/ |_/  "
    ],
    'O': [
        "   ____",
        "  / __ \\",
        " / / / /",
        "/ /_/ / ",
        "\____/  "
    ],
    'P': [
        "   ___  ",
        "  / _ \\ ",
        " / ___/ ",
        "/_/     "
    ],
    'Q': [
        "   ____ ",
        "  / __ \\",
        " / / / /",
        "/ /_/ / ",
        "\___\\_\\"
    ],
    'R': [
        "   ___  ",
        "  / _ \\ ",
        " / , _/ ",
        "/_/|_|  "
    ],
    'S': [
        "   _____",
        "  / ___/",
        "  \\__ \\ ",
        " ___/ / ",
        "/____/  "
    ],
    'T': [
        "   ______",
        "  /_  __/",
        "   / /   ",
        "  / /    ",
        " /_/     "
    ],
    'U': [
        "   __  __",
        "  / / / /",
        " / / / / ",
        "/ /_/ /  ",
        "\____/   "
    ],
    'V': [
        "__    __",
        "\\ \\  / /",
        " \\ \\/ / ",
        "  \\  /  ",
        "   \\/   "
    ],
    'W': [
        "   _      __",
        "  | | /| / /",
        "  | |/ |/ / ",
        "  |__/|__/  "
    ],
    'X': [
        "   _  __",
        "  | |/_/",
        " _>  < ",
        "/_/|_| "
    ],
    'Y': [
        "__  __",
        "\\ \\/ /",
        " \\  / ",
        " / /  ",
        "/_/   "
    ],
    'Z': [
        "   ____",
        "  /_  /",
        "   / /_",
        "  /___/"
    ],
    ' ': [
        "   ",
        "   ",
        "   ",
        "   "
    ],
    '!': [
        "   __",
        "  / /",
        " / / ",
        "/_/  ",
        "(_)  "
    ],
    '?': [
        "  ___ ",
        " / _ \\",
        "/_/ / ",
        " /_/  ",
        "(_)   "
    ]
}

# Mini Style - Compact and cute
MINI_FONT = {
    'A': [" _ ", "/_\\", ""],
    'B': ["_  ", "|_)", "|_"],
    'C': [" _ ", "/  ", "\\_"],
    'D': ["_  ", "|_)", "| \\"],
    'E': ["_ ", "|_", "|_"],
    'F': ["_ ", "|_", "| "],
    'G': [" _ ", "/ _", "\\_>"],
    'H': ["_  _", "|__|", "|  |"],
    'I': ["_", "|", "|"],
    'J': [" _", " |", "_|"],
    'K': ["_  ", "|_/", "| \\"],
    'L': ["_  ", "|  ", "|__"],
    'M': ["_  _", "|\\/|", "|  |"],
    'N': ["_  _", "|\\ |", "| \\|"],
    'O': [" _ ", "/ \\", "\\_/"],
    'P': ["_  ", "|_)", "|  "],
    'Q': [" _ ", "/ \\", "\\_|"],
    'R': ["_  ", "|_)", "|  "],
    'S': [" _ ", "/_ ", "\\_"],
    'T': ["___", " | ", " | "],
    'U': ["_  _", "|  |", "|__|"],
    'V': ["_  _", "|  |", " \\/ "],
    'W': ["_  _", "|  |", "|/\\|"],
    'X': ["_  _", " \\/ ", " /\\ "],
    'Y': ["_  _", " \\/ ", " |  "],
    'Z': ["___", " _/", "/__"],
    ' ': ["  ", "  ", "  "],
    '!': ["_", "|", "o"],
    '?': ["_ ", "_)", "o "],
    '0': [" _ ", "/ \\", "\\_/"],
    '1': [" ", "|", "|"],
    '2': ["__", " _)", "|__"],
    '3': ["__", " _)", "__/"],
    '4': ["_  ", "|_|", "  |"],
    '5': ["__", "|_ ", "__/"],
    '6': [" _ ", "|_ ", "|_/"],
    '7': ["__", " /", "/ "],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _/"]
}

# Shadow Style - Bold with shadow effect
SHADOW_FONT = {
    'A': [
        "   ▄████  ",
        "  ██▀▀██  ",
        " ██████   ",
        "██    ██  ",
        "██    ██  "
    ],
    'B': [
        "███████   ",
        "██   ██   ",
        "██████    ",
        "██   ██   ",
        "███████   "
    ],
    'C': [
        " ██████   ",
        "██    ██  ",
        "██        ",
        "██    ██  ",
        " ██████   "
    ],
    'D': [
        "██████    ",
        "██   ██   ",
        "██   ██   ",
        "██   ██   ",
        "██████    "
    ],
    'E': [
        "████████  ",
        "██        ",
        "██████    ",
        "██        ",
        "████████  "
    ],
    'F': [
        "████████  ",
        "██        ",
        "██████    ",
        "██        ",
        "██        "
    ],
    'G': [
        " ██████   ",
        "██        ",
        "██  ████  ",
        "██    ██  ",
        " ██████   "
    ],
    'H': [
        "██    ██  ",
        "██    ██  ",
        "████████  ",
        "██    ██  ",
        "██    ██  "
    ],
    'I': [
        "████████  ",
        "   ██     ",
        "   ██     ",
        "   ██     ",
        "████████  "
    ],
    'J': [
        "████████  ",
        "      ██  ",
        "      ██  ",
        "██    ██  ",
        " ██████   "
    ],
    'K': [
        "██   ██   ",
        "██  ██    ",
        "█████     ",
        "██  ██    ",
        "██   ██   "
    ],
    'L': [
        "██        ",
        "██        ",
        "██        ",
        "██        ",
        "████████  "
    ],
    'M': [
        "██    ██  ",
        "████████  ",
        "██ ██ ██  ",
        "██    ██  ",
        "██    ██  "
    ],
    'N': [
        "██    ██  ",
        "███   ██  ",
        "██ ██ ██  ",
        "██   ███  ",
        "██    ██  "
    ],
    'O': [
        " ██████   ",
        "██    ██  ",
        "██    ██  ",
        "██    ██  ",
        " ██████   "
    ],
    'P': [
        "███████   ",
        "██    ██  ",
        "███████   ",
        "██        ",
        "██        "
    ],
    'Q': [
        " ██████   ",
        "██    ██  ",
        "██    ██  ",
        "██   ███  ",
        " ███████  "
    ],
    'R': [
        "███████   ",
        "██    ██  ",
        "███████   ",
        "██  ██    ",
        "██   ██   "
    ],
    'S': [
        " ██████   ",
        "██        ",
        " ██████   ",
        "      ██  ",
        " ██████   "
    ],
    'T': [
        "████████  ",
        "   ██     ",
        "   ██     ",
        "   ██     ",
        "   ██     "
    ],
    'U': [
        "██    ██  ",
        "██    ██  ",
        "██    ██  ",
        "██    ██  ",
        " ██████   "
    ],
    'V': [
        "██    ██  ",
        "██    ██  ",
        "██    ██  ",
        " ██  ██   ",
        "  ████    "
    ],
    'W': [
        "██    ██  ",
        "██    ██  ",
        "██ ██ ██  ",
        "████████  ",
        "██    ██  "
    ],
    'X': [
        "██    ██  ",
        " ██  ██   ",
        "  ████    ",
        " ██  ██   ",
        "██    ██  "
    ],
    'Y': [
        "██    ██  ",
        " ██  ██   ",
        "  ████    ",
        "   ██     ",
        "   ██     "
    ],
    'Z': [
        "████████  ",
        "     ██   ",
        "   ████   ",
        "  ██      ",
        "████████  "
    ],
    ' ': ["     ", "     ", "     ", "     ", "     "],
    '!': ["  ██  ", "  ██  ", "  ██  ", "      ", "  ██  "],
    '?': [" ████ ", "██  ██", "   ██ ", "      ", "  ██  "],
    '0': [" ████ ", "██  ██", "██  ██", "██  ██", " ████ "],
    '1': ["  ██  ", " ███  ", "  ██  ", "  ██  ", "██████"],
    '2': [" ████ ", "██  ██", "   ██ ", "  ██  ", "██████"],
    '3': [" ████ ", "    ██", "  ███ ", "    ██", " ████ "],
    '4': ["██  ██", "██  ██", "██████", "    ██", "    ██"],
    '5': ["██████", "██    ", "█████ ", "    ██", "█████ "],
    '6': [" ████ ", "██    ", "█████ ", "██  ██", " ████ "],
    '7': ["██████", "    ██", "   ██ ", "  ██  ", " ██   "],
    '8': [" ████ ", "██  ██", " ████ ", "██  ██", " ████ "],
    '9': [" ████ ", "██  ██", " █████", "    ██", " ████ "]
}

# Bubble Style - Rounded and bubbly
BUBBLE_FONT = {
    'A': [
        " ▄▀█ ",
        " █▀█ "
    ],
    'B': [
        " █▄▄ ",
        " █▄█ "
    ],
    'C': [
        " █▀▀ ",
        " █▄▄ "
    ],
    'D': [
        " █▀▄ ",
        " █▄▀ "
    ],
    'E': [
        " █▀▀ ",
        " ██▄ "
    ],
    'F': [
        " █▀▀ ",
        " █▀  "
    ],
    'G': [
        " █▀▀ ",
        " █▄█ "
    ],
    'H': [
        " █ █ ",
        " █▀█ "
    ],
    'I': [
        " █ ",
        " █ "
    ],
    'J': [
        " █▀▀█ ",
        " █▄▄█ "
    ],
    'K': [
        " █▄▀ ",
        " █ █ "
    ],
    'L': [
        " █   ",
        " █▄▄ "
    ],
    'M': [
        " █▀▄▀█ ",
        " █ ▀ █ "
    ],
    'N': [
        " █▄ █ ",
        " █ ▀█ "
    ],
    'O': [
        " █▀█ ",
        " █▄█ "
    ],
    'P': [
        " █▀█ ",
        " █▀  "
    ],
    'Q': [
        " █▀█ ",
        " ▀▀█ "
    ],
    'R': [
        " █▀█ ",
        " █▀▄ "
    ],
    'S': [
        " █▀ ",
        " ▄█ "
    ],
    'T': [
        " ▀█▀ ",
        "  █  "
    ],
    'U': [
        " █ █ ",
        " █▄█ "
    ],
    'V': [
        " █ █ ",
        " ▀▄▀ "
    ],
    'W': [
        " █   █ ",
        " ▀▄▀▄▀ "
    ],
    'X': [
        " ▀▄▀ ",
        " █ █ "
    ],
    'Y': [
        " █ █ ",
        "  █  "
    ],
    'Z': [
        " ▀█ ",
        " █▄ "
    ],
    ' ': ["   ", "   "],
    '!': [" █ ", " ▄ "],
    '?': [" ▀█ ", "  ▄ "],
    '0': [" █▀█ ", " █▄█ "],
    '1': [" ▄█ ", " ░█ "],
    '2': [" ▀█ ", " █▄ "],
    '3': [" ▀▀█ ", " ▄▄█ "],
    '4': [" █ █ ", " ▄▄█ "],
    '5': [" █▀ ", " ▄█ "],
    '6': [" █▀ ", " █▄ "],
    '7': [" ▀▀█ ", " ░░█ "],
    '8': [" █▀█ ", " █▀█ "],
    '9': [" █▀█ ", " ▄▄█ "]
}

# Double Line Style - Double-lined box drawing
DOUBLE_FONT = {
    'A': [
        " ╔═╗ ",
        " ╠═╣ ",
        " ╩ ╩ "
    ],
    'B': [
        " ╔╗  ",
        " ╠╩╗ ",
        " ╚═╝ "
    ],
    'C': [
        " ╔═╗ ",
        " ║   ",
        " ╚═╝ "
    ],
    'D': [
        " ╔╦╗ ",
        " ║║║ ",
        " ╩╚╝ "
    ],
    'E': [
        " ╔═╗ ",
        " ║╣  ",
        " ╚═╝ "
    ],
    'F': [
        " ╔═╗ ",
        " ╠╣  ",
        " ╚   "
    ],
    'G': [
        " ╔═╗ ",
        " ║ ╦ ",
        " ╚═╝ "
    ],
    'H': [
        " ╦ ╦ ",
        " ╠═╣ ",
        " ╩ ╩ "
    ],
    'I': [
        " ╦ ",
        " ║ ",
        " ╩ "
    ],
    'J': [
        "   ╦ ",
        "   ║ ",
        " ╚═╝ "
    ],
    'K': [
        " ╦╔═ ",
        " ╠╩╗ ",
        " ╩ ╩ "
    ],
    'L': [
        " ╦   ",
        " ║   ",
        " ╩═╝ "
    ],
    'M': [
        " ╔╦╗ ",
        " ║║║ ",
        " ╩ ╩ "
    ],
    'N': [
        " ╔╗╔ ",
        " ║║║ ",
        " ╝╚╝ "
    ],
    'O': [
        " ╔═╗ ",
        " ║ ║ ",
        " ╚═╝ "
    ],
    'P': [
        " ╔═╗ ",
        " ╠═╝ ",
        " ╩   "
    ],
    'Q': [
        " ╔═╗ ",
        " ║═╬╗",
        " ╚═╝╚"
    ],
    'R': [
        " ╦═╗ ",
        " ╠╦╝ ",
        " ╩╚═ "
    ],
    'S': [
        " ╔═╗ ",
        " ╚═╗ ",
        " ╚═╝ "
    ],
    'T': [
        " ╔╦╗ ",
        "  ║  ",
        "  ╩  "
    ],
    'U': [
        " ╦ ╦ ",
        " ║ ║ ",
        " ╚═╝ "
    ],
    'V': [
        " ╦  ╦ ",
        " ╚╗╔╝ ",
        "  ╚╝  "
    ],
    'W': [
        " ╦ ╦ ",
        " ║║║ ",
        " ╚╩╝ "
    ],
    'X': [
        " ═╗ ╦ ",
        " ╔╩╦╝ ",
        " ╩ ╚═ "
    ],
    'Y': [
        " ╦ ╦ ",
        " ╚╦╝ ",
        "  ╩  "
    ],
    'Z': [
        " ╔═╗ ",
        "  ╔╝ ",
        " ╚═╝ "
    ],
    ' ': ["    ", "    ", "    "],
    '!': [" ╦ ", " ║ ", " o "],
    '?': [" ═╗ ", "  ╩ ", "  o "],
    '0': [" ╔═╗ ", " ║ ║ ", " ╚═╝ "],
    '1': [" ╔╗ ", "  ║ ", "  ╩ "],
    '2': [" ╔═╗ ", "  ╔╝ ", " ╚═╝ "],
    '3': [" ══╗ ", "  ═╣ ", " ══╝ "],
    '4': [" ╦ ╦ ", " ╚═╣ ", "   ╩ "],
    '5': [" ═══ ", " ╔═╗ ", " ╚═╝ "],
    '6': [" ╔═╗ ", " ╠═╗ ", " ╚═╝ "],
    '7': [" ═══ ", "   ║ ", "   ╩ "],
    '8': [" ╔═╗ ", " ╠═╣ ", " ╚═╝ "],
    '9': [" ╔═╗ ", " ╚═╣ ", " ╚═╝ "]
}

# Banner Style - Simple banner style
BANNER_FONT = {
    'A': [
        "  ##  ",
        " #  # ",
        " #### ",
        " #  # "
    ],
    'B': [
        " ###  ",
        " #  # ",
        " ###  ",
        " #  # ",
        " ###  "
    ],
    'C': [
        "  ### ",
        " #    ",
        " #    ",
        "  ### "
    ],
    'D': [
        " ##   ",
        " # #  ",
        " # #  ",
        " ##   "
    ],
    'E': [
        " #### ",
        " #    ",
        " ###  ",
        " #    ",
        " #### "
    ],
    'F': [
        " #### ",
        " #    ",
        " ###  ",
        " #    ",
        " #    "
    ],
    'G': [
        "  ### ",
        " #    ",
        " # ## ",
        " #  # ",
        "  ### "
    ],
    'H': [
        " #  # ",
        " #  # ",
        " #### ",
        " #  # ",
        " #  # "
    ],
    'I': [
        " ### ",
        "  #  ",
        "  #  ",
        " ### "
    ],
    'J': [
        "   ## ",
        "    # ",
        " #  # ",
        "  ##  "
    ],
    'K': [
        " #  # ",
        " # #  ",
        " ##   ",
        " # #  ",
        " #  # "
    ],
    'L': [
        " #    ",
        " #    ",
        " #    ",
        " #### "
    ],
    'M': [
        " #   # ",
        " ## ## ",
        " # # # ",
        " #   # "
    ],
    'N': [
        " #  # ",
        " ## # ",
        " # ## ",
        " #  # "
    ],
    'O': [
        "  ##  ",
        " #  # ",
        " #  # ",
        "  ##  "
    ],
    'P': [
        " ###  ",
        " #  # ",
        " ###  ",
        " #    "
    ],
    'Q': [
        "  ##  ",
        " #  # ",
        " # ## ",
        "  ### "
    ],
    'R': [
        " ###  ",
        " #  # ",
        " ##   ",
        " # #  ",
        " #  # "
    ],
    'S': [
        "  ### ",
        " #    ",
        "  ##  ",
        "    # ",
        " ###  "
    ],
    'T': [
        " ##### ",
        "   #   ",
        "   #   ",
        "   #   "
    ],
    'U': [
        " #  # ",
        " #  # ",
        " #  # ",
        "  ##  "
    ],
    'V': [
        " #   # ",
        " #   # ",
        "  # #  ",
        "   #   "
    ],
    'W': [
        " #   # ",
        " # # # ",
        " ## ## ",
        " #   # "
    ],
    'X': [
        " #   # ",
        "  # #  ",
        "   #   ",
        "  # #  ",
        " #   # "
    ],
    'Y': [
        " #   # ",
        "  # #  ",
        "   #   ",
        "   #   "
    ],
    'Z': [
        " #### ",
        "    # ",
        "   #  ",
        "  #   ",
        " #### "
    ],
    ' ': ["   ", "   ", "   ", "   "],
    '!': [" # ", " # ", "   ", " # "],
    '?': [" ## ", "  # ", "    ", " #  "],
    '0': [" ## ", " # #", " # #", " ## "],
    '1': [" # ", "## ", " # ", " # "],
    '2': ["## ", " # ", "#  ", "###"],
    '3': ["## ", " ##", " ##", "## "],
    '4': ["# #", "###", "  #", "  #"],
    '5': ["###", "## ", "  #", "## "],
    '6': [" ##", "## ", "# #", "## "],
    '7': ["###", "  #", " # ", " # "],
    '8': [" ##", "###", "# #", "## "],
    '9': [" ##", "# #", " ##", "  #"]
}

# 3D Style - Bold with depth
THREED_FONT = {
    'A': [
        "   ___   ",
        "  /   |  ",
        " / /| |  ",
        "/_/ |_|__",
        "     /_/ "
    ],
    'B': [
        " ___  ",
        "|  _ \\ ",
        "| |_) )",
        "|____/ ",
        "   /_/ "
    ],
    'C': [
        "  ___ ",
        " / __|",
        "| (__ ",
        " \\___|",
        "  /_/ "
    ],
    'D': [
        " ___  ",
        "|  _ \\",
        "| | | |",
        "|_| |_|",
        "   /_/ "
    ],
    'E': [
        " ___ ",
        "|  _|",
        "| |_ ",
        "|___|",
        " /_/ "
    ],
    'F': [
        " ___ ",
        "|  _|",
        "| |  ",
        "|_|  ",
        "/_/  "
    ],
    'G': [
        "  ___ ",
        " / __|",
        "| (_ |",
        " \\___|",
        "  /_/ "
    ],
    'H': [
        " _   _ ",
        "| | | |",
        "| |_| |",
        "|  _  |",
        "|_| |_|"
    ],
    'I': [
        " _ ",
        "| |",
        "| |",
        "|_|",
        "/_/"
    ],
    'J': [
        "    _ ",
        "   | |",
        "   | |",
        " __| |",
        "|___/ "
    ],
    'K': [
        " _  __",
        "| |/ /",
        "| ' / ",
        "| . \\ ",
        "|_|\\_\\"
    ],
    'L': [
        " _    ",
        "| |   ",
        "| |   ",
        "| |__ ",
        "|____|"
    ],
    'M': [
        " __  __ ",
        "|  \\/  |",
        "| |\\/| |",
        "| |  | |",
        "|_|  |_|"
    ],
    'N': [
        " _   _ ",
        "| \\ | |",
        "|  \\| |",
        "| |\\  |",
        "|_| \\_|"
    ],
    'O': [
        "  ___  ",
        " / _ \\ ",
        "| | | |",
        "| |_| |",
        " \\___/ "
    ],
    'P': [
        " ___  ",
        "|  _ \\",
        "| |_) )",
        "|  __/",
        "|_|   "
    ],
    'Q': [
        "  ___  ",
        " / _ \\ ",
        "| | | |",
        "| |_| |",
        " \\__\\_\\"
    ],
    'R': [
        " ___  ",
        "|  _ \\",
        "| |_) )",
        "|  _ / ",
        "|_| \\_\\"
    ],
    'S': [
        " ___ ",
        "/ __|",
        "\\__ \\",
        "|___/",
        "/_/  "
    ],
    'T': [
        " _____",
        "|_   _|",
        "  | |  ",
        "  | |  ",
        "  |_|  "
    ],
    'U': [
        " _   _ ",
        "| | | |",
        "| | | |",
        "| |_| |",
        " \\___/ "
    ],
    'V': [
        "__   __",
        "\\ \\ / /",
        " \\ V / ",
        "  \\_/  ",
        "  /_/  "
    ],
    'W': [
        "__      __",
        "\\ \\    / /",
        " \\ \\  / / ",
        "  \\ \\/ /  ",
        "   \\__/   "
    ],
    'X': [
        "__  __",
        "\\ \\/ /",
        " \\  / ",
        " /  \\ ",
        "/_/\\_\\"
    ],
    'Y': [
        "__   __",
        "\\ \\ / /",
        " \\ V / ",
        "  |_|  ",
        "  /_/  "
    ],
    'Z': [
        " ____",
        "|_  /",
        " / / ",
        "/___|",
        "/_/  "
    ],
    ' ': ["     ", "     ", "     ", "     ", "     "],
    '!': [" _ ", "| |", "|_|", "(_)", "/_/"],
    '?': [" ___ ", "|__ \\", "  /_/", " (_) ", " /_/ "],
    '0': [" ___  ", "/ _ \\ ", "| | | |", "| |_| |", " \\___/ "],
    '1': [" _ ", "/ |", "| |", "|_|", "/_/"],
    '2': [" ___ ", "|_  )", " / / ", "/___|", "/_/  "],
    '3': [" ___ ", "|__ \\", " |_ \\", "|___/", "/_/  "],
    '4': [" _ _  ", "| | | ", "|_  _|", "  |_| ", "  /_/ "],
    '5': [" ___ ", "|  _|", "|_  \\", "|___/", "/_/  "],
    '6': [" __  ", "/ /  ", "| _ \\", "| |_/ ", " \\___/"],
    '7': [" ____ ", "|__  |", "  / / ", " /_/  ", "/_/   "],
    '8': [" ___ ", "( _ )", "/ _ \\", "\\___/", "/_/  "],
    '9': [" ___ ", "|__ \\", " \\_\\ \\", "|___/", "/_/  "]
}

# Script Style - Elegant cursive
SCRIPT_FONT = {
    'A': [
        "  /\\  ",
        " // \\ ",
        "// _ \\"
    ],
    'B': [
        "___   ",
        "// )  ",
        "//___)"
    ],
    'C': [
        " ____ ",
        "//  _)",
        "\\\\___)"
    ],
    'D': [
        "___  ",
        "// \\ ",
        "\\\\__/"
    ],
    'E': [
        "____",
        "//  ",
        "\\\\__"
    ],
    'F': [
        "____",
        "//  ",
        "//  "
    ],
    'G': [
        " ____ ",
        "//  _)",
        "\\\\(_ |"
    ],
    'H': [
        "//  //",
        "//--//",
        "//  //"
    ],
    'I': [
        "//",
        "//",
        "//"
    ],
    'J': [
        "   //",
        "   //",
        " __//"
    ],
    'K': [
        "//  /",
        "///' ",
        "//  \\"
    ],
    'L': [
        "//   ",
        "//   ",
        "\\\\___"
    ],
    'M': [
        "//\\/\\//",
        "//  \\\\/",
        "//    /"
    ],
    'N': [
        "//\\  //",
        "// \\_//",
        "//   //"
    ],
    'O': [
        " ___  ",
        "//   \\",
        "\\\\___/"
    ],
    'P': [
        "___  ",
        "// ) ",
        "//   "
    ],
    'Q': [
        " ___  ",
        "//   \\",
        "\\\\___\\"
    ],
    'R': [
        "___  ",
        "// ) ",
        "// \\ "
    ],
    'S': [
        " ___ ",
        "( _ \\",
        "___) "
    ],
    'T': [
        "_____",
        " // ",
        " // "
    ],
    'U': [
        "//   //",
        "//   //",
        " \\___/ "
    ],
    'V': [
        "\\\\  //",
        " \\\\// ",
        "  \\/  "
    ],
    'W': [
        "\\\\    //",
        " \\\\  // ",
        "  \\/ \\/ "
    ],
    'X': [
        "\\\\ //",
        " >< ",
        "// \\\\"
    ],
    'Y': [
        "\\\\  //",
        " \\\\// ",
        "  //  "
    ],
    'Z': [
        "____",
        " _/ ",
        "/___"
    ],
    ' ': ["   ", "   ", "   "],
    '!': ["//", "//", "o "],
    '?': ["__ ", " _/", " o "],
    '0': [" __ ", "//0\\", "\\__/"],
    '1': ["_/ ", " / ", "/__"],
    '2': ["___ ", " _/ ", "/___"],
    '3': ["___ ", " _/ ", "___/"],
    '4': ["//  ", "//_ ", "  / "],
    '5': ["___ ", "/_  ", "___/"],
    '6': [" __ ", "/_ ", "\\(_/"],
    '7': ["____", "  / ", " /  "],
    '8': [" __ ", "/_\\ ", "\\__/"],
    '9': [" __ ", "/_/ ", " _/ "]
}

# Graffiti Style - Street art style
GRAFFITI_FONT = {
    'A': [
        "  ▄▀█  ",
        " ▄█▄█▄ ",
        "█▀   ▀█"
    ],
    'B': [
        "█▀▀▄ ",
        "█▀▀▄ ",
        "█▄▄▀ "
    ],
    'C': [
        "▄▀▀▀▄",
        "█    ",
        "▀▄▄▄▀"
    ],
    'D': [
        "█▀▀▄ ",
        "█  █ ",
        "█▄▄▀ "
    ],
    'E': [
        "█▀▀▀",
        "█▀▀ ",
        "█▄▄▄"
    ],
    'F': [
        "█▀▀▀",
        "█▀▀ ",
        "█   "
    ],
    'G': [
        "▄▀▀▀▄",
        "█  ▀▄",
        "▀▄▄▄▀"
    ],
    'H': [
        "█   █",
        "█▀▀▀█",
        "█   █"
    ],
    'I': [
        "█",
        "█",
        "█"
    ],
    'J': [
        "   █",
        "   █",
        "▀▄▄▀"
    ],
    'K': [
        "█  █",
        "█▀▀ ",
        "█  █"
    ],
    'L': [
        "█   ",
        "█   ",
        "█▄▄▄"
    ],
    'M': [
        "█▀▄▀█",
        "█ ▀ █",
        "█   █"
    ],
    'N': [
        "█▀▄ █",
        "█ █ █",
        "█  ▀█"
    ],
    'O': [
        "▄▀▀▀▄",
        "█   █",
        "▀▄▄▄▀"
    ],
    'P': [
        "█▀▀▄",
        "█▀▀▀",
        "█   "
    ],
    'Q': [
        "▄▀▀▀▄ ",
        "█   █ ",
        "▀▄▄▄▀▄"
    ],
    'R': [
        "█▀▀▄",
        "█▀▀▄",
        "█  █"
    ],
    'S': [
        "▄▀▀▀▄",
        " ▀▀▀▄",
        "▀▄▄▄▀"
    ],
    'T': [
        "▀▀█▀▀",
        "  █  ",
        "  █  "
    ],
    'U': [
        "█   █",
        "█   █",
        "▀▄▄▄▀"
    ],
    'V': [
        "█   █",
        "▀▄ ▄▀",
        "  ▀  "
    ],
    'W': [
        "█   █",
        "█ ▄ █",
        "▀▀ ▀▀"
    ],
    'X': [
        "▀▄ ▄▀",
        "  █  ",
        "▄▀ ▀▄"
    ],
    'Y': [
        "▀▄ ▄▀",
        "  █  ",
        "  █  "
    ],
    'Z': [
        "▀▀▀█",
        " ▄▀ ",
        "█▄▄▄"
    ],
    ' ': ["   ", "   ", "   "],
    '!': ["█", "█", "▀"],
    '?': ["▀▀█", " ▄▀", " ▀ "],
    '0': ["▄▀▀▄", "█  █", "▀▄▄▀"],
    '1': [" █ ", "▄█ ", " █ "],
    '2': ["▀▀█", " ▄▀", "█▄▄"],
    '3': ["▀▀█", " ▀█", "▄▄▀"],
    '4': ["▄▀█", "▀▀█", "  █"],
    '5': ["█▀▀", "▀▀▄", "▄▄▀"],
    '6': ["▄▀▀", "█▀▄", "▀▄▀"],
    '7': ["▀▀█", "  █", " ▄▀"],
    '8': ["▄▀▄", "▄▀▄", "▀▄▀"],
    '9': ["▄▀▄", "▀▄█", " ▄▀"]
}


def apply_text_effects(lines, effect):
    """Apply text effects like outline, underline, or border"""
    if effect == 'none' or not lines:
        return lines

    if effect == 'underline':
        # Add underline under text
        max_len = max(len(line) for line in lines)
        lines.append('=' * max_len)
        return lines

    elif effect == 'border':
        # Add border around text
        max_len = max(len(line) for line in lines)
        bordered = []
        bordered.append('┌' + '─' * (max_len + 2) + '┐')
        for line in lines:
            bordered.append('│ ' + line.ljust(max_len) + ' │')
        bordered.append('└' + '─' * (max_len + 2) + '┘')
        return bordered

    elif effect == 'outline':
        # Add outline effect (double the characters)
        max_len = max(len(line) for line in lines)
        outlined = []
        outlined.append('▄' * (max_len + 4))
        for line in lines:
            outlined.append('█ ' + line.ljust(max_len) + ' █')
        outlined.append('▀' * (max_len + 4))
        return outlined

    return lines


def generate_ascii_art(text, style='block', color='none', bg_color='none', effect='none'):
    """
    Generate ASCII art from text with optional color, background, and effects

    Args:
        text: String to convert to ASCII art
        style: Font style - 'block', 'slant', 'mini', 'shadow', 'bubble', 'double',
               'banner', '3d', 'script', 'graffiti'
        color: Color option - solid colors, gradients (fire, ocean, forest, sunset,
               gradient_h, gradient_v, gradient_d), rainbow, or 'none'
        bg_color: Background color - any color from BG_COLOR_MAP
        effect: Text effect - 'none', 'underline', 'border', or 'outline'

    Returns:
        ASCII art string with optional color codes and effects
    """
    text = text.upper()

    # Select font
    font_map = {
        'slant': SLANT_FONT,
        'mini': MINI_FONT,
        'shadow': SHADOW_FONT,
        'bubble': BUBBLE_FONT,
        'double': DOUBLE_FONT,
        'banner': BANNER_FONT,
        '3d': THREED_FONT,
        'script': SCRIPT_FONT,
        'graffiti': GRAFFITI_FONT,
        'block': BLOCK_FONT
    }

    font = font_map.get(style, BLOCK_FONT)

    # Handle unsupported characters
    supported_text = ''
    for char in text:
        if char in font:
            supported_text += char
        elif char.isspace():
            supported_text += ' '
        else:
            # Replace unsupported chars with ?
            supported_text += '?'

    if not supported_text.strip():
        return "No supported characters to render"

    # Get height of font
    height = len(font.get('A', ['']))
    text_len = len(supported_text)

    # Get background color code
    bg_code = BG_COLOR_MAP.get(bg_color, '')

    # Build each line
    lines = []
    for row in range(height):
        line = ''
        for char_idx, char in enumerate(supported_text):
            if char in font:
                char_lines = font[char]
                if row < len(char_lines):
                    char_str = char_lines[row]

                    # Determine color for this character
                    fg_color = ''

                    # Handle gradients
                    if color in GRADIENTS:
                        gradient = GRADIENTS[color]
                        if color == 'gradient_horizontal' or color in ['fire', 'ocean', 'forest', 'sunset']:
                            # Horizontal gradient - color changes per character
                            color_idx = int((char_idx / max(text_len - 1, 1)) * (len(gradient) - 1))
                            fg_color = gradient[color_idx]
                        elif color == 'gradient_vertical':
                            # Vertical gradient - color changes per row
                            color_idx = int((row / max(height - 1, 1)) * (len(gradient) - 1))
                            fg_color = gradient[color_idx]
                        elif color == 'gradient_diagonal':
                            # Diagonal gradient - color changes per character + row
                            color_idx = int(((char_idx + row) / max(text_len + height - 2, 1)) * (len(gradient) - 1))
                            fg_color = gradient[color_idx]
                    # Handle rainbow
                    elif color == 'rainbow':
                        rainbow_colors = [
                            Colors.RED, Colors.YELLOW, Colors.GREEN,
                            Colors.CYAN, Colors.BLUE, Colors.MAGENTA
                        ]
                        fg_color = rainbow_colors[char_idx % len(rainbow_colors)]
                    # Handle solid colors
                    elif color in COLOR_MAP and COLOR_MAP[color] and color != 'none':
                        if COLOR_MAP[color] not in ['rainbow', 'gradient_horizontal', 'gradient_vertical', 'gradient_diagonal', 'fire', 'ocean', 'forest', 'sunset']:
                            fg_color = COLOR_MAP[color]

                    # Apply colors
                    if fg_color or bg_code:
                        char_str = f"{bg_code}{fg_color}{char_str}{Colors.RESET}"

                    line += char_str + ' '
                else:
                    line += ' ' * (len(char_lines[0]) + 1)
        lines.append(line.rstrip())

    # Apply text effects
    lines = apply_text_effects(lines, effect)

    return '\n'.join(lines)


def image_to_ascii(image_path, width=80, charset='standard'):
    """
    Convert an image to ASCII art

    Args:
        image_path: Path to image file
        width: Width of ASCII output in characters
        charset: Character set to use - 'standard', 'detailed', or 'blocks'

    Returns:
        ASCII art string
    """
    try:
        from PIL import Image
    except ImportError:
        return "Error: PIL/Pillow not installed. Run: pip install Pillow"

    # Character sets (dark to light)
    charsets = {
        'standard': " .:-=+*#%@",
        'detailed': " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
        'blocks': " ░▒▓█"
    }

    chars = charsets.get(charset, charsets['standard'])

    try:
        # Load and convert image to grayscale
        img = Image.open(image_path)

        # Calculate height to maintain aspect ratio
        aspect_ratio = img.height / img.width
        height = int(width * aspect_ratio * 0.55)  # 0.55 compensates for character height

        # Resize image
        img = img.resize((width, height))
        img = img.convert('L')  # Convert to grayscale

        # Convert pixels to ASCII
        pixels = img.getdata()
        ascii_str = ''

        for i, pixel in enumerate(pixels):
            # Map pixel brightness (0-255) to character
            char_index = int((pixel / 255) * (len(chars) - 1))
            ascii_str += chars[char_index]

            # Add newline at end of row
            if (i + 1) % width == 0:
                ascii_str += '\n'

        return ascii_str.rstrip()

    except FileNotFoundError:
        return f"Error: Image file '{image_path}' not found"
    except Exception as e:
        return f"Error converting image: {str(e)}"


def mirror_text(text_art, direction='horizontal'):
    """Mirror/flip ASCII art"""
    lines = text_art.split('\n')

    if direction == 'horizontal':
        return '\n'.join(line[::-1] for line in lines)
    elif direction == 'vertical':
        return '\n'.join(reversed(lines))
    elif direction == 'both':
        return '\n'.join(line[::-1] for line in reversed(lines))

    return text_art


def rotate_text(text_art, angle=90):
    """Rotate ASCII art by 90, 180, or 270 degrees"""
    lines = text_art.split('\n')

    if angle == 180:
        return '\n'.join(line[::-1] for line in reversed(lines))

    elif angle == 90:
        # Transpose and reverse rows
        max_len = max(len(line) for line in lines)
        padded_lines = [line.ljust(max_len) for line in lines]
        rotated = [''.join(padded_lines[j][i] for j in range(len(padded_lines)-1, -1, -1))
                   for i in range(max_len)]
        return '\n'.join(rotated)

    elif angle == 270:
        # Transpose and reverse columns
        max_len = max(len(line) for line in lines)
        padded_lines = [line.ljust(max_len) for line in lines]
        rotated = [''.join(padded_lines[j][i] for j in range(len(padded_lines)))
                   for i in range(max_len-1, -1, -1)]
        return '\n'.join(rotated)

    return text_art


def stretch_text(text_art, horizontal=1.0, vertical=1.0):
    """Stretch ASCII art horizontally and/or vertically"""
    lines = text_art.split('\n')
    result = []

    for line in lines:
        if horizontal != 1.0:
            # Stretch horizontally by repeating characters
            if horizontal > 1.0:
                stretched_line = ''.join(ch * int(horizontal) for ch in line)
            else:
                # Compress by skipping characters
                step = int(1 / horizontal)
                stretched_line = ''.join(line[i] for i in range(0, len(line), step))
            line = stretched_line

        result.append(line)

    # Stretch vertically by repeating lines
    if vertical != 1.0:
        if vertical > 1.0:
            final_result = []
            for line in result:
                for _ in range(int(vertical)):
                    final_result.append(line)
            result = final_result
        else:
            # Compress by skipping lines
            step = int(1 / vertical)
            result = [result[i] for i in range(0, len(result), step)]

    return '\n'.join(result)


def animate_scroll(text_art, direction='left', speed=0.1, iterations=3):
    """Animate scrolling text"""
    import time
    import os

    lines = text_art.split('\n')
    max_len = max(len(line) for line in lines)

    for _ in range(iterations):
        if direction == 'left':
            for offset in range(max_len):
                os.system('clear' if os.name == 'posix' else 'cls')
                for line in lines:
                    print(line[offset:] + line[:offset])
                time.sleep(speed)
        elif direction == 'right':
            for offset in range(max_len, 0, -1):
                os.system('clear' if os.name == 'posix' else 'cls')
                for line in lines:
                    print(line[offset:] + line[:offset])
                time.sleep(speed)


def animate_typewriter(text_art, speed=0.05):
    """Animate text appearing character by character"""
    import time
    import sys

    for char in text_art:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != '\n':
            time.sleep(speed)


def animate_blink(text_art, times=5, speed=0.5):
    """Make text blink"""
    import time
    import os

    for _ in range(times):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(text_art)
        time.sleep(speed)
        os.system('clear' if os.name == 'posix' else 'cls')
        time.sleep(speed)

    # Show final state
    print(text_art)


# Presets system
import json
import os

PRESETS_FILE = os.path.expanduser('~/.ascii_art_presets.json')

def load_presets():
    """Load saved presets from file"""
    if os.path.exists(PRESETS_FILE):
        try:
            with open(PRESETS_FILE, 'r') as f:
                return json.load(f)
        except:
            pass

    # Default presets
    return {
        'fire_3d': {
            'style': '3d',
            'color': 'fire',
            'bg_color': 'none',
            'effect': 'border',
            'description': 'Eye-catching 3D text with fire gradient and border'
        },
        'ocean_script': {
            'style': 'script',
            'color': 'ocean',
            'bg_color': 'bright_blue',
            'effect': 'none',
            'description': 'Elegant script with ocean colors'
        },
        'rainbow_graffiti': {
            'style': 'graffiti',
            'color': 'rainbow',
            'bg_color': 'none',
            'effect': 'outline',
            'description': 'Rainbow graffiti with outline'
        },
        'sunset_elegant': {
            'style': 'double',
            'color': 'sunset',
            'bg_color': 'none',
            'effect': 'border',
            'description': 'Elegant double-line with sunset gradient'
        },
        'neon_glow': {
            'style': 'shadow',
            'color': 'bright_cyan',
            'bg_color': 'black',
            'effect': 'outline',
            'description': 'Neon glow effect with cyan on black'
        }
    }


def save_presets(presets):
    """Save presets to file"""
    try:
        with open(PRESETS_FILE, 'w') as f:
            json.dump(presets, f, indent=2)
        return True
    except:
        return False


def add_preset(name, style, color, bg_color, effect, description=''):
    """Add a new preset"""
    presets = load_presets()
    presets[name] = {
        'style': style,
        'color': color,
        'bg_color': bg_color,
        'effect': effect,
        'description': description
    }
    return save_presets(presets)


def live_editor():
    """Interactive TUI editor for real-time ASCII art creation"""
    try:
        import curses
    except ImportError:
        return "Error: curses not available on this system"

    def editor_main(stdscr):
        # Setup
        curses.curs_set(1)
        stdscr.clear()

        # Available options
        styles = ['block', 'slant', 'mini', 'shadow', 'bubble', 'double', 'banner', '3d', 'script', 'graffiti']
        colors = ['none', 'red', 'green', 'yellow', 'blue', 'cyan', 'magenta', 'rainbow', 'fire', 'ocean', 'forest', 'sunset']
        effects = ['none', 'underline', 'border', 'outline']

        # Current state
        text = "HELLO"
        current_style = 0
        current_color = 0
        current_effect = 0

        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            # Generate current ASCII art
            try:
                art = generate_ascii_art(
                    text,
                    styles[current_style],
                    colors[current_color],
                    'none',
                    effects[current_effect]
                )
                # Remove ANSI codes for curses display
                import re
                art_clean = re.sub(r'\033\[[0-9;]+m', '', art)
            except:
                art_clean = "Error generating art"

            # Display header
            header = "🎨 LIVE ASCII ART EDITOR 🎨"
            stdscr.addstr(0, (width - len(header)) // 2, header, curses.A_BOLD)

            # Display controls
            stdscr.addstr(2, 2, f"Text: {text}")
            stdscr.addstr(3, 2, f"Style: [{styles[current_style]}] (← → to change)")
            stdscr.addstr(4, 2, f"Color: [{colors[current_color]}] (↑ ↓ to change)")
            stdscr.addstr(5, 2, f"Effect: [{effects[current_effect]}] ([ ] to change)")

            # Display ASCII art preview
            preview_start = 7
            for i, line in enumerate(art_clean.split('\n')[:height-preview_start-5]):
                try:
                    stdscr.addstr(preview_start + i, 2, line[:width-4])
                except:
                    pass

            # Display help
            help_y = height - 3
            stdscr.addstr(help_y, 2, "Commands: Type to change text | ENTER: Done | ESC: Quit", curses.A_DIM)

            # Get input
            stdscr.refresh()
            try:
                key = stdscr.getch()

                if key == 27:  # ESC
                    break
                elif key == 10:  # ENTER
                    return art  # Return the full colored version
                elif key == curses.KEY_RIGHT:
                    current_style = (current_style + 1) % len(styles)
                elif key == curses.KEY_LEFT:
                    current_style = (current_style - 1) % len(styles)
                elif key == curses.KEY_UP:
                    current_color = (current_color + 1) % len(colors)
                elif key == curses.KEY_DOWN:
                    current_color = (current_color - 1) % len(colors)
                elif key == ord('['):
                    current_effect = (current_effect - 1) % len(effects)
                elif key == ord(']'):
                    current_effect = (current_effect + 1) % len(effects)
                elif key == curses.KEY_BACKSPACE or key == 127:
                    text = text[:-1] if text else ""
                elif 32 <= key <= 126:  # Printable characters
                    if len(text) < 20:  # Limit text length
                        text += chr(key)
            except:
                pass

        return None

    try:
        result = curses.wrapper(editor_main)
        return result
    except Exception as e:
        return f"Error in live editor: {str(e)}"


def export_to_png(text_art, filename='ascii_art.png', font_size=12):
    """Export ASCII art to PNG image file"""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return "Error: PIL/Pillow not installed. Run: pip install Pillow"

    # Remove ANSI color codes for PNG export
    import re
    clean_text = re.sub(r'\033\[[0-9;]+m', '', text_art)

    lines = clean_text.split('\n')
    if not lines:
        return "Error: No content to export"

    # Calculate image size
    max_width = max(len(line) for line in lines)
    height_px = len(lines) * (font_size + 4)
    width_px = max_width * (font_size // 2 + 2)

    # Create image
    img = Image.new('RGB', (width_px, height_px), color='black')
    draw = ImageDraw.Draw(img)

    # Try to use a monospace font
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', font_size)
    except:
        try:
            font = ImageFont.truetype('/System/Library/Fonts/Monaco.ttf', font_size)
        except:
            font = ImageFont.load_default()

    # Draw text
    y = 5
    for line in lines:
        draw.text((10, y), line, fill='white', font=font)
        y += font_size + 4

    # Save image
    img.save(filename)
    return f"✓ Exported to {filename}"


def main():
    """CLI interface for ASCII art generator - ULTIMATE EDITION"""
    import sys

    print("=" * 90)
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}ASCII ART GENERATOR - ULTIMATE EDITION v2.0{Colors.RESET}")
    print("=" * 90)

    # Mode selection
    print("\n" + Colors.BOLD + "🚀 Select Mode:" + Colors.RESET)
    print("  1. 📝 Text to ASCII    - Convert text to ASCII art")
    print("  2. 🖼️  Image to ASCII   - Convert image file to ASCII")
    print("  3. 🎨 Live Editor      - Interactive real-time editor")
    print("  4. ⚡ Use Preset       - Quick start with saved presets")
    print("  5. 🎬 Animation Demo   - See animation effects")

    mode = input("\nChoose mode (1-5, default=1): ").strip() or "1"

    # MODE 2: Image to ASCII
    if mode == '2':
        image_path = input("\n📁 Enter image file path: ").strip()
        if not image_path:
            print("No image path provided!")
            return

        width = input("Width in characters (default=80): ").strip()
        width = int(width) if width else 80

        print("\nCharacter set:")
        print("  1. standard - Simple (default)")
        print("  2. detailed - High detail")
        print("  3. blocks   - Block characters")
        charset_choice = input("Choose (1-3): ").strip() or "1"
        charset_map = {'1': 'standard', '2': 'detailed', '3': 'blocks'}
        charset = charset_map.get(charset_choice, 'standard')

        print("\n" + "=" * 90)
        result = image_to_ascii(image_path, width, charset)
        print(result)
        print("=" * 90)

        # Offer to save
        save = input("\n💾 Save to file? (y/N): ").strip().lower()
        if save == 'y':
            filename = input("Filename (default: ascii_image.txt): ").strip() or "ascii_image.txt"
            with open(filename, 'w') as f:
                f.write(result)
            print(f"✓ Saved to {filename}")
        return

    # MODE 3: Live Editor
    elif mode == '3':
        print("\n🎨 Launching live editor...")
        print("Use arrow keys to change style/color, type to change text, ENTER when done")
        input("Press ENTER to continue...")
        result = live_editor()
        if result:
            print("\n" + "=" * 90)
            print(result)
            print("=" * 90)
        return

    # MODE 4: Presets
    elif mode == '4':
        presets = load_presets()
        print("\n⚡ Available Presets:")
        for i, (name, preset) in enumerate(presets.items(), 1):
            print(f"  {i}. {name:20} - {preset.get('description', '')}")

        preset_choice = input("\nChoose preset (1-5): ").strip()
        if preset_choice.isdigit() and 1 <= int(preset_choice) <= len(presets):
            preset_name = list(presets.keys())[int(preset_choice) - 1]
            preset = presets[preset_name]

            text = input("\nEnter text: ").strip()
            if not text:
                text = "PRESET"

            print("\n" + "=" * 90)
            result = generate_ascii_art(
                text,
                preset['style'],
                preset['color'],
                preset.get('bg_color', 'none'),
                preset.get('effect', 'none')
            )
            print(result)
            print("=" * 90)
        return

    # MODE 5: Animation Demo
    elif mode == '5':
        text = input("\nEnter text for demo: ").strip() or "DEMO"
        art = generate_ascii_art(text, 'shadow', 'bright_cyan')

        print("\n" + Colors.BOLD + "Animation Options:" + Colors.RESET)
        print("  1. Typewriter effect")
        print("  2. Scroll left")
        print("  3. Blink")

        anim_choice = input("\nChoose animation (1-3): ").strip()

        if anim_choice == '1':
            print("\n")
            animate_typewriter(art, speed=0.03)
        elif anim_choice == '2':
            animate_scroll(art, 'left', speed=0.05, iterations=2)
        elif anim_choice == '3':
            animate_blink(art, times=3, speed=0.3)
        return

    # MODE 1: Text to ASCII (default)
    # Get text input
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("\nEnter text to convert: ").strip()
        if not text:
            print("No text provided!")
            return

    # Show available styles
    print("\n" + Colors.BOLD + "🎨 Font Styles:" + Colors.RESET)
    print("  1. block     - Bold block letters (#)")
    print("  2. slant     - Slanted/diagonal style (/\\)")
    print("  3. mini      - Compact mini style")
    print("  4. shadow    - Bold with shadow effect (█)")
    print("  5. bubble    - Rounded and bubbly (▄▀)")
    print("  6. double    - Double-lined box drawing (╔╗)")
    print("  7. banner    - Simple banner style")
    print(f"  8. {Colors.BRIGHT_YELLOW}3d{Colors.RESET}        - 3D depth effect")
    print(f"  9. {Colors.BRIGHT_MAGENTA}script{Colors.RESET}    - Elegant cursive style")
    print(f" 10. {Colors.BRIGHT_GREEN}graffiti{Colors.RESET}  - Street art style")
    print(" 11. all       - Show all styles")

    style_choice = input("\nChoose style (1-11, default=1): ").strip() or "1"

    style_map = {
        '1': 'block', '2': 'slant', '3': 'mini', '4': 'shadow',
        '5': 'bubble', '6': 'double', '7': 'banner', '8': '3d',
        '9': 'script', '10': 'graffiti', '11': 'all'
    }

    style = style_map.get(style_choice, 'block')

    # Color and effect selection (only if not showing all)
    color = 'none'
    bg_color = 'none'
    effect = 'none'
    export_png = False

    if style != 'all':
        # Color selection
        print("\n" + Colors.BOLD + "🌈 Color Options:" + Colors.RESET)
        print("  1. none")
        print(f"  2. {Colors.RED}red{Colors.RESET}            7. {Colors.MAGENTA}magenta{Colors.RESET}          12. {Colors.BRIGHT_CYAN}bright_cyan{Colors.RESET}")
        print(f"  3. {Colors.GREEN}green{Colors.RESET}          8. {Colors.BRIGHT_RED}bright_red{Colors.RESET}      13. {Colors.BRIGHT_MAGENTA}bright_magenta{Colors.RESET}")
        print(f"  4. {Colors.YELLOW}yellow{Colors.RESET}         9. {Colors.BRIGHT_GREEN}bright_green{Colors.RESET}    14. rainbow 🌈")
        print(f"  5. {Colors.BLUE}blue{Colors.RESET}          10. {Colors.BRIGHT_YELLOW}bright_yellow{Colors.RESET}   15. {Colors.RED}fire{Colors.RESET} 🔥")
        print(f"  6. {Colors.CYAN}cyan{Colors.RESET}          11. {Colors.BRIGHT_BLUE}bright_blue{Colors.RESET}     16. {Colors.BLUE}ocean{Colors.RESET} 🌊")
        print(f"                            17. {Colors.GREEN}forest{Colors.RESET} 🌲")
        print(f"                            18. {Colors.MAGENTA}sunset{Colors.RESET} 🌅")
        print(f"                            19. gradient_h (horizontal)")
        print(f"                            20. gradient_v (vertical)")
        print(f"                            21. gradient_d (diagonal)")

        color_choice = input("\nChoose color (1-21, default=1): ").strip() or "1"

        color_map = {
            '1': 'none', '2': 'red', '3': 'green', '4': 'yellow',
            '5': 'blue', '6': 'cyan', '7': 'magenta', '8': 'bright_red',
            '9': 'bright_green', '10': 'bright_yellow', '11': 'bright_blue',
            '12': 'bright_cyan', '13': 'bright_magenta', '14': 'rainbow',
            '15': 'fire', '16': 'ocean', '17': 'forest', '18': 'sunset',
            '19': 'gradient_h', '20': 'gradient_v', '21': 'gradient_d'
        }

        color = color_map.get(color_choice, 'none')

        # Background color selection
        print("\n" + Colors.BOLD + "🎭 Background Color (optional):" + Colors.RESET)
        print("  1. none (default)    5. blue     9. bright_green")
        print("  2. black             6. magenta 10. bright_blue")
        print("  3. red               7. cyan    11. bright_cyan")
        print("  4. green             8. white   12. bright_magenta")

        bg_choice = input("\nChoose background (1-12, default=1): ").strip() or "1"

        bg_map = {
            '1': 'none', '2': 'black', '3': 'red', '4': 'green',
            '5': 'blue', '6': 'magenta', '7': 'cyan', '8': 'white',
            '9': 'bright_green', '10': 'bright_blue',
            '11': 'bright_cyan', '12': 'bright_magenta'
        }

        bg_color = bg_map.get(bg_choice, 'none')

        # Text effects
        print("\n" + Colors.BOLD + "✨ Text Effects:" + Colors.RESET)
        print("  1. none (default)")
        print("  2. underline  - Add underline")
        print("  3. border     - Add box border")
        print("  4. outline    - Add outline frame")

        effect_choice = input("\nChoose effect (1-4, default=1): ").strip() or "1"

        effect_map = {
            '1': 'none',
            '2': 'underline',
            '3': 'border',
            '4': 'outline'
        }

        effect = effect_map.get(effect_choice, 'none')

        # Export option
        export_choice = input("\n💾 Export to PNG? (y/N): ").strip().lower()
        export_png = export_choice == 'y'

    print("\n" + "=" * 80)

    if style == 'all':
        all_styles = ['block', 'slant', 'mini', 'shadow', 'bubble', 'double', 'banner', '3d', 'script', 'graffiti']
        for s in all_styles:
            print(f"\n{Colors.BOLD}{s.upper()} STYLE:{Colors.RESET}")
            print("-" * 80)
            result = generate_ascii_art(text, s, 'none', 'none', 'none')
            print(result)
            print()
    else:
        result = generate_ascii_art(text, style, color, bg_color, effect)

        # Transform options
        print("\n" + Colors.BOLD + "🔄 Transform Options (optional):" + Colors.RESET)
        print("  1. none       5. stretch 2x horizontal")
        print("  2. mirror_h   6. stretch 2x vertical")
        print("  3. mirror_v   7. compress horizontal")
        print("  4. rotate_90")

        transform_choice = input("\nChoose transform (1-7, default=1): ").strip() or "1"

        if transform_choice == '2':
            result = mirror_text(result, 'horizontal')
        elif transform_choice == '3':
            result = mirror_text(result, 'vertical')
        elif transform_choice == '4':
            result = rotate_text(result, 90)
        elif transform_choice == '5':
            result = stretch_text(result, horizontal=2.0)
        elif transform_choice == '6':
            result = stretch_text(result, vertical=2.0)
        elif transform_choice == '7':
            result = stretch_text(result, horizontal=0.5)

        print(result)

        # Post-processing options
        print("\n" + Colors.BOLD + "💫 Additional Options:" + Colors.RESET)
        print("  1. 💾 Export to PNG")
        print("  2. 🎬 Animate")
        print("  3. 💾 Save preset")
        print("  4. ✅ Done")

        post_choice = input("\nChoose option (1-4, default=4): ").strip() or "4"

        if post_choice == '1' and export_png or post_choice == '1':
            print("\n" + "-" * 90)
            filename = input("Enter filename (default: ascii_art.png): ").strip() or "ascii_art.png"
            if not filename.endswith('.png'):
                filename += '.png'
            export_result = export_to_png(result, filename)
            print(export_result)

        elif post_choice == '2':
            print("\n" + Colors.BOLD + "Animation:" + Colors.RESET)
            print("  1. Typewriter")
            print("  2. Scroll")
            print("  3. Blink")
            anim_choice = input("Choose (1-3): ").strip()

            print("\n" + "=" * 90)
            if anim_choice == '1':
                animate_typewriter(result)
            elif anim_choice == '2':
                animate_scroll(result)
            elif anim_choice == '3':
                animate_blink(result)

        elif post_choice == '3':
            preset_name = input("\nPreset name: ").strip()
            if preset_name:
                desc = input("Description (optional): ").strip()
                if add_preset(preset_name, style, color, bg_color, effect, desc):
                    print(f"✓ Preset '{preset_name}' saved!")
                else:
                    print("✗ Failed to save preset")

    print("=" * 90)


if __name__ == "__main__":
    main()
