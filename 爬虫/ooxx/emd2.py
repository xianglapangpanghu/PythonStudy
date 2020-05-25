import emd as fd
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import you_get
import time
import os
import numpy as np

'''
前言（碎碎念）：
    上面的模块别忘了加载，基本可以用pip安装，有什么问题百度都能解决
    save部分如果有需要可以改成自己想要的地址
    （重要）这网站没有反爬虫，看了下网站文件，还有好多没启用的模块，估计用的模板做的，哥几个下手轻点time代码别删，让网站休息会
    还有感觉自己写的代码好丑（-o-）
    最后大家要注意身体哦OWO
已知问题：（基本是我能力不够，还在学习中QAQ）
    1.不支持断点下载
    2.不支持多线程
    3.部分视频存在音画不同步，个别视频（少数）尤其严重（网站视频本身问题，会PR和AE应该能解决）
    4.有些远古视频网站缺失视频我也米办法
    5.对于34的问题换个网站能解决，但是我不会处理Ajax异步加载，scrapy和xpath也还没学会
'''

def getVideoHTML(url):    #获取视频下载地址HTML
    try:
        r = requests.get(url, timeout = 6)
        r.raise_for_status()
        r.encoding = 'charset=utf-8'
        return r.text        
    except:
        return 'error'

def parserHTML(html, downPage):   #获取【集数】
    try:
        page = re.findall('/rhdm/\\d{4}/play-0-(\\d+).html', html)
        page = int(max(page)) +1
        downPage.append(str(page))
    except:
        return "error"

def rsUrl(start_url, downPage,downURL): #重构url
    try:
        #print(start_url)
        #print(downPage)
        for i in range(len(downPage)):
            for j in range(int(downPage[i])):
                next_url = start_url[i] + '0-{}.html'.format(j)
                downURL.append(next_url)
    except:
        return ''

def getDownID(html, downID):   #获取【每集ID】
    try:
        var = re.findall('var now=\"(\\d+)"', html)
        downID.append(var)
    except:
        return ''

def saveVedio(downID, downPage, infolist):      #下载并存储视频
    try:
        count = 0
        src="https://271dm.applinzi.com/v.php?id="
        for i in range(len(infolist)):
            root = "E://DownVedio//{}//".format(infolist[i][2][7:-1])
            for j in range(int(downPage[i])):
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
                       print("下载文件大小是：", size,"KB,开始下载》》》》》》》》")
                       for i in tqdm(iterable=r.iter_content(chunk_size=1024), total=size, unit='KB', desc=path): 
                           f.write(i)
                    print("视频下载完毕")
                    time.sleep(5)   #下载完一个视频休息一会
                else:
                   print("视频已存在")
    except:
        print("存储失败")

def main():
    a = np.load('爬虫\\ooxx\\infolist.npy', allow_pickle=True)
    infolist = a.tolist() #满足条件的视频列表
    downID = []     #视频下载ID
    downPage = []   #视频集数
    start_url = []  #传入的URL
    downURL = []    #每一页视频所在url      
    count = 0
    print("成功找到以下符合条件的番剧：")
    for i in range(len(infolist)):      #传入视频第一集url，并获取html，寻找每部视频的集数
        videoId = infolist[i][0][-6:-2]
        videoURL = 'https://m.emddm.org/rhdm/{}/play-0-0.html'.format(videoId)
        vedioHTML = getVideoHTML(videoURL)
        parserHTML(vedioHTML, downPage)
        count = count + 1
        print(count,":",infolist[i][2][7:-1])     #输出番剧名称
        time.sleep(0.5)

    for i in range(len(infolist)):      
        a = 'https://m.emddm.org/rhdm/{}/play-'.format(infolist[i][0][-6:-2])
        start_url.append(a)
    #print(start_url)
    rsUrl(start_url, downPage,downURL)  #重构【每一部视频】的【每集url】

    count = 0
    for i in range(len(downURL)):       #获取【每集】的【下载ID】
        downHTML = getVideoHTML(downURL[i])
        getDownID(downHTML, downID)
        count = count + 1
        for j in tqdm(iterable = range(count), total=len(downURL)):
            pass
    print(downID)
    m = np.array(downID)
    np.save(r'爬虫\ooxx\downID.npy',m)

    m = np.array(downPage)
    np.save(r'爬虫\ooxx\downPage.npy',m)
    saveVedio(downID, downPage, infolist)   #下载存储视频


if __name__ == "__main__":
    main()