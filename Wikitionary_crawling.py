import requests
from bs4 import BeautifulSoup

url = r'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

word = soup.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > table > tbody > tr > td:nth-child(1) > dl > dd > span > a')
print(word)