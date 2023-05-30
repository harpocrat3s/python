# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.
# In this Bite we use BeautifulSoup to scrape US holidays from OfficeHolidays 
# to make a lookup of holidays per month.


from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from datetime import datetime

# Set up the temporary directory path
tmp = os.getenv("TMP", "/tmp")

# Define the filename and full path for the holidays page
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)

# Download the holidays page using urlretrieve
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

# Read the contents of the holidays page into a variable
with open(holidays_page) as f:
    content = f.read()

# Create a defaultdict to store the bank holidays
holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    # Create a defaultdict to store the bank holidays
    holidays_dict = defaultdict(list)

    # Create a BeautifulSoup object to parse the HTML content
    content_soup = BeautifulSoup(content, 'html.parser')

    # Find the bank holiday table with the CSS class 'list-table'
    holidays_table = content_soup.find(class_='list-table')

    # Extract the rows of the table
    rows_list = holidays_table.select('tbody tr')

    # Iterate over each row and extract the full date and holiday name
    for row in rows_list:
        full_date = row.select('time[datetime]')[0].text
        month = datetime.strptime(full_date, '%Y-%m-%d')
        holiday = row.select('a[title]')[0].text

        # Add the holiday to the corresponding month in the defaultdict
        holidays_dict[month.strftime('%m')].append(holiday.strip())

    # Return the populated holidays_dict
    return holidays_dict
