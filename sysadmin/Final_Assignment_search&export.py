#!/usr/bin/env python3

# This was the final assignment of the Google Python course on Coursera
# "Using Python to interact with the operating system".
# The script scan logs for a specific error.


import sys
import os
import re
import csv
import operator

info_dict = {}
error_dict = {}
error_list = []

def error_search(log_file):
    # This function searches for error messages in the log file and populates the error_dict
    # dictionary with a list of error messages associated with each username.
    error = 'ticky: ERROR:'

    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(r"ticky: ERROR ([\w ']*) \(([\w.]*)\)$", log)
            if result is not None:
                error_list.append(result[1])
                if result[2] in error_dict:
                    temp_list = error_dict[result[2]]
                    temp_list.append(result[1])
                    error_dict[result[2]] = temp_list
                else:
                    error_dict[result[2]] = [result[1]]
    file.close()

def info_search(log_file):
    # This function searches for information messages in the log file and populates the
    # info_dict dictionary with a list of information messages associated with each username.
    info = 'ticky: INFO:'

    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(r"ticky: INFO ([\w ]*) \[#\d*\] \(([\w.]*)\)$", log)
            if result is not None:
                if result[2] in info_dict:
                    temp_list = info_dict[result[2]]
                    temp_list.append(result[1])
                    info_dict[result[2]] = temp_list
                else:
                    info_dict[result[2]] = [result[1]]
    file.close()

def create_error_messages_list():
    # This function creates a list of error messages and their counts from the error_list.
    final_unsorted_dict = {}

    for element in error_list:
        final_unsorted_dict[element] = error_list.count(element)

    return sorted(final_unsorted_dict.items(), key=operator.itemgetter(1), reverse=True)


def count_occurrences_per_user(to_count_dict):
    # This function counts the occurrences of messages for each user in the given dictionary.
    final_dict = {}
    for key in to_count_dict:
        final_dict[key] = len(to_count_dict[key])
    return final_dict

def create_csv_user_stats():
    # This function creates a CSV file named 'user_statistics.csv' and writes the statistics
    # of INFO and ERROR messages per user.
    with open('user_statistics.csv', mode='w') as csv_file:
        fieldnames = ['Username', 'INFO', 'ERROR']
        info_sum = count_occurrences_per_user(info_dict)
        error_sum = count_occurrences_per_user(error_dict)
        dict_to_write = {}

        for key in info_sum:
            if key in error_sum:
                dict_to_write[key] = (info_sum[key], error_sum[key])
            else:
                dict_to_write[key] = (info_sum[key], 0)

        for key in error_sum:
            if key in dict_to_write:
                pass
            else:
                dict_to_write[key] = (0, error_sum[key])

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for key in dict_to_write:
            info, error = dict_to_write[key]
            writer.writerow({'Username': key, 'INFO': info, 'ERROR': error})

def create_csv_error_stats():
    # This function creates a CSV file named 'error_message.csv' and writes the error messages
    # along with their counts.
    with open('error_message.csv', mode='w') as csv_file:
        fieldnames = ['Error', 'Count']

        list_to_write = create_error_messages_list()

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for element in list_to_write:
            error, count = element
            writer.writerow({'Error': error, 'Count': count})

if __name__ == "__main__":
    # The main execution starts here.
    log_file = sys.argv[1]
    error_search(log_file)
    info_search(log_file)
    
    # Uncomment the following lines to print the final dictionaries before creating CSV files.
    # print('Final error dict: ' + str(count_occurrences_per_user(error_dict)))
    # print('Final info dict: ' + str(count_occurrences_per_user(info_dict)))
    
    create_csv_user_stats()
    create_error_messages_list()
    create_csv_error_stats()

    sys.exit(0)
