#!/usr/bin/env python3

# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.
# In this exercise, the goal was to query the ipinfo API to retrieve the country code
# for a given IP address.
# I placed it in the Cybersecurity section of my GitHub because I anticipate building 
# more robust scripts in the future that will need to handle IP addresses and check
# their details, such as country codes, during the analysis of attacks, for example.


import requests
import json

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""

    ipinfourl = IPINFO_URL.format(ip=ip_address)
    json_data = requests.get(ipinfourl).json()

    return json_data['country']


if __name__ == '__main__':
    # This allows the script to be run from the command line with an argument
    import sys
    print(get_ip_country(str(sys.argv[1])))
