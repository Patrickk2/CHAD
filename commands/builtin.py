import sys
from commands.base import Command
from utils.helpers import load_config, clear_screen


class BonjourCommand(Command):
    name = "bonjour"
    description = "Receive a greeting from CHAD"

    def execute(self, args=None):
        config = load_config()
        print(config["bot"]["greeting"])


class HelpCommand(Command):
    name = "help"
    description = "Display available commands"

    def execute(self, args=None):
        from commands import registry
        print("\n=== Help CHAD ===")
        print("Available commands:")
        for cmd in registry.values():
            print(f"  {cmd.name:12} - {cmd.description}")
        print("=================\n")


class QuitCommand(Command):
    name = "quit"
    description = "Exit the chatbot"

    def execute(self, args=None):
        config = load_config()
        print(config["responses"]["quit"])
        sys.exit()


class ByeCommand(Command):
    name = "bye"
    description = "Say goodbye and exit"

    def execute(self, args=None):
        config = load_config()
        print(config["responses"]["bye"])
        sys.exit()


class VersionCommand(Command):
    name = "version"
    description = "Show CHAD version"

    def execute(self, args=None):
        config = load_config()
        version = config["bot"]["version"]
        response = config["responses"]["version"].format(version=version)
        print(response)


class ClearCommand(Command):
    name = "clear"
    description = "Clear the terminal screen"

    def execute(self, args=None):
        clear_screen()


class UnknownCommand(Command):
    name = "unknown"
    description = "Unknown command handler"

    def execute(self, args=None):
        config = load_config()
        print(config["bot"]["unknown"])