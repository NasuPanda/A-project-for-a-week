import os

from command_handler import CommandHandler

if __name__ == "__main__":
    current_directory = os.getcwd()
    command_handler = CommandHandler()

    while True:
        command_prompt = f"[{current_directory}] $> "
        user_input = input(command_prompt)

        try:
            command_flag = command_handler.handle_command(user_input)
            if "cd" in user_input:
                current_directory = command_handler.cwd
        except Exception as e:
            print(str(e))
        else:
            # When handle_command returns false, this app ends
            if not command_flag:
                break
