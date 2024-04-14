def handle_command(user_input):
    if user_input == "exit":
        return False
    else:
        raise ValueError("Command not found")
