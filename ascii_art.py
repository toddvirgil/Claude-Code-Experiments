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
    'none': ''
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


def generate_ascii_art(text, style='block', color='none'):
    """
    Generate ASCII art from text with optional color

    Args:
        text: String to convert to ASCII art
        style: Font style - 'block', 'slant', 'mini', 'shadow', 'bubble', 'double', 'banner'
        color: Color option - 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow',
               'bright_red', 'bright_green', 'bright_blue', 'bright_cyan',
               'bright_magenta', 'bright_yellow', 'rainbow', or 'none'

    Returns:
        ASCII art string with optional color codes
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

    # Build each line
    lines = []
    for row in range(height):
        line = ''
        for char_idx, char in enumerate(supported_text):
            if char in font:
                char_lines = font[char]
                if row < len(char_lines):
                    char_str = char_lines[row]

                    # Apply rainbow color (different color per character)
                    if color == 'rainbow':
                        rainbow_colors = [
                            Colors.RED, Colors.YELLOW, Colors.GREEN,
                            Colors.CYAN, Colors.BLUE, Colors.MAGENTA
                        ]
                        color_code = rainbow_colors[char_idx % len(rainbow_colors)]
                        char_str = f"{color_code}{char_str}{Colors.RESET}"
                    elif color in COLOR_MAP and COLOR_MAP[color]:
                        # Apply solid color
                        char_str = f"{COLOR_MAP[color]}{char_str}{Colors.RESET}"

                    line += char_str + ' '
                else:
                    line += ' ' * (len(char_lines[0]) + 1)
        lines.append(line.rstrip())

    return '\n'.join(lines)


def main():
    """CLI interface for ASCII art generator"""
    import sys

    print("=" * 70)
    print(f"{Colors.BOLD}ASCII ART GENERATOR{Colors.RESET}")
    print("=" * 70)

    # Get text input
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("\nEnter text to convert: ").strip()
        if not text:
            print("No text provided!")
            return

    # Show available styles
    print("\n" + Colors.BOLD + "Available styles:" + Colors.RESET)
    print("  1. block   - Bold block letters (#)")
    print("  2. slant   - Slanted/diagonal style (/\\)")
    print("  3. mini    - Compact mini style")
    print("  4. shadow  - Bold with shadow effect (█)")
    print("  5. bubble  - Rounded and bubbly (▄▀)")
    print("  6. double  - Double-lined box drawing (╔╗)")
    print("  7. banner  - Simple banner style")
    print("  8. all     - Show all styles")

    style_choice = input("\nChoose style (1-8, default=1): ").strip() or "1"

    style_map = {
        '1': 'block',
        '2': 'slant',
        '3': 'mini',
        '4': 'shadow',
        '5': 'bubble',
        '6': 'double',
        '7': 'banner',
        '8': 'all',
        'block': 'block',
        'slant': 'slant',
        'mini': 'mini',
        'shadow': 'shadow',
        'bubble': 'bubble',
        'double': 'double',
        'banner': 'banner',
        'all': 'all'
    }

    style = style_map.get(style_choice, 'block')

    # Color selection (only if not showing all)
    color = 'none'
    if style != 'all':
        print("\n" + Colors.BOLD + "Color options:" + Colors.RESET)
        print("  1. none           - No color (default)")
        print(f"  2. {Colors.RED}red{Colors.RESET}            - Red")
        print(f"  3. {Colors.GREEN}green{Colors.RESET}          - Green")
        print(f"  4. {Colors.YELLOW}yellow{Colors.RESET}         - Yellow")
        print(f"  5. {Colors.BLUE}blue{Colors.RESET}           - Blue")
        print(f"  6. {Colors.CYAN}cyan{Colors.RESET}           - Cyan")
        print(f"  7. {Colors.MAGENTA}magenta{Colors.RESET}        - Magenta")
        print(f"  8. {Colors.BRIGHT_RED}bright_red{Colors.RESET}     - Bright Red")
        print(f"  9. {Colors.BRIGHT_GREEN}bright_green{Colors.RESET}   - Bright Green")
        print(f" 10. {Colors.BRIGHT_YELLOW}bright_yellow{Colors.RESET}  - Bright Yellow")
        print(f" 11. {Colors.BRIGHT_BLUE}bright_blue{Colors.RESET}    - Bright Blue")
        print(f" 12. {Colors.BRIGHT_CYAN}bright_cyan{Colors.RESET}    - Bright Cyan")
        print(f" 13. {Colors.BRIGHT_MAGENTA}bright_magenta{Colors.RESET} - Bright Magenta")
        print(f" 14. rainbow        - Rainbow colors 🌈")

        color_choice = input("\nChoose color (1-14, default=1): ").strip() or "1"

        color_map = {
            '1': 'none',
            '2': 'red',
            '3': 'green',
            '4': 'yellow',
            '5': 'blue',
            '6': 'cyan',
            '7': 'magenta',
            '8': 'bright_red',
            '9': 'bright_green',
            '10': 'bright_yellow',
            '11': 'bright_blue',
            '12': 'bright_cyan',
            '13': 'bright_magenta',
            '14': 'rainbow'
        }

        color = color_map.get(color_choice, 'none')

    print("\n" + "=" * 70)

    if style == 'all':
        all_styles = ['block', 'slant', 'mini', 'shadow', 'bubble', 'double', 'banner']
        for s in all_styles:
            print(f"\n{Colors.BOLD}{s.upper()} STYLE:{Colors.RESET}")
            print("-" * 70)
            print(generate_ascii_art(text, s, 'none'))
            print()
    else:
        print(generate_ascii_art(text, style, color))

    print("=" * 70)


if __name__ == "__main__":
    main()
