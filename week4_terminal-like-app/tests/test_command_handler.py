import pytest

from command_handler import handle_command, ALLOWED_COMMANDS


def test_exit_handler():
    result = handle_command("exit")
    assert result == False

@pytest.mark.parametrize("command", ALLOWED_COMMANDS)
def test_valid_command_do_not_raise_error(command):
    # This will be enough to test that no error is raised
    result = handle_command(command.name)

def test_invalid_command():
    with pytest.raises(ValueError) as exception_info:
        handle_command("some_unknown_command")

    # Get an error message form exception_info
    error_message = str(exception_info.value)
    assert error_message == "Command not found"
