import sys

def clear():
    # ANSI Escape Codes
    print("\033[2J\033[H")  # Clear and move the cursor to the home position
    sys.stdout.flush()  # Ensure the output is displayed
