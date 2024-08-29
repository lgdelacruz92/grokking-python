#!/bin/bash

# Check if both arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <module> <filename>"
    exit 1
fi

# Assign the command-line arguments to variables
module_arg=$1
filename_arg=$2


# Run the command with the user-provided arguments
python3 -m pytest "tests/$module_arg/test_$filename_arg.py"