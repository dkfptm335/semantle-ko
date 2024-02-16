import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# word_list 불러온 후 배열로 만들기
words = pd.read_csv('Korean_5800.csv', sep='|', header=None)
words = words.values
words = [words[i][0] for i in range(len(words))]
count = 0

for word in words:
    url = r'https://semantle-ko.newsjel.ly/guess/685/' + word
    response = requests.get(url)
    score = response.text.split(':')[-1].split('}')[0]
    if score != 'unknown':
        score = 0.0
    else:   
        score = float(score)
        
    count += 1
    print(f'{count}/{len(words)}')
    
    if score > 0.4:
        print(word, score)
        break