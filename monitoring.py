
import time
import os
import psutil
from collections import Counter
import keyboard
import sys

# ANSI color codes for dark and light purple
dark_purple = "\033[95m"
light_purple = "\033[94m"
reset_color = "\033[0m"

# Initialize a Counter to keep track of process frequency
process_frequency = Counter()

def set_cursor_position(x, y):
    print(f"\033[{y};{x}H", end="")

def start_monitoring(stop_key, main_watch_programs):
    global process_frequency
    
    while True:
        # Set cursor to the beginning of the Most Used section
        set_cursor_position(0, 1)
        
        print(f"{light_purple}==== Most Used ===={reset_color}")
        for proc in psutil.process_iter(['name']):
            process_frequency[proc.info['name']] += 1
        most_used = process_frequency.most_common(5)
        for proc, count in most_used:
            print(f"{dark_purple}{proc} (Seen: {count} times){reset_color}               ")

        # Set cursor to the beginning of the Main Watch section
        set_cursor_position(0, 8)
        
        print(f"{light_purple}\n==== Main Watch ===={reset_color}")
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in main_watch_programs:
                print(f"{dark_purple}Monitoring {proc.info['name']} (PID: {proc.info['pid']}){reset_color}                   ")

        # Set cursor to the beginning of the System Resources section
        set_cursor_position(0, 15)
        
        print(f"{light_purple}\n==== System Resources ===={reset_color}")
        print(f"{dark_purple}CPU Usage: {psutil.cpu_percent()}%{reset_color}              ")
        print(f"{dark_purple}RAM Usage: {psutil.virtual_memory().percent}%{reset_color}              ")

        print(f"{light_purple}\nPress {stop_key} to stop.{reset_color}")
        
        if keyboard.is_pressed(stop_key):
            print(f"{dark_purple}Exiting monitoring.{reset_color}")
            break
        time.sleep(1)

if __name__ == "__main__":
    stop_key = sys.argv[1] if len(sys.argv) > 1 else "F2"
    main_watch_programs = sys.argv[2].split(',') if len(sys.argv) > 2 else []
    start_monitoring(stop_key, main_watch_programs)
