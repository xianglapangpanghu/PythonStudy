import requests
from bs4 import BeautifulSoup
import bs4
import re

info = []
infoc = []
r = requests.get('https://m.emddm.org/search.php?searchtype=5&tid=&jq=%E6%97%A0%E4%BF%AE')
r2 = requests.get('https://m.emddm.org/rhdm/8971/play-0-0.html')
r.encoding = r.apparent_encoding
r2.encoding = r2.apparent_encoding
html = r.text
html2 = r2.text
start = re.findall('href=\"/rhdm/\\d{4}/\" target=\"_blank\" title=\".+\"', html)
#start2 = re.findall('var now=\"\\d+\"', html2)

for i in range(len(start)):
    a = start[i].split(' ')
    info.append(a)
print(info[0][0][-6:-2])
#print(soup.find_all('a'))
#https://271dm.applinzi.com/v.php?id=6132223838389730
#https://271dm.applinzi.com/v.php?id=6154723838495825