if __name__ == "__main__":
    current_directory = "~/projects/2024/A-project-for-a-week/week4_terminal-like-app/"

    while True:
        prompt = input("$>")

        if prompt == "exit":
            break

        if prompt == "ls":
            print("ls")
