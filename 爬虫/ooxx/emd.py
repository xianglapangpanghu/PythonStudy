import requests
from bs4 import BeautifulSoup
import re

def getFirstHTML(url, page): #获取无修列表html代码
    try:
        url = url + '&jq=无修'
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error' + str(page)

def getSecondHTML(url, page): #获取里番列表html代码
    try:
        url = url + '&jq=里番'
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
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
        for i in range(len(WXlist)):
            for j in range(len(LFlist)):
                if WXlist[i] == LFlist[j]:
                    infolist.append(WXlist[i])              
        print(infolist)
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

def parseVedioHTML(): #
    try:

    except:
def saveVideo():    #下载并保存视频
    pass
def main():
    infolist = []   #相同列表
    WXlist = [] #无修列表
    LFlist = [] #里番列表
    star_url = 'https://m.emddm.org/search.php?&searchtype=5'
    for page in range(1,4):
        url = star_url + '&page=' + str(page)
        WXhtml = getFirstHTML(url,page)
        LFhtml = getSecondHTML(url,page)
        parseHTML(WXlist, WXhtml, page)
        parseHTML(LFlist, LFhtml, page)
    printVideo(WXlist, LFlist, infolist, page)    
    

if __name__ == "__main__":
    main()