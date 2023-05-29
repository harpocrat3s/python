#!/usr/bin/env python3

# Another assignment of a Python course I did time ago 

import sys
import subprocess

with open(sys.argv[1]) as file:
    data = file.readlines()
    new_data = []
    final_data = []

    # Read the lines from the input file
    for line in data:
        new_data.append(line.strip())

    # Replace 'jane' with 'jdoe' in each line
    for line in new_data:
        final_data.append(line.replace('jane', 'jdoe'))

    # Move the files using the 'mv' command
    for index, line in enumerate(new_data):
        subprocess.run('mv ' + line + ' ' + final_data[index], shell=True)
