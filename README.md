#!/bin/bash
echo "Hello, World!"
-------------------------------------------------------------------
#!/bin/bash

# Check if at least two arguments are passed
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 arg1 arg2"
    exit 1
fi

# Accessing arguments
arg1=$1
arg2=$2

echo "Argument 1: $arg1"
echo "Argument 2: $arg2"

# You can also access all arguments using "$@"
echo "All arguments: $@"

# Example of a loop to print all arguments
for arg in "$@"; do
    echo "Argument: $arg"
done
-------------------------------------------------------------------------------------------
#!/bin/bash

# Prompt user for input
echo "Enter a number between 1 and 10:"
read number

# Check the value of the number
if [ "$number" -lt 1 ]; then
    echo "The number is less than 1."
elif [ "$number" -gt 10 ]; then
    echo "The number is greater than 10."
else
    echo "The number is between 1 and 10."
fi
---------------------------------------------------------------------------------



