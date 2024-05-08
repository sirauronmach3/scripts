#!/usr/bin/env python

import sys

def alphabetize_lines(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            
            # Alphabetically sort the lines
            lines.sort()
            
            # Open the file in write mode to overwrite its contents
            with open(filename, 'w') as file:
                # Write the sorted lines back to the file
                for line in lines:
                    file.write(line)
                    file.write('\n')  # Add an empty line after each line
    except FileNotFoundError:
        print("File not found:", filename)

if __name__ == "__main__":
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    # Get the file name from the command-line argument
    filename = sys.argv[1]
    
    # Call the function to alphabetize the lines
    alphabetize_lines(filename)
