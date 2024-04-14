import pytest

from ls import ls
from filesystem import Directory, File

@pytest.fixture
def empty_directory():
    empty_directory = Directory(name="/", contents=[])
    return empty_directory

@pytest.fixture
def directory_with_contents():
    txt_file = File(name="script.txt")
    img_file = File(name="thumbnail.jpg")
    subdir = Directory(name="data", contents=[File("report.csv")])
    root_directory = Directory(name="/", contents=[txt_file, img_file, subdir])
    return root_directory

def test_ls_outputs_empty_string_for_empty_directory(empty_directory):
    result = ls(empty_directory)
    assert result == ""

def test_ls_lists_files_and_subdirectories_on_separate_lines(directory_with_contents):
    result = ls(directory_with_contents)
    assert result == "data\nscript.txt\nthumbnail.jpg"
