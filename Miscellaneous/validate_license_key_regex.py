# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment:
# Complete the validate_license function writing a regular expression that matches 
# a PyBites license key which:

# - Starts with PB
# - following 4 times dash (-) and 8 chars which can be upper case chars or digits,
# - for example: PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4 would be a valid license key.

# Return a bool

import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    return bool(re.search(r"^PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$", key))
