#!/usr/bin/env python3

"""
This script renames files listed in a text file by replacing a specified word with another specified word.
It assumes that the text file contains either filenames without paths or full filepaths.
"""

import sys
import subprocess

# Check if the user has provided the required arguments
if len(sys.argv) < 4:
    print("Usage: python script.py <text_file> <word_to_replace> <replacement_word>")
    sys.exit(1)

# Extract the arguments from the command line
text_file = sys.argv[1]
word_to_replace = sys.argv[2]
replacement_word = sys.argv[3]

# Open the text file
with open(text_file) as file:
    # Read the contents of the file and store them in the data list
    data = file.readlines()
    new_data = []
    final_data = []
    
    # Strip leading and trailing whitespace from each line and store in new_data list
    for line in data:
        new_data.append(line.strip())

    # Replace the specified word with the replacement word in each line and store in final_data list
    for line in new_data:
        final_data.append(line.replace(word_to_replace, replacement_word))

    index = 0
    # Iterate over each line in new_data
    for line in new_data:
        # Execute the 'mv' command in the CLI to rename the file from new_data[index] to final_data[index]
        subprocess.run(['mv', line, final_data[index]])
        index += 1
