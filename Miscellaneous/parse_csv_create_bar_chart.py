# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment:
# We put some anonymized data in a csv (using uuid4 and faker) and for this Bite 
# we ask you to use requests to load it in, use the csv module to parse it into 
# a data structure of your choice, and finally print the output to the screen in
# a specified format.


import csv
from collections import defaultdict
import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    res = requests.get(CSV_URL)
    csv_file = res.text.splitlines()
    csv_reader = csv.DictReader(csv_file)
    csv_data = list(csv_reader)
    return csv_data


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    tz_dict = defaultdict(str)
    for row in content:
        tz_dict[row['tz']]+='+'
    longest_string = len(max(tz_dict.keys(), key=len))
    for key, pluses in sorted(tz_dict.items()):
        key_justified = key.ljust(longest_string + 1)
        print(f'{key_justified}| {pluses}')

