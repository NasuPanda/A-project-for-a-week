import os
import pytest

@pytest.fixture
def reset_cwd():
    """Fixture to store and restore the original working directory

    NOTE: Each test function to test `cd` function (or related) should take this fixture as input.
    """
    current_dir = os.getcwd()
    yield current_dir
    os.chdir(current_dir)  # Restore after the test
