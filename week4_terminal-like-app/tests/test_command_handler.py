import pytest

from command_handler import CommandHandler
from exceptions import CommandNotFoundError, NotDirectoryError

@pytest.fixture
def command_handler() -> CommandHandler:
    return CommandHandler()

@pytest.fixture
def non_existed_path() -> str:
    return "non_existed_path"

@pytest.fixture
def text_file() -> str:
    return "./tests/test_filesystem/test.txt"

def test_exit_handler(command_handler: CommandHandler):
    result = command_handler.handle_command("exit")
    assert result == False

def test_invalid_command_raises_error(command_handler: CommandHandler):
    with pytest.raises(CommandNotFoundError) as exception_info:
        command_handler.handle_command("some_unknown_command")

    error_message = str(exception_info.value)
    assert error_message == "Command not found"

def test_exit_command_do_not_raise_error(command_handler: CommandHandler):
    command_handler.handle_command("exit")

def test_ls_command_do_not_raise_error(command_handler: CommandHandler):
    # This will be enough to test that no error is raised
    command_handler.handle_command("ls")

def test_cd_command_do_not_raise_error(
        command_handler: CommandHandler,
        reset_cwd: str,
    ):
    command_handler.handle_command("cd tests")

def test_change_cwd_for_non_existed_filepath_raises_error(
    command_handler: CommandHandler,
    non_existed_path: str,
    reset_cwd: str,
    ):
    with pytest.raises(FileNotFoundError) as exception_info:
        command_handler.handle_command(f"cd {non_existed_path}")
    error_message = str(exception_info.value)
    assert error_message == f"no such file or directory: {non_existed_path}"

def test_change_cwd_for_a_file_raises_error(
        command_handler: CommandHandler,
        text_file: str,
        reset_cwd: str
    ):
    with pytest.raises(NotDirectoryError) as exception_info:
        command_handler.handle_command(f"cd {text_file}")
    error_message = str(exception_info.value)
    assert error_message == f"not a directory: {text_file}"
