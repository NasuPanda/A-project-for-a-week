import os

from commands import Command
from exceptions import NotDirectoryError, CommandNotFoundError
from ls import ls

class CommandHandler:
    def __init__(self) -> None:
        # Initialize cwd
        self.cwd = os.getcwd()
        self.allowed_commands = [
        Command("exit", self.__exit_handler),
        Command("ls", self.__ls_handler)
    ]

    def __validate_cwd(self, path: str):
        # When the given path is empty (cwd moves to the root)
        if path == "":
            return True

        if not os.path.exists(path):
            raise FileNotFoundError(f"no such file or directory: {path}")
        if os.path.isfile(path):
            raise NotDirectoryError(f"not a directory: {path}")

    def __exit_handler(self):
        return False

    def __ls_handler(self):
        print(ls(self.cwd))
        return True

    def change_current_working_directory(self, path: str) -> None:
        self.__validate_cwd(path)
        self.cwd = path

    def handle_command(self, user_input: str):
        for command in self.allowed_commands:
            if user_input == command.name:
                return command.handler()
        else:
            raise CommandNotFoundError("Command not found")
