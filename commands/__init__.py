from commands.base import Command
from commands.builtin import (
    BonjourCommand,
    HelpCommand,
    QuitCommand,
    ByeCommand,
    VersionCommand,
    ClearCommand,
    UnknownCommand,
)

registry = {
    "bonjour": BonjourCommand(),
    "help": HelpCommand(),
    "quit": QuitCommand(),
    "bye": ByeCommand(),
    "version": VersionCommand(),
    "clear": ClearCommand(),
}

__all__ = ["Command", "registry"]