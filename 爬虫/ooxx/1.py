import numpy as np
from tqdm import tqdm
import requests
import os
import time

f = np.load(r'爬虫\ooxx\infolist.npy', allow_pickle=True)
infolist = f.tolist()
f = np.load(r'爬虫\ooxx\downID.npy', allow_pickle=True)
downID = f.tolist()
f = np.load(r'爬虫\ooxx\downPage.npy', allow_pickle=True)
downPage = f.tolist()
#print(infolist)
#print(downID)
#print(downPage)

def saveVedio(downID, downPage, infolist):      #下载并存储视频
    count = 0
    src="https://271dm.applinzi.com/v.php?id="
    for i in range(len(infolist)):
        root = "E://DownVedio//{}//".format(infolist[i][2][7:-1])
        for j in range(int(downPage[i])):
            count = count + 1
            url = src + downID[count-1][0]
            path = root + "第{}集.mp4".format(j+1)
            print(url)
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


saveVedio(downID, downPage, infolist)
count = 0
