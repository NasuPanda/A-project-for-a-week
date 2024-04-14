import pytest
from command_handler import handle_command

def test_exit_handler():
    result = handle_command("exit")
    assert result == False

def test_invalid_command():
    with pytest.raises(ValueError) as exception_info:
        handle_command("some_unknown_command")

    assert str(exception_info) == "Command not found"
