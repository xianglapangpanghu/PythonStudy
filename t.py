import requests
import re
from bs4 import BeautifulSoup
downPage = ['6', '3', '1', '1']
#r = requests.get('https://m.emddm.org/rhdm/7907/play-0-0.html')
#r.encoding = 'charset=utf-8'
#page = re.findall('/rhdm/\\d{4}/play-0-(\\d+).html', r.text)
#page = int(max(page)) +1
#downPage.append(str(page))
for i in range(4,6):
    print(i)