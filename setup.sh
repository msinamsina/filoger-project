# ! /bin/bash

# Install Python if it's not already installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# Install required packages
pip3 install -r requirements.txt

