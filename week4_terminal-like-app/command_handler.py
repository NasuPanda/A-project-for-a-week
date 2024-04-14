from commands import Command

# Define handlers
def exit_handler():
    return False

def ls_handler():
    # TODO: Call "ls" function defined outside of this file
    return True

ALLOWED_COMMANDS = [
    Command("exit", exit_handler),
    Command("ls", ls_handler)
]

def handle_command(user_input):
    for command in ALLOWED_COMMANDS:
        if user_input == command.name:
            return command.handler()
    else:
        raise ValueError("Command not found")
