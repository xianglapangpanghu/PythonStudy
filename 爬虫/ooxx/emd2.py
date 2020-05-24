import emd as fd
import requests
import re
from bs4 import BeautifulSoup
import you_get
import time
import os

def getVideoHTML(url):    #获取第一集视频下载地址HTML
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text        
    except:
        return 'error'

def parserHTML(html, downPage):   #获取集数
    try:
        soup = BeautifulSoup(html, "html.parser")
        lis = soup.find_all('li')
        downPage.append(len(lis))
    except:
        return "error"

def rsUrl(start_url, downPage,downURL): #重构url
    try:
        for i in range(len(downPage)):
            for j in range(downPage[i]):
                b = start_url[i] + '0-{}.html'.format(j)
                downURL.append(b)
    except:
        return ''

def getDownID(html, downID):   #获取视频下载ID
    try:
        var = re.findall('var now=\"(\\d+)"', html)
        downID.append(var)
    except:
        return ''

def saveVedio(downID, downPage, infolist):
    try:
        count = 0
        src="https://271dm.applinzi.com/v.php?id="
        for i in range(len(infolist)):
            root = "E://downVedio//{}//".format(infolist[i][2][6:])
            for j in range(downPage[i]):
                count = count + 1
                url = src + downID[count-1][0]
                path = root + "第{}集.mp4".format(j+1)
                print(path)
                print(url)
    except:
        print("存储失败")

def main():
    infolist = fd.main() #满足条件的视频列表
    downID = []     #视频下载ID
    downPage = []   #视频集数
    start_url = []  #传入的URL
    downURL = []    #每一页视频所在url

    for i in range(len(infolist)):
        videoId = infolist[i][0][-6:-2]
        videoURL = 'https://m.emddm.org/rhdm/{}/play-0-0.html'.format(videoId)
        vedioHTML = getVideoHTML(videoURL)
        parserHTML(vedioHTML, downPage)

    for i in range(len(infolist)):
        a = 'https://m.emddm.org/rhdm/{}/play-'.format(infolist[i][0][-6:-2])
        start_url.append(a)

    rsUrl(start_url, downPage,downURL)

    for i in range(len(downURL)):
        downHTML = getVideoHTML(downURL[i])
        getDownID(downHTML, downID)
    #print(infolist)
    #print(downPage)
    #print(downURL)
    #print(downID)
    saveVedio(downID, downPage, infolist)
if __name__ == "__main__":
    main()