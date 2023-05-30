# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.
# In this bite I had to find out which books get recommended the most on a Tim Ferris
# top books page.


from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()

    cnt = Counter()
    page = BeautifulSoup(content, 'html.parser')

    entry = page.find(class_='entry-content')
    links = page.select('a')

    for link in links:
        # Check if the link contains AMAZON
        if AMAZON in link['href']:
            # Increment the count of the book title
            cnt[link.text.strip()] += 1

    # Filter the items based on the minimum count
    filtered_items = [(book, count) for book, count in cnt.items() if count >= MIN_COUNT]

    # Sort the filtered items based on the count in descending order
    sorted_items = sorted(filtered_items, key=lambda x: x[1], reverse=True)

    return sorted_items
