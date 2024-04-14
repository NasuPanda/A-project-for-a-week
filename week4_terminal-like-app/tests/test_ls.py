import pytest

from ls import ls

"""
./tests/test_filesystem
├── dir_empty
├── dir_with_contents
│   ├── subdir_empty
│   ├── subdir_with_contents
│   │   └── test3.txt
│   └── test2.txt
└── test.txt
"""

@pytest.fixture
def empty_directory():
    return "./tests/test_filesystem/dir_empty"

@pytest.fixture
def directory_with_hidden_file():
    # NOTE: It's the same directory as empty_directory
    return "./tests/test_filesystem/dir_empty"

@pytest.fixture
def directory_with_contents():
    return "./tests/test_filesystem/dir_with_contents"

@pytest.fixture
def invalid_path_name():
    return "unknown_path"

@pytest.fixture
def text_file():
    return "./tests/test_filesystem/test.txt"

# Expected result from ls: sorted contents in directory_with_contents
EXPECTED_OUTPUT_FOR_DIR_WITH_CONTENTS = "subdir_empty\nsubdir_with_contents\ntest2.txt"

def test_ls_outputs_empty_string_for_empty_directory(empty_directory):
    result = ls(empty_directory)
    assert result == ""

def test_ls_outputs_empty_string_for_hidden_file(directory_with_hidden_file):
    result = ls(directory_with_hidden_file)
    assert result == ""

def test_ls_output_correct_message_for_invalid_path(invalid_path_name):
    result = ls(invalid_path_name)
    assert result == f"{invalid_path_name}: No such file or directory"

def test_ls_output_file_name_for_file_path(text_file):
    result = ls(text_file)
    assert result == text_file

def test_ls_lists_files_and_subdirectories_on_separate_lines(directory_with_contents):
    result = ls(directory_with_contents)
    assert result == EXPECTED_OUTPUT_FOR_DIR_WITH_CONTENTS
