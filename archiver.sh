#!/bin/bash


# Go to /src and install the requirements.txt if needed
cd src
if [ ! -d "venv" ]; then
    # Silently install the virtual environment
    python3 -m venv venv > /dev/null
    # Activate the virtual environment
    source venv/bin/activate
    # Install the requirements
    pip3 install -r requirements.txt
fi

# Run the archiver
source venv/bin/activate
python3 script.py
