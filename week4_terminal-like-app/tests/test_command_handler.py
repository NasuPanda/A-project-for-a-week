import pytest

from command_handler import CommandHandler
from exceptions import CommandNotFoundError, NotDirectoryError

@pytest.fixture
def command_handler() -> CommandHandler:
    return CommandHandler()

def test_exit_handler(command_handler: CommandHandler):
    result = command_handler.handle_command("exit")
    assert result == False

def test_invalid_command_raises_error(command_handler: CommandHandler):
    with pytest.raises(CommandNotFoundError) as exception_info:
        command_handler.handle_command("some_unknown_command")

    error_message = str(exception_info.value)
    assert error_message == "Command not found"

def test_valid_command_do_not_raise_error(command_handler: CommandHandler):
    # This will be enough to test that no error is raised
    [command_handler.handle_command(command.name) for command in command_handler.allowed_commands]

def test_change_cwd_for_non_existed_filepath_raises_error(command_handler: CommandHandler):
    with pytest.raises(FileNotFoundError) as exception_info:
        command_handler.change_current_working_directory("non_existed_path")
    error_message = str(exception_info.value)
    assert error_message == f"no such file or directory: non_existed_path"

def test_change_cwd_for_a_file_raises_error(command_handler: CommandHandler):
    with pytest.raises(NotDirectoryError) as exception_info:
        command_handler.change_current_working_directory("tests/test_filesystem/test.txt")
    error_message = str(exception_info.value)
    assert error_message == f"not a directory: tests/test_filesystem/test.txt"
