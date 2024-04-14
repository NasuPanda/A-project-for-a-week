import pytest

from command_handler import CommandHandler

@pytest.fixture
def command_handler() -> CommandHandler:
    return CommandHandler()

def test_exit_handler(command_handler: CommandHandler):
    result = command_handler.handle_command("exit")
    assert result == False

def test_invalid_command(command_handler: CommandHandler):
    with pytest.raises(ValueError) as exception_info:
        command_handler.handle_command("some_unknown_command")

    # Get an error message form exception_info
    error_message = str(exception_info.value)
    assert error_message == "Command not found"

def test_valid_command_do_not_raise_error(command_handler: CommandHandler):
    # This will be enough to test that no error is raised
    [command_handler.handle_command(command.name) for command in command_handler.allowed_commands]
