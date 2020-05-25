import requests
import re
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

infolist = [['href="/rhdm/9014/"', 'target="_blank"', 'title="ロマンスは剣の輝きII"'], ['href="/rhdm/3520/"', 'target="_blank"', 'title="螢子"']]
def getVideoHTML(url):    #获取视频下载地址HTML
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text        
    except:
        return 'error'
def parserHTML(html, downPage):   #解获取【集数】
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
def getDownID(html,downID):  #获取【每集ID】
    try:
        var = re.findall('var now=\"(\\d+)"', html)
        downID.append(var)
    except:
        return ''

def saveVedio(downID, downPage, infolist):   #存储视频
    try:
        src="https://271dm.applinzi.com/v.php?id="
        count = 0
        for i in range(len(infolist)):
            root = "E://DownVedio//{}//".format(infolist[i][2][7:-1])
            for j in range(downPage[i]):
                count = count + 1
                url = src + downID[count-1][0]
                path = root + "第{}集.mp4".format(j+1)
                if not os.path.exists(root):
                   os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url, stream=True)
                    r.raise_for_status()
                    size = int(r.headers['Content-Length'])/1024
                    with open(path,'wb') as f:
                       print("下载文件大小是：", size,"KB,开始下载——————————》》》")
                       for i in tqdm(iterable=r.iter_content(chunk_size=1024), total=size, unit='KB', desc=path): 
                           f.write(i)
                    print("下载完毕")
                else:
                   print("文件已存在")
    except:
        print("保存失败")

downID = []     #下载ID
downPage = []   #视频集数
start_url = []  #传入的URL
downURL = []    #每一页视频所在url

for i in range(len(infolist)):      #传入视频第一页url，并获取html，寻找每部视频的集数
    videoId = infolist[i][0][-6:-2]
    videoURL = 'https://m.emddm.org/rhdm/{}/play-0-0.html'.format(videoId)
    vedioHTML = getVideoHTML(videoURL)
    parserHTML(vedioHTML, downPage)

for i in range(len(infolist)):
    a = 'https://m.emddm.org/rhdm/{}/play-'.format(infolist[i][0][-6:-2])
    start_url.append(a)

rsUrl(start_url, downPage,downURL)      #重构【每一部视频】的【每一集url】

for i in range(len(downURL)):           #获取每集的【下载ID】
    downHTML = getVideoHTML(downURL[i])
    getDownID(downHTML, downID)

saveVedio(downID, downPage, infolist)



