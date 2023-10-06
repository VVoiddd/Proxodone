from colorama import Fore, Style, init
import os
import platform
import ctypes
import subprocess
import time

# Initialize colorama
init(autoreset=True)

# New ASCII Art
print(Fore.MAGENTA + "$$\\   $$\\                               $$$$$$\\")
print("$$ | $$  |                             $$  __$$\\")
print("$$ |$$  / $$$$$$\\   $$$$$$\\   $$$$$$\\  $$ /  $$ |")
print("$$$$$  / $$  __$$\\ $$  __$$\\ $$  __$$\\ $$$$$$$$ |")
print("$$  $$<  $$$$$$$$ |$$$$$$$$ |$$ /  $$ |$$  __$$ |")
print("$$ |\\$$\\ $$   ____|$$   ____|$$ |  $$ |$$ |  $$ |")
print("$$ | \\$$\\\\$$$$$$$\\ \\$$$$$$$\\ $$$$$$$  |$$ |  $$ |")
print("\\__|  \\__|\\_______| \\_______|$$  ____/ \\__|  \\__|")
print("                             $$ |")
print("                             $$ |")
print("                             \\__|")

# Initialize global variable for stop key
stop_key = "F2"

# Loading animation
def loading_animation():
    animation = "|/-\\\\"
    for i in range(10):
        print(f"{Fore.MAGENTA}Loading {animation[i % len(animation)]}", end="\\r")
        time.sleep(0.2)

# Prevent sleep for Windows
def prevent_sleep_windows():
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

# Prevent sleep for Mac/Linux
def prevent_sleep_mac_linux():
    subprocess.call("caffeinate -i -t 2", shell=True)

# Main Menu
def main():
    global stop_key

    while True:
        print(f"{Fore.BLUE}1. Start Script")
        print("2. Start Monitoring")
        print("3. Settings")
        print("4. Exit")

        choice = input(f"{Fore.MAGENTA}Enter your choice: ")

        loading_animation()

        if choice == "1":
            print(f"{Fore.MAGENTA}Keeping the system awake...")
            if platform.system() == 'Windows':
                prevent_sleep_windows()
            else:
                prevent_sleep_mac_linux()
        elif choice == "2":
            main_watch_programs = input(f"{Fore.MAGENTA}Enter programs to be on Main Watch, separated by commas: ")
            os.system(f'start cmd /k python monitoring.py {stop_key} "{main_watch_programs}"')
        elif choice == "3":
            new_key = input(f"{Fore.MAGENTA}Enter the new key to stop the script (current is {stop_key}): ")
            stop_key = new_key
            print(f"{Fore.BLUE}New stop key is set to {stop_key}")
        elif choice == "4":
            print(f"{Fore.MAGENTA}Exiting.")
            break
        else:
            print(f"{Fore.MAGENTA}Invalid choice. Please try again.")

if __name__ == "__main__":
    main()