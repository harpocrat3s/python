# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.
# The assignment for this exercise was to parse Packt's free learning ebook site 
# (a cached copy) and extract the HTML for the daily free ebook.


from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

# URL of the cached copy of Packt's free learning ebook site
PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
# Retrieve the HTML content of the page
CONTENT = requests.get(PACKT).text

# Define a named tuple to hold book information
Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    # Create a BeautifulSoup object to parse the HTML content
    soup = Soup(CONTENT, 'html.parser')

    # Find the relevant HTML sections for the daily free ebook
    dotd_div = soup.find('div', id='deal-of-the-day')
    dotd_summary_div = dotd_div.find('div', class_='dotd-main-book-summary float-left')
    divs_inside_summary = dotd_summary_div.find_all('div')

    # Extract the title, description, image source, and link for the ebook
    title = dotd_div.find('div', class_='dotd-title').text.strip()
    description = divs_inside_summary[2].text.strip()
    image = dotd_div.find('img')['src']
    link = dotd_div.find('a')['href']

    # Create a Book namedtuple with the extracted information
    book_tuple = Book(title=title, description=description, image=image, link=link)

    return book_tuple
