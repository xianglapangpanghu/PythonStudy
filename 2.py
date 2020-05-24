import requests
import re
from bs4 import BeautifulSoup
infolist = [['href="/rhdm/9014/"', 'target="_blank"', 'title="ロマンスは剣の輝きII"'], ['href="/rhdm/3520/"', 'target="_blank"', 'title="螢子"'], ['href="/rhdm/3482/"', 'target="_blank"', 'title="英才狂育"']]
    #寻找视频下载地址HTML
def getVideoHTML(url):    #获取视频下载地址HTML
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text        
    except:
        return 'error'
def parserHTML(html, downPage):   #解获取集数
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
def getDownID(html,downID):  
    try:
        var = re.findall('var now=\"(\\d+)"', html)
        downID.append(var)
    except:
        return ''

def saveVedio(downID, downPage, infolist):   
    try:
        src="https://271dm.applinzi.com/v.php?id="
        count = 0
        for i in range(len(infolist)):
            root = "E://downVedio//{}//".format(infolist[i][2][6:])
            for j in range(downPage[i]):
                count = count + 1
                url = src + downID[count-1][0]
                path = root + "第{}集.mp4".format(j+1)
                print(path)
                print(url)
        #if not os.path.exists(root):
        #    os.mkdir(root)
        #if not os.path.exists(path):
        #    r = requests.get(url, stream=True)
        #    r.raise_for_status()
        #    with open(path,'wb') as f:
        #        for i in r.iter_content(chunk_size=1024): 
        #            f.write(i)
        #            print("文件保存成功")
        #else:
        #    print("文件保存成功")
    except:
        print("保存失败")

downID = []     #下载ID
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

saveVedio(downID, downPage, infolist)



