#!/usr/bin/env python3.8

import sys
import os
import re
import csv
import operator

info_dict = {}
error_dict = {}
error_list = []

def error_search(log_file):
    #This populates error_dict with a list of error messages associated to each username
    error = 'ticky: ERROR:'


    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(r"ticky: ERROR ([\w ']*) \(([\w.]*)\)$", log)
            #result[0] = tutto il log da ticky: in poi
            #result[1] = error message
            #result[2] = username
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
    info = 'ticky: INFO:'

    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(r"ticky: INFO ([\w ]*) \[#\d*\] \(([\w.]*)\)$", log)
            #result[0] = tutto il log da ticky: in poi
            #result[1] = error message
            #result[2] = username
            if result is not None:
                if result[2] in info_dict:
                    temp_list = info_dict[result[2]]
                    temp_list.append(result[1])
                    info_dict[result[2]] = temp_list
                else:
                    info_dict[result[2]] = [result[1]]
    file.close()

def create_error_messages_list():
    final_unsorted_dict = {}

    for element in error_list:
        final_unsorted_dict[element] = error_list.count(element)

    return sorted(final_unsorted_dict.items(), key=operator.itemgetter(1), reverse=True)


def count_occurrences_per_user(to_count_dict):
    final_dict = {}
    for key in to_count_dict:
        final_dict[key] = len(to_count_dict[key])
    return final_dict

def create_csv_user_stats():
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
                dict_to_write[key] =(0, error_sum[key])

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for key in dict_to_write:
            info, error = dict_to_write[key]
            writer.writerow({'Username': key, 'INFO': info, 'ERROR': error})

def create_csv_user_stats():
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
                dict_to_write[key] =(0, error_sum[key])

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        dict_tuples = dict_to_write.items()
        sorted_items = sorted(dict_tuples)



        for key in sorted_items:
            username, infoerror = key
            writer.writerow({'Username': username, 'INFO': infoerror[0], 'ERROR': infoerror[1]})
               


def create_csv_error_stats():
    with open('error_message.csv', mode='w') as csv_file:
        fieldnames = ['Error', 'Count']

        list_to_write = create_error_messages_list()

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for element in list_to_write:
            error, count = element
            writer.writerow({'Error': error, 'Count': count})

if __name__ == "__main__":
    log_file = sys.argv[1]
    error_search(log_file)
    info_search(log_file)
    #print('Final error dict: ' + str(count_occurrences_per_user(error_dict)))
    #print('Final info dict: ' + str(count_occurrences_per_user(info_dict)))
    create_csv_user_stats()
    create_error_messages_list()
    create_csv_error_stats()

    sys.exit(0)