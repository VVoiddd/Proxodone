# Keep Alive Script

## Description
This is a Python script designed to keep your computer awake and act as a basic system monitoring tool.

## Features

- Prevents the system from going to sleep
- A dynamic menu for user interaction
- System monitoring capabilities
- Allows user to set a key to stop the script
- Live updates of system metrics

## Installation

1. Make sure you have Python installed.
2. Clone this repository or download the ZIP file.
3. Navigate to the project directory and run `install.bat` to install required dependencies.

## Usage

Run `start.bat` and follow the on-screen instructions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT

## Plan for Overhauling the Code

## 1. For keep_awake.py:
   - Enhance the UI with better color schemes and potentially add some ASCII art for better visual appeal.
   - Improve the loading animation.
   - Use argparse for command-line arguments instead of directly using sys.argv for better maintainability and user experience.
   - Add more settings options for customization.

## 2. For monitoring.py:
   - Use a library like 'psutil' for better system monitoring.
   - Add CPU, RAM, and other system metrics.
   - Enhance the UI and add categories like 'Most Used Programs', 'Main Watch', and 'Unknown'.
   - Use argparse for command-line arguments.
   - Show real-time updates without refreshing the entire screen.
