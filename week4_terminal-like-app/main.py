from command_handler import CommandHandler

if __name__ == "__main__":
    command_prompt = "$> "
    command_handler = CommandHandler()

    while True:
        user_input = input(command_prompt)

        try:
            command_flag = command_handler.handle_command(user_input)
        except Exception as e:
            print(str(e))
        else:
            # When handle_command returns false, this app ends
            if not command_flag:
                break
