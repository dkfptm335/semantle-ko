import requests
from bs4 import BeautifulSoup
import pandas as pd

url = r'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

words = []

for i in range(1, 7):
    words.append(soup.select(f'#mw-content-text > div.mw-content-ltr.mw-parser-output > table > tbody > tr > td:nth-child({i}) > dl > dd > span > a'))

# words = [[words_first], [words_second], [words_third], [words_fourth], [words_fifth], [words_sixth]]

words_list = []
for words_column in words:
    for word in words_column:
        if len(word.text) > 1:
            words_list.append(word.text)

# save to csv
df = pd.DataFrame(words_list, columns=['word'])

print("==================== Save to csv ====================")
df.to_csv('Korean_5800.csv', index=False, encoding='utf-8-sig', sep='|', header=False)
print("===================== Completed =====================")