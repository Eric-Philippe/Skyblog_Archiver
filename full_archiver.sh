#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null; then
    # Python is not found, so we need to install it

    # Define the Python version to install
    PYTHON_VERSION=3.9.6
    
    # Define the download URL for the Python installer
    PYTHON_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz"
    
    # Define the temporary installation directory
    INSTALL_DIR=/tmp/python-install

    # Create the temporary installation directory
    mkdir -p "$INSTALL_DIR"
    cd "$INSTALL_DIR"

    # Download and extract Python
    echo "Downloading and extracting Python..."
    curl -O "$PYTHON_URL"
    tar -xf "Python-${PYTHON_VERSION}.tar.xz"

    # Build and install Python
    echo "Building and installing Python..."
    cd "Python-${PYTHON_VERSION}"
    ./configure --prefix="$INSTALL_DIR/python"
    make -j$(nproc)
    make install

    # Add Python to PATH
    echo "Adding Python to PATH..."
    export PATH="$INSTALL_DIR/python/bin:$PATH"

    # Clean up
    echo "Cleaning up..."
    cd
    rm -rf "$INSTALL_DIR"
fi

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
