import requests
import re
infolist = [['href="/rhdm/9014/"', 'target="_blank"', 'title="ロマンスは剣の輝きII"'], ['href="/rhdm/3520/"', 'target="_blank"', 'title="螢子"'], ['href="/rhdm/3482/"', 'target="_blank"', 'title="英才狂育"']]
    #寻找视频下载地址HTML
def getVideoHTML(url):    #寻找视频下载地址HTML
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(url)
        return r.text        
    except:
        return 'error'
for i in range(len(infolist)):
    videoId = infolist[i][0][-6:-2]
    videoURL = 'https://m.emddm.org/rhdm/{}/play-0-0.html'.format(videoId)
    vedioHTML = getVideoHTML(videoURL)

