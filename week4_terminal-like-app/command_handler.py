import os

from commands import Command
from exceptions import CommandNotFoundError
from ls import ls
from cd import cd

class CommandHandler:
    def __init__(self) -> None:
        # Initialize cwd
        self.cwd = os.getcwd()
        self.allowed_commands = [
        Command("exit", self.__exit_handler),
        Command("ls", self.__ls_handler),
        Command("cd", self.__cd_handler),
    ]

    def __exit_handler(self):
        return False

    def __ls_handler(self):
        print(ls(self.cwd))
        return True

    def __cd_handler(self, path: str):
        self.cwd = cd(path)
        return True

    def handle_command(self, user_input: str):
        for command in self.allowed_commands:
            if command.name in user_input:
                if "cd" in user_input:
                    path = user_input.split()[1]
                    return command.handler(path)

                return command.handler()
        else:
            raise CommandNotFoundError("Command not found")
