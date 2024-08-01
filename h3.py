import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


h3_elements = soup.find_all('h3')


for h3 in h3_elements:
    print(h3.text.strip())
