#!/usr/bin/env python3

# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment:
# Working with APIs is very common these days and lucky for us they increasingly 
# return JSON (over XML). We saved OMDb responses for some cool movies into a file 
# that the tests load in.
# Parse this data answering some questions.

import json
import requests

FILE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/omdb_data'

def get_the_file(url):
    """Download the file from the given URL and split it into lines"""
    file = requests.get(url)
    lines = file.text.splitlines()
    return lines


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    dict_list = []
    for i in range(len(files)):
        dict_list.append(json.loads(files[i]))
    return dict_list


def get_single_comedy(movies: list) -> str:
    """Return the movie with 'Comedy' in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominations_tuple_list = []

    for movie in movies:
        nominations_tuple_list.append((movie['Title'], (get_nominations(movie['Awards']))))

    sorted_list = sorted(nominations_tuple_list, key=lambda x: x[1], reverse=True)
    return sorted_list[0][0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtime_tuple_list = []
    for movie in movies:
        runtime_tuple_list.append((movie['Title'], (get_runtime(movie['Runtime']))))

    sorted_list = sorted(runtime_tuple_list, key=lambda x: x[1], reverse=True)
    return sorted_list[0][0]


def get_runtime(runtime):
    """Extract the number of minutes from the runtime string"""
    minutes = ''
    for c in runtime:
        if c.isdigit():
            minutes += c
    return int(minutes)


def get_nominations(nominations: str):
    """Extract the number of nominations from the nominations string"""
    nominations_count = ''
    index = nominations.lower().find('nominations')
    for c in nominations[index - 3:index]:
        if c.isdigit():
            nominations_count += c
    return int(nominations_count)


print(get_single_comedy(get_movie_data(get_the_file(FILE_URL))))
print(get_movie_most_nominations(get_movie_data(get_the_file(FILE_URL))))
print(get_movie_longest_runtime(get_movie_data(get_the_file(FILE_URL))))
