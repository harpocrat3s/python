# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment:
# In this Bite we will look at this short server log, finding the first and last 
# system shutdown events:

# You'll need to calculate the time between these two events. First extract the 
# timestamps from the log entries and convert them to datetime objects. Then use 
# datetime.timedelta to calculate the time difference between them.
# You can assume the log is sorted in ascending order. 


from datetime import datetime
from datetime import timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    """Extract the timestamp from a logline and convert it to a datetime object.
    Args:
        line (str): Logline containing a timestamp in the format 'INFO YYYY-MM-DDTHH:MM:SS'.

    Returns:
        datetime: Converted datetime object representing the timestamp.
    """
    timestamp = line.split()[1]
    date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
    return date


def time_between_shutdowns(loglines):
    """Calculate the timedelta between the first and last shutdown events in the loglines.
    Args:
        loglines (list): List of loglines.

    Returns:
        timedelta: Timedelta object representing the time between the first and last shutdown events.
    """
    begin_date = None
    end_date = None

    for line in loglines:
        if 'Shutdown initiated' in line and begin_date is None:
            begin_date = datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')

        elif 'Shutdown complete' in line:
            end_date = datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')

    timedelta = end_date - begin_date
    return timedelta
