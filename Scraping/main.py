from bs4 import BeautifulSoup
import requests

url = "https://www.yelp.com/"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
print(soup.prettify())

