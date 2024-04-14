import pytest
from ls import ls

# TODO Implement this
cwd = "./"

@pytest.fixture
def empty_filesystem():
    # Here you would set up your mock file system, however you decide to represent it
    return {}  # An empty dictionary, for a start

def test_ls_when_cwd_is_empty(empty_filesystem):
    result = ls(cwd)
    assert result == ""
