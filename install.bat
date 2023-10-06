@echo off
echo Checking for Python...

python --version > NUL 2>&1
if errorlevel 1 (
    echo Python not found!
    echo Please install Python and then run this script again.
    pause
    exit
)

echo Found Python. Installing dependencies...
pip install -r requirements.txt

echo All dependencies are installed.
pause
