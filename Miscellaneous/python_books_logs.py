# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment:
# In this Bite you will make a small bar chart of the amount of books a Slack bot 
# sent every day in February.
# You need to count the sending to slack channel entries and look at the book 
# title in the previous line - and see if it was a Python book. If so print 🐍 , 
# else a dot (constants provided).



import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'  # Symbols for Python and other messages
MESSAGE = 'sending to slack channel'  # Message indicator

# Download the log file from the given URL
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS) as f:
        logs = f.readlines()

    date = None
    daily_messages = ""

    for index, line in enumerate(logs):
        current_date = line.split()[0]

        if date is None:
            date = current_date

        if date == current_date:
            if MESSAGE in line:  # Check if the line contains the message indicator
                if 'python' in logs[index - 1].lower():  # Check if the previous line contains 'python'
                    daily_messages += PY_BOOK  # Add Python symbol to the daily messages
                else:
                    daily_messages += OTHER_BOOK  # Add other symbol to the daily messages
        else:
            if daily_messages:
                print(f"{date} {daily_messages}")  # Print the date and daily messages

            date = current_date
            daily_messages = ""
            if MESSAGE in line:
                if 'python' in logs[index - 1].lower():
                    daily_messages += PY_BOOK
                else:
                    daily_messages += OTHER_BOOK

    if daily_messages:
        print(f"{date} {daily_messages}")  # Print the date and daily messages for the last iteration

create_chart()
