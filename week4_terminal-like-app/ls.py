import os


def ls(path: str) -> str:
    """`ls` command.

    For empty input, this returns an empty string.

    For invalid path, this returns a message to suggest what went wrong.

    For a file path, this returns the name of the file.

    For a directory with contents, this returns files and directories sorted alphabetically.

    Args:
        path str: current working directory.

    Returns:
        str: the output of `ls` command.
    """
    # Returns empty string for empty path
    if not path:
        return ""
    # Returns error message when given an invalid path
    if not os.path.exists(path):
        return f"{path}: No such file or directory"
    # Returns the file name when given a file path
    if os.path.isfile(path):
        return path

    files_and_directories = os.listdir(path)
    # Ignore hidden files and directories as `ls` does
    files_and_directories = [name for name in files_and_directories if not name.startswith(".")]
    return "\n".join(sorted(files_and_directories))
