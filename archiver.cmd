@echo off

REM Check if Python is installed
where python > nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    REM Python is not found, so we need to install it

    REM Define the Python version to install
    set "PYTHON_VERSION=3.9.6"
    
    REM Define the download URL for the Python installer
    set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
    
    REM Define the temporary installer file path
    set "INSTALLER_FILE=python-installer.exe"

    REM Download the Python installer
    echo Downloading Python installer...
    powershell -command "(New-Object System.Net.WebClient).DownloadFile('%PYTHON_URL%', '%INSTALLER_FILE%')"
    
    REM Install Python
    echo Installing Python...
    start /wait %INSTALLER_FILE% /quiet PrependPath=1

    REM Clean up the installer file
    echo Cleaning up...
    del %INSTALLER_FILE%
)

REM Go to \src and install the requirements.txt if needed
cd src
IF NOT EXIST venv (
    REM Silently install the virtual environment
    python -m venv venv > nul
    REM Activate the virtual environment
    call venv\Scripts\activate.bat
    REM Install the requirements
    pip install -r requirements.txt
)

REM Run the archiver
call venv\Scripts\activate.bat
python script.py
