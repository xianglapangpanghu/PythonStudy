import requests
from bs4 import BeautifulSoup
import bs4
import re

info = []
infoc = []
infolist = [['href="/rhdm/9014/"', 'target="_blank"', 'title="ロマンスは剣の輝きII"'], ['href="/rhdm/3520/"', 'target="_blank"', 'title="螢子"'], ['href="/rhdm/8927/"', 'target="_blank"', 'title="英才狂育"']]
headers ={
        'Host': 'm.emddm.org',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=171e8d23c6262-00cf49e5b942668-4c302e7f-1fa400-171e8d23c642f4; CNZZDATA1272947728=205531128-1588748759-%7C1590213234'
        }
#r = requests.get('https://m.emddm.org/search.php?searchtype=5&tid=&jq=%E6%97%A0%E4%BF%AE')
r2 = requests.get('https://m.emddm.org/rhdm/8927/play-0-0.html', headers = headers)
#r.encoding = r.apparent_encoding
r2.encoding = r2.apparent_encoding
#html = r.text
html2 = r2.text
soup = BeautifulSoup(html2)
a = soup.find_all('li')
var = re.findall('var now=\"(\\d+)"', html2)
print(var)
#print(soup.find_all('a'))
#https://271dm.applinzi.com/v.php?id=6132223838389730
#https://271dm.applinzi.com/v.php?id=6154723838495825