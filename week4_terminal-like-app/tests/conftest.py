import os
import pytest

@pytest.fixture
def original_working_dir():
    """Fixture to store and restore the original working directory"""
    current_dir = os.getcwd()
    yield current_dir
    os.chdir(current_dir)  # Restore after the test
