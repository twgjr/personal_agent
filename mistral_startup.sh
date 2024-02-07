#!/bin/bash

# make this file executable with chmod +x mistral_startup.sh
# add this file to ~/.bashrc with the line ~/Code/personal_agent/mistral_startup.sh

source ~/Code/personal_agent/venv/bin/activate
python ~/Code/personal_agent/mistral.py 2> ~/Code/personal_agent/mistral_error.log