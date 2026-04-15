import sys
from utils.helpers import load_config, clear_screen
from commands import registry


class Bot:
    def __init__(self):
        self.config = load_config()
        self.name = self.config["bot"]["name"]
        self.username = None
        self.settings = self.config.get("settings", {})

    def normalize_input(self, text: str) -> str:
        if not self.settings.get("case_sensitive", False):
            text = text.lower()
        if self.settings.get("trim_whitespace", True):
            text = text.strip()
        return text

    def get_command(self, key: str):
        return registry.get(key)

    def handle_input(self, user_input: str) -> None:
        key = self.normalize_input(user_input)
        if not key:
            return
        cmd = self.get_command(key)
        if cmd:
            cmd.execute()
        else:
            registry["unknown"].execute()

    def get_username(self) -> str:
        if self.username:
            return self.username
        prompt = self.config["bot"].get("prompt", "Username: ")
        self.username = input(prompt)
        return self.username

    def run(self):
        clear_screen()
        username = self.get_username()
        print()

        while True:
            prompt = f"{username}: "
            user_input = input(prompt)
            self.handle_input(user_input)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()