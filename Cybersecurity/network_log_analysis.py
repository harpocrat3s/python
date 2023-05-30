"""
Exercise: Network Logs Analysis

You are a cybersecurity analyst and your task is to analyze network logs to identify potentially malicious activities.

You have been provided a simple log file (in the form of a text file) that contains network traffic records. 
Each record in the log file is a single line containing the following information:

    IP Address
    Timestamp
    Request Method (GET/POST)
    Request URL
    Response Status Code

Each field is separated by a comma.

For instance, a line in the log file might look like this:

192.168.1.1,2023-05-17 13:45:23,GET,/index.html,200

Your task is to write a Python script to:

- Read and parse the log file.
- Identify any IP addresses that have made more than 100 requests within a single hour.
- For each such IP address, count the number of each type of response status code received.

The output of your script should be a dictionary with the IP addresses as keys. 
The values should be another dictionary with the status codes as keys and their respective counts 
as values.

For instance, an example output might look like this:

json

{
    "192.168.1.1": {
        "200": 85,
        "404": 10,
        "500": 6
    },
    "192.168.1.2": {
        "200": 70,
        "404": 15,
        "500": 16
    }
}


Remember to test your script with various inputs to ensure that it handles all possible cases.

""" 

from collections import defaultdict
from datetime import datetime, timedelta

# 1. Read the Log File
with open('log.txt', 'r') as f:
    log_lines = f.readlines()

# Initialize a dictionary to hold the timestamps of requests for each IP
ip_timestamps = defaultdict(list)

# Initialize a dictionary to hold the counts of status codes for each IP
ip_status_counts = defaultdict(lambda: defaultdict(int))

# 2. Parse the Log Records
for line in log_lines:
    ip, timestamp_str, method, url, status_code = line.strip().split(',')
    
    # Convert the timestamp string to a datetime object
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    # Add the timestamp to the list of timestamps for this IP
    ip_timestamps[ip].append(timestamp)

    # 3. Check if the IP has made more than 100 requests within the last hour
    # Remove any timestamps that are more than an hour before the current timestamp
    ip_timestamps[ip] = [t for t in ip_timestamps[ip] if timestamp - t < timedelta(hours=1)]
    
    if len(ip_timestamps[ip]) > 100:
        # If the IP has made more than 100 requests within the last hour,
        # count the status code for the current request
        ip_status_counts[ip][status_code] += 1

# 5. Generate the Output
output = {ip: dict(status_counts) for ip, status_counts in ip_status_counts.items() if len(ip_timestamps[ip]) > 100}

print(output)


"""
This script works by first reading the log file line by line and parsing each line into its constituent parts. 
It then adds the timestamp of each request to a list of timestamps for the IP address that made the request. 
It also removes any timestamps that are more than an hour older than the current timestamp. If the IP address has 
made more than 100 requests within the last hour, it counts the status code of the current request.

Finally, it generates the output dictionary, which contains the counts of each status code for each IP address 
that made more than 100 requests within an hour.

"""