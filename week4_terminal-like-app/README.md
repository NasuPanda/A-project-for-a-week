# Terminal-like Application in Python

## Project Description

This project explores the development of a basic terminal-like application in Python. It implements core features such as command handling, file system navigation (`cd`, `ls`), and the ability to clear the screen. At its heart, the project delves into working with directories, handling user input, and implementing custom exception classes.

## Key Features

### Supported Commands

- `exit`: Terminates the application.
- `clear`: Clears the terminal screen.
- `ls`: Lists files and directories in the current working directory.
- `cd`: Changes the current working directory.

### Custom Exception Handling
Ensures informative error messages for invalid paths, non-directory files, and unknown commands.

### Modular Design
Utilizes separate modules for commands, file system interactions, and screen clearing, promoting maintainability.

## Lessons Learned

- **Pythonic File System Interaction:** Leveraging the `os` and `os.path` modules for directory navigation and file system operations.
- **Exception Handling:** Designing custom exceptions to provide targeted error messages to the user.
- **Test-Driven Development:** Employing pytest to write robust unit tests, ensuring the correctness of individual components and overall application behavior.

### Challenges and Resolutions

- **Changing the System's Working Directory:** Understanding the use of `os.chdir()` to directly modify the working directory of the active process.
- **Fixture Scope in Pytest:** Learning how to share fixtures throughout tests using `conftest.py`, ensuring a clean environment for each test case.
- **Mocking and Isolation:** Exploring the `pytest-mock` library to isolate units of code for testing, focusing on the core logic of functions independent of external dependencies.

### Project Structure

```
.
├── README.md
├── Pipfile
├── Pipfile.lock
├── cd.py
├── clear.py
├── command_handler.py
├── commands.py
├── exceptions.py
├── ls.py
├── main.py
└── tests
    ├── conftest.py
    ├── test_cd.py
    ├── test_clear.py
    ├── test_command_handler.py
    ├── test_filesystem
    │   ├── ... test files and directories ...
    └── test_ls.py
```

### How to Run

1. **Install Dependencies:** `pipenv install`
2. **Launch Application:** `python main.py`

### Future Development

- **Additional Commands:** Implement features like `mkdir`, `touch`, `rm`.
- **Shell-like Enhancements:** Support `cd ..`, `cd ~`, and tab completion.
- **Tab Completion:** Basic filename/directory completion when using the `cd` command.
- **Command History:** Keep a history of entered commands and allow cycling through them using arrow keys.
- **Customizable Prompt:** Allow the user to configure the appearance of the command prompt.
