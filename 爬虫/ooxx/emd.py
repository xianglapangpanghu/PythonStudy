import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import re
import time
import numpy as np

'''
直接看下一个文件》》
'''

def getFirstHTML(url, page): #获取无修列表html代码
    try:
        url = url + '&jq=无修'
        r = requests.get(url)
        r.raise_for_status
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'error' + str(page)

def getSecondHTML(url, page): #获取里番列表html代码
    try:
        url = url + '&jq=里番'
        r = requests.get(url)
        r.raise_for_status
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'error' + str(page)

def parseHTML(list, html, page):    #处理html
    try:
        parse = re.findall('href=\"/rhdm/\\d{4}/\" target=\"_blank\" title=\".+\"', html)
        for i in range(len(parse)):
            a = parse[i].split(' ')
            list.append(a)

    except:
        return '{}页处理出错'.format(page)
def printVideo(WXlist, LFlist, infolist, page):   #输出符合条件的视频
    try:
        lists = []
        for i in range(len(WXlist)):
            for j in range(len(LFlist)):
                if WXlist[i] == LFlist[j]:
                    lists.append(WXlist[i])
        for i in lists:
            if i not in infolist:
                infolist.append(i)              
    except:
        return '{}合并错误'.format(page)

def getVideoHTML(url):    #获取频页面HTML
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text        
    except:
        return 'error'

def get():
    infolist = []   #相同列表
    WXlist = [] #无修列表
    LFlist = [] #里番列表
    star_url = 'https://m.emddm.org/search.php?&searchtype=5'
    for page in range(4,8):
        url = star_url + '&page=' + str(page)
        WXhtml = getFirstHTML(url,page)
        LFhtml = getSecondHTML(url,page)
        parseHTML(WXlist, WXhtml, page)
        parseHTML(LFlist, LFhtml, page)
        printVideo(WXlist, LFlist, infolist, page)
        print(infolist)

    m = np.array(infolist)
    np.save(r'爬虫\ooxx\infolist.npy',m)

if __name__ == "__main__":
    get()