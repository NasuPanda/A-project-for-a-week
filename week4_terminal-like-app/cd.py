import os
from exceptions import NotDirectoryError

def __root_path() -> str:
    """Returns a root path of system

    On Linux or Mac this returns /

    On Windows this returns C:\\ or whatever the current drive is

    Returns:
        str: root path
    """
    return os.path.abspath(os.sep)

def cd(path: str):
    # When the given path is empty (cwd moves to the root)
    if path == "":
        return __root_path()

    if not os.path.exists(path):
        raise FileNotFoundError(f"no such file or directory: {path}")
    if os.path.isfile(path):
        raise NotDirectoryError(f"not a directory: {path}")

    # Change the system's working directory
    os.chdir(path)
    return os.getcwd()
