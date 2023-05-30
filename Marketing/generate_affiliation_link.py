# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment:
# Can you help PyBites automate their Amazon affiliation link creation?
# Complete the generate_affiliation_link(url) function below which should convert 
# [a list of] links into affiliation links.

# I was not supposed to use Regex for this.


def generate_affiliation_link(url):
    """
    Generates an Amazon affiliate link from a product URL.

    Args:
    url (str): The product URL to generate a link for.

    Returns:
    str: The affiliate link with the Amazon URL, product ID, and affiliate tag.
    """

    # Check if URL is a valid Amazon URL
    if "amazon." not in url:
        return "Invalid Amazon URL"

    # Extract product ID from URL
    id_start = url.find("/dp/") + 4
    id_end = url.find("/", id_start)
    product_id = url[id_start:id_end]

    # Check if product ID is a valid ASIN code
    if len(product_id) != 10 or not product_id.isalnum():
        return "Invalid product ID"

    # Generate affiliate link with Amazon URL and affiliate tag
    amazon_url = "https://www.amazon.com/dp/" + product_id
    affiliate_tag = "?tag=affiliate-tag"
    affiliate_link = amazon_url + affiliate_tag

    return affiliate_link


original_links = [
    "https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/",
    "https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1",
    "https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234",
    "https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X",
    "https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/",
    "https://www.amazon.com/fake-book-with-longer-asin/dp/1449340377000/",
]

for link in original_links:
    print(generate_affiliation_link(link))
