# CHAD

> CHAD is just a CHATBOT — a simple, extensible chatbot written in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-Proprietary-orange)
![Status](https://img.shields.io/badge/Status-Alpha-yellow)

CHAD is a lightweight command-line chatbot designed for simplicity and expandability. Built with a clean command dictionary pattern, it's easy to modify and extend with new features.

## Features

- **Simple Command Interface** — Easy-to-use text commands
- **Extensible Design** — Add new commands by editing the dictionary
- **Clean Architecture** — Command logic centralized for easy maintenance
- **Cross-Platform** — Works on Linux, macOS, and Windows
- **No Dependencies** — Pure Python standard library

## Installation

```bash
# Clone the repository
git clone https://github.com/Patrickk2/CHAD.git
cd CHAD

# Run the bot
python bot.py
```

## Usage

```
$ python bot.py
C'est quoi ton blaze ? Alice
Alice : bonjour
Salut ! Tu tombes bien, jitais en train de réfléchir à lunivers.
Alice : aide

=== Aide CHAD ===
Voici les commandes que tu peux utiliser :
- test
- bonjour
- aide
- rien
- bye
- version
- nettoie
=================

Alice : version
CHAD est actuellement à la version 0.1 alpha.
Alice : bye
À plus dans le bus !
```

## Commands Reference

| Command | Description |
|---------|-------------|
| `test` | Verify the bot is responding |
| `bonjour` | Receive a greeting |
| `aide` | Display available commands |
| `version` | Show bot version |
| `bye` / `rien` | Exit cleanly |
| `nettoie` | Clear the terminal screen |

## Adding Custom Commands

Edit `bot.py` and add entries to the `commands` dictionary:

```python
def cmd_mycommand():
    print("Your custom response here")

commands = {
    # ... existing commands
    "mycommand": cmd_mycommand,
}
```

## File Structure

```
CHAD/
├── bot.py          # Main chatbot implementation
├── nlp_module.py # NLP preprocessing utilities
├── README.md     # This file
├── LICENSE       # Proprietary license
└── .github/      # GitHub workflows (CI/CD)
```

## Requirements

- Python 3.6+

No external packages required — uses only the Python standard library.

## License

Proprietary — All rights reserved. See [LICENSE](LICENSE) for details.

---

Coded with ☕ by Patrick