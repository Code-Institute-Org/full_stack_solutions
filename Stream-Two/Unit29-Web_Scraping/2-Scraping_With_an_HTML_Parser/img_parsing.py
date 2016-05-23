from bs4 import BeautifulSoup
from urllib2 import urlopen

my_address = "http://www.irishtimes.com/"
html_page = urlopen(my_address)
html_text = html_page.read()
soup = BeautifulSoup(html_text, "html.parser")

# Create a list to store our images in
images = []
# Store the images in the list
images = soup.find_all("img")

# Iterate over 'images' list and
# print the 'src' of each image
for img in images:
    print img['src']
