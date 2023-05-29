#!/usr/bin/env python3

"""
This script allows the user to search for specific error messages in a log file and save the matching lines to a file.
"""

import sys
import os
import re

def error_search(log_file, error):
    returned_errors = []

    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file:
            if re.search(fr"\b{re.escape(error)}\b", log, re.IGNORECASE):
                returned_errors.append(log)
    return returned_errors


def file_output(returned_errors, output_file):
    with open(output_file, 'w') as file:
        for error in returned_errors:
            file.write(error)


if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) < 3:
        print("Invalid number of arguments.")
        print("Usage: python3 log_search.py <log_file> <error_message>")
        sys.exit(1)

    log_file = sys.argv[1]
    error_message = sys.argv[2]

    # Search for errors and store in list
    returned_errors = error_search(log_file, error_message)

    # Define output file path
    output_file = os.path.expanduser('~') + '/data/errors_found.log'

    # Save errors to output file
    file_output(returned_errors, output_file)

    sys.exit(0)
