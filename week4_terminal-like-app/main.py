import os

from command_handler import handle_command

if __name__ == "__main__":
    current_directory = os.getcwd()
    command_prompt = "$> "

    while True:
        user_input = input(command_prompt)

        try:
            command_result = handle_command(user_input)
        except ValueError:
            print("Command not found.")
        else:
            # When handle_command returns false, this app ends
            if not command_result:
                break
            else:
                print("Command executed")
