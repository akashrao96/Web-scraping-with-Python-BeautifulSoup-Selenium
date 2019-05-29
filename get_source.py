# Get the source code of any website
import requests
from bs4 import BeautifulSoup
url='http://www.google.com'
# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')
# Printing Source Code
print(soup)
