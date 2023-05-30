# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# I placed this exercise in the cybersecurity section of my GitHub because I 
# believe it forms the foundation for more complex scripts used in a SOC analyst 
# role. For instance, it can be handy when investigating a phishing email.

# The PyBites assignment was:
# Write a regular expression to extract four pieces of information from an email header:
# - From email
# - To email
# - Subject
# - Date sent (without timezone info)
# Use re.match or re.search with capturing parentheses. Return the captured groupdict 
# of the match object.


import re
from typing import Dict, Optional

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501


def get_email_details(header: str) -> Optional[Dict[str, str]]:
    """User re.search or re.match to capture the from, to, subject
       and date fields. Return the groupdict() of matching object, see:
       https://docs.python.org/3.7/library/re.html#re.Match.groupdict
       If not match, return None
    """
    result = {'from': None, 'to': None, 'subject': None, 'date': None}

    # Define patterns for capturing specific fields
    patterns = {
        "from": r"^From: (?P<from>[.@ &()\w-]+)",
        "to": r"^To: (?P<to>[.@\w-]+)",
        "subject": r"^Subject: (?P<subject>.+)",
        "date": r"^Date: (?P<date>\w{3}, \d+ \w{3} \d{4} \d+:\d+:\d+)",
    }

    # Iterate through each line in the header
    for line in header.splitlines():
        # Check if the line matches any of the patterns
        for key, pattern in patterns.items():
            if re.match(pattern, line):
                # If there is a match, capture the corresponding value and store it in the result dictionary
                result[key] = re.match(pattern, line)[1]

    # Check if all values in the result dictionary are None
    if all(value is None for value in result.values()):
        return None
    else:
        return result
