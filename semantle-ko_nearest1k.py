import requests
from bs4 import BeautifulSoup
from datetime import datetime
import datetime as dt
import re
import pandas as pd

org_url = r'https://semantle-ko.newsjel.ly/'
response = requests.get(org_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2022년 4월 2일이 1번째 날, 현재 날짜를 받아와서 몇 번째 날인지 계산
today = datetime.today()
today = today.strftime('%Y-%m-%d')
today = datetime.strptime(today, '%Y-%m-%d')
start_day = datetime(2022, 4, 2)
day_diff = today - start_day + dt.timedelta(days=1)
day_diff = day_diff.days

target_url = org_url + f'nearest1k/{day_diff}'
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

word_list = list(soup.text.strip().split('\n'))

for i in range(len(word_list)):
    word_list[i] = re.sub(r'[^가-힣]', '', word_list[i])

while '' in word_list:
    word_list.remove('')
    
for _ in range(2):
    del word_list[0]
    
word_list[0] = word_list[0][7:]
word_list[0] = word_list[0][:len(word_list[0])-18]

for _ in range(3):
    del word_list[1]

del word_list[-1]
    
print(len(word_list))

# save to csv
df = pd.DataFrame(word_list, columns=['word'])
today = datetime.today().strftime('%Y-%m-%d')

print("==================== Save to csv ====================")
df.to_csv(f'nearest1k_{today}.csv', index=False, encoding='utf-8-sig', sep='|', header=False)
print("===================== Completed =====================")
