from filesystem import Directory, File


def ls(cwd: Directory) -> str:
    """`ls` command.

    For empty cwd, it returns an empty string.

    For cwd with contents, it returns files and directories sorted alphabetically.

    Args:
        cwd (Directory): current working directory.

    Returns:
        str: the output of `ls` command.
    """
    if not cwd.contents:
        return "" # Returns empty string for empty cwd

    list_of_files_and_directories = [content.name for content in cwd.contents]
    return "\n".join(sorted(list_of_files_and_directories))
