import pytest

from clear import clear

@pytest.fixture
def mocked_print(mocker):
    return mocker.patch("builtins.print")

def test_clear(mocked_print):
    clear()
    mocked_print.assert_called_once_with("\033[2J\033[H")
