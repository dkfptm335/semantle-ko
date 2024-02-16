import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = r'https://semantle-ko.newsjel.ly/nearest1k/'
response = requests.get(url)

#similarity-story